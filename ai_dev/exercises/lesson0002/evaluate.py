"""evaluate.py — chunk a corpus, then measure retrieval recall@k.

Run:  uv run evaluate.py            # paragraph vs a few fixed sizes
      uv run evaluate.py 300 50     # one fixed size of your choosing
"""
import re
import sys

import numpy as np
from sentence_transformers import SentenceTransformer

CORPUS = "corpus.md"
K = 3


def load_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def chunk_by_paragraph(text):
    """Split on blank lines; keep each paragraph as its own chunk."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return [(f"p{i}", p) for i, p in enumerate(paras)]


def chunk_fixed_size(text, size=600, overlap=120):
    """Slide a window over the text; windows overlap so nothing
    straddling a boundary is lost."""
    text = re.sub(r"\s+", " ", text).strip()
    chunks, start = [], 0
    while start < len(text):
        end = min(start + size, len(text))
        chunks.append((f"f{len(chunks)}", text[start:end]))
        if end == len(text):
            break
        start += size - overlap
    return chunks


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
]


def embed(model, texts):
    vecs = model.encode(texts)
    return vecs / np.linalg.norm(vecs, axis=1, keepdims=True)


def gold_ids(chunks, sentence):
    return [cid for cid, text in chunks if sentence in text]


def run_chunker(model, name, chunks, questions):
    ids = [cid for cid, _ in chunks]
    vecs = embed(model, [text for _, text in chunks])
    recall_sum, rows = 0.0, []
    for q, gold_sentence in questions:
        gold = gold_ids(chunks, gold_sentence)
        q_vec = embed(model, [q])[0]
        scores = vecs @ q_vec
        order = np.argsort(scores)[::-1][:K]
        retrieved = [ids[i] for i in order]
        hits = set(retrieved) & set(gold)
        recall = len(hits) / len(gold)
        recall_sum += recall
        rows.append((q, gold, retrieved, recall))
    return rows, recall_sum / len(questions)


def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    text = load_text(CORPUS)
    print(f"corpus: {len(text)} chars  |  model max seq len: "
          f"{model.get_max_seq_length()} tokens\n")

    variants = [("paragraph", chunk_by_paragraph(text))]
    if len(sys.argv) >= 3:
        variants.append((f"fixed {sys.argv[1]}/{sys.argv[2]}",
                         chunk_fixed_size(text, int(sys.argv[1]), int(sys.argv[2]))))
    else:
        for size, overlap in [(600, 120), (300, 50), (150, 30)]:
            variants.append((f"fixed {size}/{overlap}",
                             chunk_fixed_size(text, size, overlap)))

    for name, chunks in variants:
        rows, mean = run_chunker(model, name, chunks, GOLD)
        print(f"== {name:16s} chunks={len(chunks):2d}  recall@{K} = {mean:.2f}")
        for q, gold, retrieved, recall in rows:
            flag = "" if recall == 1.0 else "   <-- miss"
            print(f"   {recall:.2f}  gold={gold}  top={retrieved}{flag}")
        print()


if __name__ == "__main__":
    main()
