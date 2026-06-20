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
