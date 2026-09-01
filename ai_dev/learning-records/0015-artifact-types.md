# Learning record — ten practice-artifact types (HTML-native)

The learner flagged a persistent problem: the lessons' practice artifacts close the
feedback loop too weakly. The multiple-choice quiz (assets/quiz.js) tests
*recognition* — three pre-authored equal-length answers, you pick the right one —
not *recall or production*. The exercise scripts (exercises/lessonNNNN/*.py) are
already finished: `uv run` prints output the author produced; `--query`/`--threshold`
are cosmetic knobs on a completed machine. In both, the work is done before the
learner arrives.

The unifying fix: **the learner must produce something *before* the artifact
reveals the answer, and the feedback must be specific to *their* production** —
their predicted classification, their chosen distractor, their inversion, their
missing claim.

This record proposes ten artifact types. The first five from the conversation ask
only for HTML/CSS/JS that lives inside the lesson file — no Python runtime, no
HuggingFace download, no `uv`. The second five are heavier but still in-browser,
for where a coding task is genuinely wanted. All are reusable across lessons via a
small shared script alongside the existing `quiz.js`.

## Table of artifacts

| # | Artifact | Skill it tests | How it works | When to reach for it |
|---|----------|----------------|--------------|----------------------|
| 1 | **Predict-then-compare fold** | Committing to a prediction and being caught when wrong | Show an example with the conclusion cut off behind a `details` fold. A `textarea`/input must be non-empty before the reveal opens; the reveal shows the real output next to a "what to notice" checklist. | When the lesson's point is *why an outcome happened*, not *what the outcome is* — mispredicting *which* claim is "neutral" beats picking a noun. |
| 2 | **Graded fill-in (cloze)** | Pipeline composition; the order and rationale of stages | A sentence/flow with `select` or inline blanks, each blank carrying per-distractor `data-why`. Choosing a *specific* wrong answer gets a *specific* correction ("BM25 is unbounded, cosine is [0,1]…"), not a generic "wrong." | When the point is *how pieces compose* — the next stage, the right method, the threshold's direction — not the definition of one piece. |
| 3 | **Spot-the-defect panel** | Diagnosis of a broken mechanic | A compact but incorrect `pre` snippet embedded in the lesson; select the bug from distractors, each mapping to a distinct misconception with a tailored explanation. | When the target is *recognizing and naming what's wrong* without running code — the exact inverse of the run-and-observe exercises. |
| 4 | **Rank-the-order drag** | Sequencing of stages / points / concerns | A shuffled list; move items via buttons or drag; "check" scores longest-correct-prefix and pinpoints the first inverted adjacent pair. | When order matters more than recognition (identity → network → store → evaluation → monitoring; index → recall → rerank → generate → evaluate). |
| 5 | **Explain-then-diff (interview freeze)** | Generation under pressure; concise, accurate interview answers | An interview-form question, a textarea for the learner's answer, then a reveal with a model answer and a *claim checklist* to tick against their own words. Score is manual self-diff, not automatic. | Near-term priority (MISSION.md). Any lesson whose concept must be *articulated*, not just understood — especially the cloud-gap / boundary material. |
| 6 | **Oral recall prompt** | Memory retrieval after the file is closed | A single question in interview voice; no options, no reveal until a deliberate click; a one-line model answer plus the *must-say* claims. | The close sibling of #5, when the barrier is recall rather than articulation. |
| 7 | **Ordering / sorting task** | Internal structure (efficiency, latency, cost ranking) | Drag or click-to-step a list into the correct order; feedback highlights the first inversion. | When the lesson's mechanic is a ranking concern (pool size vs latency, most-to-least risky hallucination). |
| 8 | **Matching pane** | Vocabulary-to-mechanic mapping | Match terms in one column to their definitions/roles in another; feedback per pair, not per whole. | When a lesson introduces a cluster of new terms at once (BM25, tf-idf, RRF, dense vs sparse) and the learner needs the map, not just each definition. |
| 9 | **Scenario branching (choose-your-own)** | Judgment under conditions ("if X, then what") | A decision prompt with branches; each choice leads to a consequence page rather than a right/wrong flag. | When the point is *trade-offs*, not facts — where both branches are defensible and the lesson is to show what each costs. |
| 10 | **Fill-the-spec skeleton** | The only code-like task — filling the *decision*, not the implementation | A half-written spec / pipeline with blanks for the chosen method or threshold; a `compare` button highlights differences from a canonical answer. | When a small, contained coding check is wanted but not the full take-over-home burden of editing `exercises/`. |

## Governance rules (carry forward, not re-derive)

1. **Never** test the *example* used to teach a concept — only the concept. This is
   the same bug class already flagged in notes ("which rank did p9 move to?").
2. Any artifact with hidden distractors must not leak the answer through length,
   word count, or formatting — inherit the equal-length rule from `quiz.js`.
3. Keep artifacts **browser-only** unless a coding task is genuinely the point; do
   not smuggle a Python runtime back in by default.
4. Prefer artifacts that grade **production** (prediction, sequencing, articulation)
   over **recognition**, per the learner's explicit complaint.
5. Run the same correctness discipline as `check_quiz.py`: a script should verify
   every artifact's metadata (reveal gating, distractor mapping, claim checklists)
   before a lesson ships.

## Selection guide (which of the ten, when)

- **Concept / "why"** → #1 predict-then-compare, #3 spot-the-defect
- **Composition / order** → #2 graded fill-in, #4 rank-the-order, #7 sorting
- **Vocabulary** → #8 matching, #2 fill-in
- **Articulation / interview** → #5 explain-then-diff, #6 oral recall
- **Judgment / trade-offs** → #9 scenario branching
- **A coding check is genuinely warranted** → #10 fill-the-spec (mildest) or the
  existing `exercises/` pattern (heaviest)
