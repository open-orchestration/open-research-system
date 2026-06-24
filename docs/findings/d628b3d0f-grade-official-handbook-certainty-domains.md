---
id: d628b3d0f
topic: 01-methodology-epistemics
title: "GRADE evidence-certainty system from the official handbook: four levels, five downgrade + three upgrade domains, certainty vs recommendation"
status: draft
---

# GRADE evidence-certainty system from the official handbook

This finding grounds the GRADE evidence-certainty mechanics on the GRADE Working Group's own handbook — the primary, authoritative source — replacing the engine's prior reliance on a secondary/blog restatement. It supplies the official-handbook grounding for the GRADE half of finding dc577f3e2 ("Grade, reconcile, calibrate…"), which discusses GRADE alongside contradiction-reconciliation and calibration but rests partly on secondary GRADE sources; it does not restate that finding's reconcile/calibrate material.

## Four levels of certainty

GRADE rates the quality (certainty) of a body of evidence in four grades, each defined as our confidence that the true effect lies close to the estimate [c5b73364f]. **High**: "We are very confident that the true effect lies close to that of the estimate of the effect." **Moderate**: "We are moderately confident in the effect estimate: The true effect is likely to be close to the estimate of the effect, but there is a possibility that it is substantially different." **Low**: "Our confidence in the effect estimate is limited: The true effect may be substantially different from the estimate of the effect." **Very Low**: "We have very little confidence in the effect estimate: The true effect is likely to be substantially different from the estimate of effect" [c5b73364f]. The handbook notes that quality of evidence is a continuum and any discrete categorisation involves some arbitrariness, but the four grades are kept for simplicity, transparency, and vividness [c5b73364f].

## Starting point: study design

The GRADE approach to rating quality begins with the study design — trials or observational studies — and then addresses five reasons to possibly rate the quality down and three to possibly rate it up [c5b73364f]. Randomized trials without important limitations provide high quality evidence; observational studies without special strengths or important limitations provide low quality evidence [c5b73364f]. Equivalently, evidence from observational studies is initially classified as low quality evidence [c5b73364f].

## Five domains that can rate certainty down

The handbook lists five factors that can reduce the quality of the evidence, each able to lower the rating by one or two levels (Table 5.2) [c5b73364f]:

1. **Limitations in study design or execution (risk of bias)** — flaws in how studies were designed or run, including selective outcome reporting, which can be addressed within single studies [c5b73364f].
2. **Inconsistency of results** — "an unexplained heterogeneity of results"; widely differing estimates of the treatment effect across studies signal possible true differences in the underlying effect [c5b73364f].
3. **Indirectness of evidence** — the evidence does not directly answer the question, e.g. an outcome measured via a surrogate (such as bone mineral density for fracture rates) rather than directly [c5b73364f].
4. **Imprecision** — results are imprecise when studies include relatively few patients and few events and thus have a wide confidence interval around the estimate of the effect, creating uncertainty about the results [c5b73364f].
5. **Publication bias** — assessed by looking at a group of studies, since an entire study remaining unpublished can only be detected across a body of evidence rather than within one study [c5b73364f].

## Three domains that can rate certainty up

The handbook lists three factors that can increase the quality of the evidence (Table 5.3), applying mainly to observational evidence without downgrades [c5b73364f]:

1. **Large magnitude of effect** — can raise the rating by one or two levels [c5b73364f].
2. **All plausible confounding would reduce the demonstrated effect, or increase the effect if no effect was observed** (plausible residual confounding / opposing bias) — raises by one level [c5b73364f].
3. **Dose-response gradient** — raises by one level [c5b73364f].

These factors are additive: the reduction or increase from each individual factor is added together to set the quality of evidence for an outcome [c5b73364f].

## Certainty is not strength of recommendation

GRADE separates the confidence in effect estimates (quality of evidence) from the strength of a recommendation [c5b73364f]. High confidence in effect estimates does not necessarily imply a strong recommendation, and strong recommendations can result from low or even very low confidence in effect estimates [c5b73364f]. GRADE suggests the terms strong and weak recommendations for the two categories of recommendation strength, though those making recommendations may choose different wording [c5b73364f]. A recommendation weighs more than certainty: decision-making always involves a balance between health benefits and harms, and the balance between desirable and undesirable effects is itself a continuum [c5b73364f].

## Output artifacts

GRADE's structured reporting artifacts are the Evidence Profile and the Summary of Findings (SoF) table [c5b73364f]. The GRADE evidence profile contains detailed information about the quality-of-evidence assessment and the summary of findings for each included outcome, and is intended for review authors, those preparing SoF tables, and anyone who questions a quality assessment; it makes the judgments systematic, transparent, and inspectable [c5b73364f]. The standard SoF table format includes the list of outcomes, the assumed (baseline/control) risk, and the corresponding risk after the intervention is applied [c5b73364f].

## Synthesis: why this matters for a citation-gated engine

GRADE gives the engine a principled, domain-decomposed way to attach a certainty rating to a finding: start from the study design (trials high, observational low), then rate down across five explicit domains (risk of bias, inconsistency, indirectness, imprecision, publication bias) and rate up across three (large effect, dose-response gradient, plausible-confounding/opposing bias), with the adjustments additive [c5b73364f]. Because the domains are named and each consequence is bounded (down or up by one or two levels), the rating is auditable rather than a single opaque score — the same transparency rationale the handbook gives for the Evidence Profile [c5b73364f]. The handbook's separation of certainty from recommendation strength maps cleanly onto the engine's distinction between "how sure are we in the evidence" and "what should the system do about it," since the latter additionally weighs the balance of benefits and harms, not just confidence in the estimate [c5b73364f].
