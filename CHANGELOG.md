# Changelog

All notable changes to the `open-research-system` plugin are documented here.
This project follows [semantic versioning](https://semver.org). Because
`plugin.json` pins an explicit `version`, users receive an update only when that
field is bumped — so every user-facing change lands with a version bump and an
entry below.

## [0.2.0] — 2026-06-30

### Added
- `/open-research-system:setup` — idempotent provisioning of the research deps
  (crawl4ai + headless chromium + markitdown venv, and the graphify skill via its
  own installer). Reuses an existing `~/.venvs/crawl4ai`, else builds a plugin-owned
  venv under `${CLAUDE_PLUGIN_DATA}/venv`.
- SessionStart hook that nudges to run setup when deps are unprovisioned.

### Changed
- All dep paths resolve through one `ors_venv` resolver; the crawl4ai search/fetch
  helpers are now bundled in the plugin.
- The knowledge-graph step degrades gracefully when graphify is absent.

### Removed
- The `jq` dependency (search URLs are parsed with python3).

## [0.1.0] — 2026-06-29

Initial packaged release: open-research-system as a self-contained Claude Code
plugin, runnable against any target project.

### Added
- `/open-research-system:research` — one-prompt autonomous research run that
  bootstraps a plan and drives the goal loop to convergence.
- `/open-research-system:report` — narrative, cited report from a run.
- `/open-research-system:dashboard` — live knowledge-graph + queue + loop UI.
- `bin/ors` engine dispatcher (on the plugin PATH); internal flows in
  `skills/_flows/`.
- `DOCS_BASE=.research/docs` namespacing so all research output lands under the
  target project's `.research/` (and `.graphify/`), never the plugin repo.
- Distribution via the `open-orchestration` marketplace.
- MIT license.
