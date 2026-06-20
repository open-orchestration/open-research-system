# Loop Engine — Spine + Ingest Flow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build sub-project #1 of the loop-driven research engine — the on-disk state spine (`.research/state.json`) and the ingest flow that normalizes human-dropped sources into the corpus with durable IDs, metadata, and a lifecycle facet, then emits a graph-delta event for the realtime stream.

**Architecture:** A small Python state-ledger module (stdlib `json`, no deps) is the single source of truth. A bash `ingest_flow.sh` drains `ingest/`, routes each item by type to the right normalizer (markitdown / crawl4ai / passthrough), assigns a deterministic ID, writes the normalized markdown into `docs/NN-topic/sources/`, records it in the ledger, and flags the graph dirty. Semantic graph update for markdown is LLM-driven and runs as an agent step in the loop prompt (graphify skill `--update`); the testable delta extraction that follows is a separate Python helper. All logic that does not require network or external binaries is unit-tested offline.

**Tech Stack:** bash (matching existing `scripts/*.sh`), Python 3 stdlib only (`json`, `hashlib`, `pathlib`, `unittest`), markitdown CLI (`~/.local/bin/markitdown`), crawl4ai (`~/.venvs/crawl4ai`), graphify skill/CLI (`~/.local/bin/graphify`). No new dependencies.

## Global Constraints

- Python 3 **stdlib only** — no pip installs, no `pytest`; tests use `unittest`. Verbatim: "No new dependencies."
- Follow existing script conventions: `#!/usr/bin/env bash`, `set -euo pipefail`, `source "$HERE/lib.sh"`, `ROOT="${REPO_ROOT:-...}"`, reuse `slugify` and `resolve_topic_dir` from `scripts/lib.sh`.
- Graph path in this repo is `.graphify/graph.json` (gitignored). The graphify CLI defaults to `graphify-out/` — always pass the path explicitly.
- `graphify update <path>` is **code-only (no LLM)**; markdown corpus semantic update is done by invoking the graphify **skill** with `--update` as an agent step, never as a pure shell call.
- Durable/committed artifacts: `.research/state.json`, `.research/graph-events.jsonl`. Derived/gitignored: `.graphify/`.
- Deterministic IDs: an entry's ID is `sha256(seed)[:8]` prefixed. The **seed is the source's stable identity, never its on-disk path**: file *content hash* for dropped files, the *URL* for links — so re-ingesting the same content (even under a different filename or temp path) yields the same ID (idempotent, dedups). The human-readable `source` field stays the filename/URL for display.
- IDs/lifecycle/metadata are assigned **at ingest**, before any filing decision (findings-11 records discipline).

---

### Task 1: State ledger core — init, load, save, gen_id

**Files:**
- Create: `scripts/state.py`
- Test: `tests/test_state.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `DEFAULT_STATE: dict` — the seed schema.
  - `state_path(root=".") -> pathlib.Path` — returns `<root>/.research/state.json`.
  - `load(root=".") -> dict` — returns parsed state, writing the seed first if the file is missing.
  - `save(state: dict, root=".") -> None` — atomic write (temp file + replace).
  - `gen_id(prefix: str, seed: str) -> str` — `prefix + sha256(seed.encode()).hexdigest()[:8]`.

- [ ] **Step 1: Create the test package marker and write the failing test**

First make `tests/` an importable package so `python3 -m unittest tests.test_*` resolves deterministically (the repo has no Python tests yet):

```bash
touch tests/__init__.py
```

```python
# tests/test_state.py
import json, tempfile, unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import state


