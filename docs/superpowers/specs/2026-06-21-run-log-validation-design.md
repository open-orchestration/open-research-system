# Run-Log Observability + Validation Suite — Design

**Status:** approved design, pre-implementation
**Date:** 2026-06-21
**Umbrella spec:** `docs/superpowers/specs/2026-06-19-loop-research-engine-design.md`
**Builds on:** sub-projects #1–#6 (all merged on `phase1-research-spike`). This is validation tooling for the completed engine, not a new flow.

## 1. Purpose

The loop research engine is code-complete but has never been exercised as a live autonomous run.
Before a real smoke test, we need observability so that **each step of a run is independently
verifiable** and **an entire run writes to one consolidated log** we can inspect to confirm
everything worked.

Two deliverables:
1. A structured, append-only run log (`​.research/run.jsonl`) — every flow step emits one JSON line
   through a thin helper, carrying enough metadata to reconstruct and verify the whole run.
2. An automated verifier (`scripts/verify_run.py`) that reads the log back, asserts per-step and
   cross-step invariants, and prints a pass/fail report — so the eye is backed by a regression net.

## 2. Locked decisions

- **Structured instrumentation**, not stdout capture or pure post-hoc derivation. A `runlog.py`
  helper writes one record per step; flows call it explicitly.
- **Automated verifier + report.** `verify_run.py` asserts invariants and renders a report; the raw
  `.jsonl` stays directly human-readable.
- **Record schema carries `run_id` + `cycle` + `seq`** for segmentation, ordering, and causality
  checks. A sidecar `.research/run-context.json` holds the active `{run_id, cycle, seq}` across the
  many short-lived process invocations (each script call is a fresh process).
- **Severity tiers.** Findings are **FAIL** (exit 1) or **WARN** (surfaced, exit unaffected).
  FAIL = structural corruption, broken `seq`/ordering, `cite_check` failure, orchestrator phase
  mismatch, a gap marked `done` with 0 sources. WARN = a search retry / failed gap yielding 0
  sources (crawl4ai cold-starts fail ~half the time — a known-flaky path, not a bug), an empty
  cycle, a missing expected step.
- **Deterministic-first logging.** Bash flows (`gather.sh`, `search_flow.sh`, `ingest_flow.sh`)
  self-log reliably. The three agent prompts (`loop.md`, `process.md`, `goal.md`) are instructed to
  log each step; the verifier flags any **missing expected step** for a cycle as WARN so agent
  deviations are visible, never silently lost.
- **Single append-only log**, `run_id`-segmented. One `.research/run.jsonl`; the verifier defaults
  to the latest `run_id` (`--run-id` to select). Mirrors the existing `graph-events.jsonl` pattern.
- **Independent recompute.** The `orchestrator decide` record embeds a full `state.json` snapshot
  taken right **after** `decide --apply` (post-flip). The verifier imports `orchestrator` and
  re-runs `recommend_phase`/`next_actions`/`goal_met` against that snapshot, comparing to the logged
  and acted decision — catching a desynced orchestrator, not just a self-consistent log.
- **Python 3 stdlib only**, no pip/pytest; tests are `unittest`. No lint/type suppression comments.
- **Run artifacts are gitignored.** Add `.research/run.jsonl` and `.research/run-context.json` to
  `.gitignore` — they are large, ephemeral per-run traces regenerated each run; inspect the
  working-tree file rather than committing run history.

## 3. Record schema

One JSON object per line in `.research/run.jsonl`:

```
{
  "run_id": "r" + 8 hex,        # mints once per run via `runlog start`
  "cycle":  <int>,              # orchestrator cycle index; 0 until goal.md sets it
  "seq":    <int>,              # strictly increasing within a run_id (per-record)
  "ts":     <iso8601>,          # datetime.now(timezone.utc).isoformat()
  "flow":   <str>,              # "search" | "ingest" | "graph" | "process" | "orchestrator" | "run"
  "step":   <str>,              # e.g. "gather", "fetch", "normalize", "graphify", "replay",
                                #      "graph_events", "decide", "draft", "cite_check", "integrity"
  "status": "ok" | "fail" | "skip",
  "data":   { ... }            # step-specific metadata (see §5 invariants)
}
```

Lifecycle events use `flow:"run"`: `run_start` (first line, `cycle:0 seq:0`, `data.state` = a full
`state.json` snapshot taken at run entry, so the verifier knows the baseline counts), `run_end`
(`data.status`).

`run_id` = `"r" + sha256(iso_now + "|" + str(pid))[:8]` — 9 chars, matching the engine's durable-id
convention (`g`/`d`/`a`/`c` + 8 hex).

## 4. Components

### `scripts/runlog.py` (new)

Owns the sidecar `.research/run-context.json` `{run_id, cycle, seq}`.

