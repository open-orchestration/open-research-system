# A→C Convergence Orchestrator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the loop research engine autonomously convergent — one `/goal` loop drives ingest/search/process toward a research goal and auto-selects the budget `phase` each cycle.

**Architecture:** A new pure-function module `scripts/orchestrator.py` computes, from `.research/state.json` alone, the recommended `phase` (stateless function of signals), whether the goal is met, and which flows are eligible this cycle. A new `.claude/goal.md` prompt drives one cycle — reusing the existing ingest/search/process cycles — and loops until the orchestrator reports `goal_met`. No new state schema; the auto-flip reuses the existing `phase` field and `set_phase`.

**Tech Stack:** Python 3 standard library only. Tests are `unittest`. No pip, no pytest.

## Global Constraints

- **Python 3 stdlib only** — no pip, no new dependencies. Tests are `unittest` + bash. No `# noqa` / `# type: ignore` / suppression comments anywhere — fix the code.
- **No new state schema fields.** Reuse `phase` and `state.set_phase`. The 3×3 `weights` table stays a static constant; only the active `phase` is auto-selected.
- **`scripts/orchestrator.py` reads only `.research/state.json`** (via `state.py`). No graph or other disk reads.
- **Module import convention:** `import state as state_mod` (matches `scripts/promote.py`). Tests `sys.path.insert(0, "<repo>/scripts")` then `import state as st` / `import orchestrator as orch`.
- **Commits:** Conventional Commits, selectively staged with explicit paths — **never** `git add .`/`-A`, never stage the side-effect-seeded `.research/state.json`. No co-author trailers, no "Generated with" lines.
- **Phase-independent `processable`:** the gather→deepen decision must NOT use `state.process_candidates` (it self-gates on `subagent_count(process)<=0`, always empty in `gather` — circular). Compute un-cited-per-topic directly.

---

### Task 1: `scripts/orchestrator.py` — decision module

**Files:**
- Create: `scripts/orchestrator.py`
- Test: `tests/test_orchestrator.py`

**Interfaces:**
- Consumes (from `scripts/state.py`, all existing): `load(root)`, `save(state, root)`, `load_default()`, `set_phase(state, phase)`, `list_gaps(state, topic=None, status=None)`, `list_drafts(state, status=None, topic=None)`, `_cited_ids(state, exclude_rejected=True)`, `subagent_count(state, flow)`, `process_candidates(state, min_sources=3)`, `budget_remaining_sources(state)`, `add_gap`, `add_corpus_entry`, `add_draft` (last three used by the test).
- Produces (relied on by Task 2):
  - `recommend_phase(state, min_sources=3) -> str` — one of `"gather"|"deepen"|"synthesize"`.
  - `goal_met(state, min_sources=3) -> bool`.
  - `next_actions(state, min_sources=3) -> {"search": bool, "process": bool}`.
  - `decide(state, min_sources=3, apply=False) -> {"phase": str, "phase_changed": bool, "search": bool, "process": bool, "goal_met": bool}`.
  - CLI: `python3 scripts/orchestrator.py decide --root . --min-sources 3 [--apply]` prints the `decide` dict as JSON; `--apply` saves the phase flip to `state.json`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_orchestrator.py`:

```python
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state as st
import orchestrator as orch


def _corpus(state, topic, n, start=0):
    """Add n corpus entries on `topic` with distinct sources; return their ids."""
    ids = []
    for i in range(start, start + n):
        e = st.add_corpus_entry(
            state, title=f"t{i}", source=f"http://x/{topic}/{i}",
            topic=topic, native_path="n", extracted_path="e",
        )
        ids.append(e["id"])
    return ids


class RecommendPhase(unittest.TestCase):
    def test_gather_when_nothing_processable(self):
        s = st.load_default()
        st.add_gap(s, topic="t", desc="q")          # queued gap, no corpus
        self.assertEqual(orch.recommend_phase(s), "gather")

    def test_deepen_when_processable_but_graph_dirty(self):
        s = st.load_default()
        _corpus(s, "t", 3)                           # add_corpus sets graph.dirty
        self.assertTrue(s["graph"]["dirty"])
        self.assertEqual(orch.recommend_phase(s), "deepen")

    def test_synthesize_when_drained(self):
        s = st.load_default()
        _corpus(s, "t", 3)
        s["graph"]["dirty"] = False                  # graph merged, no queued gaps
        self.assertEqual(orch.recommend_phase(s), "synthesize")

    def test_reopened_gap_flips_synthesize_back_to_deepen(self):
        s = st.load_default()
        _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        self.assertEqual(orch.recommend_phase(s), "synthesize")
        st.add_gap(s, topic="t", desc="new question")  # process reopens a gap
        self.assertEqual(orch.recommend_phase(s), "deepen")


