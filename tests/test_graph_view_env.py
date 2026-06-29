import importlib.util, os, unittest
SPEC = os.path.join(os.path.dirname(__file__), "..", "scripts", "graph_view_server.py")


class GVEnv(unittest.TestCase):
    def test_env_vars_referenced(self):
        with open(SPEC) as f:
            src = f.read()
        for var in ("GV_GRAPH", "GV_STATE", "GV_HTML", "GV_DASHBOARD"):
            self.assertIn(var, src, var)


if __name__ == "__main__":
    unittest.main()
