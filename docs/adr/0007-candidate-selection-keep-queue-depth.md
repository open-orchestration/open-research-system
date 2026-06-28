---
status: rejected
date: 2026-06-27
---

# 0007 — Keep queue-depth candidate selection; decline BM25/PMI

## Context and Problem Statement

A proposed upgrade would ground source/candidate ranking in BM25 + probabilistic idf
(`d0fefa5d5`) and PMI/PPMI term-weighting (`d7289dbd9`), on the assumption that
`state.py candidates` ranks naively. The premise was checked against the code.

## Decision

**Declined.** `process_candidates` (`scripts/state.py`) ranks *topics* by the count of
un-cited corpus sources, descending — a deterministic work-queue depth, not a relevance
ranking. No source-relevance ranking exists anywhere in `scripts/`. BM25 and PMI rank
*documents by query relevance*; there is no query and no relevance axis here, only "which
topic still has the most pending sources to process." Replacing a correct queue-depth counter
with BM25 would not be an upgrade — it would answer a question the engine does not ask.

## Consequences

- `candidates` stays as-is; no dependency or scoring code added for a problem that does not exist
  (YAGNI).
- The BM25/PMI findings remain available if a *future* feature introduces genuine source-relevance
  ranking (e.g. ranking candidate primaries within a topic against a gap query) — at which point
  this record would be superseded.
