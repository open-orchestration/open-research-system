---
id: dc588b7cc
topic: 02-statistical-causal-inference
title: "Always-Valid Inference and the mSPRT: Controlling Type I Error When You Continuously Monitor an A/B Test"
status: draft
---

## Thesis

The companion finding [d740bae09] sizes a randomized experiment under the
*fixed-horizon* assumption: commit to a per-variant sample size *n* in advance,
run until you reach it, then test once. That sizing — `n = 16σ²/Δ²` for 80%
power, after Kohavi et al. — is correct only under that discipline. The moment
an operator "peeks" at the running test and decides to stop based on what they
see, the fixed-horizon Type I guarantee is void: continuous monitoring inflates
false positives. This finding grounds the continuous-monitoring complement on
its peer-reviewed primary — Johari, Pekelis & Walsh, *Always Valid Inference*
(Stanford; *Operations Research*; arXiv:1512.04922) [c6c0f3857] — which defines
*always valid* p-values and confidence intervals that retain Type I control at
*any* data-dependent stopping time, and constructs them with the mixture
sequential probability ratio test (mSPRT). Where [d740bae09] tells the engine
how much data a *single* test needs, this finding tells it what to do when it
cannot resist looking early — the regime an autonomous engine continuously
monitoring its own experiments will almost always be in.

## Why peeking breaks fixed-horizon Type I control

A standard A/B test is analyzed via frequentist p-values and confidence
intervals, "but these inferences are wholly unreliable if users endogenously
choose sample sizes by continuously monitoring their tests" [c6c0f3857]. The
paper makes the mechanism precise. A *fixed horizon p-value process* for a chosen
sample size *n* is any `(F_n)`-measurable `p_n` that is *super-uniform* under the
null — Eq. (1): for all `s ∈ [0,1]`, `P_{θ0}(p_n ≤ s) ≤ s` [c6c0f3857]. That
bound is exactly what lets the user reject when `p_n ≤ α` and obtain a level-α
test. Under "the default fixed horizon testing approach, we restrict to decision
rules `(n, δ)`, where the stopping time is required to be **deterministic**," and
the objective is to maximize power at that fixed *n* [c6c0f3857].

The super-uniformity in Eq. (1) is a statement about the *fixed index n only*. It
says nothing about what happens if the analyst is allowed to choose *which* `p_n`
to act on after watching the sequence `p_1, p_2, …` evolve. Peeking does exactly
that: it replaces the deterministic *n* with a data-dependent stopping time *T*,
and the level-α guarantee `P_{θ0}(p_n ≤ α) ≤ α` simply does not transfer from a
fixed *n* to a chosen *T*. The whole point of the paper's framework is to restore
control in that regime: its measures are built so that "Type I error is controlled
under any data-dependent rule the user might choose to stop the experiment (i.e.,
any stopping time for the data). Continuous monitoring does not inflate Type I
error" [c6c0f3857]. The contrast with the fixed-horizon default is the load-bearing
claim — the fixed-horizon p-value controls error at a deterministic *n*; an
always-valid p-value controls it at every stopping time at once.

## The always-valid p-value (Definition 1) and its duality with tests of power one

The paper's first contribution is the definition that closes the gap [c6c0f3857]:

> **Definition 1.** A sequence of fixed horizon p-values `(p_n)` is an *always
> valid p-value process* if, given any (possibly infinite) stopping time *T* with
> respect to `(F_n)`, there holds — Eq. (3): for all `s ∈ [0,1]`,
> `P_{θ0}(p_T ≤ s) ≤ s`.

So an always-valid process is a *sequence* of fixed-horizon p-values with the
extra property that super-uniformity survives evaluation at an arbitrary,
data-dependent stopping time *T*, not merely at a pre-committed index *n*
[c6c0f3857]. An analogous coverage requirement defines *always valid confidence
intervals* — a `(1−α)`-level always-valid CI keeps `P_θ(θ ∈ CI_T) ≥ 1−α` at any
stopping time, the interval counterpart of Eq. (2)'s fixed-horizon coverage
`P_θ(θ ∈ CI_n) ≥ 1−α` [c6c0f3857].

These processes are not constructed ad hoc; the paper establishes a *duality*
between always-valid p-values and sequential hypothesis tests (Wald 1945,
Siegmund 1985, Lai 2001) — specifically those sequential tests that "do not
accept `H_0` in finite time, known as *sequential tests of power one* (Robbins and
Siegmund 1974)" [c6c0f3857]. Theorem 1 makes the correspondence explicit: given a
sequential test `(T(α), δ(α))`, the construction `p_n = inf{α : T(α) ≤ n,
δ(α) = 1}` yields an always-valid p-value process, and conversely any always-valid
process induces a sequential test via `T̃(α) = inf{n : p_n ≤ α}` [c6c0f3857].
Under this duality "the natural policy of stopping the first time that the always
[valid] p-value process crosses the level α implements the corresponding sequential
test of power one" — which is why the framework can keep the familiar p-value
"user interface" while guaranteeing Type I control under continuous monitoring
[c6c0f3857].

