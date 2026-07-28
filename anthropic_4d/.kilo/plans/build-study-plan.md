# Build the Study Plan — Meta-Plan

**Goal**: Produce a structured, multi-file study plan at `.kilo/curriculum/` that satisfies all constraints in `groundwork.md`.

**Inputs from user**:
- Format: multiple Markdown files
- Core focus: broader architecture patterns + fundamentals (cross-cloud)
- AWS-specific depth → post-6-month ancillary backlog
- Pace: 10–15 hrs/wk
- Resources: plan recommends everything

---

## Tasks

### Task 1 — Requirements distillation
Review `groundwork.md` and extract a structured checklist that every phase must satisfy. Produce a single validation matrix.

**Output**: `.kilo/curriculum/00-validation-matrix.md`
- Maps each groundwork constraint to which phase(s) satisfy it
- Defines the "ready to defend" gate criteria for each phase

---

### Task 2 — Phase architecture design
Design the 6-month core track breakdown and the ancillary backlog structure.

**Output**: `.kilo/curriculum/01-phase-architecture.md`
- Number of phases (6 months ÷ ~monthly phases = 5–6 phases, each 4–5 weeks at 10–15 hrs/wk = ~50–75 hrs total per phase — calibrate)
- Dual-track per phase: **Lead mode** (real work design) and **Contribute mode** (case study)
- Buffer phase(s) and deferral markers
- Capstone definition (phase 5 or 6)
- Influence-without-authority strand woven through phases

---

### Task 3 — Resource research
Identify the best books, courses, articles, AWS workshops, and practice labs that cover:
- Architecture fundamentals (trade-off analysis, design patterns, quality attributes)
- Broad architecture patterns (event-driven, microservices, CQRS, Saga, transactional outbox, Strangler Fig, etc.)
- "Influence without authority" / technical writing / RFC culture
- Cost, reliability, security fundamentals (not deep — that's ancillary)
- Architecture decision records (ADRs)

**Output**: `.kilo/curriculum/resources.md`
- Ranked recommendations with rationale
- Time estimates per resource
- Free vs paid tags

---

### Task 4 — Write phase documents
For each phase, create a dedicated Markdown file:

Structure per phase:
1. **Theme & objective** — what architectural capability this phase builds
2. **Duration** — weeks, total hours
3. **Learning topics** — bullet list with resource references
4. **Lead mode deliverable** — real work output (RFC written, design defended, ADR authored)
5. **Contribute mode deliverable** — case study artifact produced
6. **Influence component** — what "influence without authority" skill is exercised
7. **Checkpoint gate** — what "ready to defend" looks like
8. **Deferral marker** — what to drop if time runs short

**Outputs**:
- `.kilo/curriculum/02-phase-1-foundations.md`
- `.kilo/curriculum/03-phase-2-patterns.md`
- `.kilo/curriculum/04-phase-3-tradeoffs.md`
- `.kilo/curriculum/05-phase-4-influence.md`
- `.kilo/curriculum/06-phase-5-capstone.md`
- `.kilo/curriculum/07-phase-6-buffer-finale.md`

---

### Task 5 — Define the case study template
Design the reusable case study document template that the learner fills in during Contribute mode.

**Output**: `.kilo/curriculum/case-study-template.md`
- Sections: Context → Constraints → Options considered → Trade-off analysis → Decision → Rationale → Outcome → Lessons
- ADR format reference
- Example from a public architecture (e.g., AWS Well-Architected lens case study)

---

### Task 6 — Ancillary backlog
Organize the topics explicitly deferred beyond 6 months.

**Output**: `.kilo/curriculum/ancillary-backlog.md`
- Grouped by topic area (multi-account, resilience, cost, security, migration, etc.)
- Each entry: prerequisite, suggested resource, estimated effort
- Mark which user already has baseline exposure to

---

### Task 7 — Validation & self-review
Cross-check the full output against the validation matrix from Task 1. Verify:
- Every constraint from `groundwork.md` is met
- Every phase has a demonstrable output
- Buffer/deferral mechanism works
- Dual-track is consistent throughout
- Timeline adds up to ~6 months × 10–15 hrs/wk = ~260–390 hrs total

**Output**: Updated `00-validation-matrix.md` with completion status.

---

## File tree (final)

```
.kilo/curriculum/
├── 00-validation-matrix.md
├── 01-phase-architecture.md
├── 02-phase-1-foundations.md
├── 03-phase-2-patterns.md
├── 04-phase-3-tradeoffs.md
├── 05-phase-4-influence.md
├── 06-phase-5-capstone.md
├── 07-phase-6-buffer-finale.md
├── resources.md
├── case-study-template.md
└── ancillary-backlog.md
```

## Execution order

Tasks 1–2 are sequential (design before writing). Tasks 3 can run in parallel with Task 2. Tasks 4 depends on Tasks 2–3. Task 5 depends on Task 4 (shape emerges from phase design). Tasks 6–7 can run after Tasks 3–4.
