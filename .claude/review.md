<!-- .claude/review.md -->

# Review gate — independent reviewer

Automated promotion gate. An **independent** reviewer (a fresh subagent, never the
agent that wrote the draft) judges a finished draft and the engine promotes or rejects it
without a human. The gate is **conservative and binary**: promote only a draft that is
clearly canon-worthy; otherwise reject (rejecting frees its cited sources for a stronger
redraft).

Run this on one draft id `D`, or loop it over every queued draft
(`python3 scripts/promote.py queue` lists them). For each `D`, do exactly this:

1. **Resolve the draft and its cited sources** (the reviewer must read the sources, not the
   draft's word for it):
   ```
   python3 - "$D" <<'PY'
   import json, sys
   s = json.load(open(".research/state.json"))
   d = next((x for x in s["drafts"] if x["id"] == sys.argv[1]), None)
   assert d, "unknown draft"
   cmap = {e["id"]: e for e in s["corpus"]}
   print("PATH", d["path"])
   for cid in d["cites"]:
       e = cmap.get(cid)
       print("CITE", cid, e["extracted_path"] if e else "MISSING", "|", (e or {}).get("source",""))
   PY
   ```

2. **Dispatch a fresh `general-purpose` reviewer subagent.** It MUST be a new subagent —
   not your own context — so the review is independent of the drafting. Give it: the draft
   file path, the list of `(corpus_id, source_path, source_url)` triples from step 1, and
   this rubric verbatim. Do not tell it which way to lean.

   > You are an independent reviewer deciding whether a machine-written research draft is
   > trustworthy enough to enter a permanent source-of-truth. You did not write it. Read the
   > draft at DRAFT_PATH, then read each cited source file. Judge three things:
   > 1. **Faithfulness** — for each `[c<id>]` claim, does the cited source file actually
   >    support it (not merely exist)? Flag any claim the source does not bear out.
   > 2. **Source provenance** — are the cited sources trustworthy (primary papers, official
   >    docs, reputable engineering writing) or promotional/secondary (vendor marketing,
   >    listicles, SEO blogs)? Load-bearing claims resting on promotional sources are a
   >    reject reason.
   > 3. **Canon-worthiness** — is the finding coherent, non-trivial, and useful as a
   >    durable reference, or thin/redundant?
   > Default to **reject**. Promote only if all three are clearly satisfied. Return your
   > verdict as the LAST line, exactly `VERDICT: promote` or `VERDICT: reject`, preceded by
   > 2–4 lines of specific reasons (name the failing claim or source).

3. **Act on the verdict** (parse the subagent's last `VERDICT:` line):
   - `promote` → `python3 scripts/promote.py promote "$D"`
   - `reject`  → `python3 scripts/promote.py reject "$D" --reason "ai-independent: <the reviewer's reasons, one line>"`
   - If no clear `VERDICT:` line is returned, treat it as **reject** (conservative default).
   Then log it:
   ```
   python3 scripts/runlog.py log --flow process --step review --status ok \
     --data "{\"draft_id\":\"$D\",\"decision\":\"<promote|reject>\",\"reviewer\":\"ai-independent\"}"
   ```

4. **Integrity:** after acting, run `python3 scripts/check_integrity.py`; if it reports
   problems, surface them and stop.

The reviewer's authority is real — a `promote` moves the draft into `docs/findings/` and
appends it to `SYNTHESIS.md`; a `reject` frees its sources. A human can still override after
the fact (`promote.py promote/reject` by hand).
