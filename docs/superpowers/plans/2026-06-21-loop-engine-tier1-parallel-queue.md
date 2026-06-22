# Tier 1 Parallel Queue Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Drain the research gap queue with `budget.max_workers` concurrent topic workers, safe against `state.json` corruption and budget overspend, with graph writes still serial.

**Architecture:** A cross-process `flock` transaction wraps every `state.json` mutation. Strict budget uses reserve-before-fetch (atomic reserve, refund the unused remainder). Workers shard by topic, each fetching into an isolated `ingest/.work/<topic>/` inbox; the existing serial step-1 graphify drains the resulting dirty graph.

**Tech Stack:** Python 3 stdlib only (`fcntl`, `contextlib`), bash, `unittest`. No pip, no pytest.

## Global Constraints

- **Python 3 stdlib only** — no pip, no pytest. Tests are `unittest` + bash `test_*.sh`.
- **No lint/type suppression comments** anywhere (`# noqa`, `# type: ignore`, etc.) — fix the code.
- **Durable ids** unchanged: gaps `g`+8 hex, corpus `c`+8 hex.
- **Commits:** Conventional Commits, selectively staged (never `git add .`/`-A`), no co-author trailers, no "Generated with" lines.
- **flock is per-process** (per open file description) — concurrency tests MUST use subprocesses, never threads in one process.
- **Backward compatibility:** an already-committed `state.json` lacks `max_workers`; every read uses `budget.get("max_workers", 4)`.
- **Read-only state commands take no lock:** `budget-remaining`, `budget-status`, `list-gaps`, `next-gap`, `list-drafts`, `candidates`.

---

### Task 1: `locked_state` transaction lock in `state.py`

**Files:**
- Modify: `scripts/state.py` (imports near line 1-8; add `lock_path` + `locked_state` after `save`, ~line 52; route every mutating CLI subcommand through it, ~lines 285-355)
- Test: `tests/test_state_lock.py` (create)

**Interfaces:**
- Produces: `lock_path(root=".") -> Path` (`.research/state.lock`); `locked_state(root=".")` — context manager yielding the loaded state dict, saving it under an exclusive `flock` on exit (no save if the body raises).
- Consumes: existing `load(root)`, `save(state, root)`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_state_lock.py
import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_PY = str(ROOT / "scripts" / "state.py")