class GoalMet(unittest.TestCase):
    def test_true_when_synthesize_drained_with_pending_draft(self):
        s = st.load_default()
        ids = _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        st.add_draft(s, topic="t", title="f", path="p", cites=ids, status="draft")
        self.assertFalse(orch._processable(s, 3))    # all sources now cited
        self.assertTrue(orch.goal_met(s))

    def test_false_when_still_processable(self):
        s = st.load_default()
        _corpus(s, "t", 3)                           # uncited -> processable
        s["graph"]["dirty"] = False
        self.assertFalse(orch.goal_met(s))

    def test_false_when_no_pending_draft(self):
        s = st.load_default()
        ids = _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        st.add_draft(s, topic="t", title="f", path="p", cites=ids, status="promoted")
        self.assertFalse(orch.goal_met(s))           # draft promoted, none pending


class NextActions(unittest.TestCase):
    def test_search_eligible_in_gather(self):
        s = st.load_default()                        # phase gather, search weight 0.7
        st.add_gap(s, topic="t", desc="q")
        a = orch.next_actions(s)
        self.assertTrue(a["search"])
        self.assertFalse(a["process"])               # process weight 0 in gather

    def test_process_eligible_in_synthesize(self):
        s = st.load_default()
        st.set_phase(s, "synthesize")
        _corpus(s, "t", 3)
        a = orch.next_actions(s)
        self.assertTrue(a["process"])
        self.assertFalse(a["search"])                # no queued gaps


class Decide(unittest.TestCase):
    def test_apply_flips_phase(self):
        s = st.load_default()                        # phase gather
        _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        res = orch.decide(s, apply=True)
        self.assertEqual(res["phase"], "synthesize")
        self.assertTrue(res["phase_changed"])
        self.assertEqual(s["budget"]["phase"], "synthesize")

    def test_dry_run_restores_phase(self):
        s = st.load_default()
        _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        res = orch.decide(s, apply=False)
        self.assertEqual(res["phase"], "synthesize")
        self.assertEqual(s["budget"]["phase"], "gather")   # not persisted


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests.test_orchestrator -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'orchestrator'`.

- [ ] **Step 3: Write the implementation**

Create `scripts/orchestrator.py`:

```python
"""Convergence orchestrator: deterministic phase + flow decisions over state.json.

Stdlib only. Reads only .research/state.json (via state.py). The phase decision is
a stateless function of current signals, so it self-corrects in either direction.
"""
import json
import sys

import state as state_mod


def _processable(state, min_sources):
    """True when some topic has >= min_sources un-cited corpus entries.

    Phase-independent on purpose: state.process_candidates self-gates on the process
    subagent count (0 in `gather`), which would make the gather->deepen decision
    circular.
    """
    cited = state_mod._cited_ids(state)
    counts = {}
    for e in state["corpus"]:
        if e["id"] not in cited:
            counts[e["topic"]] = counts.get(e["topic"], 0) + 1
    return any(n >= min_sources for n in counts.values())


def recommend_phase(state, min_sources=3):
    queued = len(state_mod.list_gaps(state, status="queued"))
    dirty = state["graph"]["dirty"]
    processable = _processable(state, min_sources)
    pending = len(state_mod.list_drafts(state, status="draft"))
    if queued == 0 and not dirty and (processable or pending):
        return "synthesize"
    if not processable and not pending:
        return "gather"
    return "deepen"


def goal_met(state, min_sources=3):
    return (
        recommend_phase(state, min_sources) == "synthesize"
        and not _processable(state, min_sources)
        and len(state_mod.list_drafts(state, status="draft")) >= 1
    )


