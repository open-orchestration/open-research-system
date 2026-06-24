---
id: d21f3389c
topic: 02-statistical-causal-inference
title: "Always-Valid Inference and the mSPRT: Controlling Type I Error When You Continuously Monitor an A/B Test"
status: rejected
---

<!-- REJECTED (ai-independent): efficiency claim mis-attributed as "Theorem 2,
M=O(log alpha^-1) => phi(M,alpha)->1"; the source's actual result is Proposition 2
with the inverse condition M/log(1/alpha)->infinity (three-regime analysis), and
no "Theorem 2"/"phi(M,alpha)" object exists. All other formulas (Def 1, Eq 1/3/7/8,
Thm 1 duality, martingale threshold) verified faithful. Superseded by dc588b7cc,
which corrects the efficiency section to the source's three patience regimes. -->

## Thesis

The companion finding [d740bae09] sizes a randomized experiment under the
*fixed-horizon* assumption: commit to a per-variant sample size *n* in advance,
run until you reach it, then test once. That sizing — `n = 16σ²/Δ²` for 80%
power, after Kohavi et al. — is correct only under that discipline. The moment
an operator "peeks" at the running test and decides to stop based on what they
see, the fixed-horizon Type I guarantee is void: continuous monitoring inflates
false positives. This finding grounds the continuous-monitoring complement on
its peer-reviewed primary — Johari, Pekelis & Walsh, *Always Valid Inference*
(Stanford; *Operations Research*; arXiv:1512.04922) [c6c0f3857].

(Body archived; the promoted, corrected version of this finding is dc588b7cc.)