class TestStateCore(unittest.TestCase):
    def test_gen_id_is_deterministic_and_prefixed(self):
        a = state.gen_id("c", "https://example.com/x")
        b = state.gen_id("c", "https://example.com/x")
        self.assertEqual(a, b)
        self.assertTrue(a.startswith("c"))
        self.assertEqual(len(a), 9)  # 1 prefix + 8 hex

    def test_gen_id_differs_by_seed(self):
        self.assertNotEqual(state.gen_id("c", "a"), state.gen_id("c", "b"))

    def test_load_seeds_when_missing(self):
        with tempfile.TemporaryDirectory() as d:
            st = state.load(d)
            self.assertIn("budget", st)
            self.assertEqual(st["corpus"], [])
            self.assertTrue((Path(d) / ".research/state.json").exists())

    def test_save_then_load_roundtrips(self):
        with tempfile.TemporaryDirectory() as d:
            st = state.load(d)
            st["corpus"].append({"id": "c001"})
            state.save(st, d)
            again = state.load(d)
            self.assertEqual(again["corpus"], [{"id": "c001"}])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_state -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'state'` (or AttributeError once the file exists but functions don't).

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/state.py
"""On-disk state ledger for the loop research engine. Stdlib only."""
import copy
import hashlib
import json
import os
import sys
from pathlib import Path

DEFAULT_STATE = {
    "budget": {
        "tokens_per_cycle": 200000,
        "max_subagents": 8,
        "phase": "gather",
        "weights": {
            "gather":     {"search": 0.7, "ingest": 0.3, "process": 0.0},
            "deepen":     {"search": 0.4, "ingest": 0.3, "process": 0.3},
            "synthesize": {"search": 0.1, "ingest": 0.1, "process": 0.8},
        },
        "spent": {"tokens": 0, "sources": 0, "cycle_started_at": None},
    },
    "gaps": [],
    "inbox": [],
    "corpus": [],
    "graph": {"dirty": False, "last_update": None, "node_count": 0, "edge_count": 0},
    "assertions": {"count": 0, "file": ".research/graph-assertions.jsonl"},
    "drafts": [],
}


def state_path(root="."):
    return Path(root) / ".research" / "state.json"


def load(root="."):
    p = state_path(root)
    if not p.exists():
        seed = copy.deepcopy(DEFAULT_STATE)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(seed, indent=2, ensure_ascii=False), encoding="utf-8")
        return seed
    return json.loads(p.read_text(encoding="utf-8"))


def save(state, root="."):
    p = state_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, p)


def gen_id(prefix, seed):
    return prefix + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:8]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_state -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py tests/test_state.py tests/__init__.py
git commit -m "feat: add state ledger core (load/save/gen_id)"
```

---

### Task 2: State ledger — corpus + graph operations

**Files:**
- Modify: `scripts/state.py`
- Test: `tests/test_state.py`

**Interfaces:**
- Consumes: `load`, `save`, `gen_id`, `DEFAULT_STATE` from Task 1.
- Produces:
  - `add_corpus_entry(state, *, title, source, topic, native_path, extracted_path, lossy=False, lifecycle="active", now=None, id=None) -> dict` — if `id` is None, computes `id = gen_id("c", source)`; if `id` already exists in `state["corpus"]`, returns the existing entry unchanged (idempotent); otherwise appends a new entry, sets `state["graph"]["dirty"] = True`, and returns it. The explicit `id` lets the ingest flow seed the id from a content hash while keeping `source` human-readable. New entry shape: `{id, title, source, topic, lifecycle, native_path, extracted_path, lossy, ingested_at}` where `ingested_at` is an ISO-ish string from `_now()`.
  - `set_graph(state, *, dirty=None, node_count=None, edge_count=None, last_update=None) -> None` — updates only the provided fields of `state["graph"]`.
  - `_now() -> str` — `datetime.now(timezone.utc).isoformat()` (injectable for tests via the `now` kwarg on `add_corpus_entry`).
  - CLI: `python3 scripts/state.py add-corpus --root R --title T --source S --topic TP --native N --extracted E [--lossy] [--id ID]` prints the entry id and saves state.
  - CLI: `python3 scripts/state.py set-graph --root R [--dirty true|false] [--node-count N] [--edge-count N] [--last-update S]` updates the named graph fields and saves state.

- [ ] **Step 1: Write the failing test**

```python
# append to tests/test_state.py inside the class
    def test_add_corpus_assigns_deterministic_id_and_sets_dirty(self):
        st = state.load_default()
        e = state.add_corpus_entry(
            st, title="T", source="src://a", topic="11-x",
            native_path="ingest/a.md", extracted_path="docs/11-x/sources/cXXXX-t.md",
            now="2026-06-19T00:00:00+00:00",
        )
        self.assertEqual(e["id"], state.gen_id("c", "src://a"))
        self.assertEqual(e["lifecycle"], "active")
        self.assertTrue(st["graph"]["dirty"])
        self.assertEqual(len(st["corpus"]), 1)

    def test_add_corpus_is_idempotent(self):
        st = state.load_default()
        state.add_corpus_entry(st, title="T", source="src://a", topic="11-x",
                               native_path="n", extracted_path="e", now="t")
        state.add_corpus_entry(st, title="T2", source="src://a", topic="11-x",
                               native_path="n", extracted_path="e", now="t")
        self.assertEqual(len(st["corpus"]), 1)  # same source -> same id -> no dup

    def test_set_graph_updates_named_fields_only(self):
        st = state.load_default()
        state.set_graph(st, dirty=False, node_count=42)
        self.assertFalse(st["graph"]["dirty"])
        self.assertEqual(st["graph"]["node_count"], 42)
        self.assertEqual(st["graph"]["edge_count"], 0)
```

