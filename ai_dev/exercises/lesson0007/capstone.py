"""capstone.py — the whole spine in one run: index → recall → rerank → generate → evaluate.

Every lesson wired together:
  - chunking + embedding            (lessons 1-2)
  - dense + BM25 + RRF recall       (lesson 3)
  - cross-encoder rerank            (lesson 6)
  - generation with citations       (this lesson)
  - recall@k + faithfulness         (lessons 2, 5)

Run:  uv run capstone.py            # full report with canned answers (offline)
      uv run capstone.py --live     # regenerate answers + decompose claims with an LLM
"""
import argparse
import json
import math
import os
import re

import numpy as np
from sentence_transformers import SentenceTransformer, CrossEncoder

CORPUS = "corpus.md"
EMBED_MODEL = "all-MiniLM-L6-v2"
RERANKER = "cross-encoder/ms-marco-MiniLM-L6-v2"
NLI_MODEL = "cross-encoder/nli-MiniLM2-L6-H768"
NLI_LABELS = ["contradiction", "entailment", "neutral"]

STOP = set("""a an and are as at be but by for from in is it of on or so that the
to was what when where which who will with do does did his her its their
""".split())


def stem(w):
    if len(w) <= 4:
        return w
    if w.endswith("ies"):
        return w[:-3] + "y"
    if w.endswith("es"):
        return w[:-2]
    if w.endswith("s"):
        return w[:-1]
    if w.endswith("ing") and len(w) > 5:
        return w[:-3]
    if w.endswith("ed") and len(w) > 5:
        return w[:-2]
    return w


def tokenize(text):
    return [stem(t) for t in re.findall(r"[a-z']+", text.lower()) if t not in STOP]


def chunk_by_paragraph(text):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return [(f"p{i}", p) for i, p in enumerate(paras)]


def bm25_okapi(docs, k1=1.5, b=0.75):
    toks = [tokenize(d) for d in docs]
    N = len(docs)
    avgdl = sum(len(t) for t in toks) / N
    df = {}
    for t in toks:
        for w in set(t):
            df[w] = df.get(w, 0) + 1
    idf = {w: math.log((N - n + 0.5) / (n + 0.5) + 1) for w, n in df.items()}

    def score(query):
        q = tokenize(query)
        out = {}
        for i, t in enumerate(toks):
            dl = len(t)
            tf = {w: t.count(w) for w in set(t)}
            s = 0.0
            for w in q:
                if w not in idf:
                    continue
                f = tf.get(w, 0)
                if f:
                    s += idf[w] * (f * (k1 + 1)) / (f + k1 * (1 - b + b * dl / avgdl))
            if s:
                out[i] = s
        return out
    return score


def embed(model, texts):
    vecs = model.encode(texts)
    return vecs / np.linalg.norm(vecs, axis=1, keepdims=True)


def rrf(lists, k=60):
    out = {}
    for ranked in lists:
        for rank, doc_id in enumerate(ranked, start=1):
            out[doc_id] = out.get(doc_id, 0.0) + 1.0 / (k + rank)
    return out


# Each question names the exact sentence that must be retrieved, a canned answer
# with inline citations, and the answer's atomic claims for the faithfulness check.
GOLD = [
    ("How does the tutor avoid teaching wrong facts?",
     "The tutor answers only from the course material, never from general knowledge",
     "The tutor answers only from the course material, never from general knowledge, so wrong facts cannot reach a learner [p3].",
     ["The tutor answers only from the course material, never from general knowledge."]),
    ("When will a word be reviewed next?",
     "The scheduler computes the next review date",
     "The scheduler computes the next review date from the learner's performance on each flashcard [p6].",
     ["The scheduler computes the next review date from the learner's performance on each flashcard."]),
    ("What does the tutor do when it cannot find an answer?",
     "the tutor says it does not know rather than guessing",
     "When no chunk is close enough, the tutor says it does not know rather than guessing [p9].",
     ["When no chunk is close enough, the tutor says it does not know rather than guessing."]),
    ("How is a learner's question answered from the course chunks?",
     "The retrieval step embeds the learner's question and searches the lesson chunks",
     "The retrieval step embeds the learner's question and searches the lesson chunks for the closest match [p8].",
     ["The retrieval step embeds the learner's question and searches the lesson chunks for the closest match."]),
    ("Which engine suggests the next lesson?",
     "suggests new lessons based on recently missed words",
     "The Lingua recommendation engine suggests new lessons based on recently missed words [p22].",
     ["The Lingua recommendation engine suggests new lessons based on recently missed words."]),
    ("What method keeps long-term recall sharp?",
     "Spaced repetition schedules the review of each word at growing intervals",
     "Spaced repetition schedules the review of each word at growing intervals [p5]. The intervals are fixed at one day, three days, and one week [p5].",
     ["Spaced repetition schedules the review of each word at growing intervals.",
      "The review intervals are fixed at one day, three days, and one week."]),
]


def gold_ids(chunks, sentence):
    return [cid for cid, text in chunks if sentence in text]


