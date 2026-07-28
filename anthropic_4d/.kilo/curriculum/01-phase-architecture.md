# Phase Architecture

> 6 months × 10–15 hrs/wk = ~260–390 hrs total.
> **Hard ceiling: 360 hrs (24 weeks × 15 hrs).** If a phase exceeds ~70 hrs (~4.5 weeks), content is deferred to ancillary.

---

## Phase Budget Overview

| Phase | Theme | Est. Hours | Weeks (at 12h/wk) | ADR Tier |
|---|---|---|---|---|
| 1 | Foundations | 60 | 5 | Pre-Tier 0 |
| 2 | Patterns | 55 | 4–5 | Tier 0–1 |
| 3 | Trade-offs | 50 | 4 | Tier 2 |
| 4 | Influence | 45 | 4 | Tier 2 |
| 5 | Capstone | 50 | 4 | Tier 3 |
| 6 | Buffer Finale | 40 | 3–4 | Complete |
| **Total** | | **300** | **24** | |

Each phase includes:
- **Influence strand** — continuous thread across all phases
- **Deferral markers** — what to drop if time runs short
- **Buffer allocation** — slack to absorb diversions

---

## Phase 1 — Foundations (~60 hrs)

**Objective**: Build fundamental architecture vocabulary and decision-making methodology. Address the highest-priority gaps (networking, security) at a basics level.

### Topics & Time Allocation

| Topic | Hours | Resources |
|---|---|---|
| Quality attributes & NFRs | 10 | *Software Architecture in Practice* Ch. 4, ISO 25010, Well-Architected intro |
| ADR format & examples | 4 | ADR GitHub org, Nygard article, Spotify/AWS examples |
| Trade-off analysis intro | 6 | ATAM overview, *Design It!* selected chapters |
| Networking fundamentals | 12 | AWS VPC workshop (VPCs, subnets, NAT, SGs, NACLs) |
| IAM & Security basics | 8 | AWS Security workshop (IAM policies, roles, KMS basics) |
| Write practice ADRs (x2) | 8 | Two pre-Tier 0 ADRs on made-up scenarios |
| Weekly review / flex | 12 | Buffer within phase |
| **Total** | **60** | |

### Deferral Markers
- Drop IAM/Security workshop → replace with docs-only reading (−4h)
- Drop one practice ADR (−4h)
- Skip ATAM deep dive, keep just the concept (−3h)

### Influence Strand
- **Skill**: Writing for an audience. Practice ADRs must be written for a technical lead who has no context.
- **Exercise**: After each practice ADR, write a 3-sentence executive summary for a non-technical stakeholder.

---

## Phase 2 — Patterns (~55 hrs)

**Objective**: Learn the core architecture patterns you need for daily design work. Write your first real ADR on the production system.

### Topics & Time Allocation

| Topic | Hours | Resources |
|---|---|---|
| Distributed systems fundamentals | 25 | *Designing Data-Intensive Applications* (all core chapters) |
| Microservices patterns | 10 | *Building Microservices* selected chapters + microservices.io |
| Event-driven patterns | 5 | AWS EDA whitepaper, SQS/SNS deep dive |
| Strangler Fig pattern | 3 | Fowler article, relate to your monolith migration |
| Write Tier 0–1 ADR | 8 | Real ADR on your production system (simple decision) |
| Weekly review / flex | 4 | Buffer |
| **Total** | **55** | |

### Deferral Markers
- Skip *Building Microservices* → use microservices.io catalog only (−6h)
- Drop event-driven deep dive (−5h)
- Defer one DDI-A chapter (replication) to Phase 6 (−4h)

### Influence Strand
- **Skill**: Methodology defense. In your ADR, include a data-gathering plan. Defend it in writing: "Why this data, why not that data."
- **Exercise**: Peer review another ADR (real or example) — practice giving feedback on decision methodology.

---

## Phase 3 — Trade-offs (~50 hrs)

**Objective**: Learn intermediate patterns (CQRS, Outbox, Saga, Circuit Breaker). Write a Tier 2 ADR that compares multiple options with trade-off analysis.

### Topics & Time Allocation

| Topic | Hours | Resources |
|---|---|---|
| CQRS / Event Sourcing | 8 | DDI-A chapters (if deferred from P2), microservices.io |
| Transactional Outbox | 4 | Richardson article, DynamoDB Streams implementation |
| Sagas (choreography vs orchestration) | 6 | Fowler + microservices.io, relate to your vendor orchestration |
| Circuit Breaker / Bulkhead | 4 | Fowler article, resilience patterns |
| Observability upgrade | 6 | AWS Observability workshop (X-Ray, alerting) |
| Write Tier 2 ADR | 12 | Real ADR on production system with ≥2 options, trade-off matrix |
| Weekly review / flex | 10 | Buffer |
| **Total** | **50** | |

### Deferral Markers
- Drop observability workshop → use docs only (−4h)
- Drop Event Sourcing deep dive → keep CQRS only (−4h)
- Write ADR with 2 options instead of 3 (−2h)

