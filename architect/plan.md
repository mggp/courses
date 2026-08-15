# Software Architect Learning Plan

> Companion to `software-architect-goal-groundwork.md`. The groundwork locks the
> goal and constraints; this document is the plan. Phases below are **derived from
> the competency gap map and its dependency analysis** (Section 2), not asserted.
>
> **Core track:** ~6 months of *available* effort (not calendar), externally
> anchored to the project due date. **Ancillary track:** explicit backlog
> (Section 6) for post-6-month extension.

---

## 1. Baseline (from groundwork)

Experienced dev, ~1yr AWS, has made real infra decisions (ECS vs Lambda, logs vs
metrics, queues vs topics, sync vs async), with IaC/deploy/monitoring exposure,
single-team scope. Org uses **ADRs** classified as De facto / Experiment /
2-way door / 1-way door.

---

## 0. Gap-validation diagnostic (run BEFORE the Enabler)

The gap map in Section 2 must be **measured, not assumed**. This diagnostic runs
first so the phase sequence reflects reality rather than inference.

**Method:**
1. Pick one real production workflow you know well.
2. Walk it through one probe per gap dimension; for each, keep going until you
   hit the edge of your knowledge:
   - **G6 ADR:** classify it and draft the ADR skeleton.
   - **G1 cross-service:** map the services and their trade-offs.
   - **G2 cost:** estimate the design's cost and a cost trade-off.
   - **G3 reliability:** state SLOs / failure modes / error budgets.
   - **G4 org-wide:** identify cross-team impacts and ownership.
   - **G5 influence:** defend a recommended option to a skeptical AI panel.
3. AI acts as the probing panel, pushing each probe until you stall.
4. Mark each dimension **Evidenced / Partial / Gap** at the point you stopped.

**Output:** a measured gap map → becomes Section 2. If the result re-orders the
dependencies, re-sort the phases. The Enabler→G1→(G2,G3)→G4→Capstone skeleton
is *conditional on this result*, not fixed.

**Guardrail:** do not skip. A confident-but-wrong gap map is worse than none.

---

## 2. Competency gap map (measured output of Step 0)

*Framework below; the Evidenced/Gap ratings are populated by Step 0. Shown here
as the working template — pending the diagnostic, treat all ratings as
provisional.*

Evidenced capabilities (levers to build on):
- **E1** single-service infra decisions
- **E2** IaC / deploy / monitoring

Gap capabilities (target architect scope):
- **G1** cross-service trade-off reasoning
- **G2** cost modeling & framing
- **G3** reliability / SLO thinking
- **G4** org-wide / cross-team patterns
- **G5** influence without authority (practice)
- **G6** ADR authoring (format)

**Dependency edges (these determine phase order):**
- **G6** is a *prerequisite enabler* — you cannot defend anything without the
  artifact. Short enabler phase, precedes all.
- **G5** is a *cross-cutting practice track*, not a phase. It runs across every
  phase as an escalating ADR-defense tier (Tier 0→3).
- **G1** builds directly on **E1** (single-service → cross-service). First real
  architectural reasoning cap. → **Phase 1**.
- **G2** and **G3** are *analysis lenses* applied to a design; both depend on
  having a design (**G1**). Independent of each other → order interchangeable.
  → **Phases 2 and 3**.
- **G4** is the broadest scope; needs **G1+G2+G3**. → **Phase 4**.
- **Capstone** synthesizes all into one 1-way-door artifact. → **Phase 5**.

This dependency chain *is* the phase plan. No phase was chosen independently of
the gap map.

---

## 3. The plan — phases (derived)

Each phase: **Outcome gate** (capability, not content), **Gap addressed**,
**Lead path**, **Contribute fallback**, **Influence track** (ADR tier),
**Buffer** (core vs stretch/deferrable), **Checkpoint**, **Real-work anchor**.
Dual-track and pivot tolerance are global (Sections 5–6).

### Enabler — ADR mechanics & classification (G6)
- **Gate:** Author a correct ADR in each class; classify any decision correctly.
- **Gap:** ADR format + classification fluency.
- **Lead:** Write a real De-facto/Experiment ADR at work if opportunity arises.
- **Contribute:** Author all four class examples on the production system regardless.
- **Influence:** Tier 0 (format only) — not a capability gate.
- **Buffer:** Core = 4 class examples. Stretch = re-cast a past real decision as an ADR.
- **Checkpoint:** *"Can you classify any decision and draft its ADR unaided?"*
- **Anchor:** Map the four known real decisions onto the classification system.

### Phase 1 — Cross-Service Design & Trade-offs (G1, builds on E1)
- **Gate:** Design one real production workflow spanning ≥3 AWS services with explicit trade-offs defended.
- **Gap:** Single-decision → cross-service reasoning.
- **Lead:** Own the design on the real system; circulate as an ADR.
- **Contribute:** If sidelined, write full ADR + trade-off analysis as case-study material.
- **Influence:** **Tier 2 (2-way-door)** ADR; AI panel red-teams; defend live.
- **Buffer:** Core = 3 services + trade-offs. Stretch = add cost model. Deferrable if diverted.
- **Checkpoint:** *"Passed a simulated 2-way-door ADR defense without notes; recommended option intact."* (transcript)
- **Anchor:** Tied to the live production system; pivot-safe.

### Phase 2 — Cost Lens (G2)
- **Gate:** Propose a cost model for a real component and defend a cost trade-off.
- **Gap:** No cost-anchored decisions yet.
- **Lead:** Drive a cost conversation on the real system.
- **Contribute:** Author the cost ADR + trade-off analysis regardless.
- **Influence:** Tier 2 (2-way-door) ADR on a cost trade-off.
- **Buffer:** Core = one cost model + defense. Stretch = multi-component model. Deferrable.
- **Checkpoint:** *"Passed a simulated 2-way-door cost-defense without notes."*
- **Anchor:** Real component on the production system.

