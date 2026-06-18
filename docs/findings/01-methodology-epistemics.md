# Findings — Research Methodology & Epistemics

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- A protocol must be written and registered *before* the evidence is examined, so eligibility criteria, comparisons, and outcomes are pre-specified independent of findings — this is the primary mechanism for minimizing reviewer bias. — [Chapter 1: Starting a review - Cochrane](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-01)
- Publishing the protocol up front "reduces the impact of review authors' biases, promotes transparency of methods, reduces the potential for duplication, and allows peer review of the planned methods before they have been completed." — [Chapter 1: Starting a review - Cochrane](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-01)
- PRISMA 2020 standardizes reporting through a fixed checklist plus a flow diagram that records identification → screening → inclusion counts, making the search-and-selection process auditable and reproducible. — [PRISMA statement](https://www.prisma-statement.org/)
- Trustworthiness of an individual source should be judged through an explicit, multi-domain rubric rather than a global impression: Cochrane's INSPECT-SR runs up to 21 checks across four domains (post-publication notices/study conduct, governance & transparency, text & figures, study results) before an overall trustworthiness judgement. — [Methods in Cochrane](https://www.cochrane.org/authors/methods-cochrane)
- Synthesis questions themselves should be specified before synthesis — the InSynQ checklist (11 items) forces explicit grouping of interventions, populations, outcomes and comparisons so the synthesis is structured, not improvised. — [Methods in Cochrane](https://www.cochrane.org/authors/methods-cochrane)
- Confidence in the *body* of evidence is a separate, gradable judgement from the validity of any one study; GRADE / GRADE-CERQual provide a tiered certainty rating that travels with each synthesized finding. — [Methods in Cochrane](https://www.cochrane.org/authors/methods-cochrane)
- Critical appraisal of a completed review is itself a defined activity with its own guidance, distinct from conducting the review — appraisal and production are separate competencies. — [Appraising systematic reviews: a comprehensive guide](https://pmc.ncbi.nlm.nih.gov/articles/PMC10764628/)

## Convergent vs contested
- **Convergent:** Pre-registration of method, transparent and reproducible search/selection reporting (PRISMA flow), per-source bias appraisal with explicit domain rubrics, and a separate certainty grade for each synthesized conclusion. Sources agree the value is *process discipline*, not any single statistic.
- **Contested / open:** Newer trustworthiness tools (INSPECT-SR, CAMELOT) are endorsed as *optional* and several are still preprints — Cochrane itself flags that authors should record the access date because guidance is unsettled. The right rigor level for fast, non-clinical research is undefined here.

## Implications for the system (Phase 2)
- Make the research run *protocol-first*: generate and freeze a machine-readable plan (question, inclusion/exclusion criteria, sub-questions, target source types) before any retrieval, and diff actual behavior against it.
- Emit a PRISMA-style provenance trail per run: how many sources were found, screened, kept, and rejected (with reasons) — this is the system's auditability surface.
- Score each source with an explicit multi-domain credibility rubric (provenance, transparency, recency, corroboration) rather than a single trust score, and attach a per-claim certainty grade to synthesized output.

## Gaps found → re-scan
- Sources are clinical/Cochrane-centric. Missing: epistemics of *web/grey-literature* credibility, source-triangulation heuristics, and how to map systematic-review rigor onto fast LLM research. Deep-dive query: "source triangulation and credibility scoring for web and grey literature in automated research" and "lightweight evidence-grading rubrics for non-clinical synthesis".
