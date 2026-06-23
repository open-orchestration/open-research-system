## [Intelligence notes](https://intelligencenotes.com/)
Search
Search
Dark modeLight mode
Reader mode
[◉Dashboard↗](https://intelligencenotes.com/static/dashboard/)⬡Graph
## Explorer
* [](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses)
◈INTELLIGENCE NODE // PIA·host » intelligencenotes.com·node » active · monitoring · secure·build » 2026-06-23·[◉ dashboard](https://intelligencenotes.com/static/dashboard/)
[Home](https://intelligencenotes.com/)
❯ 
[08 Guides & Manuals](https://intelligencenotes.com/08-Guides--and--Manuals/)
❯ 
[Analytical Frameworks](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/)
❯ 
[Analysis of Competing Hypotheses (ACH)](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses)
# Analysis of Competing Hypotheses (ACH)
Jun 17, 20266 min read
  * [framework](https://intelligencenotes.com/tags/framework)
  * [analysis](https://intelligencenotes.com/tags/analysis)
  * [ach](https://intelligencenotes.com/tags/ach)
  * [heuer](https://intelligencenotes.com/tags/heuer)
  * [structured-analytical-techniques](https://intelligencenotes.com/tags/structured-analytical-techniques)
  * [cognitive-bias](https://intelligencenotes.com/tags/cognitive-bias)
  * [tradecraft](https://intelligencenotes.com/tags/tradecraft)


# Analysis of Competing Hypotheses (ACH)[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#analysis-of-competing-hypotheses-ach)
## BLUF[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#bluf)
**Analysis of Competing Hypotheses (ACH)** is the structured analytical methodology developed by [Richards J. Heuer Jr](https://intelligencenotes.com/06-Authors--and--Thinkers/Doctrinal-Contributors/Richards-J.-Heuer-Jr) at the CIA in the 1970s–1980s and formalized in _Psychology of Intelligence Analysis_ (1999). It is the most robust operational countermeasure against the cognitive biases — confirmation bias, anchoring, satisficing, mirror imaging — that produce the majority of analytical failures. Where intuitive analysis seeks the most likely explanation and builds evidence for it, ACH starts from the full hypothesis space and systematically identifies which hypotheses the evidence most _diagnostically refutes_. The hypothesis with the least disconfirming evidence — not the most supporting evidence — is the most robust assessment. ACH is the operational discipline that transforms OSINT from information aggregation into intelligence production.
* * *
## The Eight Steps of ACH[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#the-eight-steps-of-ach)
### Step 1: Identify All Plausible Hypotheses[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-1-identify-all-plausible-hypotheses)
Brainstorm the complete set of possible explanations for the observed situation — including hypotheses that seem unlikely or politically uncomfortable. A hypothesis missed at this stage cannot be evaluated later.
**Discipline:** Generate hypotheses _before_ looking at evidence. Evidence-first hypothesis generation anchors on whatever is most salient in the current information, not on the structural possibilities.
**Example (2014 Crimea):**
  * H1: Russia will not use military force in Crimea
  * H2: Russia will conduct limited military pressure to extract political concessions
  * H3: Russia will seize Crimea through covert action with plausible deniability
  * H4: Russia will conduct overt military invasion of Crimea
  * H5: Russia will annex Crimea
  * H6: Russia will annex Crimea and then advance into eastern Ukraine


### Step 2: List the Evidence[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-2-list-the-evidence)
Compile all evidence, arguments, indicators, and assumptions relevant to each hypothesis. Include absence of evidence as evidence — if a particular hypothesis would predict specific observables that are not present, that absence is significant.
**Discipline:** Evidence must be treated atomically. “Russian forces are massing at the border” is multiple evidence items: the massing itself, the specific units involved, the timing, the public communications around the massing, the logistical patterns.
### Step 3: Build the Matrix[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-3-build-the-matrix)
Create a matrix: hypotheses as columns, evidence items as rows. For each cell, assess whether the evidence is:
  * **C** — Consistent with the hypothesis
  * **I** — Inconsistent with the hypothesis
  * **N/A** — Not applicable / irrelevant to the hypothesis
  * **?** — Ambiguous; could go either way

  
| Evidence  | H1  | H2  | H3  | H4  | H5  |  
| --- | --- | --- | --- | --- | --- |  
| Evidence item 1  | C  | C  | C  | I  | I  |  
| Evidence item 2  | I  | C  | C  | C  | C  |  
| Evidence item 3  | I  | I  | C  | C  | C  |  
### Step 4: Refine the Matrix[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-4-refine-the-matrix)
For each evidence item, assess its **diagnosticity** — how well does it discriminate between hypotheses? Evidence that is consistent with _all_ hypotheses has zero diagnostic value, no matter how strong it feels. Evidence that is consistent with exactly one hypothesis is maximally diagnostic.
**Example:** “Russian forces have deployed near the border” is consistent with H2, H3, H4, H5 — low diagnosticity. “Russian forces are wearing uniforms without insignia” is consistent with H3 but inconsistent with H4 — high diagnosticity.
Remove non-diagnostic evidence from the matrix. It clutters analysis without advancing it.
### Step 5: Identify the Hypothesis with the Fewest Inconsistencies[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-5-identify-the-hypothesis-with-the-fewest-inconsistencies)
Count the “I” (inconsistent) entries in each column. The hypothesis with the **fewest inconsistencies** is the most robust assessment — not the one with the most consistencies.
**The critical insight:** Evidence can be consistent with multiple hypotheses simultaneously, so “most supporting evidence” is not a discriminating metric. But a single piece of strong disconfirming evidence can eliminate a hypothesis entirely. Therefore, survivor-by-disconfirmation is the more powerful analytical move than winner-by-confirmation.
### Step 6: Examine Critical Assumptions[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-6-examine-critical-assumptions)
Identify which evidence items are most important to the analysis, and challenge the assumptions underlying their interpretation. If a single evidence item is driving the assessment, is that item reliably interpreted? Could it be deception? Could it mean something different than assumed?
This is the step where [maskirovka](https://intelligencenotes.com/02-Concepts--and--Tactics/21-Information--and--Cognitive-Warfare/Maskirovka) and active measures are explicitly considered — the possibility that some evidence was deliberately planted to mislead analysis.
### Step 7: Report Conclusions with Confidence and Sensitivity[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-7-report-conclusions-with-confidence-and-sensitivity)
State the assessment with explicit confidence calibration:
  * **High confidence:** Multiple independent strong-diagnostic evidence items converge on one hypothesis; few inconsistencies; low sensitivity to assumption changes
  * **Moderate confidence:** Single hypothesis clearly favored but with caveats or gaps
  * **Low confidence:** Multiple hypotheses remain plausible; evidence is ambiguous or sparse


Report the hypotheses that were _not_ selected, and what evidence would be needed to change the assessment.
### Step 8: Identify Indicators for Future Observation[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-8-identify-indicators-for-future-observation)
Define the observations that would confirm or disconfirm the current assessment. What, if it happens, would tell us we were wrong? Establishing these tripwires in advance prevents rationalization later.
* * *
## Why ACH Works[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#why-ach-works)
ACH is effective against specific cognitive biases:
**Confirmation bias:** By explicitly tracking inconsistent evidence, ACH forces attention to disconfirming information that intuitive analysis systematically underweights.
**Anchoring:** By generating hypotheses before looking at evidence, ACH prevents the initial impression from becoming the default conclusion.
**Satisficing:** By requiring evaluation of all hypotheses against all evidence, ACH prevents analysis from stopping at the first satisfactory explanation.
**Mirror imaging:** By forcing explicit articulation of adversary hypotheses, ACH makes cultural and ideological projection visible.
* * *
## ACH Limitations[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#ach-limitations)
ACH is not a panacea:
  * **Garbage in, garbage out:** If the hypothesis set is incomplete, or evidence is misinterpreted, the method produces wrong answers with high confidence
  * **Time cost:** Rigorous ACH takes hours per analytical question — unsustainable for high-volume tactical analysis
  * **Adversarial ACH:** A sophisticated adversary who knows ACH is being used can craft deception that is consistent with their preferred false hypothesis — exploiting the analyst’s methodology against them
  * **Organizational resistance:** ACH surfaces disagreements within analytical teams. Bureaucratic pressure to produce unified assessments can push analysts to abandon methodological rigor in favor of consensus


* * *
## Operational Use in This Vault[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#operational-use-in-this-vault)
Every analytical note in this vault — every BLUF, confidence rating, identified intelligence gap, and “Key Findings” section — implicitly applies ACH discipline. The explicit markers of ACH in the vault:
  * **“Confidence: High/Moderate/Low”** labels in analytical notes
  * **“Intelligence Gaps”** sections that identify what’s unknown
  * **“Alternative hypotheses”** or “What would change this assessment” sections
  * **Key Connections** that surface alternative interpretations


The [OSINT Manual](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Open-Source-Intelligence-Manual) operationalizes ACH specifically for the open-source domain.
* * *
## Key Connections[](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#key-connections)
  * [Richards J. Heuer Jr.](https://intelligencenotes.com/06-Authors--and--Thinkers/Doctrinal-Contributors/Richards-J.-Heuer-Jr) — originator of ACH
  * [Cognitive Biases in Intelligence Analysis](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Cognitive-Biases-in-Intelligence-Analysis) — the bias taxonomy ACH is designed to mitigate
  * [Structured Analytic Techniques (SATs)](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Structured-Analytic-Techniques) — the broader toolkit; ACH as one of the contrarian category
  * [Intelligence Confidence Levels](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Intelligence-Confidence-Levels) — the confidence calibration that ACH produces
  * [Open-Source Intelligence Manual](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Open-Source-Intelligence-Manual) — operational application
  * [LLM-Assisted OSINT SOP (A2IC)](https://intelligencenotes.com/08-Guides--and--Manuals/OSINT-Methodologies/LLM-OSINT-SOP-A2IC) — adversarial review (two-AI protocol) applies ACH logic
  * [Intelligence Cycle](https://intelligencenotes.com/02-Concepts--and--Tactics/22-Intelligence--and--OSINT/Intelligence-Cycle) — the Analysis phase where ACH operates
  * [Indications and Warning](https://intelligencenotes.com/02-Concepts--and--Tactics/22-Intelligence--and--OSINT/Indications-and-Warning) — I&W warning judgments require ACH to avoid premature closure
  * [Strategic Surprise](https://intelligencenotes.com/02-Concepts--and--Tactics/25-Geopolitics--and--IR-Theory/Strategic-Surprise) — what happens when ACH discipline is missing
  * [Maskirovka](https://intelligencenotes.com/02-Concepts--and--Tactics/21-Information--and--Cognitive-Warfare/Maskirovka) — adversarial countermeasures against analytical methodology
  * [Field Manual Part 05 — Analysis Without Institutional Support](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/05-%E2%80%94-Analysis-Without-Institutional-Support) — solo SAT discipline for practitioners without peer review
  * [Field Manual Part 06 — Adversarial Review Without a Peer Team](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/06-%E2%80%94-Adversarial-Review-Without-a-Peer-Team) — two-AI adversarial protocol operationalising ACH for solo analysts


* * *
◈ Intelligence Notes — Weekly Brief
High-signal strategic analysis on the structural shifts in global security. Every Monday. No noise.
[Subscribe →](https://subscribe.intelligencenotes.com/subscription/form?l=4413aea4-4f41-4089-8222-6743e4c75c85)
### Graph View
### Table of Contents
  * [Analysis of Competing Hypotheses (ACH)](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#analysis-of-competing-hypotheses-ach)
  * [BLUF](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#bluf)
  * [The Eight Steps of ACH](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#the-eight-steps-of-ach)
  * [Step 1: Identify All Plausible Hypotheses](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-1-identify-all-plausible-hypotheses)
  * [Step 2: List the Evidence](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-2-list-the-evidence)
  * [Step 3: Build the Matrix](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-3-build-the-matrix)
  * [Step 4: Refine the Matrix](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-4-refine-the-matrix)
  * [Step 5: Identify the Hypothesis with the Fewest Inconsistencies](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-5-identify-the-hypothesis-with-the-fewest-inconsistencies)
  * [Step 6: Examine Critical Assumptions](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-6-examine-critical-assumptions)
  * [Step 7: Report Conclusions with Confidence and Sensitivity](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-7-report-conclusions-with-confidence-and-sensitivity)
  * [Step 8: Identify Indicators for Future Observation](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#step-8-identify-indicators-for-future-observation)
  * [Why ACH Works](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#why-ach-works)
  * [ACH Limitations](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#ach-limitations)
  * [Operational Use in This Vault](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#operational-use-in-this-vault)
  * [Key Connections](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Analysis-of-Competing-Hypotheses#key-connections)


### Backlinks
  * [Complex Adaptive Systems](https://intelligencenotes.com/02-Concepts--and--Tactics/22-Intelligence--and--OSINT/Complex-Adaptive-Systems)
  * [Confirmation Bias](https://intelligencenotes.com/02-Concepts--and--Tactics/22-Intelligence--and--OSINT/Confirmation-Bias)
  * [ICD 203 — Analytic Standards](https://intelligencenotes.com/02-Concepts--and--Tactics/22-Intelligence--and--OSINT/ICD-203)
  * [Intelligence Cycle](https://intelligencenotes.com/02-Concepts--and--Tactics/22-Intelligence--and--OSINT/Intelligence-Cycle)
  * [Mirror Imaging](https://intelligencenotes.com/02-Concepts--and--Tactics/22-Intelligence--and--OSINT/Mirror-Imaging)
  * [Open Source Intelligence (OSINT)](https://intelligencenotes.com/02-Concepts--and--Tactics/22-Intelligence--and--OSINT/OSINT)
  * [Berlin Crisis (1961)](https://intelligencenotes.com/05-Historical-Events/Cold-War/Berlin-Crisis-1961)
  * [Yom Kippur War (1973)](https://intelligencenotes.com/05-Historical-Events/Cold-War/Yom-Kippur-War)
  * [Iraq WMD 2003](https://intelligencenotes.com/05-Historical-Events/Intelligence-History/Iraq-WMD-2003)
  * [Psychology of Intelligence Analysis — Heuer (1999)](https://intelligencenotes.com/06-Authors--and--Thinkers/Key-Works--and--Publications/Psychology-of-Intelligence-Analysis---Heuer-\(1999\))
  * [08 Guides & Manuals](https://intelligencenotes.com/08-Guides--and--Manuals/08-Guides--and--Manuals)
  * [Admiralty Code (Source and Information Grading)](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Admiralty-Code)
  * [Cognitive Biases in Intelligence Analysis](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Cognitive-Biases-in-Intelligence-Analysis)
  * [Intelligence Confidence Levels](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Intelligence-Confidence-Levels)
  * [PMESII-PT Framework](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/PMESII-PT)
  * [Structured Analytic Techniques (SATs)](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Structured-Analytic-Techniques)
  * [Target-Centric Analysis](https://intelligencenotes.com/08-Guides--and--Manuals/Analytical-Frameworks/Target-Centric-Analysis)
  * [AI-Generated Content Detection Methodology](https://intelligencenotes.com/08-Guides--and--Manuals/OSINT-Methodologies/AI-Content-Detection-Methodology)
  * [Geolocation and Chronolocation Methodology](https://intelligencenotes.com/08-Guides--and--Manuals/OSINT-Methodologies/Geolocation-Methodology)
  * [Pattern of Life Analysis (POLA)](https://intelligencenotes.com/08-Guides--and--Manuals/OSINT-Methodologies/Pattern-of-Life-Analysis)
  * [Source Verification Framework](https://intelligencenotes.com/08-Guides--and--Manuals/OSINT-Methodologies/Source-Verification-Framework)
  * [Independent Intelligence Analysis: A Field Manual for Open-Source Practitioners](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/00-%E2%80%94-Field-Manual-Index)
  * [Independent Intelligence Analysis — Part 01: The Independent Analyst](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/01-%E2%80%94-The-Independent-Analyst)
  * [Independent Intelligence Analysis — Part 02: Self-Tasking and Intelligence Requirements](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/02-%E2%80%94-Self-Tasking-and-Intelligence-Requirements)
  * [Independent Intelligence Analysis — Part 04: Source Evaluation Without Institutional Context](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/04-%E2%80%94-Source-Evaluation-Without-Institutional-Context)
  * [Independent Intelligence Analysis — Part 05: Analysis Without Institutional Support](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/05-%E2%80%94-Analysis-Without-Institutional-Support)
  * [Independent Intelligence Analysis — Part 06: Adversarial Review Without a Peer Team](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/06-%E2%80%94-Adversarial-Review-Without-a-Peer-Team)
  * [Independent Intelligence Analysis — Part 07: Production and Writing for Non-Institutional Consumers](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/07-%E2%80%94-Production-and-Writing-for-Non-Institutional-Consumers)
  * [Independent Intelligence Analysis — Part 09: Legal Exposure and Liability Management](https://intelligencenotes.com/08-Guides--and--Manuals/Operational-Manuals/Independent-Intelligence-Analysis/09-%E2%80%94-Legal-Exposure-and-Liability-Management)
  * [OSINT Toolkit Essentials](https://intelligencenotes.com/08-Guides--and--Manuals/Tool-Guides--and--Workflows/OSINT-Toolkit-Essentials)
  * [Obsidian for Intelligence Analysis](https://intelligencenotes.com/08-Guides--and--Manuals/Tool-Guides--and--Workflows/Obsidian-for-Intelligence-Analysis)


Created with [Quartz v4.5.2](https://quartz.jzhao.xyz/) © 2026
  * [Global Dashboard](https://intelligencenotes.com/static/dashboard/)
  * [Subscribe](https://subscribe.intelligencenotes.com/subscription/form?l=4413aea4-4f41-4089-8222-6743e4c75c85)
  * [X / @LuizHSBrandao](https://x.com/LuizHSBrandao)
  * [Newsletter Archive](https://intelligencenotes.com/Intelligence-Notes/)
  * [RSS Feed](https://intelligencenotes.com/index.xml)
  * [PT-BR: Intellecta Estratégia](https://intellectaestrategia.com.br/Firm/)
  * [GitHub](https://github.com/luizhsbrandao)
  * Consulting Inquiry



