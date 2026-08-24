# Mission: Building AI Systems in Python

## Why

You are an experienced Python web developer who wants to move from *knowing about* AI to *building with* it. The concrete goals: a web app that helps people learn languages (an AI tutor grounded in course material — still hypothetical), real applications at your fintech (fraud detection, KYC auditing, loan underwriting, credit risk assessment, document Q&A), and staying ahead of where the job market is going. An upcoming interview makes concise, truthful articulation of AI-system design a near-term priority. You are not a product person, so this use-case list is expected to grow as you build. Your mentor asking whether you knew what RAG is — and your answer being "yes, but I couldn't build one" — is the gap this workspace closes.

## Success looks like

- Build a working RAG system from scratch (no framework hiding the mechanics) and explain every moving part
- Ship an AI feature end-to-end: documents in, retrieved context, grounded answers out — with citations the user can verify
- Design and critique AI features at work, including where RAG helps, where it doesn't, and the compliance/security constraints a fintech must respect
- Choose sensibly between building your own pipeline vs. using frameworks (LangChain, vector DBs) once you understand what they're doing for you
- See the fintech short-list as two problems with two toolkits: retrieval-heavy work (KYC auditing, document Q&A) and prediction work (fraud detection, loan underwriting, credit risk) — and know which is which
- Give concise, technically accurate interview answers about LLM systems, agents, RAG architecture, guardrails, data stores, and cloud trade-offs — without overstating hands-on experience

## Constraints

- Compliance rules at work forbid using AI in day-to-day work — all learning and experimentation happens outside work hours, on personal projects
- Strong Python and web background; database background is MySQL and DynamoDB — not Postgres, and limited Postgres exposure
- Personal projects may run on ordinary hardware — prefer approaches that work locally where possible (small models, local stores)
- No assumption about the employer's production stack; treat database-specific recipes as mechanics to transfer, not facts about the environment
- Interview topics are a near-term sequencing constraint: cover uncovered agent, safety, data-architecture, and cloud concepts before deeper elective work
- Never inflate personal or production experience; distinguish maintained services, personal projects, configuration work, and concepts learned in this workspace

## Out of scope

- Training models from scratch, fine-tuning for now, and deep ML theory (gradients, backprop) — return later only if a mission goal demands it
- Using AI at work until compliance gives the go-ahead; learning is not permission to use it in production
