# Validation Matrix

> Gap analysis, checkpoint gates, pivot analysis, and constraint cross-reference for the 6-month study plan.

---

## 1. Gap Matrix

### Must-have (core 6-month track)

| Competency Area | Current Level | Target | Priority |
|---|---|---|---|
| Cloud Compute | ECS(4), Lambda(3) | Architect-level multi-service design | High |
| Cloud Networking | VPC/subnets/SGs all (1) | Design secure, scalable networks | High |
| Cloud Storage/DB | DynamoDB(4), but S3(2), Aurora(1) | Storage strategy across services | High |
| Cloud Security/IAM | IAM(2), KMS(1), SecretsManager(2) | Least-privilege, encryption patterns | High |
| Messaging/Events | SQS(3), SNS(2), Event-Driven(1) | Event-driven architecture design | High |
| Observability | Grafana(3), Metrics(3), Logs(2), X-Ray(1) | Distributed tracing, alerting | High |
| Architecture Methodologies | ADRs(1), Trade-off(2), NFRs(2) | Systematic decision-making | High |
| Architecture Patterns | All untouched (CQRS, Saga, Strangler Fig, Outbox, Circuit Breaker) | Apply in real designs | High |
| ADR Authorship | Never authored | Write Tiers 0-3 ADRs | High |
| Multi-service Design | Never done | Design cross-service boundaries | High |

### Ancillary backlog (post-6mo or pull-into-core)

> Marked as **Pull** if it might be urgent enough to absorb into the 6-month track. This is for you to prioritize.

| # | Competency Area | Notes | Priority |
|---|---|---|---|
| A | RFC Authorship | Natural extension of ADR writing | Low |
| B | Stakeholder Defense | Influence strand, Phase 4 depth | Low |
| C | Cost Modeling | Can be introduced in trade-off phases | **High** |
| D | Disaster Recovery | RTO/RPO design | Medium |
| E | Resilience Patterns | Bulkhead, Chaos Engineering | Medium |
| F | Compliance / Localization | Triggered by UK/EU expansion roadmap | Low |
| G | Kubernetes / EKS | Industry standard orchestration; not in your stack | Medium |
| H | Domain-Driven Design | Bounded contexts, strategic design — relevant to monolith split | **High** |
| I | CI/CD Pipeline Design | Own the full deploy strategy, not just use it | **High** |
| J | API Design & Contract Testing | Service contracts for gRPC/HTTP services | **High** |
| K | Data Engineering / Analytics | Kinesis, Redshift, Athena for card transaction analysis | Low |
| L | FinOps | Cloud cost accountability, extends cost modeling | **High** |
| M | SRE Practices | SLIs/SLOs, error budgets — next step for your on-call rotas | Medium |

---

## 2. Checkpoint Gates

> Per phase: what "ready to defend this ADR tier" looks like. Gates are cumulative — passing Phase 3 assumes Phases 1-2 are complete.

| Phase | Gate | Evidence |
|---|---|---|
| **1 — Foundations** | Can write a correct ADR using the template. Can explain quality attributes and basic trade-off concepts. | 2 practice ADRs written (any topic). Verbal or written explanation of NFRs in your own words. |
| **2 — Patterns** | Authored a real Tier 0–1 ADR on your production system. Can defend your data-gathering methodology. | 1 real ADR (Tier 0–1). Written answers to AI methodology probes. References to at least 2 patterns from DDI-A or microservices.io. |
| **3 — Trade-offs** | Authored a Tier 2 ADR with structured trade-off analysis (≥3 attributes, ≥2 options). Survived probing on reversibility and alternatives. | 1 Tier 2 ADR with completed trade-off matrix. No significant revision needed after AI challenge. |
| **4 — Influence** | Authored a Tier 2 ADR that explicitly addresses stakeholder concerns. Can frame a decision in cost/risk terms. | 1 Tier 2 ADR with stakeholder argumentation section. Multi-audience summary (eng / PM / CTO). |
| **5 — Capstone** | Completed Tier 3 ADR with cost/risk/mitigation analysis. Passed defense questionnaire. | 1 Tier 3 ADR on production system + ≥5 written answers to decision reviewer questions. |
| **6 — Buffer Finale** | All incomplete artifacts from prior phases are complete. Case study or capstone ADR is polished and portfolio-ready. | All prior gates closed. One document ready to show a hiring manager. |

