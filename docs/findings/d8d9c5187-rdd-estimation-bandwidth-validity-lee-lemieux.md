---
id: d8d9c5187
topic: 02-statistical-causal-inference
title: "RDD in practice: local-linear estimation at a boundary, cross-validated bandwidth, and the McCrary/covariate falsification tests that make the design testable"
status: draft
---

# RDD estimation and validity in practice (Lee & Lemieux)

## Thesis

Once a regression-discontinuity design is *identified* — a forcing variable
crossing a cutoff, treatment effects recovered under continuity of the
conditional expectation functions (the identification layer covered in
df8ca1aeb) — the work that decides whether an applied RD estimate is credible
is **estimation and falsification**, not identification. Lee & Lemieux's
review is rich on exactly this practical layer: it argues RD variation near the
cutoff is "as good as randomized" and therefore *testable like an experiment*
[c213028d1]; it explains why estimation at the cutoff is a hard **boundary
problem** that motivates **local linear regression** over both global
polynomials and plain kernel averages [c213028d1]; it lays out a
boundary-specific **cross-validation** bandwidth rule against a bias–variance
tradeoff [c213028d1]; and it specifies the **falsification tests** — the
McCrary density test for manipulation and the continuity-of-covariates check —
that a valid RD must survive [c213028d1]. This finding develops that
estimation/validity machinery, which df8ca1aeb deliberately does not.

## Sub-question 1 — RD as a *local randomized experiment*: what the interpretation buys, and its limits

Lee & Lemieux's central interpretive claim is that an RD design does not merely
*assume* "as good as randomized" treatment variation — such variation is a
*consequence* of a weaker behavioral assumption: that individuals have
**imprecise control** over the assignment variable X [c213028d1]. Formally, if
control is imprecise, then `Pr[W = w, U = u | X = x]` is continuous in x at the
threshold, so "the treatment is 'as good as' randomly assigned around the
cutoff" — their stated **Local Randomization** result [c213028d1]. (This
"as-if-random at the cutoff" claim is the identification-level bridge already
established in df8ca1aeb; what follows is what that bridge *lets you do* in
practice.)

What this buys, and the reason it matters for *practice*, is a testable
falsification program: "RD designs can be analyzed – and tested – like
randomized experiments" [c213028d1]. The key implication is concrete — if
variation in treatment near the threshold is approximately randomized, then all
**baseline characteristics** (variables determined *prior* to the realization
of the assignment variable) should have the same distribution just above and
just below the cutoff, and a discontinuity in those covariates means the
identifying assumption is unwarranted [c213028d1]. Lee & Lemieux note this kind
of test is "arguably more important in the RD design than in the experimental
context," because whether an individual's control is precise or imprecise is
often "nothing more than a conjecture" — but a conjecture with testable
predictions [c213028d1].

**Limits.** The interpretation is local and the assumption is only *partly*
testable. The identifying condition is about each individual's *ex ante*
density of X being continuous, which is "fundamentally untestable, since for
each individual we only observe one realization of X"; in principle individual
densities could jump up and down and offset in the aggregate, though Lee &
Lemieux judge such occurrences "far-fetched" in recent applications
[c213028d1]. Like a randomized experiment, the strongest honest claim is that
the data "failed to reject" the assumption of (local) randomization, since
balance in *unobserved* characteristics can never be directly tested
[c213028d1].

## Sub-question 2 — Estimation: the boundary problem, global polynomials vs. local linear, and kernel choice

RD estimation is hard for a specific reason: the effect is the value of the
regression function evaluated *right at the cutoff*, which is a **boundary
point**, and "this results in a 'boundary problem' that causes some
complications for non-parametric methods" [c213028d1].

**Global polynomials (series estimation).** A simple way to relax linearity is
to add polynomial functions of X to the regression — the "series estimation
approach" of nonparametric analysis [c213028d1]. Its disadvantage is that it
gives *global* estimates over all values of X, while RD depends on a *local*
estimate at the cutoff; using "data far away from the cutoff point to predict
the value of Y at the cutoff point is not intuitively appealing" [c213028d1].
Lee & Lemieux still recommend trying higher-order polynomials as a robustness
check on the RD estimate [c213028d1].

