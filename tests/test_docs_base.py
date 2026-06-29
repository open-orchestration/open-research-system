import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state


class DocsBase(unittest.TestCase):
    def test_default(self):
        os.environ.pop("DOCS_BASE", None)
        self.assertEqual(state.docs_base(), ".research/docs")

    def test_env_override(self):
        os.environ["DOCS_BASE"] = "custom/dir"
        try:
            self.assertEqual(state.docs_base(), "custom/dir")
        finally:
            os.environ.pop("DOCS_BASE", None)


if __name__ == "__main__":
    unittest.main()
