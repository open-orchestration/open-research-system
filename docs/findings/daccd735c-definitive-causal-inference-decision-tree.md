---
id: daccd735c
topic: 02-statistical-causal-inference
title: "The definitive causal-inference decision tree: can you randomize, which design, which estimator, which falsification test"
status: draft
---

# The definitive causal-inference decision tree

## What this composes

This finding distils six sibling findings into one decision procedure an analyst
walks top-down: **can you randomize → which design → which estimator → which
falsification test**. It composes the two identification *calculi*
(d2c5150e6 — Pearl's do-calculus and Rubin's potential outcomes), the
quasi-experimental *identification* strategies for when randomization is
impossible (df8ca1aeb — IV/LATE, difference-in-differences, RDD), the RDD
*estimation* mechanics (d8d9c5187 — local-linear at the boundary with a
cross-validated bandwidth), the RDD *falsification* battery (dd02167c3 —
McCrary, polynomial discipline, placebo tests), the selection-on-observables
*estimation* layer (d77c7f685 — propensity-score stratification, IPW,
doubly-robust ATE), and the *designed-experiment* layer (d740bae09 — OEC,
power, Type I/II, effect size). Cross-references to those `d…` findings are
navigational only; every load-bearing claim below is re-anchored to the primary
`[c…]` source that backs that specific clause, so the synthesis inherits its
evidence rather than launders it.

## Provenance note

The strong primaries — anchoring the load-bearing spine — are the named papers:
Imbens & Angrist 1994 on IV/LATE [c13c50bdd], Card & Krueger 1994 on DiD
[c49a7ccc4], Lee & Lemieux 2010 on RDD [c213028d1], McCrary 2008 on the density
test [c2240c18b], Gelman & Imbens 2019 against high-order polynomials
[cd47fcc07], Cattaneo, Idrobo & Titiunik 2020 on the falsification battery
[c9a8f30ef], Lunceford & Davidian 2004 on IPW/doubly-robust estimation
[ca5712e1b], and Kohavi et al. 2009 on controlled web experiments [c2a793560].
The framework-summary sources for do-calculus/DAGs [c3a6803c7] and potential
outcomes [c7944da9a, c8d67f5ca] are `file://`-provenance secondary material;
they are used here only to *frame* the reconciliation of the two calculi, never
to carry the thesis. Where a framework point also has a named-primary anchor,
that anchor is cited.

---

## Step 1 — Can you randomize?

The first branch is whether the analyst controls the assignment mechanism.

**Yes → designed experiment.** When users (or units) can be *randomly* exposed
to Control or Treatment, randomization is the assignment mechanism that makes
the average causal effect estimable without modeling confounders — Kohavi et al.
underline that "the key here is 'random'": units cannot be distributed "any old
which way," and no factor can influence the assignment decision [c2a793560].
Proper randomization is also what validates the analysis: the confidence-interval
formulas assume the covariance between the Treatment and Control means is zero,
"which will be true in a controlled experiment when the randomization is carried
out properly" [c2a793560]. In potential-outcomes terms, randomized assignment
makes the potential outcomes independent of treatment [c7944da9a]; this is the
point where Pearl's and Rubin's frameworks collapse together (Step "Tensions"
below).

**No → quasi-experimental identification.** In observational data the
independence/ignorability assumption is routinely violated because units
self-select into treatment on observed and unobserved characteristics, so naive
observational comparisons are almost always incapable of recovering causal
effects without an explicit identification strategy [c7944da9a]. The analyst must
choose a design that manufactures as-if-random variation (Step 2).

## Step 2 — Which design?

### Designed-experiment branch (RCT / A/B test)

Under randomization the design *is* the A/B test: units are randomly split into
Control (A) and Treatment (B), and the system is validated with an **A/A test** —
assigning units to two groups but exposing both to the same experience, which
(i) supplies the variance estimate the sample-size formula needs and (ii) tests
the pipeline itself, since the null should be rejected about 5% of the time at a
95% confidence level [c2a793560]. Estimator and falsification choices for this
branch are Steps 3 and 4.

### Quasi-experimental branch — pick by the assumption you can defend

Each design buys identification with a *different* assumption and pays by
identifying a *local* or *sub-population* effect rather than the full-population
ATE [c13c50bdd][c49a7ccc4][c213028d1]:

