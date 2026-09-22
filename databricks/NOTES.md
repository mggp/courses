# Teaching notes

- The learner is preparing for the Databricks Certified Generative AI Engineer Associate exam described by the March 18, 2026 guide.
- Use only current Databricks product names and behaviors. Preserve older guide terms only when needed to recognize exam wording, and label the mapping.
- Ground key claims in `docs.databricks.com` or Databricks Academy. Link the source next to the claim.
- If an official source does not confirm a claim, say so.
- Do not add study objectives beyond the guide.
- The learner has completed all five Databricks Academy courses recommended by the March 18, 2026 exam guide. Treat this as broad prior exposure, not proof of mastery.
- Prefer exam-style retrieval, scenario discrimination, and targeted remediation over introductory course summaries.

## Canonical product terms

Verified against current documentation on September 23, 2026. Use the canonical terms in new material. Keep a guide term only when mapping the wording a learner may see on the March 18, 2026 exam.

| Guide or legacy wording | Canonical term | Use it this way |
| --- | --- | --- |
| Vector Search, Mosaic AI Vector Search, Vector Search index | [Databricks AI Search](https://docs.databricks.com/aws/en/ai-search/ai-search), AI Search index | Databricks AI Search is the current product name. “Vector search” remains a lower-case retrieval technique. Say “standard AI Search endpoint” or “storage-optimized AI Search endpoint,” not a Vector Search endpoint. |
| Model Serving, model serving endpoint | [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving), model serving endpoint | The current docs use this shorter name. An agent deployed through the legacy serving path is an agent on a Model Serving endpoint. |
| Mosaic AI Agent endpoint | [agent endpoint](https://docs.databricks.com/aws/en/agents/custom-agents/query-agent) or Model Serving endpoint | “Agent endpoint” is used for an Agent Bricks agent. For a custom agent, name the deployment target precisely: a Databricks App or a Model Serving endpoint. |
| Foundation Model APIs | [Databricks Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis) | Use the full product name on first mention. |
| `ai_query()` | [`ai_query` AI Function](https://docs.databricks.com/aws/en/machine-learning/model-inference) | The function identifier is `ai_query`; parentheses belong only in code that calls it. |
| AI Gateway, Inference Tables, Usage Tables | [Unity Gateway](https://docs.databricks.com/aws/en/ai-gateway), [inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables-beta), usage tracking tables | Unity Gateway is the current governance product. Its usage data is in governed system tables, including `system.ai_gateway.usage`; do not treat “Usage Tables” as a standalone product. |
| Agent Bricks Multiagent Supervisor | [Agent Bricks Supervisor Agent](https://docs.databricks.com/aws/en/agents/agent-bricks/multi-agent-supervisor) | “Multiagent Supervisor” was renamed to “Supervisor Agent.” |
| Agent Bricks, Knowledge Assistant, Information Extraction | [Agent Bricks](https://docs.databricks.com/aws/en/agents/agent-bricks/info-extraction), Knowledge Assistant, Information Extraction | These are still the current names. Capitalize Agent Bricks and the named capabilities. |
| Agent Framework | [Mosaic AI Agent Framework](https://docs.databricks.com/aws/en/release-notes/product/2025/march) | Use the full product name on first mention, then “Agent Framework” is fine. |
| Agent Monitoring | [MLflow production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) | Use this for scheduled MLflow scorers over production traces. Inference tables track endpoint requests and responses, which is a different mechanism. |
| MLflow scoring and tracing, Databricks custom Scorers | [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/concepts/core-concepts), MLflow Evaluation, and [MLflow scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/manage-production-scorers) | “Databricks custom Scorers” means custom MLflow scorers. Use lower-case “scorers” unless it starts a heading or sentence. |
| prompt version control, prompts as MLflow versions | [MLflow Prompt Registry](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/) | This is the named facility for registered, versioned prompts and aliases. |
| Genie Spaces, conversational API | [Genie space](https://docs.databricks.com/api/genie/v1/genie-space), Genie Agent, Genie Conversation API | Use “Genie space” in the singular and “Genie spaces” in the plural. A Genie Agent is the current agent integration built around a configured Genie space. |
| managed, external, and custom MCP servers | [Model Context Protocol (MCP)](https://docs.databricks.com/aws/en/agents/agent-framework/agent-tool), Databricks managed MCP server, external MCP server, custom MCP server | “MCP Service” is the Unity Gateway securable for a registered external server. It is not a synonym for every MCP server. |
| managed web browser MCP server | No current product with this name | Current [Databricks managed MCP servers](https://docs.databricks.com/aws/en/agents/mcp-tools/managed-mcp) cover Genie, AI Search, and Databricks SQL. Do not turn this distractor into a product name. |
| Apps, Databricks App | [Databricks Apps](https://docs.databricks.com/aws/en/dev-tools/databricks-apps), Databricks app | Use the plural product name and the lower-case singular for one app. |
| feature store table | [Databricks Feature Store](https://docs.databricks.com/aws/en/machine-learning/feature-store) feature table | A “feature table” is the current object name. For governed data, say “feature table in Unity Catalog.” |
| Databricks Secrets | [Databricks secrets](https://docs.databricks.com/aws/en/security/secrets), secret scope | “Secrets” is not a product proper name. A secret scope contains secrets. |
| GTE Large | [GTE-Large](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints) | Preserve the hyphen in the model name. |

The following names are still current and need no mapping: **MLflow**, **Unity Catalog**, **Delta Lake**, **LangChain**, **Hugging Face Transformers**, **Slack**, and **Microsoft Teams**. The guide’s “Langchain” spelling is wrong. The Python package identifiers in its OCR question are `beautifulsoup4`, `scrapy`, `pytesseract`, and `pyquery`; these are package names, not Databricks products.
