# Phase 2 — Patterns

> Learn the core architecture patterns you need for daily design work. Write your first real ADR on the production system.

## Duration

**5 weeks / ~55 hours** (11h/wk average)

## Weekly Breakdown

### Week 6 — DDI-A Part 1
- Read *Designing Data-Intensive Applications* Ch. 1–5 (reliability, replication, partitioning)
- For each chapter: write down 1–2 sentences connecting the concept to your production system
- **Exercise**: Identify which replication and partitioning strategies your system uses (or should use). Map DynamoDB partitioning, Valkey replication, etc.
- **Hours**: 12

### Week 7 — DDI-A Part 2
- Read DDI-A Ch. 6–10 (transactions, batch processing, stream processing, CQRS intro)
- **Exercise**: Write a half-page analysis — does your credit application flow need transactions? Where are the consistency boundaries?
- **Hours**: 12

### Week 8 — Microservices Patterns
- Read *Building Microservices* (Newman) selected chapters — service boundaries, decomposition, integration, testing
- Browse microservices.io catalog — identify 5+ patterns relevant to your system
- **Exercise**: Map microservices patterns to your system with a simple table: Pattern → Applied where? → Not yet but could?
- **Hours**: 11

### Week 9 — Event-Driven + Strangler Fig
- Read AWS EDA whitepaper (event-driven patterns with EventBridge, SQS, SNS)
- Read Martin Fowler's Strangler Fig article
- Relate Strangler Fig to your monolith migration
- Start writing Tier 0–1 ADR for a real production decision (write Context + Constraints + Options)
- **Hours**: 10 (5h reading + 5h ADR start)

### Week 10 — Write ADR + AI Challenge
- Complete Tier 0–1 ADR (add Decision + Rationale)
- **AI session (2h)**: Methodology probing — AI asks "How did you gather data?" "Are you missing options?" "Who should have been consulted?"
- Revise ADR based on challenge
- **Exercise**: Peer review a sample ADR — practice giving feedback on decision methodology
- **Hours**: 10 (6h write + 2h AI + 2h flex)

## Lead Mode Deliverable
1 real Tier 0–1 ADR on your production system — a decision you participated in, documented in ADR format.

## Contribute Mode Deliverable
Same ADR, but written from the perspective of observing someone else's decision. Fill in the context and rationale as if you were reconstructing it.

## Influence Component
Methodology defense — your ADR includes a data-gathering plan section. Defend it in writing: "Why this data, why not that data."

## Checkpoint Gate
Authored a real Tier 0–1 ADR on your production system. Can defend methodology choices to AI probing.

## Deferral Markers
- Skip *Building Microservices* → use microservices.io catalog only (−6h)
- Drop event-driven deep read → skim whitepaper (−5h)
- Defer DDI-A Ch. 9–10 to Phase 6 (−4h)
- Final fallback: Week 10 flex absorbs up to 2h
