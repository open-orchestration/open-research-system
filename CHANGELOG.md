# Changelog

All notable changes to the `open-research-system` plugin are documented here.
This project follows [semantic versioning](https://semver.org). Because
`plugin.json` pins an explicit `version`, users receive an update only when that
field is bumped — so every user-facing change lands with a version bump and an
entry below.

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
