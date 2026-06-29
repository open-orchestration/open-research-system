# ORS: The Package — design (sub-project B)

Make open-research-system installable and runnable against **any** project's
directory: a self-contained, personal, local Claude Code **plugin** so
`/ors:research "<prompt>"` and `/ors:report` work from another repo, writing all
artifacts into that target project. This is sub-project B from
`docs/superpowers/HANDOFF-PLANNER.md`. Sub-project A (the planner engine) is done
and live-validated (`HANDOFF-PLANNER.md` Gap-1, commit `0270ca1`).

## Goal & success criteria

From a fresh target repo with the ORS plugin enabled, a user runs
`/ors:research "<small question>" --budget <N>` and gets the full autonomous
chain — plan → search → ingest → graph → decide/meter loop → cited findings —
with every artifact under the **target**: `<target>/.research/` (state, runlog,
topic dirs, findings) and `<target>/.graphify/` (knowledge graph). `/ors:report`
emits the narrative; `/ors:dashboard` serves the live graph UI against the
target. The ORS repo's own scripts are the engine; nothing is copied per-run.

**Done when:** the plugin installs via `--plugin-dir <ors-repo>`; `/ors:research`
runs end-to-end against a throwaway target dir distinct from the ORS repo;
artifacts land under `<target>/.research` + `<target>/.graphify`; the existing
suite + smokes + integrity stay green (adapted to the new convention); a plugin
structural test passes.

## Decisions (locked in brainstorming)

1. **Distribution:** personal, local plugin (no marketplace/semver overhead).
   Bundled + self-contained.
2. **Repo IS the plugin:** restructure the ORS repo root into the plugin —
   add `.claude-plugin/plugin.json`, `bin/`, `skills/`; move `.claude/*.md`
   flows into `skills/`; keep `scripts/` + `public/` in place. No script
   duplication, single source of truth. `${CLAUDE_PLUGIN_ROOT}` = the installed
   repo dir.
3. **Engine entry = `bin/ors` dispatcher.** Plugin `bin/` is on the Bash tool's
   PATH while enabled (plugins-reference §"Plugin components", verified
   2026-06-29), so `ors <verb>` is callable from every (non-persistent) Bash
   tool call. The flow docs call `ors <verb>` instead of `python3 scripts/X.py`.
4. **Artifact namespace:** single uniform convention `DOCS_BASE = .research/docs`
   for **all** runs (in-repo and target). Topic dirs → `.research/docs/NN-slug/`,
   findings → `.research/docs/findings/` (under the same `DOCS_BASE`, so one
   knob governs the whole tree). `.graphify/` stays at root (graphify owns it).
   `.research/` + `.graphify/`
   are the only dirs a target user gitignores.
5. **`public/dashboard.html`** stays the user's protected file, already in
   `public/`; it becomes part of the bundle in place — no copy/move, not
   re-committed unless it actually changes (ask first).
6. **graphify** is a documented prerequisite (installed + active on the target
   machine); invoked from the target cwd so it writes `<target>/.graphify`.

## Architecture

### Execution model: cwd == target

When the user invokes `/ors:research` from their project, the agent's session
cwd is the target repo root. Everything keys off cwd; only engine **code**
points back to the plugin:

- Python engine scripts already take `--root` (default `.` = cwd = target).
- Shell flows already honor `REPO_ROOT` (default `$PWD` = target).
- graphify runs in cwd → `<target>/.graphify`.
- The dashboard server is already env-parametrized (`GV_GRAPH`, `GV_STATE`,
  `GV_HTML`, `GV_DASHBOARD` — see `graph_view_server.py:199-207`).

The only thing that must resolve to the plugin install dir is the script code,
which `bin/ors` resolves from its own location.

### `bin/ors` — the dispatcher (~40-60 lines, stdlib bash)

Single entrypoint that makes path-indirection survive shell non-persistence and
bakes in the env contract:

```sh
#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"          # = plugin/repo root
export REPO_ROOT="${REPO_ROOT:-$PWD}"             # target project
export DOCS_BASE="${DOCS_BASE:-.research/docs}"    # uniform namespace
verb="${1:?usage: ors <verb> [args]}"; shift
case "$verb" in
  search)  exec bash   "$HERE/scripts/search_flow.sh" "$@" ;;
  ingest)  exec bash   "$HERE/scripts/ingest_flow.sh" "$@" ;;
  gather)  exec bash   "$HERE/scripts/gather.sh"      "$@" ;;
  *)
    if   [ -f "$HERE/scripts/$verb.py" ]; then exec python3 "$HERE/scripts/$verb.py" "$@"
    elif [ -f "$HERE/scripts/$verb.sh" ]; then exec bash    "$HERE/scripts/$verb.sh" "$@"
    else echo "ors: unknown verb '$verb'" >&2; exit 2; fi ;;
esac
```

- Verb = script basename: `ors plan apply ...` → `scripts/plan.py apply ...`;
  `ors decide --apply` → `orchestrator.py`? No — `orchestrator` is the
  basename, so `ors orchestrator decide --apply`. To keep flow docs terse,
  alias the common ones explicitly in the `case` (`decide`→orchestrator,
  `dim`→dimension_gate, `meter`/`runlog`/`promote`/`state` pass through). Final
  verb table fixed during implementation; the generic resolver is the fallback.
