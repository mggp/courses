# Study Plan — Meta Plan

> Companion to `groundwork.md`. Defines tasks to produce the study plan,
> including which parts need human judgment, which parts benefit from AI,
> and where collaboration has the most impact.
>
> **Output structure**: All concrete artifacts are written to `.kilo/curriculum/`. See file tree at end.

---

## Phase 0 — Foundation & Context

### Task 1 — Inventory current knowledge

Map existing AWS services used, decisions participated in, current confidence levels per competency area.

| Dimension | Ownership |
|---|---|
| **Human-only** | Honest self-assessment, surfacing tacit knowledge ("I just knew which service to pick"). No one else can do this. |
| **AI leverage** | Structured interview prompts, competency checklists, gap-probing questions (e.g. "Have you modelled cost across 3 AZs?"). |
| **Collaboration impact** | **High** — AI acts as structured interviewer, human provides raw material. Produces a more thorough inventory with less blind-spot risk. |

### Task 2 — Map the production system

Document the available production system's architecture, upcoming roadmap decisions, and spheres of influence.

| Dimension | Ownership |
|---|---|
| **Human-only** | Deep context about the specific org, team dynamics, political landscape, what is actually buildable. Proprietary knowledge of the codebase and stakeholders. |
| **AI leverage** | Suggest diagramming formats (C4, 4+1), produce structured templates for documenting current architecture, identify common decision patterns from descriptions. |
| **Collaboration impact** | **Medium** — AI organizes output, but most value comes from the human's institutional knowledge. |

### Task 3 — Identify the gap

Cross-reference current knowledge against Cloud/Infra Architect competencies. Produce gap matrix.

| Dimension | Ownership |
|---|---|
| **Human-only** | Judging which gaps are actually career-limiting vs nice-to-have. Calibrating against real job market and personal context. |
| **AI leverage** | Access to architect role competencies (TOGAF, AWS SA Framework, industry standards). AI produces a comprehensive reference competency model. |
| **Collaboration impact** | **High** — human provides context and judgment, AI provides comprehensive reference model. Both needed for a gap analysis worth acting on. |

**Output**: Gap matrix incorporated into `.kilo/curriculum/00-validation-matrix.md`.

### Task 3.5 — Resource research

Identify books, courses, articles, AWS workshops, and practice labs covering: architecture fundamentals, broad patterns (event-driven, microservices, CQRS, Saga, etc.), influence-without-authority / RFC culture, cost/reliability/security fundamentals, and ADR practice.

| Dimension | Ownership |
|---|---|
| **Human-only** | Knowing which learning formats actually work for them (books vs video vs hands-on). Filtering by relevance to their specific context. |
| **AI leverage** | Generate ranked recommendations with rationale, time estimates, free vs paid tags. Cross-reference against architect competency frameworks. |
| **Collaboration impact** | **High** — AI produces breadth and structured comparisons; human curates based on personal learning style and schedule constraints. |

**Output**: `.kilo/curriculum/resources.md`

---

## Phase 1 — Structure Design

### Task 4 — Design 6-phase breakdown with ADR tier progression

Each phase targets a specific ADR tier, with a dedicated foundations phase and a combined buffer/capstone phase:

- Phase 1: **Foundations** — architectural fundamentals, quality attributes, trade-off analysis methods, ADR format introduction (pre-Tier 0)
- Phase 2: **Patterns** — Tier 0–1 ADRs (format practice, experiment with data-gathering methodology)
- Phase 3: **Trade-offs** — Tier 2 ADRs (2-way door, trade-off analysis)
- Phase 4: **Influence** — Tier 2 ADRs (deeper trade-offs, multiple options, stakeholder defense)
- Phase 5: **Capstone** — Tier 3 ADRs (1-way door, cost/risk/mitigation, real ADR on production system)
- Phase 6: **Buffer Finale** — absorbs overruns from prior phases; completes capstone artifact and written case study

All phases must define three cross-cutting dimensions:

- **Influence-without-authority strand**: a continuous thread across all phases. Each phase specifies an explicit influence skill exercised (e.g., RFC writing, cost/risk framing, stakeholder defense). Phase 4 serves as the dedicated depth phase for this strand.
- **Deferral markers**: per-phase specification of what to drop if time runs short, so scope can be shed locally without cascading delay.
- **Buffer allocation**: explicit schedule capacity designed into the phase architecture, not left to later scheduling decisions.

