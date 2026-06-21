# Run-Log Observability + Validation Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make a live engine run independently verifiable — every flow step writes one structured line to a consolidated log, an automated verifier asserts per-step + cross-step invariants, and every failure is matched against a durable gotchas registry.

**Architecture:** One append-only JSONL (`.research/run.jsonl`) is the single source of truth for a run; a thin `runlog.py` helper writes records through a context sidecar (`run-context.json`) that carries `run_id`/`cycle`/`seq` across short-lived processes. `verify_run.py` reads the log back, checks invariants, recomputes the orchestrator's decisions from logged state snapshots, and matches each finding against `gotchas.py`'s committed registry. The deterministic bash flows and the three agent prompts are instrumented to emit step records.

**Tech Stack:** Python 3 standard library only; bash. Tests are `unittest`. No pip, no pytest.

## Global Constraints

- **Python 3 stdlib only** — no pip, no new dependencies. Tests are `unittest` + bash. No `# noqa` / `# type: ignore` / suppression comments anywhere — fix the code. Post-`sys.path.insert` alias imports are bare.
- **Module imports** use `import <mod> as <mod>_mod` where a name clash exists (`import state as state_mod`), matching `scripts/promote.py` / `scripts/assertions.py`.
- **Record schema** (one JSON object per `.research/run.jsonl` line): `{run_id, cycle, seq, ts, flow, step, status, data}`. `run_id` = `"r"` + 8 hex; `seq` strictly increasing within a run (`run_start` is seq 0); `cycle` monotonic non-decreasing.
- **Severity tiers:** verifier findings are `FAIL` (exit 1) or `WARN` (exit unaffected).
- **Run artifacts gitignored; gotchas registry committed.** `.research/run.jsonl` and `.research/run-context.json` are gitignored; `.research/gotchas.jsonl` is committed.
- **Gotcha id** = `"gh"` + 8 hex of `sha256(check + "|" + token)`; same signature dedupes to one entry. `root_cause`/`fix` default `"TODO"` — never auto-authored.
- **Atomic writes** use the repo pattern: write `*.tmp`, then `os.replace` (see `state.py.save`, `assertions.py`).
- **Commits:** Conventional Commits, selectively staged with exact paths — never `git add .`/`-A`. No co-author trailers, no "Generated with" lines. Do NOT stage `.research/run.jsonl`, `.research/run-context.json`, or `.research/state.json` (side-effect artifacts).

---

### Task 1: `scripts/runlog.py` — structured run log + context sidecar

**Files:**
- Create: `scripts/runlog.py`
- Test: `tests/test_runlog.py`
- Modify: `.gitignore`

**Interfaces:**
- Consumes (from `scripts/state.py`): `load(root)`.
- Produces (relied on by Task 3 + instrumentation):
  - `start(root=".") -> str` — mints `run_id`, resets context, appends a `run_start` record carrying `data.state` = a full `state.json` snapshot. Returns the id.
  - `set_cycle(n, root=".") -> int`.
  - `log_event(flow, step, status="ok", data=None, root=".") -> dict` — appends one record, `seq`-incremented.
  - `end(status="ok", root=".") -> dict` — appends `run_end`.
  - CLI: `start` · `set-cycle N` · `log --flow F --step S [--status …] [--data '<json>'] [--snapshot]` · `end [--status …]`; all take `--root`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_runlog.py`:

```python
import json
import os
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import runlog


def _lines(root):
    p = Path(root) / ".research" / "run.jsonl"
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]


class RunLog(unittest.TestCase):
    def test_start_mints_id_and_resets_context(self):
        with TemporaryDirectory() as d:
            rid = runlog.start(d)
            self.assertTrue(rid.startswith("r") and len(rid) == 9)
            recs = _lines(d)
            self.assertEqual(len(recs), 1)
            self.assertEqual(recs[0]["step"], "run_start")
            self.assertEqual(recs[0]["seq"], 0)
            self.assertIn("state", recs[0]["data"])          # baseline snapshot
            ctx = json.loads((Path(d) / ".research" / "run-context.json").read_text())
            self.assertEqual(ctx, {"run_id": rid, "cycle": 0, "seq": 0})

    def test_log_increments_seq_across_separate_calls(self):
        with TemporaryDirectory() as d:
            runlog.start(d)
            runlog.log_event("search", "gather", "ok", {"a": 1}, d)
            runlog.log_event("ingest", "normalize", "ok", {"b": 2}, d)  # fresh ctx read each call
            recs = _lines(d)
            self.assertEqual([r["seq"] for r in recs], [0, 1, 2])
            self.assertEqual(recs[1]["flow"], "search")
            self.assertEqual(recs[2]["data"], {"b": 2})

    def test_set_cycle_tags_subsequent_records(self):
        with TemporaryDirectory() as d:
            runlog.start(d)
            runlog.set_cycle(3, d)
            runlog.log_event("process", "draft", "ok", {}, d)
            self.assertEqual(_lines(d)[-1]["cycle"], 3)

    def test_end_writes_run_end(self):
        with TemporaryDirectory() as d:
            runlog.start(d)
            runlog.end("ok", d)
            last = _lines(d)[-1]
            self.assertEqual(last["step"], "run_end")
            self.assertEqual(last["data"]["status"], "ok")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests.test_runlog -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'runlog'`.

- [ ] **Step 3: Write the implementation**

Create `scripts/runlog.py`:

```python
"""Structured run log + run-context sidecar for engine-run validation. Stdlib only.

One JSON record per step is appended to .research/run.jsonl (run_id-segmented). The
sidecar .research/run-context.json holds the active {run_id, cycle, seq} across the
many short-lived process invocations that make up a run.
"""
import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

LOG_REL = ".research/run.jsonl"
CTX_REL = ".research/run-context.json"


