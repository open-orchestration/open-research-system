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
