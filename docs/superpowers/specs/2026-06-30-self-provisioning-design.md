# ORS self-provisioning — design (sub-project C)

Make the `open-research-system` plugin **runnable, not just installable**, on a
fresh machine. Today a run needs host-side deps the plugin neither bundles nor
provisions, and the engine hardcodes the author's personal paths. This sub-project
removes those assumptions and provisions the deps on demand. Builds on sub-project
B (the plugin, `docs/superpowers/specs/2026-06-29-ors-package-design.md`, published
`open-orchestration/open-research-system` v0.1.0).

## Goal & success criteria

From a fresh machine with the plugin installed and **python3.12** present, the user
runs `/open-research-system:setup` once, then `/open-research-system:research`
works end-to-end. No engine script references a hardcoded `$HOME/.venvs/...` or
`$HOME/.local/bin/...` path; dep locations resolve through one shared resolver with
env overrides. A user who skips setup is nudged (not failed silently) by a
SessionStart hook.

**Done when:** a run resolves its python/search/fetch/markitdown deps via the
resolver (plugin venv → reused `~/.venvs/crawl4ai` → fail-with-nudge); `jq` is gone;
`/open-research-system:setup` is idempotent and provisions the venv + graphify;
existing suite + smokes + integrity stay green; new tests cover the resolver, the
jq removal, setup idempotency, and the hook nudge.

## Decisions (locked in brainstorming)

1. **Provisioning = hybrid.** A lightweight `SessionStart` hook only *checks* and
   *nudges* ("run `/open-research-system:setup`"); the heavy install lives in the
   explicit `/open-research-system:setup` skill. No multi-hundred-MB surprise on
   session start.
2. **Venv = plugin-owned, reuse if present.** Provision into
   `${CLAUDE_PLUGIN_DATA}/venv` (persists across updates, removed on uninstall).
   If a working `~/.venvs/crawl4ai` already exists, reuse it instead of rebuilding.
3. **graphify = installed via its own official installer.** graphify is MIT
   (Safi Shamsi, `github.com/safishamsi/graphify`), distributed as the `graphifyy`
   PyPI package + a `graphify install` CLI that writes the skill into
   `~/.claude/skills/graphify/`. It is **not** a Claude plugin, so a `plugin.json`
   `dependencies` entry cannot target it. `/setup` runs graphify's installer
   (`uv tool install graphifyy` → `graphify install`) when the skill is absent; the
   loop **degrades gracefully** if it is still missing (graph + dashboard
   graph-panel become optional enrichment; the run still produces cited findings).
