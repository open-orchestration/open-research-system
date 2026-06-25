---
id: dd02167c3
topic: 02-statistical-causal-inference
title: "Falsifying an RD design: the McCrary density test for manipulation, the case against high-order polynomials, and the placebo-cutoff/covariate battery"
status: draft
---

# RDD falsification: density manipulation test, polynomial-order discipline, and the placebo battery

## Thesis

A regression-discontinuity estimate is only as credible as the falsification
evidence it survives. The Lee–Lemieux survey layer (d8d9c5187) names McCrary
and covariate continuity but stops short of the formal machinery; it explicitly
flags two gaps — no *named* placebo/non-cutoff test, and no principled
polynomial-order criterion. This finding closes both with the primary sources
behind them: McCrary's (2008) two-step density-discontinuity test for
manipulation [c2240c18b]; Gelman & Imbens's (2019) three-part argument that
high-order global polynomials should be replaced by local low-order ones
[cd47fcc07]; and Cattaneo, Idrobo & Titiunik's (2020) five-test falsification
battery, including treatment effects at *artificial/placebo cutoffs*
[c9a8f30ef]. Identification (df8ca1aeb) and the Lee–Lemieux estimation
mechanics (d8d9c5187) are taken as given; this finding develops only the
testable falsification machinery.

## Sub-question 1 — The McCrary (2008) density test as a formal procedure [c2240c18b]

**What it tests.** Standard sufficient conditions for RD identification are
continuity of the conditional expectation of counterfactual outcomes in the
running variable; these may fail when agents can *manipulate* the running
variable [c2240c18b]. McCrary develops a test "related to continuity of the
running variable density function" — the null is that the density of the
running variable is *continuous at the cutoff*, and the manipulation
alternative is a discontinuity (sorting). The test is "implemented as a Wald
test of the null hypothesis that the discontinuity is zero" [c2240c18b].

**Two-step estimator.** The estimator is "a simple extension of the local
linear density estimator (Cheng, Fan and Marron 1997)" and "proceeds in two
steps": (i) the first step is a "finely-gridded" — deliberately
"under-smoothed" — histogram of the running variable, with bins "defined
carefully enough that no one histogram bin includes points both to the left and
right of the point of discontinuity"; (ii) the second step "smooths the
histogram using local linear regression, separately on either side of the
cutoff" [c2240c18b]. In the second step the bin *midpoints* are treated as the
regressor and the *normalized bin counts* (heights) as the outcome, and McCrary
notes it is "easier and more accurate to estimate two separate local linear
regressions, one on either side of c," giving most weight to bins nearest the
evaluation point [c2240c18b].

**Test statistic.** The parameter of interest is the *log difference in height*
of the two one-sided density estimates at the cutoff:

> θ = ln f⁺ − ln f⁻ (canonical form)

i.e. the log of the right limit minus the log of the left limit of the density
at c, and θ̂ = ln f̂⁺ − ln f̂⁻ is the log difference of the two intercept
coefficients from the one-sided local linear regressions [c2240c18b]. (The
source PDF-extraction garbles equation (3) and the estimator line — rendered as
`lnlimf(r)−lnlimf(r) ≡ lnf+−lnf−` and `θ(cid:98) lnf(cid:98)+−lnf(cid:98)−`; the
canonical form shown is recovered from the surrounding prose, which is intact.)

**Inference.** θ̂ is "consistent and asymptotically normal" under nonparametric
regularity conditions; McCrary uses the triangle kernel K(t) = max{0, 1−|t|}
[c2240c18b]. The asymptotic standard error of θ̂ has the canonical form

> σ̂²(θ̂) ≈ (1/(nh)) · (24/5) · (1/f̂⁺ + 1/f̂⁻) (canonical form)

