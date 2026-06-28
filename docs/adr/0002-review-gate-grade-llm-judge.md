---
status: accepted
date: 2026-06-27
---

# 0002 — Ground the review gate in GRADE certainty + LLM-judge debiasing

## Context and Problem Statement

The promotion review gate was binary promote/reject on an ad-hoc rubric: it recorded *whether*
a finding was canon-worthy but not *how certain* its evidence was, and the reviewer's own
reliability was unaddressed. The corpus holds the methods that fix both: the GRADE four-level
certainty scale with its downgrade/upgrade domains (`d628b3d0f`), the
grade-reconcile-calibrate framing that flagged the engine had no explicit certainty rating
(`dc577f3e2`), and LLM-as-judge bias controls — position/verbosity/self-preference (`d4c45dd7e`).

## Decision

Rewrite `.claude/review.md` to (a) emit a GRADE certainty level alongside the verdict, with
explicit per-domain downgrades, and (b) order the reviewer's work as a debiasing control —
judge faithfulness from the source bytes *before* the draft's own confidence framing, decompose
into per-axis judgments, never reward length.

## Consequences

- Every promote now records graded confidence (`CERTAINTY:` + `VERDICT:`), so the corpus carries
  certainty, not a bare bit.
- The reviewer is treated as one judge under documented controls, not as ground truth.
- The higher bar for definitive/synthesis findings is encoded in the same gate.