def next_actions(state, min_sources=3):
    queued = len(state_mod.list_gaps(state, status="queued"))
    search = (
        queued > 0
        and state_mod.budget_remaining_sources(state) > 0
        and state_mod.subagent_count(state, "search") > 0
    )
    process = len(state_mod.process_candidates(state, min_sources)) > 0
    return {"search": bool(search), "process": bool(process)}


def decide(state, min_sources=3, apply=False):
    before = state["budget"]["phase"]
    rec = recommend_phase(state, min_sources)
    state_mod.set_phase(state, rec)                 # in-memory flip (validated)
    result = {
        "phase": rec,
        "phase_changed": rec != before,
        **next_actions(state, min_sources),
        "goal_met": goal_met(state, min_sources),
    }
    if not apply:
        state_mod.set_phase(state, before)          # restore for dry-run
    return result


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("decide")
    d.add_argument("--root", default=".")
    d.add_argument("--min-sources", type=int, default=3)
    d.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)
    if args.cmd == "decide":
        st = state_mod.load(args.root)
        res = decide(st, min_sources=args.min_sources, apply=args.apply)
        if args.apply:
            state_mod.save(st, args.root)
        print(json.dumps(res))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 -m unittest tests.test_orchestrator -v`
Expected: PASS — all 11 tests OK.

- [ ] **Step 5: Verify the CLI end to end (and confirm no state artifact is staged)**

Run:
```bash
cd "$(git rev-parse --show-toplevel)"
python3 scripts/orchestrator.py decide --apply
```
Expected: a JSON line like `{"phase": "gather", "phase_changed": false, "search": false, "process": false, "goal_met": false}` (exact booleans depend on the live `.research/state.json`). This call seeds/loads `.research/state.json` as a side effect — do NOT stage it.

- [ ] **Step 6: Commit**

```bash
git add scripts/orchestrator.py tests/test_orchestrator.py
git commit -m "feat: convergence orchestrator — phase auto-flip + goal check"
```

---

### Task 2: `.claude/goal.md` prompt + README section

**Files:**
- Create: `.claude/goal.md`
- Modify: `README.md` (append a new top-level section after the existing "Realtime graph view" section)

**Interfaces:**
- Consumes (from Task 1): `python3 scripts/orchestrator.py decide --apply` → JSON `{phase, phase_changed, search, process, goal_met}`.
- Consumes (existing): the Ingest cycle (`.claude/loop.md`), the Process cycle (`.claude/process.md`), `bash scripts/search_flow.sh --topic <T>`, `python3 scripts/promote.py queue`, `python3 scripts/state.py list-gaps --status failed`.
- Produces: the agent-run `/goal` convergence loop. No automated test — exercised by the real end-to-end smoke.

- [ ] **Step 1: Write the `/goal` prompt**

Create `.claude/goal.md`:

```markdown
# Convergence goal

Drive the research engine toward convergence. This is the `/goal` orchestrator: it runs
the three flows (ingest, search, process) until the engine has drained its autonomous
work and drafts are waiting for human review.

Run cycles until step 2 reports `goal_met: true`, then stop. Keep a cycle counter `K`
starting at 0; increment it in step 5 each cycle.

Each cycle, do exactly this:

1. **Ingest.** Run the Ingest cycle exactly as defined in `.claude/loop.md` (drain
   `ingest/`, graphify `--update` if the graph is dirty, replay assertions, append graph
   events, clear the dirty flag, integrity check). If `ingest/` was empty and the graph
   was clean it is a no-op — continue.

2. **Decide.** Run:
   ```
   python3 scripts/orchestrator.py decide --apply
   ```
   This prints JSON `{phase, phase_changed, search, process, goal_met}` and auto-flips
   the budget `phase` in `.research/state.json`. Parse it as `D`.
   - If `D.goal_met` is `true`: **stop**. Report convergence, then surface the human
     review queue and any stuck gaps:
     ```
     python3 scripts/promote.py queue
     python3 scripts/state.py list-gaps --status failed
     ```
     Do not run any more cycles.

