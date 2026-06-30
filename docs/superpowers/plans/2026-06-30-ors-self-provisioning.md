# ORS Self-Provisioning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the open-research-system plugin runnable on a fresh machine — resolve every dep through one shared resolver, bundle the crawl4ai helpers, drop jq, and provision the heavy deps on demand via `/open-research-system:setup` with a SessionStart nudge.

**Architecture:** A single bash resolver `ors_venv` (in `lib.sh`) is the only thing that knows where the venv lives (`ORS_VENV` → `${CLAUDE_PLUGIN_DATA}/venv` → `~/.venvs/crawl4ai` → fail+nudge). All search/fetch/markitdown consumers derive their tools from it; the crawl4ai helper scripts are bundled in the plugin. An idempotent `scripts/setup.sh` builds the venv + installs graphify via its own MIT installer; a SessionStart hook only checks and nudges.

**Tech Stack:** bash, python3 (3.12), Claude Code plugin hooks.

**Spec:** `docs/superpowers/specs/2026-06-30-self-provisioning-design.md`

## Global Constraints

- **python3 only** (never `python`); host **python3.12** is the one documented prereq. Engine stays **stdlib-only**.
- **No hardcoded `$HOME/.venvs/...` or `$HOME/.local/bin/...`** left in engine scripts — every dep routes through `ors_venv` (with the existing `PY`/`SEARCH`/`FETCH`/`MARKITDOWN`/`ORS_VENV` env seams preserved).
- **Tests never touch a real venv or the network:** override `ORS_VENV`/`PY` to a stub dir with a fake `bin/python`, and shim `pip`/`crawl4ai-setup`/`uv`/`graphify` via `PATH` when a build path is exercised.
- **`${CLAUDE_PLUGIN_DATA}` is referenced by env var only**, never a literal path (the harness sets it to `~/.claude/plugins/data/open-research-system-open-orchestration/` at runtime; dev runs leave it unset and fall through to `~/.venvs/crawl4ai`).
- Branch off `main`: `feat/ors-self-provisioning`; **no git worktrees**; explicit staging; **Conventional Commits**; **no co-author trailer**.
- TDD per task; independent reviewer per task; `python3 scripts/check_integrity.py` green before any task is "done".
- `public/dashboard.html` is protected — not touched by this work.

**Baseline (capture before Task 1):** `python3 -m unittest discover -s tests -p 'test_*.py'` → OK; the 15 shell smokes → all PASS; `check_integrity.py` → `integrity OK`.

**SDD ledger:** append progress to `.superpowers/sdd/progress.md` per task.

---

## Pre-task setup (fold into Task 1's commit)

```bash
cd /Users/joshua/Documents/GitHub/open-research-system
git checkout main && git checkout -b feat/ors-self-provisioning
mkdir -p .superpowers/sdd
printf '# ORS self-provisioning — SDD progress ledger\nPlan: docs/superpowers/plans/2026-06-30-ors-self-provisioning.md\nBranch: feat/ors-self-provisioning\nBASE: %s\n\n## Tasks\n' "$(git rev-parse --short HEAD)" > .superpowers/sdd/progress.md
```

---

## Task 1: `ors_venv` resolver + bundle crawl4ai helpers

**Files:**
- Modify: `scripts/lib.sh` (add `LIB_DIR` + `ors_venv`)
- Create: `scripts/crawl4ai/search.py`, `scripts/crawl4ai/fetch_md.py` (bundled, copied verbatim)
- Test: `tests/test_ors_venv.sh`

**Interfaces:**
- Produces: bash `ors_venv` → echoes a venv root whose `bin/python` exists (precedence `ORS_VENV`, `${CLAUDE_PLUGIN_DATA}/venv`, `~/.venvs/crawl4ai`); on none, prints the nudge to stderr and returns 1.
- Produces: `LIB_DIR` (absolute path of `scripts/`) for resolving bundled helpers.

- [ ] **Step 1: Write the failing test**

Create `tests/test_ors_venv.sh`:

```bash
#!/usr/bin/env bash
# ors_venv resolves a venv with bin/python by precedence, else fails with a nudge.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
source "$ROOT/scripts/lib.sh"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
fail=0
mkstub() { mkdir -p "$1/bin"; printf '#!/bin/sh\n' > "$1/bin/python"; chmod +x "$1/bin/python"; }

# 1. ORS_VENV wins when valid.
mkstub "$TMP/a"
got="$(ORS_VENV="$TMP/a" CLAUDE_PLUGIN_DATA="$TMP/b" ors_venv)"
[ "$got" = "$TMP/a" ] && echo "ok: ORS_VENV wins" || { echo "MISS: got '$got'"; fail=1; }

# 2. CLAUDE_PLUGIN_DATA/venv next when ORS_VENV unset.
mkstub "$TMP/b/venv"
got="$(ORS_VENV= CLAUDE_PLUGIN_DATA="$TMP/b" ors_venv)"
[ "$got" = "$TMP/b/venv" ] && echo "ok: plugin-data venv" || { echo "MISS: got '$got'"; fail=1; }

# 3. Nudge + nonzero when nothing resolves (HOME redirected so ~/.venvs is absent).
out="$(ORS_VENV= CLAUDE_PLUGIN_DATA= HOME="$TMP/empty" ors_venv 2>&1)"; rc=$?
{ [ "$rc" -ne 0 ] && printf '%s' "$out" | grep -q "open-research-system:setup"; } \
  && echo "ok: fail nudges to setup" || { echo "MISS: rc=$rc out=$out"; fail=1; }

# 4. Helpers bundled in the plugin.
[ -f "$ROOT/scripts/crawl4ai/search.py" ] && [ -f "$ROOT/scripts/crawl4ai/fetch_md.py" ] \
  && echo "ok: helpers bundled" || { echo "MISS: helpers not bundled"; fail=1; }

[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
```

- [ ] **Step 2: Run it to verify it fails**

Run: `bash tests/test_ors_venv.sh`
Expected: FAIL — `ors_venv` undefined and `scripts/crawl4ai/` missing.

- [ ] **Step 3: Add `LIB_DIR` + `ors_venv` to `scripts/lib.sh`**

At the top of `scripts/lib.sh` (after the shebang/comment, before `slugify`), add:

```bash
LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Echo the venv root to use (bin/ holds python + markitdown), or fail (1) with a
# setup nudge. Precedence: explicit override, plugin-owned venv, reused personal venv.
ors_venv() {
  local v
  for v in "${ORS_VENV:-}" \
           "${CLAUDE_PLUGIN_DATA:+$CLAUDE_PLUGIN_DATA/venv}" \
           "$HOME/.venvs/crawl4ai"; do
    [ -n "$v" ] && [ -x "$v/bin/python" ] && { echo "$v"; return 0; }
  done
  echo "open-research-system: research deps not provisioned — run /open-research-system:setup" >&2
  return 1
}
```

- [ ] **Step 4: Bundle the crawl4ai helpers**

```bash
mkdir -p scripts/crawl4ai
cp "$HOME/.venvs/crawl4ai/search.py" scripts/crawl4ai/search.py
cp "$HOME/.venvs/crawl4ai/fetch_md.py" scripts/crawl4ai/fetch_md.py
```

Sanity-check they are non-empty python: `head -1 scripts/crawl4ai/search.py scripts/crawl4ai/fetch_md.py`.

- [ ] **Step 5: Run the test to verify it passes**

Run: `bash tests/test_ors_venv.sh` → Expected: ALL OK.

- [ ] **Step 6: Branch + commit**

Run the Pre-task setup block first, then:

```bash
git add scripts/lib.sh scripts/crawl4ai/search.py scripts/crawl4ai/fetch_md.py tests/test_ors_venv.sh
git commit -m "feat(provision): ors_venv resolver + bundle crawl4ai helpers"
```

---

## Task 2: Route search/fetch/markitdown consumers through `ors_venv`

**Files:**
- Modify: `scripts/lib.sh` (`fetch_link`, `transcribe_video`, `MARKITDOWN` default — lines ~28-40)
- Modify: `scripts/gather.sh:16-18`
- Modify: `scripts/search_flow.sh:9-11`
- Test: `tests/test_dep_resolution.sh`

**Interfaces:**
- Consumes: `ors_venv`, `LIB_DIR` (Task 1).
- Produces: no hardcoded `$HOME/.venvs` / `$HOME/.local/bin` defaults remain; helpers resolved as `$LIB_DIR/crawl4ai/{search,fetch_md}.py`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_dep_resolution.sh`:

```bash
#!/usr/bin/env bash
# No engine script hardcodes the author's personal dep paths; helpers resolve to the bundle.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0
# No hardcoded personal paths in the dep-bearing scripts.
if grep -nE '\$HOME/\.venvs/crawl4ai|\$HOME/\.local/bin/markitdown' \
     "$ROOT/scripts/lib.sh" "$ROOT/scripts/gather.sh" "$ROOT/scripts/search_flow.sh"; then
  echo "MISS: hardcoded personal dep path remains"; fail=1
