# Engine Quirk Cleanup — kill the re-learn tax

**Status:** proposed, pre-implementation
**Date:** 2026-06-30
**Trigger:** External agents repeatedly re-derive five engine "quirks" and re-invent
workarounds each run. Goal: make each quirk self-evident at the point an agent meets it,
so it is never re-identified.
**Verified against:** `scripts/orchestrator.py`, `scripts/state.py`, `scripts/junk.py`,
`scripts/gotchas.py`, `bin/ors`, `skills/_flows/loop.md`, `skills/_flows/process.md`,
`skills/dashboard/SKILL.md`, `docs/adr/0007-*`,
`docs/superpowers/specs/2026-06-20-loop-engine-convergence-design.md`.

---

## Cross-check (per planning policy)

| Quirk | Reality after reading code | Reclassified as |
|-------|----------------------------|-----------------|
| 1 `goal_met` never flips on inline review | True behavior; `goal_met` *requires* ≥1 draft in `status="draft"` (`orchestrator.py` `goal_met`). Documented in convergence spec §2 but not at point of use. | **By-design, under-surfaced** |
| 2 process needs ≥3 uncited; 1–2 stranded | Exact (`state.py` `process_candidates`, `n >= min_sources`). **Already an accepted decision** in ADR 0007. | **Already documented; agent hadn't read ADR** |
| 3 no drop verb; junk blocks convergence | Confirmed — no `remove-corpus`/`drop`/`purge` verb in `state.py` CLI; `junk.py` only detects. Uncited junk keeps `_processable` True forever. | **Genuine code gap** |
| 4 cwd-drift writes wrong `.research/` | Real footgun: `state.py --root` defaults to `"."` (cwd-relative); `bin/ors:7` bakes `REPO_ROOT="${REPO_ROOT:-$PWD}"`. Flows themselves guard via absolute `ROOT`. | **Genuine footgun, not engine-logic bug** |
| 5 dual graph (`graphify-out` 850 vs repo-root 1023) | **False in tree.** One graph: `.graphify/graph.json` (2487 nodes, 2804 links). No `.research/docs/graphify-out/`, no repo-root `graph.json`. `loop.md`, `process.md`, `dashboard/SKILL.md:15` all point at `.graphify/graph.json`. | **Phantom — record so it is not re-chased** |

**Discrepancies vs the original quirk note:** #1 states the `goal_met` precondition backwards
(note says "pending=0 ⇒ gather"; truth is `goal_met` *needs* pending≥1). #2 is not a quirk,
it is ADR 0007. #5 does not reproduce. Plan reflects corrected reality, not the note.

---

## Principle