def _add_gap(root, i):
    return subprocess.Popen([sys.executable, STATE_PY, "add-gap", "--root", root,
                             "--topic", f"t{i}", "--desc", f"gap number {i}"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

class TestLockedState(unittest.TestCase):
    def test_concurrent_add_gap_loses_no_updates(self):
        with tempfile.TemporaryDirectory() as d:
            subprocess.run([sys.executable, STATE_PY, "add-gap", "--root", d,
                            "--topic", "seed", "--desc", "seed gap"], check=True,
                           stdout=subprocess.DEVNULL)
            N = 12
            procs = [_add_gap(d, i) for i in range(N)]
            for p in procs:
                self.assertEqual(p.wait(), 0)
            state = json.loads((Path(d) / ".research" / "state.json").read_text())
            self.assertEqual(len(state["gaps"]), N + 1)  # seed + N, none lost

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_state_lock -v`
Expected: FAIL — concurrent writers clobber each other, final gap count < 13 (flaky but < N+1).

- [ ] **Step 3: Add imports**

In `scripts/state.py`, change the import block (lines 2-8) to add `fcntl` and `contextmanager`:

```python
import copy
import fcntl
import hashlib
import json
import os
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
```

- [ ] **Step 4: Add `lock_path` + `locked_state` after `save`**

Insert immediately after the `save` function (after line ~52):

```python
def lock_path(root="."):
    return Path(root) / ".research" / "state.lock"


@contextmanager
def locked_state(root="."):
    """Load -> yield -> save the state under an exclusive cross-process flock.

    The lock is a stable sidecar file (never the state file, whose os.replace
    swaps the inode). The state is saved only on clean exit; an exception
    propagates without a partial write. flock releases when the fd closes.
    """
    lp = lock_path(root)
    lp.parent.mkdir(parents=True, exist_ok=True)
    with open(lp, "w") as lf:
        fcntl.flock(lf, fcntl.LOCK_EX)
        st = load(root)
        yield st
        save(st, root)
```

- [ ] **Step 5: Route every mutating CLI subcommand through `locked_state`**

Replace each `st = load(args.root); …; save(st, args.root)` mutator body (lines ~287-355) with a `with locked_state(args.root) as st:` block. The mutators to convert: `add-corpus`, `set-graph`, `budget-reset`, `budget-spend`, `add-gap`, `set-gap`, `add-draft`, `set-draft`, `set-phase`. **`add-corpus` is critical** — parallel ingest workers call it concurrently, so an unlocked corpus add loses entries. It becomes:

```python
    if args.cmd == "add-corpus":
        with locked_state(args.root) as st:
            e = add_corpus_entry(st, title=args.title, source=args.source, topic=args.topic,
                                 native_path=args.native, extracted_path=args.extracted,
                                 lossy=args.lossy, id=args.id)
        print(e["id"]); return 0
```

And `add-gap` becomes:

```python
    if args.cmd == "add-gap":
        with locked_state(args.root) as st:
            g = add_gap(st, topic=args.topic, desc=args.desc, origin=args.origin)
        print(g["id"]); return 0
```

And `set-gap`:

```python
    if args.cmd == "set-gap":
        with locked_state(args.root) as st:
            set_gap_status(st, args.id, args.status, requeue=args.requeue)
        print("gap updated"); return 0
```

Apply the same transform to `set-graph`, `budget-reset`, `budget-spend` (keep its trailing `print(budget_remaining_sources(st))` after the `with`), `add-draft`, `set-draft` (keep the unknown-id `return 1` guard *inside* the `with`, before save — if unknown, `print(...); return 1` without mutating), and `set-phase` (keep the `ValueError` guard inside the `with`). Leave read-only commands (`budget-remaining`, `budget-status`, `list-gaps`, `next-gap`, `list-drafts`, `candidates`, `gen-id`) on plain `load()`.

- [ ] **Step 6: Run test to verify it passes**

Run: `python3 -m unittest tests.test_state_lock -v`
Expected: PASS — all 13 gaps present.

- [ ] **Step 7: Run the full suite (no regressions)**

Run: `python3 -m unittest discover -s tests -v 2>&1 | tail -5`
Expected: OK.

- [ ] **Step 8: Commit**

```bash
git add scripts/state.py tests/test_state_lock.py
git commit -m "feat(state): cross-process flock transaction for mutations"
```

---

### Task 2: Strict budget (reserve/refund) + `max_workers`

**Files:**
- Modify: `scripts/state.py` (`DEFAULT_STATE` budget block ~line 11-22; add `budget_reserve`/`budget_refund` near `budget_spend_source` ~line; argparse + dispatch ~line 259-314)
- Test: `tests/test_budget_strict.py` (create)

**Interfaces:**
- Produces: `budget_reserve(state, n=1) -> int` (grants `max(0, min(n, remaining))`, adds to `spent.sources`, returns granted); `budget_refund(state, n=1)` (subtracts `n` from `spent.sources`, clamped ≥ 0); CLI `budget-reserve --sources N` (prints granted), `budget-refund --sources N`; `budget.max_workers` in `DEFAULT_STATE` (= 4); `budget-status` JSON gains `max_workers`.
- Consumes: `locked_state` (Task 1), `budget_remaining_sources`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_budget_strict.py
import json, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_PY = str(ROOT / "scripts" / "state.py")

def _seed(d):
    subprocess.run([sys.executable, STATE_PY, "budget-reset", "--root", d],
                   check=True, stdout=subprocess.DEVNULL)

class TestStrictBudget(unittest.TestCase):
    def test_concurrent_reserve_never_exceeds_cap(self):
        with tempfile.TemporaryDirectory() as d:
            _seed(d)  # sources_per_cycle defaults to 8, spent.sources = 0
            procs = [subprocess.Popen([sys.executable, STATE_PY, "budget-reserve",
                                       "--root", d, "--sources", "1"],
                                      stdout=subprocess.PIPE, text=True) for _ in range(12)]
            grants = [int(p.communicate()[0].strip() or 0) for p in procs]
            self.assertEqual(sum(grants), 8)            # exactly the cap granted
            st = json.loads((Path(d) / ".research" / "state.json").read_text())
            self.assertEqual(st["budget"]["spent"]["sources"], 8)  # never exceeded

    def test_refund_round_trips_and_clamps(self):
        with tempfile.TemporaryDirectory() as d:
            _seed(d)
            g = subprocess.run([sys.executable, STATE_PY, "budget-reserve", "--root", d,
                                "--sources", "3"], capture_output=True, text=True)
            self.assertEqual(g.stdout.strip(), "3")
            subprocess.run([sys.executable, STATE_PY, "budget-refund", "--root", d,
                            "--sources", "5"], check=True, stdout=subprocess.DEVNULL)  # over-refund
            st = json.loads((Path(d) / ".research" / "state.json").read_text())
            self.assertEqual(st["budget"]["spent"]["sources"], 0)  # clamped at 0

    def test_status_reports_max_workers_default(self):
        with tempfile.TemporaryDirectory() as d:
            _seed(d)
            out = subprocess.run([sys.executable, STATE_PY, "budget-status", "--root", d],
                                 capture_output=True, text=True).stdout
            self.assertEqual(json.loads(out)["max_workers"], 4)

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_budget_strict -v`
Expected: FAIL — `budget-reserve`/`budget-refund` subcommands do not exist (nonzero exit / empty output), `max_workers` missing from status.

- [ ] **Step 3: Add `max_workers` to `DEFAULT_STATE`**

In the `DEFAULT_STATE["budget"]` dict, add the key after `max_subagents` (line ~14):

```python
        "max_subagents": 8,
        "max_workers": 4,
```

- [ ] **Step 4: Add `budget_reserve` + `budget_refund`**

Insert right after `budget_spend_source` (the bare `+= n` function):

```python
def budget_reserve(state, n=1):
    granted = max(0, min(n, budget_remaining_sources(state)))
    state["budget"]["spent"]["sources"] += granted
    return granted


def budget_refund(state, n=1):
    s = state["budget"]["spent"]
    s["sources"] = max(0, s["sources"] - n)
```

- [ ] **Step 5: Add argparse subparsers**

Next to the other budget subparsers (line ~261), add:

```python
    brv = sub.add_parser("budget-reserve"); brv.add_argument("--root", default="."); brv.add_argument("--sources", type=int, required=True)
    brf = sub.add_parser("budget-refund"); brf.add_argument("--root", default="."); brf.add_argument("--sources", type=int, required=True)
```

- [ ] **Step 6: Add dispatch + extend `budget-status`**

Add two handlers next to `budget-spend` (line ~306):

```python
    if args.cmd == "budget-reserve":
        with locked_state(args.root) as st:
            granted = budget_reserve(st, args.sources)
        print(granted); return 0
    if args.cmd == "budget-refund":
        with locked_state(args.root) as st:
            budget_refund(st, args.sources)
        print("refunded"); return 0
```

Extend the `budget-status` output dict to include `max_workers`:

```python
        out = {"phase": st["budget"]["phase"],
               "remaining_sources": budget_remaining_sources(st),
               "max_workers": st["budget"].get("max_workers", 4),
               "subagents": {f: subagent_count(st, f) for f in ("search", "ingest", "process")}}
```

- [ ] **Step 7: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_budget_strict -v`
Expected: PASS (3 tests).

- [ ] **Step 8: Commit**

```bash
git add scripts/state.py tests/test_budget_strict.py
git commit -m "feat(state): strict reserve/refund budget + max_workers config"
```

---

### Task 3: `search_flow.sh` — reserve-before-fetch + `--inbox`

**Files:**
- Modify: `scripts/search_flow.sh` (arg parse lines 16-22; gap loop lines 27-67)
- Test: `tests/test_search_flow_reserve.sh` (create)

**Interfaces:**
- Consumes: `budget-reserve`/`budget-refund` CLI (Task 2); env overrides `PY`, `SEARCH`, `FETCH`, `PER_GAP`.
- Produces: `search_flow.sh --topic <T> [--inbox DIR]` — reserves budget per gap, fetches ≤ reservation into `DIR` (default `$ROOT/ingest`), refunds the unused remainder, never overspends `sources_per_cycle`.

- [ ] **Step 1: Write the failing test**

```bash
# tests/test_search_flow_reserve.sh
#!/usr/bin/env bash
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$HERE/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
export REPO_ROOT="$TMP"
mkdir -p "$TMP/.research" "$TMP/scripts"
# stub crawl tools: SEARCH prints 5 fake urls, FETCH prints clean prose
cat > "$TMP/fakesearch.py" <<'PY'
import json,sys
print(json.dumps([{"url":f"http://e/{i}"} for i in range(int(sys.argv[2]))]))
PY
cat > "$TMP/fakefetch.py" <<'PY'
print("This is a substantial clean research document about retrieval methods. " * 40)
PY
# seed budget=8 and two gaps for one topic
python3 "$ROOT/scripts/state.py" budget-reset --root "$TMP" >/dev/null
python3 "$ROOT/scripts/state.py" add-gap --root "$TMP" --topic 06-x --desc "alpha question" >/dev/null
python3 "$ROOT/scripts/state.py" add-gap --root "$TMP" --topic 06-x --desc "beta question" >/dev/null
IN="$TMP/ingest/.work/06-x"
PER_GAP=3 PY=python3 SEARCH="$TMP/fakesearch.py" FETCH="$TMP/fakefetch.py" \
  bash "$ROOT/scripts/search_flow.sh" --topic 06-x --inbox "$IN"
# assert: kept files landed in the scoped inbox, and budget spent == files kept (no overspend)
files="$(find "$IN" -name '*.md' | wc -l | tr -d ' ')"
spent="$(python3 -c "import json;print(json.load(open('$TMP/.research/state.json'))['budget']['spent']['sources'])")"
echo "files=$files spent=$spent"
[ "$files" = "$spent" ] || { echo "FAIL: spent ($spent) != files ($files)"; exit 1; }
[ "$spent" -le 8 ] || { echo "FAIL: overspent $spent"; exit 1; }
[ "$files" -ge 1 ] || { echo "FAIL: nothing landed in scoped inbox"; exit 1; }
echo "PASS search_flow reserve"
```

Make it executable: `chmod +x tests/test_search_flow_reserve.sh`

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/test_search_flow_reserve.sh`
Expected: FAIL — `--inbox` is ignored (files land in `$ROOT/ingest`, not the scoped dir), so `files` in `$IN` is 0.

- [ ] **Step 3: Rewrite arg parsing (lines 16-22)**

Replace lines 16-22 (the `--topic`-only parse, the top `mkdir -p ingest`, and the top `budget-remaining` read) with:

```bash
topic=""; INBOX=""
while [ $# -gt 0 ]; do
  case "$1" in
    --topic) topic="${2:?--topic requires a value}"; shift 2 ;;
    --inbox) INBOX="${2:?--inbox requires a DIR}"; shift 2 ;;
    *) shift ;;
  esac
done
[ -n "$topic" ] || { echo "usage: search_flow.sh --topic <topic> [--inbox DIR]" >&2; exit 2; }
INBOX="${INBOX:-$ROOT/ingest}"
mkdir -p "$INBOX"
```

- [ ] **Step 4: Rewrite the gap loop (lines 24-67) to reserve-before-fetch**

Replace the body from `gaps="$(...)"` through the end with:

```bash
gaps="$($SP list-gaps --root "$ROOT" --topic "$topic" --status queued)"
[ -n "$gaps" ] || { echo "search: no queued gaps for $topic"; exit 0; }

while IFS= read -r line; do
  [ -n "$line" ] || continue
  gid="$(printf '%s' "$line" | cut -f1)"
  desc="$(printf '%s' "$line" | cut -f3)"

  granted="$($SP budget-reserve --root "$ROOT" --sources "$PER_GAP")"
  [ "$granted" -gt 0 ] || break   # budget exhausted for this cycle

  results="$("$PY" "$SEARCH" "$desc" "$granted" 2>/dev/null)" || results="[]"
  urls="$(printf '%s' "$results" | jq -r '.[].url' 2>/dev/null)"
  kept=0; i=0
  while IFS= read -r url; do
    [ -n "$url" ] || continue
    [ "$kept" -lt "$granted" ] || break   # reservation filled
    i=$((i+1))
    tmp="$(mktemp)"
    "$PY" "$FETCH" "$url" > "$tmp" 2>/dev/null || { rm -f "$tmp"; continue; }
    if python3 "$HERE/junk.py" check "$tmp"; then
      slug="$(slugify "$desc")"
      mv "$tmp" "$INBOX/${gid}-${slug}-${i}.md"
      kept=$((kept+1))
    else
      rm -f "$tmp"
    fi
  done <<< "$urls"

  refund=$((granted - kept))
  [ "$refund" -gt 0 ] && $SP budget-refund --root "$ROOT" --sources "$refund" >/dev/null

  if [ "$kept" -gt 0 ]; then
    $SP set-gap --root "$ROOT" --id "$gid" --status done >/dev/null
    $RL log --root "$ROOT" --flow search --step gather --status ok \
      --data "{\"gap_id\":\"$gid\",\"gap_status\":\"done\",\"sources_added\":$kept}"
    echo "search: gap $gid -> $kept source(s) into $INBOX"
  else
    $SP set-gap --root "$ROOT" --id "$gid" --status queued --requeue >/dev/null
    att="$(python3 -c "import json,sys;print(next((g['attempts'] for g in json.load(open(sys.argv[1]+'/.research/state.json'))['gaps'] if g['id']==sys.argv[2]), -1))" "$ROOT" "$gid")"
    [ "$att" -ge 3 ] && $SP set-gap --root "$ROOT" --id "$gid" --status failed >/dev/null
    gs=queued; [ "$att" -ge 3 ] && gs=failed
    $RL log --root "$ROOT" --flow search --step gather --status skip \
      --data "{\"gap_id\":\"$gid\",\"gap_status\":\"$gs\",\"sources_added\":0,\"attempts\":$att}"
    echo "search: gap $gid produced no non-junk sources (attempt $att)"
  fi
done <<< "$gaps"
echo "Done. New sources (if any) await the ingest cycle."
```

- [ ] **Step 5: Run test to verify it passes**

Run: `bash tests/test_search_flow_reserve.sh`
Expected: `PASS search_flow reserve` (files land in scoped inbox; spent == files; ≤ 8).

- [ ] **Step 6: Commit**

```bash
git add scripts/search_flow.sh tests/test_search_flow_reserve.sh
git commit -m "feat(search): reserve-before-fetch budget + --inbox isolation"
```

---

### Task 4: `ingest_flow.sh` — `--inbox`

**Files:**
- Modify: `scripts/ingest_flow.sh` (arg parse line 11; `fail_item` ~line 15; drain block lines ~19-25; `--native` arg ~line 60)
- Test: `tests/test_ingest_flow_inbox.sh` (create)

**Interfaces:**
- Produces: `ingest_flow.sh <topic> [--inbox DIR]` — drains `DIR/*` (default `$ROOT/ingest`), normalizes into `docs/<topic>/sources/`, archives to `DIR/_done`, quarantines to `DIR/_failed`.
- Consumes: nothing new.

- [ ] **Step 1: Write the failing test**

```bash
# tests/test_ingest_flow_inbox.sh
#!/usr/bin/env bash
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$HERE/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
export REPO_ROOT="$TMP"
mkdir -p "$TMP/.research" "$TMP/docs"
IN="$TMP/ingest/.work/06-rag-retrieval"; mkdir -p "$IN"
printf 'clean research text about retrieval %.0s' {1..40} > "$IN/cabc12345-sample-1.md"
bash "$ROOT/scripts/ingest_flow.sh" 06-rag-retrieval --inbox "$IN"
landed="$(find "$TMP/docs/06-rag-retrieval/sources" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')"
archived="$(find "$IN/_done" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')"
echo "landed=$landed archived=$archived"
[ "$landed" -ge 1 ] || { echo "FAIL: source not normalized into topic dir"; exit 1; }
[ "$archived" -ge 1 ] || { echo "FAIL: source not archived into scoped _done"; exit 1; }
echo "PASS ingest_flow inbox"
```

Make it executable: `chmod +x tests/test_ingest_flow_inbox.sh`

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/test_ingest_flow_inbox.sh`
Expected: FAIL — `--inbox` unparsed, ingest drains empty `$ROOT/ingest`, nothing lands.

- [ ] **Step 3: Parse `--inbox` and define `INBOX` before `fail_item`**

Replace line 11 (`topic="${1:-}"; …`) with:

```bash
topic="${1:-}"; [ -n "$topic" ] || { echo "usage: ingest_flow.sh <topic> [--inbox DIR]" >&2; exit 2; }
shift
INBOX="$ROOT/ingest"
while [ $# -gt 0 ]; do
  case "$1" in --inbox) INBOX="${2:?--inbox requires a DIR}"; shift 2 ;; *) shift ;; esac
done
INBOX_REL="$("$PY" -c "import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]))" "$INBOX" "$ROOT")"
```

- [ ] **Step 4: Point `fail_item` and the drain at `$INBOX`**

Change `fail_item` (line ~14) to move into `$INBOX/_failed/`:

```bash
fail_item() { echo "$2" >&2; mv "$1" "$INBOX/_failed/" 2>/dev/null; \
  $RL log --root "$ROOT" --flow ingest --step normalize --status fail --data "{\"reason\":\"$2\"}"; }