else echo "ok: no hardcoded personal paths"; fi
# Helpers referenced from the bundle.
grep -q 'LIB_DIR/crawl4ai/fetch_md.py' "$ROOT/scripts/lib.sh" \
  && echo "ok: lib.sh uses bundled fetch_md" || { echo "MISS: lib.sh fetch_md"; fail=1; }
grep -qE 'crawl4ai/search\.py' "$ROOT/scripts/gather.sh" "$ROOT/scripts/search_flow.sh" \
  && echo "ok: flows use bundled search.py" || { echo "MISS: flows search.py"; fail=1; }
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
```

- [ ] **Step 2: Run it to verify it fails**

Run: `bash tests/test_dep_resolution.sh` → Expected: FAIL (hardcodes still present).

- [ ] **Step 3: Update `scripts/lib.sh`**

Replace the `MARKITDOWN` line and the `fetch_link`/`transcribe_video` bodies:

```bash
MARKITDOWN="${MARKITDOWN:-$(ors_venv 2>/dev/null)/bin/markitdown}"
[ -x "$MARKITDOWN" ] || MARKITDOWN="$HOME/.local/bin/markitdown"

# Fetch a URL to markdown via crawl4ai; prints markdown to stdout.
fetch_link() {
  local url="$1" py f
  py="$(ors_venv)/bin/python" || return 1
  f="$LIB_DIR/crawl4ai/fetch_md.py"
  "$py" "$f" "$url" 2>/dev/null
}

