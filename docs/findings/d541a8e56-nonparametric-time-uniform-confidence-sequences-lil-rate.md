---
id: d541a8e56
topic: 02-statistical-causal-inference
title: "Confidence Sequences: The Nonparametric, LIL-Rate Machinery Behind Anytime-Valid A/B Inference"
status: draft
---

## Thesis

The continuous-monitoring finding [dc588b7cc] establishes *why* peeking at a
running A/B test breaks fixed-horizon Type I control and *how* the mixture-SPRT
restores an anytime-valid p-value/CI interface — but it grounds that on Johari,
Pekelis & Walsh, who **reference** the broader nonparametric, nonasymptotic
confidence-sequence machinery without deriving it. This finding grounds that
machinery on its peer-reviewed primary: Howard, Ramdas, McAuliffe & Sekhon,
*Time-uniform, nonparametric, nonasymptotic confidence sequences*
(arXiv:1810.08240, v9, August 2022) [c90529a6e]. A confidence sequence (CS) is a
sequence of confidence intervals that is uniformly valid over an unbounded time
horizon [c90529a6e]. The paper's contribution is CSs whose widths go to zero,
with nonasymptotic coverage under nonparametric conditions — the explicit
LIL-rate boundaries, the sub-Gaussian/sub-gamma generality, and the
line-vs-curved boundary tradeoff that the mSPRT finding takes as given
[c90529a6e]. Where [dc588b7cc] gives the test/p-value interface for one
exponential-family parameter, this finding supplies the concentration-theoretic
foundation that makes anytime-valid interval estimation work across far broader
settings.

## What a confidence sequence is, and how its guarantee differs from a fixed-horizon CI

For `α ∈ (0,1)`, a `(1−α)`-confidence sequence is a sequence of confidence sets
`(CI_t)`, typically intervals `CI_t = (L_t, U_t) ⊆ R`, computed after observing
the *t*-th unit for the unknown quantity of interest `θ_t`, satisfying a
**uniform** coverage guarantee — eq (1) [c90529a6e]:

```
P(∀ t ≥ 1 : θ_t ∈ CI_t) ≥ 1 − α
```

The quantifier `∀ t ≥ 1` *inside* the probability is the whole point: coverage
holds simultaneously across the entire unbounded horizon, not merely at one
pre-committed index *n* as with an ordinary fixed-horizon CI [c90529a6e]. This is
exactly what licenses arbitrary, data-dependent stopping. The paper lists the
properties it targets: (P1) nonasymptotic and nonparametric coverage for all
sample sizes without exact distributional assumptions or asymptotic
approximations; (P2) no final sample size need be chosen ahead of time; (P3) no
assumptions on the experimenter's stopping rule — "stop at any time according to
any rule"; and (P4) interval widths that shrink toward zero at a `1/√t` rate
(ignoring log factors), just as pointwise CIs do [c90529a6e]. The flexibility has
a cost the paper states plainly: these intervals are wider than ones relying on
asymptotics or a known stopping rule, and typical fixed-sample CLT intervals
satisfy none of (P1)–(P3) [c90529a6e].

The motivation is the same failure [dc588b7cc] describes from the other side:
continuously monitoring an experiment with fixed-sample inference inflates Type I
error substantially (the paper cites Armitage et al. 1969) [c90529a6e].

## The concrete sub-Gaussian confidence sequence, and its LIL rate

For i.i.d. observations `(X_t)` from a 1-sub-Gaussian distribution whose mean `µ`
is to be estimated, Theorem 1 yields the following `(1−α)`-confidence sequence —
eq (2), a special case of the more general bound (10) [c90529a6e]:

```
µ̂_t = (1/t) · Σ_{i=1}^t X_i  ±  1.7 · √[ ( loglog(2t) + 0.72·log(10.4/α) ) / t ]
```

The constants are re-grepped clean from the source bytes
(whitespace-insensitive): the multiplier `1.7`, the term `loglog(2t)`, and
`0.72·log(10.4/α)` all appear verbatim [c90529a6e]. The asymptotic rate of this
bound is `O(√(t⁻¹·loglog t))`, which **matches the lower bound implied by the law
of the iterated logarithm (LIL)**; nonasymptotic bounds of this form are called
*finite LIL bounds* [c90529a6e]. This is the precise machinery — the closed-form,
constant-explicit, LIL-rate boundary — that the mSPRT finding [dc588b7cc] refers
to as "LIL-based confidence sequences, Howard et al." but does not derive.

The generality is broad: the paper's tools (Theorems 1–3 and Lemma 2) all build
on the authors' general framework for uniform exponential concentration (Howard
et al. 2020), so the techniques apply to sub-Gaussian and Bernstein/sub-gamma
conditions, self-normalized processes, matrix martingales, Banach-space-valued
observations, and continuous-time scalar martingales [c90529a6e]. The abstract
draws three structural connections, in clean prose: confidence sequences are
**time-uniform extensions of the Cramér–Chernoff method** for exponential
concentration; provide **tight, nonasymptotic characterizations of the LIL**; and
**generalize the sequential probability ratio test (SPRT) to nonparametric
settings** [c90529a6e]. That third connection is the conceptual bridge to
[dc588b7cc]: the mSPRT is the parametric-exponential-family instance, while
Howard et al. supply the nonparametric generalization of the same SPRT idea.

