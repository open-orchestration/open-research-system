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

    def test_recompute_divergence_fails(self):
        with TemporaryDirectory() as d:
            base = st.load_default()
            st.save(st.load_default(), d)                      # final state = empty default
            recs = [
                {"run_id": "r1", "cycle": 0, "seq": 0, "ts": "t", "flow": "run",
                 "step": "run_start", "status": "ok", "data": {"state": base}},
                {"run_id": "r1", "cycle": 1, "seq": 1, "ts": "t", "flow": "orchestrator",
                 "step": "decide", "status": "ok",
                 "data": {"decide": {"phase": "synthesize", "search": False,
                                     "process": False, "goal_met": False}, "state": base}},
            ]
            p = Path(d) / ".research" / "run.jsonl"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("".join(json.dumps(r) + "\n" for r in recs))
            findings, code = vr.verify(d, use_gotchas=False)
            self.assertTrue(any(x["check"] == "orchestrator_recompute" and x["severity"] == vr.FAIL
                                for x in findings))
            self.assertEqual(code, 1)

    def test_work_after_goal_met_fails(self):
        with TemporaryDirectory() as d:
            base = st.load_default()
            st.save(st.load_default(), d)
            recs = [
                {"run_id": "r1", "cycle": 0, "seq": 0, "ts": "t", "flow": "run",
                 "step": "run_start", "status": "ok", "data": {"state": base}},
                {"run_id": "r1", "cycle": 1, "seq": 1, "ts": "t", "flow": "orchestrator",
                 "step": "decide", "status": "ok",
                 "data": {"decide": {"phase": "synthesize", "search": False,
                                     "process": False, "goal_met": True}, "state": base}},
                {"run_id": "r1", "cycle": 1, "seq": 2, "ts": "t", "flow": "search",
                 "step": "gather", "status": "ok",
                 "data": {"gap_id": "g1", "gap_status": "done", "sources_added": 1}},
            ]
            p = Path(d) / ".research" / "run.jsonl"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("".join(json.dumps(r) + "\n" for r in recs))
            findings, code = vr.verify(d, use_gotchas=False)
            self.assertTrue(any(x["check"] == "work_after_goal_met" and x["severity"] == vr.FAIL
                                for x in findings))
            self.assertEqual(code, 1)


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
