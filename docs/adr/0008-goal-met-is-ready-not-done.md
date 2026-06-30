---
status: accepted
date: 2026-06-30
---

# 0008 — `goal_met` is "ready for adjudication", not "done"

## Context and Problem Statement

Agents reviewing drafts inline report that `goal_met` "never flips," and chase the flag
as if it were a terminal done-signal. The behavior was checked against the code
(`scripts/orchestrator.py`).

## Decision

**Keep the semantics; document them at the point of use.** `goal_met` returns true only
when a finished draft still sits in `status="draft"` (≥1 pending), nothing is processable,
the phase is `synthesize`, and no dimension candidate is accept-eligible:

```python
goal_met = (recommend_phase(...) == "synthesize"
            and not _processable(...)
            and len(list_drafts(status="draft")) >= 1
            and not accept_eligible(...))
```

So `goal_met` is a **"the engine has drained its autonomous work and handed a draft to the
human review queue"** signal — exactly the locked decision in the convergence design
(`docs/superpowers/specs/2026-06-20-loop-engine-convergence-design.md` §2: "done-check cannot
require promoted findings"). Promotion is a human gate; the loop in `skills/_flows/goal.md`
stops on `goal_met` and leaves the draft for a human to adjudicate later — it does **not**
adjudicate inline, so it observes the flag correctly.

An agent that promotes/rejects the last draft *inline* removes the `status="draft"`
precondition, so `goal_met` goes false and `recommend_phase` falls back to `gather`. That is
correct, not a bug. **Real convergence = no queued gaps + not processable + drafts
adjudicated.** Do not poll `goal_met` while reviewing inline.

## Consequences

- `goal_met` stays as-is; the invariant is now stated in its docstring and here.
- `tests/test_orchestrator.py` pins it: true with a pending draft + nothing processable, false
  the instant that draft is promoted — a future refactor cannot silently turn it into a
  naive done-flag.
- Related: ADR 0007 (queue-depth candidate selection; 1–2-source topics stranded by design).