(source equation (5) is extraction-garbled — rendered as
`σ(cid:98) = ... 1 24 ... θ nh 5 f(cid:98)+ f(cid:98)−`; the constant 24/5 and
the 1/(nh) scaling and 1/f̂⁺ + 1/f̂⁻ terms are legible, so the canonical form is
shown.) "t-tests constructed using this standard error are very nearly normally
distributed under the null hypothesis," with simulated test size of roughly
5–7 percent [c2240c18b].

**What a rejection implies — and its limit.** A significant density
discontinuity is evidence of sorting/manipulation, which undermines the
continuity assumptions and so the RD design — McCrary's application finds no
sorting in popular House elections but does find it in roll-call voting, "where
sorting is both expected and found" [c2240c18b]. The honest limit: a continuous
density is "neither necessary nor sufficient for identification except under
auxiliary assumptions" [c2240c18b]. Passing the test is therefore reassuring
but not proof of validity, and failing it does not mechanically rule out a
meaningful parameter.

## Sub-question 2 — Why high-order polynomials should not be used (Gelman & Imbens 2019) [cd47fcc07]

A common RD practice is "to control for high order (third, fourth, or higher)
polynomials of the forcing variable." Gelman & Imbens argue such estimators
"can be misleading" and that "high order global polynomial approximations
should not be used," recommending instead "inference based on local low order
polynomials" — specifically "local linear or quadratic polynomials or other
smooth functions" [cd47fcc07]. They give "three, somewhat related, reasons":

**Issue 1 — Noisy weights (the core contribution).** Any polynomial-regression
RD estimate "can be interpreted as the difference between a weighted average of
the outcomes for the treated and a weighted average for the controls," where
"the weights depend only on the threshold and the values of the forcing
variable, not on the values for the outcomes" [cd47fcc07]. Inspecting these
implied weights shows that "higher-order regressions can give huge weights to
points that are far from the discontinuity, thus creating highly noisy estimates
of the causal estimand of interest" [cd47fcc07]. For an extreme forcing-variable
value outside the bandwidth, the *local linear* weight would be 0, "whereas one
would like to give little or zero weight to the individuals with extreme values"
the "global polynomial regressions attach large weights, sometimes positive,
sometimes negative ... generally larger than the average weight of 1"
[cd47fcc07]. The authors recommend researchers "routinely present the implicit
weights arising from regression estimates" [cd47fcc07].

**Issue 2 — Sensitivity to polynomial order.** "Results based on high order
polynomial regressions are sensitive to the order of the polynomial. Moreover,
we do not have good methods for choosing that order in a way that is optimal for
the objective of a good estimator for the causal effect of interest"
[cd47fcc07]. This is the primary-source answer to the Lee–Lemieux gap: there is
*no* principled global-polynomial-order selection rule, which is itself an
argument against the approach.

**Issue 3 — Confidence intervals that miss nominal coverage.** "Conventional
inference for treatment effects in regression discontinuity settings can be
misleading, in the sense that ... confidence intervals are too narrow." Even
"if there is no discontinuity in the regression function, high-order polynomial
regressions often lead to confidence intervals that fail to include zero with
probability substantially higher than the nominal Type 1 error rate"
[cd47fcc07]. The three issues are "complementary": "the noisiness of the
implicit weights explains how the global polynomial regressions can have poor
coverage and wide confidence intervals at the same time" [cd47fcc07].

**Estimand.** Throughout, the recommended local low-order approach keeps the
estimand defined at the cutoff, with the polynomial fit locally within a
bandwidth rather than globally across the support [cd47fcc07].

## Sub-question 3 — The falsification battery (Cattaneo, Idrobo & Titiunik 2020) [c9a8f30ef]

A virtue of the RD design is that "the score changes discontinuously at the
cutoff—a condition that is directly testable," and the design "comes with an
extensive array of falsification tests" [c9a8f30ef]. The Element enumerates
"five empirical validation tests based on (i) the null treatment effect on
predetermined covariates or placebo outcomes, (ii) the continuity of the score
density around the cutoff, (iii) the treatment effect at artificial cutoff
values, (iv) the exclusion of observations near the cutoff, and (v) the
sensitivity to bandwidth choices" [c9a8f30ef].

