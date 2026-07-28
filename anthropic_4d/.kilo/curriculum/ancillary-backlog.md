# Ancillary Backlog

> Topics beyond the 6-month core track, grouped by priority. Each includes prerequisites, suggested resources, and estimated effort.

---

## High Priority

### C — Cost Modeling
Cloud cost is an architect accountability. Your cost modeling is untouched, but FinOps (L) also ranks High — they pair together.

| Field | Detail |
|---|---|
| Prerequisites | Phase 1 NFRs, Well-Architected Cost pillar reading (already in Phase 1) |
| Resources | AWS Well-Architected Cost Pillar whitepaper, AWS Pricing Calculator, *Cloud FinOps* (O'Reilly), re:Invent cost optimization talks |
| Estimated effort | 15–20h |
| Suggested timing | After Phase 3 (when trade-off analysis is comfortable) |

### H — Domain-Driven Design
Directly relevant to your monolith → microservices migration and domain repo split. Bounded contexts map directly to service boundaries.

| Field | Detail |
|---|---|
| Prerequisites | Phase 2 patterns (DDIA + Building Microservices) |
| Resources | "Domain-Driven Design" — Eric Evans (tackle selected chapters), "Implementing Domain-Driven Design" — Vaughn Vernon, tactical patterns quick ref online |
| Estimated effort | 25–35h |
| Suggested timing | After Phase 2 (patterns phase), can run alongside Phase 3 |

### I — CI/CD Pipeline Design
You use CI/CD but don't own the pipeline. An architect should be able to design the full deploy strategy.

| Field | Detail |
|---|---|
| Prerequisites | Terraform comfort (already 3/5), some Phase 1 networking |
| Resources | "Continuous Delivery" — Humble & Farley (classic), Bitbucket Pipelines + CodePipeline docs, GitHub Actions examples for comparison |
| Estimated effort | 10–15h |
| Suggested timing | Anytime after Phase 1, or as a practical thread during Phase 3 |

### J — API Design & Contract Testing
Your services communicate via gRPC and HTTP. Defining contracts and testing them is architect-level scope.

| Field | Detail |
|---|---|
| Prerequisites | Phase 2 distributed systems fundamentals |
| Resources | "API Design Patterns" — JJ Geewax (gRPC focus), "RESTful Web APIs" — Richardson & Amundsen, contract testing with Pact / Sandbox |
| Estimated effort | 15–20h |
| Suggested timing | After Phase 2, relevant to your production system now |

### L — FinOps
Extends cost modeling (C). Cloud cost governance at org level.

| Field | Detail |
|---|---|
| Prerequisites | Cost Modeling (C) first, Well-Architected Cost pillar |
| Resources | *Cloud FinOps* (O'Reilly), AWS Cost Explorer, Budgets, Trusted Advisor, re:Invent FinOps talks |
| Estimated effort | 15–20h |
| Suggested timing | After Phase 3 |

---

## Medium Priority

### D — Disaster Recovery
RTO/RPO design, backup strategies, multi-region considerations.

| Field | Detail |
|---|---|
| Prerequisites | Phase 1 networking + Phase 3 resilience patterns |
| Resources | AWS Well-Architected Reliability Pillar, AWS DR whitepaper, re:Invent DR sessions |
| Estimated effort | 10–15h |

### E — Resilience Patterns (deep dive)
Bulkhead, circuit breaker, chaos engineering. Phase 3 covers the basics; this adds depth with practice.

| Field | Detail |
|---|---|
| Prerequisites | Phase 3 circuit breaker / bulkhead intro |
| Resources | Chaos Engineering (Principles of Chaos), AWS Fault Injection Simulator, resilience testing workshops |
| Estimated effort | 10–15h |

### G — Kubernetes / EKS
Industry standard. Not in your stack, but most architect roles expect awareness.

| Field | Detail |
|---|---|
| Prerequisites | Phase 1 networking (K8s networking is complex without fundamentals) |
| Resources | "Kubernetes in Action" — Marko Luksa, EKS Workshop (catalog.workshops.aws), CKAD prep materials for learning structure |
| Estimated effort | 30–40h (significant — K8s is a deep topic) |

### M — SRE Practices
SLIs/SLOs, error budgets, on-call maturity. Directly relevant as you build on-call rotas.

| Field | Detail |
|---|---|
| Prerequisites | Phase 3 observability upgrade |
| Resources | "Site Reliability Engineering" — Google (free online), "The SRE Book" chapters on SLIs/SLOs, Error Budgets |
| Estimated effort | 15–20h |

---

## Low Priority

### A — RFC Authorship
Natural extension of ADR work. The influence strand in phases 4–5 already builds this muscle.

### B — Stakeholder Defense
Covered in Phase 4 influence strand depth. No separate deep dive needed unless you want formal training.

### F — Compliance / Localization
Triggered by UK/EU expansion timeline. Do this when it becomes a concrete blocker, not before. GDPR / PCI-DSS / local regulations.

### K — Data Engineering / Analytics
Card transaction analytics is relevant but not urgent for an architect role. Pick up when the team needs it.

---

## Suggested Extension Schedule (Post-6-Month)

| Window | Topic(s) | Hours |
|---|---|---|
| Month 7–8 | DDD (H) + Cost Modeling (C) | 50h |
| Month 8–9 | CI/CD (I) + API Design (J) | 30h |
| Month 9–10 | FinOps (L) + DR (D) + Resilience (E) | 40h |
| Month 10–12 | K8s (G) + SRE (M) + Compliance (F) if triggered | 60h |