### Influence Strand
- **Skill**: Trade-off communication. Your Tier 2 ADR must include a "trade-offs at a glance" table. Write a 1-page summary for a team lead who disagrees with your choice.
- **Exercise**: Role-play a 5-minute verbal defense of your ADR to a skeptical peer.

---

## Phase 4 — Influence (~45 hrs)

**Objective**: Deepen the influence-without-authority strand. Write a Tier 2 ADR focused on stakeholder argumentation.

### Topics & Time Allocation

| Topic | Hours | Resources |
|---|---|---|
| Influence Without Authority book | 10 | Cohen & Bradford |
| RFC / technical writing patterns | 6 | Calcado RFC article, Amazon 6-pager examples |
| Stakeholder argumentation | 6 | *Articulating Design Decisions* selected chapters |
| Cost / risk framing | 4 | Well-Architected Cost pillar, basic cost modeling |
| Write Tier 2 Influencer ADR | 12 | ADR on production system with cost/risk analysis, stakeholder Q&A prep |
| Verbal defense practice | 4 | Write Q&A script, practice aloud |
| Weekly review / flex | 3 | Buffer |
| **Total** | **45** | |

### Deferral Markers
- Drop *Influence Without Authority* book → use article summaries only (−5h)
- Drop cost modeling → keep conceptual (−4h)
- Skip verbal defense practice → keep written only (−4h)

### Influence Strand
- **Skill**: Stakeholder persuasion. This phase is the depth phase for the influence strand. ADR must address "who cares about this decision and why."
- **Exercise**: Write a mock Slack message / email to a non-technical stakeholder explaining your ADR in 5 sentences.

---

## Phase 5 — Capstone (~50 hrs)

**Objective**: Produce the final proof artifact — a Tier 3 ADR on your production system (Lead mode) and/or a complete written case study (Contribute mode).

### Topics & Time Allocation

| Topic | Hours | Resources |
|---|---|---|
| Tier 3 ADR methodology | 4 | Review irreversible decision patterns, cost/risk/mitigation |
| Real ADR on production system | 16 | Own the design, document all options, write the ADR |
| Case study write-up | 16 | Full context → trade-off → decision → outcome document |
| Written defense prep | 6 | Prepare for mock defense interview |
| Weekly review / flex | 8 | Buffer |
| **Total** | **50** | |

### Deferral Markers
- Case study: reduce depth (1-page summary instead of full document) (−10h)
- Skip written defense prep (−6h)
- Narrow ADR scope to a single decision (−4h)

### Influence Strand
- **Skill**: Multi-audience communication. Same decision — explain it to: (a) engineering team, (b) product manager, (c) CTO. Three different documents.
- **Exercise**: Write all three versions.

---

## Phase 6 — Buffer Finale (~40 hrs)

**Objective**: Absorb overruns from phases 1–5. Complete any unfinished artifact. Polish the case study.

### Topics & Time Allocation

| Topic | Hours | Notes |
|---|---|---|
| Overrun absorption | 16 | Draw from per-phase deferral markers as needed |
| Capstone completion | 12 | Finish any incomplete ADR / case study sections |
| Full plan retrospective | 6 | What worked, what didn't, what's next |
| Ancillary backlog triage | 6 | Prioritize post-6-month learning |
| **Total** | **40** | Can shrink to 20h if unused |

### Deferral Markers
- The whole phase is a deferral sink. See per-phase markers above.

### Influence Strand
- **Skill**: Retrospective communication. Produce a "learning summary" that could go in a portfolio or performance review.
- **Exercise**: Write a 2-page narrative: "What I learned as an architect in 6 months."

---

## Weekly Schedule

> Week-by-week buckets at ~12h/wk average. AI challenge sessions are integrated as sparring blocks. Flex hours absorb diversions without breaking the trajectory.

### Phase 1 — Foundations (Weeks 1–5)

| Week | Focus | Activities | Hours |
|---|---|---|---|
| 1 | NFRs & Quality Attributes | Read *Software Architecture in Practice* Ch. 4 + ISO 25010. Read Well-Architected intro (all 6 pillars skim). Write down NFRs for your own system. | 12 |
| 2 | ADR Format + Trade-off Intro | Read Nygard article + ADR examples. Read *Design It!* trade-off chapters. AI spar: format review only. | 12 |
| 3 | Networking Workshop | AWS VPC workshop (hands-on). VPCs, subnets, NAT, SGs, NACLs end-to-end. | 12 |
| 4 | Security Workshop | AWS Security workshop (hands-on). IAM policies, roles, KMS basics. | 12 |
| 5 | Practice ADRs + Close | Write 2 practice ADRs (generic scenarios). Executive summaries for each. AI spar: format review. Flex: catch any overflow. | 12 |

### Phase 2 — Patterns (Weeks 6–10)

