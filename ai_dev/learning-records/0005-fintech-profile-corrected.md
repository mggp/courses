# Fintech profile corrected: MySQL/DynamoDB stack and the real use-case list

The learner corrected the fintech assumptions baked into lesson 3: the employer does not use Postgres (his database background is MySQL and DynamoDB), and the short-term use cases are fraud detection, KYC auditing, loan underwriting, credit risk assessment, and document Q&A. He is not a product person — the use-case list is expected to grow and he explicitly wants suggestions of other relevant directions. The language app (Lingua) keeps its invented specifics only because they are framed as hypothetical; the app does not exist yet.

**Evidence**: Direct disclosure in this session; lesson 3 rewritten to be stack-agnostic with all code, corpus, and gold set reused unchanged.

**Implications**: Never claim a specific production stack again; present database-specific recipes (pgvector, FULLTEXT indexes) as transferable mechanics. The use-case list splits into two problems with two toolkits: retrieval-heavy work (KYC auditing, document Q&A — served by the current RAG spine through grounded-answer evaluation) and prediction work (fraud detection, loan underwriting, credit risk — a future lesson on LLM-as-classifier, structured-data classification, or anomaly detection). Since he invited other directions, keep proposing genuinely relevant tracks as the retrieval spine completes.