3. **Search.** If `D.search` is `true`: run one search cycle:
   ```
   bash scripts/search_flow.sh --topic 13-reference-systems-case-studies
   ```
   (Use the goal's topic if a different one is in play.) Output lands in `ingest/` and is
   drained by the next cycle's step 1.

4. **Process.** If `D.process` is `true`: run the Process cycle exactly as defined in
   `.claude/process.md` (pick a candidate topic, draft with inline citations, pass both
   success gates, record the draft, emit gaps, optional assertions, integrity check).

5. **Safety.** Increment `K`. If `K >= 25` and `goal_met` was never `true`, **stop**: the
   loop did not converge. Surface the failed/stuck gaps
   (`python3 scripts/state.py list-gaps --status failed`) and the review queue
   (`python3 scripts/promote.py queue`) so a human can intervene. This is a backstop —
   normal termination comes from step 2.

The budget `phase` is chosen for you each cycle by `orchestrator.py` (gather → deepen →
synthesize, and back to deepen if a gap reopens). Never set `phase` by hand inside this
loop.
```

- [ ] **Step 2: Add the README section**

In `README.md`, append this as a new top-level section after the "Realtime graph view" section:

```markdown
## Convergence loop (`/goal`)

`scripts/orchestrator.py` turns the three manually-kicked flows into one autonomously
convergent loop. Launch it with the `/goal` prompt in `.claude/goal.md`.

Each cycle the orchestrator reads `.research/state.json`, **auto-selects the budget
`phase`** from deterministic signals, and reports which flows are eligible:

- `gather` — nothing processable yet; search + ingest dominate.
- `deepen` — corpus is processable but gathering / graph work is still in flight.
- `synthesize` — gaps drained and graph merged; process dominates.

The phase function is stateless, so a gap reopened during synthesis flips the engine back
to `deepen` automatically. The loop stops when `orchestrator.py decide` reports
`goal_met` — the autonomous work is drained and drafts wait in the review queue. Promotion
stays a human gate (`python3 scripts/promote.py queue`).

Inspect a decision without changing anything:

```
python3 scripts/orchestrator.py decide
```

Add `--apply` to persist the phase flip (the `/goal` loop does this).
```

- [ ] **Step 3: Sanity-check the referenced commands resolve**

Run:
```bash
cd "$(git rev-parse --show-toplevel)"
test -f .claude/loop.md && test -f .claude/process.md && test -f scripts/search_flow.sh \
  && test -f scripts/promote.py && python3 scripts/orchestrator.py decide >/dev/null \
  && echo OK
```
Expected: `OK` (every path the prompt names exists and the decide CLI runs).

- [ ] **Step 4: Commit**

```bash
git add .claude/goal.md README.md
git commit -m "feat: /goal convergence prompt + README section"
```

---

## Self-Review

**1. Spec coverage:**
- §2 auto-flip discrete phase → Task 1 `recommend_phase` + `decide(apply)`; Task 1 Step `test_apply_flips_phase`. ✓
- §2 goal = work-exhausted in synthesize → Task 1 `goal_met`; tests true/false. ✓
- §2 all eligible flows, dependency order → Task 2 `goal.md` steps 1/3/4 (ingest→search→process), `next_actions`. ✓
- §2 no new state schema → Task 1 reuses `phase`/`set_phase`; no schema edits. ✓
- §3 two signals + stateless self-correct → `recommend_phase`; `test_reopened_gap_flips_synthesize_back_to_deepen`. ✓
- §3 phase-independent `processable` → `_processable` (not `process_candidates`). ✓
- §4 termination backstop → Task 2 Step 1 cycle cap (`K >= 25`). ✓
- §5 `orchestrator.py` API + CLI → Task 1. ✓
- §5 `.claude/goal.md` → Task 2 Step 1. ✓
- §5 README → Task 2 Step 2. ✓
- §7 testing (transitions, goal_met, next_actions, decide apply) → Task 1 test suite. ✓

**2. Placeholder scan:** No TBD/TODO; every code/command step has full content. No suppression comments (`# noqa`/`# type: ignore`) anywhere — the post-`sys.path.insert` alias imports are bare, matching the existing `tests/test_*.py`.

**3. Type consistency:** `recommend_phase`/`goal_met`/`next_actions`/`decide`/`_processable` names and signatures identical across Task 1 definition, the test, and Task 2's CLI usage. `decide` return keys (`phase`, `phase_changed`, `search`, `process`, `goal_met`) match the prompt's `D.*` references. ✓
```
