---
id: dd90b2c09
topic: 02-statistical-causal-inference
title: "The definitive anytime-valid testing kit: test continuously without inflating error (confidence sequences, mSPRT, online FDR)"
status: draft
---

## Thesis

An autonomous research engine that streams experiments and reacts to them is, by
construction, *peeking*: it chooses data-dependent stopping times. The classical
fixed-horizon discipline — commit to a sample size *n* in advance, look once —
is the thing it cannot hold to, and the moment it acts early the fixed-horizon
Type I guarantee is void. This finding composes the three contributing findings
that, together, supply the complete replacement contract: [d541a8e56]
(nonparametric, LIL-rate **confidence sequences**), [dc588b7cc] (**always-valid
p-values and the mSPRT** for one continuously-monitored test), and [d42ec736c]
(**online FDR via LORD** for a stream of tests). The synthesis is a single
decision rule organized by *what* the operator is monitoring: **one estimated
quantity → a confidence sequence; one hypothesis tested under peeking → an
always-valid p-value / mSPRT; many hypotheses arriving as a stream → an
online-FDR controller layered on top.** Each layer relaxes the same
fixed-horizon assumption, and the first two are duals — both are martingale-based
time-uniform guarantees viewed from the interval side and the test side.

## Provenance

All three layers rest on strong arXiv primaries with no secondary material in
between, so the discipline here is faithfulness/precision rather than
provenance-tiering. Layer 1 is Howard, Ramdas, McAuliffe & Sekhon,
*Time-uniform, nonparametric, nonasymptotic confidence sequences*
(arXiv:1810.08240) [c90529a6e]. Layer 2 is Johari, Pekelis & Walsh, *Always
Valid Inference* (arXiv:1512.04922) [c6c0f3857]. Layer 3 is Yang, Ramdas,
Jamieson & Wainwright, *A framework for Multi-A(rmed)/B(andit) testing with
online FDR control* (arXiv:1706.05378) [ca971f6ec]. The PDF→markdown conversions
are lossy on subscripts and inline math; every formula below was re-grepped
whitespace-insensitively against the source bytes, and any token mangled in
conversion is stated in canonical form with an explicit lossiness note.

## Layer 1 — One estimated quantity, watched over time: a confidence sequence

When the operator is tracking a *single* unknown quantity (a treatment effect, a
mean) and wants an interval valid at every peek, the object is a **confidence
sequence (CS)**: a sequence of confidence sets `(CI_t)` for the target `θ_t` with
a *time-uniform* coverage guarantee, valid simultaneously across the whole
unbounded horizon rather than at one pre-committed index — the `∀ t ≥ 1` sits
*inside* the probability [c90529a6e]:

```
P(∀ t ≥ 1 : θ_t ∈ CI_t) ≥ 1 − α
```

(The membership term `θ_t ∈ CI_t` is mangled in the byte conversion; the
quantifier `∀ t ≥ 1` and the `1 − α` bound are re-grepped clean, and the
canonical eq (1) coverage statement is what is cited [c90529a6e].) This uniform
quantifier is exactly what licenses arbitrary, data-dependent stopping —
fixed-sample CLT intervals satisfy no such thing, and continuously monitoring
with fixed-sample inference inflates Type I error substantially [c90529a6e].

The concrete sub-Gaussian CS for a 1-sub-Gaussian mean is the closed-form
"stitched" bound, eq (2) [c90529a6e]:

```
µ̂_t  ±  1.7 · √[ ( loglog(2t) + 0.72·log(10.4/α) ) / t ]
```

The multiplier `1.7`, the term `loglog(2t)`, and `0.72·log(10.4/α)` are all
re-grepped verbatim from the bytes [c90529a6e]. Its asymptotic rate is
`O(√(t⁻¹·loglog t))`, which matches the lower bound implied by the **law of the
iterated logarithm (LIL)** — a finite-LIL boundary [c90529a6e].

The load-bearing design trade-off the operator inherits is **linear vs.
curved/stitched** boundaries. A linear uniform boundary is valid uniformly over
time and nonasymptotically but **does not shrink to zero width**; the confidence
radius for the mean is asymptotically zero-width only if the boundary is
*sublinear* [c90529a6e]. The curved boundary is built by *stitching* — breaking
time into geometric epochs, optimizing a linear bound per epoch, and union-bounding
(the "peeling" argument) — yielding a CS that is uniformly and nonasymptotically
valid **while also shrinking toward zero** [c90529a6e]. So the operator's choice
is: a linear boundary is simplest and time-uniform but never converges; a curved
one buys both validity and shrinkage.