def _now():
    return datetime.now(timezone.utc).isoformat()


def log_path(root="."):
    return Path(root) / LOG_REL


def ctx_path(root="."):
    return Path(root) / CTX_REL


def _load_ctx(root="."):
    p = ctx_path(root)
    if not p.exists():
        return {"run_id": None, "cycle": 0, "seq": 0}
    return json.loads(p.read_text(encoding="utf-8"))


def _save_ctx(ctx, root="."):
    p = ctx_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(ctx, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, p)


def _append(rec, root="."):
    p = log_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _record(ctx, flow, step, status, data):
    return {"run_id": ctx["run_id"], "cycle": ctx["cycle"], "seq": ctx["seq"],
            "ts": _now(), "flow": flow, "step": step, "status": status,
            "data": data or {}}


def start(root="."):
    run_id = "r" + hashlib.sha256(
        (_now() + "|" + str(os.getpid())).encode("utf-8")).hexdigest()[:8]
    ctx = {"run_id": run_id, "cycle": 0, "seq": 0}
    rec = _record(ctx, "run", "run_start", "ok", {"state": state_mod.load(root)})
    _append(rec, root)
    _save_ctx(ctx, root)
    return run_id


def set_cycle(n, root="."):
    ctx = _load_ctx(root)
    ctx["cycle"] = n
    _save_ctx(ctx, root)
    return n


def log_event(flow, step, status="ok", data=None, root="."):
    ctx = _load_ctx(root)
    ctx["seq"] += 1
    rec = _record(ctx, flow, step, status, data)
    _append(rec, root)
    _save_ctx(ctx, root)
    return rec


def end(status="ok", root="."):
    return log_event("run", "run_end", status, {"status": status}, root)


