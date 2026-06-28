---
status: accepted
date: 2026-06-27
---

# 0005 — Ground drafting reasoning in Chain-of-Draft + the prompting ladder

## Context and Problem Statement

`process.md` step 3 required every claim to carry a citation but said nothing about *how* to
reason while drafting, leaving room for verbose, low-density chain-of-thought narration in the
finding body. The corpus holds the grounded alternatives: Chain-of-Draft generates minimal,
informative reasoning steps that match chain-of-thought accuracy at a fraction of the tokens
(`d6432467b`), and the prompting ladder shows added reasoning is emergent-at-scale and
cost-incurring, to escalate only when it pays (`d0b1fc5c6`).

## Decision

Add a reasoning directive to step 3: draft citation-dense in Chain-of-Draft style — the body is
evidence and its citations, not a deliberation transcript — and escalate reasoning depth only on
a genuinely contested or multi-source claim.

## Consequences

- Finding bodies stay dense and auditable; every sentence states or connects cited facts.
- Reasoning cost scales with claim difficulty, not by default — cheaper drafts, same rigor.