GEN_PROMPT = (
    "You answer questions using ONLY the retrieved chunks below. Each chunk is "
    "labelled with its id. Answer in one or two sentences and cite every claim "
    "with the id of the chunk that supports it, like [p3]. If no chunk supports "
    "the answer, say you do not know.\n\n"
    "Chunks:\n{chunks}\n\nQuestion: {question}"
)

DECOMPOSE_PROMPT = (
    "Break the following answer into a list of atomic claims. Each claim must be "
    "a single verifiable statement with no conjunctions. Return JSON only:\n"
    '  {{"claims": ["claim one", "claim two"]}}\n'
    "Answer: {answer}"
)


def extract_citations(answer):
    return re.findall(r"\[(p\d+)\]", answer)


def check_claim(claim, top, nli, texts):
    """Which retrieved chunk (if any) entails the claim? NLI cross-encoders have
    short max sequence lengths, so a claim is checked against each chunk
    individually — not against the whole concatenated context."""
    best, best_chunk = "neutral", None
    for c in top:
        label = NLI_LABELS[int(nli.predict([(texts[c], claim)])[0].argmax())]
        if label == "entailment":
            return "entailment", c
        if label == "contradiction":
            best, best_chunk = "contradiction", c
    return best, best_chunk


def call_llm(prompt):
    from openai import OpenAI

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),
                    base_url=os.environ.get("OPENAI_BASE_URL"))
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    reply = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"} if "claims" in prompt else None,
    )
    return reply.choices[0].message.content


def main():
    parser = argparse.ArgumentParser(description="Full RAG pipeline with citations and evaluation.")
    parser.add_argument("--live", action="store_true",
                        help="regenerate answers and decompose claims with an LLM")
    args = parser.parse_args()
    k, pool = 3, 10

    embedder = SentenceTransformer(EMBED_MODEL)
    reranker = CrossEncoder(RERANKER)
    nli = CrossEncoder(NLI_MODEL)

    text = open(CORPUS, encoding="utf-8").read()
    chunks = chunk_by_paragraph(text)
    ids = [cid for cid, _ in chunks]
    texts = {cid: t for cid, t in chunks}
    vecs = embed(embedder, [t for _, t in chunks])
    bm25 = bm25_okapi([t for _, t in chunks])

    def fused_list(query):
        qv = embed(embedder, [query])[0]
        dense = [ids[i] for i in np.argsort(vecs @ qv)[::-1][:pool]]
        bm = [ids[i] for i, _ in sorted(bm25(query).items(), key=lambda kv: -kv[1])][:pool]
        return [i for i, _ in sorted(rrf([dense, bm], 60).items(), key=lambda kv: -kv[1])]

    def rerank(query):
        candidates = fused_list(query)[:pool]
        scores = reranker.predict([(query, texts[c]) for c in candidates])
        return [candidates[i] for i in np.argsort(scores)[::-1]]

    print(f"Lingua RAG — full pipeline  |  k={k}  |  pool={pool}  |  "
          f"answers: {'live LLM' if args.live else 'canned'}\n")

    recall_sum = 0.0
    faithful_sum = 0.0
    for q, gold_sentence, canned, canned_claims in GOLD:
        gold = gold_ids(chunks, gold_sentence)
        top = rerank(q)[:k]
        context = " ".join(texts[c] for c in top)

        if args.live:
            answer = call_llm(GEN_PROMPT.format(chunks="\n".join(f"[{c}] {texts[c]}" for c in top),
                                                question=q))
            claims = json.loads(call_llm(DECOMPOSE_PROMPT.format(answer=answer)))["claims"]
        else:
            answer = canned
            claims = canned_claims

        cited = extract_citations(answer)
        cited_ok = all(c in top for c in cited)
        checks = [check_claim(c, top, nli, texts) for c in claims]
        supported = sum(1 for v, _ in checks if v == "entailment")
        recall = len(set(top) & set(gold)) / len(gold)
        faithful = supported / len(claims)
        recall_sum += recall
        faithful_sum += faithful

        print(f"Q: {q}")
        print(f"    context: {' '.join(top)}")
        print(f"    answer:  {answer}")
        cited_txt = ", ".join(cited) if cited else "none"
        flag = "ok" if cited_ok else "DANGLING"
        print(f"    cited:   {cited_txt} ({flag})   gold {','.join(gold)}  "
              f"recall@3={recall:.2f}")
        for c, (v, src) in zip(claims, checks):
            if v == "entailment":
                mark = f"supported by {src}"
            elif v == "contradiction":
                mark = f"contradicted ({src})"
            else:
                mark = "not in context"
            print(f"      [{mark}] {c}")
        print(f"    faithfulness: {supported}/{len(claims)} = {faithful:.2f}\n")

    print(f"mean recall@3 = {recall_sum/len(GOLD):.2f}   "
          f"mean faithfulness = {faithful_sum/len(GOLD):.2f}")


if __name__ == "__main__":
    main()