Note: this test uses `state.load_default()` — add it as a tiny helper returning `copy.deepcopy(DEFAULT_STATE)` so tests do not touch disk.

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_state -v`
Expected: FAIL — `AttributeError: module 'state' has no attribute 'load_default'` (the first new helper the added tests reference; `add_corpus_entry`/`set_graph` are likewise undefined until Step 3).

- [ ] **Step 3: Write minimal implementation**

```python
# add to scripts/state.py
import copy
from datetime import datetime, timezone


def load_default():
    return copy.deepcopy(DEFAULT_STATE)


def _now():
    return datetime.now(timezone.utc).isoformat()


def add_corpus_entry(state, *, title, source, topic, native_path, extracted_path,
                     lossy=False, lifecycle="active", now=None, id=None):
    cid = id or gen_id("c", source)
    for e in state["corpus"]:
        if e["id"] == cid:
            return e
    entry = {
        "id": cid, "title": title, "source": source, "topic": topic,
        "lifecycle": lifecycle, "native_path": native_path,
        "extracted_path": extracted_path, "lossy": lossy,
        "ingested_at": now or _now(),
    }
    state["corpus"].append(entry)
    state["graph"]["dirty"] = True
    return entry


def set_graph(state, *, dirty=None, node_count=None, edge_count=None, last_update=None):
    g = state["graph"]
    if dirty is not None:
        g["dirty"] = dirty
    if node_count is not None:
        g["node_count"] = node_count
    if edge_count is not None:
        g["edge_count"] = edge_count
    if last_update is not None:
        g["last_update"] = last_update


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("gen-id")
    g.add_argument("prefix"); g.add_argument("seed")
    a = sub.add_parser("add-corpus")
    a.add_argument("--root", default=".")
    for f in ("title", "source", "topic", "native", "extracted"):
        a.add_argument(f"--{f}", required=True)
    a.add_argument("--lossy", action="store_true")
    a.add_argument("--id", default=None)
    sg = sub.add_parser("set-graph")
    sg.add_argument("--root", default=".")
    sg.add_argument("--dirty", choices=("true", "false"), default=None)
    sg.add_argument("--node-count", type=int, default=None)
    sg.add_argument("--edge-count", type=int, default=None)
    sg.add_argument("--last-update", default=None)
    args = ap.parse_args(argv)
    if args.cmd == "gen-id":
        print(gen_id(args.prefix, args.seed)); return 0
    if args.cmd == "add-corpus":
        st = load(args.root)
        e = add_corpus_entry(st, title=args.title, source=args.source, topic=args.topic,
                             native_path=args.native, extracted_path=args.extracted,
                             lossy=args.lossy, id=args.id)
        save(st, args.root)
        print(e["id"]); return 0
    if args.cmd == "set-graph":
        st = load(args.root)
        set_graph(st,
                  dirty={"true": True, "false": False}.get(args.dirty),
                  node_count=args.node_count, edge_count=args.edge_count,
                  last_update=args.last_update)
        save(st, args.root)
        print("graph updated"); return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_state -v`
Expected: PASS (7 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py tests/test_state.py
git commit -m "feat: add corpus + graph ops to state ledger"
```

---

### Task 3: Source type detection

**Files:**
- Create: `scripts/ingest_lib.py`
- Test: `tests/test_ingest_lib.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `detect_type(name: str) -> str` — returns one of `"link" | "rawtext" | "document"`.
    Rules, in order: a value starting with `http://`/`https://` or ending `.url` → `"link"` (the flow's link branch re-routes YouTube URLs to transcription after reading the URL — see Task 4); `.md`/`.txt` → `"rawtext"`; everything else (`.pdf`/`.docx`/`.pptx`/`.xlsx`/`.png`/`.jpg`/`.jpeg`/`.webp`/`.mp4`/`.webm`/`.mov`/unknown) → `"document"` (markitdown handles it, including local audio/video).
  - CLI: `python3 scripts/ingest_lib.py detect <name>` prints the type.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_ingest_lib.py
import unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import ingest_lib as il