- Does **not** inject `--root`: scripts default `--root .`, and the dispatcher
  leaves cwd at the target, so `.` resolves correctly. (`REPO_ROOT`/`DOCS_BASE`
  exported for the shell flows + the docs-base helper.)
- In-repo: `bin/ors` resolves its own dir, so the engine still runs from the
  ORS repo without the plugin installed (tests call `bin/ors` by path).

### `DOCS_BASE` threading (the convention migration)

Replace the hardcoded `docs` / `docs/findings` literals with a single resolved
base (env `DOCS_BASE`, default `.research/docs`):

- `scripts/lib.sh` `resolve_topic_dir` — `find "$root/$DOCS_BASE"` and create
  `"$root/$DOCS_BASE/NN-slug"` (lines 15/18/21).
- `scripts/promote.py:8-9` — `FINDINGS_DIR`/`SYNTHESIS` from a
  `docs_base()` helper (`os.environ.get("DOCS_BASE", ".research/docs")`), e.g.
  `<DOCS_BASE>/findings` + `<DOCS_BASE>/findings/SYNTHESIS.md`.
- `scripts/ingest.sh:14` — findings fallback under `$DOCS_BASE`.
- `.claude`→`skills/_flows`: `process.md` / `loop.md` literal `docs/findings/...`
  refs rewritten to the resolved base (these are agent-facing; reference the
  base, don't hardcode the old path).
- `scripts/gather.sh:34` — cosmetic echo string only.
- **Verify in implementation:** `check_integrity.py` + `cite_check.py` resolve
  cite/corpus paths from the relative `extracted` paths stored in `state.json`
  (already root-relative — likely no change), not from a hardcoded `docs/`.

A single helper is the source of truth on each side (one bash default in
`lib.sh`, one `docs_base()` in `state.py` imported where needed).

### Plugin structure (repo root)

```
open-research-system/            (= the plugin; ${CLAUDE_PLUGIN_ROOT})
├── .claude-plugin/plugin.json   # name: ors, version, description
├── bin/ors                      # dispatcher (on PATH when enabled)
├── skills/
│   ├── research/SKILL.md        # /ors:research  (disable-model-invocation)
│   ├── report/SKILL.md          # /ors:report    (disable-model-invocation)
│   ├── dashboard/SKILL.md       # /ors:dashboard (disable-model-invocation)
│   └── _flows/{goal,loop,process,review}.md   # internal, referenced by name
├── scripts/                     # engine (unchanged behavior, DOCS_BASE-aware)
├── public/{index.html,dashboard.html}
└── tests/                       # existing + new
```

- `plugin.json`: minimal — `name: "ors"`, `description`, `version: "0.1.0"`.
  Skills namespace as `/ors:research` etc.
- The three user-facing skills are side-effecting → `disable-model-invocation:
  true` (the model must not auto-launch a research run / start a server).
- `_flows/*.md` are the former `.claude/{goal,loop,process,review}.md`, kept as
  internal procedure docs referenced by `research`/`report` ("run the goal loop
  as defined in `_flows/goal.md`"), with all `python3 scripts/X.py` → `ors`.
- `research/SKILL.md` body = the former `.claude/research.md` bootstrap, calling
  `ors plan apply` / `ors runlog start` / `ors meter update`, then the goal loop.
- Backward-compat: leave `.claude/research.md` etc. as thin pointers OR remove
  them (plugin version takes precedence); decided during the plan — default is
  to move them into `skills/` and delete the originals to avoid drift.

### Metering wiring

`ors meter update` must read real `output_tokens` from this session's transcript
(`~/.claude/projects/<project-slug>/<session>.jsonl`) rather than the subagent
estimate. Because each goal-loop cycle's `ors meter update` runs in a *separate*
Bash call (shells don't persist), the transcript path is discovered and exported
**inside `bin/ors`** (newest `*.jsonl` for the cwd's project slug), not in a
one-off skill step — so every cycle is metered, not just the first. (Plan
refinement over the original "export in research/SKILL.md".) If no transcript is
found, metering falls back to the per-cycle subagent estimate and the cycle cap
remains the backstop.

### Dashboard skill

`/ors:dashboard` launches `graph_view_server.py` against the target:

```
GV_GRAPH="$PWD/.graphify/graph.json" GV_STATE="$PWD/.research/state.json" \
GV_DASHBOARD="${CLAUDE_PLUGIN_ROOT}/public/dashboard.html" \
GV_HTML="${CLAUDE_PLUGIN_ROOT}/public/index.html" \
  python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph_view_server.py" [--port N]
```

Server already supports these env vars (no server code change beyond confirming
defaults). Manual launch only (not auto-started by `/ors:research`).

## Data flow

```
/ors:research "q" (cwd = target)
  → ors plan apply           → <target>/.research/state.json (goal, plan, gaps, budget)
  → ors runlog start; ors meter update (baseline)
  → goal loop (_flows/goal.md):
      ors decide --apply      → phase + search/process/goal_met
      ors search --topic …    → sources into <target>/.research/docs/NN-slug/… (via inbox)
      ors ingest …            → corpus in state, graph dirty
      graphify --update        → <target>/.graphify/graph.json
      ors dim eligible/accept  → plan growth
      ors meter update         → budget.run.tokens_spent
    until decide.stop (plateau | budget | cycle cap)
  → findings in <target>/.research/findings/, SYNTHESIS.md
/ors:report  → narrative from goal+plan+findings
/ors:dashboard → live graph UI against <target>
```

## Testing

1. **`bin/ors` dispatcher** (`tests/test_ors_dispatch.sh`): verb→script
   resolution (python + shell), unknown-verb exit 2, `REPO_ROOT`/`DOCS_BASE`
   defaults exported, runs from its own dir regardless of cwd.
2. **`DOCS_BASE` namespacing** (`tests/test_docs_base.sh`): with
   `DOCS_BASE=.research/docs`, ingest routes a source to
   `<root>/.research/docs/NN-slug/sources/`; promote writes
   `<root>/.research/docs/findings/…` + `SYNTHESIS.md`.
3. **Plugin structure** (`tests/test_plugin_manifest.sh` or py): `plugin.json`
   parses, has `name`/`description`; each `skills/*/SKILL.md` has frontmatter
   `name` + `description`; side-effecting skills set
   `disable-model-invocation: true`; no `python3 scripts/` literals remain in
   `skills/**` (all migrated to `ors`).
4. **Regression:** the existing unit suite + 4 shell smokes + `check_integrity`
   updated to the `.research/docs` convention and green. Tests that asserted
   `docs/...` paths get updated to `.research/docs/...`.
5. **Live target run (manual, in the plan's final task):** `/ors:research` from
   a throwaway target dir distinct from the ORS repo; confirm artifacts land
   under the target, not the ORS repo. (Extends the Gap-1 live validation to
   the packaged/target path.)

## Risks & mitigations

- **graphify absent on target machine** → graph step + dashboard degrade; the
  loop still produces cited findings (graph is enrichment). Documented prereq;
  `research/SKILL.md` notes it.
- **`${CLAUDE_PLUGIN_ROOT}` changes on plugin update** → never write state there
  (we don't; all state under target). Re-`/reload-plugins` after an update.
- **Protected `public/dashboard.html`** → not modified; if a change is ever
  needed, ask first (handoff rule).
- **Convention migration churn** → `DOCS_BASE` default is the single switch;
  legacy ORS `docs/01-10` dirs become stale artifacts (not migrated — out of
  scope; new runs use `.research/docs`).

## Out of scope

- Marketplace/semver distribution (personal local only).
- Migrating the legacy `docs/01-10` corpus into `.research/docs`.
- Changing graphify itself (its `.graphify` location is taken as given).
- The agentic content quality of `process`/`report` drafting (unchanged from A).

## Open questions (resolve in the plan, not blockers)

- **Final `ors` verb aliases** (decide→orchestrator, dim→dimension_gate, etc.)
  — fixed during implementation against the actual script CLIs; the generic
  basename resolver is the fallback.

## Cross-check (per global instruction)

Verified against the codebase as it is on 2026-06-29:

- **Plugin `bin/` on PATH + `${CLAUDE_PLUGIN_ROOT}`** — confirmed against
  `code.claude.com/docs/en/plugins-reference.md` (fetched this session): `bin/`
  files "invokable as bare commands in any Bash tool call while the plugin is
  enabled"; `${CLAUDE_PLUGIN_ROOT}` substituted inline in skill content.
- **Engine root-awareness** — `state.py`/`orchestrator.py`/`plan.py`/`meter.py`/
  `dimension_gate.py` take `--root` (verified via `--help` + Gap-1 live run).
- **Shell flows honor `REPO_ROOT`** — `gather.sh:8`, `search_flow.sh:8`,
  `ingest_flow.sh:7`, `ingest.sh:7` all `ROOT="${REPO_ROOT:-…}"`.
- **`docs/` migration surface** — `promote.py:8-9`, `ingest.sh:14`,
  `lib.sh:15/18/21`, `gather.sh:34` (cosmetic); `process.md`/`loop.md` literals.
  `verify_run.py` "findings" hits are an unrelated local variable, not the path.
- **Dashboard env-parametrized** — `graph_view_server.py:199-207` reads
  `GV_GRAPH`/`GV_HTML`/`GV_STATE`/`GV_DASHBOARD` with root-relative defaults.
- **Internal consistency** — execution model (cwd==target) is consistent across
  dispatcher (no `--root` injection), shell flows (`REPO_ROOT=$PWD`), and
  graphify (runs in cwd). DOCS_BASE default is the single namespacing switch
  used uniformly.
- **Prior specs** — extends `2026-06-28-planner-bootstrap-design.md` (the
  engine); does not contradict it. A was "built root-aware on purpose" so B is
  extraction + a packaging shell, as that spec's handoff anticipated.
- **No discrepancies that block the plan.** The two Open questions above are
  deliberately deferred to implementation, not unresolved contradictions.