## The mSPRT construction (Eq. 7 mixture statistic, Eq. 8 stopping rule)

The paper's main constructive tool is the *mixture sequential probability ratio
test* (mSPRT, Robbins 1970) [c6c0f3857]. The data are modeled as independent
observations from a single-parameter exponential family `X_i ~ F_θ`, testing a
simple null `H_0: θ = θ_0` against the composite alternative `H_1: θ ≠ θ_0`
[c6c0f3857]. The mSPRT is parameterized by a *mixing distribution* `H` over the
parameter space `Θ`. For an observed sample average `S_n` up to time *n*, the
likelihood ratio of `θ` against `θ_0` is `(f_θ(S_n) / f_{θ0}(S_n))^n`, and the
**mixture likelihood ratio** with respect to `H` is — Eq. (7):

```
Λ^H_n(S_n) = ∫_Θ [ f_θ(S_n) / f_{θ0}(S_n) ]^n dH(θ)
```

i.e. a mixture, over potential alternative values `θ` drawn according to `H`, of
the likelihood ratio of the alternative to the null based on the first *n*
observations [c6c0f3857]. (The source is a lossy PDF→markdown conversion; the
exponent *n* and the subscripted `S_n`, `θ_0` are mangled in the raw text — the
canonical form is stated here, and the per-sample-average likelihood-ratio-to-the-
*n* structure is confirmed by the surrounding prose.)

The mSPRT then stops the first time this accumulated evidence crosses a fixed
threshold — Eq. (8):

```
T^H(α) = inf{ n : Λ^H_n(S_n) ≥ α^{-1} },   δ^H(α) = 1{ T^H(α) < ∞ }
```

[c6c0f3857]. "The choice of threshold `α^{-1}` on the likelihood ratio ensures
Type I error is controlled at level α, via standard martingale techniques
(Siegmund 1985)" — `Λ^H_n` is a martingale under `H_0`, so the probability it
ever crosses `α^{-1}` is at most α [c6c0f3857]. Intuitively `Λ^H_n(S_n)`
"represents the evidence against `H_0` in favor of a mixture of alternative
hypotheses, based on the first *n* observations," and the test rejects whenever
that evidence ever becomes large enough [c6c0f3857]. Because it is a test of power
one, feeding it through the Theorem 1 duality produces an always-valid p-value
process whose `α`-level stopping rule *is* the mSPRT — restoring the peek-proof
guarantee of Definition 1.

## Efficiency: three patience regimes, and the role of the mixing distribution

A peek-proof test is only useful if it does not waste data. The paper measures a
user by two profiles over the non-null effects `θ ≠ θ_0`: the **power profile**
`ν(θ) = P_θ(δ = 1)` (which she wants to maximize) and the **relative run-length
profile** `ρ(θ) = E_θ(T)/M`, the expected run-time as a fraction of the maximum
run-length the user is willing to tolerate (which she wants to minimize)
[c6c0f3857]. Here *M* is the user's **patience** — the maximum failure time at
which she gives up; a larger *M* signals willingness to run longer to detect
smaller effects [c6c0f3857]. *Perfect* efficiency would be `ρ(θ) = 0` and
`ν(θ) = 1` for all `θ ≠ θ_0`, which "is generally unattainable for feasible
decision rules"; the paper studies the best achievable performance in the limit
`α → 0` [c6c0f3857].

In that limit the efficiency analysis "divides into three cases depending on the
relative values of `M` and `log(1/α)`" [c6c0f3857]:

- **"Aggressive" users, `M ≫ log(1/α)`** — *M* is large relative to the evidence
  threshold. Here "any mSPRT asymptotically recovers perfect efficiency in the
  limit where α is small," because the user is willing to wait far longer than the
  evidence requires [c6c0f3857].
- **"Conservative" users, `M ≪ log(1/α)`** — *M* is small relative to the
  threshold. "Experimentation is not productive: the user is unwilling to wait long
  enough to detect any effects," so any mSPRT trivially performs as well as any
  feasible rule (efficiency is a weak requirement) [c6c0f3857].
- **"Goldilocks" users, `M ∼ log(1/α)`** — "the interesting case, where
  experimentation is worthwhile but statistical analysis is non-trivial"
  [c6c0f3857]. The paper's main efficiency result is that **in this regime any
  mSPRT has relative efficiency approaching unity as `α → 0`**, and moreover the
  mSPRT satisfies a *first-order optimality* property: "there is no other feasible
  decision rule that yields a relative run-length that is lower on some non-null
  effects, while meeting the size constraint α and yielding higher power at all
  non-null effects" [c6c0f3857].

