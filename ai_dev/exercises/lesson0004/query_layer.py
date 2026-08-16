"""query_layer.py — three query-layer fixes measured against the gold set.

The retrieval helpers (chunking, BM25, RRF, embedding) are reused from lesson 3.

Run:  uv run query_layer.py                     # comparison table (k=3, RRF 60)
      uv run query_layer.py 5 60                # different k / RRF constant
      uv run query_layer.py --live              # generate rewrites with an LLM
                                                # (needs OPENAI_API_KEY, optional OPENAI_BASE_URL)
"""
import argparse
import json
import math
import os
import re

import numpy as np
from sentence_transformers import SentenceTransformer

CORPUS = "corpus.md"
MODEL = "all-MiniLM-L6-v2"

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


def gold_ids(chunks, sentence):
    return [cid for cid, text in chunks if sentence in text]


# (question, answer sentence, optional query-layer set).
# The rewrite / variants / hyde strings are what a good LLM produces for the hard
# question; --live regenerates them with your own model instead.
GOLD = [
    ("How does the tutor avoid teaching wrong facts?",
     "The tutor answers only from the course material, never from general knowledge",
     None),
    ("When will a word be reviewed next?",
     "The scheduler computes the next review date",
     None),
    ("What does the tutor do when it cannot find an answer?",
     "the tutor says it does not know rather than guessing",
     {
        "rewrite": "How does the tutor respond when it has no answer?",
        "variants": [
            "What happens when the tutor cannot answer a learner's question?",
            "What does the tutor do if it is unable to answer?",
            "How does the tutor handle a question it cannot answer?",
            "How does the tutor respond when it has no answer?",
            "What happens when no answer can be found for the learner's question?",
        ],
        "hyde": "If no chunk is close enough, the tutor says it does not know rather than guessing.",
     }),
    ("How is a learner's question answered from the course chunks?",
     "The retrieval step embeds the learner's question and searches the lesson chunks",
     None),
    ("Which engine suggests the next lesson?",
     "suggests new lessons based on recently missed words",
     None),
    ("What method keeps long-term recall sharp?",
     "Spaced repetition schedules the review of each word at growing intervals",
     None),
]

LIVE_PROMPT = (
    "You are a query rewriter for a retrieval system over a language-tutor product brief.\n"
    "Given a user question, return JSON with three fields:\n"
    '  "rewrite": one search query that matches how the corpus phrases things,\n'
    '  "variants": four alternative search queries, covering different phrasings,\n'
    '  "hyde": a short hypothetical passage from the corpus that would answer the question.\n'
    'Reply with JSON only.\n'
    "User question: {question}"
)


def live_query_set(question):
    from openai import OpenAI

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),
                    base_url=os.environ.get("OPENAI_BASE_URL"))
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    reply = client.chat.completions.create(
        model=model,
        messages=[{"role": "user",
                   "content": LIVE_PROMPT.format(question=question)}],
        response_format={"type": "json_object"},
    )
    data = json.loads(reply.choices[0].message.content)
    return {
        "rewrite": data["rewrite"],
        "variants": [data["rewrite"]] + data["variants"][:3],
        "hyde": data["hyde"],
    }


def main():
    parser = argparse.ArgumentParser(description="Query-layer fixes: rewrite, multi, HyDE.")
    parser.add_argument("k", nargs="?", type=int, default=3)
    parser.add_argument("rrf_k", nargs="?", type=int, default=60)
    parser.add_argument("--live", action="store_true",
                        help="generate rewrites with an LLM instead of the canned set")
    args = parser.parse_args()
    k, rrf_k = args.k, args.rrf_k

    model = SentenceTransformer(MODEL)
    text = open(CORPUS, encoding="utf-8").read()
    chunks = chunk_by_paragraph(text)
    ids = [cid for cid, _ in chunks]
    vecs = embed(model, [t for _, t in chunks])
    bm25 = bm25_okapi([t for _, t in chunks])

    def dense_list(q):
        qv = embed(model, [q])[0]
        return [ids[i] for i in np.argsort(vecs @ qv)[::-1][:10]]

    def bm25_list(q):
        return [ids[i] for i, _ in sorted(bm25(q).items(), key=lambda kv: -kv[1])][:10]

    def fused_list(queries):
        ballots = []
        for q in queries:
            ballots.append(dense_list(q))
            ballots.append(bm25_list(q))
        return [i for i, _ in sorted(rrf(ballots, rrf_k).items(), key=lambda kv: -kv[1])]

    def recall(fused, gold):
        return len(set(fused[:k]) & set(gold)) / len(gold)

    print(f"chunks: {len(chunks)}  |  k={k}  |  rrf k={rrf_k}  |  "
          f"queries: {'live LLM' if args.live else 'canned'}\n")
    header = f"{'':44s}{'raw':>6}{'rewrite':>8}{'multi':>7}{'hyde':>6}"
    print(header)
    print("-" * len(header))
    totals = {"raw": 0.0, "rewrite": 0.0, "multi": 0.0, "hyde": 0.0}
    variant_detail = None
    for q, answer, qset in GOLD:
        gold = gold_ids(chunks, answer)
        if args.live:
            qset = live_query_set(q)
        qset = qset or {}
        variants = qset.get("variants") or [q]
        strategies = {
            "raw": [q],
            "rewrite": [qset.get("rewrite", q)],
            "multi": variants,
            "hyde": [qset.get("hyde", q)],
        }
        cells = {name: recall(fused_list(queries), gold) for name, queries in strategies.items()}
        for name in totals:
            totals[name] += cells[name]
        if qset and "variants" in qset:
            variant_detail = (q, answer, gold, variants)
        print(f"{q[:42]:44s}{cells['raw']:6.2f}{cells['rewrite']:8.2f}"
              f"{cells['multi']:7.2f}{cells['hyde']:6.2f}  <-- gold {','.join(gold)}")
    print("-" * len(header))
    print(f"{'recall@k mean':44s}{totals['raw']/len(GOLD):6.2f}"
          f"{totals['rewrite']/len(GOLD):8.2f}{totals['multi']/len(GOLD):7.2f}"
          f"{totals['hyde']/len(GOLD):6.2f}")

    if variant_detail:
        q, answer, gold, variants = variant_detail
        hyde = next(gs.get("hyde") for gq, ga, gs in GOLD if gq == q and gs)
        print(f"\nWhy rewrite is fragile — fused rank of the gold chunk for each variant of:\n"
              f"  \"{q}\"")
        for v in variants:
            fused = fused_list([v])
            rank = fused.index(gold[0]) + 1 if gold[0] in fused else None
            hit = "  <-- inside k" if rank is not None and rank <= k else ""
            print(f"  {rank if rank else '-':>3}  {v}{hit}")
        fused = fused_list(variants)
        rank = fused.index(gold[0]) + 1 if gold[0] in fused else None
        print(f"  {rank if rank else '-':>3}  multi: RRF over all variants above")
        fused = fused_list([hyde])
        rank = fused.index(gold[0]) + 1 if gold[0] in fused else None
        print(f"  {rank if rank else '-':>3}  hyde: {hyde[:50]}")


if __name__ == "__main__":
    main()