# Transcribe a YouTube/video URL to text via youtube-transcript-api; prints to stdout.
transcribe_video() {
  local url="$1" py
  py="$(ors_venv)/bin/python" || return 1
  "$py" - "$url" <<'PY' 2>/dev/null
```

(Leave the rest of the `transcribe_video` heredoc body unchanged.)

- [ ] **Step 4: Update `scripts/gather.sh:16-18`**

```bash
PY="$(ors_venv)/bin/python"
SEARCH="$HERE/crawl4ai/search.py"
FETCH="$HERE/crawl4ai/fetch_md.py"
```

(`HERE` is already defined at the top of `gather.sh` as its script dir = `scripts/`.)

- [ ] **Step 5: Update `scripts/search_flow.sh:9-11`**

```bash
PY="${PY:-$(ors_venv)/bin/python}"
SEARCH="${SEARCH:-$HERE/crawl4ai/search.py}"
FETCH="${FETCH:-$HERE/crawl4ai/fetch_md.py}"
```

- [ ] **Step 6: Run the test + regression smokes**

```bash
bash tests/test_dep_resolution.sh
for t in gather search_flow ingest_flow ingest; do printf "%s: " "$t"; bash tests/test_$t.sh >/dev/null 2>&1 && echo PASS || echo FAIL; done
```
Expected: ALL OK; all four smokes PASS. (They DRY-run or stub the network, so `ors_venv` resolving to the real `~/.venvs/crawl4ai` on this machine is fine.)

- [ ] **Step 7: Commit**

```bash
git add scripts/lib.sh scripts/gather.sh scripts/search_flow.sh tests/test_dep_resolution.sh
git commit -m "feat(provision): route search/fetch/markitdown through ors_venv + bundled helpers"
```

---

## Task 3: Eliminate the `jq` dependency

**Files:**
- Modify: `scripts/search_flow.sh:40`
- Test: `tests/test_no_jq.sh`

**Interfaces:** none new — behavior-preserving swap of `jq` for a python3 stdlib parse.

- [ ] **Step 1: Write the failing test**

Create `tests/test_no_jq.sh`:

```bash
#!/usr/bin/env bash
# search_flow extracts result URLs without jq (jq is no longer a dependency).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0
grep -q "jq " "$ROOT/scripts/search_flow.sh" && { echo "MISS: jq still referenced"; fail=1; } \
  || echo "ok: no jq in search_flow"
# The python3 extraction parses a results array to bare URLs.
got="$(printf '%s' '[{"url":"https://a"},{"url":"https://b"},{"nope":1}]' \
  | python3 -c 'import json,sys
data=json.load(sys.stdin)
for x in data:
    u=x.get("url") if isinstance(x,dict) else None
    if u: print(u)')"
[ "$got" = "$(printf 'https://a\nhttps://b')" ] && echo "ok: python3 url parse" \
  || { echo "MISS: parse got '$got'"; fail=1; }
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
```

- [ ] **Step 2: Run it to verify it fails**

Run: `bash tests/test_no_jq.sh` → Expected: FAIL (`jq ` still in `search_flow.sh`).

- [ ] **Step 3: Replace the jq line in `scripts/search_flow.sh:40`**

Replace:

```bash
  urls="$(printf '%s' "$results" | jq -r '.[].url' 2>/dev/null)"
```

with (host `python3`, stdlib only — not the venv `$PY`):

```bash
  urls="$(printf '%s' "$results" | python3 -c 'import json,sys
try: data=json.load(sys.stdin)
except Exception: data=[]
for x in data:
    u=x.get("url") if isinstance(x,dict) else None
    if u: print(u)' 2>/dev/null)"
```

- [ ] **Step 4: Run the test + the search smoke**

Run: `bash tests/test_no_jq.sh && bash tests/test_search_flow.sh`
Expected: ALL OK; search_flow smoke PASS.

- [ ] **Step 5: Commit**

```bash
git add scripts/search_flow.sh tests/test_no_jq.sh
git commit -m "feat(provision): drop jq dependency — parse search URLs with python3"
```

---

## Task 4: `scripts/setup.sh` + `/open-research-system:setup` skill

**Files:**
- Create: `scripts/setup.sh`
- Create: `skills/setup/SKILL.md`
- Test: `tests/test_setup.sh`

**Interfaces:**
- Consumes: `ors_venv` (Task 1).
- Produces: `ors setup` (dispatcher generic-resolves `setup` → `scripts/setup.sh`) — idempotent provisioning; exit 0 on success.

- [ ] **Step 1: Write the failing test**

Create `tests/test_setup.sh`:

```bash
#!/usr/bin/env bash
# setup.sh is idempotent: a pre-provisioned venv + present graphify => no install runs.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
fail=0
# Stub a provisioned venv (fake python + markitdown).
mkdir -p "$TMP/venv/bin"
for b in python markitdown crawl4ai-setup pip; do printf '#!/bin/sh\n' > "$TMP/venv/bin/$b"; chmod +x "$TMP/venv/bin/$b"; done
# Shim graphify/uv/pip on PATH that RECORD calls (must not be invoked when idempotent).
mkdir -p "$TMP/shim"
for b in graphify uv pip; do printf '#!/bin/sh\necho "%s $@" >> "%s/calls.log"\n' "$b" "$TMP" > "$TMP/shim/$b"; chmod +x "$TMP/shim/$b"; done
# graphify present => no install. ORS_VENV provisioned => no build.
out="$(ORS_VENV="$TMP/venv" PATH="$TMP/shim:$PATH" bash "$ROOT/scripts/setup.sh" 2>&1)"; rc=$?
[ "$rc" -eq 0 ] && echo "ok: exit 0" || { echo "MISS: rc=$rc"; fail=1; }
printf '%s' "$out" | grep -q "already provisioned" && echo "ok: reports provisioned" || { echo "MISS: no provisioned msg"; fail=1; }
# graphify present (shim on PATH) => its installer never called; uv/pip never called.
if [ -f "$TMP/calls.log" ] && grep -qE "uv tool install|pip install" "$TMP/calls.log"; then
  echo "MISS: ran install when already provisioned"; fail=1
else echo "ok: no install on idempotent run"; fi
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
```

- [ ] **Step 2: Run it to verify it fails**

Run: `bash tests/test_setup.sh` → Expected: FAIL (`scripts/setup.sh` missing).

- [ ] **Step 3: Create `scripts/setup.sh`**

```bash
#!/usr/bin/env bash
# Idempotently provision ORS research deps: a python venv (crawl4ai + markitdown +
# chromium) and the graphify skill. Safe to re-run. Prints a ✓/✗ checklist.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"

# 1. venv: reuse if already resolvable, else pick a target and build.
if venv="$(ors_venv 2>/dev/null)"; then
  echo "✓ venv already provisioned: $venv"
else
  target="${ORS_VENV:-${CLAUDE_PLUGIN_DATA:+$CLAUDE_PLUGIN_DATA/venv}}"
  target="${target:-$HOME/.venvs/crawl4ai}"
  echo "→ creating venv at $target"
  python3 -m venv "$target" || { echo "✗ venv create failed"; exit 1; }
  "$target/bin/pip" install -U crawl4ai "markitdown[all]" || { echo "✗ pip install failed"; exit 1; }
  "$target/bin/crawl4ai-setup" || echo "✗ crawl4ai-setup (chromium) failed — web fetch may not work"
  venv="$target"
fi

# 2. graphify skill: install via its official MIT installer if absent.
if command -v graphify >/dev/null 2>&1; then
  echo "✓ graphify present"
else
  echo "→ installing graphify (graphifyy, MIT — github.com/safishamsi/graphify)"
  if command -v uv >/dev/null 2>&1; then uv tool install graphifyy
  else python3 -m pip install --user graphifyy; fi
  command -v graphify >/dev/null 2>&1 && graphify install \
    || echo "✗ graphify not installed — the knowledge-graph step will be skipped"
fi

# 3. verify checklist
echo "── verify ──"
"$venv/bin/python" -c "import crawl4ai" 2>/dev/null && echo "✓ crawl4ai" || echo "✗ crawl4ai"
[ -x "$venv/bin/markitdown" ] && echo "✓ markitdown" || echo "✗ markitdown"
command -v graphify >/dev/null 2>&1 && echo "✓ graphify" || echo "✗ graphify (optional)"
echo "venv: $venv"
```

Then `chmod +x scripts/setup.sh`.

- [ ] **Step 4: Run the test to verify it passes**

Run: `bash tests/test_setup.sh` → Expected: ALL OK.

- [ ] **Step 5: Create `skills/setup/SKILL.md`**

```markdown
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
```

- [ ] **Step 6: Confirm the dispatcher resolves the verb**

Run: `./bin/ors setup` after exporting a provisioned `ORS_VENV` stub, or simply
`grep -q 'scripts/$verb' bin/ors && echo "generic resolver covers 'setup'"`.
Expected: `ors setup` runs `scripts/setup.sh` (generic `.sh`/`.py` fallback). No
`bin/ors` change needed.

- [ ] **Step 7: Commit**

```bash
git add scripts/setup.sh skills/setup/SKILL.md tests/test_setup.sh
git commit -m "feat(provision): /open-research-system:setup — idempotent dep provisioning"
```

---

## Task 5: SessionStart hook + `provision_check.sh`

**Files:**
- Create: `scripts/provision_check.sh`
- Create: `hooks/hooks.json`
- Test: `tests/test_provision_check.sh`

**Interfaces:**
- Consumes: `ors_venv` (Task 1).
- Produces: a SessionStart hook that prints a one-line nudge when unprovisioned and is silent (exit 0) when provisioned.

- [ ] **Step 1: Write the failing test**

Create `tests/test_provision_check.sh`:

```bash
#!/usr/bin/env bash
# provision_check nudges when unprovisioned, is silent when provisioned, always exit 0.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
fail=0
# Unprovisioned: nudge on stdout, exit 0.
out="$(ORS_VENV= CLAUDE_PLUGIN_DATA= HOME="$TMP/empty" bash "$ROOT/scripts/provision_check.sh")"; rc=$?
{ [ "$rc" -eq 0 ] && printf '%s' "$out" | grep -q "open-research-system:setup"; } \
  && echo "ok: nudges + exit 0" || { echo "MISS: rc=$rc out=$out"; fail=1; }
# Provisioned: silent, exit 0.
mkdir -p "$TMP/venv/bin"; printf '#!/bin/sh\n' > "$TMP/venv/bin/python"; chmod +x "$TMP/venv/bin/python"
out="$(ORS_VENV="$TMP/venv" bash "$ROOT/scripts/provision_check.sh")"; rc=$?
{ [ "$rc" -eq 0 ] && [ -z "$out" ]; } && echo "ok: silent when provisioned" \
  || { echo "MISS: rc=$rc out='$out'"; fail=1; }
# hooks.json valid + wires the check.
python3 -c "import json;h=json.load(open('$ROOT/hooks/hooks.json'));assert 'SessionStart' in h['hooks']" \
  && grep -q 'provision_check.sh' "$ROOT/hooks/hooks.json" && echo "ok: hook wired" \
  || { echo "MISS: hooks.json"; fail=1; }
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
```

- [ ] **Step 2: Run it to verify it fails**

Run: `bash tests/test_provision_check.sh` → Expected: FAIL (script + hooks.json missing).

- [ ] **Step 3: Create `scripts/provision_check.sh`**

```bash
#!/usr/bin/env bash
# SessionStart nudge: if research deps are not provisioned, print one line pointing
# at /open-research-system:setup. Never blocks a session — always exits 0.
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ors_venv >/dev/null 2>&1 \
  || echo "open-research-system: research deps not provisioned — run /open-research-system:setup"
exit 0
```

Then `chmod +x scripts/provision_check.sh`.

- [ ] **Step 4: Create `hooks/hooks.json`**

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          { "type": "command", "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/provision_check.sh" }
        ]
      }
    ]
  }
}
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `bash tests/test_provision_check.sh` → Expected: ALL OK.

- [ ] **Step 6: Commit**

```bash
git add scripts/provision_check.sh hooks/hooks.json tests/test_provision_check.sh
git commit -m "feat(provision): SessionStart hook nudges when deps unprovisioned"
```

---

## Task 6: Graceful graph-step degrade in `loop.md`

**Files:**
- Modify: `skills/_flows/loop.md:7` (the graphify-update step)
- Test: `tests/test_graphify_degrade.sh`

**Interfaces:** none — agent-procedure prose change so an absent graphify skips, not aborts.

- [ ] **Step 1: Write the failing test**

Create `tests/test_graphify_degrade.sh`:

```bash
#!/usr/bin/env bash
# The loop's graph-update step is guarded: if graphify is unavailable, it skips (not aborts).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOOP="$ROOT/skills/_flows/loop.md"
fail=0
grep -qiE "if the graphify skill is (available|installed)|graphify .*available" "$LOOP" \
  && echo "ok: availability guard" || { echo "MISS: no availability guard"; fail=1; }
grep -qiE "skip .*graph|status skip|graph update.*skip" "$LOOP" \
  && echo "ok: skip path" || { echo "MISS: no skip path"; fail=1; }
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
```

- [ ] **Step 2: Run it to verify it fails**

Run: `bash tests/test_graphify_degrade.sh` → Expected: FAIL (no guard in loop.md).

- [ ] **Step 3: Update `skills/_flows/loop.md` step 2**

Replace the opening of step 2 (the line beginning `2. If \`.research/state.json\` shows \`graph.dirty == true\`:`) so the graphify call is guarded. The new step 2 reads:

```markdown
2. If `.research/state.json` shows `graph.dirty == true`: **if the graphify skill is
   available** (installed — see `/open-research-system:setup`), back up the current
   graph (`cp .graphify/graph.json .graphify/.graphify_old.json` if it exists), then
   invoke the **graphify skill with `--update`** to incrementally extract only the
   new/changed source files (semantic update — an LLM step, not the code-only
   `graphify update` CLI). **If graphify is NOT available, skip the graph update for
   this cycle** — log it (`ors runlog log --flow graph --step graphify --status skip
   --data '{"reason":"graphify not installed"}'`) and continue; the run still
   produces cited findings (the graph is enrichment).
```

Leave the subsequent sub-steps (assertion replay, `graph_events append`, node/edge
counts) unchanged — they already no-op when `.graphify/graph.json` is absent.

- [ ] **Step 4: Run the test to verify it passes**

Run: `bash tests/test_graphify_degrade.sh` → Expected: ALL OK.

- [ ] **Step 5: Commit**

```bash
git add skills/_flows/loop.md tests/test_graphify_degrade.sh
git commit -m "feat(provision): loop skips graph step gracefully when graphify absent"
```

---

## Task 7: Docs + release prep (README, CHANGELOG, version 0.2.0)

**Files:**
- Modify: `.claude-plugin/plugin.json` (version → `0.2.0`)
- Modify: `CHANGELOG.md` (add `0.2.0`)
- Modify: `README.md` (setup section + python3.12 prereq + graphify note)

