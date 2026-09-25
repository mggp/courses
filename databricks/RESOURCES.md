# Databricks Generative AI Engineer Associate resources

## Knowledge

- [Exam guide: March 18, 2026](references/exam-guide.md)
  The controlling source for exam scope. Use it to decide what belongs in the course, not as authority for current product behavior after its publication date.
- [Agent development lifecycle](https://docs.databricks.com/aws/en/agents/agents-dev-lifecycle)
  Current Databricks workflow for scoping, building, evaluating, and operating agents. Use for requirements, inputs, expected responses, success criteria, tools, and lifecycle questions.
- [Agent system design patterns](https://docs.databricks.com/aws/en/agents/agent-system-design-patterns)
  Current comparison of an LLM with a prompt, deterministic chains, single-agent systems, and multi-agent systems. Use for application design and tool-ordering objectives.
- [Improve RAG chain quality](https://docs.databricks.com/aws/en/agents/tutorials/ai-cookbook/quality-rag-chain)
  Official breakdown of query understanding, retrieval, prompt augmentation, generation, and post-processing. Use for RAG chain and prompt-context objectives.
- [Databricks AI Search](https://docs.databricks.com/aws/en/ai-search/ai-search)
  Current product overview for the feature called Vector Search in the March guide. Use for retrieval, index, filtering, hybrid search, and reranking objectives.
- [June 2026 Databricks release notes](https://docs.databricks.com/aws/en/release-notes/product/2026/june)
  Primary evidence that Vector Search was renamed Databricks AI Search on June 1, 2026.
- [Databricks Academy](https://customer-academy.databricks.com/learn)
  Sign-in portal. Search for the four self-paced course titles named in the exam guide and for “Generative AI Engineering with Databricks.”
- [Genie Agents concepts](https://docs.databricks.com/aws/en/genie-agents/concepts)
  Current terminology, response generation, semantic context, supported structured data, and the split between compute identity and data identity. Use for Genie Agent architecture and governance questions.
- [Use the Genie Agents API](https://docs.databricks.com/aws/en/genie-agents/conversation-api)
  Current API guidance, including Chat mode versus Agent mode, polling, session boundaries, authentication, and conversation cleanup. Use for integration and lifecycle questions.
- [Genie API reference](https://docs.databricks.com/api/genie/v1/genie-start-conversation)
  Exact Chat mode endpoints, message statuses, response attachments, and identifiers. Use when code or a scenario depends on API mechanics.
- [Build a multi-agent system on Databricks Apps](https://docs.databricks.com/aws/en/agents/custom-agents/multi-agent-apps)
  Current custom-orchestrator pattern in which a Genie Agent is a structured-data subagent reached through the built-in Databricks MCP server. Use for managed-versus-custom orchestration decisions.
- [Configure authorization in a Databricks app](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/auth)
  Official distinction between app authorization and on-behalf-of-user authorization. Use when a Genie integration must preserve each caller's Unity Catalog policies.
- [Service policies for AI securables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/service-policies/)
  Current service-policy scope, enforcement phases, built-in guardrails, decisions, and beta limits. Use for runtime guardrail questions.
- [Create and attach a service policy](https://docs.databricks.com/aws/en/data-governance/unity-catalog/service-policies/create-service-policy)
  Policy-function shape, permissions, attachment workflow, and verification. Use for implementation questions.
- [Tracing overview](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/overview)
  What MLflow Tracing records and how traces support debugging and monitoring.
- [Core concepts for agent observability](https://docs.databricks.com/aws/en/mlflow3/genai/concepts/core-concepts)
  Distinguishes traces and spans from scorers, evaluation runs, and production monitoring.
- [Unity Gateway observability](https://docs.databricks.com/aws/en/ai-gateway/observability)
  Distinguishes gateway usage tables and inference tables from application-level MLflow traces.
- [Create AI Search endpoints and indexes](https://docs.databricks.com/aws/en/ai-search/create-ai-search)
  Section 4 source for Delta Sync versus Direct Vector Access, continuous versus triggered updates, and endpoint requirements.
- [Query an AI Search index](https://docs.databricks.com/aws/en/ai-search/query-ai-search)
  SDK, REST, and SQL query paths, including hybrid search and index permissions.
- [Deploy Python code with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/deploy-custom-python-code)
  Custom MLflow pyfunc packaging with preprocessing, postprocessing, and serving dependencies.
- [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle)
  MLflow model registration, three-level names, and model signatures.
- [Migrate an agent from Model Serving to Databricks Apps](https://docs.databricks.com/aws/en/agents/custom-agents/migrate-agent-to-apps)
  Current guidance for choosing an app or a Model Serving deployment for an agent.
- [Agent memory and sessions](https://docs.databricks.com/aws/en/agents/custom-agents/stateful-agents)
  Current distinction between persistent conversation state and cross-conversation memory.
- [Use prompts in deployed applications](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/use-prompts-in-deployed-apps)
  Prompt Registry versions and aliases for deployment promotion.
- [Use MCP servers in agents](https://docs.databricks.com/aws/en/agents/mcp-tools/use-mcp-in-agents)
  Current managed, external, and custom MCP integration paths.
- [Use `ai_query`](https://docs.databricks.com/aws/en/large-language-models/ai-query)
  Current decision guidance, supported model types, production batch practices, and examples for the general-purpose AI Function.
- [`ai_query` function reference](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_query)
  Exact requirements, request shapes, return types, model parameters, structured output, and row-level error behavior.
- [Deploy batch inference pipelines](https://docs.databricks.com/aws/en/large-language-models/batch-inference-pipelines)
  Lakeflow, scheduled workflow, and Structured Streaming patterns for production inference pipelines.
- [Databricks managed MCP servers](https://docs.databricks.com/aws/en/agents/mcp-tools/managed-mcp)
  Current managed-server list, use cases, URL patterns, and OAuth scopes.
- [Register an external MCP server](https://docs.databricks.com/aws/en/ai-gateway/register-mcp-service)
  MCP Service registration, Unity Catalog connections, credentials, grants, and network requirements.
- [Host your own MCP server](https://docs.databricks.com/aws/en/agents/mcp-tools/custom-mcp)
  Custom MCP hosting in Databricks Apps and the HTTP transport requirement.
- [Govern an MCP Service](https://docs.databricks.com/aws/en/ai-gateway/govern-mcp-service)
  Tool selection, service policies, network controls, privileges, rate limits, usage, and audit records.
- [CI/CD on Databricks](https://docs.databricks.com/aws/en/dev-tools/ci-cd)
  Git, tests, and Declarative Automation Bundles for releases.

## Gaps

- The Academy catalog is sign-in gated, so the current availability and exact Academy URLs for the guide's course titles were not independently confirmed on September 23, 2026. This does not block the study plan because the learner has completed the recommended courses and the exam guide defines the scope.

## Wisdom

- No community sources are included because the learner asked for official Databricks sources only.
