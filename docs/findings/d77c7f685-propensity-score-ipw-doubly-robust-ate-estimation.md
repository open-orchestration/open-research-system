---
id: d77c7f685
topic: 02-statistical-causal-inference
title: "Estimating the ATE under ignorability: propensity-score stratification, IPW, and the doubly-robust estimator's two chances to be right"
status: draft
---

# Estimating the ATE under ignorability: propensity-score stratification, IPW, and the doubly-robust estimator's two chances to be right

## Thesis

Identification tells you *whether* a causal effect can be recovered from
observational data; it does not tell you *how* to recover it. Lunceford &
Davidian (2004) take up the estimation half: given that exposure to treatment
is **confounded** with subject characteristics in **observational** data, and
working in the potential-outcomes framework with the average **treatment
effect** Δ = E[Y₁ − Y₀] as the estimand, they compare the propensity-score
adjustment methods that turn an identifying assumption (no unmeasured
confounding) into an actual number [ca5712e1b]. The load-bearing result is the
**doubly-robust** (augmented) estimator: it stays consistent if *either* the
propensity-score model *or* the outcome-regression models are correctly
specified — two chances to be right — which the authors argue gives "broad
protection against misspecification not available with these other approaches"
and "support[s] routine use of this estimator in practice" [ca5712e1b]. This
finding completes the identification→estimation arc that the identification
calculi [d2c5150e6] and the quasi-experimental designs [df8ca1aeb] leave open:
once you have assumed ignorability, this is the machinery that estimates the
ATE.

## Sub-question 1 — What is the propensity score, and what two adjustment families does it enable?

The propensity score e(X) is the probability of treatment exposure conditional
on covariates X, and it is the basis for two distinct adjustment approaches
[ca5712e1b]. The first is **stratification**: observations are grouped by
**quantiles** of the estimated propensity score, and the treatment effect is
formed within and then across strata [ca5712e1b]. The second is **weighting**:
observations are weighted by the **inverse** of the estimated propensity score
— the **inverse-probability-of-treatment-weighted (IPW)** estimator, which is
the paper's central object (IPW appears ~123 times in the source) [ca5712e1b].
The paper's key-word list explicitly names "covariate balance," "double
robustness," "inverse-probability-of-treatment-weighted estimator," and
"observational data," signaling that the comparison spans both adjustment
families [ca5712e1b].

## Sub-question 2 — What must IPW get right to be consistent?

IPW-type estimators are **consistent if the propensity-score model is correctly
specified** — i.e. if the model for the "complete-case" probability of exposure
is right [ca5712e1b]. This is a single-model bet: the entire consistency of the
weighted estimator rides on the analyst having modeled treatment assignment
correctly. If that model is wrong, the IPW estimate is biased, and there is no
second line of defense within the plain IPW estimator [ca5712e1b].

## Sub-question 3 — What is double-robustness, and why is "two chances to be right" the practical win?

The doubly-robust / **augmented** estimator augments the IPW estimator with
**outcome-regression** models (one per treatment arm) [ca5712e1b]. Its defining
property is that it **remains consistent if *either* (i) the propensity-score
model is correctly specified — even when the regression models are wrong — *or*
(ii) the outcome-regression models are correctly specified** [ca5712e1b]. You do
not need both to be right; getting one of the two models correct suffices. This
is the practical hedge: model misspecification is the normal condition of
observational analysis, and double-robustness converts a single point of failure
(IPW's lone propensity model) into a redundant pair. Notably, the
outcome-regression models are incorporated "only as a way to gain efficiency
over simpler weighted estimators," yet their presence is precisely what buys the
second chance at consistency — efficiency and robustness arrive together
[ca5712e1b]. The authors frame this as "broad protection against
misspecification not available with these other approaches" and an argument for
its "routine use" [ca5712e1b]. The paper backs the comparison with extensive
**simulation** studies of the methods' relative performance [ca5712e1b].

## Sub-question 4 — How does this complete the identification→estimation story?

The identification calculi finding [d2c5150e6] establishes *when* an effect is
estimable — Pearl's backdoor adjustment and Rubin's conditional ignorability are
two notations for the same content — and explicitly notes that the
potential-outcomes literature "foregrounds the estimation layer through
matching, propensity scores, inverse-probability weighting, and doubly robust
estimators" [d2c5150e6]. This finding is that estimation layer made concrete.
The quasi-experimental finding [df8ca1aeb] covers the *other* branch — what to do
when you cannot assume ignorability and instead lean on an instrument, a
pre/post comparison, or a discontinuity — and its own gap note flags that "a
worked IPW / doubly-robust ATE estimation finding remains ungrounded" [df8ca1aeb].
The division is clean: when no-unmeasured-confounding is plausible (selection on
observables), use the propensity-score machinery here; when it is not, use the
design-based identification strategies of [df8ca1aeb]. Both presuppose the
identification discipline of [d2c5150e6].

## Gaps found

- **Exact estimator algebra is not transcribed.** The source is a PDF→markdown
  conversion in which math and estimator symbols are garbled (ligatures render as
  `(cid:…)`, estimator hats are mangled). The IPW and doubly-robust estimators
  are therefore stated by *structure* (inverse-propensity weighting; augmentation
  by outcome regressions; the either-or consistency property) rather than by
  transcribed equations [ca5712e1b]. The byte-verifiable claims are the prose
  statements; tokens confirmed whitespace-insensitively include `IPW`,
  `propensity`, `quantiles`, `consistentif`, `correctly`, `completecase`,
  `doublerobustness`, `augmented`, `simplerweighted`, `protectionagainstmisspeci`,
  `routineuse`, and `broadprotection`.
- **No simulation numbers quoted.** The paper reports extensive simulation
  comparisons, but the result tables are garbled in the conversion, so no
  specific bias, variance, or efficiency figures are claimed here — only the
  qualitative finding that the methods are compared empirically [ca5712e1b].
- **Ignorability is an assumption this machinery does not test.** Propensity-score
  stratification, IPW, and the doubly-robust estimator all presuppose
  no-unmeasured-confounding (and positivity/overlap); double-robustness protects
  against *model* misspecification, not against unmeasured confounders. Whether
  ignorability holds is an identification question settled upstream by
  [d2c5150e6] / [df8ca1aeb], not something the estimator can verify from the data
  [ca5712e1b].