- **IV / LATE** — when you have an instrument that shifts treatment but affects
  the outcome only through it. Under **monotonicity** ("either D_i(z) ≥ D_i(w)
  for all i, or D_i(z) ≤ D_i(w) for all i") and an **exclusion restriction**, an
  instrument identifies the **Local Average Treatment Effect** — the average
  effect for the subpopulation the instrument moves (the compliers), not the
  population ATE [c13c50bdd].
- **Difference-in-differences** — when a policy changes for one group but not a
  comparable control. Card & Krueger study New Jersey's minimum wage rising from
  $4.25 to $5.05 on April 1, 1992, with Pennsylvania as control [c49a7ccc4]. The
  estimator is the *second* difference: (change in NJ) − (change in PA); the
  first difference removes fixed state-level differences, the second removes any
  shock common to both, so it is unbiased only under the **parallel-/common-
  trends** assumption [c49a7ccc4].
- **Regression discontinuity** — when a rule assigns treatment by whether a
  running variable crosses a **cutoff** (sharp RD: treatment = 1[X ≥ c])
  [c213028d1]. Identification rests on **continuity** of the conditional
  expectations of the potential outcomes at the cutoff; the variation near the
  cutoff is "as good as randomized" as a *consequence* of agents' inability to
  precisely control the running variable at the threshold, so RD identifies a
  **local** effect at the cutoff, not the ATE [c213028d1].
- **Selection-on-observables / ignorability** — when no instrument, panel, or
  cutoff is available but you believe treatment is ignorable given measured
  covariates. This is the weakest-credibility branch (its key assumption is
  untestable — see Honest limits) and routes straight to the propensity-score
  estimators of Step 3.

## Step 3 — Which estimator?

### Designed experiments — size the experiment to detect the effect

The design inputs that *determine* the experiment are the **OEC** (one outcome,
chosen in advance), the **minimum detectable effect** Δ, and the **power**.
Kohavi et al. give a per-variant sample-size formula for 80% power: described
faithfully, the required per-variant n is sixteen times the variance of the OEC
divided by the square of the sensitivity Δ (rendered cleanly, n = 16σ²/Δ²); the
coefficient 16 is what delivers 80% power, and replacing it with 21 raises power
to 90% [c2a793560]. Larger OEC variance demands more units — hence the value of a
low-variance metric [c2a793560].

### Selection-on-observables — propensity-score estimators

The **propensity score** e(X) is the probability of treatment given covariates X,
and it enables two adjustment families [ca5712e1b]: **stratification** (group
observations by quantiles of the estimated score, form the effect within and then
across strata) and **weighting** by the inverse of the estimated score — the
**inverse-probability-of-treatment-weighted (IPW)** estimator [ca5712e1b]. IPW is
consistent only if the propensity-score model is correctly specified
[ca5712e1b]. The **doubly-robust / augmented** estimator augments IPW with
outcome-regression models and remains consistent if *either* the propensity model
*or* the outcome-regression models are correct — two chances to be right, which
the authors frame as "broad protection against misspecification" and an argument
for its "routine use" [ca5712e1b].

### Regression discontinuity — local-linear at the boundary

Estimate the jump with **local low-order** (linear or quadratic) regression at
the cutoff, not a global polynomial (see Step 4 and Tensions). Bandwidth choice
trades bias against variance: "a larger bandwidth yields more precise, but
potentially biased, estimates," while shrinking it produces "extremely noisy
estimates" — "a fundamental feature of kernel regressions" [c213028d1].
Lee & Lemieux give a rule-of-thumb plug-in bandwidth (closed form for the
rectangular kernel with a kernel-specific constant 2.702, built from the
regression standard error, the curvature m″(·), the range R, and an N^(−1/5)
rate) and point to Imbens & Kalyanaraman (2009) for an RD-specific optimal
bandwidth and a data-dependent method to choose it [c213028d1]. (Fuzzy RD, where
the cutoff shifts treatment *probability*, is estimated like IV using the jump in
treatment probability as the instrument [c213028d1].)

## Step 4 — Which falsification / validity test?

### Designed experiments — power and the two error types

The falsification frame here is the Type I / Type II error framing baked into the
power calculation: 80% power is "an 80% probability of rejecting the null
hypothesis that there is no difference ... if the true mean is different ... by
Δ," and the A/A test is the continuous integrity check — robots accepting cookies
once caused "much more than 5% false positives for an A/A test," exposing a biased
pipeline [c2a793560].

### Regression discontinuity — the falsification battery

An RD estimate is only as credible as the falsification evidence it survives.
Three tests compose into one pass:

1. **McCrary density / manipulation test.** The null is that the running-
   variable density is *continuous at the cutoff*; a discontinuity signals
   sorting/manipulation, "implemented as a Wald test of the null hypothesis that
   the discontinuity is zero" [c2240c18b]. The estimator is "a simple extension
   of the local linear density estimator," proceeding in two steps — a
   finely-gridded, deliberately "under-smoothed" histogram whose bins never
   straddle the cutoff, then a local linear regression on each side — with the
   parameter of interest the *log difference in height* of the two one-sided
   density estimates at c [c2240c18b]. McCrary uses the triangle kernel and finds
   no sorting in popular House elections but does find it in roll-call voting,
   "where sorting is both expected and found" [c2240c18b].

2. **Covariate-continuity and placebo tests.** Cattaneo, Idrobo & Titiunik
   enumerate five validation tests: null effects on **predetermined covariates**
   or placebo outcomes, continuity of the score **density**, treatment effects at
   **artificial/placebo cutoffs**, **exclusion of observations near the cutoff**
   (the "donut hole" approach), and **sensitivity to bandwidth** [c9a8f30ef].
   Because a predetermined covariate "could not have been affected by the
   treatment," a discontinuity in it at the cutoff is evidence against the design
   [c9a8f30ef]; and at an artificial cutoff estimated on "only observations with
   the same treatment status," the effect "should be zero" by construction, so a
   detected jump signals a violation [c9a8f30ef].

3. **Polynomial-order discipline (estimator-as-falsification).** Gelman & Imbens
   argue "high order global polynomial approximations should not be used,"
   recommending "local linear" or quadratic fits instead [cd47fcc07]. Their core
   reason: an RD polynomial estimate is a difference of weighted averages whose
   weights depend only on the threshold and forcing-variable values, and
   "higher-order regressions can give huge weights to points that are far from
   the discontinuity, thus creating highly noisy estimates" [cd47fcc07]. They add
   that results are "sensitive to the order of the polynomial" with no good method
   to choose it, and that such regressions yield confidence intervals that miss
   nominal coverage [cd47fcc07].

### Selection-on-observables — the unverifiable-assumption caveat

There is no positive falsification test for ignorability itself; its honest
status is a caveat, treated in Honest limits.

---

## Tensions reconciled

**Pearl's do-calculus vs. Rubin's potential outcomes — complementary, not
rival.** The two frameworks express the *same identifying content* in different
notation: Pearl's requirement of a covariate set Z that blocks every backdoor
path is the graphical face of Rubin's conditional unconfoundedness, and
do-calculus is what makes the connection between reading confounders off a DAG and
the ignorability assumption explicit [c3a6803c7]. They partition the workflow
differently — Pearl's identification formulas tell you *what* to estimate, while
the potential-outcomes literature foregrounds the estimation layer (matching,
propensity scores, IPW, doubly-robust estimators) that tells you *how well* it
can be estimated [c3a6803c7]. Both carry a shared, load-bearing warning:
adjustment is not automatically benign — conditioning on a collider introduces
bias and conditioning on a mediator blocks part of the effect, so what to control
for must be chosen by the causal structure, not by p-values, and "adjusting for
everything" is not a valid strategy [c3a6803c7]. The decision tree therefore uses
both: a DAG to choose the adjustment set, potential outcomes to choose the
estimator.

**Global polynomials vs. local-linear in RDD — the findings take a side.** Where
the two approaches conflict, this synthesis sides with **local low-order**
estimation: high-order global polynomials "should not be used" because their
implied weights are noisy and give large weight to points far from the cutoff,
their results are sensitive to an unchoosable polynomial order, and their
confidence intervals undercover [cd47fcc07]. Local-linear-at-the-boundary with a
principled bandwidth is the recommended estimator [c213028d1][cd47fcc07].

## Honest limits

- **Ignorability and SUTVA are untestable assumptions.** The selection-on-
  observables branch rests on conditional ignorability, which observational data
  cannot verify — independence is routinely violated by self-selection on
  unobservables, and no test confirms it holds [c7944da9a]. Rubin's framework
  also restricts well-posed causal questions to *manipulable* treatments — "no
  causation without manipulation" [c8d67f5ca].
- **RDD identifies only a local effect at the cutoff.** Continuity buys
  identification only at the threshold, so the estimate is "local in nature" and
  "generally not representative" of effects far from the cutoff
  [c213028d1][c9a8f30ef]. The density test is one-sided: a continuous density is
  "neither necessary nor sufficient for identification except under auxiliary
  assumptions," so passing it cannot prove validity [c2240c18b].
- **LATE is the complier-subpopulation effect.** IV identifies the effect only
  for units the instrument moves, not always-takers or never-takers, and not the
  population ATE [c13c50bdd].
- **DiD's identifying assumption is unfalsified here.** Common trends is assumed,
  not formally tested in the source; Card & Krueger's headline result — "no
  indication that the rise in the minimum wage reduced employment" — is the
  finding *of that paper*, contested in the literature, and is not adopted here
  as settled fact [c49a7ccc4].

## Composed recommendation

Walk the tree top-down. If you can randomize, run an A/B test, fix the OEC in
advance, size it with n = 16σ²/Δ² for 80% power, and guard it with an A/A test and
Type I/II framing [c2a793560]. If you cannot, choose the quasi-experimental design
by the assumption you can defend — an instrument (LATE, under exclusion +
monotonicity) [c13c50bdd], a policy change with a clean control (DiD, under common
trends) [c49a7ccc4], a cutoff rule (RDD, under continuity) [c213028d1], or, as the
weakest-credibility fallback, ignorability with propensity-score estimators,
preferring the doubly-robust estimator for its two chances to be right
[ca5712e1b]. Use a DAG to pick the adjustment set and potential outcomes to pick
the estimator — they are complementary [c3a6803c7]. For RDD, estimate local-linear
at the boundary with a cross-validated bandwidth [c213028d1], reject high-order
global polynomials [cd47fcc07], and report the full falsification battery —
McCrary density [c2240c18b], covariate-continuity and placebo-cutoff checks, and
bandwidth/donut-hole sensitivity [c9a8f30ef]. Throughout, state the estimand
honestly: designed experiments give the ATE under randomization, but IV gives a
complier LATE, RDD a local-at-cutoff effect, and ignorability rests on an
assumption no test can confirm.
