<!-- skills/_flows/loop.md -->
# Ingest cycle

Run one ingest cycle for the research engine. Do exactly this, then stop:

1. Run `ors ingest <default-topic>` (default topic: `13-reference-systems-case-studies` unless a dropped file names another). This drains `ingest/`, normalizes each item, records it in `.research/state.json`, and flags the graph dirty.
2. If `.research/state.json` shows `graph.dirty == true`: **if the graphify skill is available**
   (installed — see `/open-research-system:setup`), back up the current graph
   (`cp .graphify/graph.json .graphify/.graphify_old.json` if it exists), then invoke
   the **graphify skill with `--update`** to incrementally extract only the new/changed
   source files (semantic update — an LLM step, not the code-only `graphify update` CLI).
   **If graphify is NOT available, skip the graph update for this cycle** — log it
   (`ors runlog log --flow graph --step graphify --status skip
   --data '{"reason":"graphify not installed"}'`) and continue; the run still
   produces cited findings (the graph is enrichment).
3. **Replay the assertion overlay** into the freshly-updated graph (asserted
   edges survive `graphify --update`, which only knows the corpus):
   `ors assertions replay`
   This strips and re-merges every active asserted edge into
   `.graphify/graph.json` (tagged `_origin: asserted`); it is idempotent and a
   no-op if no graph or no assertions exist. It must run **before** the
   `graph_events append` below so the delta feed sees the merged graph.
4. After the graph update and replay, append the delta to the event stream:
   `ors graph_events append --old .graphify/.graphify_old.json --new .graphify/graph.json --events .research/graph-events.jsonl`
5. Clear the dirty flag and record the new graph size:
   ```
   N=$(python3 -c 'import json;print(len(json.load(open(".graphify/graph.json")).get("nodes",[])))')
   E=$(python3 -c 'import json;g=json.load(open(".graphify/graph.json"));print(len(g.get("links",g.get("edges",[]))))')
   ors state set-graph --dirty false --node-count "$N" --edge-count "$E"
   ```
   Now emit the three graph-step log records in pipeline order (this fixes their
   relative `seq` for the verifier — graphify, then replay, then graph_events):
   ```
   ors runlog log --flow graph --step graphify --status ok --data "{\"node_count\":$N,\"edge_count\":$E}"
   ors runlog log --flow graph --step replay --status ok
   ors runlog log --flow graph --step graph_events --status ok
   ```
6. Run `ors check_integrity` — if it reports problems, stop and surface them; do not claim the cycle succeeded.
   Log the integrity result: `ors runlog log --flow ingest --step integrity --status ok`
   (use `--status fail` and stop if it reported problems).

If `ingest/` was empty (step 1 printed "no new sources"), stop early — nothing to do this cycle.
