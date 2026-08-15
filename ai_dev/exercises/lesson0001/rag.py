"""rag.py — a minimal Retrieval-Augmented Generation pipeline."""
import numpy as np
from sentence_transformers import SentenceTransformer

# ---- your corpus: five one-line "documents" ----
docs = [
    "RAG stands for Retrieval-Augmented Generation.",
    "An embedding maps text into a vector space where similar meaning sits nearby.",
    "Cosine similarity measures how close two normalized vectors are.",
    "Chunking splits a document into pieces small enough to retrieve precisely.",
    "Generation feeds retrieved chunks to an LLM along with the question.",
]

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    vecs = model.encode(texts)
    return vecs / np.linalg.norm(vecs, axis=1, keepdims=True)

doc_vecs = embed(docs)

def retrieve(query, k=2):
    q = embed([query])[0]
    scores = doc_vecs @ q
    order = np.argsort(scores)[::-1][:k]
    return [(docs[i], float(scores[i])) for i in order]

def generate(question, context):
    prompt = (
        "Answer the question using only the context below.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}\n"
    )
    # Swap in any provider you have access to: OpenAI, Anthropic, a local model…
    import openai
    reply = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return reply.choices[0].message.content

if __name__ == "__main__":
    question = "How does RAG stop the model making things up?"
    hits = retrieve(question, k=4)
    for doc, score in hits:
        print(f"{score:.3f}  {doc}")
    context = "\n\n".join(doc for doc, _ in hits)
    print("\n--- generation (optional) ---")
    # print(generate(question, context))