class TestDetectType(unittest.TestCase):
    def test_links(self):
        self.assertEqual(il.detect_type("https://example.com/a"), "link")
        self.assertEqual(il.detect_type("source.url"), "link")
        # YouTube is a link here; the flow re-routes it to transcription after reading the URL.
        self.assertEqual(il.detect_type("https://www.youtube.com/watch?v=abc"), "link")

    def test_rawtext(self):
        self.assertEqual(il.detect_type("notes.md"), "rawtext")
        self.assertEqual(il.detect_type("paste.txt"), "rawtext")

    def test_document(self):
        self.assertEqual(il.detect_type("report.pdf"), "document")
        self.assertEqual(il.detect_type("scan.png"), "document")
        self.assertEqual(il.detect_type("clip.mp4"), "document")
        self.assertEqual(il.detect_type("mystery.bin"), "document")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_ingest_lib -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'ingest_lib'`.

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/ingest_lib.py
"""Pure helpers for the ingest flow. Stdlib only."""
import sys

_RAWTEXT_EXT = (".md", ".txt")


def detect_type(name):
    low = name.lower()
    if low.startswith(("http://", "https://")) or low.endswith(".url"):
        return "link"
    if low.endswith(_RAWTEXT_EXT):
        return "rawtext"
    return "document"


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "detect":
        print(detect_type(sys.argv[2]))
    else:
        print("usage: ingest_lib.py detect <name>", file=sys.stderr)
        sys.exit(2)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_ingest_lib -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/ingest_lib.py tests/test_ingest_lib.py
git commit -m "feat: add source type detection for ingest"
```

---

### Task 4: Ingest flow script (drain → normalize → record)

**Files:**
- Create: `scripts/ingest_flow.sh`
- Modify: `scripts/lib.sh` (add `fetch_link` + `transcribe_video` helpers)
- Test: `tests/test_ingest_flow.sh`

**Interfaces:**
- Consumes: `slugify`, `resolve_topic_dir` (existing `lib.sh`); `detect_type` (Task 3); `state.py add-corpus` / `gen-id` (Tasks 1–2).
- Produces: a runnable `scripts/ingest_flow.sh <topic>` that, for each non-`.gitkeep` entry in `ingest/`, normalizes it to markdown under `docs/<topic>/sources/<id>-<slug>.md`, records it in `state.json`, sets `graph.dirty=true`, and moves the consumed native file to `ingest/_done/`. Exits 0 with "no new sources" when `ingest/` is empty.
- **ID seed (per Global Constraints):** for a file, the id seed is its **content hash** (`sha256` of the bytes) and `source` is `file://<name>`; for a `.url`/link item, the id seed and `source` are the **URL read from the file's contents**. Never the on-disk path. The id is computed up front and passed to `add-corpus --id`.
- **Failure isolation (spec §9):** every per-item step (normalize, record, move) is guarded; any failure moves the native file to `ingest/_failed/` and `continue`s to the next item — one bad item never aborts the cycle.
- Env: `DRY_RUN=1` prints the planned actions without writing. `REPO_ROOT` overrides root (used by the test).

- [ ] **Step 1: Write the failing test**

```bash
# tests/test_ingest_flow.sh
#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Minimal fake repo: one topic dir + ingest + scripts + lib
mkdir -p "$TMP/docs/11-x/sources" "$TMP/ingest" "$TMP/scripts"
cp "$ROOT/scripts/lib.sh" "$ROOT/scripts/state.py" "$ROOT/scripts/ingest_lib.py" \
   "$ROOT/scripts/ingest_flow.sh" "$TMP/scripts/"
printf '# Hello\n\nsome content\n' > "$TMP/ingest/notes.md"

REPO_ROOT="$TMP" bash "$TMP/scripts/ingest_flow.sh" 11-x

fail=0
# corpus file written under sources/
n=$(find "$TMP/docs/11-x/sources" -name '*.md' | wc -l | tr -d ' ')
[ "$n" = "1" ] && echo "ok: one source file" || { echo "MISS: source file count=$n"; fail=1; }
# state records exactly one corpus entry and graph dirty
python3 - "$TMP" <<'PY' || fail=1
import json, sys
st = json.load(open(sys.argv[1] + "/.research/state.json"))
assert len(st["corpus"]) == 1, st["corpus"]
assert st["graph"]["dirty"] is True
assert st["corpus"][0]["lifecycle"] == "active"
print("ok: state has one active corpus entry, graph dirty")
PY
# native moved out of ingest/
[ -f "$TMP/ingest/_done/notes.md" ] && echo "ok: native archived" || { echo "MISS: native not archived"; fail=1; }
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"
exit "$fail"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/test_ingest_flow.sh`
Expected: FAIL — `ingest_flow.sh` does not exist yet, so the `cp` into `$TMP/scripts/` errors and no source file is produced; the test prints `MISS: source file count=0` and exits 1.

- [ ] **Step 3: Write minimal implementation**