---

## 2b. Specialization Pivot Analysis

> Verifies Cloud/Infra Architect → Solutions Architect or Technical Architect pivot does not invalidate any phase or checkpoint.

### Core 6-month track — Pivot-compatible? YES

| Phase | Cloud/Infra Weight | Pivot Impact | Assessment |
|---|---|---|---|
| 1 — Foundations | Medium (networking + security workshops) | NFRs, ADRs, trade-off analysis are universal | ✅ Fully compatible |
| 2 — Patterns | Low | DDI-A, microservices, events are universal | ✅ Fully compatible |
| 3 — Trade-offs | Low | CQRS, Outbox, Sagas are universal | ✅ Fully compatible |
| 4 — Influence | Low | Stakeholder communication is MORE relevant for SA | ✅ Fully compatible |
| 5 — Capstone | Medium (AWS-specific ADR) | ADR/case study format is universal | ✅ Compatible — use any system |
| 6 — Buffer | None | Retrospective + polish, universal | ✅ Fully compatible |
| Checkpoint gates | None | All gates are format/methodology-based | ✅ Fully compatible |

### Ancillary backlog — Pivot-dependent

| Topic | Cloud/Infra | Solutions Architect | Technical Architect |
|---|---|---|---|
| Cost Modeling (C) | High | High | Medium |
| DDD (H) | Medium | Medium | **High** |
| CI/CD (I) | Medium | Low | **High** |
| API Design (J) | Medium | Medium | **High** |
| FinOps (L) | **High** | Medium | Low |
| K8s (G) | Medium | Low | Medium |
| SRE (M) | **High** | Low | Medium |

### Verdict

**No phase, checkpoint, or gate is invalidated by any pivot.** The core plan is methodology-and-pattern-focused, not tool-specific. The ancillary backlog would be reprioritized, but the 6-month trajectory stays intact.

---

## 3. Groundwork Constraints — Validation

> Cross-reference of every constraint from `groundwork.md` against the final plan.

| Constraint | Status | How It's Met |
|---|---|---|
| Outcome-anchored (not content-anchored) | ✅ Met | All phases culminate in an ADR deliverable, not course completion. Phase 5 is the capstone artifact. |
| Builds on existing AWS baseline | ✅ Met | Phase 1 uses existing ECS/DynamoDB/SQS comfort as foundation. Phases 2–3 extend with patterns, Phase 4 adds influence. |
| Resilient to non-architect work (buffers + deferrals) | ✅ Met | Per-phase deferral markers allow local scope shedding. Phase 6 absorbs global overflow. Deferral decision tree defined. See `01-phase-architecture.md`. |
| Dual proof modes (Lead + Contribute) | ✅ Met | Two templates in `case-study-template.md`. Each phase specifies both Lead and Contribute deliverables. |
| Explicit influence-without-authority competency | ✅ Met | 6-phase influence strand, each with a distinct skill and exercise. Phase 4 is the dedicated depth phase. Tracked in `01-phase-architecture.md`. |
| Capstone: real system design + case study | ✅ Met | Phase 5 produces a Tier 3 ADR (Lead mode) and a case study (Contribute mode). Phase 6 polishes both. |
| Dual-track (6mo core + ancillary backlog) | ✅ Met | Core: phases 1–6 (300h). Ancillary: 13 topics in `ancillary-backlog.md` with post-6-month extension schedule. |
| Self-validating checkpoints (no certification) | ✅ Met | Per-phase gates defined in section 2 above. Evidence is concrete ADRs, not exam scores. |
| Pivot-compatible (Cloud/Infra ↔ Solutions/Technical) | ✅ Met | Section 2b analysis confirms no phase or gate breaks. Ancillary backlog is pivot-dependent but core plan is methodology-focused. |
| Pacing: ~6 months × 10-15 hrs/wk | ✅ Met | 300h total ÷ 24 weeks = 12.5h/wk average. Within the 260–390h window. Hard ceiling: 360h at 15h/wk max. |
