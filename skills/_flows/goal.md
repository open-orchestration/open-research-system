# Convergence goal

Drive the research engine toward convergence. This is the `/goal` orchestrator: it runs
the three flows (ingest, search, process) until the engine has drained its autonomous
work and drafts are waiting for human review.

Run cycles until step 2 reports `goal_met: true`, then stop. Keep a cycle counter `K`
starting at 0; increment it in step 5 each cycle.

Each cycle, do exactly this:

0. **Run start (once).** On the first cycle only, run `ors runlog start` to open
   the run log. Each cycle, run `ors runlog set-cycle K` (K = your cycle counter)
   before doing anything else, so every step this cycle is tagged with the cycle number.

1. **Ingest.** Run the Ingest cycle exactly as defined in `skills/_flows/loop.md` (drain
   `ingest/`, graphify `--update` if the graph is dirty, replay assertions, append graph
   events, clear the dirty flag, integrity check). If `ingest/` was empty and the graph
   was clean it is a no-op — continue.

2. **Decide.** Run:
   ```
   ors decide --apply
   ```
   This prints JSON `{phase, phase_changed, search, process, goal_met}` and auto-flips
   the budget `phase` in `.research/state.json`. Parse it as `D`.
   Log the decision with a state snapshot so the verifier can independently recompute it.
   The record's `data` must be `{"decide": <the decide JSON>, "state": <snapshot>}`, so pass the
   decide JSON nested under `decide` and let `--snapshot` add `state`:
   `ors runlog log --flow orchestrator --step decide --status ok --snapshot --data "{\"decide\": $D}"`
   - If `D.stop` is `true`: **stop**. If `D.goal_met` is true, report convergence
     (plateau). If instead `D.budget_exhausted` is true, report the run was cut short on
     budget: print the finding/dimension counts and the pending-candidate count so the
     user knows it did not fully converge. Then surface the review queue + stuck gaps
     (`ors promote queue`; `ors state list-gaps --status failed`),
     close the run log (`ors runlog end --status ok`), and run no more cycles.

3. **Search.** If `D.search` is `true`: run search+ingest concurrently, one worker per topic
   with queued gaps, each isolated in its own `ingest/.work/<topic>/` inbox so parallel
   ingests never share files or mis-route. Worker count is `budget.max_workers`:
   ```
   W=$(ors state budget-status | python3 -c 'import json,sys;print(json.load(sys.stdin)["max_workers"])')
   ors state list-gaps --status queued | cut -f2 | sort -u | \
     xargs -P "$W" -I{} bash -c '
       T="{}"; IN="ingest/.work/$T"; mkdir -p "$IN"
       ors search --topic "$T" --inbox "$IN"
       ors ingest "$T" --inbox "$IN"
     '
   # self-certify: a search-only cycle still ingested, so it must log its own
   # integrity step (the verifier requires one per cycle with work; don't defer
   # it to the next cycle's step 1).
   ors check_integrity \
     && ors runlog log --flow ingest --step integrity --status ok \
     || ors runlog log --flow ingest --step integrity --status fail
   ```
   Each worker fetches within the shared strict budget (atomic reserve/refund, so concurrent
   workers never overspend `sources_per_cycle`) and flags the graph dirty. The graph update +
   replay + event append stay serial — they run in the next cycle's step 1, which still fires
   on an empty drain because the dirty flag persists in `.research/state.json`. The integrity
   check above closes the cycle so a search-only (`gather`-phase) cycle self-certifies.

4. **Process.** If `D.process` is `true`: run the Process cycle exactly as defined in
   `skills/_flows/process.md` (pick a candidate topic, draft with inline citations, pass both
   success gates, record the draft, emit gaps, optional assertions, integrity check).

4b. **Dimension gate** (plan growth — runs every cycle, see `.claude/research.md` and
    the spec's §1.5). Do exactly this:
    - List deterministically-eligible candidates:
      `ors dim eligible --root <root>` (these already pass the
      corroboration threshold, have α-wealth left, and fit the remaining budget).
    - For EACH eligible candidate, judge the three LLM axes against `goal.question` in
      `.research/state.json`: (1) goal-relevance, (2) distinctness from existing
      `plan.dimensions`, (3) comparability — both entities are scoreable on it
      (comparison shape only). Accept only if all three pass.
      - Accept: `ors dim accept --root <root> --name "<name>"`,
        then seed one gap per `entity × new dimension`
        (`ors state add-gap --topic "<name>" --desc "<entity> <name>" --origin dimension`).
      - Reject: `ors dim reject --root <root> --name "<name>" --reason "<axis that failed>" --cycle K`.
    - Expire stale candidates: `ors dim expire --root <root> --cycle K`.
    - Log: `ors runlog log --flow dimension --step gate --status ok --data "{\"accepted\":A,\"rejected\":R}"`.

4c. **Meter.** Update cumulative run-token spend so the next `decide` sees it:
    `ors meter update --root <root> --fallback-subagents <subagents dispatched this cycle>`.
    (primary token metering requires the CLAUDE_TRANSCRIPT_PATH env var; without it the per-cycle subagent estimate is used, and the cycle cap remains the backstop)

5. **Safety.** Increment `K`. If `K >= 25` and `goal_met` was never `true`, **stop**: the
   loop did not converge. Surface the failed/stuck gaps
   (`ors state list-gaps --status failed`) and the review queue
   (`ors promote queue`) so a human can intervene. This is a backstop —
   normal termination comes from step 2.
   Before stopping, close the run log: `ors runlog end --status capped`

The budget `phase` is chosen for you each cycle by `orchestrator.py` (gather → deepen →
synthesize, and back to deepen if a gap reopens). Never set `phase` by hand inside this
loop.
