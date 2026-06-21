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