## Layer 2 — One hypothesis under optional stopping: always-valid p-values + mSPRT

When the operator is *testing* one hypothesis rather than estimating, and wants
to stop the first time the evidence is convincing, the object is an **always-valid
p-value**. A fixed-horizon p-value process is super-uniform under the null at a
fixed index — eq (1), `∀ s ∈ [0,1] : P_{θ0}(p_n ≤ s) ≤ s` [c6c0f3857] — but that
says nothing about evaluating the process at a *data-dependent* stopping time. An
always-valid p-value closes the gap: super-uniformity survives evaluation at *any*
stopping time *T* — eq (3), `P_{θ0}(p_T ≤ s) ≤ s` for any stopping time *T*
[c6c0f3857]. (In the byte conversion the subscripts `θ0`, `n`, `T` are stripped:
the source shows `p(p ≤ s) ≤ s` as eq (1) and again as eq (3); the canonical
indexed forms are cited, with this lossiness noted.) The framework is built so
"Type I error is controlled under any data-dependent rule the user might choose to
stop the experiment (i.e., any stopping time for the data)" [c6c0f3857].

The constructive engine is the **mixture SPRT (mSPRT)**. For independent
observations from a single-parameter exponential family, the **mixture likelihood
ratio** with respect to a mixing distribution `H` is — eq (7) [c6c0f3857]:

```
Λ^H_n(S_n) = ∫_Θ [ f_θ(S_n) / f_{θ0}(S_n) ]^n dH(θ)
```

and the test stops the first time this crosses a fixed threshold — eq (8)
[c6c0f3857]:

```
T^H(α) = inf{ n : Λ^H_n(S_n) ≥ α^{-1} }
```

(The exponent `n` and subscripts are mangled in the bytes; the re-grepped tokens
confirm the eq (7) mixture integral `λh(s)=∫…dH(θ)` and the eq (8) stopping rule
`inf{n : λh(s) ≥ α−1}` — the canonical forms are cited with the lossiness note.)
The threshold `α⁻¹` controls Type I error at level α "via standard martingale
techniques" — `Λ^H_n` is a martingale under `H_0`, so the probability it ever
crosses `α⁻¹` is at most α [c6c0f3857]. Because the mSPRT is a *test of power one*
(it does not accept `H_0` in finite time), feeding it through the paper's
test↔p-value duality yields an always-valid p-value process whose α-level stopping
rule *is* the mSPRT [c6c0f3857].

Efficiency is governed by the operator's **patience** *M* relative to `log(1/α)`,
splitting into three regimes [c6c0f3857]: "aggressive" users (`M ≫ log(1/α)`)
recover perfect efficiency as α → 0; "conservative" users (`M ≪ log(1/α)`) find
experimentation unproductive; and the "Goldilocks" regime (`M ∼ log(1/α)`) is the
interesting case, where any mSPRT's relative efficiency approaches unity as
α → 0 [c6c0f3857]. First-order efficiency holds for *any* mixing distribution, so
`H` matters only at second order and is best read as a prior over effect sizes
[c6c0f3857].

## Layer 3 — Many hypotheses as a stream: online FDR (LORD)

When the engine runs not one test but a *stream* of tests over time, bounding each
test's individual Type I error is no longer enough — the accumulating rate of
false rejections across the family is what matters, i.e. **false discovery rate
(FDR)** control [ca971f6ec]. The framework replaces each A/B test with a best-arm
multi-armed-bandit instance that can be continuously monitored, attaches an
**always-valid sequential p-value** to each (the same always-valid discipline of
Layer 2, here applied per stream member), and **interleaves them with an
online-FDR algorithm** to get "the best of both worlds: low sample complexity and
any-time online FDR control" [ca971f6ec]. The load-bearing wiring is contribution
(3): the online-FDR procedure's **rejection thresholds are used as the confidence
levels** fed to the bandit algorithms [ca971f6ec].