4. **Eliminate jq.** Its single use (`search_flow.sh:40`) becomes a python3 one-liner.
5. **Bundle the crawl4ai helpers.** `search.py` + `fetch_md.py` (today in the
   author's venv dir) move into the plugin at `scripts/crawl4ai/`, run by whichever
   resolved venv python.

## Architecture

### The dep resolver (`scripts/lib.sh`)

A single bash helper is the only thing that knows where deps live:

```sh
# Echo the venv root to use (its bin/ holds python + markitdown), or fail (1) so the
# caller can nudge the user to run /open-research-system:setup. Precedence: explicit
# override, plugin-owned venv, reused personal venv.
ors_venv() {
  for v in "${ORS_VENV:-}" \
           "${CLAUDE_PLUGIN_DATA:+$CLAUDE_PLUGIN_DATA/venv}" \
           "$HOME/.venvs/crawl4ai"; do
    [ -n "$v" ] && [ -x "$v/bin/python" ] && { echo "$v"; return 0; }
  done
  echo "ors: research deps not provisioned — run /open-research-system:setup" >&2
  return 1
}
```

Consumers derive everything from it:
- python: `"$(ors_venv)/bin/python"`
- markitdown: `MARKITDOWN="${MARKITDOWN:-$(ors_venv)/bin/markitdown}"` (env override
  still honored; falls back inside the venv).
- search/fetch helpers: `"$HERE/crawl4ai/search.py"` and
  `"$HERE/crawl4ai/fetch_md.py"` (plugin-bundled; `HERE` = the scripts dir).

This replaces the hardcodes at `lib.sh:32,38` (`fetch_link`, `transcribe_video`),
`gather.sh:16-18`, and the `PY/SEARCH/FETCH` defaults in `search_flow.sh:9-11`. All
keep their existing env-override seams (`PY`, `SEARCH`, `FETCH`, `MARKITDOWN`) for
tests and power users; only the *defaults* change to route through `ors_venv` +
bundled helpers.

`CLAUDE_PLUGIN_DATA` is set only when ORS runs as an installed plugin; unset in
dev/in-repo runs, where the resolver falls through to `~/.venvs/crawl4ai`. Tests
override `ORS_VENV`/`PY` to a stub so they never touch a real venv or the network.

### `scripts/setup.sh` + `skills/setup/SKILL.md`

`/open-research-system:setup` (`disable-model-invocation: true`) runs
`scripts/setup.sh`, which is idempotent and prints a human-readable status. It:

1. **Resolve/choose the venv.** If `ors_venv` already succeeds, report "provisioned"
   and skip the build (idempotent). Else pick the target: `${CLAUDE_PLUGIN_DATA}/venv`
   when `CLAUDE_PLUGIN_DATA` is set, otherwise `~/.venvs/crawl4ai`.
2. **Create + populate the venv:** `python3 -m venv <target>`; `<target>/bin/pip
   install -U crawl4ai "markitdown[all]"`; `<target>/bin/crawl4ai-setup` (downloads
   headless chromium). Each step's failure is reported, not swallowed.
3. **Install graphify if absent:** if `command -v graphify` fails, run
   `uv tool install graphifyy` (fall back to `python3 -m pip install --user graphifyy`
   if `uv` is absent), then `graphify install`. If graphify still isn't resolvable,
   warn that the knowledge-graph step will be skipped — do not fail the run.
4. **Verify + report:** check the venv python imports crawl4ai, `markitdown` runs,
   chromium is present, and graphify is on PATH; print a checklist with ✓/✗ per dep.

### SessionStart hook (`hooks/hooks.json`)

A presence check only — never installs:

```json
{ "hooks": { "SessionStart": [ { "hooks": [ { "type": "command",
  "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/provision_check.sh" } ] } ] } }
```

`scripts/provision_check.sh` calls `ors_venv` (quietly); on failure it prints one
line: `open-research-system: research deps not provisioned — run /open-research-system:setup`.
It always exits 0 (a nudge must never block a session) and emits nothing when
provisioned.

### Bundled crawl4ai helpers

`scripts/crawl4ai/search.py` and `scripts/crawl4ai/fetch_md.py` are copied from the
author's venv into the plugin verbatim (they are plain scripts that import
crawl4ai / scrape DuckDuckGo). The resolved venv python runs them; the plugin owns
the code, the venv owns the libraries.

## Data flow

```
install plugin → /open-research-system:setup (once):
    ors_venv? no → create ${CLAUDE_PLUGIN_DATA}/venv (or reuse ~/.venvs/crawl4ai)
      → pip install crawl4ai markitdown[all] → crawl4ai-setup (chromium)
    graphify? no → uv tool install graphifyy → graphify install
    verify → ✓ checklist
session start (hook): ors_venv? no → print one-line nudge ; yes → silent
/open-research-system:research → ors search/ingest:
    PY=$(ors_venv)/bin/python  runs  scripts/crawl4ai/search.py + fetch_md.py
    markitdown=$(ors_venv)/bin/markitdown  for document ingest
    loop graphify step → present? run : skip (findings still produced)
```

## Testing

1. **Resolver precedence** (`tests/test_ors_venv.sh`): with a stub `bin/python`,
   assert `ORS_VENV` wins, then `CLAUDE_PLUGIN_DATA/venv`, then `~/.venvs/crawl4ai`;
   and that an all-missing case returns non-zero with the nudge on stderr.
2. **jq removal** (`tests/test_search_flow.sh` extended or new): the URL extraction
   from a search-results JSON works via python3 with no `jq` on PATH (run a slice
   with `PATH` scrubbed of jq, or assert no `jq` token remains in `search_flow.sh`).
