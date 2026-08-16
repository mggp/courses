"""Hybrid search demo: BM25 vs dense vs RRF fusion, with light stemming."""
import math
import re

import numpy as np
from sentence_transformers import SentenceTransformer

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


def rrf(lists, k=60):
    out = {}
    for ranked in lists:
        for rank, doc_id in enumerate(ranked, start=1):
            out[doc_id] = out.get(doc_id, 0.0) + 1.0 / (k + rank)
    return out


text = open("corpus.md").read()
paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_vecs = np.array([model.encode([p])[0] for p in paras])
doc_vecs = doc_vecs / np.linalg.norm(doc_vecs, axis=1, keepdims=True)
bm25 = bm25_okapi(paras)

QUERIES = [
    "What does the tutor do when it cannot find an answer?",
    "How is a learner's account kept secure?",
    "How often are words reviewed?",
]

for q in QUERIES:
    qv = model.encode([q])[0]
    qv = qv / np.linalg.norm(qv)
    dense_list = [int(i) for i in np.argsort(doc_vecs @ qv)[::-1][:10]]
    bm25_scores = bm25(q)
    bm25_list = [i for i, _ in sorted(bm25_scores.items(), key=lambda kv: -kv[1])][:10]
    fused = rrf([dense_list, bm25_list])
    fused_list = [i for i, _ in sorted(fused.items(), key=lambda kv: -kv[1])]

    print(f"Q: {q}")
    for r in range(4):
        d = dense_list[r]
        b = bm25_list[r] if r < len(bm25_list) else None
        f = fused_list[r] if r < len(fused_list) else None
        cells = [f"dense={d:<3}", f"bm25={b if b is not None else '-':<3}",
                 f"fused={f if f is not None else '-':<3}"]
        label = paras[f][:40] if f is not None else ""
        print(f"  {r}. {'  '.join(cells)} {label}")
    print()
