<!-- .claude/loop.md -->
# Ingest cycle

Run one ingest cycle for the research engine. Do exactly this, then stop:

1. Run `bash scripts/ingest_flow.sh <default-topic>` (default topic: `13-reference-systems-case-studies` unless a dropped file names another). This drains `ingest/`, normalizes each item, records it in `.research/state.json`, and flags the graph dirty.
2. If `.research/state.json` shows `graph.dirty == true`: back up the current graph (`cp .graphify/graph.json .graphify/.graphify_old.json` if it exists), then invoke the **graphify skill with `--update`** to incrementally extract only the new/changed source files (semantic update — this is an LLM step, not the code-only `graphify update` CLI).
3. After the graph update, append the delta to the event stream:
   `python3 scripts/graph_events.py append --old .graphify/.graphify_old.json --new .graphify/graph.json --events .research/graph-events.jsonl`
4. Clear the dirty flag and record the new graph size:
   ```
   N=$(python3 -c 'import json;print(len(json.load(open(".graphify/graph.json")).get("nodes",[])))')
   E=$(python3 -c 'import json;print(len(json.load(open(".graphify/graph.json")).get("edges",[])))')
   python3 scripts/state.py set-graph --dirty false --node-count "$N" --edge-count "$E"
   ```
5. Run `python3 scripts/check_integrity.py` — if it reports problems, stop and surface them; do not claim the cycle succeeded.

If `ingest/` was empty (step 1 printed "no new sources"), stop early — nothing to do this cycle.