The asymptotic run-time itself is pinned down — Eq. (10): for a fixed mixing
distribution `H`, as `α → 0`, `T^H(α) / log(1/α) → I(θ, θ_0)^{-1}` (in probability
and in `L²`), where `I(θ, θ_0) = (θ − θ_0)·ψ'(θ) − (ψ(θ) − ψ(θ_0))` and `ψ` is the
log-partition function of the exponential family [c6c0f3857]. So run-time scales
like `log(1/α)` divided by an information rate — tighter α costs proportionally
more samples, and easier-to-detect effects (larger `I`) stop sooner.

That the *first-order* efficiency holds for **any** mixing distribution is why the
mSPRT is robust to the choice of `H`; the mixing distribution "plays an important
role in **second order** performance" [c6c0f3857]. The paper therefore picks among
mSPRTs by choosing the `H` that minimizes expected run-length for `(M, α)` users in
the Goldilocks regime, and finds that the run-length-minimizing mixture "involves
'matching' the prior in an appropriate sense": in a Bayesian setting where effect
sizes are drawn from a prior, the optimal mixture — for normal data — approximately
matches the variance of the mixing distribution to the variance of the prior
distribution of effect sizes [c6c0f3857]. So `H` is best read as a prior over
plausible effect sizes, and the practical tuning rule is prior-matching. Numerics
show the choice is both impactful and robust across a wide range of conditions
[c6c0f3857]. This methodology was implemented in a large-scale commercial A/B
testing platform and used to analyze hundreds of thousands of experiments
[c6c0f3857].

## The bridge to fixed-horizon sizing: when each applies

The two findings meet at one precise point. An always-valid p-value process *is*
a sequence of fixed-horizon p-values (Definition 1 begins "a sequence of fixed
horizon p-values `(p_n)`") [c6c0f3857]; the fixed-horizon p-value that [d740bae09]
implicitly tests against is the *n*-th element of such a process, valid as a
standalone test only under a *deterministic* stopping rule — exactly the
restriction the paper names for fixed-horizon testing [c6c0f3857]. The decision
rule is therefore clean:

- **Commit to one pre-registered *n*, look once.** Use Kohavi's sizing
  [d740bae09]: pick the OEC and its variance `σ²`, the minimum detectable change
  `Δ`, the power; compute `n = 16σ²/Δ²` (or `21σ²/Δ²` for 90% power); run to *n*;
  test once at `p_n ≤ α`. Type I error is controlled because the stopping time is
  deterministic [c6c0f3857]. This is maximally data-efficient *if* you can actually
  hold to it.

- **Monitor continuously / stop when convinced.** Use always-valid inference: the
  mSPRT (Eq. 7–8), reporting an always-valid p-value and CI [c6c0f3857]. Type I
  error is then controlled at *whatever* data-dependent time you stop (Definition
  1). The efficiency cost of that freedom is asymptotically benign in the relevant
  regime — in the Goldilocks case `M ∼ log(1/α)` any mSPRT's relative efficiency
  approaches unity as `α → 0`, and the run-length-minimizing mixture is found by
  matching `H` to your prior over effect sizes [c6c0f3857].

For an autonomous research engine the practical implication is sharp: a system
that streams results and reacts to them is *by construction* choosing a
data-dependent stopping time, so Kohavi's fixed-horizon sizing [d740bae09] is the
wrong contract for it the moment it acts early. The always-valid / mSPRT machinery
is the contract that matches how such an engine actually behaves — keep the
p-value/CI interface, swap the underlying statistic for the mixture-likelihood-ratio
construction, and continuous monitoring stops inflating false positives.

## Gaps found

- **Interference / SUTVA-violating sizing (gd78c76ea) is NOT addressed by this
  source.** The always-valid result is derived for *independent* observations from
  an exponential family [c6c0f3857]; it assumes units do not interfere. Network
  effects, marketplace cannibalization, and other SUTVA violations are out of
  scope here and need a separate primary.
- **Finite-*M* and non-exponential-family behavior is only partially grounded.**
  The efficiency results are `α → 0` asymptotics over a single-parameter
  exponential family, split by the `M`-vs-`log(1/α)` regime [c6c0f3857]; the paper
  studies finite-*M* performance empirically rather than with a closed guarantee,
  and always-valid inference for broader parametric / non-parametric settings (e.g.
  LIL-based confidence sequences, Howard et al.) is referenced but not derived
  here — a candidate deepening if the engine needs guarantees outside this family.
- **Always-valid *multiple-testing* control (FWER/FDR under continuous
  monitoring) is mentioned but not grounded.** The paper notes always-valid
  p-values yield sequential multiple-hypothesis control [c6c0f3857]; the
  mechanics are not extracted here and could anchor a separate finding tying this
  to the familywise-error discipline in [d740bae09].
