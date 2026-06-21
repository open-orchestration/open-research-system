"""Validate an engine run from .research/run.jsonl. Stdlib only.

Reads the structured run log, asserts per-step + cross-step invariants, recomputes
the orchestrator's decisions from logged state snapshots, matches every finding
against the gotchas registry, prints a report, and exits 1 on any FAIL.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod
import orchestrator as orch
import gotchas as gotchas_mod

FAIL = "FAIL"
WARN = "WARN"


def _f(check, severity, title, detail, seq=None, data=None, token=""):
    return {"check": check, "severity": severity, "title": title,
            "detail": detail, "seq": seq, "data": data or {}, "token": token}


def parse_recs(lines):
    recs, findings = [], []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            recs.append(json.loads(line))
        except json.JSONDecodeError as e:
            findings.append(_f("line_parse", FAIL, "unparseable log line", str(e)))
    return recs, findings


def select_run(recs, run_id=None):
    if run_id:
        return [r for r in recs if r.get("run_id") == run_id]
    starts = [r for r in recs if r.get("step") == "run_start"]
    target = starts[-1]["run_id"] if starts else (recs[-1]["run_id"] if recs else None)
    return [r for r in recs if r.get("run_id") == target]


def _by_cycle(recs):
    out = {}
    for r in recs:
        out.setdefault(r.get("cycle", 0), []).append(r)
    return out


def check_seq_monotonic(recs):
    out, prev = [], None
    for r in recs:
        s = r.get("seq")
        if prev is not None and s is not None and s <= prev:
            out.append(_f("seq_monotonic", FAIL, "seq not increasing",
                          f"seq {s} follows {prev}", s, r.get("data")))
        if s is not None:
            prev = s
    return out


def check_cycle_monotonic(recs):
    out, prev = [], None
    for r in recs:
        c = r.get("cycle")
        if prev is not None and c is not None and c < prev:
            out.append(_f("cycle_monotonic", FAIL, "cycle went backwards",
                          f"cycle {c} follows {prev}", r.get("seq"), r.get("data")))
        if c is not None:
            prev = c
    return out


def check_run_start(recs):
    starts = [r for r in recs if r.get("step") == "run_start"]
    if len(starts) != 1:
        return [_f("run_start_count", FAIL, "run_start not unique",
                   f"found {len(starts)}")]
    if starts[0].get("seq") != 0:
        return [_f("run_start_seq", FAIL, "run_start not seq 0",
                   f"seq {starts[0].get('seq')}", starts[0].get("seq"))]
    return []


def check_search(recs):
    out = []
    for r in recs:
        if r.get("flow") == "search" and r.get("step") == "gather":
            d = r.get("data", {})
            gs, n = d.get("gap_status"), d.get("sources_added", 0)
            if gs == "done" and n < 1:
                out.append(_f("search_done_zero_sources", FAIL,
                              "gap marked done with 0 sources",
                              f"gap {d.get('gap_id')}", r.get("seq"), d))
            elif gs in ("queued", "failed") and n < 1:
                out.append(_f("search_zero_sources", WARN,
                              "search yielded 0 sources (flaky path)",
                              f"gap {d.get('gap_id')} -> {gs}", r.get("seq"), d, token=gs or ""))
    return out


def check_ingest(recs):
    out = []
    for r in recs:
        if r.get("flow") == "ingest" and r.get("step") == "summary":
            d = r.get("data", {})
            if d.get("corpus_added", 0) >= 1 and not d.get("graph_dirty"):
                out.append(_f("ingest_dirty_not_set", FAIL,
                              "corpus added but graph not marked dirty",
                              f"added {d.get('corpus_added')}", r.get("seq"), d))
    return out


def check_graph(recs):
    out, last = [], None
    for r in recs:
        if r.get("flow") == "graph" and r.get("step") == "graphify":
            nc = r.get("data", {}).get("node_count")
            if nc is not None and last is not None and nc < last:
                out.append(_f("graph_nodes_decreased", FAIL,
                              "graph node_count decreased (not incremental)",
                              f"{nc} < {last}", r.get("seq"), r.get("data")))
            if nc is not None:
                last = nc
    return out


def check_process(recs):
    out = []
    for r in recs:
        if r.get("flow") == "process" and r.get("step") == "cite_check" and r.get("status") == "fail":
            out.append(_f("cite_check_failed", FAIL, "recorded draft failed cite_check",
                          str(r.get("data")), r.get("seq"), r.get("data")))
        if r.get("flow") == "process" and r.get("step") == "draft" and not r.get("data", {}).get("draft_id"):
            out.append(_f("draft_missing_id", WARN, "draft step without draft_id",
                          str(r.get("data")), r.get("seq"), r.get("data")))
    return out


def check_integrity_per_cycle(recs):
    out = []
    for cyc, rs in _by_cycle(recs).items():
        has_work = any(x.get("flow") in ("ingest", "process") for x in rs)
        if has_work:
            ok = any(x.get("step") == "integrity" and x.get("status") == "ok" for x in rs)
            if not ok:
                out.append(_f("integrity_missing_or_failed", FAIL,
                              "cycle with work has no passing integrity step",
                              f"cycle {cyc}"))
    return out


def check_replay_ordering(recs):
    out = []
    for cyc, rs in _by_cycle(recs).items():
        def seq_of(step):
            xs = [x.get("seq") for x in rs if x.get("flow") == "graph" and x.get("step") == step]
            return xs[0] if xs else None
        g, rp, ge = seq_of("graphify"), seq_of("replay"), seq_of("graph_events")
        if g is not None and ge is not None:
            if rp is None:
                out.append(_f("replay_missing", WARN, "graph updated without a replay step",
                             f"cycle {cyc}"))
            elif not (g < rp < ge):
                out.append(_f("replay_ordering", FAIL,
                             "replay not between graphify and graph_events",
                             f"cycle {cyc}: graphify={g} replay={rp} events={ge}"))
    return out


def check_recompute(recs):
    out = []
    for r in recs:
        if r.get("flow") == "orchestrator" and r.get("step") == "decide":
            d = r.get("data", {})
            stt, dec = d.get("state"), d.get("decide")
            if stt is None or dec is None:
                out.append(_f("decide_missing_snapshot", WARN,
                              "decide record missing state/decide", "", r.get("seq")))
                continue
            na = orch.next_actions(stt)
            if (dec.get("phase") != orch.recommend_phase(stt)
                    or bool(dec.get("search")) != na["search"]
                    or bool(dec.get("process")) != na["process"]
                    or bool(dec.get("goal_met")) != orch.goal_met(stt)):
                out.append(_f("orchestrator_recompute", FAIL,
                              "logged decision diverges from recompute",
                              json.dumps(dec), r.get("seq"), d))
    return out


def check_work_after_goal(recs):
    gseq = None
    for r in recs:
        if (r.get("flow") == "orchestrator" and r.get("step") == "decide"
                and r.get("data", {}).get("decide", {}).get("goal_met")):
            gseq = r.get("seq")
            break
    if gseq is None:
        return []
    return [_f("work_after_goal_met", FAIL, "flow ran after goal_met",
               f"{r.get('flow')} at seq {r.get('seq')}", r.get("seq"))
            for r in recs
            if r.get("seq", -1) > gseq and r.get("flow") in ("search", "process")]


def check_completeness(recs):
    out = []
    bycyc = _by_cycle(recs)
    for r in recs:
        if r.get("flow") == "orchestrator" and r.get("step") == "decide":
            dec = r.get("data", {}).get("decide", {})
            same = bycyc.get(r.get("cycle"), [])
            if dec.get("search") and not any(x.get("flow") == "search" for x in same):
                out.append(_f("missing_search_step", WARN,
                              "search eligible but no search step logged",
                              f"cycle {r.get('cycle')}", r.get("seq")))
            if dec.get("process") and not any(x.get("flow") == "process" for x in same):
                out.append(_f("missing_process_step", WARN,
                              "process eligible but no process step logged",
                              f"cycle {r.get('cycle')}", r.get("seq")))
    return out


def check_consistency(recs, root):
    starts = [r for r in recs if r.get("step") == "run_start"]
    if not starts:
        return []
    base = starts[-1].get("data", {}).get("state") or {}
    final = state_mod.load(root)
    out = []

    base_corpus = {e["id"] for e in base.get("corpus", [])}
    final_corpus = {e["id"] for e in final.get("corpus", [])}
    logged_corpus = {r["data"]["corpus_id"] for r in recs
                     if r.get("flow") == "ingest" and r.get("step") == "normalize"
                     and r.get("data", {}).get("corpus_id")}
    if (final_corpus - base_corpus) != logged_corpus:
        out.append(_f("corpus_id_mismatch", FAIL,
                      "logged corpus ids != new corpus in state",
                      f"logged {sorted(logged_corpus)} vs new {sorted(final_corpus - base_corpus)}"))

    base_drafts = {d["id"] for d in base.get("drafts", [])}
    final_drafts = {d["id"] for d in final.get("drafts", [])}
    logged_drafts = {r["data"]["draft_id"] for r in recs
                     if r.get("flow") == "process" and r.get("step") == "draft"
                     and r.get("data", {}).get("draft_id")}
    if (final_drafts - base_drafts) != logged_drafts:
        out.append(_f("draft_id_mismatch", FAIL,
                      "logged draft ids != new drafts in state",
                      f"logged {sorted(logged_drafts)} vs new {sorted(final_drafts - base_drafts)}"))
    return out


def all_findings(recs, root):
    out = []
    for fn in (check_seq_monotonic, check_cycle_monotonic, check_run_start,
               check_search, check_ingest, check_graph, check_process,
               check_integrity_per_cycle, check_replay_ordering,
               check_recompute, check_work_after_goal, check_completeness):
        out += fn(recs)
    return out


def _compute(root, run_id, path, use_gotchas):
    p = Path(path) if path else Path(root) / ".research" / "run.jsonl"
    lines = p.read_text(encoding="utf-8").splitlines() if p.exists() else []
    recs, findings = parse_recs(lines)
    run = select_run(recs, run_id)
    findings += all_findings(run, root)
    starts = [r for r in recs if r.get("step") == "run_start"]
    latest_id = starts[-1]["run_id"] if starts else None
    is_latest = bool(run) and run[0].get("run_id") == latest_id
    if is_latest:
        findings += check_consistency(run, root)
    notes = {}
    if use_gotchas:
        reg = gotchas_mod.load_registry(root)
        for fnd in findings:
            entry, is_new = gotchas_mod.record(reg, {**fnd, "severity": fnd["severity"].lower()})
            notes[id(fnd)] = (f"[NEW {entry['id']} — capture in gotchas.jsonl]" if is_new
                              else f"[KNOWN {entry['id']}: {entry['fix']}]")
        gotchas_mod.save_registry(reg, root)
    code = 1 if any(f["severity"] == FAIL for f in findings) else 0
    return run, findings, notes, code


def verify(root=".", run_id=None, path=None, use_gotchas=True):
    _run, findings, _notes, code = _compute(root, run_id, path, use_gotchas)
    return findings, code


def _render(run, findings, notes):
    lines = []
    bycyc = _by_cycle(run)
    rid = run[0]["run_id"] if run else "(none)"
    lines.append(f"Run {rid}: {len(run)} records")
    for cyc in sorted(bycyc):
        lines.append(f"  cycle {cyc}:")
        for r in bycyc[cyc]:
            lines.append(f"    [{r.get('seq')}] {r.get('flow')}/{r.get('step')} {r.get('status')}")
    fails = sum(1 for f in findings if f["severity"] == FAIL)
    warns = sum(1 for f in findings if f["severity"] == WARN)
    lines.append(f"FINDINGS: {fails} FAIL, {warns} WARN")
    for f in findings:
        note = notes.get(id(f), "")
        lines.append(f"  {f['severity']} {f['check']} (seq {f['seq']}): {f['detail']} {note}")
    return "\n".join(lines)


def _main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--path", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-gotchas", action="store_true")
    args = ap.parse_args(argv)
    run, findings, notes, code = _compute(args.root, args.run_id, args.path, not args.no_gotchas)
    if args.json:
        print(json.dumps({"run_id": run[0]["run_id"] if run else None,
                          "exit": code, "findings": findings}, ensure_ascii=False))
    else:
        print(_render(run, findings, notes))
    return code


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