**(a) Density / manipulation test.** Researchers should examine the running
variable's density for a jump at the cutoff, both graphically (a histogram of
the score) and "more formally using a statistical test, often called a density"
test [c9a8f30ef]. Two implementations are described: a *binomial* test of
whether, in a small window around the cutoff, treated and control counts are
consistent with success probability 1/2 — "finite sample exact, under the
assumptions imposed" (e.g. with X ∈ [−2,2], 47 control vs. 53 treated,
binom.test(53,100,1/2) giving p = 0.6173) [c9a8f30ef]; and the local-polynomial
density-discontinuity test in the `rddensity` command, whose null is "no
difference in the density of treated and control observations at the cutoff"
[c9a8f30ef]. The Element credits the density test to McCrary (2008) [c9a8f30ef].

**(b) Predetermined covariates and placebo outcomes.** "One of the most
important RD falsification tests involves examining whether, near the cutoff,
treated units are similar to control units in terms of observable
characteristics." Because "the predetermined covariate (or placebo outcome)
could not have been affected by the treatment, the null hypothesis of no
treatment effect should not be rejected if the RD design is valid"; a
discontinuity in such a covariate or placebo outcome at the cutoff is evidence
against the design [c9a8f30ef].

**(c) Artificial / placebo cutoffs.** "Another useful falsification analysis
examines treatment effects at artificial or placebo cutoff values," motivated by
the continuity of the regression functions away from the true threshold. The
procedure estimates a local-polynomial effect at a non-cutoff point using "only
observations with the same treatment status," so that "by construction, the
treatment effect at each artificial cutoff should be zero" — a detected jump at
a placebo cutoff signals a violation [c9a8f30ef]. This is the *named non-cutoff
placebo test* flagged as a gap in d8d9c5187.

**(d) Exclusion of observations near the cutoff (donut hole).** Excluding the
units closest to the cutoff and re-running estimation/inference — "sometimes
referred to as a 'donut hole' approach" — probes robustness to possible
manipulation right at the threshold and "to the unavoidable extrapolation
involved in local polynomial estimation" [c9a8f30ef].

**(e) Sensitivity to bandwidth.** Repeating the analysis across bandwidth
choices checks that conclusions are not an artifact of one window; for
falsification it "may be more appropriate to use the CER-optimal bandwidth"
since the interest is testing the null of no effect rather than point estimation
[c9a8f30ef].

## Sub-question 4 — Composition into a protocol, and honest limits

The three primaries compose into a single falsification pass an applied RD
should report: (1) test the *running-variable density* for manipulation
(McCrary's two-step log-difference test [c2240c18b], reported via the binomial
and `rddensity` implementations in [c9a8f30ef]); (2) verify *continuity of
predetermined covariates and placebo outcomes* and run *placebo-cutoff* checks
that should yield zero effects [c9a8f30ef]; and (3) estimate the effect itself
with *local linear or quadratic* polynomials rather than a high-order global
polynomial, presenting the implied weights and checking bandwidth/donut-hole
sensitivity [cd47fcc07][c9a8f30ef].

Each test has an honest limit. The density test is one-sided evidence: a
continuous density is "neither necessary nor sufficient for identification
except under auxiliary assumptions," so passing it cannot prove validity and
failing it cannot by itself condemn a meaningful parameter [c2240c18b]. The
polynomial argument is about *choice of estimator*, not identification — Gelman
& Imbens note we "do not have good methods" for choosing a high polynomial
order, which is precisely why they prefer the local low-order alternative
[cd47fcc07]. Covariate and placebo-cutoff tests can only *fail to reject*; they
provide "indirect evidence" of validity and, like all the battery, the RD
effect they protect "is local in nature" and "generally not representative" of
treatment effects far from the cutoff [c9a8f30ef].
