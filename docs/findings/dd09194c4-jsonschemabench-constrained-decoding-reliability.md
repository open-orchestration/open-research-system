---
id: dd09194c4
topic: 16-evaluation-benchmarks
title: "JSONSchemaBench: constrained decoding is not a uniform capability — frameworks differ ~2x in real-world schema support, yet constrained decoding helps downstream quality (up to 4%)"
status: draft
---

# JSONSchemaBench: constrained decoding is not a uniform capability — frameworks differ ~2x in real-world schema support, yet constrained decoding helps downstream quality (up to 4%)

Constrained decoding has become the dominant technology for forcing language models to emit structured output, and the industry has standardized that interface around **JSON Schema** [c4f5787db]. But until this work its real-world effectiveness was poorly characterized: the *mechanism* was understood without the *reliability* being measured. This finding grounds **JSONSchemaBench** — an evaluation framework plus benchmark that asks, empirically and across competing implementations, *does constrained decoding actually work, and which framework, and at what cost?* It is the reliability-evaluation layer that sits on top of the method finding [d270b0177], which grounds *how* constrained decoding works (regex/grammar → finite-state index, per-step token masking) but does not measure whether real frameworks deliver it on real schemas. The load-bearing thesis here is that constrained decoding is **not** a solved, uniform capability: frameworks diverge by roughly 2x in how many real-world schemas they support, there is a permissiveness/coverage trade-off, and — reassuringly — constraining the decoder tends to *improve* downstream task quality rather than degrade it.

## What JSONSchemaBench measures, and on what corpus

JSONSchemaBench is a collection of **10K real-world JSON schemas** drawn from multiple sources and organized into 10 datasets of varying complexity and diversity, spanning domains such as function signatures, service APIs, and system configurations [c4f5787db]. The sources named in the paper include the **JSON Schema Store** (described as the largest collection of independent JSON schemas), the **GlaiveAI function-calling dataset V2** (function-signature schemas), and **Kubernetes configuration files** (schemas with intricate hierarchical structure) [c4f5787db]. The real-world schema set is paired with the **official JSON Schema Test Suite**, which the benchmark uses to extract feature-level coverage insights [c4f5787db]. Schemas were validated against the Draft 2020-12 specification and cleaned (deduplicated, empty schemas dropped, unresolved external `$ref`s removed) before inclusion [c4f5787db].

The evaluation is explicitly **three-dimensional**, framed as three persistent questions [c4f5787db]:

- **Efficiency (Q1):** does constrained decoding slow down or speed up generation, and which framework is most efficient?
- **Coverage (Q2):** how well do frameworks support the evolving, expansive JSON Schema feature set?
- **Quality (Q3):** does constraining the output negatively affect the *semantic* quality of what the model produces?

To make coverage measurable the authors define three notions: **declared coverage** (the framework processes the schema without rejecting it or crashing), **empirical coverage** (experiments confirm valid instances are generated), and **compliance rate** [c4f5787db].

## Six frameworks, and how they diverge on coverage

The paper evaluates **six state-of-the-art** constrained-decoding frameworks: **Guidance, Outlines, Llama.cpp, XGrammar, OpenAI, and Gemini** [c4f5787db]. The central coverage result is that they are far from interchangeable — "**Single Highest: Guidance has the single highest coverage in 19 categories, followed by XGrammar with 10, and Outlines with one, and Llamacpp with none**" on the JSON Schema Test Suite [c4f5787db]. The headline cross-framework spread is the same point stated at the schema level: frameworks "demonstrate significant differences in their actual support for real-world JSON schemas, with the **best framework supporting twice as many schemas as the worst**" [c4f5787db].

This is the contribution that the method paper [d270b0177] cannot make. [d270b0177] establishes that constrained decoding is *constructively sound* — invalid tokens are masked by construction via a finite-state index — but soundness of the method says nothing about how completely a given implementation translates the JSON Schema feature set into those constraints. JSONSchemaBench measures exactly that gap, and finds it large.

## The permissiveness vs. coverage trade-off

