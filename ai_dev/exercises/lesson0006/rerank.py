"""rerank.py — two-stage retrieval: cheap recall, then a cross-encoder re-ranks.

Lessons 3-4 recalled with two bi-encoders (dense + BM25) fused by RRF. This
lesson adds the second stage: take the fused candidate list, run a cross-encoder
over the top N (query, passage) pairs, and re-sort by its relevance score. The
recall stage reads each text separately; the cross-encoder reads the pair
together, so it can see paraphrase relationships the recall stage missed — at
the price of one model pass per candidate, which is why it only sees the top N.

Run:  uv run rerank.py            # fused vs reranked recall@k (k=3, pool N=10)
      uv run rerank.py 5 20       # different k / rerank pool size
      uv run rerank.py --query "..." --gold "sentence that must be retrieved"
"""
import argparse
import math
import re

import numpy as np
from sentence_transformers import SentenceTransformer, CrossEncoder

CORPUS = "corpus.md"
MODEL = "all-MiniLM-L6-v2"
RERANKER = "cross-encoder/ms-marco-MiniLM-L6-v2"

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


# Same gold set as lessons 3-4: each question names the exact sentence that
# must end up in the context the generator sees.
GOLD = [
    ("How does the tutor avoid teaching wrong facts?",
     "The tutor answers only from the course material, never from general knowledge"),
    ("When will a word be reviewed next?",
     "The scheduler computes the next review date"),
    ("What does the tutor do when it cannot find an answer?",
     "the tutor says it does not know rather than guessing"),
    ("How is a learner's question answered from the course chunks?",
     "The retrieval step embeds the learner's question and searches the lesson chunks"),
    ("Which engine suggests the next lesson?",
     "suggests new lessons based on recently missed words"),
    ("What method keeps long-term recall sharp?",
     "Spaced repetition schedules the review of each word at growing intervals"),
]


def gold_ids(chunks, sentence):
    return [cid for cid, text in chunks if sentence in text]


def main():
    parser = argparse.ArgumentParser(description="Cross-encoder reranking of fused retrieval.")
    parser.add_argument("k", nargs="?", type=int, default=3,
                        help="context size k (how many chunks reach the generator)")
    parser.add_argument("pool", nargs="?", type=int, default=10,
                        help="rerank pool N (candidates the cross-encoder re-orders)")
    parser.add_argument("--query", help="run one query of your own and show both orderings")
    parser.add_argument("--gold", help="with --query: a sentence whose chunk is the correct answer")
    args = parser.parse_args()
    k, pool = args.k, args.pool

    model = SentenceTransformer(MODEL)
    reranker = CrossEncoder(RERANKER)
    text = open(CORPUS, encoding="utf-8").read()
    chunks = chunk_by_paragraph(text)
    ids = [cid for cid, _ in chunks]
    texts = {cid: t for cid, t in chunks}
    vecs = embed(model, [t for _, t in chunks])
    bm25 = bm25_okapi([t for _, t in chunks])

    def fused_list(query):
        qv = embed(model, [query])[0]
        dense = [ids[i] for i in np.argsort(vecs @ qv)[::-1][:pool]]
        bm = [ids[i] for i, _ in sorted(bm25(query).items(), key=lambda kv: -kv[1])][:pool]
        return [i for i, _ in sorted(rrf([dense, bm], 60).items(), key=lambda kv: -kv[1])]

    def reranked_list(query):
        candidates = fused_list(query)[:pool]
        scores = reranker.predict([(query, texts[c]) for c in candidates])
        order = np.argsort(scores)[::-1]
        return [candidates[i] for i in order]

    if args.query:
        fused = fused_list(args.query)
        reranked = reranked_list(args.query)
        print(f"query: {args.query}")
        print(f"chunks: {len(chunks)}  |  k={k}  |  rerank pool N={pool}  |  reranker: {RERANKER}\n")
        print(f"  fused   top-{k}: {' '.join(fused[:k])}")
        print(f"  reranked top-{k}: {' '.join(reranked[:k])}")
        if args.gold:
            gold = gold_ids(chunks, args.gold)
            print()
            for name, top in (("fused", fused), ("reranked", reranked)):
                ranks = {cid: r + 1 for r, cid in enumerate(top)}
                hit = len(set(top[:k]) & set(gold)) / len(gold)
                where = ", ".join(f"{c}@{ranks[c]}" for c in gold if c in ranks)
                where = where or "not in pool"
                print(f"    {name:8s} recall@{k}={hit:.2f}  gold {where}")
        return

    print(f"chunks: {len(chunks)}  |  k={k}  |  rerank pool N={pool}  |  reranker: {RERANKER}\n")
    header = f"{'':44s}{'fused':>6}{'reranked':>9}"
    print(header)
    print("-" * len(header))
    totals = {"fused": 0, "reranked": 0}
    for q, gold_sentence in GOLD:
        gold = gold_ids(chunks, gold_sentence)
        fused = fused_list(q)
        reranked = reranked_list(q)
        cells = {}
        for name, top in (("fused", fused), ("reranked", reranked)):
            hit = len(set(top[:k]) & set(gold)) / len(gold)
            totals[name] += hit
            cells[name] = hit
        tag = "  <-- gold " + ",".join(gold) if gold else ""
        print(f"{q[:42]:44s}{cells['fused']:6.2f}{cells['reranked']:9.2f}{tag}")
    print("-" * len(header))
    print(f"{'recall@k mean':44s}{totals['fused']/len(GOLD):6.2f}"
          f"{totals['reranked']/len(GOLD):9.2f}")


if __name__ == "__main__":
    main()
