# AI Systems Resources

## Knowledge

- [Article: "Embeddings: What they are and why they matter" — Simon Willison](https://simonwillison.net/2023/Oct/23/embeddings/)
  The best practical introduction to embeddings and RAG for a working developer. Covers cosine similarity, semantic search, and a one-liner RAG shell script. Use for: lesson 1, any time embeddings need an intuition.
- [Paper: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" — Lewis et al. (arXiv:2005.11401)](https://arxiv.org/abs/2005.11401)
  The primary source that named RAG (NeurIPS 2020). Use for: the definition of RAG, why parametric memory alone is insufficient, provenance as a research goal.
- [Repo: pgvector — open-source vector similarity search for Postgres](https://github.com/pgvector/pgvector)
  Vector search as a Postgres extension: HNSW/IVFFlat indexes, cosine distance, hybrid search. Use for: the canonical worked example of hybrid fusion (its README's [RRF / cross-encoder example](https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/rrf.py)) — read for the mechanics, not the stack, since the learner runs MySQL/DynamoDB rather than Postgres. Also Simon Willison's preferred direction over dedicated vector DBs.
- [Course: Hugging Face NLP Course — "Sentence embeddings and semantic search" chapter](https://huggingface.co/learn/nlp-course)
  Hugging Face's free course. Use for: sentence-transformers, embedding models, and how they're trained. Not yet verified in-session; verify before citing in a lesson.
- [TIL: "Embedding paragraphs from my blog with E5-large-v2" — Simon Willison](https://til.simonwillison.net/llms/embed-paragraphs)
  Production-grade paragraph chunking: a 19,000-chunk index built from HTML paragraphs, plus E5's `query:`/`passage:` prefixes (a model trained to distinguish questions from facts). Use for: chunking strategy, provenance (his ids are `entry-paragraph`), and the fix direction for paraphrase gaps.
- [Docs: Ragas — evaluation framework for RAG applications](https://docs.ragas.io/en/stable/)
  The standard open-source framework for moving "from vibe checks to evaluation loops": context recall, faithfulness, answer correctness. Use for: lesson 2's evaluation concept, and later when hand-rolled metrics need a framework.
- [Model card: sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
  The local embedding model used in lessons 1–2. 384-dim, max sequence length 256 tokens (the card's "word pieces"; ≈200 words of English prose) — the ceiling that bounds chunk size. Use for: chunk size limits, embedding model facts.
- [Paper: "Query Rewriting for Retrieval-Augmented Large Language Models" — Ma et al., EMNLP 2023 (arXiv:2305.14283)](https://arxiv.org/abs/2305.14283)
  The query-layer anchor: names the gap between input text and needed knowledge, and the rewrite-retrieve-read pipeline. Use for: lesson 4, any query-rewriting discussion.
- [Paper: "RAG-Fusion: a New Take on Retrieval-Augmented Generation" — Rackauckas (arXiv:2402.03367)](https://arxiv.org/abs/2402.03367)
  Multi-query generation fused with RRF, applied in industry, with an honest caveat about off-topic variants. Use for: lesson 4's multi-query family.
- [Paper: "Precise Zero-Shot Dense Retrieval without Relevance Labels" (HyDE) — Gao et al. (arXiv:2212.10496)](https://arxiv.org/abs/2212.10496)
  The hypothetical-document-embeddings paper: generate a plausible answer, embed it, retrieve by it; the encoder filters the false details. Use for: lesson 4's HyDE family.
- [Paper: "RAGAS: Automated Evaluation of Retrieval Augmented Generation" — Es et al. (arXiv:2309.15217)](https://arxiv.org/abs/2309.15217)
  Reference-free evaluation framework spanning retrieval, faithfulness, and generation quality. Its faithfulness recipe (claims → inferable-from-context → supported/total) is the anchor for lesson 5. Use for: faithfulness evaluation, any RAG evaluation discussion.
- [Paper: "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation" — Min et al., EMNLP 2023 (arXiv:2305.14251)](https://arxiv.org/abs/2305.14251)
  Decomposes a generation into atomic facts and scores each against a knowledge source; ChatGPT only reaches 58%. The conceptual parent of faithfulness-as-decomposition. Use for: lesson 5's decompose step.
- [Docs: Ragas — Faithfulness metric](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)
  The canonical worked definition: identify claims, check each is inferable from context, score = supported/total, with the Einstein 0.5 example. Use for: lesson 5's score step and citation.
- [Model card: cross-encoder/nli-MiniLM2-L6-H768](https://huggingface.co/cross-encoder/nli-MiniLM2-L6-H768)
  The local NLI cross-encoder used in lesson 5 (82M params, SNLI + MultiNLI; labels contradiction / entailment / neutral). Small enough for ordinary hardware. Use for: the entailment check, the three-label distinction.
- [Paper: "Passage Re-ranking with BERT" — Nogueira & Cho (arXiv:1901.04085)](https://arxiv.org/abs/1901.04085)
  The origin of the reranking stage: BERT over the top candidates, +27% MRR@10 on MS MARCO. Use for: lesson 6, any two-stage retrieval discussion.
- [Model card: cross-encoder/ms-marco-MiniLM-L6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2)
  The local relevance cross-encoder used in lesson 6 (22.7M params, MS MARCO passage ranking, MRR@10 39.01). Documents that the score is uncalibrated — only the order matters — and links SBERT.net's "Retrieve & Re-rank" guide. Use for: the rerank stage, the pool-size tradeoff.
- [Docs: Ragas — Context Precision](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/)
  The canonical definition of the noise metric: precision@k averaged over ranks, rank-weighted. Use for: precision@k / context precision, the "how much of the retrieved set is noise" question, and its sibling Context Recall.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" — Liu et al., TACL 2023 (arXiv:2307.03172)](https://arxiv.org/abs/2307.03172)
  The caveat that keeps rank from being fully irrelevant to a generator: relevant info at the start or end of context is used best; performance degrades in the middle of long contexts. Use for: the "raise k vs rerank" tradeoff, why order still matters a little at large k.
- [Paper: "Attributed Question Answering: Evaluation and Modeling for Attributed LLMs" — Bohnet et al. (arXiv:2212.08037)](https://arxiv.org/abs/2212.08037)
  Formulates *attribution* as the task — can the model point to the source supporting each claim? — and how to measure it. Use for: the citation/provenance concern, "attribution" as the umbrella term.
- [Paper: "Enabling Large Language Models to Generate Text with Citations" (ALCE) — Gao et al., EMNLP 2023 (arXiv:2305.14627)](https://arxiv.org/abs/2305.14627)
  The first automatic citation-evaluation benchmark: fluency, correctness, and citation quality (recall = every claim cited, precision = every citation supports its claim). Finding: best models lack complete citation support 50% of the time on ELI5. Use for: citation precision/recall, the capstone's attribution upgrade.
- [Docs: scikit-learn — Text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
  The official explanation of bag-of-words and TF-IDF: a representation born in information retrieval that also works with supervised document classifiers. Use for: lesson 8's retrieval-versus-classification bridge, any sparse-text baseline.
- [Example: scikit-learn — Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)
  Official end-to-end text-classification example with held-out evaluation, confusion matrix, and a real metadata-leakage failure mode. Use for: the first local classifier, leakage discipline, error review.
- [Docs: scikit-learn — Tuning the decision threshold for class prediction](https://scikit-learn.org/stable/modules/classification_threshold.html)
  Separates probability estimation from the action policy; warns that a 0.5 cutoff is only a default and threshold tuning must not reuse training data. Use for: lesson 8's abstain path, future cost-sensitive classification.
- [Paper: "Language Models (Mostly) Know What They Know" — Kadavath et al. (arXiv:2207.05221)](https://arxiv.org/abs/2207.05221)
  Finds useful self-evaluation calibration in some formats but poor transfer of P(IK) calibration to new tasks. Use for: the later LLM-as-classifier lesson; generated confidence is not a deployment-ready probability without target-distribution validation.
- [Guide: "Building Effective Agents" — Anthropic](https://www.anthropic.com/research/building-effective-agents)
  Framework-neutral enough practical distinction between fixed workflows and agents that dynamically choose tools/process. Use for: agent versus LLM, begin with a single agent plus tools.
- [Paper: "ReAct: Synergizing Reasoning and Acting in Language Models" — Yao et al. (arXiv:2210.03629)](https://arxiv.org/abs/2210.03629)
  Primary action-loop paper: interleave model reasoning with external actions and observations. Use for: the agent control loop, tools, and feedback.
- [Specification: Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25)
  Official protocol specification: host/client/server architecture and standardized tool, resource, and prompt access. Use for: MCP versus tools/skills; MCP does not provide planning, memory, or authorization policy by itself.
- [Specification: MCP server tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)
  A tool is a schema-described callable capability. Descriptions/annotations are untrusted unless the server is trusted; validate inputs and require approval for sensitive calls. Use for: tool safety and guardrails.
- [Specification: Agent Skills](https://agentskills.io/specification)
  A skill is a reusable instruction-and-resource package (typically `SKILL.md` plus optional scripts/references/assets), distinct from an MCP primitive or callable tool. Use for: tools versus skills versus MCP.
- [Guide: "How we built our multi-agent research system" — Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
  Concrete multi-agent tradeoffs: use independent breadth-first work or context isolation; expect higher token cost, coordination complexity, and difficult debugging. Use for: single versus multi-agent choice.
- [Paper: "MemGPT: Towards LLMs as Operating Systems" — Packer et al. (arXiv:2310.08560)](https://arxiv.org/abs/2310.08560)
  Primary framing for externalized agent memory under a limited context window. Use for: short-term prompt state versus long-term persisted/retrieved memory.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
  Non-vendor governance framework: govern, map, measure, manage AI risk. Use for: interview framing of guardrails as lifecycle controls, not merely prompt filters.
- [NIST Generative AI Profile, AI 600-1](https://doi.org/10.6028/NIST.AI.600-1)
  Generative-AI risk profile that grounds guardrails in system design, monitoring, human oversight, and residual-risk management. Use for: financial-RAG safety and compliance controls.
- [Paper: "The Curious Case of Neural Text Degeneration" — Holtzman et al. (arXiv:1904.09751)](https://arxiv.org/abs/1904.09751)
  Primary source for nucleus (`top_p`) sampling: sample from the smallest dynamic set whose probability mass reaches p. Use for: temperature/top-p interview answers and sampling tradeoffs.
- [Docs: Neo4j — What is a graph database?](https://neo4j.com/docs/getting-started/graph-database/)
  Official graph-database introduction: nodes, relationships, properties, and graph traversal. Use for: vector versus graph data architecture, relationship-heavy fraud and ownership questions.
- [Docs: Amazon Bedrock — Overview](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
  Official Bedrock overview. Use for: truthful cloud-platform architecture discussion: model inference, managed features, IAM, networking, observability, and cost.
- [Docs: Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
  Official managed/custom RAG documentation. Use for: mapping the hand-built RAG spine to Bedrock without claiming production experience.
- [Docs: Microsoft Foundry — What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)
  Official current Microsoft/Azure AI platform overview. Use for: Azure AI comparison, deployment, agents, RBAC, evaluation, and monitoring vocabulary.
- [Docs: Google Vertex AI generative AI quickstart](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart)
  Official requested Vertex AI generative-AI starting point; currently redirects toward Gemini Enterprise Agent Platform documentation. Use for: Google platform vocabulary, with version/date awareness.

## Wisdom (Communities)

- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)
  High-signal practitioner community focused on running models locally. Use for: practical questions about local models, embedding models, and RAG setups that work on ordinary hardware.
- Hacker News threads on Simon Willison's posts
  His embeddings and RAG posts regularly spark informed technical discussion. Use for: seeing practitioners argue trade-offs (vector DB vs. Postgres, chunking strategies).
- Your mentor
  A real-world practitioner who already asked you about RAG. Use for: reviewing your designs, sanity-checking your architecture choices as you build.

## Gaps

- No verified high-trust resource yet on **the full evaluation loop at scale** (Ragas as a framework, HHEM-2.1-Open as an alternative hallucination classifier, and running metrics in CI) — worth verifying before the capstone lesson adds a citation-backed grounded answer.
- Query-rewriting/HyDE coverage is now closed (lesson 4 + three verified papers); a practitioner write-up with a runnable example would still be a nice complement but is no longer blocking.
- Retrieval-metric coverage is now closed (recall@k, precision@k/context precision, MRR, NDCG, and the set-vs-rank rule all have glossary entries and sources; see LR-0009).
- The capstone (lesson 7) is delivered. Remaining unverified: a practitioner guide on a citation/attribution UI or an evaluation dashboard.
- Prediction track has begun with local sparse text classification (lesson 8). Still missing before the fintech applications: verified sources on label design and class imbalance, probability calibration, LLM-as-classifier with structured output, structured/tabular classification, and anomaly detection. Do not claim the fictional support-ticket baseline transfers to fraud, underwriting, or credit risk.
- Interview-first gaps now have verified sources. Still missing before interview drills become production claims: hands-on cloud AI work, framework experience beyond the learner's personal LangGraph/MCP work, and a verified source on fixed-size versus semantic chunking. The roadmap is `reference/interview-roadmap.html`.
