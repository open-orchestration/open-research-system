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
