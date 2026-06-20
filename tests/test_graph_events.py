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

    def test_load_empty_or_missing_path_is_empty_graph(self):
        # Empty string (the CLI default for --old) must be treated as an empty
        # graph, not Path(".") — which is a directory and would raise IsADirectoryError.
        self.assertEqual(ge._load(""), {})
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(ge._load(str(Path(t) / "nope.json")), {})


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


if __name__ == "__main__":
    unittest.main()
