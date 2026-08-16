# Embedding similarity ≠ domain ontology: why the lesson-2 miss happened

Deepening of lesson 2's miss. The user correctly suspected the embedding model was "unaware" of the system's context — that the chunk↔answer↔citation coupling is an ontology of the app, not something a general English model encodes. Diagnosing the actual ranking confirmed the mechanism is more precise than the lesson's original "no vocabulary overlap" gloss:

- The gold chunk p10 was **rank 4**, a near-miss at k=3, not rank 13.
- The winners won on **surface form**: p4 literally shares the query's word "cannot"; p3/p4 share "answers" (morphological sibling of "answer"); p10 shares only function words (`does it the tutor`) while its content words (`chunk, know, guessing`) have no query counterpart.
- Because MiniLM pools by averaging token vectors, distinctive content words contribute a whisper against the shared grammatical scaffolding — so the model ranked on token overlap, not meaning.

**Evidence**: diagnostic script output (shared-token table and full 13-chunk ranking for the question), plus two confirmed rescues: (1) paraphrasing the query into the answer's vocabulary lifts p10 to rank 1 with the *same* model (the HyDE/query-expansion direction); (2) a cross-encoder rerank (cross-encoder/ms-marco-MiniLM-L6-v2) lifts p10 from rank 4 to rank 2 — a real gain, but not a full fix for this off-the-shelf reranker, which still prefers the literal-overlap passage.

**Implications**: Lesson 3 must cover the retrieval-layer fixes, in order of leverage: query expansion / HyDE (arXiv:2212.10496), cross-encoder reranking, retriever models trained on question–passage pairs (E5/BGE — the `query:`/`passage:` prefix idea from lesson 2's primary source), hybrid search (BM25 + dense + RRF), and domain fine-tuning on synthetic question–chunk pairs. The learner engages at the mechanism level and wants empirical demonstration, not assertion — keep showing real numbers from his own corpus. Also: teach the no-match threshold ("tutor says it does not know") as a system-design pattern, since p10 literally describes it.
