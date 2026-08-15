# Completed lesson 1: built the RAG loop, and his run exposed the quality problem

The learner completed the lesson-1 exercise on his own initiative: set the project up with `uv`, adapted the lesson code, changed the question to the harder paraphrase one ("How does RAG stop the model making things up?"), and raised k to 4. Running his exact script shows the answer chunk ("Generation feeds retrieved chunks to an LLM…") ranked 3rd at 0.133, behind a keyword hit ("RAG stands for…", 0.583).

**Evidence**: The exercise lives at `exercises/lesson0001/` (pyproject, uv.lock, rag.py); I executed his script and reproduced the output above.

**Implications**: He has the full loop working and now knows embeddings/cosine/retrieval mechanically. The gap is quality: chunking real corpora and measuring retrieval — lesson 2. His own output is the strongest possible motivation ("seems fine" hiding a rank-3 answer). Also establishes a workspace convention: runnable exercises in `exercises/lessonNNNN/` using uv.