- `start(root=".") -> run_id` — mint `run_id`, reset context to `{run_id, cycle:0, seq:0}`, append a
  `run_start` record with `data.state` = a full `state.json` snapshot (the verifier's baseline),
  return/print the id.
- `set_cycle(n, root=".")` — set `cycle = n` in the context (goal.md calls this each loop).
- `log_event(flow, step, status="ok", data=None, root=".")` — read context, `seq += 1`, persist
  context, append the record. Importable so `orchestrator.py` / other Python can log directly.
- `end(status="ok", root=".")` — append a `run_end` record.
- Atomic append: open in append mode, write one `json.dumps(...) + "\n"`. Context sidecar written
  via the existing tmp + `os.replace` atomic pattern (`state.py.save`).
- CLI: `start` · `set-cycle N` · `log --flow F --step S [--status …] [--data '<json>']` ·
  `end [--status …]`. All take `--root`. `log --snapshot` embeds the current `state.json` into
  `data.state` (used by the `decide` step for independent recompute).

### Instrumentation (edits)

Small additions at each step boundary:
- **`gather.sh` / `search_flow.sh` / `ingest_flow.sh`** — `python3 scripts/runlog.py log --flow … --step … --status … --data '…'` after each step, recording the metadata §5 needs (sources fetched, junk filtered, gap outcome, corpus added, dirty flag).
- **`.claude/loop.md`** — log `graphify`, `replay`, `graph_events`, `integrity` steps.
- **`.claude/process.md`** — log `draft`, `cite_check`, `gaps_emitted`, `assertions`, `integrity` steps.
- **`.claude/goal.md`** — `runlog start` at loop entry; `runlog set-cycle K` each cycle; log the
  `orchestrator decide` step with `--snapshot`; `runlog end` at stop.
- `orchestrator.py` stays pure — `goal.md` performs its logging.

### `scripts/verify_run.py` (new)

- Reads `.research/run.jsonl`, selects the latest `run_id` (or `--run-id`).
- Runs the §5 invariant checks; each yields findings tagged FAIL or WARN.
- Prints: a per-cycle timeline (steps in order with status) + an invariant summary table
  (check name → PASS / WARN / FAIL with offending `seq`/line). `--json` for a machine-readable
  verdict.
- Exit 1 if any FAIL, else 0 (WARNs do not fail).
- Imports `orchestrator` and `state` for the recompute and consistency checks.

## 5. Invariants

**Structural (FAIL):** every line parses as JSON; `seq` strictly increasing within the run;
`cycle` monotonic non-decreasing; exactly one `run_start`; `run_start` is `seq` 0.

**Per-step:**
- search: a gap marked `done` (`data.gap_status=="done"`) must have `data.sources_added >= 1`
  (FAIL otherwise). A `requeued`/`failed` gap with 0 sources is the expected flaky path (WARN).
- ingest: `data.corpus_added >= 1` and `data.graph_dirty == true` when sources were drained (FAIL
  if corpus added but dirty not set).
- graph (`graphify`): `data.node_count` / `data.edge_count` present and **non-decreasing** vs the
  prior recorded graph step (incremental update; FAIL on a decrease).
- process: each `draft` step has `data.draft_id`; the paired `cite_check` step `status=="ok"` (FAIL
  on a recorded draft whose `cite_check` failed).
- integrity: each cycle that ran ingest or process ends with an `integrity` step `status=="ok"`
  (FAIL otherwise).

**Cross-step ordering (FAIL):** within a cycle, `replay` appears after `graphify` and before
`graph_events` (matches the `loop.md` contract so the delta feed sees merged assertions).

**Causality / recompute (FAIL):** for each `decide` record, recompute
`orchestrator.recommend_phase(data.state)`, `next_actions(data.state)`, `goal_met(data.state)` and
compare to `data.decide`. Any divergence is a FAIL. Additionally: once a `decide` logs
`goal_met==true`, no later `search` or `process` steps may appear (FAIL — the loop should have
stopped).

**Completeness (WARN):** for a cycle whose `decide` marked a flow eligible (`search`/`process`
true), a corresponding logged step is expected; a missing one is WARN (agent deviation or
legitimately idle — surfaced, not failed).

**Consistency (FAIL):** baseline counts from the `run_start` snapshot (`data.state`) plus the deltas
logged during the run (corpus added, drafts created, assertions applied) reconcile with the live
`state.json` (`len(corpus)`, draft count, `assertions.count`): `baseline + sum(logged deltas) ==
final`. Divergence is a FAIL.

**Out of scope:** the agent-side faithfulness self-check in `process.md` is not deterministically
checkable and is already gated in-flow; the verifier does not attempt it. `ponytail: verifier covers
deterministic invariants only; faithfulness stays an in-flow agent gate.`

## 6. Data flow

```
runlog start ──> run-context.json {run_id, cycle:0, seq:0} + run_start line
   │
goal.md set-cycle K ──> each flow step: runlog log ──append──> run.jsonl
   │                         (decide step embeds state snapshot)
runlog end ──> run_end line
   │
verify_run.py ──read run.jsonl (latest run_id)──> invariant checks + recompute
   │                                                (imports orchestrator, state)
   └──> report (timeline + FAIL/WARN table) + exit 0/1
```

## 7. Testing

- `tests/test_runlog.py` (unittest, temp root): `start` mints a 9-char `r…` id and resets context;
  `log_event` appends a well-formed record with `seq` incrementing across calls; `set_cycle` updates
  the context and subsequent records; `end` writes `run_end`; context survives across separate calls
  (simulating separate processes by re-reading the sidecar).
- `tests/test_verify_run.py` (unittest, temp root): a hand-built **good** `run.jsonl` passes with no
  FAIL/WARN; then one crafted log per invariant (non-increasing `seq`; a `done` gap with 0 sources;
  a graph step with decreasing node count; a `decide` whose logged phase diverges from the recompute;
  a `search` step after `goal_met==true`; a log/`state.json` count mismatch) trips **exactly** its
  check at the right severity. This makes the verifier's own correctness the thing under test.

The live full-loop smoke run itself is the consumer of this suite, performed after it merges — not a
unit test.

## 8. Out of scope (YAGNI)

- No logging framework, no DB, no live dashboard, no per-function tracing — one JSONL + one verifier.
- No new flow behavior; instrumentation only observes existing steps.
- No committing of run traces (gitignored); evidence-keeping is a manual copy if ever needed.