| Dimension | Ownership |
|---|---|
| **Human-only** | Taste for what is motivating, realistic pacing given life constraints, knowing how hard is "hard enough" to grow but not stall. Feels the span of attention. |
| **AI leverage** | Suggest phase structures informed by learning science, scaffold ADR tier descriptions into concrete exercises, generate examples at each tier, design influence skill progressions across phases, and produce deferral-marker templates that allow local scope shedding. |
| **Collaboration impact** | **Very high** — human sets the strategic shape and pacing intuition, AI fleshes out details and checks for pedagogical soundness. |

**Output**: `.kilo/curriculum/01-phase-architecture.md`

### Task 5 — Design ancillary backlog

Separate track of topics beyond 6 months, categorized and prioritized, with extension schedule.

| Dimension | Ownership |
|---|---|
| **Human-only** | Knowing which tangential topics are actually career-relevant vs interesting-but-irrelevant. Time valuation. |
| **AI leverage** | Brainstorm comprehensive topic lists from architect competency frameworks, categorize and suggest dependencies. |
| **Collaboration impact** | **Medium** — human filters, AI generates breadth. |

**Output**: `.kilo/curriculum/ancillary-backlog.md`

### Task 6 — Design dual proof-mode system

Templates for: **Lead mode** (real ADR on production system) and **Contribute mode** (case study ADR with full trade-off analysis). Define when each mode activates. Each phase template must include an **Influence component** section specifying what "influence without authority" skill is exercised in that phase.

| Dimension | Ownership |
|---|---|
| **Human-only** | Designing something that actually feels safe to use when sidelined. Psychological safety considerations. Knowing what "good enough" evidence looks like for a real hiring manager. |
| **AI leverage** | Produce ADR template drafts, trade-off analysis frameworks, rubric drafts, case study outlines. Generate counterexample scenarios for robustness. |
| **Collaboration impact** | **Very high** — templates are tedious to draft alone but require human taste to be useful. |

**Output**: `.kilo/curriculum/case-study-template.md`

### Task 7 — Design ADR practice structure per tier

For each tier: define AI-simulated challenge format, what "defended" looks like, and artifact standard.

- **Tier 1** — AI challenges methodology and data-gathering plan, and probes clarity of written communication.
- **Tier 2** — AI probes reversibility, trade-offs, alternative options, and the strength of stakeholder argumentation.
- **Tier 3** — AI argues "this is permanent — show cost, risk, mitigation," and presses on how the decision would be defended to non-technical stakeholders.

| Dimension | Ownership |
|---|---|
| **Human-only** | Designing realistic scenarios that feel like the real org culture. Knowing which challenges are actually hard vs arbitrarily hard. |
| **AI leverage** | Acts as the simulated challenger — methodology critic (Tier 1), reversibility prober (Tier 2), permanent-cost arguer (Tier 3). Generates specific architecture scenarios on demand, pushes back with consistency. |
| **Collaboration impact** | **Maximal** — this is the core of the plan. AI is the practice partner (stakeholder simulator, design reviewer), human designs the progression and brings real scenarios. The AI sparring partner is what makes the plan self-validating without a certification. |

---

## Phase 2 — Schedule & Validation

### Task 8 — Design self-validating checkpoints

Per phase: what "ready to defend this ADR tier" looks like. ADR review gates, mock defense criteria, written artifact standards.

| Dimension | Ownership |
|---|---|
| **Human-only** | Knowing what actually signals readiness to *them*, not a generic standard. Designing gates that feel earned, not academic. |
| **AI leverage** | Suggest checkpoint formats (mock ADR defenses, design reviews, peer feedback frameworks), produce rubrics with specific criteria per tier. |
| **Collaboration impact** | **High** — checkpoint design benefits from AI's ability to exhaustively list criteria and the human's ability to pick the ones that matter. |

**Output**: Checkpoint gates incorporated into `.kilo/curriculum/00-validation-matrix.md`.

### Task 9 — Build weekly schedule

