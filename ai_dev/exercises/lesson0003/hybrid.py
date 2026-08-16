"""hybrid.py — dense, BM25, and fused (RRF) retrieval, scored by recall@k.

Run:  uv run hybrid.py                          # gold-set recall table (k=3, RRF 60)
      uv run hybrid.py 5 100                    # same, with k=5 and RRF constant 100
      uv run hybrid.py --query "..."            # explore one query of your own
      uv run hybrid.py --query "..." --gold "sentence that must be retrieved"
"""
import argparse
import math
import re

import numpy as np
from sentence_transformers import SentenceTransformer

CORPUS = "corpus.md"
MODEL = "all-MiniLM-L6-v2"

STOP = set("""a an and are as at be but by for from in is it of on or so that the
to was what when where which who will with do does did his her its their
""".split())


# ---------- text analysis: lowercase + light stemming ----------
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


# ---------- chunking (lesson 2) ----------
def chunk_by_paragraph(text):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return [(f"p{i}", p) for i, p in enumerate(paras)]


# ---------- BM25: the classic keyword scorer ----------
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


# ---------- dense retrieval (lessons 1-2) ----------
def embed(model, texts):
    vecs = model.encode(texts)
    return vecs / np.linalg.norm(vecs, axis=1, keepdims=True)


# ---------- fusion by rank, not by score ----------
def rrf(lists, k=60):
    out = {}
    for ranked in lists:
        for rank, doc_id in enumerate(ranked, start=1):
            out[doc_id] = out.get(doc_id, 0.0) + 1.0 / (k + rank)
    return out


# Each question names the exact sentence that must end up in context.
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
    parser = argparse.ArgumentParser(description="BM25 + dense + RRF retrieval.")
    parser.add_argument("k", nargs="?", type=int, default=3,
                        help="context size k (how many chunks reach the generator)")
    parser.add_argument("rrf_k", nargs="?", type=int, default=60,
                        help="RRF damping constant")
    parser.add_argument("--query", help="run one query of your own and show all three rankings")
    parser.add_argument("--gold", help="with --query: a sentence whose chunk is the correct answer")
    args = parser.parse_args()
    k, rrf_k = args.k, args.rrf_k

    model = SentenceTransformer(MODEL)
    text = open(CORPUS, encoding="utf-8").read()
    chunks = chunk_by_paragraph(text)
    ids = [cid for cid, _ in chunks]
    vecs = embed(model, [t for _, t in chunks])
    bm25 = bm25_okapi([t for _, t in chunks])

    def ranked(query):
        qv = embed(model, [query])[0]
        dense = [ids[i] for i in np.argsort(vecs @ qv)[::-1][:10]]
        bm = [ids[i] for i, _ in sorted(bm25(query).items(), key=lambda kv: -kv[1])][:10]
        fused = [i for i, _ in sorted(rrf([dense, bm], rrf_k).items(), key=lambda kv: -kv[1])]
        return dense, bm, fused

    if args.query:
        dense, bm, fused = ranked(args.query)
        print(f"query: {args.query}")
        print(f"chunks: {len(chunks)}  |  k={k}  |  rrf k={rrf_k}\n")
        for name, top in (("dense", dense), ("bm25", bm), ("fused", fused)):
            print(f"  {name:6s} top-{k}: {' '.join(top[:k])}")
        if args.gold:
            gold = gold_ids(chunks, args.gold)
            print()
            if not gold:
                print("  gold: no chunk contains that sentence")
            else:
                print(f"  gold: {','.join(gold)}")
                for name, top in (("dense", dense), ("bm25", bm), ("fused", fused)):
                    ranks = {cid: r + 1 for r, cid in enumerate(top)}
                    hit = len(set(top[:k]) & set(gold)) / len(gold)
                    where = ", ".join(f"{c}@{ranks[c]}" for c in gold if c in ranks)
                    where = where or "not in top-10 ballot"
                    print(f"    {name:6s} recall@{k}={hit:.2f}  gold {where}")
        return

    print(f"chunks: {len(chunks)}  |  k={k}  |  rrf k={rrf_k}\n")
    header = f"{'':44s}{'dense':>6}{'bm25':>6}{'fused':>6}"
    print(header)
    print("-" * len(header))
    totals = {"dense": 0, "bm25": 0, "fused": 0}
    for q, gold_sentence in GOLD:
        gold = gold_ids(chunks, gold_sentence)
        dense, bm, fused = ranked(q)
        cells = {}
        for name, top in (("dense", dense), ("bm25", bm), ("fused", fused)):
            hit = len(set(top[:k]) & set(gold)) / len(gold)
            totals[name] += hit
            cells[name] = hit
        tag = "  <-- gold " + ",".join(gold) if gold else ""
        print(f"{q[:42]:44s}{cells['dense']:6.2f}{cells['bm25']:6.2f}{cells['fused']:6.2f}{tag}")
    print("-" * len(header))
    print(f"{'recall@k mean':44s}{totals['dense']/len(GOLD):6.2f}"
          f"{totals['bm25']/len(GOLD):6.2f}{totals['fused']/len(GOLD):6.2f}")


if __name__ == "__main__":
    main()
