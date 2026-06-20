# Process Flow (Sub-Project #3) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the process flow — the `/goal` that turns the ingested corpus into drafted findings (cited to `corpus` ids), emits new gaps to close the autonomous loop, and surfaces drafts to a human promote/reject gate.

**Architecture:** Deterministic, unit-tested Python scaffolding (draft ledger ops in `state.py`, a citation validator, a phase-gated candidate picker, a promote/reject gate) wraps one agent-driven prose prompt (`.claude/process.md`). The agent reads the corpus + graph, drafts a finding citing `[corpus_id]` markers, runs the citation validator as its success check, records the draft, and emits gaps. Drafts live in `docs/findings/_drafts/` with `status:"draft"` until a human promotes them to `docs/findings/` + `SYNTHESIS.md` or rejects them.

**Tech Stack:** Python 3 stdlib only (`json`, `re`, `argparse`, `pathlib`, `shutil`, `unittest`); bash smoke tests. No pip, no pytest, no new dependencies.

## Global Constraints

- **Python 3 stdlib only** — no pip, no pytest. Unit tests are `unittest`; integration tests are bash `test_*.sh`. `tests/__init__.py` exists; tests insert `scripts/` on `sys.path`.
- **No lint/type suppression comments** anywhere (`# noqa`, `# type: ignore`, etc.) — fix the code.
- **Commits:** Conventional Commits, selectively staged (never `git add .`/`-A`), **no co-author trailers, no "Generated with" lines**.
- **Durable ids:** drafts seed on `gen_id("d", topic + "|" + title)` — never on the on-disk path.
- **Drafts cite `corpus` ids** with inline `[c<8 hex>]` markers (e.g. `[c1a2b3c4d]`), distinct from the URL-link citations existing findings use. This is the machine-checkable contract.
- **Process is phase-gated:** in the `gather` phase `subagent_count(state,"process") == 0`, so the candidate picker returns nothing and the flow idles. It only runs in `deepen`/`synthesize`.
- **Branch:** build on `phase2-process-flow` off `phase1-research-spike`; fast-forward merge back and delete the branch at the end (the repo's branch-per-sub-project pattern).

---

## File Structure

- `scripts/state.py` (modify) — add draft ledger ops (`add_draft`, `list_drafts`, `get_draft`, `set_draft_status`, `promote_draft`, `reject_draft`), the candidate picker (`unprocessed_sources`, `process_candidates`, `_cited_ids`), a `set_phase` op, and matching CLI subcommands. Owns all `state.json` mutation.
- `scripts/cite_check.py` (create) — the success check: parse a draft's `[c…]` citations, verify each resolves to a real `corpus` id and that ≥1 citation exists. CLI exits `1` on any problem, `0` when clean (mirrors `junk.py`'s exit-code contract).
- `scripts/promote.py` (create) — the human review gate: `promote` moves a draft file `docs/findings/_drafts/ → docs/findings/`, flips status, appends a `SYNTHESIS.md` line; `reject` flips status, leaving the file as a record; `queue` lists review-ready drafts. Owns the filesystem side-effects; delegates `state.json` mutation to `state.py`.
- `scripts/check_integrity.py` (modify) — extend the lint to assert every non-promoted draft's file exists and every draft cite resolves to a `corpus` id.
- `.claude/process.md` (create) — the `/goal` prompt the agent follows each process cycle (mirrors `.claude/loop.md`'s numbered-step style).
- `tests/test_process_state.py` (create) — unit tests for the draft + candidate + phase ops.
- `tests/test_cite_check.py` (create) — unit tests for the citation validator.
- `tests/test_promote.py` (create) — unit tests for the promote/reject gate.
- `tests/test_process_flow.sh` (create) — end-to-end smoke: seed a tiny corpus + a passing draft, run cite_check, add-draft, promote, assert the file moved and `SYNTHESIS.md` grew.
- `tests/test_check_integrity.py` (modify) — add draft-cite + draft-file integrity cases.

---

## Task 1: Draft ledger ops in `state.py`

**Files:**
- Modify: `scripts/state.py` (add functions after `set_gap_status`, before `_main`)
- Test: `tests/test_process_state.py` (create)

**Interfaces:**
- Consumes: `gen_id`, `_now`, `load_default` (existing in `state.py`).
- Produces:
  - `add_draft(state, *, topic, title, path, cites, status="draft", now=None, id=None) -> dict` — appends `{id, topic, title, path, status, cites, created_at, promoted_path:None}`; idempotent on id; `id` defaults to `gen_id("d", topic + "|" + title)`.
  - `list_drafts(state, status=None, topic=None) -> list[dict]`
  - `get_draft(state, draft_id) -> dict | None`
  - `set_draft_status(state, draft_id, status) -> dict | None`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_process_state.py`:

```python
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import state


class TestDraftOps(unittest.TestCase):
    def test_add_draft_assigns_deterministic_id(self):
        st = state.load_default()
        d = state.add_draft(
            st, topic="05-ai", title="Deep research systems",
            path="docs/findings/_drafts/dXXX-deep.md", cites=["c001", "c002"],
            now="2026-06-20T00:00:00+00:00",
        )
        self.assertEqual(d["id"], state.gen_id("d", "05-ai|Deep research systems"))
        self.assertTrue(d["id"].startswith("d"))
        self.assertEqual(d["status"], "draft")
        self.assertEqual(d["cites"], ["c001", "c002"])
        self.assertIsNone(d["promoted_path"])
        self.assertEqual(st["drafts"], [d])

    def test_add_draft_is_idempotent_on_id(self):
        st = state.load_default()
        a = state.add_draft(st, topic="t", title="x", path="p.md", cites=[])
        b = state.add_draft(st, topic="t", title="x", path="p2.md", cites=["c9"])
        self.assertEqual(a["id"], b["id"])
        self.assertEqual(len(st["drafts"]), 1)
        self.assertEqual(st["drafts"][0]["path"], "p.md")  # first write wins

    def test_list_drafts_filters_by_status_and_topic(self):
        st = state.load_default()
        state.add_draft(st, topic="a", title="1", path="1.md", cites=[], status="draft")
        state.add_draft(st, topic="a", title="2", path="2.md", cites=[], status="promoted")
        state.add_draft(st, topic="b", title="3", path="3.md", cites=[], status="draft")
        self.assertEqual(len(state.list_drafts(st)), 3)
        self.assertEqual(len(state.list_drafts(st, status="draft")), 2)
        self.assertEqual(len(state.list_drafts(st, topic="a")), 2)
        self.assertEqual(len(state.list_drafts(st, status="draft", topic="a")), 1)

    def test_get_and_set_draft_status(self):
        st = state.load_default()
        d = state.add_draft(st, topic="t", title="x", path="p.md", cites=[])
        self.assertEqual(state.get_draft(st, d["id"])["id"], d["id"])
        self.assertIsNone(state.get_draft(st, "dffffffff"))
        state.set_draft_status(st, d["id"], "in_review")
        self.assertEqual(state.get_draft(st, d["id"])["status"], "in_review")
        self.assertIsNone(state.set_draft_status(st, "dffffffff", "x"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_process_state -v`
Expected: FAIL with `AttributeError: module 'state' has no attribute 'add_draft'`

- [ ] **Step 3: Implement the draft ops**

In `scripts/state.py`, insert immediately after `set_gap_status` (before `def _main`):

```python
def add_draft(state, *, topic, title, path, cites, status="draft", now=None, id=None):
    did = id or gen_id("d", topic + "|" + title)
    for d in state["drafts"]:
        if d["id"] == did:
            return d
    draft = {
        "id": did, "topic": topic, "title": title, "path": path,
        "status": status, "cites": list(cites),
        "created_at": now or _now(), "promoted_path": None,
    }
    state["drafts"].append(draft)
    return draft


def list_drafts(state, status=None, topic=None):
    return [
        d for d in state["drafts"]
        if (status is None or d["status"] == status)
        and (topic is None or d["topic"] == topic)
    ]


def get_draft(state, draft_id):
    for d in state["drafts"]:
        if d["id"] == draft_id:
            return d
    return None


def set_draft_status(state, draft_id, status):
    d = get_draft(state, draft_id)
    if d is not None:
        d["status"] = status
    return d
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_process_state -v`
Expected: PASS (4 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py tests/test_process_state.py
git commit -m "feat: add draft ledger ops to state ledger"
```

---

## Task 2: Candidate picker + `set_phase` in `state.py`

**Files:**
- Modify: `scripts/state.py` (add functions after `set_draft_status`)
- Test: `tests/test_process_state.py` (extend)

**Interfaces:**
- Consumes: `subagent_count` (existing), the draft ops from Task 1.
- Produces:
  - `_cited_ids(state, exclude_rejected=True) -> set[str]` — corpus ids cited by any draft (rejected drafts excluded so their sources become processable again).
  - `unprocessed_sources(state, topic) -> list[dict]` — corpus entries for `topic` not cited by any non-rejected draft.
  - `process_candidates(state, min_sources=3) -> list[tuple[str,int]]` — `(topic, unprocessed_count)` for topics with `>= min_sources` unprocessed sources, richest first; **empty when `subagent_count(state,"process") <= 0`** (phase gate).
  - `set_phase(state, phase) -> str` — sets `budget.phase`; raises `ValueError` for an unknown phase.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_process_state.py` (before the `if __name__` block):

```python
class TestCandidates(unittest.TestCase):
    def _corpus(self, st, topic, n):
        for i in range(n):
            state.add_corpus_entry(
                st, title=f"{topic}-{i}", source=f"src://{topic}/{i}", topic=topic,
                native_path=f"ingest/{topic}-{i}.md",
                extracted_path=f"docs/{topic}/sources/{topic}-{i}.md",
                now="2026-06-20T00:00:00+00:00",
            )

    def test_cited_ids_excludes_rejected(self):
        st = state.load_default()
        state.add_draft(st, topic="t", title="ok", path="a.md", cites=["c1"], status="draft")
        state.add_draft(st, topic="t", title="no", path="b.md", cites=["c2"], status="rejected")
        self.assertEqual(state._cited_ids(st), {"c1"})
        self.assertEqual(state._cited_ids(st, exclude_rejected=False), {"c1", "c2"})

    def test_unprocessed_sources_skips_cited(self):
        st = state.load_default()
        self._corpus(st, "05-ai", 3)
        cited_id = st["corpus"][0]["id"]
        state.add_draft(st, topic="05-ai", title="d", path="d.md", cites=[cited_id])
        un = state.unprocessed_sources(st, "05-ai")
        self.assertEqual(len(un), 2)
        self.assertNotIn(cited_id, [e["id"] for e in un])

    def test_process_candidates_empty_in_gather_phase(self):
        st = state.load_default()  # phase defaults to "gather" -> process weight 0.0
        self._corpus(st, "05-ai", 5)
        self.assertEqual(state.process_candidates(st), [])

    def test_process_candidates_ranks_richest_first_when_phase_open(self):
        st = state.load_default()
        state.set_phase(st, "synthesize")
        self._corpus(st, "05-ai", 5)
        self._corpus(st, "06-rag", 3)
        self._corpus(st, "07-orch", 2)  # below min_sources
        self.assertEqual(state.process_candidates(st), [("05-ai", 5), ("06-rag", 3)])

    def test_set_phase_rejects_unknown(self):
        st = state.load_default()
        self.assertEqual(state.set_phase(st, "deepen"), "deepen")
        self.assertEqual(st["budget"]["phase"], "deepen")
        with self.assertRaises(ValueError):
            state.set_phase(st, "bogus")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_process_state -v`
Expected: FAIL with `AttributeError: module 'state' has no attribute 'set_phase'` (and `process_candidates`)

- [ ] **Step 3: Implement the candidate picker + `set_phase`**

In `scripts/state.py`, insert after `set_draft_status`:

```python
def _cited_ids(state, exclude_rejected=True):
    out = set()
    for d in state["drafts"]:
        if exclude_rejected and d["status"] == "rejected":
            continue
        out.update(d.get("cites", []))
    return out


def unprocessed_sources(state, topic):
    cited = _cited_ids(state)
    return [e for e in state["corpus"]
            if e["topic"] == topic and e["id"] not in cited]


def process_candidates(state, min_sources=3):
    if subagent_count(state, "process") <= 0:
        return []
    cited = _cited_ids(state)
    counts = {}
    for e in state["corpus"]:
        if e["id"] not in cited:
            counts[e["topic"]] = counts.get(e["topic"], 0) + 1
    cands = [(t, n) for t, n in counts.items() if n >= min_sources]
    cands.sort(key=lambda tn: (-tn[1], tn[0]))
    return cands


def set_phase(state, phase):
    if phase not in state["budget"]["weights"]:
        raise ValueError(f"unknown phase: {phase}")
    state["budget"]["phase"] = phase
    return phase
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_process_state -v`
Expected: PASS (9 tests total)

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py tests/test_process_state.py
git commit -m "feat: add process candidate picker + set-phase to state ledger"
```

---

## Task 3: Draft + phase CLI subcommands in `state.py`

**Files:**
- Modify: `scripts/state.py` (`_main`: add parsers + dispatch branches)
- Test: `tests/test_process_state.py` (extend with a CLI subprocess test)

**Interfaces:**
- Consumes: all Task 1/2 functions, `load`, `save`.
- Produces CLI subcommands (all accept `--root`, default `"."`):
  - `add-draft --topic T --title S --path P [--cites c1,c2] [--status draft] [--id D]` → prints draft id.
  - `list-drafts [--status S] [--topic T]` → tab-separated `id\tstatus\ttopic\ttitle` per line.
  - `set-draft --id D --status S` → prints `draft updated`.
  - `candidates [--min-sources N]` → tab-separated `topic\tcount` per line (empty in `gather`).
  - `set-phase --phase P` → prints the phase.

- [ ] **Step 1: Write the failing test**

Append to `tests/test_process_state.py` (before `if __name__`):

```python
import subprocess, tempfile

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"


class TestDraftCLI(unittest.TestCase):
    def _run(self, root, *args):
        return subprocess.run(
            ["python3", str(SCRIPTS / "state.py"), *args, "--root", root],
            capture_output=True, text=True,
        )

    def test_add_list_set_draft_via_cli(self):
        with tempfile.TemporaryDirectory() as d:
            self._run(d, "set-phase", "--phase", "synthesize")
            r = self._run(d, "add-draft", "--topic", "05-ai", "--title", "X",
                          "--path", "docs/findings/_drafts/dX.md", "--cites", "c1,c2")
            self.assertEqual(r.returncode, 0)
            did = r.stdout.strip()
            self.assertTrue(did.startswith("d"))
            lst = self._run(d, "list-drafts", "--status", "draft")
            self.assertIn(did, lst.stdout)
            self.assertIn("05-ai", lst.stdout)
            self._run(d, "set-draft", "--id", did, "--status", "in_review")
            self.assertEqual(self._run(d, "list-drafts", "--status", "draft").stdout.strip(), "")
            self.assertIn(did, self._run(d, "list-drafts", "--status", "in_review").stdout)

    def test_set_phase_then_candidates_via_cli(self):
        with tempfile.TemporaryDirectory() as d:
            for i in range(3):
                self._run(d, "add-corpus", "--title", f"t{i}", "--source", f"s{i}",
                          "--topic", "05-ai", "--native", f"n{i}.md", "--extracted", f"e{i}.md")
            self.assertEqual(self._run(d, "candidates").stdout.strip(), "")  # gather phase
            self._run(d, "set-phase", "--phase", "synthesize")
            self.assertIn("05-ai\t3", self._run(d, "candidates").stdout)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_process_state.TestDraftCLI -v`
Expected: FAIL (returncode 2 / `invalid choice: 'add-draft'`)

- [ ] **Step 3: Add the parsers and dispatch branches**

In `scripts/state.py` `_main`, add these parsers after the `stg` (set-gap) parser block, before `args = ap.parse_args(argv)`:

```python
    ad = sub.add_parser("add-draft"); ad.add_argument("--root", default=".")
    ad.add_argument("--topic", required=True); ad.add_argument("--title", required=True)
    ad.add_argument("--path", required=True); ad.add_argument("--cites", default="")
    ad.add_argument("--status", default="draft"); ad.add_argument("--id", default=None)
    ld = sub.add_parser("list-drafts"); ld.add_argument("--root", default=".")
    ld.add_argument("--status", default=None); ld.add_argument("--topic", default=None)
    sd = sub.add_parser("set-draft"); sd.add_argument("--root", default=".")
    sd.add_argument("--id", required=True); sd.add_argument("--status", required=True)
    cd = sub.add_parser("candidates"); cd.add_argument("--root", default=".")
    cd.add_argument("--min-sources", type=int, default=3)
    sph = sub.add_parser("set-phase"); sph.add_argument("--root", default=".")
    sph.add_argument("--phase", required=True)
```

Then add these dispatch branches before the final `return 1`:

```python
    if args.cmd == "add-draft":
        st = load(args.root)
        cites = [c for c in args.cites.split(",") if c]
        d = add_draft(st, topic=args.topic, title=args.title, path=args.path,
                      cites=cites, status=args.status, id=args.id)
        save(st, args.root); print(d["id"]); return 0
    if args.cmd == "list-drafts":
        for d in list_drafts(load(args.root), status=args.status, topic=args.topic):
            print(f"{d['id']}\t{d['status']}\t{d['topic']}\t{d['title']}")
        return 0
    if args.cmd == "set-draft":
        st = load(args.root)
        if set_draft_status(st, args.id, args.status) is None:
            print(f"unknown draft: {args.id}", file=sys.stderr); return 1
        save(st, args.root); print("draft updated"); return 0
    if args.cmd == "candidates":
        for topic, n in process_candidates(load(args.root), min_sources=args.min_sources):
            print(f"{topic}\t{n}")
        return 0
    if args.cmd == "set-phase":
        st = load(args.root)
        try:
            set_phase(st, args.phase)
        except ValueError as e:
            print(str(e), file=sys.stderr); return 1
        save(st, args.root); print(args.phase); return 0
```

- [ ] **Step 4: Run the full state test suite to verify it passes**

Run: `python3 -m unittest tests.test_process_state -v`
Expected: PASS (11 tests total)

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py tests/test_process_state.py
git commit -m "feat: add draft + phase CLI to state ledger"
```

---

## Task 4: Citation validator `cite_check.py`

**Files:**
- Create: `scripts/cite_check.py`
- Test: `tests/test_cite_check.py` (create)

**Interfaces:**
- Consumes: `state.load`, the `corpus` id set.
- Produces:
  - `find_cites(text) -> list[str]` — all `[c<8 hex>]` markers (without brackets).
  - `check_draft(text, corpus_ids) -> list[str]` — problem strings; non-empty if zero citations or any dangling cite (each dangling reported once).
  - CLI `cite_check.py <draft> [--root .]` → prints `PROBLEM: …` lines and exits `1` on any problem, else prints `citations OK` and exits `0` (mirrors `junk.py`).

- [ ] **Step 1: Write the failing tests**

Create `tests/test_cite_check.py`:

```python
import unittest, subprocess, tempfile
from pathlib import Path
import sys
SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import cite_check
import state


class TestCiteCheck(unittest.TestCase):
    def test_find_cites_extracts_markers(self):
        text = "claim one [c1a2b3c4d]. claim two [cdeadbeef]. not a cite [c12]."
        self.assertEqual(cite_check.find_cites(text), ["c1a2b3c4d", "cdeadbeef"])

    def test_check_draft_flags_missing_citations(self):
        self.assertEqual(cite_check.check_draft("no cites here", {"c1a2b3c4d"}),
                         ["no [corpus_id] citations found"])

    def test_check_draft_flags_dangling_once(self):
        text = "a [c1a2b3c4d] b [cffffffff] c [cffffffff]"
        probs = cite_check.check_draft(text, {"c1a2b3c4d"})
        self.assertEqual(probs, ["dangling citation: cffffffff"])

    def test_check_draft_clean(self):
        self.assertEqual(cite_check.check_draft("a [c1a2b3c4d] b [cdeadbeef]",
                                                {"c1a2b3c4d", "cdeadbeef"}), [])

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as d:
            st = state.load(d)
            state.add_corpus_entry(st, title="T", source="s", topic="t",
                                   native_path="n.md", extracted_path="e.md", id="c1a2b3c4d")
            state.save(st, d)
            good = Path(d) / "good.md"; good.write_text("claim [c1a2b3c4d]", encoding="utf-8")
            bad = Path(d) / "bad.md"; bad.write_text("claim [cffffffff]", encoding="utf-8")
            r_good = subprocess.run(["python3", str(SCRIPTS / "cite_check.py"),
                                     str(good), "--root", d], capture_output=True, text=True)
            r_bad = subprocess.run(["python3", str(SCRIPTS / "cite_check.py"),
                                    str(bad), "--root", d], capture_output=True, text=True)
            self.assertEqual(r_good.returncode, 0)
            self.assertIn("citations OK", r_good.stdout)
            self.assertEqual(r_bad.returncode, 1)
            self.assertIn("dangling", r_bad.stdout)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_cite_check -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'cite_check'`

- [ ] **Step 3: Implement `cite_check.py`**

Create `scripts/cite_check.py`:

```python
"""Validate a draft's inline [corpus_id] citations resolve. Stdlib only."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

_CITE = re.compile(r"\[(c[0-9a-f]{8})\]")


def find_cites(text):
    return _CITE.findall(text)


def check_draft(text, corpus_ids):
    cites = find_cites(text)
    problems = []
    if not cites:
        problems.append("no [corpus_id] citations found")
    for cid in dict.fromkeys(cites):
        if cid not in corpus_ids:
            problems.append(f"dangling citation: {cid}")
    return problems


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    st = state_mod.load(args.root)
    ids = {e["id"] for e in st["corpus"]}
    text = Path(args.draft).read_text(encoding="utf-8", errors="replace")
    probs = check_draft(text, ids)
    for p in probs:
        print("PROBLEM:", p)
    if probs:
        return 1
    print("citations OK")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_cite_check -v`
Expected: PASS (5 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/cite_check.py tests/test_cite_check.py
git commit -m "feat: add citation validator for process-flow drafts"
```

---

## Task 5: Promote/reject gate `promote.py` + `state.py` ops

**Files:**
- Modify: `scripts/state.py` (add `promote_draft`, `reject_draft` after `set_draft_status`)
- Create: `scripts/promote.py`
- Test: `tests/test_promote.py` (create)

**Interfaces:**
- Consumes: `state.load`, `state.save`, `state.get_draft`.
- Produces in `state.py`:
  - `promote_draft(state, draft_id, dest_path, now=None) -> dict | None` — sets `status="promoted"`, `promoted_path=dest_path`, `promoted_at`.
  - `reject_draft(state, draft_id, reason=None, now=None) -> dict | None` — sets `status="rejected"`, optional `reject_reason`.
- Produces in `promote.py` (CLI, all accept `--root`, default `"."`):
  - `promote <draft_id>` — moves `docs/findings/_drafts/<file> → docs/findings/<file>`, calls `promote_draft`, appends a link line to `docs/findings/SYNTHESIS.md` (created with a header if absent). Prints `promoted <id> -> <dest>`; exits `1` on unknown id or missing file.
  - `reject <draft_id> [--reason R]` — calls `reject_draft`, leaves the draft file as a record. Prints `rejected <id>`.
  - `queue` — lists review-ready drafts (`status="draft"`): `id\ttopic\ttitle`.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_promote.py`:

```python
import unittest, subprocess, tempfile
from pathlib import Path
import sys
SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import state


def _seed_draft(root):
    st = state.load(root)
    drafts_dir = Path(root) / "docs/findings/_drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)
    did = state.gen_id("d", "05-ai|Deep research")
    fname = f"{did}-deep-research.md"
    (drafts_dir / fname).write_text("# Deep research\n\nclaim [c1a2b3c4d]\n", encoding="utf-8")
    state.add_draft(st, topic="05-ai", title="Deep research",
                    path=f"docs/findings/_drafts/{fname}", cites=["c1a2b3c4d"], id=did)
    state.save(st, root)
    return did, fname


class TestPromoteOps(unittest.TestCase):
    def test_promote_draft_sets_fields(self):
        st = state.load_default()
        d = state.add_draft(st, topic="t", title="x", path="p.md", cites=["c1"])
        out = state.promote_draft(st, d["id"], "docs/findings/p.md",
                                  now="2026-06-20T00:00:00+00:00")
        self.assertEqual(out["status"], "promoted")
        self.assertEqual(out["promoted_path"], "docs/findings/p.md")
        self.assertEqual(out["promoted_at"], "2026-06-20T00:00:00+00:00")
        self.assertIsNone(state.promote_draft(st, "dffffffff", "x"))

    def test_reject_draft_sets_fields(self):
        st = state.load_default()
        d = state.add_draft(st, topic="t", title="x", path="p.md", cites=[])
        out = state.reject_draft(st, d["id"], reason="thin")
        self.assertEqual(out["status"], "rejected")
        self.assertEqual(out["reject_reason"], "thin")


class TestPromoteCLI(unittest.TestCase):
    def _run(self, root, *args):
        return subprocess.run(["python3", str(SCRIPTS / "promote.py"), *args, "--root", root],
                              capture_output=True, text=True)

    def test_promote_moves_file_and_appends_synthesis(self):
        with tempfile.TemporaryDirectory() as d:
            did, fname = _seed_draft(d)
            r = self._run(d, "promote", did)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertFalse((Path(d) / "docs/findings/_drafts" / fname).exists())
            self.assertTrue((Path(d) / "docs/findings" / fname).exists())
            syn = (Path(d) / "docs/findings/SYNTHESIS.md").read_text(encoding="utf-8")
            self.assertIn(fname, syn)
            self.assertIn("Deep research", syn)
            st = state.load(d)
            self.assertEqual(state.get_draft(st, did)["status"], "promoted")

    def test_promote_unknown_id_fails(self):
        with tempfile.TemporaryDirectory() as d:
            r = self._run(d, "promote", "dffffffff")
            self.assertEqual(r.returncode, 1)

    def test_reject_leaves_file_and_flips_status(self):
        with tempfile.TemporaryDirectory() as d:
            did, fname = _seed_draft(d)
            r = self._run(d, "reject", did, "--reason", "thin")
            self.assertEqual(r.returncode, 0)
            self.assertTrue((Path(d) / "docs/findings/_drafts" / fname).exists())
            st = state.load(d)
            self.assertEqual(state.get_draft(st, did)["status"], "rejected")

    def test_queue_lists_review_ready(self):
        with tempfile.TemporaryDirectory() as d:
            did, _ = _seed_draft(d)
            self.assertIn(did, self._run(d, "queue").stdout)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_promote -v`
Expected: FAIL — `AttributeError: module 'state' has no attribute 'promote_draft'` and `No module named 'promote'`

- [ ] **Step 3a: Add `promote_draft`/`reject_draft` to `state.py`**

In `scripts/state.py`, insert after `set_draft_status`:

```python
def promote_draft(state, draft_id, dest_path, now=None):
    d = get_draft(state, draft_id)
    if d is None:
        return None
    d["status"] = "promoted"
    d["promoted_path"] = dest_path
    d["promoted_at"] = now or _now()
    return d


def reject_draft(state, draft_id, reason=None, now=None):
    d = get_draft(state, draft_id)
    if d is None:
        return None
    d["status"] = "rejected"
    if reason:
        d["reject_reason"] = reason
    return d
```

- [ ] **Step 3b: Implement `promote.py`**

Create `scripts/promote.py`:

```python
"""Human review gate: promote or reject process-flow drafts. Stdlib only."""
import shutil
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

FINDINGS_DIR = "docs/findings"
SYNTHESIS = "docs/findings/SYNTHESIS.md"


def promote(root, draft_id):
    st = state_mod.load(root)
    d = state_mod.get_draft(st, draft_id)
    if d is None:
        return 1, f"unknown draft: {draft_id}"
    src = Path(root) / d["path"]
    if not src.exists():
        return 1, f"draft file missing: {d['path']}"
    dest_rel = f"{FINDINGS_DIR}/{src.name}"
    dest = Path(root) / dest_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dest))
    state_mod.promote_draft(st, draft_id, dest_rel)
    state_mod.save(st, root)
    syn = Path(root) / SYNTHESIS
    if not syn.exists():
        syn.write_text("# Synthesis — promoted findings\n\n", encoding="utf-8")
    with syn.open("a", encoding="utf-8") as f:
        f.write(f"- [{d['title']}]({src.name}) — {d['topic']}\n")
    return 0, f"promoted {draft_id} -> {dest_rel}"


def reject(root, draft_id, reason=None):
    st = state_mod.load(root)
    if state_mod.reject_draft(st, draft_id, reason) is None:
        return 1, f"unknown draft: {draft_id}"
    state_mod.save(st, root)
    return 0, f"rejected {draft_id}"


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("promote"); p.add_argument("draft_id"); p.add_argument("--root", default=".")
    r = sub.add_parser("reject"); r.add_argument("draft_id"); r.add_argument("--root", default=".")
    r.add_argument("--reason", default=None)
    q = sub.add_parser("queue"); q.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    if args.cmd == "promote":
        code, msg = promote(args.root, args.draft_id)
    elif args.cmd == "reject":
        code, msg = reject(args.root, args.draft_id, args.reason)
    else:  # queue
        for d in state_mod.list_drafts(state_mod.load(args.root), status="draft"):
            print(f"{d['id']}\t{d['topic']}\t{d['title']}")
        return 0
    if code == 0:
        print(msg)
    else:
        print(msg, file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_promote -v`
Expected: PASS (6 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py scripts/promote.py tests/test_promote.py
git commit -m "feat: add promote/reject review gate for drafts"
```

---

## Task 6: Extend `check_integrity.py` for drafts

**Files:**
- Modify: `scripts/check_integrity.py` (extend `check`)
- Test: `tests/test_check_integrity.py` (add cases)

**Interfaces:**
- Consumes: existing `check(root)`.
- Produces: `check` additionally reports `draft <id> missing file: <path>` for any non-promoted draft whose file is absent, and `draft <id> dangling cite: <cid>` for any cite not in the corpus.

- [ ] **Step 1: Write the failing tests**

`tests/test_check_integrity.py` already imports `check_integrity as ci` and seeds state
inline via the `_write_state(root, corpus)` helper. Match that style exactly. First, add
a drafts-aware seeding helper next to `_write_state`:

```python
def _write_state_drafts(root, corpus, drafts):
    p = Path(root) / ".research"; p.mkdir(parents=True, exist_ok=True)
    base = {"budget": {}, "gaps": [], "inbox": [], "corpus": corpus,
            "graph": {}, "assertions": {}, "drafts": drafts}
    (p / "state.json").write_text(json.dumps(base), encoding="utf-8")
```

Then add these methods to the existing `TestIntegrity` class:

```python
    def test_flags_dangling_draft_cite(self):
        with tempfile.TemporaryDirectory() as t:
            drafts = Path(t) / "docs/findings/_drafts"; drafts.mkdir(parents=True)
            (drafts / "dX.md").write_text("x [cffffffff]", encoding="utf-8")
            _write_state_drafts(t, [], [{"id": "dX", "status": "draft",
                "path": "docs/findings/_drafts/dX.md", "cites": ["cffffffff"]}])
            probs = ci.check(t)
            self.assertTrue(any("dangling cite: cffffffff" in p for p in probs))

    def test_flags_missing_draft_file(self):
        with tempfile.TemporaryDirectory() as t:
            _write_state_drafts(t, [], [{"id": "dG", "status": "draft",
                "path": "docs/findings/_drafts/gone.md", "cites": []}])
            probs = ci.check(t)
            self.assertTrue(any("dG missing file" in p for p in probs))

    def test_promoted_draft_skips_file_check(self):
        with tempfile.TemporaryDirectory() as t:
            _write_state_drafts(t, [], [{"id": "dP", "status": "promoted",
                "path": "docs/findings/_drafts/moved.md", "cites": []}])
            self.assertEqual(ci.check(t), [])
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_check_integrity -v`
Expected: FAIL — the new assertions find no matching problem string

- [ ] **Step 3: Extend `check`**

In `scripts/check_integrity.py`, inside `check`, after the corpus loop and before `return problems`:

```python
    corpus_ids = {e.get("id") for e in st.get("corpus", [])}
    for dft in st.get("drafts", []):
        did = dft.get("id")
        if dft.get("status") != "promoted":
            dp = dft.get("path", "")
            if not (Path(root) / dp).exists():
                problems.append(f"draft {did} missing file: {dp}")
        for cid in dft.get("cites", []):
            if cid not in corpus_ids:
                problems.append(f"draft {did} dangling cite: {cid}")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_check_integrity -v`
Expected: PASS (existing + 2 new)

- [ ] **Step 5: Commit**

```bash
git add scripts/check_integrity.py tests/test_check_integrity.py
git commit -m "feat: extend integrity check to draft files + cites"
```

---

## Task 7: The `/goal` process prompt `.claude/process.md`

**Files:**
- Create: `.claude/process.md`

**Interfaces:**
- Consumes: `state.py candidates`, `state.py gen-id`, `cite_check.py`, `state.py add-draft`, `state.py add-gap`, `check_integrity.py`.
- Produces: the agent-followed cycle prompt (prose; no unit test — verified by the Task 8 smoke and human review).

- [ ] **Step 1: Write the prompt**

Create `.claude/process.md`:

```markdown
<!-- .claude/process.md -->

# Process cycle

Run one process cycle for the research engine. Do exactly this, then stop:

1. Pick a topic: run `python3 scripts/state.py candidates`. If it prints nothing,
   stop early — either the phase is `gather` (process is gated off) or no topic has
   enough un-processed sources. Otherwise take the top line's topic `T`.

2. Plan: read the un-processed sources for `T`
   (`python3 scripts/state.py list-drafts` shows what is already drafted; the source
   files live under `docs/<T>/sources/`). Read the existing finding for `T` under
   `docs/findings/` and the knowledge graph (`.graphify/graph.json`) for context.
   Frame **3–5 sub-questions across different perspectives** (method, evidence,
   contradiction, application).

3. Draft: write a finding answering those sub-questions. **Every claim must carry an
   inline `[corpus_id]` citation** to the `corpus` entry it came from (the `c…` ids
   from `state.json`), e.g. `… pre-registration reduces bias [c1a2b3c4d].` Compute the
   draft id and filename:
   ```
   ID=$(python3 scripts/state.py gen-id d "T|<your title>")
   ```
   Write the draft to `docs/findings/_drafts/$ID-<slug>.md` with a `status: draft`
   line in its header.

4. Success check — **two gates**, do not skip either:
   - **(a) Citation resolution (deterministic):** run
     `python3 scripts/cite_check.py docs/findings/_drafts/$ID-<slug>.md`.
     - Exit 0 → continue. Exit 1 → the draft has missing or dangling citations. Fix the
       draft (cite real corpus ids, or remove the unsupported claim) and re-run until it
       passes.
   - **(b) Faithfulness self-check (agent judgment):** re-read each claim **against the
     source it cites** and confirm the source actually supports the claim — not merely
     that the cited id exists. Rewrite or drop any claim the source does not bear out.
     This gate is intentionally agent-side: faithfulness is not deterministically
     checkable, so `cite_check.py` does not attempt it.

   Do **not** record a draft until **both** gates pass.

5. Record the draft:
   ```
   python3 scripts/state.py add-draft --id "$ID" --topic "T" --title "<your title>" \
     --path "docs/findings/_drafts/$ID-<slug>.md" --cites "c…,c…"
   ```
   (`--cites` is the comma-separated list of every corpus id you cited.)

6. Emit gaps (closes the loop to search): for each open question the corpus could not
   answer, run
   `python3 scripts/state.py add-gap --topic "T" --desc "<the missing question>" --origin process`.

7. Run `python3 scripts/check_integrity.py` — if it reports problems, stop and surface
   them; do not claim the cycle succeeded.

The draft now waits in the review queue (`python3 scripts/promote.py queue`). A human
promotes it (`promote.py promote <id>`) into `docs/findings/` + `SYNTHESIS.md`, or
rejects it (`promote.py reject <id>`). Graph assertions (§6④) are sub-project #4 — do
not author them here.
```

- [ ] **Step 2: Verify the referenced commands exist**

Run:
```bash
python3 scripts/state.py candidates --root . >/dev/null && \
python3 scripts/state.py gen-id d "x|y" >/dev/null && \
python3 scripts/cite_check.py --help >/dev/null && \
python3 scripts/promote.py queue --root . >/dev/null && echo "all process commands resolve"
```
Expected: `all process commands resolve`

- [ ] **Step 3: Commit**

```bash
git add .claude/process.md
git commit -m "docs: add the process-flow /goal prompt"
```

---

## Task 8: End-to-end smoke `tests/test_process_flow.sh`

**Files:**
- Create: `tests/test_process_flow.sh`

**Interfaces:**
- Consumes: every script above, end to end, in a throwaway temp root.
- Produces: a bash smoke test asserting the full draft → check → record → promote path works and integrity stays clean.

- [ ] **Step 1: Write the smoke test**

Create `tests/test_process_flow.sh`:

```bash
#!/usr/bin/env bash
# Smoke: seed corpus -> draft cites a real id -> cite_check passes -> add-draft ->
# promote moves the file + grows SYNTHESIS -> integrity clean.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SCRIPTS="$(cd "$HERE/.." && pwd)/scripts"
ROOT="$(mktemp -d)"
trap 'rm -rf "$ROOT"' EXIT
fail() { echo "FAIL: $1"; exit 1; }

SP="python3 $SCRIPTS/state.py"

# Open the phase so process is not gated off, then seed 3 sources for one topic.
$SP set-phase --root "$ROOT" --phase synthesize >/dev/null
for i in 1 2 3; do
  $SP add-corpus --root "$ROOT" --title "src$i" --source "https://ex/$i" \
    --topic "05-ai" --native "ingest/$i.md" --extracted "docs/05-ai/sources/$i.md" >/dev/null
done

CID="$($SP gen-id c "https://ex/1")"
[ -n "$CID" ] || fail "no corpus id"

# A candidate topic should now be offered.
$SP candidates --root "$ROOT" | grep -q "05-ai" || fail "no candidate topic"

# Write a draft that cites a real corpus id.
ID="$($SP gen-id d "05-ai|AI deep research")"
DRAFTS="$ROOT/docs/findings/_drafts"; mkdir -p "$DRAFTS"
DRAFT="$DRAFTS/$ID-ai-deep-research.md"
printf '# AI deep research\n\nstatus: draft\n\nClaim grounded in a source [%s].\n' "$CID" > "$DRAFT"

# Success check must pass.
python3 "$SCRIPTS/cite_check.py" "$DRAFT" --root "$ROOT" || fail "cite_check rejected a valid draft"

# A dangling cite must be rejected (negative check).
BAD="$DRAFTS/bad.md"; printf 'x [cffffffff]\n' > "$BAD"
if python3 "$SCRIPTS/cite_check.py" "$BAD" --root "$ROOT" >/dev/null 2>&1; then
  fail "cite_check passed a dangling cite"
fi
rm -f "$BAD"

# Record the draft + emit a gap.
$SP add-draft --root "$ROOT" --id "$ID" --topic "05-ai" --title "AI deep research" \
  --path "docs/findings/_drafts/$ID-ai-deep-research.md" --cites "$CID" >/dev/null
$SP add-gap --root "$ROOT" --topic "05-ai" --desc "unanswered question" --origin process >/dev/null

# Draft shows in the review queue.
python3 "$SCRIPTS/promote.py" queue --root "$ROOT" | grep -q "$ID" || fail "draft not in review queue"

# Promote: file moves, SYNTHESIS grows, status flips.
python3 "$SCRIPTS/promote.py" promote "$ID" --root "$ROOT" >/dev/null || fail "promote failed"
[ ! -f "$DRAFT" ] || fail "draft file not moved out of _drafts"
[ -f "$ROOT/docs/findings/$ID-ai-deep-research.md" ] || fail "promoted file missing"
grep -q "AI deep research" "$ROOT/docs/findings/SYNTHESIS.md" || fail "SYNTHESIS not updated"

# Integrity stays clean (promoted draft's file moved; cite resolves).
python3 "$SCRIPTS/check_integrity.py" --root "$ROOT" || fail "integrity reported problems"

echo "PASS: process flow smoke"
```

- [ ] **Step 2: Make it executable and run it (expect PASS once Tasks 1–6 are merged)**

Run:
```bash
chmod +x tests/test_process_flow.sh
bash tests/test_process_flow.sh
```
Expected: `PASS: process flow smoke`

- [ ] **Step 3: Run the whole suite**

Run:
```bash
python3 -m unittest discover -s tests -v
for t in tests/test_*.sh; do echo "== $t =="; bash "$t" || exit 1; done
```
Expected: all unit tests pass; every bash smoke prints `PASS`.

- [ ] **Step 4: Commit**

```bash
git add tests/test_process_flow.sh
git commit -m "test: add end-to-end process-flow smoke"
```

---

## Out of scope (this sub-project)

- **Graph assertions overlay (§6④)** — that is sub-project #4. The process prompt explicitly defers it.
- **Auto-numbering promoted findings** (`NN-…`) — promote keeps the draft's `<id>-slug` filename; renaming is a human concern.
- **Orchestrator weight self-tuning / phase auto-flip** — deferred per §5; `phase` stays human-set via `set-phase`.
- **Realtime view, A→C convergence** — sub-projects #5/#6.

---

## Self-Review

**Spec coverage (§6③ + §5):**
- "Reads corpus[], .graphify/, existing findings" → Task 7 steps 1–2.
- "Pick a topic with enough un-processed sources" → Task 2 `process_candidates` (min 3) + Task 3 CLI.
- "0 subagents in gather phase" → Task 2 phase gate (`subagent_count<=0 → []`), tested.
- "Two-stage deep-research loop → draft with inline corpus-id citations" → Task 7 steps 2–3.
- "Write to docs/findings/_drafts/ with status:draft" → Task 7 step 3 + Task 1 default status.
- "Emit new gaps[] (origin process)" → Task 7 step 6, reuses existing `add-gap`.
- "Success check: every claim cites a real corpus id; faithfulness self-check" → Task 4 `cite_check.py` (dangling + zero-citation), wired in Task 7 step 4.
- "Otherwise keep draft, do not surface" → Task 7 step 4 (don't `add-draft` until the check passes).
- "Output contract: draft → review queue → human promotes/rejects" → Task 5 `promote.py` + Task 7 closing note.
- §10 integrity "every draft cite resolves to a corpus id" → Task 6.

**Placeholder scan:** none — every code step shows complete code; every command shows expected output.

**Type consistency:** `add_draft` signature, draft dict keys (`id/topic/title/path/status/cites/created_at/promoted_path`), and the `[c<8 hex>]` cite regex are used identically across Tasks 1, 3, 4, 5, 6, 8. `subagent_count`/`set_phase`/`candidates` names match between `state.py` and the prompt. `cite_check.py` and `junk.py` share the exit-1-on-problem contract.
