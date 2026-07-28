# Phase 3 — Trade-offs

> Learn intermediate patterns (CQRS, Outbox, Saga, Circuit Breaker). Write a Tier 2 ADR that compares multiple options with structured trade-off analysis.

## Duration

**4 weeks / ~50 hours** (12.5h/wk average)

## Weekly Breakdown

### Week 11 — CQRS + Outbox
- Read DDI-A CQRS / Event Sourcing sections (if deferred from Phase 2)
- Read Chris Richardson's Transactional Outbox article
- Read DynamoDB Streams implementation patterns
- **Exercise**: Sketch a CQRS design for one bounded context in your system. Read model vs write model — what tables, what triggers?
- **Hours**: 12

### Week 12 — Sagas + Resilience
- Read Martin Fowler's Saga article (choreography vs orchestration)
- Relate Saga patterns to your vendor orchestration flow
- Read Circuit Breaker (Fowler) and Bulkhead patterns
- **Exercise**: Map your authoring flow onto choreography vs orchestration. Which is it now? Which should it be? Why?
- **Hours**: 12

### Week 13 — Observability Workshop
- Complete AWS Observability workshop (catalog.workshops.aws/observability)
- Hands-on: X-Ray traces, OpenTelemetry sidecars, CloudWatch alarms
- **Exercise**: Design an alert for one critical path in your system. What metric? What threshold? What escalation?
- **Hours**: 12

### Week 14 — Write ADR + AI Challenge
- Write a Tier 2 ADR on a production decision: ≥2 options, ≥3 quality attributes in trade-off matrix
- **AI session (2h)**: Reversibility probing — "What's the rollback plan?" "You ranked latency over cost — who disagrees?" "What third option did you dismiss too quickly?"
- Revise ADR based on challenge
- **Exercise**: Write the "trade-offs at a glance" table and a 1-page summary for a team lead who disagrees with your choice
- **Hours**: 14 (12h write + 2h AI)

## Lead Mode Deliverable
1 Tier 2 ADR with completed trade-off matrix and written rationale that survives AI probing without significant revision.

## Contribute Mode Deliverable
Same ADR, reconstructed as a case study with explicit trade-off analysis. Include a note: "If I had chosen Option B instead, here's what would have happened."

## Influence Component
Trade-off communication — Tier 2 ADR includes an at-a-glance trade-off table. 1-page summary for a disagreeing team lead.

## Checkpoint Gate
Authored a Tier 2 ADR with structured trade-off analysis (≥3 attributes, ≥2 options). Survived AI probing on reversibility and alternatives.

## Deferral Markers
- Drop observability workshop → use docs only (−4h)
- Drop Event Sourcing deep read → keep CQRS only (−4h)
- Write ADR with 2 options instead of 3 (−2h)
- Final fallback: Week 11–12 each have 0 flex; overflow goes to Phase 6