| Week | Focus | Activities | Hours |
|---|---|---|---|
| 6 | DDI-A Part 1 | Read DDI-A Ch. 1–5 (reliability, replication, partitioning). Take notes on concepts that connect to your system. | 12 |
| 7 | DDI-A Part 2 | Read DDI-A Ch. 6–10 (transactions, CQRS intro, batch/stream). | 12 |
| 8 | Microservices Patterns | Read *Building Microservices* selected chapters + microservices.io catalog. Map each pattern to your system (yes/no/partial). | 11 |
| 9 | Event-Driven + Strangler Fig | AWS EDA whitepaper. Fowler Strangler Fig article. Write ADR context + options. | 10 |
| 10 | Write ADR + AI Challenge | Complete Tier 0–1 ADR. AI spar: methodology probing. Flex: catch overflow. | 10 |

### Phase 3 — Trade-offs (Weeks 11–14)

| Week | Focus | Activities | Hours |
|---|---|---|---|
| 11 | CQRS + Outbox | Read DDI-A CQRS/event sourcing sections. Richardson Outbox article. DynamoDB Streams patterns. | 12 |
| 12 | Sagas + Resilience | Fowler Saga article + choreography vs orchestration. Circuit breaker + bulkhead patterns. Relate to your vendor orchestration. | 12 |
| 13 | Observability Workshop | AWS Observability workshop (X-Ray, OpenTelemetry, alerting). | 12 |
| 14 | Write ADR + AI Challenge | Complete Tier 2 ADR with trade-off matrix. AI spar: reversibility + alternatives probing. Flex. | 14 |

### Phase 4 — Influence (Weeks 15–18)

| Week | Focus | Activities | Hours |
|---|---|---|---|
| 15 | Influence Theory | Read *Influence Without Authority*. Read Calcado RFC article + Amazon 6-pager examples. | 12 |
| 16 | Stakeholder Communication | Read *Articulating Design Decisions* selected chapters. Write a mock RFC. | 12 |
| 17 | Cost/Risk Framing | Well-Architected Cost pillar. Write ADR context + options with cost estimates. | 11 |
| 18 | Complete ADR + AI Challenge | Finish Tier 2 influencer ADR. Write multi-audience summaries. AI spar: stakeholder argumentation. Flex. | 10 |

### Phase 5 — Capstone (Weeks 19–22)

| Week | Focus | Activities | Hours |
|---|---|---|---|
| 19 | Tier 3 Prep + Start ADR | Read cost/risk/mitigation patterns. Start real Tier 3 ADR on production system. Define options and constraints. | 12 |
| 20 | Complete ADR | Finish Tier 3 ADR with full cost/risk/mitigation section. Write eng / PM / CTO summaries. | 13 |
| 21 | Case Study Write-up | Document Contribute-mode case study from ADR. Full Context → Constraints → Options → Trade-off → Decision → Outcome → Lessons. | 13 |
| 22 | Defense Questionnaire + Polish | AI spar: Tier 3 questionnaire (≥5 answers). Polish ADR and case study. Flex. | 12 |

### Phase 6 — Buffer Finale (Weeks 23–24)

| Week | Focus | Activities | Hours |
|---|---|---|---|
| 23 | Overrun Absorption | Draw from per-phase deferral markers. Complete any unfinished ADR or case study sections. | 14 |
| 24 | Retrospective + Polish | Write learning narrative ("What I learned as an architect in 6 months"). Triage ancillary backlog for post-6mo. Polish portfolio artifacts. | 12 |

---

### AI Challenge Session Summary

| Phase | Tier | Session Type | Hours |
|---|---|---|---|
| 1 | Pre-T0 | Format review | 1 |
| 2 | T0–1 | Methodology probing | 2 |
| 3 | T2 | Reversibility + alternatives | 2 |
| 4 | T2 | Stakeholder argumentation | 2 |
| 5 | T3 | Permanent decision questionnaire | 2 |
| **Total** | | | **9** |

---

### Deferral Decision Tree

If a phase runs over its allocated weeks:

```
Phase running over?
├── Yes → Apply deferral markers in listed order
│   ├── Still over? → Move overflow to Phase 6 buffer
│   │   ├── Phase 6 also full? → Shed lowest-priority content permanently
│   │   └── Phase 6 has space → Absorbed without trajectory impact
│   └── Not over → Continue normally
└── No → Continue normally
```

---

## Buffer Strategy (Across All Phases)

Each phase has ~10–20% internal buffer. Phase 6 adds an additional 40h as a global overflow. Combined with per-phase deferral markers, this guarantees resilience:

> Worst case: every phase sheds its deferrable content → total ~220h core. Phase 6 buffer absorbs the remaining delta, keeping the 24-week trajectory intact.

---

## Summary (Influence Strand Across Phases)

| Phase | Influence Skill | Medium |
|---|---|---|
| 1 | Writing for an audience | Practice ADRs + executive summaries |
| 2 | Methodology defense | ADR data-gathering rationale |
| 3 | Trade-off communication | At-a-glance trade-off table + verbal practice |
| 4 | Stakeholder persuasion | Multi-audience ADR + cost/risk framing |
| 5 | Multi-audience communication | Same decision → eng / PM / CTO versions |
| 6 | Retrospective communication | Learning narrative for portfolio |
