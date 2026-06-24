---
id: d42ec736c
topic: 02-statistical-causal-inference
title: "Online FDR Control for Streams of A/B Tests: Interleaving Always-Valid MAB p-values with LORD"
status: draft
---

## Thesis

Two existing findings protect a *single* continuously-monitored A/B test:
[dc588b7cc] grounds always-valid p-values and the mSPRT that keep Type I error
controlled at any data-dependent stopping time, and [d541a8e56] grounds the
confidence-sequence machinery that makes anytime-valid interval estimation work.
But an autonomous engine does not run one test — it runs a *stream* of tests over
time, the way an internet company tests many webpage variants over time or a
pharmaceutical company tests many treatments [ca971f6ec]. Once tests arrive as a
sequence, controlling each one's individual false-alarm rate is no longer enough:
the right target becomes controlling **false alarms across the whole family** —
i.e. the **false discovery rate (FDR)** [ca971f6ec]. This finding grounds that
family-level, continuous-monitoring complement on Yang, Ramdas, Jamieson &
Wainwright, *A framework for Multi-A(rmed)/B(andit) testing with online FDR
control* (arXiv:1706.05378; NeurIPS 2017) [ca971f6ec]. Together with [dc588b7cc]
and [d541a8e56] it closes the gap both of those findings explicitly flagged as
referenced-but-not-grounded: multiple-testing control under continuous
monitoring.

## Why single-test Type I control is not enough for a stream of tests

The problem the paper addresses is controlling false alarms when **multiple A/B
tests are run over time** [ca971f6ec]. A single test's Type-I guarantee bounds the
chance that *that* test falsely rejects; it says nothing about the accumulating
rate of false rejections once you run a continuously-arriving sequence of tests.
For a stream, the discipline that matters is **false-discovery-rate (FDR)
control** across the family [ca971f6ec]. The framework's stated aim is to combine
two things that are usually in tension and get "the best of both worlds: low
sample complexity and any-time online FDR control" [ca971f6ec].

## The framework: best-arm MAB instances interleaved with an online-FDR algorithm

The paper's construction replaces a sequence of A/B tests with a sequence of
**best-arm multi-armed-bandit (MAB) instances** that can be **continuously
monitored**, and **interleaves them with an online-FDR algorithm** [ca971f6ec].
The abstract states three contributions [ca971f6ec]:

1. reasonable definitions of a **null hypothesis** for MAB instances;
2. an **always-valid sequential p-value** for each MAB instance, which is what
   permits **continuous monitoring** of each test — the same always-valid
   discipline [dc588b7cc] grounds for one test, here attached to each member of
   the stream [ca971f6ec];
3. using the **rejection thresholds of the online-FDR algorithm as the confidence
   levels** fed to the MAB algorithms, which yields sample-optimality, high power,
   and low FDR at any time [ca971f6ec].

The third point is the load-bearing wiring: the online-FDR procedure and the
bandit procedures are not bolted together after the fact — the FDR procedure's
per-test rejection threshold *is* the confidence level each best-arm bandit runs
at [ca971f6ec].

## What is controlled: the modified FDR (mFDR)

The quantity the framework controls is the **modified FDR (mFDR)** — the ratio of
the *expected* number of false discoveries to the *expected* number of total
discoveries [ca971f6ec]. (FDR and its variants such as mFDR are standard
criteria for multiple testing [ca971f6ec].) Taking the ratio of expectations,
rather than the expectation of the ratio, is what makes the quantity tractable to
control online as tests stream in.

## How LORD's alpha-wealth / alpha-investing mechanism works

The online-FDR algorithm the paper uses is **LORD**, from Javanmard &
Montanari [ca971f6ec]. Given a desired level α, LORD starts with an initial
**"α-wealth"** `W(0) < α` [ca971f6ec]. Based on an infinite sequence `{γ_i}` that
sums to one, together with the time of the most recent discovery, LORD **spends a
fraction γ of the remaining α-wealth to test** each new hypothesis [ca971f6ec].
This is an **alpha-investing / alpha-wealth** mechanism: each test consumes some
of a finite error budget, and each rejection (discovery) earns wealth back, so a
procedure that keeps making true discoveries can keep affording to test
[ca971f6ec]. LORD is not the only choice — other online-FDR procedures could be
substituted for essentially the same guarantees [ca971f6ec].

The sufficient condition for the guarantee is general: **generalized
alpha-investing** procedures such as LORD control mFDR provided the null
p-values are **conditionally super-uniform** [ca971f6ec]. This is exactly why
contribution (2) matters — the always-valid sequential p-value supplied for each
MAB instance is what lets these p-values satisfy the super-uniformity premise
under continuous monitoring, so the alpha-investing controller's mFDR guarantee
holds at any time [ca971f6ec].

## How this completes the always-valid corner relative to [dc588b7cc] and [d541a8e56]

The three findings now tile the anytime-valid space. [dc588b7cc] gives the
test/p-value interface for *one* continuously-monitored test — always-valid
p-values and the mSPRT that keep Type I control at any stopping time. [d541a8e56]
gives the concentration-theoretic foundation — confidence sequences that stay
valid over an unbounded horizon. This finding adds the *family-wise extension*:
when you run *many* always-valid tests over time, you additionally need an
online-FDR controller, and the mechanism is LORD's alpha-investing scheme
interleaved with always-valid sequential p-values [ca971f6ec]. The
load-bearing thesis is the union of the three: continuous monitoring of one test
needs always-valid p-values [dc588b7cc]; continuous monitoring of *many* tests
over time additionally needs online FDR control [ca971f6ec] — together they
deliver anytime-valid inference at the family level. This is precisely the
residual [dc588b7cc] recorded ("always-valid *multiple-testing* control
(FWER/FDR under continuous monitoring) is mentioned but not grounded") and that
[d541a8e56] echoed.

## Gaps found

- **The exact LORD update equation is not transcribed.** The PDF→markdown
  conversion garbles the inline math; only the prose-confirmed mechanics are used
  here — initial α-wealth `W(0) < α`, the `{γ_i}` summing to one, "spends a
  fraction γ of the remaining α-wealth," and rejection-earns-wealth [ca971f6ec].
  The coefficient-level update formula is deliberately not reconstructed.
- **Simulation numbers are not quoted.** The paper runs extensive simulations,
  but the tables are fragmented in conversion; no simulation figure is stated as
  load-bearing [ca971f6ec].
- **FWER under continuous monitoring is a different, stricter criterion this
  paper does not center on.** The framework controls mFDR (a false-*discovery*-rate
  variant), not the family-wise error rate; an engine that needs FWER-level
  control across a stream would require a separate primary [ca971f6ec].