Add helpers to `scripts/lib.sh` (append). Note: `transcribe_video` needs `youtube-transcript-api` in the crawl4ai venv — install once with `~/.venvs/crawl4ai/bin/pip install -q youtube-transcript-api` (markitdown's own YouTube path is unreliable; this is the working fallback). If absent, the helper degrades to a `_failed/` quarantine rather than crashing.

```bash
# Fetch a URL to markdown via crawl4ai; prints markdown to stdout.
fetch_link() {
  local url="$1" py="$HOME/.venvs/crawl4ai/bin/python" f="$HOME/.venvs/crawl4ai/fetch_md.py"
  "$py" "$f" "$url" 2>/dev/null
}

# Transcribe a YouTube/video URL to text via youtube-transcript-api; prints to stdout.
transcribe_video() {
  local url="$1" py="$HOME/.venvs/crawl4ai/bin/python"
  "$py" - "$url" <<'PY' 2>/dev/null
import sys, re
url = sys.argv[1]
m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
if not m:
    sys.exit(1)
from youtube_transcript_api import YouTubeTranscriptApi as A
try:
    data = A().fetch(m.group(1)); segs = [s.text for s in data]
except Exception:
    data = A.get_transcript(m.group(1)); segs = [s["text"] for s in data]
print("# " + url + "\n\n" + " ".join(segs))
PY
}
```

Create `scripts/ingest_flow.sh`:

```bash
#!/usr/bin/env bash
# Drain ingest/, normalize each item, record in state.json, flag graph dirty.
# Usage: ingest_flow.sh <topic>
set -uo pipefail   # NOT -e: a single bad item must not abort the cycle; failures are guarded per item.
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ROOT="${REPO_ROOT:-$(cd "$HERE/.." && pwd)}"
PY="python3"

topic="${1:-}"; [ -n "$topic" ] || { echo "usage: ingest_flow.sh <topic>" >&2; exit 2; }
dest="$(resolve_topic_dir "$ROOT" "$topic")/sources" || exit 1; mkdir -p "$dest"

# Fail one item: move its native to _failed and skip to the next.
fail_item() { echo "$2" >&2; mv "$1" "$ROOT/ingest/_failed/" 2>/dev/null; }

shopt -s nullglob
items=("$ROOT"/ingest/*)
real=(); for f in "${items[@]+"${items[@]}"}"; do
  b="$(basename "$f")"; [ "$b" = ".gitkeep" ] || [ "$b" = "_done" ] || [ "$b" = "_failed" ] || real+=("$f")
done
[ "${#real[@]}" -gt 0 ] || { echo "no new sources in ingest/"; exit 0; }

mkdir -p "$ROOT/ingest/_done" "$ROOT/ingest/_failed"
for f in "${real[@]}"; do
  name="$(basename "$f")"
  type="$("$PY" "$HERE/ingest_lib.py" detect "$name")"
  title="${name%.*}"
  slug="$(slugify "$title")"

  # Determine the stable seed + human-readable source per type.
  case "$type" in
    link)
      url="$(cat "$f")" || { fail_item "$f" "unreadable .url: $f"; continue; }
      seed="$url"; source_disp="$url" ;;
    *)
      seed="$("$PY" -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" "$f")" \
        || { fail_item "$f" "hash failed: $f"; continue; }
      source_disp="file://$name" ;;
  esac
  id="$("$PY" "$HERE/state.py" gen-id c "$seed")"
  out="$dest/${id}-${slug}.md"
  rel="$("$PY" -c "import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]))" "$out" "$ROOT")"

  if [ "${DRY_RUN:-}" = "1" ]; then echo "would ingest [$type] $source_disp -> $out"; continue; fi

  case "$type" in
    rawtext)  cp "$f" "$out" || { fail_item "$f" "copy failed: $f"; continue; } ;;
    link)
      case "$url" in
        *youtube.com*|*youtu.be*) transcribe_video "$url" > "$out" || { fail_item "$f" "transcribe failed: $url"; continue; } ;;
        *)                        fetch_link "$url"       > "$out" || { fail_item "$f" "fetch failed: $url"; continue; } ;;
      esac ;;
    document) "$MARKITDOWN" "$f" > "$out" 2>/dev/null || { fail_item "$f" "markitdown failed: $f"; continue; } ;;
  esac

  "$PY" "$HERE/state.py" add-corpus --root "$ROOT" --id "$id" --title "$title" --source "$source_disp" \
        --topic "$topic" --native "ingest/_done/$name" --extracted "$rel" >/dev/null \
        || { fail_item "$f" "record failed: $f"; rm -f "$out"; continue; }
  mv "$f" "$ROOT/ingest/_done/" || { echo "warning: could not archive $f" >&2; }
  echo "ingested [$type]: $source_disp -> $out"
done
echo "Done. Graph marked dirty; run the graph-update step next."
```

Make it executable:

```bash
chmod +x scripts/ingest_flow.sh
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/test_ingest_flow.sh`
Expected: `ALL OK`, exit 0. (Uses a `.md` fixture → `rawtext` passthrough, so no network/binary needed.)

- [ ] **Step 5: Commit**

```bash
git add scripts/ingest_flow.sh scripts/lib.sh tests/test_ingest_flow.sh
git commit -m "feat: add ingest flow (drain, normalize, record)"
```

---

### Task 5: Graph-delta event extraction

**Files:**
- Create: `scripts/graph_events.py`
- Test: `tests/test_graph_events.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `node_edge_sets(graph: dict) -> tuple[set, set]` — `({node ids}, {(source,target) tuples})`. Reads `graph["nodes"]` (each `{"id": ...}`) and `graph["edges"]` (each `{"source":..., "target":...}`); tolerates missing keys by returning empty sets.
  - `diff(old: dict, new: dict) -> dict` — `{"new_nodes": [...ids...], "new_edges": [[s,t],...]}` present in `new` but not `old`.
  - `append_event(events_path, delta: dict, now=None) -> None` — appends one JSON line `{"ts": now, "new_nodes": [...], "new_edges": [...]}` to `events_path`.
  - CLI: `python3 scripts/graph_events.py append --old O --new N --events E` — loads two graph.json files (missing `--old` treated as empty graph) and appends the delta.
- **Why a Python diff and not graphify's own:** graphify prints a diff during `--update`, but as console text, not a stable machine artifact. Diffing two `graph.json` snapshots here is the authoritative, tool-agnostic path. There is no race: in the session runtime the loops interleave between turns, so the back-up → `--update` → diff sequence runs sequentially within one agent turn.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_graph_events.py
import json, tempfile, unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import graph_events as ge


class TestGraphEvents(unittest.TestCase):
    def test_diff_reports_only_new(self):
        old = {"nodes": [{"id": "a"}], "edges": []}
        new = {"nodes": [{"id": "a"}, {"id": "b"}],
               "edges": [{"source": "a", "target": "b"}]}
        d = ge.diff(old, new)
        self.assertEqual(d["new_nodes"], ["b"])
        self.assertEqual(d["new_edges"], [["a", "b"]])

    def test_append_writes_one_jsonl_line(self):
        with tempfile.TemporaryDirectory() as t:
            ev = Path(t) / "graph-events.jsonl"
            ge.append_event(ev, {"new_nodes": ["b"], "new_edges": []}, now="2026-06-19T00:00:00Z")
            lines = ev.read_text(encoding="utf-8").strip().splitlines()
            self.assertEqual(len(lines), 1)
            rec = json.loads(lines[0])
            self.assertEqual(rec["new_nodes"], ["b"])
            self.assertEqual(rec["ts"], "2026-06-19T00:00:00Z")

    def test_missing_keys_tolerated(self):
        self.assertEqual(ge.diff({}, {}), {"new_nodes": [], "new_edges": []})


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_graph_events -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'graph_events'`.

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/graph_events.py
"""Compute graph deltas and append them to the event stream. Stdlib only."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def node_edge_sets(graph):
    nodes = {n.get("id") for n in graph.get("nodes", []) if n.get("id") is not None}
    edges = {(e.get("source"), e.get("target")) for e in graph.get("edges", [])
             if e.get("source") is not None and e.get("target") is not None}
    return nodes, edges


def diff(old, new):
    on, oe = node_edge_sets(old)
    nn, ne = node_edge_sets(new)
    return {
        "new_nodes": sorted(nn - on),
        "new_edges": [list(p) for p in sorted(ne - oe)],
    }


def append_event(events_path, delta, now=None):
    p = Path(events_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    rec = {"ts": now or datetime.now(timezone.utc).isoformat(),
           "new_nodes": delta.get("new_nodes", []),
           "new_edges": delta.get("new_edges", [])}
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _load(path):
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p and p.exists() else {}


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("append")
    a.add_argument("--old", default="")
    a.add_argument("--new", required=True)
    a.add_argument("--events", required=True)
    args = ap.parse_args(argv)
    if args.cmd == "append":
        d = diff(_load(args.old), _load(args.new))
        append_event(args.events, d)
        print(f"appended delta: +{len(d['new_nodes'])} nodes, +{len(d['new_edges'])} edges")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_graph_events -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/graph_events.py tests/test_graph_events.py
git commit -m "feat: add graph-delta event extraction"
```

---

### Task 6: Integrity check + spine lint

**Files:**
- Create: `scripts/check_integrity.py`
- Test: `tests/test_check_integrity.py`

**Interfaces:**
- Consumes: `state.load` (Task 1).
- Produces:
  - `check(root=".") -> list[str]` — returns a list of problem strings (empty = healthy). Checks: `state.json` parses and has the required top-level keys (`budget, gaps, inbox, corpus, graph, drafts`); every `corpus[*].extracted_path` resolves to an existing file under `root`; no two corpus entries share an `id`.
  - CLI: `python3 scripts/check_integrity.py [--root R]` prints each problem, exits 1 if any, else prints `integrity OK` and exits 0.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_check_integrity.py
import json, tempfile, unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_integrity as ci


def _write_state(root, corpus):
    p = Path(root) / ".research"; p.mkdir(parents=True, exist_ok=True)
    base = {"budget": {}, "gaps": [], "inbox": [], "corpus": corpus,
            "graph": {}, "drafts": []}
    (p / "state.json").write_text(json.dumps(base), encoding="utf-8")


class TestIntegrity(unittest.TestCase):
    def test_healthy_when_files_exist(self):
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "docs").mkdir()
            (Path(t) / "docs/x.md").write_text("hi", encoding="utf-8")
            _write_state(t, [{"id": "c1", "extracted_path": "docs/x.md"}])
            self.assertEqual(ci.check(t), [])

    def test_flags_missing_file(self):
        with tempfile.TemporaryDirectory() as t:
            _write_state(t, [{"id": "c1", "extracted_path": "docs/missing.md"}])
            probs = ci.check(t)
            self.assertTrue(any("missing.md" in p for p in probs))

    def test_flags_duplicate_id(self):
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "docs").mkdir()
            (Path(t) / "docs/x.md").write_text("hi", encoding="utf-8")
            _write_state(t, [{"id": "c1", "extracted_path": "docs/x.md"},
                             {"id": "c1", "extracted_path": "docs/x.md"}])
            self.assertTrue(any("duplicate" in p.lower() for p in ci.check(t)))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_check_integrity -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'check_integrity'`.

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/check_integrity.py
"""Integrity lint for the state spine. Stdlib only."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

REQUIRED_KEYS = ("budget", "gaps", "inbox", "corpus", "graph", "drafts")


def check(root="."):
    problems = []
    p = state_mod.state_path(root)
    if not p.exists():
        return ["no state.json found"]
    try:
        st = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"state.json unreadable: {e}"]
    for k in REQUIRED_KEYS:
        if k not in st:
            problems.append(f"state.json missing key: {k}")
    seen = set()
    for e in st.get("corpus", []):
        cid = e.get("id")
        if cid in seen:
            problems.append(f"duplicate corpus id: {cid}")
        seen.add(cid)
        ep = e.get("extracted_path", "")
        if not (Path(root) / ep).exists():
            problems.append(f"corpus {cid} missing file: {ep}")
    return problems


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    probs = check(args.root)
    for p in probs:
        print("PROBLEM:", p)
    if probs:
        return 1
    print("integrity OK")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_check_integrity -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/check_integrity.py tests/test_check_integrity.py
