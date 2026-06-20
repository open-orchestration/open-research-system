"""On-disk state ledger for the loop research engine. Stdlib only."""
import copy
import hashlib
import json
import os
import sys
from pathlib import Path

DEFAULT_STATE = {
    "budget": {
        "tokens_per_cycle": 200000,
        "max_subagents": 8,
        "phase": "gather",
        "weights": {
            "gather":     {"search": 0.7, "ingest": 0.3, "process": 0.0},
            "deepen":     {"search": 0.4, "ingest": 0.3, "process": 0.3},
            "synthesize": {"search": 0.1, "ingest": 0.1, "process": 0.8},
        },
        "spent": {"tokens": 0, "sources": 0, "cycle_started_at": None},
    },
    "gaps": [],
    "inbox": [],
    "corpus": [],
    "graph": {"dirty": False, "last_update": None, "node_count": 0, "edge_count": 0},
    "assertions": {"count": 0, "file": ".research/graph-assertions.jsonl"},
    "drafts": [],
}


def state_path(root="."):
    return Path(root) / ".research" / "state.json"


def load(root="."):
    p = state_path(root)
    if not p.exists():
        seed = copy.deepcopy(DEFAULT_STATE)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(seed, indent=2, ensure_ascii=False), encoding="utf-8")
        return seed
    return json.loads(p.read_text(encoding="utf-8"))


def save(state, root="."):
    p = state_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, p)


def gen_id(prefix, seed):
    return prefix + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:8]
