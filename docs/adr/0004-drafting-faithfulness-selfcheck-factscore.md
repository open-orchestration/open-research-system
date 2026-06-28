---
status: accepted
date: 2026-06-27
---

# 0004 — Ground the drafting faithfulness self-check in FActScore atomic decomposition

## Context and Problem Statement

`process.md` step 4's faithfulness self-check was informal — "check the draft is faithful"
with no method, so it could pass on a skim while an unsupported clause hid inside a vague
paragraph. The corpus holds the rigorous form: FActScore decomposes a generation into atomic
facts, scores each as supported/not against its source, and abstains rather than guesses
(`d1ad78766`); the faithfulness machinery checks per-claim entailment against the exact cited
bytes (`dfa42bc8a`).

## Decision

Rewrite step 4(b) as an explicit FActScore-style pass: decompose the draft into atomic
load-bearing claims, score each against the bytes it cites (whitespace-insensitive re-grep for
any number/formula/quote), and abstain — a number not in the bytes is not reported; a garbled
formula gets a canonical form + lossiness note, never a transcribed garble.

## Consequences

- The same atomic pass powers Workstream-1 definitive findings' self-verify step.
- The check is now reproducible across drafters and catches the synthesis failure mode (a claim
  true of one source asserted as general).