Higher raw coverage is not automatically a virtue: the way a framework *fails* matters. The benchmark distinguishes two failure modes beyond outright compilation errors — **over-constrained** (the engine rejects JSON instances that are valid under the schema, i.e. too strict) and **under-constrained** (the engine permits JSON instances that are invalid under the schema, i.e. too permissive) [c4f5787db]. Against these, "**XGrammar minimizes compilation errors but shows the highest number of under-constrained failures, indicating a trade-off favoring permissiveness**" [c4f5787db]. In other words, a framework can buy apparent coverage by being lax about enforcement — accepting schemas it does not actually constrain correctly — and that permissiveness is itself a correctness liability, not just a quality. Guidance, by contrast, demonstrates the fewest total failures and in particular minimizes under-constrained errors [c4f5787db]. This reframes "which framework has the most coverage" into "which framework enforces the constraint it claims to enforce."

## Does constraining the decoder hurt output quality? No — it helps

The most counterintuitive and reassuring result concerns Q3. A natural fear is that forcing the decoder to stay inside a structural grammar degrades the *content* of what the model writes. The paper finds the opposite: "**Constrained decoding consistently improves the performance of downstream tasks up to 4%, even for tasks with minimal structure like GSM8k**" [c4f5787db]. Stated carefully as the paper's own finding: constrained decoding does not degrade downstream task quality and tends to improve it, by *up to* 4% across the tasks measured — it is an upper-bound improvement figure, not a guaranteed flat +4% on every task [c4f5787db]. The efficiency side carries a complementary positive: constrained decoding "can speed up the generation process by 50% compared to unconstrained decoding" [c4f5787db]. Together these undercut the assumption that structural guarantees come at a cost in either speed or semantic quality.

## Author-stated caveats

The authors are explicit that the picture is not tidy. Test-suite performance is not a clean proxy for real-world behavior: there is "**no straightforward correspondence between test suite performance and empirical [coverage]**" [c4f5787db]. And the benchmark as a whole "presents a **significant challenge** for both LLMs and constrained decoding frameworks, highlighting ample room for improvement and exposing gaps in the existing solutions" [c4f5787db]. The benchmark is released at github.com/**guidance-ai/jsonschemabench** [c4f5787db].

## How this complements the Outlines method finding [d270b0177]

[d270b0177] grounds the *mechanism*: generation reformulated as transitions over a finite-state machine, with an index supplying an O(1) per-step token mask, extended to context-free grammars and data formats (JSON, Python, SQL) via pushdown automata. That finding answers "how is structured output guaranteed by construction?" This finding answers the orthogonal, empirical questions the method paper does not touch: across competing production frameworks, *how much* of the real JSON Schema feature surface is actually supported, *how* they fail, and *what it costs* in speed and downstream accuracy. The two are stacked, not redundant: a sound masking mechanism [d270b0177] is necessary but not sufficient, and JSONSchemaBench shows that implementations of that mechanism vary by ~2x in real-world support [c4f5787db].

## Gaps found

- **Per-framework efficiency/latency numbers are not reported here.** The source's efficiency tables (GCT — grammar compilation time, TTFT — time to first token, TPOT — time per output token) are garbled by the PDF→markdown conversion (whitespace-collapsed), so specific per-framework latency figures are not extracted; only the prose-level "up to 50% speedup" claim and the relative ordering (e.g. Guidance achieving high efficiency via fast-forwarding / guidance acceleration) are confirmable [c4f5787db]. The exact per-dataset coverage and compliance-rate cells (Table 4 / Table 12) are likewise garbled and not quoted as numbers.
- **This benchmarks behavior, not compilation mechanics.** The schema-keyword → regex → FSM/grammar *compilation algorithm* — the step that turns a specific JSON Schema keyword into the automaton [d270b0177] masks against — remains ungrounded in this corpus (residual gap g3460ddda). JSONSchemaBench measures what frameworks *do*, not the internal algorithm by which a schema becomes constraints.
- **Compliance-rate definition is named but its full formal statement is not extracted** verbatim here beyond the declared/empirical/compliance triad [c4f5787db]; the precise numeric ratios per dataset live in the garbled tables.