def _main(argv):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("start"); s.add_argument("--root", default=".")
    sc = sub.add_parser("set-cycle"); sc.add_argument("n", type=int); sc.add_argument("--root", default=".")
    lg = sub.add_parser("log"); lg.add_argument("--root", default=".")
    lg.add_argument("--flow", required=True); lg.add_argument("--step", required=True)
    lg.add_argument("--status", default="ok"); lg.add_argument("--data", default=None)
    lg.add_argument("--snapshot", action="store_true")
    e = sub.add_parser("end"); e.add_argument("--root", default="."); e.add_argument("--status", default="ok")
    args = ap.parse_args(argv)
    if args.cmd == "start":
        print(start(args.root)); return 0
    if args.cmd == "set-cycle":
        set_cycle(args.n, args.root); print(args.n); return 0
    if args.cmd == "log":
        data = json.loads(args.data) if args.data else {}
        if args.snapshot:
            data["state"] = state_mod.load(args.root)
        log_event(args.flow, args.step, args.status, data, args.root); return 0
    if args.cmd == "end":
        end(args.status, args.root); print("run ended"); return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 -m unittest tests.test_runlog -v`
Expected: PASS — 4 tests OK.

- [ ] **Step 5: Gitignore the run artifacts**

Add these two lines to `.gitignore` under the existing `.research/*.tmp` line:

```
.research/run.jsonl
.research/run-context.json
```

Verify: `git check-ignore .research/run.jsonl .research/run-context.json` prints both paths.

- [ ] **Step 6: Commit**

```bash
git add scripts/runlog.py tests/test_runlog.py .gitignore
git commit -m "feat: structured run log + context sidecar (runlog)"
```

---

### Task 2: `scripts/gotchas.py` — durable failure registry

**Files:**
- Create: `scripts/gotchas.py`
- Test: `tests/test_gotchas.py`

**Interfaces:**
- Produces (relied on by Task 3):
  - `sig_id(check, token) -> str` — `"gh"` + 8 hex.
  - `load_registry(root=".") -> dict[id, entry]` — last-write-wins, tolerates blank/torn lines.
  - `save_registry(registry, root=".")` — atomic full rewrite, sorted by id.
  - `match(registry, finding) -> entry | None`.
  - `record(registry, finding, now=None) -> (entry, is_new)`.
- A `finding` is a dict with at least `check` (str), `severity` (`"fail"`/`"warn"` or `FAIL`/`WARN`), `data` (dict); optional `title`, `symptom`, `token`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_gotchas.py`:

```python
import os
import sys
import unittest
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import gotchas


def _finding(check, data, token="", severity="warn"):
    return {"check": check, "data": data, "token": token,
            "severity": severity, "title": check, "symptom": ""}


class Gotchas(unittest.TestCase):
    def test_sig_id_stable_and_distinct(self):
        a = gotchas.sig_id("search_zero_sources", "")
        self.assertEqual(a, gotchas.sig_id("search_zero_sources", ""))
        self.assertTrue(a.startswith("gh") and len(a) == 10)
        self.assertNotEqual(a, gotchas.sig_id("search_zero_sources", "Uh oh"))

    def test_match_honors_check_and_token_substring(self):
        reg = {}
        e, _ = gotchas.record(reg, _finding("c", {"msg": "boom Uh oh"}, token="Uh oh"))
        self.assertIsNotNone(gotchas.match(reg, _finding("c", {"msg": "x Uh oh y"})))
        self.assertIsNone(gotchas.match(reg, _finding("c", {"msg": "clean"})))
        self.assertIsNone(gotchas.match(reg, _finding("other", {"msg": "Uh oh"})))

    def test_empty_token_matches_any_data(self):
        reg = {}
        gotchas.record(reg, _finding("c", {"x": 1}, token=""))
        self.assertIsNotNone(gotchas.match(reg, _finding("c", {"y": 2})))

    def test_record_creates_todo_stub_then_bumps(self):
        reg = {}
        e, is_new = gotchas.record(reg, _finding("c", {"x": 1}), now="t0")
        self.assertTrue(is_new)
        self.assertEqual((e["root_cause"], e["fix"]), ("TODO", "TODO"))
        self.assertEqual(e["occurrences"], 1)
        e2, is_new2 = gotchas.record(reg, _finding("c", {"x": 9}), now="t1")
        self.assertFalse(is_new2)
        self.assertEqual(e2["id"], e["id"])           # dedup by signature
        self.assertEqual(e2["occurrences"], 2)
        self.assertEqual(e2["last_seen"], "t1")
        self.assertEqual(len(reg), 1)

    def test_save_load_round_trip(self):
        with TemporaryDirectory() as d:
            reg = {}
            gotchas.record(reg, _finding("c", {"x": 1}))
            gotchas.save_registry(reg, d)
            again = gotchas.load_registry(d)
            self.assertEqual(set(again), set(reg))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests.test_gotchas -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'gotchas'`.

- [ ] **Step 3: Write the implementation**

Create `scripts/gotchas.py`:

```python
"""Gotchas registry: durable memory of run failures + their fixes. Stdlib only.

.research/gotchas.jsonl is committed. Each line is a gotcha keyed by a signature
(check name + optional data token). verify_run matches every finding against it:
known -> annotate with the recorded fix + bump occurrences; unknown -> append a
TODO stub so the failure is captured, not lost. root_cause/fix are filled by hand.
"""
import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

REG_REL = ".research/gotchas.jsonl"


def _now():
    return datetime.now(timezone.utc).isoformat()


def reg_path(root="."):
    return Path(root) / REG_REL


def sig_id(check, token):
    return "gh" + hashlib.sha256(
        (check + "|" + (token or "")).encode("utf-8")).hexdigest()[:8]


def load_registry(root="."):
    p = reg_path(root)
    if not p.exists():
        return {}
    by_id = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        rid = rec.get("id")
        if rid is not None:
            by_id[rid] = rec
    return by_id


def save_registry(registry, root="."):
    p = reg_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    body = "".join(json.dumps(registry[k], ensure_ascii=False) + "\n" for k in sorted(registry))
    tmp = p.with_suffix(".jsonl.tmp")
    tmp.write_text(body, encoding="utf-8")
    os.replace(tmp, p)


def _data_str(finding):
    return json.dumps(finding.get("data", {}), ensure_ascii=False, sort_keys=True)


def match(registry, finding):
    for entry in registry.values():
        if entry.get("check") != finding.get("check"):
            continue
        tok = entry.get("token", "")
        if tok == "" or tok in _data_str(finding):
            return entry
    return None


def record(registry, finding, now=None):
    now = now or _now()
    hit = match(registry, finding)
    if hit is not None:
        hit["occurrences"] = hit.get("occurrences", 0) + 1
        hit["last_seen"] = now
        return hit, False
    check = finding["check"]
    token = finding.get("token", "") or ""
    gid = sig_id(check, token)
    sev = finding.get("severity", "warn")
    sev = sev.lower() if isinstance(sev, str) else "warn"
    entry = {
        "id": gid, "check": check, "token": token,
        "title": finding.get("title") or check,
        "symptom": finding.get("symptom") or _data_str(finding),
        "root_cause": "TODO", "fix": "TODO",
        "severity": sev, "occurrences": 1,
        "first_seen": now, "last_seen": now,
    }
    registry[gid] = entry
    return entry, True


def _main(argv):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    l = sub.add_parser("list"); l.add_argument("--root", default=".")
    sh = sub.add_parser("show"); sh.add_argument("id"); sh.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    reg = load_registry(args.root)
    if args.cmd == "list":
        todo = [e for e in reg.values() if e["root_cause"] == "TODO"]
        done = [e for e in reg.values() if e["root_cause"] != "TODO"]
        for e in sorted(todo, key=lambda x: x["id"]) + sorted(done, key=lambda x: x["id"]):
            flag = "NEEDS-DIAGNOSIS" if e["root_cause"] == "TODO" else ""
            print(f"{e['id']}\t{e['severity']}\t{e['occurrences']}\t{e['check']}\t{e['title']}\t{flag}")
        return 0
    if args.cmd == "show":
        e = reg.get(args.id)
        if e is None:
            print(f"unknown gotcha: {args.id}", file=sys.stderr); return 1
        print(json.dumps(e, indent=2, ensure_ascii=False)); return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 -m unittest tests.test_gotchas -v`
Expected: PASS — 5 tests OK.

- [ ] **Step 5: Commit**

```bash
git add scripts/gotchas.py tests/test_gotchas.py
git commit -m "feat: gotchas registry — durable failure memory"
```

---

### Task 3: `scripts/verify_run.py` — invariant verifier + recompute + gotchas pass

**Files:**
- Create: `scripts/verify_run.py`
- Test: `tests/test_verify_run.py`

**Interfaces:**
- Consumes: `runlog` record schema (Task 1); `gotchas.load_registry/record/save_registry` (Task 2); `orchestrator.recommend_phase/next_actions/goal_met` and `state.load` (existing).
- Produces:
  - `parse_recs(lines) -> (recs, findings)`; `select_run(recs, run_id=None) -> recs`.
  - `all_findings(run_recs, root) -> [finding]`.
  - `verify(root=".", run_id=None, path=None, use_gotchas=True) -> (findings, exit_code)`.
  - CLI: `python3 scripts/verify_run.py [--root .] [--run-id R] [--path P] [--json] [--no-gotchas]` → prints report, exit 1 on any FAIL.
- A `finding` dict: `{check, severity (FAIL|WARN), title, detail, seq, data, token}`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_verify_run.py`:

```python
import json
import os
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state as st
import verify_run as vr


def _corpus_state(n_topic_t=3):
    s = st.load_default()
    ids = []
    for i in range(n_topic_t):
        e = st.add_corpus_entry(s, title=f"s{i}", source=f"http://x/{i}", topic="t",
                                native_path="n", extracted_path="e")
        ids.append(e["id"])
    s["graph"]["dirty"] = False
    return s, ids


def _good_log(root):
    """A minimal clean run: gather -> deepen with a draft, ending drained."""
    base, _ = _corpus_state(0)
    st.save(base, root)                                  # baseline = empty corpus
    recs = [
        {"run_id": "r1", "cycle": 0, "seq": 0, "ts": "t", "flow": "run",
         "step": "run_start", "status": "ok", "data": {"state": base}},
        {"run_id": "r1", "cycle": 1, "seq": 1, "ts": "t", "flow": "search",
         "step": "gather", "status": "ok",
         "data": {"gap_id": "g1", "gap_status": "done", "sources_added": 2}},
        {"run_id": "r1", "cycle": 1, "seq": 2, "ts": "t", "flow": "ingest",
         "step": "normalize", "status": "ok", "data": {"corpus_id": "cAAAAAAA1"}},
        {"run_id": "r1", "cycle": 1, "seq": 3, "ts": "t", "flow": "ingest",
         "step": "summary", "status": "ok", "data": {"corpus_added": 1, "graph_dirty": True}},
        {"run_id": "r1", "cycle": 1, "seq": 4, "ts": "t", "flow": "graph",
         "step": "graphify", "status": "ok", "data": {"node_count": 5, "edge_count": 4}},
        {"run_id": "r1", "cycle": 1, "seq": 5, "ts": "t", "flow": "graph",
         "step": "replay", "status": "ok", "data": {}},
        {"run_id": "r1", "cycle": 1, "seq": 6, "ts": "t", "flow": "graph",
         "step": "graph_events", "status": "ok", "data": {}},
        {"run_id": "r1", "cycle": 1, "seq": 7, "ts": "t", "flow": "ingest",
         "step": "integrity", "status": "ok", "data": {}},
    ]
    # final state: baseline + one logged corpus id
    final = st.load_default()
    st.add_corpus_entry(final, title="s", source="http://x/0", topic="t",
                        native_path="n", extracted_path="e", id="cAAAAAAA1")
    st.save(final, root)
    p = Path(root) / ".research" / "run.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("".join(json.dumps(r) + "\n" for r in recs))
    return recs


class VerifyGood(unittest.TestCase):
    def test_clean_run_has_no_fail(self):
        with TemporaryDirectory() as d:
            _good_log(d)
            findings, code = vr.verify(d, use_gotchas=False)
            fails = [f for f in findings if f["severity"] == vr.FAIL]
            self.assertEqual(fails, [], msg=str(fails))
            self.assertEqual(code, 0)


class VerifyCatches(unittest.TestCase):
    def _run(self, mutate):
        with TemporaryDirectory() as d:
            recs = _good_log(d)
            recs = mutate(recs)
            p = Path(d) / ".research" / "run.jsonl"
            p.write_text("".join(json.dumps(r) + "\n" for r in recs))
            findings, code = vr.verify(d, use_gotchas=False)
            return findings, code

    def test_done_gap_zero_sources_fails(self):
        def m(recs):
            recs[1]["data"]["sources_added"] = 0
            return recs
        f, code = self._run(m)
        self.assertTrue(any(x["check"] == "search_done_zero_sources" and x["severity"] == vr.FAIL for x in f))
        self.assertEqual(code, 1)

    def test_seq_not_increasing_fails(self):
        def m(recs):
            recs[3]["seq"] = 1
            return recs
        f, code = self._run(m)
        self.assertTrue(any(x["check"] == "seq_monotonic" and x["severity"] == vr.FAIL for x in f))

    def test_graph_nodes_decrease_fails(self):
        def m(recs):
            recs.append({"run_id": "r1", "cycle": 1, "seq": 8, "ts": "t", "flow": "graph",
                         "step": "graphify", "status": "ok", "data": {"node_count": 2}})
            return recs
        f, code = self._run(m)
        self.assertTrue(any(x["check"] == "graph_nodes_decreased" for x in f))

    def test_replay_out_of_order_fails(self):
        def m(recs):
            recs[4]["seq"], recs[5]["seq"] = 5, 4   # graphify after replay
            return recs
        f, code = self._run(m)
        self.assertTrue(any(x["check"] in ("seq_monotonic", "replay_ordering") and x["severity"] == vr.FAIL for x in f))

    def test_consistency_mismatch_fails(self):
        def m(recs):
            recs[2]["data"]["corpus_id"] = "cZZZZZZZZ"   # logged id not in final state
            return recs
        f, code = self._run(m)
        self.assertTrue(any(x["check"] == "corpus_id_mismatch" and x["severity"] == vr.FAIL for x in f))


class VerifyGotchas(unittest.TestCase):
    def test_unknown_appends_stub_known_annotates(self):
        import gotchas
        with TemporaryDirectory() as d:
            recs = _good_log(d)
            recs[1]["data"]["sources_added"] = 0          # trips search_done_zero_sources (FAIL)
            Path(d, ".research", "run.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs))
            findings, code = vr.verify(d, use_gotchas=True)
            reg = gotchas.load_registry(d)
            self.assertTrue(any(e["check"] == "search_done_zero_sources" for e in reg.values()))
            # second run: now a known gotcha, occurrences bumps
            vr.verify(d, use_gotchas=True)
            reg2 = gotchas.load_registry(d)
            hit = [e for e in reg2.values() if e["check"] == "search_done_zero_sources"][0]
            self.assertGreaterEqual(hit["occurrences"], 2)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests.test_verify_run -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'verify_run'`.

- [ ] **Step 3: Write the implementation**

Create `scripts/verify_run.py`:

```python
"""Validate an engine run from .research/run.jsonl. Stdlib only.

Reads the structured run log, asserts per-step + cross-step invariants, recomputes
the orchestrator's decisions from logged state snapshots, matches every finding
against the gotchas registry, prints a report, and exits 1 on any FAIL.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod
import orchestrator as orch
import gotchas as gotchas_mod

FAIL = "FAIL"
WARN = "WARN"


def _f(check, severity, title, detail, seq=None, data=None, token=""):
    return {"check": check, "severity": severity, "title": title,
            "detail": detail, "seq": seq, "data": data or {}, "token": token}


def parse_recs(lines):
    recs, findings = [], []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            recs.append(json.loads(line))
        except json.JSONDecodeError as e:
            findings.append(_f("line_parse", FAIL, "unparseable log line", str(e)))
    return recs, findings


def select_run(recs, run_id=None):
    if run_id:
        return [r for r in recs if r.get("run_id") == run_id]
    starts = [r for r in recs if r.get("step") == "run_start"]
    target = starts[-1]["run_id"] if starts else (recs[-1]["run_id"] if recs else None)
    return [r for r in recs if r.get("run_id") == target]


def _by_cycle(recs):
    out = {}
    for r in recs:
        out.setdefault(r.get("cycle", 0), []).append(r)
    return out


def check_seq_monotonic(recs):
    out, prev = [], None
    for r in recs:
        s = r.get("seq")
        if prev is not None and s is not None and s <= prev:
            out.append(_f("seq_monotonic", FAIL, "seq not increasing",
                          f"seq {s} follows {prev}", s, r.get("data")))
        if s is not None:
            prev = s
    return out


def check_cycle_monotonic(recs):
    out, prev = [], None
    for r in recs:
        c = r.get("cycle")
        if prev is not None and c is not None and c < prev:
            out.append(_f("cycle_monotonic", FAIL, "cycle went backwards",
                          f"cycle {c} follows {prev}", r.get("seq"), r.get("data")))
        if c is not None:
            prev = c
    return out


def check_run_start(recs):
    starts = [r for r in recs if r.get("step") == "run_start"]
    if len(starts) != 1:
        return [_f("run_start_count", FAIL, "run_start not unique",
                   f"found {len(starts)}")]
    if starts[0].get("seq") != 0:
        return [_f("run_start_seq", FAIL, "run_start not seq 0",
                   f"seq {starts[0].get('seq')}", starts[0].get("seq"))]
    return []


def check_search(recs):
    out = []
    for r in recs:
        if r.get("flow") == "search" and r.get("step") == "gather":
            d = r.get("data", {})
            gs, n = d.get("gap_status"), d.get("sources_added", 0)
            if gs == "done" and n < 1:
                out.append(_f("search_done_zero_sources", FAIL,
                              "gap marked done with 0 sources",
                              f"gap {d.get('gap_id')}", r.get("seq"), d))
            elif gs in ("queued", "failed") and n < 1:
                out.append(_f("search_zero_sources", WARN,
                              "search yielded 0 sources (flaky path)",
                              f"gap {d.get('gap_id')} -> {gs}", r.get("seq"), d, token=gs or ""))
    return out


def check_ingest(recs):
    out = []
    for r in recs:
        if r.get("flow") == "ingest" and r.get("step") == "summary":
            d = r.get("data", {})
            if d.get("corpus_added", 0) >= 1 and not d.get("graph_dirty"):
                out.append(_f("ingest_dirty_not_set", FAIL,
                              "corpus added but graph not marked dirty",
                              f"added {d.get('corpus_added')}", r.get("seq"), d))
    return out


def check_graph(recs):
    out, last = [], None
    for r in recs:
        if r.get("flow") == "graph" and r.get("step") == "graphify":
            nc = r.get("data", {}).get("node_count")
            if nc is not None and last is not None and nc < last:
                out.append(_f("graph_nodes_decreased", FAIL,
                              "graph node_count decreased (not incremental)",
                              f"{nc} < {last}", r.get("seq"), r.get("data")))
            if nc is not None:
                last = nc
    return out


def check_process(recs):
    out = []
    for r in recs:
        if r.get("flow") == "process" and r.get("step") == "cite_check" and r.get("status") == "fail":
            out.append(_f("cite_check_failed", FAIL, "recorded draft failed cite_check",
                          str(r.get("data")), r.get("seq"), r.get("data")))
        if r.get("flow") == "process" and r.get("step") == "draft" and not r.get("data", {}).get("draft_id"):
            out.append(_f("draft_missing_id", WARN, "draft step without draft_id",
                          str(r.get("data")), r.get("seq"), r.get("data")))
    return out


def check_integrity_per_cycle(recs):
    out = []
    for cyc, rs in _by_cycle(recs).items():
        has_work = any(x.get("flow") in ("ingest", "process") for x in rs)
        if has_work:
            ok = any(x.get("step") == "integrity" and x.get("status") == "ok" for x in rs)
            if not ok:
                out.append(_f("integrity_missing_or_failed", FAIL,
                              "cycle with work has no passing integrity step",
                              f"cycle {cyc}"))
    return out


def check_replay_ordering(recs):
    out = []
    for cyc, rs in _by_cycle(recs).items():
        def seq_of(step):
            xs = [x.get("seq") for x in rs if x.get("flow") == "graph" and x.get("step") == step]
            return xs[0] if xs else None
        g, rp, ge = seq_of("graphify"), seq_of("replay"), seq_of("graph_events")
        if g is not None and ge is not None:
            if rp is None:
                out.append(_f("replay_missing", WARN, "graph updated without a replay step",
                             f"cycle {cyc}"))
            elif not (g < rp < ge):
                out.append(_f("replay_ordering", FAIL,
                             "replay not between graphify and graph_events",
                             f"cycle {cyc}: graphify={g} replay={rp} events={ge}"))
    return out


def check_recompute(recs):
    out = []
    for r in recs:
        if r.get("flow") == "orchestrator" and r.get("step") == "decide":
            d = r.get("data", {})
            stt, dec = d.get("state"), d.get("decide")
            if not stt or not dec:
                out.append(_f("decide_missing_snapshot", WARN,
                              "decide record missing state/decide", "", r.get("seq")))
                continue
            na = orch.next_actions(stt)
            if (dec.get("phase") != orch.recommend_phase(stt)
                    or bool(dec.get("search")) != na["search"]
                    or bool(dec.get("process")) != na["process"]
                    or bool(dec.get("goal_met")) != orch.goal_met(stt)):
                out.append(_f("orchestrator_recompute", FAIL,
                              "logged decision diverges from recompute",
                              json.dumps(dec), r.get("seq"), d))
    return out


def check_work_after_goal(recs):
    gseq = None
    for r in recs:
        if (r.get("flow") == "orchestrator" and r.get("step") == "decide"
                and r.get("data", {}).get("decide", {}).get("goal_met")):
            gseq = r.get("seq")
            break
    if gseq is None:
        return []
    return [_f("work_after_goal_met", FAIL, "flow ran after goal_met",
               f"{r.get('flow')} at seq {r.get('seq')}", r.get("seq"))
            for r in recs
            if r.get("seq", -1) > gseq and r.get("flow") in ("search", "process")]


def check_completeness(recs):
    out = []
    bycyc = _by_cycle(recs)
    for r in recs:
        if r.get("flow") == "orchestrator" and r.get("step") == "decide":
            dec = r.get("data", {}).get("decide", {})
            same = bycyc.get(r.get("cycle"), [])
            if dec.get("search") and not any(x.get("flow") == "search" for x in same):
                out.append(_f("missing_search_step", WARN,
                              "search eligible but no search step logged",
                              f"cycle {r.get('cycle')}", r.get("seq")))
            if dec.get("process") and not any(x.get("flow") == "process" for x in same):
                out.append(_f("missing_process_step", WARN,
                              "process eligible but no process step logged",
                              f"cycle {r.get('cycle')}", r.get("seq")))
    return out


def check_consistency(recs, root):
    starts = [r for r in recs if r.get("step") == "run_start"]
    if not starts:
        return []
    base = starts[-1].get("data", {}).get("state") or {}
    final = state_mod.load(root)
    out = []

    base_corpus = {e["id"] for e in base.get("corpus", [])}
    final_corpus = {e["id"] for e in final.get("corpus", [])}
    logged_corpus = {r["data"]["corpus_id"] for r in recs
                     if r.get("flow") == "ingest" and r.get("step") == "normalize"
                     and r.get("data", {}).get("corpus_id")}
    if (final_corpus - base_corpus) != logged_corpus:
        out.append(_f("corpus_id_mismatch", FAIL,
                      "logged corpus ids != new corpus in state",
                      f"logged {sorted(logged_corpus)} vs new {sorted(final_corpus - base_corpus)}"))

    base_drafts = {d["id"] for d in base.get("drafts", [])}
    final_drafts = {d["id"] for d in final.get("drafts", [])}
    logged_drafts = {r["data"]["draft_id"] for r in recs
                     if r.get("flow") == "process" and r.get("step") == "draft"
                     and r.get("data", {}).get("draft_id")}
    if (final_drafts - base_drafts) != logged_drafts:
        out.append(_f("draft_id_mismatch", FAIL,
                      "logged draft ids != new drafts in state",
                      f"logged {sorted(logged_drafts)} vs new {sorted(final_drafts - base_drafts)}"))
    return out


def all_findings(recs, root):
    out = []
    for fn in (check_seq_monotonic, check_cycle_monotonic, check_run_start,
               check_search, check_ingest, check_graph, check_process,
               check_integrity_per_cycle, check_replay_ordering,
               check_recompute, check_work_after_goal, check_completeness):
        out += fn(recs)
    out += check_consistency(recs, root)
    return out


def _compute(root, run_id, path, use_gotchas):
    p = Path(path) if path else Path(root) / ".research" / "run.jsonl"
    lines = p.read_text(encoding="utf-8").splitlines() if p.exists() else []
    recs, findings = parse_recs(lines)
    run = select_run(recs, run_id)
    findings += all_findings(run, root)
    notes = {}
    if use_gotchas:
        reg = gotchas_mod.load_registry(root)
        for fnd in findings:
            entry, is_new = gotchas_mod.record(reg, {**fnd, "severity": fnd["severity"].lower()})
            notes[id(fnd)] = (f"[NEW {entry['id']} — capture in gotchas.jsonl]" if is_new
                              else f"[KNOWN {entry['id']}: {entry['fix']}]")
        gotchas_mod.save_registry(reg, root)
    code = 1 if any(f["severity"] == FAIL for f in findings) else 0
    return run, findings, notes, code


def verify(root=".", run_id=None, path=None, use_gotchas=True):
    _run, findings, _notes, code = _compute(root, run_id, path, use_gotchas)
    return findings, code


def _render(run, findings, notes):
    lines = []
    bycyc = _by_cycle(run)
    rid = run[0]["run_id"] if run else "(none)"
    lines.append(f"Run {rid}: {len(run)} records")
    for cyc in sorted(bycyc):
        lines.append(f"  cycle {cyc}:")
        for r in bycyc[cyc]:
            lines.append(f"    [{r.get('seq')}] {r.get('flow')}/{r.get('step')} {r.get('status')}")
    fails = sum(1 for f in findings if f["severity"] == FAIL)
    warns = sum(1 for f in findings if f["severity"] == WARN)
    lines.append(f"FINDINGS: {fails} FAIL, {warns} WARN")
    for f in findings:
        note = notes.get(id(f), "")
        lines.append(f"  {f['severity']} {f['check']} (seq {f['seq']}): {f['detail']} {note}")
    return "\n".join(lines)


def _main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--path", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-gotchas", action="store_true")
    args = ap.parse_args(argv)
    run, findings, notes, code = _compute(args.root, args.run_id, args.path, not args.no_gotchas)
    if args.json:
        print(json.dumps({"run_id": run[0]["run_id"] if run else None,
                          "exit": code, "findings": findings}, ensure_ascii=False))
    else:
        print(_render(run, findings, notes))
    return code


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 -m unittest tests.test_verify_run -v`
Expected: PASS — all tests OK.

- [ ] **Step 5: Commit**

```bash
git add scripts/verify_run.py tests/test_verify_run.py
git commit -m "feat: run verifier — invariants, recompute, gotchas pass"
```

---

### Task 4: Instrument the flows + prompts

**Files:**
- Modify: `scripts/search_flow.sh`
- Modify: `scripts/ingest_flow.sh`
- Modify: `.claude/loop.md`
- Modify: `.claude/process.md`
- Modify: `.claude/goal.md`

**Interfaces:**
- Consumes: `runlog` CLI (Task 1) — `python3 scripts/runlog.py log --flow … --step … --status … --data '<json>'`, `start`, `set-cycle`, `end`.
- Produces: a `.research/run.jsonl` that `verify_run.py` can validate.

Note: `gather.sh` is the manual spike tool and is **not** in the `/goal` orchestrated path, so it is not instrumented — only `search_flow.sh` and `ingest_flow.sh` run inside the loop.

- [ ] **Step 1: Instrument `scripts/search_flow.sh`**

After line 13 (`SP="python3 $HERE/state.py"`) add:

```bash
RL="python3 $HERE/runlog.py"
```

Replace the done-branch (the `if [ "$kept" -gt 0 ]; then` block, lines ~51–54) so it logs after recording the gap:

```bash
  if [ "$kept" -gt 0 ]; then
    $SP set-gap --root "$ROOT" --id "$gid" --status done >/dev/null
    $SP budget-spend --root "$ROOT" --sources "$kept" >/dev/null
    $RL log --root "$ROOT" --flow search --step gather --status ok \
      --data "{\"gap_id\":\"$gid\",\"gap_status\":\"done\",\"sources_added\":$kept}"
    echo "search: gap $gid -> $kept source(s) into ingest/"
```

In the `else` branch, after the line that may mark the gap `failed` (the `[ "$att" -ge 3 ] && …` line) and before its `echo`, add:

```bash
    gs=queued; [ "$att" -ge 3 ] && gs=failed
    $RL log --root "$ROOT" --flow search --step gather --status skip \
      --data "{\"gap_id\":\"$gid\",\"gap_status\":\"$gs\",\"sources_added\":0,\"attempts\":$att}"
```

- [ ] **Step 2: Instrument `scripts/ingest_flow.sh`**

After line 8 (`PY="python3"`) add:

```bash
RL="python3 $HERE/runlog.py"
```

In `fail_item()` (line 14), add a log call so failures are recorded:

```bash
fail_item() { echo "$2" >&2; mv "$1" "$ROOT/ingest/_failed/" 2>/dev/null; \
  $RL log --root "$ROOT" --flow ingest --step normalize --status fail --data "{\"reason\":\"$2\"}"; }
```

After line 23 (`mkdir -p "$ROOT/ingest/_done" "$ROOT/ingest/_failed"`) add a counter init:

```bash
added=0
```

Replace the success tail of the loop (lines 59–60) so it logs and counts:

```bash
  mv "$f" "$ROOT/ingest/_done/" || { echo "warning: could not archive $f" >&2; }
  added=$((added+1))
  $RL log --root "$ROOT" --flow ingest --step normalize --status ok \
    --data "{\"corpus_id\":\"$id\",\"type\":\"$type\"}"
  echo "ingested [$type]: $source_disp -> $out"
```

Replace the final line (line 62, `echo "Done. …"`) so a summary is logged:

```bash
$RL log --root "$ROOT" --flow ingest --step summary --status ok \
  --data "{\"corpus_added\":$added,\"graph_dirty\":true}"
echo "Done. Graph marked dirty; run the graph-update step next."
```

- [ ] **Step 3: Instrument `.claude/loop.md`**

The verifier's `replay_ordering` invariant requires, within a cycle, `seq(graphify) < seq(replay) < seq(graph_events)`. But the node/edge counts (`$N`/`$E`) that the `graphify` log needs are only computed in step 5 (after replay and the event append have run). To satisfy both, emit **all three** `graph` log lines together in step 5, in pipeline order, using the counts from step 5. Do not scatter them across steps 3/4.

Append to the Ingest cycle prompt's step 5 (right after `set-graph` records `$N`/`$E`):

```markdown
   Now emit the three graph-step log records in pipeline order (this fixes their
   relative `seq` for the verifier — graphify, then replay, then graph_events):
   ```
   python3 scripts/runlog.py log --flow graph --step graphify --status ok --data "{\"node_count\":$N,\"edge_count\":$E}"
   python3 scripts/runlog.py log --flow graph --step replay --status ok
   python3 scripts/runlog.py log --flow graph --step graph_events --status ok
   ```
```

Append to the Ingest cycle prompt's step 6 (the integrity check):

```markdown
   Log the integrity result: `python3 scripts/runlog.py log --flow ingest --step integrity --status ok`
   (use `--status fail` and stop if it reported problems).
```

- [ ] **Step 4: Instrument `.claude/process.md`**

After the draft is recorded (step 5), append:

```markdown
   Log the draft: `python3 scripts/runlog.py log --flow process --step draft --status ok --data "{\"draft_id\":\"$ID\"}"`.
```

After the citation gate (step 4a), append:

```markdown
   Log the citation gate: on exit 0 `python3 scripts/runlog.py log --flow process --step cite_check --status ok`;
   on exit 1 (after you have exhausted fixes) `--status fail`.
```

After the integrity check (step 8), append:

```markdown
   Log it: `python3 scripts/runlog.py log --flow process --step integrity --status ok` (or `--status fail` if it reported problems).
```

- [ ] **Step 5: Instrument `.claude/goal.md`**

At loop entry (before step 1 of the cycle), add:

```markdown
0. **Run start (once).** On the first cycle only, run `python3 scripts/runlog.py start` to open
   the run log. Each cycle, run `python3 scripts/runlog.py set-cycle K` (K = your cycle counter)
   before doing anything else, so every step this cycle is tagged with the cycle number.
```

In step 2 (Decide), after capturing the decide JSON the orchestrator printed as `$D`, add:

```markdown
   Log the decision with a state snapshot so the verifier can independently recompute it.
   The record's `data` must be `{"decide": <the decide JSON>, "state": <snapshot>}`, so pass the
   decide JSON nested under `decide` and let `--snapshot` add `state`:
   `python3 scripts/runlog.py log --flow orchestrator --step decide --status ok --snapshot --data "{\"decide\": $D}"`
```

This produces `data = {"decide": {...}, "state": {...}}`, exactly what `verify_run.check_recompute`
reads (`data.decide` vs the recompute from `data.state`).

At the stop/goal-met point and the safety-cap stop, add:

```markdown
   Before stopping, close the run log: `python3 scripts/runlog.py end --status ok`
   (use `--status capped` at the safety-cap stop).
```

- [ ] **Step 6: Verify the instrumentation is well-formed**

Run:
```bash
cd "$(git rev-parse --show-toplevel)"
bash -n scripts/search_flow.sh && bash -n scripts/ingest_flow.sh && echo "SYNTAX OK"
grep -q "runlog.py" scripts/search_flow.sh && grep -q "runlog.py" scripts/ingest_flow.sh \
  && grep -q "runlog.py" .claude/loop.md && grep -q "runlog.py" .claude/process.md \
  && grep -q "runlog.py start" .claude/goal.md && echo "WIRED OK"
```
Expected: `SYNTAX OK` then `WIRED OK`.

> The true end-to-end exercise of the instrumentation is the post-merge live `/goal` smoke run (the consumer of this whole suite), which produces a real `.research/run.jsonl` for `verify_run.py`. This step confirms only that the wiring is syntactically sound and present.

- [ ] **Step 7: Commit**

```bash
git add scripts/search_flow.sh scripts/ingest_flow.sh .claude/loop.md .claude/process.md .claude/goal.md
git commit -m "feat: instrument flows + prompts to emit run-log records"
```

---

## Self-Review

**1. Spec coverage:**
- §2 structured instrumentation → Task 1 (`runlog.py`) + Task 4 (wiring). ✓
- §2 automated verifier + report → Task 3. ✓
- §2 record schema run_id/cycle/seq + sidecar → Task 1. ✓
- §2 severity tiers FAIL/WARN → Task 3 `_f` + exit code; tests assert both. ✓
- §2 deterministic-first logging + missing-step WARN → Task 4 bash logs; Task 3 `check_completeness`. ✓
- §2 single append run_id-segmented → Task 1 append + Task 3 `select_run`. ✓
- §2 independent recompute → Task 3 `check_recompute`; Task 4 goal.md `--snapshot`. ✓
- §2 gotchas process + signature → Task 2 + Task 3 gotchas pass. ✓
- §2 gitignore run artifacts / commit gotchas → Task 1 Step 5 (gitignore); gotchas.jsonl not ignored. ✓
- §3 schema + run_start baseline snapshot → Task 1 `start`. ✓
- §5 invariants → Task 3 `check_*` (structural, search, ingest, graph, process, integrity, replay ordering, recompute, work-after-goal, completeness, consistency). ✓
- §7 tests → Tasks 1/2/3 test files. ✓
- **Deviations from spec (flag at cross-check):** (a) `gather.sh` NOT instrumented — it is not in the `/goal` path; (b) consistency checks compare **distinct logged ids vs new-in-state id sets** (robust to idempotent dedup) rather than raw count arithmetic; (c) assertions consistency is **not** strictly checked (replay is idempotent and prune uses tombstones, making a strict equality fragile) — corpus and draft id-set reconciliation cover the deterministic part. Each is a deliberate, defensible narrowing of spec §4/§5.

**2. Placeholder scan:** No TBD/TODO-as-work and no placeholder code. The literal string `"TODO"` is intentional data (gotcha stub `root_cause`/`fix`). `verify()` returns a clean `(findings, code)` via the shared `_compute` helper (no dead ternary). The loop.md graph-logging instruction emits the three records together in step 5 in graphify→replay→graph_events order (satisfies `replay_ordering`); the goal.md decide-logging instruction is a single unambiguous command producing `data = {"decide", "state"}`.

**3. Type consistency:** record schema keys (`run_id, cycle, seq, ts, flow, step, status, data`) identical across `runlog._record`, the tests, and every `verify_run` check. Finding dict keys (`check, severity, title, detail, seq, data, token`) consistent between `_f`, `gotchas.record` consumption, and the tests. `gotchas.sig_id`/`load_registry`/`save_registry`/`match`/`record` names match between Task 2 definition, its test, and Task 3 usage. Severity constants `FAIL`/`WARN` (upper) in verify_run; gotchas stores lowercased severity — the bridge is explicit in `verify`/`_main` (`fnd["severity"].lower()`).
