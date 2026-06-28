---
status: accepted
date: 2026-06-27
---

# 0001 — Adopt an ADR decision log for process changes

## Context and Problem Statement

The engine had begun upgrading its own process from its findings (review gate, drafting,
faithfulness check), but those decisions lived only in commit messages — there was no
single artifact recording *what changed, why, and at what cost*. The corpus contains the
grounded format for exactly this: an ADR "captures a single AD and its rationale" and "the
collection of ADRs … constitute its decision log" (`decf6989c`), and Nygard's originating
template plus `adr-tools` supply the numbering/supersede mechanics (`d657c1d86`).

## Decision

Maintain a decision log under `docs/adr/`, one MADR-lite record per process change, numbered
`NNNN-kebab-title.md`. Use the corpus's own promoted ADR format — dogfooding the conclusion
the engine researched and promoted rather than inventing a bespoke log.

## Consequences

- The engine's self-improvement is now auditable as a first-class artifact, not reconstructed
  from `git log`.
- Each future process change costs one short record; the discipline is cheap and the format is
  already grounded, so there is no new convention to invent.
- A reversed decision is recorded by setting `status: superseded by ADR-NNNN`, never by deleting
  history (`d657c1d86`).
