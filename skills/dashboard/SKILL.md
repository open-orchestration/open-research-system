---
name: dashboard
description: Launch the live knowledge-graph dashboard for the current research run. Use when the user runs /open-research-system:dashboard or asks to see the realtime graph/state UI for an ORS run in this project.
disable-model-invocation: true
---

# /open-research-system:dashboard — live graph UI

Copy the UI into THIS project so it owns a standalone copy, then serve every panel
against this project's artifacts. Run:

```
DASH="$PWD/.research/dashboard"; mkdir -p "$DASH"
cp "${CLAUDE_PLUGIN_ROOT}/public/index.html" "${CLAUDE_PLUGIN_ROOT}/public/dashboard.html" "$DASH/"
GV_GRAPH="$PWD/.graphify/graph.json" \
GV_STATE="$PWD/.research/state.json" \
GV_RUNLOG="$PWD/.research/run.jsonl" \
GV_EVENTS="$PWD/.research/graph-events.jsonl" \
GV_HTML="$DASH/index.html" \
GV_DASHBOARD="$DASH/dashboard.html" \
  python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph_view_server.py" --port 8765
```

Then open the printed URL (`…/dashboard`). The UI files live in
`<project>/.research/dashboard/` (refreshed from the plugin on each launch, so the
project keeps a working copy even if the plugin is later removed). All four panels —
graph, queue, loop, and the live graph-events feed — read this project's `.graphify/`
and `.research/`. Stop with Ctrl-C. (graphify must have produced
`.graphify/graph.json` for the graph panel to populate.)