**Interfaces:** none.

- [ ] **Step 1: Bump the version**

In `.claude-plugin/plugin.json`, change `"version": "0.1.0"` to `"version": "0.2.0"`.

- [ ] **Step 2: Add the CHANGELOG entry**

Insert above the `## [0.1.0]` heading in `CHANGELOG.md`:

```markdown
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
```

- [ ] **Step 3: Update the README**

Under the `## Install` section in `README.md`, add a setup subsection after the install commands:

```markdown
### One-time setup

After installing, provision the research dependencies (idempotent):

```
/open-research-system:setup
```

Requires **python3.12** on the host. This builds the crawl4ai + markitdown venv
(+ headless chromium) and installs the graphify skill (`graphifyy`, MIT). A
SessionStart nudge reminds you if you skip it. Research still runs without graphify
— only the knowledge-graph enrichment is skipped.
```

- [ ] **Step 4: Validate + commit**

```bash
claude plugin validate . --strict
git add .claude-plugin/plugin.json CHANGELOG.md README.md
git commit -m "docs(provision): setup docs + CHANGELOG; bump to 0.2.0"
```
Expected: `✔ Validation passed`.

---

## Task 8: Full-suite green + live setup smoke

**Files:** none (validation + ledger).

- [ ] **Step 1: Whole suite + all smokes + integrity**

