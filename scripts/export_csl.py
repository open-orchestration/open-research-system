#!/usr/bin/env python3
"""Export the corpus as CSL-JSON so the engine's provenance is interchangeable, not
just internally consistent.

Grounded in the corpus's own citation-format findings: CSL-JSON fixes a closed
45-item-type enum on `type` and requires exactly `["type", "id"]` per item
(d59d1279b, primary csl-data.json schema); biblatex's @online/@dataset/@software model
the web-native sources the legacy BibTeX set cannot (de47719c4). We emit CSL-JSON
because its two-required-field minimum maps cleanly onto every corpus entry.
"""
import json
import sys
from pathlib import Path

# The closed CSL-JSON item-type enumeration (csl-data.json `type`), per d59d1279b.
CSL_TYPES = {
    "article", "article-journal", "article-magazine", "article-newspaper", "bill",
    "book", "broadcast", "chapter", "classic", "collection", "dataset", "document",
    "entry", "entry-dictionary", "entry-encyclopedia", "event", "figure", "graphic",
    "hearing", "interview", "legal_case", "legislation", "manuscript", "map",
    "motion_picture", "musical_score", "pamphlet", "paper-conference", "patent",
    "performance", "periodical", "personal_communication", "post", "post-weblog",
    "regulation", "report", "review", "review-book", "software", "song", "speech",
    "standard", "thesis", "treaty", "webpage",
}


def _csl_type(source: str) -> str:
    """Map a corpus source URI to the closest standard CSL type from the closed enum."""
    s = (source or "").lower()
    if "arxiv.org" in s:
        return "article-journal"
    if s.startswith("http"):
        return "webpage"
    return "document"  # file:// internal ingest — a document with no public URL


def to_csl(entry: dict) -> dict:
    item = {"type": _csl_type(entry.get("source", "")), "id": entry["id"]}
    if entry.get("title"):
        item["title"] = entry["title"]
    src = entry.get("source", "")
    if src.startswith("http"):
        item["URL"] = src
    if entry.get("ingested_at"):
        item["accessed"] = {"raw": entry["ingested_at"]}
    if entry.get("topic"):
        item["keyword"] = entry["topic"]
    return item


def export(state: dict) -> list:
    items = [to_csl(e) for e in state.get("corpus", [])]
    for it in items:  # the gate the format spec defines: closed enum + both required fields
        assert it["type"] in CSL_TYPES, f"non-CSL type {it['type']!r} for {it['id']}"
        assert it.get("type") and it.get("id"), f"missing required type/id: {it}"
    return items


def _demo():
    sample = {"corpus": [
        {"id": "c0000arxiv", "title": "A Paper", "source": "https://arxiv.org/abs/1",
         "topic": "06", "ingested_at": "2026-01-01T00:00:00+00:00"},
        {"id": "c0000web", "title": "A Doc Page", "source": "https://docs.example/x", "topic": "12"},
        {"id": "c0000file", "title": "Internal", "source": "file://g1.md", "topic": "08"},
    ]}
    out = export(sample)
    assert out[0]["type"] == "article-journal" and out[0]["URL"].startswith("http")
    assert out[1]["type"] == "webpage"
    assert out[2]["type"] == "document" and "URL" not in out[2]
    assert all(i["type"] in CSL_TYPES and i["id"] for i in out)
    print("export_csl self-check OK")


if __name__ == "__main__":
    if "--selfcheck" in sys.argv:
        _demo()
    else:
        root = sys.argv[1] if len(sys.argv) > 1 else "."
        state = json.loads((Path(root) / ".research" / "state.json").read_text(encoding="utf-8"))
        json.dump(export(state), sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
