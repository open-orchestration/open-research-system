"""Heuristic junk detection for fetched pages. Stdlib only."""
import sys
from pathlib import Path

_MARKERS = (
    "just a moment", "enable javascript", "uh oh", "captcha",
    "are you a robot", "access denied", "403 forbidden",
    "page not found", "rate limit",
)
_MIN_CHARS = 200


def is_junk(text):
    stripped = "".join(text.split())
    if len(stripped) < _MIN_CHARS:
        return True
    low = text.lower()
    return any(m in low for m in _MARKERS)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "check":
        content = Path(sys.argv[2]).read_text(encoding="utf-8", errors="replace")
        sys.exit(1 if is_junk(content) else 0)
    print("usage: junk.py check <file>", file=sys.stderr)
    sys.exit(2)
