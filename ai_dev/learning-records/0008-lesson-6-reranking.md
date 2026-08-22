# Lesson 6 delivered: reranking — the second retrieval stage, measured honestly

The learner flagged that reranking had been referenced repeatedly (glossary retrieval-layer, lesson 2's "next lesson's material", the lesson-2 diagnosis) but never taught. Lesson 6 closes that gap: two-stage retrieval — bi-encoder recall, then a cross-encoder re-orders the candidate pool. `exercises/lesson0006/rerank.py` reuses the lesson-3 machinery and adds `cross-encoder/ms-marco-MiniLM-L6-v2`.

**Evidence**: on the 24-chunk Lingua corpus, the same six-question gold set:
- Default (pool N=10): fused recall@3 mean **0.83 → reranked 1.00**. The paraphrase row is rescued: gold p9 moves from fused rank 5 → reranked rank 3, with no query rewriting. Cross-encoder scores p3 3.65, p2 0.09, p9 −2.14, p4 −4.90 — uncalibrated (negative is normal), and p9 only clears k=3 at the edge (a rescue, not a slam dunk).
- Pool N=3: the paraphrase row stays 0.00 — p9 is at fused rank 5, never reaches the reranker. Recall is the floor.
- Pool N=24 (whole corpus): the paraphrase row is rescued but the "long-term recall sharp" row *drops* (p5 falls rank 1 → rank 4; the cross-encoder's scores bunch near −11.2 over the junk tail and GDPR/daily-streak/2FA sneak above it). Net mean back to 0.83 — one row traded for another.

**Implications**: (1) Reranking is the first retrieval-layer tool to rescue the paraphrase row without touching the query — complementing, not replacing, lessons 3–4. (2) The candidate-pool size is a real knob with a U-shaped failure: too small = floor blocks the reranker, too large = the cross-encoder's own errors reappear; the sweet spot is recall's filtered top-N. (3) Cross-encoder scores are uncalibrated — teach order, not magnitude. (4) "Measured, never trusted" now applies to reranking exactly as it did to fusion. Retrieval layer is complete (hybrid → query → rerank); next is the capstone with citations + both metrics.