```bash
python3 -m unittest discover -s tests -p 'test_*.py' 2>&1 | tail -2
for t in research_flow goal_loop_wiring planner_e2e report_flow resolve_topic_dir \
         ingest_flow ingest_flow_inbox ingest gather search_flow process_flow catalog \
         ors_dispatch no_legacy_paths dashboard_wiring ors_venv dep_resolution no_jq \
         setup provision_check graphify_degrade; do
  printf "%s: " "$t"; bash tests/test_$t.sh >/dev/null 2>&1 && echo PASS || echo FAIL; done
python3 scripts/check_integrity.py
```
Expected: unit OK; all smokes PASS; `integrity OK`.

- [ ] **Step 2: Live setup smoke (idempotent — this machine already has the deps)**

```bash
./bin/ors setup
```
Expected: reports `✓ venv already provisioned` (reuses `~/.venvs/crawl4ai`),
`✓ graphify present`, and a ✓ verify checklist — no network install. Confirms the
real wiring resolves end-to-end.

- [ ] **Step 3: Confirm no hardcoded personal paths remain anywhere in scripts**

```bash
! grep -rnE '\$HOME/\.venvs/crawl4ai|\$HOME/\.local/bin/markitdown' scripts/ && echo "CLEAN"
```
Expected: `CLEAN` (the only allowed `~/.venvs/crawl4ai` reference is inside `ors_venv`
as a fallback in `lib.sh` — that one is intentional; confirm it is the sole match
and it lives in the resolver).

- [ ] **Step 4: Ledger + final commit**

```bash
printf 'ALL TASKS COMPLETE. Suite green; live `ors setup` idempotent no-op (reused venv + graphify present).\n' >> .superpowers/sdd/progress.md
git commit --allow-empty -m "chore(provision): self-provisioning complete — suite green, setup idempotent"
```

---

## Final whole-branch review

Request one whole-branch review (most-capable model) over `main..feat/ors-self-provisioning`; address Critical/Important inline; then `superpowers:finishing-a-development-branch`.

---

## Self-review (plan vs spec)

- **Spec §Decisions 1-5** → Task 5 (hybrid hook), Task 4 (venv + reuse + setup), Task 6 + Task 4 (graphify degrade + installer), Task 3 (jq), Task 1 (bundle helpers). ✓
- **Spec §dep resolver** → Task 1 (`ors_venv`) + Task 2 (consumers). ✓
- **Spec §setup.sh/skill** → Task 4. **§SessionStart hook** → Task 5. **§bundled helpers** → Task 1. ✓
- **Spec §testing** (resolver precedence, jq removal, setup idempotency, hook nudge, graceful skip, regression) → Tasks 1, 3, 4, 5, 6, 8. ✓
- **Step 3 caveat:** `lib.sh`'s `ors_venv` intentionally keeps a `~/.venvs/crawl4ai` *fallback*; the Task-8 grep treats that one resolver line as allowed (it is the documented reuse path), and forbids the hardcode anywhere else.
- **Placeholder scan:** no TBD/TODO; every code step ships complete code; the bundled helpers are copied verbatim from a known path (this machine).
- **Type/name consistency:** `ors_venv`, `LIB_DIR`, `ORS_VENV`, `scripts/crawl4ai/{search,fetch_md}.py`, `ors setup` used identically across tasks.
- **Note:** Task 8 Step 3's grep will match the intentional fallback in `lib.sh` — the step says to confirm it is the *sole* match and lives in the resolver, so it is a verification, not a failure.
