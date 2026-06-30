# Decision log

The collection of ADRs in this directory constitutes the engine's **decision log** —
the record of each *process* change made to the research engine, one decision plus its
rationale per file. Format and lineage are grounded in the corpus's own findings:
the MADR field schema (`decf6989c`) and Nygard's original five-section template plus the
`adr-tools` numbered-file + supersede convention (`d657c1d86`). Recording the engine's
self-improvement as ADRs **dogfoods the corpus** — the engine documents its own decisions
using the format it researched and promoted.

Each record uses the lean MADR-lite shape: YAML frontmatter (`status`, `date`) over the
core sections — Context and Problem Statement, Decision, Consequences. Files are numbered
`NNNN-kebab-title.md`; `status` is one of `accepted`, `rejected`, `deprecated`, or
`superseded by ADR-NNNN`.

| ADR | Decision | Status | Grounds |
| --- | --- | --- | --- |
| [0001](0001-adopt-adr-decision-log.md) | Adopt an ADR decision log for process changes | accepted | decf6989c, d657c1d86 |
| [0002](0002-review-gate-grade-llm-judge.md) | Ground the review gate in GRADE certainty + LLM-judge debiasing | accepted | d628b3d0f, dc577f3e2, d4c45dd7e |
| [0003](0003-promotion-as-streaming-multiple-testing.md) | Frame promotion as a streaming multiple-testing problem | accepted | d42ec736c, dc588b7cc |
| [0004](0004-drafting-faithfulness-selfcheck-factscore.md) | Ground the drafting faithfulness self-check in FActScore atomic decomposition | accepted | d1ad78766, dfa42bc8a |
| [0005](0005-drafting-chain-of-draft-prompting-ladder.md) | Ground drafting reasoning in Chain-of-Draft + the prompting ladder | accepted | d6432467b, d0b1fc5c6 |
| [0006](0006-citation-export-csl-json.md) | Export the corpus as CSL-JSON for interchangeable provenance | accepted | d59d1279b, de47719c4 |
| [0007](0007-candidate-selection-keep-queue-depth.md) | Keep queue-depth candidate selection; decline BM25/PMI | rejected | d0fefa5d5, d7289dbd9 |
| [0008](0008-goal-met-is-ready-not-done.md) | `goal_met` is "ready for adjudication", not "done" | accepted | convergence-design §2 |
