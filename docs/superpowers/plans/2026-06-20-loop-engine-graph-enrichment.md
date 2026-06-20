# Graph Enrichment (Asserted Edges) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an append-only, committed assertion overlay that lets the process flow author cross-community "bridge" edges which survive `graphify --update`, replayed into `graph.json` after every update so god-node/bridge analysis can read asserted structure distinctly from observed structure.

**Architecture:** Asserted edges live in `.research/graph-assertions.jsonl` (one JSON object per line, committed). A new `scripts/assertions.py` authors lines, prunes them via tombstones, and **replays** the active set into `.graphify/graph.json`'s `links` array — each merged link tagged `_origin:"asserted"`. Replay first strips prior asserted links, so it is idempotent; pruning a line and re-replaying removes the edge. Replay runs in the ingest cycle between `graphify --update` and the `graph_events.py` delta append, so the realtime feed sees the merged graph.

**Tech Stack:** Python 3 stdlib only (`json`, `hashlib`, `argparse`, `pathlib`). Tests are `unittest`. No pip, no pytest.

## Global Constraints

- **Python 3 stdlib only** — no pip, no pytest, no new dependencies. Tests are `unittest` + bash `test_*.sh`. `tests/__init__.py` exists; tests do `sys.path.insert(0, .../scripts)`.
- **No lint/type/static-analysis suppression comments anywhere** (`# noqa`, `# type: ignore`, etc.) — fix the code.
- **Durable ids** seed on a structural key, never on-disk path. Assertion id = `gen_id("a", from + "|" + to + "|" + relation)` → `"a"` + 8 lowercase hex (9 chars total). Corpus/cite ids are `"c"` + 8 hex — literal example ids in code/tests must be exactly 8 hex or `cite`/assertion validation silently mismatches.
- **`graph.json` is NetworkX node_link format:** top keys `directed, multigraph, graph, nodes, links, hyperedges, built_at_commit`. **Edges live under `links`** (not `edges`). A node is `{"id": ..., "label": ..., ...}`. A link is `{"source": <from-node-id>, "target": <to-node-id>, "relation": ..., "weight": ..., ...}`. `source`/`target` are the endpoint keys — provenance is tagged with `_origin`, mirroring the node convention (`node["_origin"] == "ast"`).
- **`.graphify/` is gitignored; `.research/` is committed** (only `.research/*.tmp` ignored). The overlay `.research/graph-assertions.jsonl` is therefore a committed artifact.
- **Assertions are autonomous, not human-gated:** auto-applied and always recorded (unlike drafts). `author`/`confidence`/`cites` keep each edge accountable.
- **Commits:** Conventional Commits, selectively staged (never `git add .`/`-A`), no co-author trailers, no "Generated with" lines.
- Running `state.py`/`assertions.py` CLIs against a clean repo **seeds a default `.research/state.json`** as a side effect — do not stage that artifact when it appears in a clean tree.

## File Structure

