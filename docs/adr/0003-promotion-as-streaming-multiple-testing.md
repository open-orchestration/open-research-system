---
status: accepted
date: 2026-06-27
---

# 0003 — Frame promotion as a streaming multiple-testing problem

## Context and Problem Statement

Each draft is independently "tested" for promotion, and the corpus has run that test 60+
times. Treating every promote as an isolated decision ignores the corpus-wide
false-promotion rate. The corpus names the discipline: a single peeked-at-stopping-time
decision is an always-valid sequential test (`dc588b7cc`), and across a stream the right
target is mFDR control via an online-FDR/alpha-investing scheme (`d42ec736c`).

## Decision

Document in `.claude/review.md` that a promote is the rejection of the null "this draft is
not canon-worthy," so each promote is a discovery contributing to a family-wide error rate.
The conservative defaults (default-reject, higher synthesis bar, GRADE downgrades) act as a
qualitative α-budget; the `runlog.py` decision+certainty ledger is the append-only record
needed to measure the false-promotion rate.

## Consequences

- The gate now reasons about corpus-wide error, not just per-draft validity.
- A real quantitative α-budget (a debited wealth counter, an enforced mFDR bound) is left as a
  named, grounded upgrade (`d42ec736c`) — adopted only if a hard guarantee is ever needed.