Map 6 phases to weeks (~24 weeks). Include buffer, ADR writing blocks, AI challenge sessions, case study blocks. The buffer from Phase 6 combined with per-phase deferral markers must guarantee the 24-week trajectory is resilient to diversions.

| Dimension | Ownership |
|---|---|
| **Human-only** | Knowing their actual available time, energy patterns, diversions. Honest calibration on what "6 months" means in practice. |
| **AI leverage** | Template schedules, dependency ordering, progressive difficulty curves, ensure buffers are spaced appropriately. Optimize for consistency. |
| **Collaboration impact** | **Medium** — schedule is mostly owned by the human's reality; AI helps avoid common pacing mistakes. |

### Task 10 — Add specialization pivot compatibility

Verify Cloud/Infra → Solutions/Technical pivot does not invalidate any phase or checkpoint.

| Dimension | Ownership |
|---|---|
| **Human-only** | Knowing which direction actually fits their career preferences and local market. |
| **AI leverage** | Map each ADR tier exercise to multiple role contexts, identify where scope shifts, produce alternate forks. |
| **Collaboration impact** | **Medium** — AI provides the mapping exhaustively, human decides which fork to keep. |

---

## Phase 3 — Compilation

### Task 11 — Write the study plan document

Single actionable document with next-action instructions. Compiles output of all prior tasks.

| Dimension | Ownership |
|---|---|
| **Human-only** | Voice, prioritization of what to emphasize, making it motivating. Only the human knows what format they will actually follow and use. |
| **AI leverage** | Produce first draft from all prior outputs, format consistently, ensure no gaps. Format as markdown, Notion template, or other format on request. |
| **Collaboration impact** | **Very high** — AI does the heavy drafting, human edits for voice and usability. |

**Output**: `.kilo/curriculum/02-phase-1-foundations.md` through `.kilo/curriculum/07-phase-6-buffer-finale.md`

### Task 12 — Review against groundwork constraints

Verify final plan satisfies every constraint in `groundwork.md` (dual-track, buffer, influence without authority, self-validating, pivot-compatible, etc.).

| Dimension | Ownership |
|---|---|
| **Human-only** | Spotting when a constraint is technically met but does not *feel* met. Judging whether the plan will actually be followed. |
| **AI leverage** | Exhaustive cross-reference of every constraint to plan sections, flag gaps mechanically. AI will not miss a line item. |
| **Collaboration impact** | **High** — AI catches mechanical gaps, human catches substantive ones. |

**Output**: Updated `00-validation-matrix.md` with completion status.

---

## File tree (final output)

```
.kilo/curriculum/
├── 00-validation-matrix.md        ← Tasks 3, 8, 12 (gaps + checkpoints + validation)
├── 01-phase-architecture.md       ← Task 4 (phase breakdown)
├── 02-phase-1-foundations.md      ← Task 11
├── 03-phase-2-patterns.md         ← Task 11
├── 04-phase-3-tradeoffs.md        ← Task 11
├── 05-phase-4-influence.md        ← Task 11
├── 06-phase-5-capstone.md         ← Task 11
├── 07-phase-6-buffer-finale.md    ← Task 11
├── resources.md                   ← Task 3.5 (resource research)
├── case-study-template.md         ← Task 6 (dual proof-mode)
└── ancillary-backlog.md           ← Task 5 (ancillary topics)
```

## Execution order

Tasks are grouped by phase and should be executed sequentially within each phase.
- **Phase 0** (Tasks 1, 2, 3, 3.5): sequential — each builds on the previous.
- **Phase 1** (Tasks 4, 5, 6, 7): sequential; Task 3.5 (resources) can run in parallel with Task 4.
- **Phase 2** (Tasks 8, 9, 10): sequential; depends on Phase 1 outputs.
- **Phase 3** (Tasks 11, 12): sequential; Task 12 is the final validation pass.

---

## Delegation pattern summary

| AI strengths → | Human strengths → |
|---|---|
| Exhaustive generation & checklists | Self-awareness & institutional context |
| Consistent probing & drilling | Taste & pacing intuition |
| Template & rubric drafting | Psychological safety judgment |
| Reference knowledge (frameworks) | Real-world calibration |
| Mechanical gap detection | Motivational voice & prioritization |
