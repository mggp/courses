# Case Study & ADR Templates

> Dual proof-mode system: **Lead mode** (real-time decision capture) and **Contribute mode** (retrospective case study for portfolio evidence). Use Lead mode when you own the design. Use Contribute mode when the decision was made by others and you need to demonstrate your analysis.

---

## Lead Mode — ADR Template (Decision Capture)

Use this when you are actively participating in or driving a real architecture decision on your production system. Capture at decision time.

```markdown
# ADR-{NNN}: {Title}

## Context
{What system, what team, what problem. Enough for an outsider to understand the landscape.}

## Constraints
{Hard boundaries: time, budget, compliance, existing commitments, irreversible prior decisions.}

## Options Considered
- **Option A**: {Brief description. Why was it viable?}
- **Option B**: {Brief description. Why was it viable?}
- **Option C**: {Brief description. Why was it viable?}

## Trade-off Analysis
| Attribute | Option A | Option B | Option C |
|---|---|---|---|
| {Attribute 1} | | | |
| {Attribute 2} | | | |
| {Attribute 3} | | | |

*Attributes: cost, latency, durability, operational complexity, team familiarity, scalability, security, etc.*

## Decision
**Chosen**: Option {X}

{Who decided? Architect lead, team consensus, stakeholder directive?}

## Rationale
{Why this option won despite its trade-offs. Which attribute was weighted most heavily and why.}
```

---

## Contribute Mode — Case Study Template (Portfolio Artifact)

Use this when the design/decision was made by others, or when you want to document past work for your portfolio. Take the available information and reconstruct the decision process retrospectively.

```markdown
# Architecture Case Study: {Title}

## Context
{What system, what team, what problem. Same as ADR but with more narrative — background, history, why this decision mattered.}

## Constraints
{Hard boundaries that shaped the decision.}

## Options Considered
- **Option A**: {Description, viability, who advocated for it}
- **Option B**: {Description, viability, who advocated for it}
- **Option C**: {Description, viability, who advocated for it}

## Trade-off Analysis
| Attribute | Option A | Option B | Option C |
|---|---|---|---|
| {Attribute 1} | | | |
| {Attribute 2} | | | |
| {Attribute 3} | | | |

{Free-text explanation of the trade-off reasoning.}

## Decision
**Chosen**: Option {X}

{Who decided and how? Was there conflict? How was it resolved?}

## Rationale
{Why this option won despite its trade-offs.}

## Outcome
{What happened after implementation. Did it work as expected? What surprised you? Metrics if available.}

## Lessons
{What you would do differently. What you learned about the system, the team, or the domain. What signals to watch for next time.}
```

---

## ADR Format Reference (Both Modes)

| Element | Purpose | Required in Lead? | Required in Contribute? |
|---|---|---|---|
| Context | Landscape for an outsider | Yes | Yes |
| Constraints | Hard boundaries | Yes | Yes |
| Options | ≥2 distinct alternatives | Yes | Yes |
| Trade-off Analysis | Structured comparison | Yes | Yes |
| Decision | The chosen path | Yes | Yes |
| Rationale | Why it won | Yes | Yes |
| Outcome | Post-hoc results | No | Yes |
| Lessons | Retrospective learning | No | Yes |

---

## Tier Reference

Use this to calibrate the depth of your ADR:

| Tier | Decision Type | Expected Depth | When Used |
|---|---|---|---|
| 0 | Trivial / obvious | Context + Decision only | Phase 1 practice |
| 1 | Reversible, low impact | + Rationale | Phase 2 (first real ADR) |
| 2 | Reversible, moderate impact | + Options + Trade-off Analysis | Phases 3–4 |
| 3 | Irreversible, high impact | + Cost/Risk/Mitigation section | Phase 5 (Capstone) |

### Tier 3 Addendum (Cost / Risk / Mitigation)

For Tier 3 ADRs, add this section after Rationale:

```markdown
## Cost / Risk / Mitigation

### Cost Impact
{Estimate. One-time vs recurring. Direct vs indirect.}

### Risks
{Risks of the chosen option. What could go wrong.}

### Mitigations
{What's in place or planned to address each risk.}

### Reversibility
{Why this is or is not reversible. If irreversible, what's the rollback plan?}
```