git commit -m "feat: add state spine integrity check"
```

---

### Task 7: Ingest loop prompt + wiring docs

**Files:**
- Create: `.claude/loop.md`
- Create: `.research/.gitkeep`
- Modify: `.gitignore` (ensure `.research/` is committed except temp files)
- Modify: `README.md` (document the ingest loop + graph step)
- Test: manual smoke (documented below) + run the full offline suite.

**Interfaces:**
- Consumes: `scripts/ingest_flow.sh`, `scripts/graph_events.py`, the graphify skill.
- Produces: a default `/loop` prompt that runs one ingest cycle. No code under test (it is an agent prompt); correctness is verified by the manual smoke and the existing unit/integration suites.

- [ ] **Step 1: Write the loop prompt**

```markdown
<!-- .claude/loop.md -->
# Ingest cycle

Run one ingest cycle for the research engine. Do exactly this, then stop:

1. Run `bash scripts/ingest_flow.sh <default-topic>` (default topic: `13-reference-systems-case-studies` unless a dropped file names another). This drains `ingest/`, normalizes each item, records it in `.research/state.json`, and flags the graph dirty.
2. If `.research/state.json` shows `graph.dirty == true`: back up the current graph (`cp .graphify/graph.json .graphify/.graphify_old.json` if it exists), then invoke the **graphify skill with `--update`** to incrementally extract only the new/changed source files (semantic update — this is an LLM step, not the code-only `graphify update` CLI).
3. After the graph update, append the delta to the event stream:
   `python3 scripts/graph_events.py append --old .graphify/.graphify_old.json --new .graphify/graph.json --events .research/graph-events.jsonl`
