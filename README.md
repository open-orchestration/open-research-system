# open-research-system (ORS)

One prompt → an autonomous, cited research run against **any project's directory**.
This repo *is* a self-contained Claude Code **plugin** (named `open-research-system`) and
the engine it bundles.

## Install

From the `open-orchestration` marketplace (hosted in this repo):

```
claude plugin marketplace add open-orchestration/open-research-system
claude plugin install open-research-system@open-orchestration
```

### One-time setup

After installing, provision the research dependencies (idempotent):

```
/open-research-system:setup
```

Requires **python3.12** on the host. This builds the crawl4ai + markitdown venv
(+ headless chromium) and installs the graphify skill (`graphifyy`, MIT). A
SessionStart nudge reminds you if you skip it. Research still runs without graphify
— only the knowledge-graph enrichment is skipped.

`/plugin update open-research-system` pulls new releases (the `version` in
`plugin.json` is the update key — see `CHANGELOG.md`). For local development,
skip the marketplace and load the working tree directly:
`claude --plugin-dir /path/to/open-research-system`.

## Run it against another project

ORS runs from inside a target project; all research output lands in **that** project,
never here.

1. In the target project, with the plugin installed (or `--plugin-dir`-loaded), confirm
   `/open-research-system:research` is available (`/plugin` lists it).
2. Add `.research/` and `.graphify/` to the target's `.gitignore` (ORS output is generated).
3. Kick off a run:
   ```
   /open-research-system:research "<your question>" [--budget <tokens>] [--root <dir>]
   ```
   ORS classifies the question, writes a plan, then drives the autonomous loop
   (search → ingest → graph → decide) to convergence — stopping on plateau, budget, or
   the cycle cap.
4. `/open-research-system:report` — narrative, cited summary of the run.
5. `/open-research-system:dashboard` — live knowledge-graph + queue + loop UI (localhost).

Prerequisites on the host: the **graphify** skill, the **crawl4ai** venv (search/fetch),
`jq`, `markitdown`, and `python3`.

## Where output goes (in the target project)

- `<target>/.research/state.json` — the run spine: goal, plan, gaps, corpus, budget.
- `<target>/.research/docs/NN-<topic>/sources/` — fetched, normalized source material.
- `<target>/.research/docs/findings/` — synthesized, cited findings + `SYNTHESIS.md`.
- `<target>/.graphify/` — the relational knowledge graph (graphify owns this dir).
- `<target>/.research/run.jsonl`, `graph-events.jsonl` — run trace + the dashboard feed.

All paths are root-relative to the target and namespaced under `.research/` (the
`DOCS_BASE` convention), so ORS never collides with the target's own `docs/`.

## How it's built

- **`bin/ors`** — the engine dispatcher, on the Bash-tool PATH while the plugin is
  enabled. Flows call `ors <verb>` (e.g. `ors plan apply`, `ors search`, `ors decide`),
  which resolves to the bundled `scripts/`. It also exports `REPO_ROOT`/`DOCS_BASE` and
  discovers the session transcript for real token metering.
- **`skills/`** — `research`, `report`, `dashboard` (user-invocable, side-effecting), plus
  internal procedures in `skills/_flows/` (`goal`, `loop`, `process`, `review`).
- **`scripts/`** — the stdlib-only python engine (`state.py`, `orchestrator.py`, `plan.py`,
  `meter.py`, `dimension_gate.py`, `promote.py`, …) and the bash flows
  (`search_flow.sh`, `ingest_flow.sh`).
- **`.claude-plugin/plugin.json`** — the plugin manifest.

## Convergence loop

`scripts/orchestrator.py decide` auto-selects the budget **phase** each cycle from
deterministic signals (`gather` → `deepen` → `synthesize`, and back to `deepen` if a gap
reopens) and reports which flows are eligible. The loop stops when `decide` reports
`goal_met` (autonomous work drained, drafts waiting in the human review gate),
`budget_exhausted`, or the cycle cap. Promotion stays a human gate (`ors promote queue`).

## Legacy corpus (this repo only — not produced by a plugin run)

This repo also contains the original 2026 research-spike output: `RESEARCH-CATALOG.md`
and `SYNTHESIS.md` at the root, and `docs/01-…`/`docs/findings/`. Those are the spike's
**frozen** artifacts and are *not* the layout a `/open-research-system:research` run produces in a target
project (that output lives under `<target>/.research/` as above). Design history lives in
`docs/superpowers/specs/` and `docs/superpowers/plans/`.