**Plain kernel averaging fails at the boundary.** Kernel regression is "a local
method well suited for estimating the regression function at a particular
point," but "this property does not help very much in the RD setting because
the cutoff represents a boundary point where kernel regressions perform poorly"
[c213028d1]. With a rectangular kernel, computing the kernel regression on each
side just amounts to averaging Y in the bin to the left and the bin to the
right of the cutoff; when the regression function is sloped, the difference of
those two bin means **systematically overstates** the true jump — a
**systematic bias** in kernel estimates of the treatment effect, derived more
formally by Hahn et al. (2001) [c213028d1].

**Why local linear at a boundary.** Hahn et al. (2001)'s solution is to run
**local linear regressions** — with a rectangular kernel, "standard linear
regressions within the bins on both sides of the cutoff point" — which predict
the value at the cutoff far better and "reduces the bias by an order of
magnitude" [c213028d1]. The order-of-magnitude claim is precise about
asymptotic bias: the usual kernel bias is of order *h²* at interior points but
of order *h* at boundary points (where *h* is the bandwidth), so at the
boundary the bias dies off more slowly as *h → 0*; local linear regression
brings the boundary bias back down to the interior order [c213028d1]. *(The
source's bias-order notation is PDF-extraction garbled — it renders as `h2`
inline; canonical orders are O(h²) interior and O(h) boundary as stated in the
source's footnote on Hahn et al. (2001) and Imbens & Lemieux (2008)
[c213028d1].)*

**Implementation.** In practice RD is run as two separate regressions, one on
each side of the cutoff. It is convenient to transform X to **X − c** so the
two intercepts directly give the regression-function values at the cutoff and
their difference is the RD estimate [c213028d1]. *(The source's two-sided
regression equations are extraction-garbled — e.g. `Y = a l + fl (X − c) + e`
for X < c — but the canonical form is two linear-in-(X−c) regressions whose
intercept gap is the treatment effect [c213028d1].)*

## Sub-question 3 — Bandwidth: the bias–variance tradeoff and cross-validation

Choosing the bandwidth (the width of the window/bin) trades bias against
variance: "A larger bandwidth yields more precise, but potentially biased,
estimates of the regression," while shrinking it to cut bias produces
"extremely noisy estimates of the treatment effect" because too few
observations remain [c213028d1]. This bias–precision tradeoff is called "a
fundamental feature of kernel regressions" [c213028d1].

Lee & Lemieux give two formal bandwidth-selection routes beyond eyeballing the
graph:

1. **Rule-of-thumb (ROT) plug-in.** A two-step plug-in: estimate a ROT
   bandwidth over the whole data range, then use it to estimate the optimal
   bandwidth at the cutoff [c213028d1]. For the rectangular kernel the ROT
   bandwidth has a closed form with a **kernel-specific constant 2.702**, built
   from the estimated standard error of the regression, the **second
   derivative (curvature) m″(·)** of an estimated regression of Y on X, the
   **range R** of the assignment variable, and an **N^(−1/5)** rate
   [c213028d1]. They credit Silverman (1986)'s analogous density-estimation
   rule (the `0.9 · … · N^(−1/5)` form) and point to **Imbens & Kalyanaraman
   (2009)**, who derive an optimal bandwidth specifically for the RD setting
   and a data-dependent method to choose it [c213028d1]. *(The closed-form ROT
   formula is heavily PDF-garbled — summation, second-derivative, and exponent
   symbols are mangled; only the constant 2.702, the inputs (σ̂, m″, R), and
   the N^(−1/5) rate are stated here as recovered from the source
   [c213028d1].)*

2. **Cross-validation ("leave one out").** Following Ludwig & Miller (2007) and
   Imbens & Lemieux (2008), a leave-one-out procedure aimed *specifically at
   the boundary*: drop observation *i*, fit a regression with bandwidth *h*
   using only observations on the **same side and toward the cutoff** —
   `Xi − h ≤ X < Xi` for points left of the cutoff, `Xi < X ≤ Xi + h` for
   points right of it — predict Y at Xi, repeat for every observation, and pick
   the *h* that **minimizes the mean squared** prediction error [c213028d1].
   This deliberately differs from standard kernel cross-validation (where the
   left-out point sits in the *middle* of its window, per Blundell & Duncan
   (1998)) so as to mimic RD estimation at a **boundary** rather than an
   interior point [c213028d1].

