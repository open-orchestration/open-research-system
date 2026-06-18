# Findings — Decision-Making Frameworks

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- An Architectural Decision Record captures a *single* justified design choice plus its underlying rationale; MADR is a lean, structured Markdown template for recording such decisions so the "why" survives. — [Markdown Architectural Decision Records - MADR](https://adr.github.io/madr/)
- The core, non-negotiable parts of a decision record are **context**, **decision**, and **consequences**; supplemental parts are **status**, **decision drivers**, **options with pros and cons**, and **more information** — most of the value is in recording the *considered options* with their tradeoffs. — [The Markdown ADR (MADR) Template Explained and Distilled](https://www.ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html)
- "We think that the considered options with their pros and cons are crucial to understand the reasons for choosing a particular design" — the rejected alternatives are first-class content, not an afterthought. — [ADR Templates | Architectural Decision Records](https://adr.github.io/adr-templates/)
- MADR scales to decision size: a record can be a terse "context + options + outcome" or a fuller form, and "there is no formal definition of short, medium-sized, and large decision records" — the template flexes to the weight of the decision. — [madr/docs/examples.md](https://github.com/adr/madr/blob/develop/docs/examples.md)
- A compact decision can be expressed in one canonical sentence: "In the context of `<use case>`, facing `<concern>`, we decided for `<option>` and neglected `<other options>`, to achieve `<desired consequences>`, accepting `<downsides>`, because `<rationale>`." — [ADR Templates | Architectural Decision Records](https://adr.github.io/adr-templates/)
- Records carry an explicit **status** (e.g. proposed/accepted) and optional metadata such as decision-makers and a confirmation section, so a decision's lifecycle and authority are tracked. — [The Markdown ADR (MADR) Template Explained and Distilled](https://www.ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html)
- MADR deliberately broadened from "Markdown *Architectural* Decision Records" to "Markdown *Any* Decision Records" — the same structure is meant to capture any significant decision, not only architecture. — [Markdown Architectural Decision Records - MADR](https://adr.github.io/madr/)

## Convergent vs contested
- **Convergent:** Every source agrees the record's job is to preserve rationale and the rejected options; that context/decision/consequences are the irreducible core; and that the format must be lightweight, plain-Markdown, and version-control-friendly (no special tooling — "use any text editor").
- **Contested / open:** How much structure to mandate. v3 added optional metadata and a "Confirmation" section, then merged positive/negative consequences into one "Consequences" section to ease copy-paste — there is ongoing tension between completeness and friction. The sources are entirely MADR/ADR; ACH and decision-matrix scoring (named in the search) are absent.

## Implications for the system (Phase 2)
- Have the research system emit decision records for its own non-obvious choices (scope cuts, source-trust thresholds, conflicting-evidence resolutions) using the MADR core: context → considered options w/ pros-cons → decision → consequences → status. This makes the agent's reasoning auditable and re-litigable.
- Treat the rejected alternatives as required output, not optional — when the system picks among competing hypotheses or sources, record what it discarded and why.
- Use the one-sentence canonical form as a cheap default for minor decisions, escalating to the full template only for high-weight ones (the format flexes to decision size).

## Gaps found → re-scan
- All five sources are MADR/ADR; the catalog title also implies **decision-matrix analysis** and **Analysis of Competing Hypotheses (ACH)**, which were not gathered. Deep-dive queries: "Analysis of Competing Hypotheses ACH method structured intelligence analysis" and "weighted decision matrix / Pugh matrix scoring for comparing options".