3. **Setup idempotency** (`tests/test_setup.sh`): with a pre-provisioned stub venv
   (fake `bin/python`), `setup.sh` reports "already provisioned" and runs no
   install command (assert via a `pip`/`crawl4ai-setup` shim that records calls).
4. **Hook nudge** (`tests/test_provision_check.sh`): unprovisioned (scrubbed env) →
   prints the nudge, exit 0; provisioned (stub venv) → prints nothing, exit 0.
5. **Graceful graph skip** — covered by asserting `skills/_flows/loop.md` guards the
   graphify step on presence (a `test_no_legacy_paths`-style grep that the graph
   step is conditional), so an absent graphify never aborts the loop.
6. **Regression:** the full unit suite + shell smokes + `check_integrity` stay green.
   The crawl4ai-helper move keeps `search_flow`/`gather` smokes passing (they already
   stub or DRY-run the network).

## Risks & mitigations

- **No network / no python3.12 on host** → setup reports the failed step in its
  checklist; documented as the one hard prereq. `crawl4ai-setup` (chromium) is the
  slowest/largest step; it runs only in explicit setup.
- **`uv` absent** → setup falls back to `pip install --user graphifyy`.
- **graphify still missing after setup** → loop skips the graph step; run still
  yields cited findings; dashboard graph panel is empty but queue/loop work.
- **Reused `~/.venvs/crawl4ai` is stale/broken** → `ors_venv` only checks for
  `bin/python`; a deeper breakage surfaces at first search. `/setup --rebuild`
  (force a fresh `${CLAUDE_PLUGIN_DATA}/venv`) is the escape hatch.
- **Protected `public/dashboard.html`** untouched by this sub-project.

## Out of scope

- Bundling a python interpreter (the venv needs a host python3.12).
- Republishing or vendoring graphify (use its official MIT installer).
- A Claude `plugin.json` `dependencies` entry for graphify (it is not a plugin).
- Windows-specific provisioning beyond what crawl4ai/graphify already document.

## Cross-check (per global instruction)

Verified against the codebase + canonical docs on 2026-06-30:

- **Hardcoded dep paths** — `lib.sh:28` (`MARKITDOWN`, already env-seamed), `:32,38`
  (crawl4ai hardcoded), `gather.sh:16-18` (hardcoded), `search_flow.sh:9-11`
  (`PY/SEARCH/FETCH` env-seamed, default to `$HOME/.venvs/crawl4ai`). All confirmed.
- **jq** — single use at `search_flow.sh:40` (`jq -r '.[].url'`); confirmed the only
  occurrence in `scripts/*.sh`.
- **crawl4ai helpers** — `~/.venvs/crawl4ai/{search.py,fetch_md.py}` exist; to be
  bundled at `scripts/crawl4ai/`.
- **`${CLAUDE_PLUGIN_DATA}`** — canonical (`plugins-reference.md`): resolves to
  `~/.claude/plugins/data/{id}/`, persists across updates, intended for venvs,
  created on first reference; removed on uninstall (unless `--keep-data`).
- **SessionStart hook + `${CLAUDE_PLUGIN_ROOT}`** — canonical hook event; command
  substitutes `${CLAUDE_PLUGIN_ROOT}` inline. Confirmed.
- **graphify** — MIT (Safi Shamsi); `uv tool install graphifyy` → `graphify install`
  writes `~/.claude/skills/graphify/SKILL.md`; repo `safishamsi/graphify` default
  branch `v8` has **no** `.claude-plugin/` manifest (not a Claude plugin), so the
  `dependencies`-field path is correctly ruled out.
- **Internal consistency** — every consumer routes through `ors_venv`; the SessionStart
  hook and the skills share the same resolver; the venv location decision (plugin-data,
  reuse personal) is applied uniformly in the resolver and `setup.sh`.
- **Prior specs** — extends B (the plugin) without contradiction; B deliberately left
  deps as host prereqs (`README` "Prerequisites"), which this sub-project provisions.
- **No blocking discrepancies.**