The quantity controlled is the **modified FDR (mFDR)** — the ratio of the expected
number of false discoveries to the expected number of total discoveries
[ca971f6ec]; taking the ratio of expectations (rather than the expectation of the
ratio) is what makes it tractable online. The controller is **LORD**
(Javanmard & Montanari): it starts with an initial **"α-wealth"** `W(0) < α`,
and on a sequence `{γ_i}` summing to one it **spends a fraction γ of the remaining
α-wealth** to test each new hypothesis, earning wealth back on each rejection — an
**alpha-investing / alpha-wealth** scheme, so a procedure that keeps making true
discoveries can keep affording to test [ca971f6ec]. The sufficient condition is
general: generalized alpha-investing procedures such as LORD control mFDR provided
the null p-values are **conditionally super-uniform** [ca971f6ec] — which is
precisely why Layer 2's always-valid sequential p-value is the load-bearing
premise: it is what lets each stream member's p-value satisfy super-uniformity
under continuous monitoring, so the mFDR guarantee holds at any time [ca971f6ec].

## How they compose

The three layers are a single decision rule keyed to *what* is being monitored:

- **Tracking one estimated quantity over time → confidence sequence
  [c90529a6e].** Use the closed-form sub-Gaussian CS (eq 2) for a mean, or a
  curved/stitched boundary when you need the interval to actually shrink. Read off
  an interval at any peek; coverage holds across the whole horizon.
- **Testing one hypothesis with peeking → always-valid p-value / mSPRT
  [c6c0f3857].** Keep the familiar p-value/CI interface, swap the underlying
  statistic for the mixture likelihood ratio `Λ^H_n`, and stop when it crosses
  `α⁻¹`. Type I error is controlled at whatever data-dependent time you stop.
- **A stream of such tests → online FDR on top [ca971f6ec].** Wrap an
  alpha-investing controller (LORD) around the always-valid per-test p-values and
  let its rejection thresholds set each test's confidence level, controlling mFDR
  across the family at any time.

The first two layers are **dual descriptions of the same martingale machinery**.
An always-valid p-value process *is* a sequence of fixed-horizon p-values whose
super-uniformity survives any stopping time `P_{θ0}(p_T ≤ s) ≤ s` [c6c0f3857]; a
confidence sequence is the interval-side statement of the same time-uniform
guarantee, `P(∀ t ≥ 1 : θ_t ∈ CI_t) ≥ 1 − α` [c90529a6e] — both rest on
martingale concentration (the mSPRT's `Λ^H_n` is a martingale under `H_0`
[c6c0f3857]; Howard's CSs are time-uniform extensions of Cramér–Chernoff
concentration [c90529a6e]). What all three relax is the *same* fixed-horizon
discipline — commit to *n*, look once — under which a fixed-index super-uniform
p-value `P_{θ0}(p_n ≤ s) ≤ s` [c6c0f3857] is valid only because the stopping time
is deterministic. The kit is what you reach for the moment the engine cannot hold
to that discipline.

## Honest limits

- **Independence / sub-Gaussian (exponential-family) assumptions.** The Layer-1
  closed-form CS is for i.i.d. 1-sub-Gaussian observations [c90529a6e]; the
  always-valid mSPRT result is derived for *independent* observations from a
  single-parameter exponential family [c6c0f3857]. Interference / SUTVA-violating
  settings (network effects, marketplace cannibalization) are out of scope for all
  three and would need a separate primary.
- **mFDR is not FWER.** Layer 3 controls the **modified FDR** — a ratio-of-expectations
  *false-discovery*-rate variant [ca971f6ec] — not the family-wise error rate.
  (The Yang framework notes its procedure trivially "allows for anytime FWER, and
  thus FDR control" in its setting [ca971f6ec], but the centered, general guarantee
  is mFDR; an engine that genuinely needs FWER-level control across a stream should
  not treat mFDR control as equivalent.)
- **Linear-boundary non-shrinkage.** A CS built on a linear boundary is
  time-uniform and nonasymptotically valid but **never shrinks to zero width**
  [c90529a6e]; only a sublinear (curved/stitched) boundary delivers both validity
  and convergence. An operator who picks the simplest boundary inherits intervals
  that stay wide forever.
- **Conversion lossiness.** The eq (1)/eq (3) super-uniformity subscripts, the
  eq (7) exponent and the eq (8) subscripts are mangled in the PDF→markdown bytes;
  the verified tokens (`∀ s ∈ [0,1]`, `p(p ≤ s) ≤ s`, `λh(s)=∫…dH(θ)`,
  `inf{n : λh ≥ α−1}`) anchor the canonical forms cited above, and no
  coefficient-level boundary table beyond the re-grepped eq (2) constants is
  reconstructed.