- **Create `scripts/assertions.py`** — overlay author + prune + count-sync + replay, plus CLI (`add`, `prune`, `list`, `replay`). One responsibility: the assertion overlay and its projection into `graph.json`. Imports `state` as a module (same pattern as `check_integrity.py`) to validate cites and sync `state.assertions.count`.
- **Modify `scripts/check_integrity.py`** — add assertion validation (every active assertion's `from`/`to` resolve to a real `graph.json` node id when the graph exists; every `cites` entry resolves to a `corpus` id).
- **Modify `scripts/graph_events.py`** — `node_edge_sets` must read the `links` array (NetworkX), falling back to `edges`, so asserted edges actually appear in the delta feed. This is a latent defect (it has always read the absent `edges` key); sub-project #4 is the first to depend on edge deltas, so it is fixed here.
- **Modify `.claude/loop.md`** — insert a replay step between the `graphify --update` step and the `graph_events.py append` step.
- **Modify `.claude/process.md`** — re-enable the assertion-authoring step deferred in sub-project #3.
- **Create `tests/test_assertions.py`** — unittest for load/dedup/tombstone/add/prune/count-sync/replay idempotency.
- **Modify `tests/test_check_integrity.py`** — assertion validation cases.
- **Modify `tests/test_graph_events.py`** — `links`-based edge delta.

---

### Task 1: Assertion overlay — author, prune, load, count-sync

**Files:**
- Create: `scripts/assertions.py`
- Test: `tests/test_assertions.py`

**Interfaces:**
- Consumes: `state.gen_id(prefix, seed)`, `state.load(root)`, `state.save(state, root)`, `state._now()` from `scripts/state.py`.
- Produces:
  - `OVERLAY_REL = ".research/graph-assertions.jsonl"`
  - `RELATIONS = ("bridges", "supports", "contradicts", "refines")`
  - `overlay_path(root=".") -> pathlib.Path`
  - `load_overlay(root=".") -> list[dict]` — active assertions only (tombstones removed), last-write-wins by `id`, in first-seen order.
  - `add_assertion(root=".", *, frm, to, relation, rationale, cites, author="ai", confidence=0.8, id=None, now=None) -> dict` — validates `relation` and that every `cites` id is a real `corpus` id; appends one line; syncs count; returns the assertion dict.
  - `prune_assertion(root=".", assertion_id, now=None) -> bool` — appends a tombstone line `{"id":..., "pruned": true, "pruned_at": ...}`; syncs count; returns True if an active assertion by that id existed.
  - `sync_count(root=".") -> int` — sets `state["assertions"]["count"]` to `len(load_overlay(root))`, saves state, returns the count.

- [ ] **Step 1: Write the failing test**

Create `tests/test_assertions.py`:

```python
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import assertions
import state as state_mod


def _seed_corpus(root, ids):
    st = state_mod.load(root)
    for cid in ids:
        st["corpus"].append({
            "id": cid, "title": cid, "source": cid, "topic": "t",
            "lifecycle": "active", "native_path": "n", "extracted_path": "e",
            "lossy": False, "ingested_at": "now",
        })
    state_mod.save(st, root)


class AddAndLoad(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        _seed_corpus(self.tmp, ["c0000aaaa", "c0000bbbb"])

    def test_add_appends_active_assertion_with_durable_id(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="both describe provenance", cites=["c0000aaaa"],
        )
        self.assertEqual(a["id"], state_mod.gen_id("a", "node_x|node_y|bridges"))
        self.assertTrue(a["id"].startswith("a"))
        self.assertEqual(len(a["id"]), 9)
        loaded = assertions.load_overlay(root=self.tmp)
        self.assertEqual([x["id"] for x in loaded], [a["id"]])
        self.assertEqual(loaded[0]["relation"], "bridges")
        self.assertEqual(loaded[0]["author"], "ai")
        self.assertEqual(loaded[0]["confidence"], 0.8)

    def test_add_rejects_unknown_relation(self):
        with self.assertRaises(ValueError):
            assertions.add_assertion(
                root=self.tmp, frm="a", to="b", relation="causes",
                rationale="r", cites=["c0000aaaa"])

    def test_add_rejects_dangling_cite(self):
        with self.assertRaises(ValueError):
            assertions.add_assertion(
                root=self.tmp, frm="a", to="b", relation="supports",
                rationale="r", cites=["c9999dead"])

    def test_count_synced_into_state(self):
        assertions.add_assertion(
            root=self.tmp, frm="a", to="b", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        st = state_mod.load(self.tmp)
        self.assertEqual(st["assertions"]["count"], 1)


class Prune(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        _seed_corpus(self.tmp, ["c0000aaaa"])

    def test_prune_removes_from_active_set_but_file_stays_append_only(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="a", to="b", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        lines_before = assertions.overlay_path(self.tmp).read_text().count("\n")
        ok = assertions.prune_assertion(root=self.tmp, assertion_id=a["id"])
        self.assertTrue(ok)
        self.assertEqual(assertions.load_overlay(root=self.tmp), [])
        lines_after = assertions.overlay_path(self.tmp).read_text().count("\n")
        self.assertEqual(lines_after, lines_before + 1)  # tombstone appended, nothing deleted
        st = state_mod.load(self.tmp)
        self.assertEqual(st["assertions"]["count"], 0)

    def test_readd_after_prune_reactivates(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="a", to="b", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        assertions.prune_assertion(root=self.tmp, assertion_id=a["id"])
        assertions.add_assertion(
            root=self.tmp, frm="a", to="b", relation="bridges",
            rationale="r2", cites=["c0000aaaa"])
        loaded = assertions.load_overlay(root=self.tmp)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["rationale"], "r2")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_assertions -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'assertions'` (file not created yet).

- [ ] **Step 3: Write minimal implementation**

Create `scripts/assertions.py`:

```python
"""Asserted-edge overlay for the knowledge graph. Stdlib only.

The overlay (.research/graph-assertions.jsonl) is append-only and committed.
Each active line is an asserted edge; a `{"id": ..., "pruned": true}` line is a
tombstone that retires an earlier id (last-write-wins). Replay (Task 2) projects
the active set into graph.json's `links` array.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

OVERLAY_REL = ".research/graph-assertions.jsonl"
RELATIONS = ("bridges", "supports", "contradicts", "refines")


def overlay_path(root="."):
    return Path(root) / OVERLAY_REL


def load_overlay(root="."):
    p = overlay_path(root)
    if not p.exists():
        return []
    by_id = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rec = json.loads(line)
        rid = rec.get("id")
        if rid is None:
            continue
        by_id[rid] = rec  # last-write-wins
    return [r for r in by_id.values() if not r.get("pruned")]


def _append_line(root, rec):
    p = overlay_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def sync_count(root="."):
    st = state_mod.load(root)
    n = len(load_overlay(root))
    st["assertions"]["count"] = n
    st["assertions"]["file"] = OVERLAY_REL
    state_mod.save(st, root)
    return n


def add_assertion(root=".", *, frm, to, relation, rationale, cites,
                  author="ai", confidence=0.8, id=None, now=None):
    if relation not in RELATIONS:
        raise ValueError(f"unknown relation: {relation} (allowed: {RELATIONS})")
    st = state_mod.load(root)
    corpus_ids = {e["id"] for e in st["corpus"]}
    for cid in cites:
        if cid not in corpus_ids:
            raise ValueError(f"dangling cite: {cid}")
    aid = id or state_mod.gen_id("a", frm + "|" + to + "|" + relation)
    rec = {
        "id": aid, "from": frm, "to": to, "relation": relation,
        "rationale": rationale, "cites": list(cites), "author": author,
        "confidence": confidence, "created_at": now or state_mod._now(),
    }
    _append_line(root, rec)
    sync_count(root)
    return rec


def prune_assertion(root=".", assertion_id=None, now=None):
    active = {r["id"] for r in load_overlay(root)}
    existed = assertion_id in active
    _append_line(root, {"id": assertion_id, "pruned": True,
                        "pruned_at": now or state_mod._now()})
    sync_count(root)
    return existed


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add")
    a.add_argument("--root", default=".")
    a.add_argument("--from", dest="frm", required=True)
    a.add_argument("--to", required=True)
    a.add_argument("--relation", required=True)
    a.add_argument("--rationale", required=True)
    a.add_argument("--cites", required=True, help="comma-separated corpus ids")
    a.add_argument("--author", default="ai")
    a.add_argument("--confidence", type=float, default=0.8)
    a.add_argument("--id", default=None)

    pr = sub.add_parser("prune")
    pr.add_argument("--root", default=".")
    pr.add_argument("id")

    li = sub.add_parser("list")
    li.add_argument("--root", default=".")

    args = ap.parse_args(argv)
    if args.cmd == "add":
        cites = [c for c in args.cites.split(",") if c]
        rec = add_assertion(root=args.root, frm=args.frm, to=args.to,
                            relation=args.relation, rationale=args.rationale,
                            cites=cites, author=args.author,
                            confidence=args.confidence, id=args.id)
        print(rec["id"])
        return 0
    if args.cmd == "prune":
        ok = prune_assertion(root=args.root, assertion_id=args.id)
        print("pruned" if ok else "no such active assertion")
        return 0
    if args.cmd == "list":
        for r in load_overlay(args.root):
            print(f"{r['id']} {r['relation']} {r['from']} -> {r['to']}")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

> **Import style:** the repo runs no flake8 — existing tests (`test_state.py`, `test_check_integrity.py`) place `sys.path.insert` before the local import with **no** suppression comments. The snippet above already matches; do not add `# noqa`.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_assertions -v`
Expected: PASS (5 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/assertions.py tests/test_assertions.py
git commit -m "feat: add asserted-edge overlay author/prune/load"
```

---

### Task 2: Replay overlay into graph.json

**Files:**
- Modify: `scripts/assertions.py` (add `replay` + CLI `replay` subcommand)
- Test: `tests/test_assertions.py` (add `Replay` test case)

**Interfaces:**
- Consumes: `load_overlay(root)` from Task 1; `graph.json` NetworkX node_link shape.
- Produces:
  - `GRAPH_REL = ".graphify/graph.json"`
  - `replay(root=".", graph_path=None) -> dict` — strips links with `_origin == "asserted"`, appends one asserted link per active assertion, writes `graph.json` atomically, returns `{"asserted": int, "stripped": int, "skipped": str | None}`. If the graph file does not exist, no-op returning `{"asserted": 0, "stripped": 0, "skipped": "no graph at <path>"}`.
  - Asserted link shape merged into `links`:
    `{"source": <from>, "target": <to>, "relation": <relation>, "weight": 1.0, "_origin": "asserted", "assertion_id": <id>, "rationale": <rationale>, "cites": <cites>, "author": <author>, "confidence": <confidence>}`

- [ ] **Step 1: Write the failing test**

Append to `tests/test_assertions.py` (before the `if __name__` block):

```python
class Replay(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        _seed_corpus(self.tmp, ["c0000aaaa"])
        gp = Path(self.tmp) / ".graphify" / "graph.json"
        gp.parent.mkdir(parents=True, exist_ok=True)
        gp.write_text(json.dumps({
            "directed": False, "multigraph": False, "graph": {},
            "nodes": [{"id": "node_x"}, {"id": "node_y"}],
            "links": [{"source": "node_x", "target": "node_y",
                       "relation": "contains", "weight": 1.0}],
        }), encoding="utf-8")
        self.gp = gp

    def _links(self):
        return json.loads(self.gp.read_text())["links"]

    def test_replay_merges_asserted_link_tagged_origin(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        res = assertions.replay(root=self.tmp)
        self.assertEqual(res["asserted"], 1)
        asserted = [l for l in self._links() if l.get("_origin") == "asserted"]
        self.assertEqual(len(asserted), 1)
        self.assertEqual(asserted[0]["source"], "node_x")
        self.assertEqual(asserted[0]["target"], "node_y")
        self.assertEqual(asserted[0]["assertion_id"], a["id"])
        observed = [l for l in self._links() if l.get("_origin") != "asserted"]
        self.assertEqual(len(observed), 1)  # original observed link preserved

    def test_replay_is_idempotent(self):
        assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        assertions.replay(root=self.tmp)
        first = self._links()
        assertions.replay(root=self.tmp)
        second = self._links()
        self.assertEqual(first, second)
        self.assertEqual(
            len([l for l in second if l.get("_origin") == "asserted"]), 1)

    def test_pruned_assertion_disappears_on_replay(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        assertions.replay(root=self.tmp)
        assertions.prune_assertion(root=self.tmp, assertion_id=a["id"])
        res = assertions.replay(root=self.tmp)
        self.assertEqual(res["asserted"], 0)
        self.assertEqual(
            [l for l in self._links() if l.get("_origin") == "asserted"], [])

    def test_replay_no_graph_is_noop(self):
        empty = tempfile.mkdtemp()
        res = assertions.replay(root=empty)
        self.assertEqual(res["asserted"], 0)
        self.assertIn("no graph", res["skipped"])
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_assertions.Replay -v`
Expected: FAIL — `AttributeError: module 'assertions' has no attribute 'replay'`.

- [ ] **Step 3: Write minimal implementation**

In `scripts/assertions.py`, add the constant near `OVERLAY_REL`:

```python
GRAPH_REL = ".graphify/graph.json"
```

Add the `replay` function after `prune_assertion`:

```python
def _asserted_link(rec):
    return {
        "source": rec["from"], "target": rec["to"],
        "relation": rec["relation"], "weight": 1.0, "_origin": "asserted",
        "assertion_id": rec["id"], "rationale": rec.get("rationale", ""),
        "cites": rec.get("cites", []), "author": rec.get("author", "ai"),
        "confidence": rec.get("confidence"),
    }


def replay(root=".", graph_path=None):
    gp = Path(graph_path) if graph_path else Path(root) / GRAPH_REL
    if not gp.exists():
        return {"asserted": 0, "stripped": 0, "skipped": f"no graph at {gp}"}
    graph = json.loads(gp.read_text(encoding="utf-8"))
    links = graph.get("links", [])
    kept = [l for l in links if l.get("_origin") != "asserted"]
    stripped = len(links) - len(kept)
    active = load_overlay(root)
    graph["links"] = kept + [_asserted_link(r) for r in active]
    tmp = gp.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(graph, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, gp)
    return {"asserted": len(active), "stripped": stripped, "skipped": None}
```

Add the `replay` CLI subcommand inside `_main`, after the `list` parser:

```python
    rp = sub.add_parser("replay")
    rp.add_argument("--root", default=".")
    rp.add_argument("--graph", default=None)
```

And the dispatch branch, before `return 1`:

```python
    if args.cmd == "replay":
        res = replay(root=args.root, graph_path=args.graph)
        if res["skipped"]:
            print(res["skipped"])
        else:
            print(f"replayed: +{res['asserted']} asserted links "
                  f"(stripped {res['stripped']})")
        return 0
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_assertions -v`
Expected: PASS (9 tests total).

- [ ] **Step 5: Commit**

```bash
git add scripts/assertions.py tests/test_assertions.py
git commit -m "feat: replay assertion overlay into graph.json links (idempotent)"
```

---

### Task 3: Integrity check for assertions

**Files:**
- Modify: `scripts/check_integrity.py`
- Test: `tests/test_check_integrity.py`

**Interfaces:**
- Consumes: `assertions.load_overlay(root)` (Task 1), `assertions.GRAPH_REL` (Task 2), existing `check(root)` problems list.
- Produces: additional `problems` entries:
  - `f"assertion {aid} references missing node: {nid}"` — when `graph.json` exists and `from`/`to` is not a node id.
  - `f"assertion {aid} dangling cite: {cid}"` — when a `cites` id is not a `corpus` id.
  - Node validation is **skipped** when `graph.json` is absent (the graph may not be built yet — mirrors the existing "absent state.json ⇒ healthy" leniency).

- [ ] **Step 1: Write the failing test**

First inspect the existing test layout: `python3 -m unittest tests.test_check_integrity -v` and open `tests/test_check_integrity.py`. Its import block is `import check_integrity as ci` only — **add `import assertions` and `import state as state_mod`** below the `sys.path.insert` line (the path insert is already there). The existing helpers (`_write_state`) write a raw dict; the new class below seeds via `state_mod.load`/`save` instead because `assertions.add_assertion` needs a real default state. Note the module is aliased `ci` — use `ci.check`, not `check_integrity.check`. Then add:

```python
class AssertionIntegrity(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        st = state_mod.load(self.tmp)
        st["corpus"].append({
            "id": "c0000aaaa", "title": "t", "source": "s", "topic": "t",
            "lifecycle": "active", "native_path": "n",
            "extracted_path": "e.md", "lossy": False, "ingested_at": "now",
        })
        (Path(self.tmp) / "e.md").write_text("x", encoding="utf-8")
        state_mod.save(st, self.tmp)
        gp = Path(self.tmp) / ".graphify" / "graph.json"
        gp.parent.mkdir(parents=True, exist_ok=True)
        gp.write_text(json.dumps({
            "nodes": [{"id": "node_x"}, {"id": "node_y"}], "links": [],
        }), encoding="utf-8")

    def test_clean_assertion_passes(self):
        assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        self.assertEqual(ci.check(self.tmp), [])

    def test_missing_node_flagged(self):
        assertions.add_assertion(
            root=self.tmp, frm="node_x", to="ghost", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        probs = ci.check(self.tmp)
        self.assertTrue(any("missing node: ghost" in p for p in probs))

    def test_node_check_skipped_without_graph(self):
        (Path(self.tmp) / ".graphify" / "graph.json").unlink()
        assertions.add_assertion(
            root=self.tmp, frm="node_x", to="ghost", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        probs = ci.check(self.tmp)
        self.assertFalse(any("missing node" in p for p in probs))
```

The existing import block already provides `json`, `tempfile`, `Path`, and `ci`; you only need to add `import assertions` and `import state as state_mod`.

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_check_integrity.AssertionIntegrity -v`
Expected: FAIL — `test_missing_node_flagged` fails (no assertion validation yet; `check` returns `[]`).

- [ ] **Step 3: Write minimal implementation**

In `scripts/check_integrity.py`, add to the import block (after `import state as state_mod`):

```python
import assertions as assertions_mod
```

Then, inside `check()`, after the drafts loop and before `return problems`, add:

```python
    active = assertions_mod.load_overlay(root)
    if active:
        gp = Path(root) / assertions_mod.GRAPH_REL
        node_ids = None
        if gp.exists():
            graph = json.loads(gp.read_text(encoding="utf-8"))
            node_ids = {n.get("id") for n in graph.get("nodes", [])}
        for a in active:
            aid = a.get("id")
            if node_ids is not None:
                for endpoint in (a.get("from"), a.get("to")):
                    if endpoint not in node_ids:
                        problems.append(
                            f"assertion {aid} references missing node: {endpoint}")
            for cid in a.get("cites", []):
                if cid not in corpus_ids:
                    problems.append(f"assertion {aid} dangling cite: {cid}")
```

(`corpus_ids` is already computed earlier in `check()` for the drafts loop — reuse it.)

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_check_integrity -v`
Expected: PASS (existing tests + 3 new).

- [ ] **Step 5: Commit**

```bash
git add scripts/check_integrity.py tests/test_check_integrity.py
git commit -m "feat: integrity-check assertion node + cite references"
```

---

### Task 4: graph_events reads `links` so asserted edges reach the feed

**Files:**
- Modify: `scripts/graph_events.py:node_edge_sets`
- Test: `tests/test_graph_events.py`

**Interfaces:**
- Produces: `node_edge_sets(graph)` reads edges from `graph["links"]` when present, else `graph["edges"]` (back-compat). Unchanged return shape `(nodes:set, edges:set[(source,target)])`.

**Why:** `graph.json` (NetworkX node_link) stores edges under `links`, not `edges`. `node_edge_sets` reads `graph.get("edges", [])`, so every delta has reported zero edges. The replay step (Task 2) appends asserted edges to `links`; without this fix the ingest cycle's `graph_events.py append` (which runs *after* replay) would still emit empty edge deltas, defeating the "the events feed sees the merged graph" requirement.

- [ ] **Step 1: Write the failing test**

First run `python3 -m unittest tests.test_graph_events -v` and read `tests/test_graph_events.py`. The module is imported aliased as `import graph_events as ge` — use `ge.diff`. Add:

```python
class LinksFormat(unittest.TestCase):
    def test_diff_reads_links_array(self):
        old = {"nodes": [{"id": "a"}], "links": []}
        new = {"nodes": [{"id": "a"}, {"id": "b"}],
               "links": [{"source": "a", "target": "b"}]}
        d = ge.diff(old, new)
        self.assertEqual(d["new_nodes"], ["b"])
        self.assertEqual(d["new_edges"], [["a", "b"]])

    def test_diff_still_reads_legacy_edges_key(self):
        old = {"nodes": [], "edges": []}
        new = {"nodes": [{"id": "a"}, {"id": "b"}],
               "edges": [{"source": "a", "target": "b"}]}
        d = ge.diff(old, new)
        self.assertEqual(d["new_edges"], [["a", "b"]])
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_graph_events.LinksFormat -v`
Expected: FAIL — `test_diff_reads_links_array` returns `new_edges == []` (the `links` array is ignored).

- [ ] **Step 3: Write minimal implementation**

In `scripts/graph_events.py`, change `node_edge_sets`:

```python
def node_edge_sets(graph):
    nodes = {n.get("id") for n in graph.get("nodes", []) if n.get("id") is not None}
    raw_edges = graph.get("links", graph.get("edges", []))
    edges = {(e.get("source"), e.get("target")) for e in raw_edges
             if e.get("source") is not None and e.get("target") is not None}
    return nodes, edges
```

Keep the key-presence fallback (`graph.get("links", …)`) exactly as written. Do **not** rewrite it as `graph.get("links") or graph.get("edges", [])` — that truthiness form would ignore a present-but-empty `links: []`, changing behavior. Real graphify output emits `links` only, so the key-presence form is correct.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_graph_events -v`
Expected: PASS (existing tests + 2 new).

- [ ] **Step 5: Commit**

```bash
git add scripts/graph_events.py tests/test_graph_events.py
git commit -m "fix: graph_events diffs the links array (networkx node_link)"
```

---

### Task 5: Wire replay into the ingest cycle and re-enable assertion authoring in process

**Files:**
- Modify: `.claude/loop.md` (insert replay step between graph update and event append)
- Modify: `.claude/process.md` (re-enable the deferred assertion-authoring step)

**Interfaces:** none (prompt files). Verified by an end-to-end smoke, not a unit test.

- [ ] **Step 1: Read both prompt files**

Run: `cat .claude/loop.md .claude/process.md` to get the exact current numbered steps to anchor the edits.

- [ ] **Step 2: Edit `.claude/loop.md` — insert the replay step**

The current cycle is: (1) `ingest_flow.sh`, (2) backup + graphify `--update`, (3) `graph_events.py append`, (4) `set-graph`, (5) `check_integrity`. Insert a new step **between current step 2 and step 3**, and renumber the rest. The new step text:

```markdown
3. **Replay the assertion overlay** into the freshly-updated graph (asserted
   edges survive `graphify --update`, which only knows the corpus):
   `python3 scripts/assertions.py replay`
   This strips and re-merges every active asserted edge into
   `.graphify/graph.json` (tagged `_origin: asserted`); it is idempotent and a
   no-op if no graph or no assertions exist. It must run **before** the
   `graph_events.py append` below so the delta feed sees the merged graph.
```

After inserting, the `graph_events.py append`, `set-graph`, and `check_integrity` steps shift to 4/5/6. Renumber them so the list reads 1–6 in order.

**Also fix the `edge_count` computation in the (now-renumbered) `set-graph` step.** That step currently computes `E` from `…get("edges",[])`, but the graph stores edges under `links` (the same defect Task 4 fixes in `graph_events.py`); left as-is it records `edge_count: 0` even after replay merges asserted edges. Change the `E=` line to read `links` with an `edges` fallback:

```bash
   E=$(python3 -c 'import json;g=json.load(open(".graphify/graph.json"));print(len(g.get("links",g.get("edges",[]))))')
```

- [ ] **Step 3: Edit `.claude/process.md` — re-enable assertion authoring**

The process cycle currently ends step 6 (emit gaps), step 7 (`check_integrity`), and a closing paragraph whose last sentence reads:

> Graph assertions (§6④) are sub-project #4 — do not author them here.

Replace that deferral. Insert a new authoring step **between the current step 6 (emit gaps) and step 7 (`check_integrity`)**, renumber `check_integrity` to step 8, and delete the entire final sentence `Graph assertions (§6④) are sub-project #4 — do not author them here.` from the closing paragraph (leaving the paragraph ending at "...or rejects it (`promote.py reject <id>`)."). The new step:

```markdown
7. Author graph assertions (optional, autonomous — no human gate). While
   reading the knowledge graph in step 2, if you perceive a **missing
   cross-community link** — two nodes in different communities that your
   sources show are genuinely related (a bridge), or one source that
   `supports`/`contradicts`/`refines` another — append one assertion per link:
   ```
   python3 scripts/assertions.py add \
     --from "<node_id>" --to "<node_id>" \
     --relation bridges|supports|contradicts|refines \
     --rationale "<why these two connect>" \
     --cites "c…,c…"
   ```
   `--from`/`--to` are `id`s from `.graphify/graph.json` (the `nodes[].id`
   field, not the label); `--cites` are the `corpus` ids that justify the edge.
   Assertions are auto-applied on the next ingest cycle's replay and are always
   recorded — only assert links you can defend from cited sources. Skip this
   step if no missing link is evident; do not invent edges to fill a quota.
```

Renumber the final `check_integrity` step to 8.

- [ ] **Step 4: Verify the prompt edits are coherent**

Run: `cat .claude/loop.md .claude/process.md` and confirm: loop.md steps run 1–6 with replay between graphify-update and event-append; process.md steps run 1–8 with authoring before the final integrity check; the "do not author" sentence is gone.

- [ ] **Step 5: Commit**

```bash
git add .claude/loop.md .claude/process.md
git commit -m "feat: wire assertion replay into ingest cycle, re-enable authoring in process"
```

---

### Task 6: End-to-end smoke + full test suite

**Files:**
- Create: `tests/test_assertions_smoke.sh` (bash, mirrors `tests/test_process_flow.sh` style)

**Interfaces:** exercises the real CLIs against a throwaway temp root — the smallest thing that fails if author→replay→integrity breaks together.

- [ ] **Step 1: Write the smoke test**

Create `tests/test_assertions_smoke.sh`:

```bash
#!/usr/bin/env bash
# End-to-end: seed corpus + graph -> add assertion -> replay -> integrity clean
# -> prune -> replay -> assertion gone. Stdlib only; no network.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/.graphify"
# Minimal corpus entry (extracted file must exist for integrity).
echo "src" > "$TMP/e.md"
python3 "$ROOT/scripts/state.py" add-corpus --root "$TMP" \
  --title T --source S --topic t --native n --extracted e.md --id c0000aaaa >/dev/null
# Minimal node_link graph with two nodes.
cat > "$TMP/.graphify/graph.json" <<'JSON'
{"nodes":[{"id":"node_x"},{"id":"node_y"}],"links":[]}
JSON

AID="$(python3 "$ROOT/scripts/assertions.py" add --root "$TMP" \
  --from node_x --to node_y --relation bridges \
  --rationale "bridge" --cites c0000aaaa)"
echo "added $AID"

python3 "$ROOT/scripts/assertions.py" replay --root "$TMP"
COUNT="$(python3 -c "import json,sys; g=json.load(open('$TMP/.graphify/graph.json')); print(sum(1 for l in g['links'] if l.get('_origin')=='asserted'))")"
[ "$COUNT" = "1" ] || { echo "FAIL: expected 1 asserted link, got $COUNT"; exit 1; }

python3 "$ROOT/scripts/check_integrity.py" --root "$TMP"

python3 "$ROOT/scripts/assertions.py" prune --root "$TMP" "$AID"
python3 "$ROOT/scripts/assertions.py" replay --root "$TMP"
COUNT2="$(python3 -c "import json,sys; g=json.load(open('$TMP/.graphify/graph.json')); print(sum(1 for l in g['links'] if l.get('_origin')=='asserted'))")"
[ "$COUNT2" = "0" ] || { echo "FAIL: expected 0 asserted links after prune, got $COUNT2"; exit 1; }

# Success-check invariant: asserted links == active overlay lines.
ACTIVE="$(python3 -c "import sys; sys.path.insert(0,'$ROOT/scripts'); import assertions; print(len(assertions.load_overlay('$TMP')))")"
[ "$ACTIVE" = "0" ] || { echo "FAIL: expected 0 active assertions, got $ACTIVE"; exit 1; }

echo "PASS assertions smoke"
```

- [ ] **Step 2: Run the smoke**

Run: `bash tests/test_assertions_smoke.sh`
Expected: ends with `PASS assertions smoke`.

- [ ] **Step 3: Run the whole suite**

Run: `python3 -m unittest discover -s tests -v` and each bash test (`for t in tests/test_*.sh; do echo "== $t"; bash "$t"; done`).
Expected: all green. The default `.research/state.json` may appear at repo root as a side effect — discard it (`git checkout -- .research/state.json 2>/dev/null || rm -f .research/state.json`) if it is untracked/modified noise, and do not stage it.

- [ ] **Step 4: Commit**

```bash
git add tests/test_assertions_smoke.sh
git commit -m "test: end-to-end assertion overlay author/replay/prune smoke"
```

---

## Self-Review

**Spec coverage (design §6④ + §8/§10, handoff #4):**
- Store `.research/graph-assertions.jsonl`, append-only, committed → Task 1 (`OVERLAY_REL`, `_append_line`; committed because `.research/` is tracked).
- Assertion schema (`id, from, to, relation, rationale, cites, author, confidence, created_at`) → Task 1 `add_assertion` record.
- Durable id `gen_id("a", from|to|relation)` → Task 1, asserted by `test_add_appends_active_assertion_with_durable_id`.
- Validate `cites` resolve to corpus ids → Task 1 (`add_assertion`) + Task 3 (integrity, second line of defense).
- `state.json assertions.count` kept in sync → Task 1 `sync_count` (recomputed, not incremented — no drift).
- Replay merges overlay into `graph.json` tagged distinctly → Task 2 (`_origin:"asserted"`, chosen over the spec's literal `source:"asserted"` because `source` is the node_link endpoint key — documented in Global Constraints).
- Replay idempotent; pruning + re-replay removes the edge → Task 2 (`test_replay_is_idempotent`, `test_pruned_assertion_disappears_on_replay`).
- Wire replay between `graphify --update` and `graph_events` append → Task 5 (loop.md) + Task 4 (graph_events must read `links` for the wiring to be meaningful).
- Author = process flow (re-enable deferred step) → Task 5 (process.md).
- Gating: auto-applied + always recorded (not human-gated) → Task 1/2 design; process.md step says "no human gate".
- Integrity: assertions reference existing node ids + cites resolve → Task 3.
- Success check: replay idempotent, asserted count == non-pruned overlay lines → Task 2 tests + Task 6 smoke invariant.

**Placeholder scan:** No TBD/TODO. Every code step shows complete code. No suppression comments anywhere (the no-flake8 import style is matched directly — Task 1 note).

**Type consistency:** `frm` param (CLI `--from`) consistent across `add_assertion` and `_main`. `load_overlay`/`replay`/`prune_assertion`/`sync_count`/`add_assertion` signatures match between definition (Tasks 1–2) and call sites (Tasks 3, 6). `_origin == "asserted"` tag string identical in `_asserted_link` (Task 2), `replay` strip filter (Task 2), and integrity (Task 3 reads it implicitly via overlay, not graph). `GRAPH_REL`/`OVERLAY_REL` referenced consistently.

**Open verification for plan cross-check:** confirm `tests/test_check_integrity.py` and `tests/test_graph_events.py` import names (`check_integrity`, `graph_events`, `state as state_mod`) match the additions in Tasks 3–4; the implementer must read those files first (Steps direct them to).