Put the truth where the agent already looks: **the function's docstring** (point of use),
**an ADR** (the decision), **`loop.md`/`process.md`** (the running entry point). Add code
only for the two genuine gaps (#3, #4). No new registry — the repo's channels suffice.

---

## Phase 1 — Code (genuine gaps #3, #4)

### 1.1 `remove-corpus` verb — `scripts/state.py`  *(quirk 3)*
Primitive to purge a corpus entry, mirroring existing verb style.

- `remove_corpus_entry(state, cid, *, force=False)`: refuse (raise) if `cid ∈ _cited_ids(state)`
  unless `force`; drop the entry from `state["corpus"]`; set `graph.dirty = True`; return the
  removed entry (or `None` if absent).
- CLI: `remove-corpus --root --id [--force] [--purge-files]`. Default prints removed id +
  its `native_path`/`extracted_path` for the caller to delete. `--purge-files` unlinks both
  paths (best-effort, ignore-missing). Backup is the caller's job (git); the verb refuses to
  delete a cited source — that is the "assert none are cited" guard, enforced in code.
- **Test** `tests/test_state.py`: add → remove uncited (gone, graph dirty); cite then remove
  (raises without `--force`, succeeds with it); `--purge-files` unlinks.

> Deliberately **not** building an `ors junk-sweep` auto-purge now. The verb is the primitive;
> a sweep over `junk.is_junk(extracted)` for uncited entries can wrap it later if the manual
> path proves too slow. `// ponytail: primitive only — sweep when manual purge measurably hurts`.

### 1.2 `--root` drift guard — `scripts/state.py`  *(quirk 4)*
Stop a drifted cwd from creating a nested `.research/`.

- In `state_path()`/`lock_path()` (and the `load()` create path), resolve root precedence:
  explicit `--root` if absolute → use it; else if `$REPO_ROOT` set → resolve `--root` against it;
  else `Path(root).resolve()` against cwd **and** emit one stderr line
  `note: resolving relative --root '<r>' against cwd '<cwd>'`.
- **Guard the reported incident:** in `load()`, before *creating* a fresh seed state, if
  `$REPO_ROOT` is set and the resolved root is **not** under it, fail with
  `refusing to seed .research/ outside REPO_ROOT (<root> ⊄ <REPO_ROOT>)` instead of silently
  writing a nested ledger. (Reads of an existing state are unaffected.)
- **Test** `tests/test_state.py`: relative root + `REPO_ROOT` set from a foreign cwd lands the
  ledger under `REPO_ROOT`, not cwd; seeding outside `REPO_ROOT` raises.

---

## Phase 2 — Truth at point of use (by-design #1, #2, #5)

### 2.1 Docstrings — `scripts/orchestrator.py`, `scripts/state.py`
One line each, stating the non-obvious invariant (WHY), no change narrative:

- `goal_met`: `"""True only while a finished draft still waits (status='draft') and nothing
  else is processable — a 'ready for human adjudication' signal, NOT 'done'. Adjudicating the
  last draft clears it by design (see ADR 0008)."""`
- `process_candidates`: `"""Topics with >= min_sources UN-cited corpus entries, queue-depth
  ranked. Topics with 1-2 uncited are intentionally not surfaced (ADR 0007)."""`
- `recommend_phase`: note that the `processable` disjunct makes `synthesize` reachable with no
  draft, and that `goal_met` narrows it.

### 2.2 ADR 0008 — `docs/adr/0008-goal-met-is-ready-not-done.md`  *(quirk 1)*
Codify, in the established ADR format: `goal_met` = ready-for-adjudication; promotion is a human
gate (per convergence spec §2 "done-check cannot require promoted findings"); real convergence =
no queued gaps + not processable + drafts adjudicated; **do not poll the flag while adjudicating
inline.** Cross-link the convergence spec and ADR 0007.

### 2.3 `loop.md` / `process.md` — "Convergence & footguns" pointer
A short block at the human/agent entry point linking ADR 0007 + 0008 and stating the three
durable facts:
- `goal_met` is ready-not-done; convergence is "work drained + drafts adjudicated."
- 1–2-source topics are stranded by design — drain by hand if wanted.
- **One graph only:** `.graphify/graph.json`. No `graphify-out`, no repo-root `graph.json`.
  *(quirk 5 — kills the phantom dual-graph hunt.)*

---

## Phase 3 — Regression lock

- `tests/test_orchestrator.py`: assert `goal_met` True with a pending draft + nothing
  processable; assert it goes False the instant that draft is promoted/rejected (encodes the
  ADR-0008 invariant so a future refactor cannot silently turn it into a done-flag).
- `tests/test_no_legacy_paths.sh` (already exists): extend to assert no source references a
  repo-root `graph.json` or `graphify-out` path, so quirk 5 can never re-emerge as a real
  mismatch.
- `CHANGELOG.md`: one line under a new entry — "remove-corpus verb; --root drift guard;
  goal_met semantics (ADR 0008)."

---

## Decisions to confirm (defaults chosen, override if wrong)

1. **`remove-corpus` deletes files?** Default: only with `--purge-files`; otherwise prints paths.
   (Keeps the verb a state primitive, leaves file deletion explicit.)
2. **Strict `--root`?** Default: refuse to *seed* outside `REPO_ROOT`, but still *read* any root.
   (Prevents nested-`.research/` without breaking existing flows.)
3. **Auto junk-sweep?** Default: not now — ship the verb only.

---

## Out of scope
- Changing the ≥3 threshold (ADR 0007 stands).
- Re-architecting `goal_met` (it is correct; only its meaning needs surfacing).
- Any dual-graph reconciliation (there is no second graph).
