# Loop Engine — A→C Convergence Orchestrator (sub-project #6)

**Status:** approved design, pre-implementation
**Date:** 2026-06-20
**Umbrella spec:** `docs/superpowers/specs/2026-06-19-loop-research-engine-design.md` (§5 budget governor, §6 flows)
**Builds on:** #1 ingest · #2 search · #3 process · #4 graph enrichment · #5 realtime view (all merged)

## 1. Purpose

The final sub-project. Sub-projects #1–#5 built three flows that a human kicks manually
(ingest, search, process) coordinating through the `.research/state.json` spine. #6 makes the
engine **autonomously convergent**: a single `/goal` loop drives all three flows toward a
research goal and **auto-selects the budget governor's `phase`** each cycle, turning the
deferred "orchestrator self-tuning" from the umbrella spec §5 into a v1 reality — in its
smallest defensible form.

The umbrella spec deferred self-tuning to "avoid a fragile auto-classifier in v1," keeping
`phase` human-set with the flow writing only a *suggestion*. #6 enables it as an **auto-flip of
the discrete `phase` field** (not continuous weight tuning): the static 3×3 `weights` table is
untouched; only which row is active is chosen by a deterministic, stateless function of state
signals each cycle.

## 2. Locked decisions

- **Self-tuning = auto-flip discrete phase.** The orchestrator computes `phase`
  (`gather`/`deepen`/`synthesize`) from deterministic state thresholds and flips it itself each
  cycle. The 3×3 `weights` table stays a static human-set constant; no float-level tuning. This
  is the smallest reversible, inspectable surface that satisfies "self-tuning."
- **Goal done = work-exhausted in synthesize.** `/goal` stops when the engine has drained its
  autonomous work and handed drafts to the human review queue. Promotion is a human gate, so the
  done-check cannot require promoted findings.
- **Each cycle runs all eligible flows in dependency order** (ingest → search → process), gated
  by derivable eligibility and `subagent_count` (which the flipped phase drives). No new
  scheduler; flows are not mutually exclusive per phase.
- **No new state schema.** `phase` and `set_phase` already exist; auto-flip reuses them. No new
  fields, no global budget tracking.
- **Python 3 stdlib only**, no pip/pytest; tests are `unittest` + bash. No lint/type
  suppression comments.

## 3. The two signals (why phases flip)

The phase decision is a **stateless function of current state signals** — no cross-cycle history
is tracked. It can move in *either* direction, so a reopened gap during synthesis self-corrects
back to deepening.

Signals (all derived from `state.json`, reusing `state.py`):

- `queued_gaps` — `len(list_gaps(status="queued"))`. Search backlog depth.
- `graph_dirty` — `state["graph"]["dirty"]`. Un-merged corpus pending.
- `processable` — **phase-independent**: at least one topic has ≥`min_sources` un-cited corpus
  entries. Computed directly (un-cited count per topic via `_cited_ids`), **not** via
  `process_candidates` — the latter self-gates on `subagent_count(process)<=0` and is therefore
  always empty in `gather`, which would make the gather→deepen transition circular.
- `drafts_pending` — `len(list_drafts(status="draft"))`. Drafts awaiting the human gate
  (`"draft"` is the only awaiting-review status; `promote.py queue` lists exactly these — note
  `queued` is a *gap* status, not a draft status).

**Phase recommendation** (`recommend_phase(state, min_sources=3)`):

```
if queued_gaps == 0 and not graph_dirty and (processable or drafts_pending):
    return "synthesize"          # gathering dried up, material ready
if not processable and not drafts_pending:
    return "gather"              # nothing processable yet — bootstrapping
return "deepen"                  # mid-flight
```

Transition trace:
- Fresh start (no corpus, gaps queued): `gather` — search/ingest dominate.
- A topic reaches ≥`min_sources` un-cited sources: `deepen` — effort splits across all three.
- Gaps drain, graph merged, material ready: `synthesize` — process dominates.
- Process emits a new gap during synthesize: `queued_gaps>0` → falls back to `deepen` → search
  picks it up. Self-correcting.

## 4. Goal success check

```
goal_met(state, min_sources) =
    recommend_phase(state, min_sources) == "synthesize"
    and not processable
    and drafts_pending >= 1
```

`synthesize` already implies `queued_gaps==0 and not graph_dirty`; the extra `not processable`
means every topic with enough sources has been drafted, and `drafts_pending>=1` means the
engine produced output now waiting for the human. This is the verifiable condition `/goal`
requires.