## Why the linear boundary does not shrink while the curved one does

The load-bearing design tradeoff is between two boundary shapes. The simplest
uniform boundaries are **linear** (positive intercept and slope), formalized in
Lemma 1 (restated from Howard et al. 2020) [c90529a6e]. But the confidence radius
for the mean is `u(V_t)/t`, and since the variance process typically grows
`V_t = Θ(t)`, the radius is asymptotically zero-width **only if** the boundary is
sublinear, `u(v) = o(v)` — "we cannot achieve arbitrary estimation precision with
arbitrarily large samples unless the uniform boundary is sublinear" [c90529a6e].
A linear boundary fails this: from a concentration view the typical deviations of
`S_t` are only `O(√V_t)`, so a linear bound "will rapidly become loose for large
*t*" [c90529a6e]. Figure 1 states the consequence directly: the CS based on a
**linear boundary (Lemma 1) is valid uniformly over time and nonasymptotically,
but does not shrink to zero width**, whereas the CS based on a **curved boundary**
(the two-sided normal mixture, eq (14), qualitatively similar to the stitched
bound eq (2)) is uniformly and nonasymptotically valid **while also shrinking
toward zero width** [c90529a6e].

The curved boundary is built by *stitching*: Theorem 1 breaks time into
geometrically-spaced epochs `η^k ≤ V_t < η^{k+1}`, constructs a linear uniform
bound optimized for each epoch (per Lemma 1), and takes a union bound over all
crossing events — a standard "peeling" / chaining argument — yielding a smooth
analytic curved boundary as the upper envelope of the piecewise-linear pieces
(Figure 3) [c90529a6e]. Tight constants come from optimizing each epoch's linear
boundary at the geometric mean of the epoch endpoints [c90529a6e]. The paper also
notes a rate choice within the curved family: conjugate-mixture boundaries grow
at `O(√(t·log t))`, which "may be preferable to the slower `O(√(t·loglog t))`
rate" in practice — i.e. the LIL-rate boundary is not always the operationally
best one [c90529a6e].

## How this complements the mSPRT finding, and what it does not cover

[dc588b7cc] and this finding are two faces of anytime-valid inference. The mSPRT
finding owns the **test/p-value interface** for a single-parameter exponential
family: always-valid p-values (Definition 1), the mixture-likelihood-ratio
statistic, and the proof that peeking no longer inflates false positives
[dc588b7cc]. This finding owns the **interval-estimation / concentration
foundation**: the uniform-coverage definition (eq 1), the explicit LIL-rate
sub-Gaussian CS (eq 2), and the linear-vs-curved boundary tradeoff that makes
widths shrink [c90529a6e]. Both descend from the same SPRT lineage — Howard et
al. state their CSs *generalize the SPRT to nonparametric settings* [c90529a6e] —
which is precisely the generality [dc588b7cc] flags as referenced-but-not-derived
in its own gaps. They also share the fixed-horizon counterpoint of [d740bae09]:
that finding sizes a single pre-registered test (`n = 16σ²/Δ²`), valid only under
a deterministic stopping rule; confidence sequences are the contract for a system
that streams results and stops on a data-dependent rule.

The paper's applications confirm the scope: nonasymptotic sequential estimation
of the sample average treatment effect in the **Neyman–Rubin potential-outcomes
model**, and uniform matrix bounds / **covariance-matrix** confidence sequences
[c90529a6e]. It also derives a state-of-the-art empirical-Bernstein bound for
bounded observations [c90529a6e].

## Gaps found

- **Multiple-testing control under continuous monitoring (FWER/FDR) is NOT
  grounded by this source.** `FWER` does not appear in the source bytes at all,
  and `FDR` / "false discovery" appear only in citation context (Berman et
  al. 2018) — re-grepped: zero `FWER`, one `FDR`, two "false discover" hits, all
  references [c90529a6e]. This paper develops single-target confidence sequences,
  not familywise- or false-discovery-rate machinery. This is the same residual
  [dc588b7cc] records; it still needs a separate primary.
- **Interference / SUTVA-violating settings are out of scope.** The CS guarantees
  are for i.i.d. (or martingale-structured) observations; the term `SUTVA` does
  not appear in the bytes. Network effects and marketplace cannibalization need a
  separate source.
- **Exact mixture-boundary constants are lossy in the PDF→markdown conversion.**
  The eq (2) constants `1.7`, `0.72`, `10.4/α` and the eq (1) coverage statement
  are re-grepped clean and used as load-bearing; but the surrounding tables
  (eq 14 normal-mixture boundary, the Table 2 comparison of `A,B,C` constants,
  and the inline fraction layout of eq 2) are fragmented with `(cid:...)`
  artifacts. Boundary *formulas* beyond the verified tokens are stated only at the
  level the prose confirms (shape, rate, validity), not reconstructed
  coefficient-by-coefficient.
