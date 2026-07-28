# ADR Practice Structure per Tier

> Defines AI-simulated challenge format, what "defended" looks like, and artifact standards at each tier. This reference is embedded in each phase document and used during AI sparring sessions.

---

## Tier 0 — Trivial / Obvious

**Purpose**: Practice the ADR format without any real pressure. Build the habit of writing decisions down.

**AI Challenge Format**: None. AI reviews format only.
- Is the ADR using the correct template structure?
- Is Context clear enough for an outsider?
- Is the Decision unambiguous?

**What "Defended" Looks Like**: Writing 2 practice ADRs that follow the template correctly. No probing questions.

**Example Scenarios**:
- "Why host this static site on S3+CloudFront vs a single EC2 instance?"
- "Why host your API behind a load balancer vs pointing DNS directly at the server?"
- Use your own production decisions when comfortable — the format is the point.

---

## Tier 0 ADR Example

```markdown
# ADR-001: Static site hosting approach

## Context
A marketing landing page with minimal dynamic content. Team has AWS experience.
No requirement for server-side rendering or complex routing.

## Decision
Host on S3 with CloudFront CDN.

## Rationale
Zero servers to manage, pay-per-request pricing, built-in CDN for global latency,
easy to roll back via S3 versioning. Meets all requirements with lowest operational cost.
```

---

## Tier 1 — Reversible, Low Impact

**Purpose**: Write a real ADR on your production system. Practice writing for clarity.

**AI Challenge Format**: AI challenges the **methodology** and **data-gathering plan**.
- "How did you gather the data to support this decision?"
- "Are you missing any options?"
- "Can you explain [term/concept] in simpler terms?"
- "Who else should have been consulted?"

**What "Defended" Looks Like**: Being able to answer each AI question with a coherent written response or revision to the ADR.

**Example Scenarios**:
- Should user session data be stored in a cache (Redis/Valkey) or a database (DynamoDB)?
- Should a recurring job be scheduled (cron-triggered Lambda) or event-driven (SQS + consumer)?
- Should service-to-service auth use API keys or mutual TLS?
- Use your own production decisions — the tier means the decision should be reversible and low-risk.

---

## Tier 2 — Reversible, Moderate Impact

**Purpose**: Compare multiple options with structured trade-off analysis. Demonstrate you can weigh competing attributes.

**AI Challenge Format**: AI probes **reversibility**, **trade-offs**, **alternatives**, and **stakeholder argumentation**.
- "What's the rollback plan if this doesn't work?"
- "You ranked latency higher than cost. Who disagrees and why?"
- "What third option did you dismiss too quickly?"
- "If your team lead demands the other option, how do you respond?"
- "What attribute weight did you assign and why?"

**What "Defended" Looks Like**: A completed trade-off matrix with ≥3 attributes, ≥2 options, and a written rationale that survives AI probing without significant revision.

**Example Scenarios**:
- Should the notification service use SQS + Lambda or EventBridge + Step Functions?
- CQRS with separate read/write stores vs single database with indexes?
- Monorepo vs multi-repo: what boundaries define the split?
- Database table design — single table with composite keys vs multiple normalized tables?
- Use your own production decisions — the tier means the decision should be reversible with moderate impact.

---

## Tier 3 — Irreversible, High Impact

**Purpose**: Handle irreversible decisions with cost, risk, and mitigation analysis. This is capstone-level.

**AI Challenge Format**: AI plays the role of a **decision reviewer** who pushes on permanence.
- "This is permanent. Show your cost estimate across 12 and 36 months."
- "What's the single point of failure in your design?"
- "How would you defend this to a non-technical CTO?"
- "What data would you collect over the next 3 months to validate this was the right call?"
- "If this decision is wrong, what's the cost of reversing it?"
- "What compliance or regulatory boundary does this touch?"

**What "Defended" Looks Like**: Passing a **questionnaire** — written answers to ≥5 probing counterarguments from the AI. No oral defense required. The questionnaire response is appended to the ADR.

**Example Scenarios**:
- Choose a message broker for a new platform that must handle high throughput with strong durability guarantees.
- Database migration strategy — cutover approach, rollback plan, data integrity verification.
- Service boundary redesign — should two domains share a service or be split?
- Adopting a new infrastructure component that changes how multiple services communicate.
- Use your own production decisions — the tier means the decision is irreversible or very high impact.

---

## Challenge Flow Summary

| Tier | AI Role | Probing Dimension | Passing Criterion |
|---|---|---|---|
| 0 | Format reviewer | Template compliance | 2 practice ADRs written |
| 1 | Methodology critic | Data gathering, completeness | Written response to each question |
| 2 | Trade-off prober | Reversibility, attributes, alternatives | Trade-off matrix + survives probing |
| 3 | Decision reviewer | Cost, risk, mitigation, permanence | Questionnaire (≥5 answers) appended to ADR |

## Example Tier 3 Questionnaire Entry

```markdown
## Defense Questionnaire

**Q1: This is permanent. Show your cost estimate across 12 and 36 months.**
A: [Answer]

**Q2: What's the single point of failure in your design?**
A: [Answer]

**Q3: How would you defend this to a non-technical CTO?**
A: [Answer]

**Q4: What data would you collect over the next 3 months to validate this call?**
A: [Answer]

**Q5: What is the cost of reversing this decision?**
A: [Answer]

**Q6: What compliance boundary does this touch?**
A: [Answer]
```