**Termination is guaranteed by existing mechanisms, not the goal-check:**
- Search marks a gap `failed` after K attempts (#2), so `queued_gaps` always drains to 0.
- Drafting a topic cites its sources → `_cited_ids` removes them from the un-cited pool →
  `processable` for that topic eventually goes false. Bounded by corpus size.

The cycle-cap (§5) is a backstop for the one productive-but-long case: process keeps emitting
gaps that search keeps resolving with new sources. That is convergence working, but capped to
bound cost.

## 5. Components

### `scripts/orchestrator.py` (new)

Pure deterministic decisions over a loaded `state`. Reuses `state.py`
(`load`, `save`, `set_phase`, `list_gaps`, `list_drafts`, `_cited_ids`, `subagent_count`,
`process_candidates`, `budget_remaining_sources`). No graph or disk reads beyond `state.json`.

API:
- `recommend_phase(state, min_sources=3) -> str` — §3.
- `goal_met(state, min_sources=3) -> bool` — §4.
- `next_actions(state, min_sources=3) -> dict` — assumes `phase` is current:
  - `search`: `queued_gaps>0 and budget_remaining_sources(state)>0 and subagent_count(state,"search")>0`
  - `process`: `process_candidates(state, min_sources)` is non-empty (folds the subagent gate).
- `decide(state, min_sources=3, apply=False) -> dict` — applies `recommend_phase`; when `apply`,
  flips `phase` via `set_phase` (caller saves, or `decide` saves when run from CLI). Returns
  `{phase, phase_changed, search, process, goal_met}`.

CLI: `python3 scripts/orchestrator.py decide --root . --min-sources 3 [--apply]` → prints the
decide JSON. `--apply` persists the phase flip to `state.json`.

### `.claude/goal.md` (new) — the `/goal` convergence prompt

Drives one cycle, then loops (via `/goal`) until `goal_met`. Per cycle:

1. **Ingest** — run the Ingest cycle (`.claude/loop.md`). Self-no-ops if `ingest/` is empty and
   the graph is clean.
2. **Decide** — `D=$(python3 scripts/orchestrator.py decide --apply)`. This auto-flips `phase`.
   If `D.goal_met` is true → **stop**: report convergence and surface the review queue
   (`python3 scripts/promote.py queue`) plus any `failed` gaps
   (`python3 scripts/state.py list-gaps --status failed`).
3. **Search** — if `D.search`: run the search cycle (`bash scripts/search_flow.sh --topic <T>`).
   Output lands in `ingest/` for the next cycle's ingest.
4. **Process** — if `D.process`: run the Process cycle (`.claude/process.md`).
5. **Safety** — maintain a cycle counter; at ~25 cycles without `goal_met`, stop and surface
   stuck/`failed` gaps. Backstop only.

### README

Add a "Convergence loop (`/goal`)" section: what the orchestrator does, the phase signals, the
done-condition, and how to launch it.

## 6. Data flow

```
state.json ──read──> orchestrator.decide ──flip phase──> state.json
     ^                      │ returns {phase, search, process, goal_met}
     │                      v
   flows  <── ingest / search / process cycles run per eligibility
     │
     └──mutate state (corpus, gaps, graph, drafts)──> loop
```

`state.json` is the sole coordination point — flows never coordinate through conversation
memory. The orchestrator adds no new persistent artifact.

## 7. Testing

`tests/test_orchestrator.py` (unittest, `sys.path.insert` + `import orchestrator as orch`):
- `recommend_phase`: each phase from a hand-built state; the self-correct case (synthesize state
  + one reopened queued gap → `deepen`).
- `goal_met`: true on a drained-synthesize state with a pending `status="draft"` draft; false when `processable`
  still holds or no draft pending.
- `next_actions`: search eligible only with queued gaps + budget + weight; process eligible only
  with candidates.
- `decide(apply=True)` flips `state["budget"]["phase"]` and reports `phase_changed`.

`goal.md` is agent-run prose, exercised by the handoff's real end-to-end smoke (launch `/goal`
on a seeded corpus, observe phase flips and the stop-at-goal handoff to the review queue).

## 8. Out of scope (YAGNI)

- Continuous weight-vector tuning (PID on density slope etc.) — `ponytail: static 3×3 table +
  discrete auto-flip; add float tuning if the heuristic measurably falls short`.
- A flow scheduler / pick-one-per-cycle priority — dependency order + subagent weighting covers
  it.
- New state fields, global cross-cycle budget, graph-density history tracking.
- Any new event-stream or view work — #6 sits on the existing flows and spine.
