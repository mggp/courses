# AI Systems Resources

## Knowledge

- [Article: "Embeddings: What they are and why they matter" — Simon Willison](https://simonwillison.net/2023/Oct/23/embeddings/)
  The best practical introduction to embeddings and RAG for a working developer. Covers cosine similarity, semantic search, and a one-liner RAG shell script. Use for: lesson 1, any time embeddings need an intuition.
- [Paper: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" — Lewis et al. (arXiv:2005.11401)](https://arxiv.org/abs/2005.11401)
  The primary source that named RAG (NeurIPS 2020). Use for: the definition of RAG, why parametric memory alone is insufficient, provenance as a research goal.
- [Repo: pgvector — open-source vector similarity search for Postgres](https://github.com/pgvector/pgvector)
  Vector search as a Postgres extension: HNSW/IVFFlat indexes, cosine distance, hybrid search. Use for: the fintech angle — storing vectors next to the rest of your data, no new database. Also Simon Willison's preferred direction over dedicated vector DBs.
- [Course: Hugging Face NLP Course — "Sentence embeddings and semantic search" chapter](https://huggingface.co/learn/nlp-course)
  Hugging Face's free course. Use for: sentence-transformers, embedding models, and how they're trained. Not yet verified in-session; verify before citing in a lesson.
- [TIL: "Embedding paragraphs from my blog with E5-large-v2" — Simon Willison](https://til.simonwillison.net/llms/embed-paragraphs)
  Production-grade paragraph chunking: a 19,000-chunk index built from HTML paragraphs, plus E5's `query:`/`passage:` prefixes (a model trained to distinguish questions from facts). Use for: chunking strategy, provenance (his ids are `entry-paragraph`), and the fix direction for paraphrase gaps.
- [Docs: Ragas — evaluation framework for RAG applications](https://docs.ragas.io/en/stable/)
  The standard open-source framework for moving "from vibe checks to evaluation loops": context recall, faithfulness, answer correctness. Use for: lesson 2's evaluation concept, and later when hand-rolled metrics need a framework.
- [Model card: sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
  The local embedding model used in lessons 1–2. 384-dim, max sequence length 256 tokens (≈1000 chars) — the ceiling that bounds chunk size. Use for: chunk size limits, embedding model facts.

## Wisdom (Communities)

- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)
  High-signal practitioner community focused on running models locally. Use for: practical questions about local models, embedding models, and RAG setups that work on ordinary hardware.
- Hacker News threads on Simon Willison's posts
  His embeddings and RAG posts regularly spark informed technical discussion. Use for: seeing practitioners argue trade-offs (vector DB vs. Postgres, chunking strategies).
- Your mentor
  A real-world practitioner who already asked you about RAG. Use for: reviewing your designs, sanity-checking your architecture choices as you build.

## Gaps

- No verified high-trust resource yet on **hybrid search** (keyword + semantic, e.g. reciprocal rank fusion) — needed for lesson 3, which fixes the paraphrase gap observed in lesson 2. Candidates: pgvector's hybrid search example, blog posts on RRF.
- No verified resource yet on **evaluation of generated answers** (faithfulness/groundedness of the text the model writes, not just retrieval recall). Ragas covers this; verify a hands-on guide before turning it into a lesson.
