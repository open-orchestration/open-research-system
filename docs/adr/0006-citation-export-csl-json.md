---
status: accepted
date: 2026-06-27
---

# 0006 — Export the corpus as CSL-JSON for interchangeable provenance

## Context and Problem Statement

The engine's provenance was internally consistent (`cite_check.py` validates `c…` ids against
the corpus) but not *interchangeable* — it could not be handed to any standard citation tool.
The corpus holds the interchange formats: CSL-JSON fixes a closed 45-item-type enum and requires
exactly `type` + `id` per item (`d59d1279b`), and biblatex's web-native types (@online,
@dataset, @software) model the source kinds a research engine actually cites (`de47719c4`).

## Decision

Add `scripts/export_csl.py`, mapping each corpus entry to a CSL-JSON item (arxiv→article-journal,
http→webpage, file://→document), validating every emitted item against the closed enum and the
two required fields before printing. CSL-JSON over biblatex because its two-required-field minimum
maps cleanly onto every corpus entry with no synthesized fields.

## Consequences

- The corpus is now exportable to any CSL-consuming tool; provenance is portable, not just valid.
- A runnable `--selfcheck` guards the type-mapping; the validation gate is grounded in the format
  spec itself.
- Import (CSL-JSON → corpus) and a biblatex emitter remain available as follow-ups if a consumer
  needs them; not built speculatively.