4. Clear the dirty flag and record the new graph size:
   ```
   N=$(python3 -c 'import json;print(len(json.load(open(".graphify/graph.json")).get("nodes",[])))')
   E=$(python3 -c 'import json;print(len(json.load(open(".graphify/graph.json")).get("edges",[])))')
   python3 scripts/state.py set-graph --dirty false --node-count "$N" --edge-count "$E"
   ```
5. Run `python3 scripts/check_integrity.py` — if it reports problems, stop and surface them; do not claim the cycle succeeded.

If `ingest/` was empty (step 1 printed "no new sources"), stop early — nothing to do this cycle.
```

- [ ] **Step 2: Add `.research/` keep + gitignore rule**

```bash
mkdir -p .research && touch .research/.gitkeep
```

Append to `.gitignore`:

```gitignore
# research engine state spine is committed; only atomic-write temp files are ignored
.research/*.tmp
```

- [ ] **Step 3: Document in README**

Add under the Quickstart section of `README.md`:

```markdown
### Continuous ingest loop
- Drop sources (files/links/videos/raw text) into `ingest/`.
- `scripts/ingest_flow.sh <topic>` normalizes them into `docs/<topic>/sources/`, records each in `.research/state.json` with a durable id + lifecycle, and flags the graph dirty.
- The graph is updated incrementally (graphify `--update`); deltas append to `.research/graph-events.jsonl` (the realtime-view feed + audit log).
- Run the loop hands-off with `/loop` (uses `.claude/loop.md`).
```

- [ ] **Step 4: Manual smoke test**

```bash
echo "# Smoke

test content" > ingest/smoke-test.md
bash scripts/ingest_flow.sh 13-reference-systems-case-studies
python3 scripts/check_integrity.py
git status --short   # expect: new file under docs/13-.../sources/, updated .research/state.json
```
Expected: ingest prints `ingested [rawtext]`, integrity prints `integrity OK`, a new source file and an updated `state.json` appear. Clean up the smoke artifacts before committing if undesired.

- [ ] **Step 5: Run the full offline suite**

Run:
```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
bash tests/test_ingest_flow.sh
bash tests/test_catalog.sh
```
Expected: all PASS / `ALL OK`.

- [ ] **Step 6: Commit**

```bash
git add .claude/loop.md .research/.gitkeep .gitignore README.md
git commit -m "feat: wire ingest loop prompt and document the flow"
```

---

## Self-Review

**Spec coverage (sub-project #1 scope = spine + ingest flow):**
- `state.json` spine schema (§4) → Tasks 1–2 (full `DEFAULT_STATE`, corpus + graph ops).
- Durable IDs + metadata + lifecycle at ingest (§4, findings-11) → Task 2 `add_corpus_entry` (deterministic id, `lifecycle="active"`, `ingested_at`).
- Type-routed normalization markitdown/crawl4ai/raw + YouTube-transcript (§6②) → Tasks 3–4 (`detect_type` returns `link|rawtext|document`; `ingest_flow.sh` reads the URL for links and re-routes YouTube to `transcribe_video`).
- Incremental graph update, not rebuild (§6②, decision) → Task 7 step 2 (graphify skill `--update`, with the accurate note that the CLI `update` is code-only).
- Graph-delta event stream for realtime view (§7) → Task 5 + Task 7 step 3 (`graph_events.py` → `.research/graph-events.jsonl`).
- Crash-safety / idempotency (§9) → Task 2 deterministic-id dedup; `ingest/_done` + `_failed` quarantine in Task 4.
- Integrity test (§10) → Task 6 (`check_integrity.py`) + Task 7 step 5 (full suite incl. existing `test_catalog.sh`).
- Fixture self-check (§10) → Task 4 `tests/test_ingest_flow.sh`.

Deferred to later sub-projects (correctly out of scope here): assertions overlay replay (§6④ → sub-project #4), search/gaps flow (§6① → #2), process/drafts flow (§6③ → #3), websocket view (§7 → #5), budget governor fan-out (§5 → #2/#3). The `budget`, `gaps`, `inbox`, `assertions`, `drafts` fields are seeded empty by Task 1 so later sub-projects extend rather than reshape the schema.

**Placeholder scan:** no TBD/TODO; every code step contains complete runnable code; commands have expected output. None found.

**Type consistency:** `gen_id(prefix, seed)` used identically in Tasks 1, 2, 4. `add_corpus_entry(..., id=None)` keyword signature matches its CLI (`--title/--source/--topic/--native/--extracted/--lossy/--id`); Task 4 passes `--id "$id"` with the content-hash/URL seed. `set_graph(...)` matches its `set-graph` CLI (`--dirty/--node-count/--edge-count/--last-update`) used by Task 4's helper and the Task 7 loop prompt. `diff`/`append_event`/`node_edge_sets` names match between Task 5 implementation, its test, and the Task 7 CLI invocation. `check(root)` matches between Task 6 implementation, test, and CLI. Graph path `.graphify/graph.json` used consistently; the graphify CLI default `graphify-out/` is never relied on.