```

Change the drain block (lines ~28-33) from `$ROOT/ingest` to `$INBOX`:

```bash
shopt -s nullglob
items=("$INBOX"/*)
real=(); for f in "${items[@]+"${items[@]}"}"; do
  b="$(basename "$f")"; [ "$b" = ".gitkeep" ] || [ "$b" = "_done" ] || [ "$b" = "_failed" ] || real+=("$f")
done
[ "${#real[@]}" -gt 0 ] || { echo "no new sources in $INBOX"; exit 0; }

mkdir -p "$INBOX/_done" "$INBOX/_failed"
```

- [ ] **Step 5: Point the archive + `--native` at the scoped inbox**

Change the `--native` argument (line ~60) from `ingest/_done/$name` to the scoped relative path:

```bash
  "$PY" "$HERE/state.py" add-corpus --root "$ROOT" --id "$id" --title "$title" --source "$source_disp" \
        --topic "$topic" --native "$INBOX_REL/_done/$name" --extracted "$rel" >/dev/null \
        || { fail_item "$f" "record failed: $f"; rm -f "$out"; continue; }
  mv "$f" "$INBOX/_done/" || { echo "warning: could not archive $f" >&2; }
```

- [ ] **Step 6: Run test to verify it passes**

Run: `bash tests/test_ingest_flow_inbox.sh`
Expected: `PASS ingest_flow inbox`.

- [ ] **Step 7: Verify default inbox still works (no regression)**

Run: `REPO_ROOT="$(mktemp -d)" bash -c 'mkdir -p "$REPO_ROOT/ingest"; printf "clean text %.0s" {1..40} > "$REPO_ROOT/ingest/cabc12345-x.md"; bash scripts/ingest_flow.sh 06-rag-retrieval; find "$REPO_ROOT/docs" -name "*.md" | wc -l'`
Expected: `1` (default `$ROOT/ingest` path unchanged).

- [ ] **Step 8: Commit**

```bash
git add scripts/ingest_flow.sh tests/test_ingest_flow_inbox.sh
git commit -m "feat(ingest): --inbox for per-topic worker isolation"
```

---

### Task 5: Parallel driver in `.claude/goal.md` step 3

**Files:**
- Modify: `.claude/goal.md` (step 3 "Search" block)

**Interfaces:**
- Consumes: `budget-status` `max_workers` (Task 2); `search_flow.sh --inbox` (Task 3); `ingest_flow.sh --inbox` (Task 4).
- Produces: a `xargs -P <max_workers>` driver that shards queued topics into isolated `ingest/.work/<topic>/` inboxes. Documentation only — no automated test; covered by the end-to-end smoke.

- [ ] **Step 1: Replace step 3's sequential loop**

In `.claude/goal.md`, replace the current step 3 `for T in …` shell block with:

````markdown
3. **Search.** If `D.search` is `true`: run search+ingest concurrently, one worker per topic
   with queued gaps, each isolated in its own `ingest/.work/<topic>/` inbox so parallel
   ingests never share files or mis-route. Worker count is `budget.max_workers`:
   ```
   W=$(python3 scripts/state.py budget-status | python3 -c 'import json,sys;print(json.load(sys.stdin)["max_workers"])')
   python3 scripts/state.py list-gaps --status queued | cut -f2 | sort -u | \
     xargs -P "$W" -I{} bash -c '
       T="{}"; IN="ingest/.work/$T"; mkdir -p "$IN"
       bash scripts/search_flow.sh --topic "$T" --inbox "$IN"
       bash scripts/ingest_flow.sh "$T" --inbox "$IN"
     '
   ```
   Each worker fetches within the shared strict budget (atomic reserve/refund) and flags the
   graph dirty. The graph update stays serial — it runs in the next cycle's step 1, which fires
   on the persisted dirty flag even when the next drain is empty.
````

- [ ] **Step 2: Verify the driver parses + reads max_workers (dry check)**

Run: `python3 scripts/state.py budget-status | python3 -c 'import json,sys;print(json.load(sys.stdin)["max_workers"])'`
Expected: prints `4` (or the configured value) — confirms the `W=` line resolves.

- [ ] **Step 3: Commit**

```bash
git add .claude/goal.md
git commit -m "feat(goal): parallel per-topic search+ingest driver (max_workers)"
```

---

## End-to-end smoke (after all tasks)

Real two-topic concurrent run against a temp root with stubbed crawl tools, asserting no cross-routing and budget respected:

- [ ] Seed a temp root with `budget.max_workers=2`, queued gaps under two topics; run the step-3 driver with stubbed `SEARCH`/`FETCH`; assert each topic's sources land only under its own `docs/<topic>/sources/`, `ingest/.work/<topic>/` inboxes stayed disjoint, and total `spent.sources` ≤ `sources_per_cycle`.
- [ ] Run the full suite: `python3 -m unittest discover -s tests` and every `bash tests/test_*.sh` → all green.

## Self-review

- **Spec coverage:** §3.1 locked_state + mutator routing → Task 1. §3.1 reserve/refund + max_workers + budget-status → Task 2. §3.2 search_flow reserve + `--inbox` → Task 3. §3.3 ingest_flow `--inbox` → Task 4. §3.4 goal.md driver → Task 5. §6 tests → per-task tests + end-to-end smoke. §3.4 `ingest/.work/` ignore → already covered by existing `.gitignore` `ingest/*` (no task needed; noted in plan intro).
- **Type/name consistency:** `budget_reserve`/`budget_refund`, CLI `budget-reserve`/`budget-refund`, `--inbox`, `INBOX`, `max_workers` used identically across tasks. `granted`/`kept`/`refund` names consistent in search_flow.
- **Placeholder scan:** none — every code/test step carries full content.
