# Loop Engine — Search Flow + Budget Governor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build sub-project #2 of the loop-driven research engine — the autonomous search flow that drains a gap queue (within a source budget) by searching + fetching sources and dropping them into `ingest/` for the existing ingest flow to record, plus the phase-weighted budget governor that caps it.

**Architecture:** The state ledger (`scripts/state.py`) gains gap-queue ops and budget-governor ops. A new `scripts/junk.py` flags low-value fetched pages. A new `scripts/search_flow.sh` pops queued gaps, runs the existing crawl4ai `search.py`/`fetch_md.py` (paths env-overridable so tests inject offline fakes), junk-filters each result, drops the good markdown into `ingest/` (where sub-project #1's ingest flow normalizes + records it with durable IDs + graph-dirty), spends budget, and marks each gap done or re-queues it. Search runs sequentially within the source budget; parallel subagent fan-out is the loop/`/goal` layer (deferred to the C convergence).

**Tech Stack:** bash (matching existing `scripts/*.sh`), Python 3 stdlib only (`json`, `unittest`), `jq` (already installed) for parsing search JSON in shell, crawl4ai (`~/.venvs/crawl4ai`) for the real search/fetch (stubbed in tests). No new dependencies.

## Global Constraints

- Python 3 **stdlib only** — no pip, no pytest; tests use `unittest`. No new dependencies.
- Follow existing script conventions: `#!/usr/bin/env bash`, `source "$HERE/lib.sh"`, `ROOT="${REPO_ROOT:-...}"`, env-overridable `PY`/`SEARCH`/`FETCH` like `scripts/gather.sh`.
- No lint/type suppression comments anywhere (`# noqa`, `# type: ignore`, etc.).
- Search drops sources into `ingest/` (as `.md` files), NEVER directly into `docs/<topic>/sources/` — the ingest flow (sub-project #1) owns recording, durable IDs, lifecycle, and graph-dirty.
- v1 scoping (within the approved design): gaps are **human-seeded** via a `state.py add-gap` CLI (the process flow that auto-authors gaps is sub-project #3); the budget meter is **`sources_per_cycle`** (token metering waits for the `/goal` layer); the flow drains gaps **sequentially**.
- Deterministic IDs: a gap id is `gen_id("g", topic + "|" + desc)` (re-adding the same topic+desc dedups).
- Commits: no co-author trailers, no "Generated with" lines.
- Existing state schema (`scripts/state.py` `DEFAULT_STATE`): `budget` has `tokens_per_cycle, max_subagents, phase, weights{gather,deepen,synthesize each {search,ingest,process}}, spent{tokens,sources,cycle_started_at}`; `gaps` is a list. This plan ADDS `sources_per_cycle` to `budget`.

---

### Task 1: Budget governor (state.py)

**Files:**
- Modify: `scripts/state.py`
- Test: `tests/test_state.py`

**Interfaces:**
- Consumes: `load`, `save`, `load_default`, `DEFAULT_STATE` (sub-project #1).
- Produces:
  - `DEFAULT_STATE["budget"]` gains `"sources_per_cycle": 8`.
  - `budget_reset(state, now=None) -> None` — sets `state["budget"]["spent"] = {"tokens": 0, "sources": 0, "cycle_started_at": now or _now()}`.
  - `budget_remaining_sources(state) -> int` — `max(0, budget.get("sources_per_cycle", 8) - budget["spent"]["sources"])`.
  - `budget_spend_source(state, n=1) -> None` — `budget["spent"]["sources"] += n`.
  - `subagent_count(state, flow) -> int` — `round(budget["max_subagents"] * budget["weights"][budget["phase"]][flow])`.
  - CLI: `python3 scripts/state.py budget-remaining --root R` prints the integer remaining sources; `budget-reset --root R`; `budget-spend --root R --sources N`; `budget-status --root R` prints JSON `{"phase","remaining_sources","subagents":{"search","ingest","process"}}`.

- [ ] **Step 1: Write the failing tests**

```python
# append to tests/test_state.py inside the TestStateCore class
    def test_budget_reset_zeroes_spent(self):
        st = state.load_default()
        st["budget"]["spent"]["sources"] = 5
        state.budget_reset(st, now="t")
        self.assertEqual(st["budget"]["spent"], {"tokens": 0, "sources": 0, "cycle_started_at": "t"})

    def test_budget_remaining_sources(self):
        st = state.load_default()
        self.assertEqual(state.budget_remaining_sources(st), 8)  # default sources_per_cycle
        state.budget_spend_source(st, 3)
        self.assertEqual(state.budget_remaining_sources(st), 5)
        state.budget_spend_source(st, 99)
        self.assertEqual(state.budget_remaining_sources(st), 0)  # floored at 0

    def test_subagent_count_follows_phase_weights(self):
        st = state.load_default()  # phase "gather": search 0.7, process 0.0; max_subagents 8
        self.assertEqual(state.subagent_count(st, "search"), 6)   # round(8*0.7)=6 (banker's: round(5.6)=6)
        self.assertEqual(state.subagent_count(st, "process"), 0)
        st["budget"]["phase"] = "synthesize"
        self.assertEqual(state.subagent_count(st, "process"), 6)  # round(8*0.8)=6
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_state -v`
Expected: FAIL — `AttributeError: module 'state' has no attribute 'budget_reset'`.

- [ ] **Step 3: Write minimal implementation**

```python
# in scripts/state.py: add "sources_per_cycle": 8 to DEFAULT_STATE["budget"], next to "max_subagents"
# DEFAULT_STATE["budget"] becomes:
#     "budget": {
#         "tokens_per_cycle": 200000,
#         "sources_per_cycle": 8,
#         "max_subagents": 8,
#         ...
#     },

# add these functions (after set_graph):
def budget_reset(state, now=None):
    state["budget"]["spent"] = {"tokens": 0, "sources": 0, "cycle_started_at": now or _now()}


def budget_remaining_sources(state):
    b = state["budget"]
    return max(0, b.get("sources_per_cycle", 8) - b["spent"]["sources"])


def budget_spend_source(state, n=1):
    state["budget"]["spent"]["sources"] += n


def subagent_count(state, flow):
    b = state["budget"]
    return round(b["max_subagents"] * b["weights"][b["phase"]][flow])
```

```python
# in _main, add these subcommands to the existing subparser block:
    br = sub.add_parser("budget-remaining"); br.add_argument("--root", default=".")
    brs = sub.add_parser("budget-reset"); brs.add_argument("--root", default=".")
    bsp = sub.add_parser("budget-spend"); bsp.add_argument("--root", default="."); bsp.add_argument("--sources", type=int, required=True)
    bst = sub.add_parser("budget-status"); bst.add_argument("--root", default=".")
# ...and these handlers (before the final `return 1`):
    if args.cmd == "budget-remaining":
        print(budget_remaining_sources(load(args.root))); return 0
    if args.cmd == "budget-reset":
        st = load(args.root); budget_reset(st); save(st, args.root); print("budget reset"); return 0
    if args.cmd == "budget-spend":
        st = load(args.root); budget_spend_source(st, args.sources); save(st, args.root)
        print(budget_remaining_sources(st)); return 0
    if args.cmd == "budget-status":
        st = load(args.root)
        out = {"phase": st["budget"]["phase"],
               "remaining_sources": budget_remaining_sources(st),
               "subagents": {f: subagent_count(st, f) for f in ("search", "ingest", "process")}}
        print(json.dumps(out)); return 0
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_state -v`
Expected: PASS (all prior + 3 new). The full-file run confirms adding `sources_per_cycle` to `DEFAULT_STATE` did not break any sub-project #1 budget assertion (none assert the budget sub-dict exactly, so it won't — but the run is the proof).

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py tests/test_state.py
git commit -m "feat: add phase-weighted budget governor to state ledger"
```

---

### Task 2: Gap queue ops (state.py)

**Files:**
- Modify: `scripts/state.py`
- Test: `tests/test_state.py`

**Interfaces:**
- Consumes: `load`, `save`, `load_default`, `gen_id` (sub-project #1).
- Produces:
  - `add_gap(state, *, topic, desc, origin="human", id=None) -> dict` — `gid = id or gen_id("g", topic + "|" + desc)`; if `gid` already in `state["gaps"]`, return the existing gap; else append `{"id":gid,"topic":topic,"desc":desc,"origin":origin,"status":"queued","attempts":0}` and return it.
  - `next_queued_gap(state, topic=None) -> dict | None` — the first gap whose `status == "queued"` (and, when `topic` is given, whose `topic` matches), else `None`.
  - `set_gap_status(state, gap_id, status, *, requeue=False) -> None` — find the gap by id; if `requeue` is True, set `status="queued"` and increment `attempts` (the `status` arg is ignored in this branch); otherwise set `status=status`. No-op if the id is absent.
  - CLI: `add-gap --root R --topic T --desc D [--origin O]` prints the gap id; `next-gap --root R [--topic T]` prints `id\ttopic\tdesc` for the next queued gap (optionally filtered to `topic`) or nothing (empty) if none; `set-gap --root R --id ID --status S [--requeue]` saves.

- [ ] **Step 1: Write the failing tests**

```python
# append to tests/test_state.py inside the TestStateCore class
    def test_add_gap_dedups_on_topic_desc(self):
        st = state.load_default()
        g1 = state.add_gap(st, topic="06-rag", desc="hybrid retrieval rerank")
        g2 = state.add_gap(st, topic="06-rag", desc="hybrid retrieval rerank")
        self.assertEqual(len(st["gaps"]), 1)
        self.assertEqual(g1["id"], g2["id"])
        self.assertEqual(g1["status"], "queued")
        self.assertEqual(g1["attempts"], 0)

    def test_next_queued_gap_skips_non_queued(self):
        st = state.load_default()
        state.add_gap(st, topic="a", desc="one")
        g2 = state.add_gap(st, topic="b", desc="two")
        st["gaps"][0]["status"] = "done"
        self.assertEqual(state.next_queued_gap(st)["id"], g2["id"])
        self.assertEqual(state.next_queued_gap(st, topic="b")["id"], g2["id"])
        self.assertIsNone(state.next_queued_gap(st, topic="a"))  # a's only gap is done

    def test_set_gap_status_requeue_increments_attempts(self):
        st = state.load_default()
        g = state.add_gap(st, topic="a", desc="one")
        state.set_gap_status(st, g["id"], "x", requeue=True)
        self.assertEqual(st["gaps"][0]["status"], "queued")
        self.assertEqual(st["gaps"][0]["attempts"], 1)
        state.set_gap_status(st, g["id"], "failed")
        self.assertEqual(st["gaps"][0]["status"], "failed")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_state -v`
Expected: FAIL — `AttributeError: module 'state' has no attribute 'add_gap'`.

- [ ] **Step 3: Write minimal implementation**

```python
# add to scripts/state.py (after the budget functions):
def add_gap(state, *, topic, desc, origin="human", id=None):
    gid = id or gen_id("g", topic + "|" + desc)
    for g in state["gaps"]:
        if g["id"] == gid:
            return g
    gap = {"id": gid, "topic": topic, "desc": desc, "origin": origin,
           "status": "queued", "attempts": 0}
    state["gaps"].append(gap)
    return gap


def next_queued_gap(state, topic=None):
    for g in state["gaps"]:
        if g["status"] == "queued" and (topic is None or g["topic"] == topic):
            return g
    return None


def set_gap_status(state, gap_id, status, *, requeue=False):
    for g in state["gaps"]:
        if g["id"] == gap_id:
            if requeue:
                g["status"] = "queued"
                g["attempts"] += 1
            else:
                g["status"] = status
            return
```

```python
# in _main, add subcommands:
    ag = sub.add_parser("add-gap"); ag.add_argument("--root", default=".")
    ag.add_argument("--topic", required=True); ag.add_argument("--desc", required=True)
    ag.add_argument("--origin", default="human")
    ng = sub.add_parser("next-gap"); ng.add_argument("--root", default="."); ng.add_argument("--topic", default=None)
    stg = sub.add_parser("set-gap"); stg.add_argument("--root", default=".")
    stg.add_argument("--id", required=True); stg.add_argument("--status", required=True)
    stg.add_argument("--requeue", action="store_true")
# ...and handlers:
    if args.cmd == "add-gap":
        st = load(args.root); g = add_gap(st, topic=args.topic, desc=args.desc, origin=args.origin)
        save(st, args.root); print(g["id"]); return 0
    if args.cmd == "next-gap":
        g = next_queued_gap(load(args.root), topic=args.topic)
        if g:
            print(f"{g['id']}\t{g['topic']}\t{g['desc']}")
        return 0
    if args.cmd == "set-gap":
        st = load(args.root); set_gap_status(st, args.id, args.status, requeue=args.requeue)
        save(st, args.root); print("gap updated"); return 0
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_state -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py tests/test_state.py
git commit -m "feat: add gap queue ops to state ledger"
```

---

### Task 3: Junk detection (junk.py)

**Files:**
- Create: `scripts/junk.py`
- Test: `tests/test_junk.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `is_junk(text: str) -> bool` — True when the fetched page is low-value: empty/whitespace, shorter than 200 non-whitespace chars, or contains (case-insensitive) any of: `just a moment`, `enable javascript`, `uh oh`, `captcha`, `are you a robot`, `access denied`, `403 forbidden`, `page not found`, `rate limit`.
  - CLI: `python3 scripts/junk.py check <file>` — exits 1 if the file's content is junk, 0 if clean.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_junk.py
import unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import junk


class TestIsJunk(unittest.TestCase):
    def test_clean_long_content_is_not_junk(self):
        self.assertFalse(junk.is_junk("# Real Article\n\n" + ("word " * 200)))

    def test_empty_is_junk(self):
        self.assertTrue(junk.is_junk(""))
        self.assertTrue(junk.is_junk("   \n  "))

    def test_too_short_is_junk(self):
        self.assertTrue(junk.is_junk("# Title\nthin"))

    def test_js_shell_markers_are_junk(self):
        body = "x" * 300
        self.assertTrue(junk.is_junk("Just a moment... " + body))
        self.assertTrue(junk.is_junk("Please enable JavaScript " + body))
        self.assertTrue(junk.is_junk("Uh oh! There was an error " + body))
        self.assertTrue(junk.is_junk("403 Forbidden " + body))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_junk -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'junk'`.

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/junk.py
"""Heuristic junk detection for fetched pages. Stdlib only."""
import sys
from pathlib import Path

_MARKERS = (
    "just a moment", "enable javascript", "uh oh", "captcha",
    "are you a robot", "access denied", "403 forbidden",
    "page not found", "rate limit",
)
_MIN_CHARS = 200


def is_junk(text):
    stripped = "".join(text.split())
    if len(stripped) < _MIN_CHARS:
        return True
    low = text.lower()
    return any(m in low for m in _MARKERS)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "check":
        content = Path(sys.argv[2]).read_text(encoding="utf-8", errors="replace")
        sys.exit(1 if is_junk(content) else 0)
    print("usage: junk.py check <file>", file=sys.stderr)
    sys.exit(2)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_junk -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/junk.py tests/test_junk.py
git commit -m "feat: add junk detection for fetched pages"
```

---

### Task 4: Search flow script (search_flow.sh)

**Files:**
- Create: `scripts/search_flow.sh`
- Test: `tests/test_search_flow.sh`

**Interfaces:**
- Consumes: `state.py` (`budget-remaining`, `budget-spend`, `next-gap --topic`, `set-gap`), `junk.py` (`check`), `slugify` (`lib.sh`).
- Produces: a runnable `scripts/search_flow.sh --topic <T>` that, while `budget-remaining > 0` and a queued gap **for topic T** exists, pops that gap, runs `$PY $SEARCH "<desc>" <n>` (n = min(remaining, 5)) to get `[{url,title,...}]`, fetches each url via `$PY $FETCH <url>`, drops each non-junk result into `ingest/<gapid>-<slug>-<i>.md`, spends one source of budget per kept result, and marks the gap `done` if it produced ≥1 kept source, else re-queues it (`failed` after 3 attempts). Exits 0 with a message when budget is spent or no gaps remain.
- **Topic scoping (fixes the ingest routing handoff):** because `ingest_flow.sh` routes a whole `ingest/` batch to one topic, search is run per topic. The loop runs `search_flow.sh --topic T` then `ingest_flow.sh T` for each topic with queued gaps, so every source search drops is recorded under the correct topic. `search_flow.sh` only ever drains gaps matching its `--topic`.
- Env: `PY`/`SEARCH`/`FETCH` override the crawl4ai defaults (tests inject offline fakes); `REPO_ROOT` overrides root; `PER_GAP` caps results per gap (default 5).

- [ ] **Step 1: Write the failing test**

```bash
# tests/test_search_flow.sh
#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/scripts" "$TMP/ingest" "$TMP/docs/06-x/sources"
cp "$ROOT/scripts/lib.sh" "$ROOT/scripts/state.py" "$ROOT/scripts/junk.py" \
   "$ROOT/scripts/search_flow.sh" "$TMP/scripts/"

# Fake search: ignores args, prints two results (one good, one junk).
cat > "$TMP/scripts/fake_search.py" <<'PY'
import json
print(json.dumps([{"url": "http://x/good", "title": "Good Source"},
                  {"url": "http://x/junk", "title": "Junk Source"}]))
PY
# Fake fetch: clean markdown for /good, a JS-shell page for /junk.
cat > "$TMP/scripts/fake_fetch.py" <<'PY'
import sys
url = sys.argv[1]
if url.endswith("/good"):
    print("# Good Source\n\n" + ("real content " * 60))
else:
    print("Just a moment...")
PY

# Seed a queued gap.
REPO_ROOT="$TMP" python3 "$TMP/scripts/state.py" add-gap --root "$TMP" --topic 06-x --desc "hybrid retrieval" >/dev/null

PY=python3 SEARCH="$TMP/scripts/fake_search.py" FETCH="$TMP/scripts/fake_fetch.py" REPO_ROOT="$TMP" \
  bash "$TMP/scripts/search_flow.sh" --topic 06-x || { echo "MISS: search_flow exited nonzero"; exit 1; }

fail=0
# Exactly one good source dropped into ingest/ (junk excluded).
n=$(find "$TMP/ingest" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
[ "$n" = "1" ] && echo "ok: one non-junk source in ingest/" || { echo "MISS: ingest .md count=$n"; fail=1; }
# Gap marked done; budget spent by 1.
python3 - "$TMP" <<'PY' || fail=1
import json, sys
st = json.load(open(sys.argv[1] + "/.research/state.json"))
assert st["gaps"][0]["status"] == "done", st["gaps"][0]
assert st["budget"]["spent"]["sources"] == 1, st["budget"]["spent"]
print("ok: gap done, budget spent=1")
PY
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"
exit "$fail"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/test_search_flow.sh`
Expected: FAIL — `search_flow.sh` does not exist yet, so the `cp ... "$TMP/scripts/"` errors and (under `set -uo pipefail`, no `-e`) the later `bash "$TMP/scripts/search_flow.sh"` hits "No such file"; the test exits non-zero. (The exact line that fails is the missing-script cp/run, not an assertion.)

- [ ] **Step 3: Write minimal implementation**

```bash
#!/usr/bin/env bash
# Drain one topic's gap queue within the source budget: search, fetch,
# junk-filter, drop good markdown into ingest/ for the ingest flow to record.
# Usage: search_flow.sh --topic <topic>
set -uo pipefail   # NOT -e: one bad gap/result must not abort the cycle.
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ROOT="${REPO_ROOT:-$(cd "$HERE/.." && pwd)}"
PY="${PY:-$HOME/.venvs/crawl4ai/bin/python}"
SEARCH="${SEARCH:-$HOME/.venvs/crawl4ai/search.py}"
FETCH="${FETCH:-$HOME/.venvs/crawl4ai/fetch_md.py}"
PER_GAP="${PER_GAP:-5}"
SP="python3 $HERE/state.py"

topic=""
[ "${1:-}" = "--topic" ] && topic="${2:-}"
[ -n "$topic" ] || { echo "usage: search_flow.sh --topic <topic>" >&2; exit 2; }
mkdir -p "$ROOT/ingest"

remaining="$($SP budget-remaining --root "$ROOT")"
[ "$remaining" -gt 0 ] || { echo "search: budget spent ($remaining remaining)"; exit 0; }

while [ "$remaining" -gt 0 ]; do
  line="$($SP next-gap --root "$ROOT" --topic "$topic")"
  [ -n "$line" ] || { echo "search: no queued gaps for $topic"; break; }
  gid="$(printf '%s' "$line" | cut -f1)"
  desc="$(printf '%s' "$line" | cut -f3)"
  n="$PER_GAP"; [ "$remaining" -lt "$n" ] && n="$remaining"

  results="$("$PY" "$SEARCH" "$desc" "$n" 2>/dev/null)" || results="[]"
  urls="$(printf '%s' "$results" | jq -r '.[].url' 2>/dev/null)"
  kept=0; i=0
  while IFS= read -r url; do
    [ -n "$url" ] || continue
    [ "$remaining" -gt 0 ] || break
    i=$((i+1))
    tmp="$(mktemp)"
    "$PY" "$FETCH" "$url" > "$tmp" 2>/dev/null || { rm -f "$tmp"; continue; }
    if python3 "$HERE/junk.py" check "$tmp"; then
      slug="$(slugify "$desc")"
      mv "$tmp" "$ROOT/ingest/${gid}-${slug}-${i}.md"
      kept=$((kept+1)); remaining=$((remaining-1))
    else
      rm -f "$tmp"
    fi
  done <<< "$urls"

  if [ "$kept" -gt 0 ]; then
    $SP set-gap --root "$ROOT" --id "$gid" --status done >/dev/null
    $SP budget-spend --root "$ROOT" --sources "$kept" >/dev/null
    echo "search: gap $gid -> $kept source(s) into ingest/"
  else
    $SP set-gap --root "$ROOT" --id "$gid" --status requeue --requeue >/dev/null
    # Fail permanently after 3 attempts. Default -1 if the gap vanished, so the
    # comparison never errors and a missing gap is simply not failed.
    att="$(python3 -c "import json,sys;print(next((g['attempts'] for g in json.load(open(sys.argv[1]+'/.research/state.json'))['gaps'] if g['id']==sys.argv[2]), -1))" "$ROOT" "$gid")"
    [ "$att" -ge 3 ] && $SP set-gap --root "$ROOT" --id "$gid" --status failed >/dev/null
    echo "search: gap $gid produced no non-junk sources (attempt $att)"
  fi
done
echo "Done. New sources (if any) await the ingest cycle."
```

Note on `junk.py check`: it exits **1 for junk, 0 for clean**, so `if python3 junk.py check "$tmp"; then ... (clean) ...` keeps the result. Make the script executable: `chmod +x scripts/search_flow.sh`.

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/test_search_flow.sh`
Expected: `ALL OK`, exit 0. (Offline — fake search/fetch injected via env; only one of the two fake results survives junk-filtering.)

- [ ] **Step 5: Commit**

```bash
git add scripts/search_flow.sh tests/test_search_flow.sh
git commit -m "feat: add search flow (drain gaps, fetch, junk-filter into ingest)"
```

---

### Task 5: Wiring — search loop prompt + README + full suite gate

**Files:**
- Modify: `README.md`
- Test: manual smoke (documented) + full offline suite.

**Interfaces:**
- Consumes: `scripts/search_flow.sh`, `scripts/state.py` (`add-gap`, `budget-reset`).
- Produces: documentation for queuing gaps and running the search loop. No code under test (prose + the existing suites are the gate).

- [ ] **Step 1: Document in README**

Add under the Quickstart section of `README.md`, after the "Continuous ingest loop" block:

```markdown
### Autonomous search loop
- Queue a research gap: `python3 scripts/state.py add-gap --topic 06-rag-retrieval --desc "hybrid retrieval rerank 2025"`.
- `scripts/search_flow.sh --topic <T>` drains that topic's queued gaps within the source budget (`budget.sources_per_cycle`): it searches + fetches via crawl4ai, drops non-junk results into `ingest/`, and marks each gap done (or re-queues it; failed after 3 attempts).
- Search is run **per topic** so the ingest flow routes each batch correctly: for every topic with queued gaps, run `scripts/search_flow.sh --topic <T>` then `scripts/ingest_flow.sh <T>`.
- Reset the per-cycle budget with `python3 scripts/state.py budget-reset`; inspect it with `python3 scripts/state.py budget-status`.
- Run hands-off on a slow interval, e.g. `/loop 10m for each topic with queued gaps, run scripts/search_flow.sh --topic <T> then scripts/ingest_flow.sh <T>`.
```

- [ ] **Step 2: Manual smoke test (offline-safe with fakes; or live if crawl4ai available)**

```bash
# Offline: reuse the test's fakes against the real repo state.
python3 scripts/state.py budget-reset
python3 scripts/state.py add-gap --topic 12-tooling-landscape --desc "smoke search gap"
python3 scripts/state.py budget-status
cat > /tmp/fs.py <<'PY'
import json; print(json.dumps([{"url":"http://x/good","title":"G"}]))
PY
cat > /tmp/ff.py <<'PY'
print("# G\n\n" + ("content " * 80))
PY
PY=python3 SEARCH=/tmp/fs.py FETCH=/tmp/ff.py bash scripts/search_flow.sh --topic 12-tooling-landscape
ls ingest/*.md 2>/dev/null && echo "smoke: source dropped"
# Clean up smoke artifacts:
rm -f ingest/*.md; rm -rf .research/state.json
```
Expected: `budget-status` shows `remaining_sources` 8; search drops one `.md` into `ingest/`; cleanup leaves the tree clean.

- [ ] **Step 3: Run the full offline suite**

Run:
```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
bash tests/test_ingest_flow.sh
bash tests/test_search_flow.sh
bash tests/test_catalog.sh
```
Expected: all PASS / `ALL OK`.

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "docs: document the autonomous search loop"
```

---

## Self-Review

**Spec coverage (sub-project #2 scope = search flow + budget governor):**
- Phase-weighted budget governor, subagent fan-out from weights (design §5) → Task 1 (`subagent_count`, `budget_*`, `sources_per_cycle`). Token metering deferred to the `/goal` layer per Global Constraints; v1 meters sources.
- Gap queue: human + (future) process-authored, dedup, status lifecycle (design §6①, §4 `gaps`) → Task 2 (`add_gap`/`next_queued_gap`/`set_gap_status`). v1 = human-seeded via `add-gap` CLI; process-authored gaps arrive in sub-project #3 and reuse the same ops.
- Search drains gaps within budget, fans out to fetch, drops into `ingest/` (design §6①) → Task 4 (`search_flow.sh --topic`), sequential within the source budget (parallel subagent fan-out is the loop/C layer). **Topic-scoped per run** so `ingest_flow.sh <T>` routes each batch correctly — the loop iterates topics (search then ingest per topic). `subagent_count` is not dead code: `budget-status` surfaces it for observability now and the `/goal` orchestrator consumes it in sub-project #6.
- Junk-detect + re-queue (design §6① success check) → Task 3 (`junk.py`) + Task 4 (re-queue, `failed` after 3 attempts).
- Closed loop to ingest: search → `ingest/` → ingest flow records (sub-project #1) → no direct coupling, coordinate via `state.json` and the `ingest/` dir.

Deferred to later sub-projects (correctly out of scope): process flow auto-authoring gaps (#3); parallel subagent fan-out + the `/goal` orchestrator that meters tokens and applies `subagent_count` (#6 / C); assertions (#4); websocket view (#5).

**Placeholder scan:** no TBD/TODO; every code step contains complete runnable code; commands have expected output. None found.

**Type consistency:** `budget_remaining_sources`/`budget_spend_source`/`subagent_count`/`budget_reset` names match between Task 1 implementation, its tests, and the CLI handlers, and the CLI subcommands (`budget-remaining`/`budget-spend`/`budget-status`/`budget-reset`) match Task 4's shell usage. `add_gap`/`next_queued_gap`/`set_gap_status` and the `add-gap`/`next-gap`/`set-gap` CLIs match between Task 2 and Task 4. `junk.is_junk` / `junk.py check` (exit 1 = junk) matches between Task 3 and Task 4's `if python3 junk.py check` (clean → keep). Gap shape `{id,topic,desc,origin,status,attempts}` is consistent with the sub-project #1 `DEFAULT_STATE["gaps"]` intent. Search writes `.md` into `ingest/`, which the sub-project #1 ingest flow treats as `rawtext` passthrough → records with a durable id.