### Phase 3 — Reliability & SLO Lens (G3)
- **Gate:** Propose SLOs/error budgets for a real component; defend reliability-vs-cost.
- **Gap:** Monitoring exists; SLOs/error budgets not owned.
- **Lead:** Drive an SLO conversation on the real system.
- **Contribute:** Author the SLO ADR + trade-off analysis regardless.
- **Influence:** Tier 2 (2-way-door) ADR on an SLO-vs-cost trade-off.
- **Buffer:** Core = SLOs + one defense. Stretch = error-budget policy. Deferrable.
- **Checkpoint:** *"Passed a simulated 2-way-door SLO-vs-cost defense without notes."*
- **Anchor:** Real component on the production system.

### Phase 4 — Org-wide Patterns (G4, needs P1–P3)
- **Gate:** Defend a cross-team pattern proposal at 1-way-door difficulty.
- **Gap:** Single-team → org-wide scope.
- **Lead:** Circulate a real cross-team ADR.
- **Contribute:** Author the org-wide ADR + trade-off analysis regardless.
- **Influence:** **Tier 3 (1-way-door)** simulated defense; AI panel at max skepticism.
- **Buffer:** Core = one 1-way-door defense passed. Stretch = two. Deferrable.
- **Checkpoint:** *"Passed a simulated 1-way-door ADR defense; recommended option survived."*
- **Anchor:** Pattern applicable across the production system's teams.

### Phase 5 — Capstone (synthesis)
- **Gate:** Real-work **1-way-door ADR** (min. 2-way) designed + defended + written case study.
- **Gap:** Synthesizes G1–G5 into one defensible artifact.
- **Lead:** Own and defend the design at work.
- **Contribute:** Written case study guaranteed even if others implement.
- **Influence:** Final Tier 3 defense; case-study draft reviewed by AI panel.
- **Buffer:** Core = ADR + case study. Stretch = internal publish/present.
- **Checkpoint:** *"Capstone ADR at 1-way-door class defended (real or simulated); case study complete + self-validated."*
- **Anchor:** The production system; externally anchored to the project due date.

---

## 4. Proof artifacts & dual-proof (Task 2)

- **Success metric:** proven capability — design and defend a real system end-to-end. No certification.
- **Lead-mode proof:** a real production-system design you own and defend at work.
- **Contribute-mode proof (guaranteed fallback):** written ADR + trade-off analysis + simulated-defense transcript, produced even when sidelined.
- **Capstone artifact:** one real-work **1-way-door ADR** (minimum 2-way) plus a written case study. A De facto ADR as capstone is excluded — it proves nothing.
- **"Defended" defined:** attend (real or simulated) with a *recommended option* and survive adversarial questioning without notes.

---

## 5. Influence track — Mock ADR defense protocol (G5, cross-cutting)

You don't attend the real meetings yet, so AI plays the review panel using the
org's classification rules. This makes the track **authority-independent** and
always ships an artifact.

**Escalating tier (laid across Phases 1–5):**
- **Tier 0 — De facto:** format only; not a gate.
- **Tier 1 — Experiment:** defend the data-gathering plan; AI challenges methodology.
- **Tier 2 — 2-way door:** attend (simulated) with a recommended option; AI probes reversibility/trade-offs. (Phases 1–3)
- **Tier 3 — 1-way door:** irreversible; AI argues "permanent — show cost, risk, mitigation." (Phases 4–5)

**Per-rep cycle:** write ADR (with recommended option) → AI panel red-teams through
the class lens → defend live → checkpoint. Transcript + ADR feed the case study.

---

## 6. Dual-track & pivot tolerance (global)

- **Core (≤6 months available effort):** Step 0 (diagnostic) + Enabler + Phases 1–5. Role-readiness track.
- **Ancillary backlog (post-6-month):** formal frameworks (TOGAF/C4), multi-region
  DR, capacity/load modeling, org review-process study, external portfolio.
  Pulled forward only if core gates are met early.
- **Pivot tolerance:** No phase assumes a fixed specialization. Cross-service,
  cost/reliability, and influence reps apply equally to Cloud/Infra, Solutions,
  and Technical paths. A mid-plan pivot only shifts the capstone's framing.

---

## 7. Self-validating checkpoints (Task 7)

No certification exists, so each gate is self-administered with explicit pass
criteria; AI acts as the unbiased gatekeeper (compensates for self-bias).

| Phase | Pass criterion |
| --- | --- |
| Enabler | Classify any decision + draft its ADR unaided |
| 1 | Simulated 2-way-door defense passed without notes; option intact |
| 2 | Simulated 2-way-door cost-defense passed without notes |
| 3 | Simulated 2-way-door SLO-vs-cost defense passed without notes |
| 4 | Simulated 1-way-door defense passed; option survived |
| 5 | Capstone 1-way-door ADR defended; case study complete + self-validated |

Format: yes/no + evidence (ADR + transcript). A "no" consumes buffer, not abandons the plan.

---

## 8. Open questions / assumptions

- **Step 0 diagnostic not yet run** — Section 2 ratings are provisional until then.
- Concrete project due date anchoring Phase 5?
- How frequently do diversions typically occur (calibrates buffer sizing)?
- Who, if anyone, reviews the real-work ADR/case study for external validation?
- Which existing production workflow to use for Step 0 (and Phases 1–3)?

*These refine pacing; they do not block planning.*
