---
name: dashboard
description: Launch the live knowledge-graph dashboard for the current research run. Use when the user runs /ors:dashboard or asks to see the realtime graph/state UI for an ORS run in this project.
disable-model-invocation: true
---

# /ors:dashboard — live graph UI

Serve the realtime graph + run dashboard against THIS project's artifacts. Run:

```
GV_GRAPH="$PWD/.graphify/graph.json" \
GV_STATE="$PWD/.research/state.json" \
GV_HTML="${CLAUDE_PLUGIN_ROOT}/public/index.html" \
GV_DASHBOARD="${CLAUDE_PLUGIN_ROOT}/public/dashboard.html" \
  python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph_view_server.py" --port 8765
```

Then open the printed URL. The server reads the target's `.graphify/graph.json`
and `.research/state.json`; the HTML is served from the plugin bundle. Stop it
with Ctrl-C when done. (graphify must have produced `.graphify/graph.json` for the
graph panel to populate.)
