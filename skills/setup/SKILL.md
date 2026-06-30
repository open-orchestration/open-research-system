---
name: setup
description: Provision the research dependencies (crawl4ai + headless chromium + markitdown venv, and the graphify skill) so /open-research-system:research can run. Use when the user runs /open-research-system:setup or a run reports deps are not provisioned.
disable-model-invocation: true
---

# /open-research-system:setup — provision research dependencies

One-time (idempotent) setup so research runs work on this machine. Requires
**python3.12** on the host. Run:

```
ors setup
```

This reuses an existing `~/.venvs/crawl4ai` if present, otherwise builds a
plugin-owned venv under `${CLAUDE_PLUGIN_DATA}/venv` (`crawl4ai` + `markitdown[all]`
+ headless chromium), and installs the graphify skill via its own installer
(`graphifyy`, MIT — github.com/safishamsi/graphify) when absent. It prints a ✓/✗
checklist; re-running when already provisioned is a no-op. The chromium download is
the slow step. If graphify cannot be installed, research still runs — only the
knowledge-graph enrichment is skipped.