**Sensitivity / robustness.** Lee & Lemieux caution that the bandwidth is not a
mechanical choice: "a range of bandwidths often yield similar values of the
cross-validation function in practical applications," so the researcher retains
some discretion [c213028d1]. The standard robustness practice is to present RD
estimates over **varying window widths** and **higher-order polynomial terms**
and show the estimate is stable; estimates "sensitive to minor changes in
specification" are viewed as less reliable [c213028d1]. They also note settings
where results are inherently more bandwidth-sensitive, so the bandwidth-
selection procedure plays a larger role [c213028d1].

## Sub-question 4 — Validity / falsification: McCrary density, covariate smoothness, and reading the whole curve

Because the local-randomization result yields testable predictions, a credible
applied RD reports falsification tests, not just a point estimate.

**McCrary (2008) density test for manipulation/sorting.** The most direct check
on imprecise control is to examine the **density of the assignment variable X
itself** [c213028d1]. If each individual's density of X is continuous, the
population marginal density of X should be continuous too; "a jump in the
density at the threshold is probably the most direct evidence of some degree of
sorting around the threshold, and should provoke serious skepticism about the
appropriateness of the RD design" [c213028d1]. A practical advantage: the
density test "can always be performed in a RD setting," whereas the covariate
test depends on having covariate data [c213028d1]. The test is only *partial*
(the individual ex-ante density is fundamentally untestable, and offsetting
jumps could in principle leave the aggregate density continuous), but Lee &
Lemieux argue stratifying by observables would typically expose such
discontinuities [c213028d1]. The empirical pass criterion is a formal test that
"fails to reject the null hypothesis of no discontinuity in the density at the
cutoff" [c213028d1].

**Continuity of predetermined covariates ("no jump in baseline covariates").**
The complementary test compares the **local values of baseline covariates on
the two sides of the cutoff** [c213028d1]. Formally, one assesses whether
`Pr[W = w | X = x]` is continuous in x at the threshold; "a discontinuity would
indicate a failure of the identifying assumption" [c213028d1]. Lee & Lemieux
draw the explicit analogy to experiments: this is "akin to the tests performed
to empirically assess whether the randomization was carried out properly in
randomized experiments," where one demonstrates treatment and control groups
are "similar in their observed baseline covariates" [c213028d1]. (A related
point, distinct from validity: covariates are *not* needed for consistency —
because of local randomization, assignment is independent of baseline
covariates by construction — but researchers include them to **reduce sampling
variability** [c213028d1].)

**Reading the whole curve (placebo-style intuition).** Lee & Lemieux do not
frame a separate "test at non-cutoff points" procedure, but they stress a
graphical analogue: a plot of binned outcome means lets the reader judge
"whether the 'jump' in the outcome variable at the cutoff is unusually large
compared to the **bumps in the regression curve away from the cutoff**"
[c213028d1] — i.e., the cutoff jump is only convincing relative to the
non-cutoff variation in the same data.

## Sub-question 5 — Graphical presentation and its honesty constraints

RD's "major advantage … is its transparency," shown graphically by binning the
assignment variable — with **separate bins on each side of the cutoff** so
treated and untreated observations are never mixed in one bin — and plotting
each bin's mean outcome against the bin midpoint [c213028d1]. Because a bin mean
*is* a rectangular-kernel nonparametric estimate at the bin midpoint, "the set
of bin means literally represent non-parametric estimates of the regression
function," which guides the choice of functional form before any regression is
run [c213028d1]. Plotting the **count of observations per bin** doubles as a
visual manipulation check — a discontinuity in the number of observations at the
threshold "would suggest manipulation" [c213028d1].

The honesty constraint: graphical presentation is "helpful and informative, but
the visual presentation should not be tilted toward either finding an effect
or finding no effect," because
"there is some room for the researcher to construct graphs making it seem as
though there are effects when [there are none]" — bin width is itself a degree
of freedom, which is exactly why the formal bandwidth/cross-validation
machinery of Sub-question 3 matters [c213028d1].

## Bottom line

For the practitioner: identify the design via continuity (df8ca1aeb), then
**estimate** it with local linear regression on each side of `X − c` to defuse
the boundary bias (not a global polynomial alone, not raw kernel averages)
[c213028d1]; **choose the bandwidth** by boundary-specific cross-validation or
an RD-tuned plug-in, and show the estimate survives varying windows and
polynomial orders [c213028d1]; and **falsify** it with the McCrary density test
and a continuity-of-covariates check, treating an RD like a randomized
experiment whose randomization must be empirically defended rather than assumed
[c213028d1].
