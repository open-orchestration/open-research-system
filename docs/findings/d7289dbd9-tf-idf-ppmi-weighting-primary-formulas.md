---
id: d7289dbd9
topic: 15-textbooks-longform
title: "Term-weighting formulas grounded: PMI/PPMI (Church-Hanks, Levy-Goldberg) and tf-idf-in-NLP (SLP3 Ch.11), with the word2vec ↔ shifted-PMI bridge"
status: draft
---

# Term-weighting formulas grounded: PMI/PPMI and tf-idf-in-NLP, plus the word2vec ↔ shifted-PMI bridge

Two prior 15 findings left named formula gaps that this finding closes on genuine
primaries. `ddc396092` (vector semantics from SLP3 Ch.5) grounded the
distributional hypothesis, cosine, and dense word2vec/SGNS embeddings, but its
own scope note recorded that Ch.5 **mentions PPMI only in passing** — as the
implicit weighting behind word2vec, citing "Levy and Goldberg, 2014" — and gives
**no defining formula** for PMI or PPMI (gap `g1919d0da`). Separately, `ddc396092`
and `d2fbbb962` both noted that SLP3 Ch.5 **defers tf-idf to its Chapter 11**,
which was not yet ingested (gap `g857b90f5`); `d2fbbb962` grounds tf-idf for
*ranked retrieval* on the Manning–Raghavan–Schütze IR-book, but not the SLP3 NLP
framing. This finding deepens both: it grounds (1) the PMI defining formula on its
computational-linguistics origin (Church & Hanks 1990) [cc475631e], (2) the PPMI
defining formula and the word2vec↔shifted-PMI
result on the exact primary SLP3 Ch.5 defers to (Levy & Goldberg 2014), and (3) the
tf-idf and tf-idf-cosine formulas in the NLP setting on SLP3 Ch.11. It does **not**
re-derive `d2fbbb962`'s IR-book ranked-retrieval content — the SLP3 Ch.11 material
here is the NLP-textbook framing of the same tf-idf primitive, added alongside it.

## Sub-questions

1. **Method** — how is (pointwise) mutual information defined and interpreted at
   its computational-linguistics origin (Church-Hanks)?
2. **Method** — how does Levy-Goldberg define PMI empirically and PPMI, and why is
   the positive clip needed (sparsity / `log 0` undefined)?
3. **Method / bridge** — what exactly is the word2vec↔shifted-PMI result that
   grounds "PPMI as word2vec's implicit weighting"?
4. **Method** — how does SLP3 Ch.11 define tf, idf, tf-idf, and the tf-idf cosine
   relevance score?
5. **Contrast** — how does association weighting (PMI/PPMI on word-context counts)
   differ in purpose from salience weighting (tf-idf on term-document counts)?

## Method — PMI at its origin: the "association ratio" (Church-Hanks 1990)

Church & Hanks introduce an **association ratio** for estimating word-association
norms from corpora, built on the information-theoretic notion of **mutual
information** [cc475631e]. Attributing the definition to Fano (1961), they state:
if two points (words) *x* and *y* have probabilities *P(x)* and *P(y)*, then their
mutual information *I(x,y)* is defined as [cc475631e]:

> **I(x,y) = log₂ [ P(x,y) / ( P(x)·P(y) ) ]**

i.e. the log (base 2) of the ratio between the joint probability of observing *x*
and *y* together and the product of the probabilities of observing them
independently (chance) [cc475631e]. Joint probabilities *P(x,y)* are estimated by
counting the number of times *x* is followed by *y* within a **window of w words**,
*f_w(x,y)*, and normalizing by corpus size *N*; the window-size parameter lets one
probe associations at different distances [cc475631e].

The **sign and magnitude carry the interpretation** [cc475631e]:

- If there is a genuine association, *P(x,y)* ≫ chance *P(x)·P(y)*, so **I(x,y) ≫ 0**.
- If there is no interesting relationship, *P(x,y)* ≈ *P(x)·P(y)*, so **I(x,y) ≈ 0**.
- If *x* and *y* are in **complementary distribution**, *P(x,y)* ≪ *P(x)·P(y)*,
  forcing **I(x,y) ≪ 0**.

Church & Hanks also flag an estimation caveat that becomes the through-line to the
PPMI clip: the association ratio is **unstable when counts are very small**, and
they discard pairs with *f(x,y)* ≤ 5; moreover, although *I(x,y)* ≪ 0 *predicts*
complementary distribution, "we are rarely able to observe I(x,y) ≪ 0 because our
corpora are too small" — the negative tail is the least reliable region of the
statistic [cc475631e]. This is the canonical computational-linguistics origin that
later NLP work (including SLP3 and Levy-Goldberg) cites for PMI.

## Method — PMI empirically and PPMI (Levy-Goldberg 2014)

Levy & Goldberg restate the same measure in the skip-gram word/context setting.
With *D* the collection of observed (word, context) pairs, `#(w,c)` the count of
the pair, and `#(w)`, `#(c)` the marginals, PMI measures association by the log
ratio of joint to marginal probabilities, **estimated empirically** as [c8860abb2]:

> **PMI(w,c) = log [ #(w,c)·|D| / ( #(w)·#(c) ) ]**   (their Eq. 10)

They explicitly note this use of PMI as an association measure in NLP "was
introduced by Church and Hanks" — confirming the lineage above [c8860abb2].

The **motivation for the positive clip** is concrete and load-bearing. The PMI
matrix M^PMI has rows full of word-context pairs that were *never observed*, for
which `PMI(w,c) = log 0 = −∞` — i.e. the raw PMI is **undefined / negative-infinite
on the unobserved cells**, which dominate a real co-occurrence matrix [c8860abb2].
Even among observed pairs, a frequent pair seen only once gets a strongly negative
entry, whereas an unobserved frequent pair gets 0 — an inconsistency [c8860abb2].
The "sparse and consistent alternative from the NLP literature" is the **positive
PMI (PPMI) metric**, replacing all negative values by 0 [c8860abb2]:

> **PPMI(w,c) = max( PMI(w,c), 0 )**   (their Eq. 11)

This both **resolves the `log 0 = −∞` problem** (unobserved/negative cells become
0) and yields a **sparse** matrix [c8860abb2]. Levy & Goldberg add an intuition
mirroring Church-Hanks's unreliable-negative-tail caveat: humans easily produce
positive associations ("Canada"/"snow") but struggle to invent negative ones
("Canada"/"desert"), so perceived similarity is driven more by shared positive
context than by shared negative context — making it reasonable to discard
negatively-associated contexts as "uninformative" (0) [c8860abb2]. They note PPMI
empirically performs very well on semantic-similarity tasks [c8860abb2].

This is precisely the **defining PPMI/PMI treatment that `ddc396092` lacked**: that
finding could only report PPMI as a one-word aside; Eqs. 10–11 here are the formulas
behind it.

## Method / bridge — word2vec ↔ shifted-PMI (Levy-Goldberg Eq. 7)

The headline result of Levy & Goldberg is that **skip-gram with negative sampling
(SGNS)** — the algorithm `ddc396092` grounds from SLP3 Ch.5 — is *implicitly
factorizing a word-context PMI matrix shifted by a global constant* [c8860abb2].
For word vector **w⃗** and context vector **c⃗**, SGNS's objective is optimized by
setting their dot product to a shifted PMI value, which (in matrix form, their
Eq. 7) reads [c8860abb2]:

> **M_SGNS = W·C ,  with  w⃗·c⃗ = PMI(w,c) − log k**

where *k* is the negative-sampling count. For **k = 1**, SGNS factorizes the plain
word-context **PMI matrix M^PMI** (association measured by `f(w,c) = PMI(w,c)`);
for **k > 1**, it factorizes a **shifted PMI matrix**,
**M^PMI_k = M^PMI − log k** [c8860abb2]. Because the dense shifted-PMI matrix is
impractical to use directly, Levy & Goldberg approximate it with the **sparse
positive (shifted-PPMI) matrix**, which is far better at optimizing SGNS's
objective and slightly outperforms word2vec-derived vectors on several tasks; they
further propose SVD over the shifted-PPMI matrix [c8860abb2]. (For completeness and
non-load-bearing: they show a parallel result casting NCE as factorizing a shifted
log-conditional-probability matrix [c8860abb2].)

This is the **explicit bridge** that `ddc396092` named but could not show: word2vec
embeddings are not an unrelated method to PPMI count weighting — SGNS *is* (up to
the `−log k` shift and a low-rank approximation) a factorization of the PMI/PPMI
word-context matrix. So "PPMI as word2vec's implicit weighting" is grounded in
Eq. 7, not asserted [c8860abb2].

## Method — tf-idf in NLP and the tf-idf cosine score (SLP3 Ch.11)

SLP3 Chapter 11 ("Information Retrieval and Retrieval-Augmented Generation"),
§11.1.2 "Term weighting: tf-idf and BM25", is the chapter Ch.5 deferred to. It
states that, rather than raw word counts, IR computes a **term weight** per
document word, and that **tf-idf** (the "-" is a hyphen, not a minus) "is the
product of two terms, the term frequency tf and the inverse document frequency
idf" [c1008a26d].

**Term frequency.** SLP3 uses **log-weighted** tf, since a word appearing 100 times
isn't 100× more relevant, and handles zero counts specially because `log 0` is
undefined. With `count(t,d)` the raw count, the chapter defines (Eq. 11.4)
[c1008a26d]:

> **tf_{t,d} = 1 + log₁₀ count(t,d)   if count(t,d) > 0 ,  else 0**

so tf = 0 at 0 occurrences, 1 at 1 occurrence, 2 at 10, 3 at 100, 4 at 1000, etc.
[c1008a26d]. (A footnote gives the alternative `tf_{t,d} = log₁₀(count(t,d)+1)`
used in earlier editions [c1008a26d].)

**Inverse document frequency.** With *df_t* the number of documents term *t* occurs
in and *N* the total number of documents, the idf weight (Sparck Jones 1972) is
(Eq. 11.5) [c1008a26d]:

> **idf_t = log₁₀ ( N / df_t )**

The fewer documents a term appears in, the higher this weight; a term occurring in
every document gets idf 0 [c1008a26d]. (Note this matches the IR-book idf form
`log(N/df_t)` grounded in `d2fbbb962` [c1008a26d], with SLP3 fixing log base 10;
the base does not affect ranking.)

**tf-idf.** The composite weight (Eq. 11.6) is the product [c1008a26d]:

> **tf-idf(t,d) = tf_{t,d} · idf_t**

**tf-idf cosine relevance score.** SLP3 scores a document *d* against a query *q* by
the **cosine similarity** from Ch.5 — the geometric similarity of the tf-idf vectors
(Eqs. 11.7–11.8) [c1008a26d]:

> **score(q,d) = cos(q,d) = ( q·d ) / ( |q|·|d| )**

equivalently the dot product of the unit-normalized query and document vectors
[c1008a26d]. Spelled out over tf-idf components (Eq. 11.9) [c1008a26d]:

> **score(q,d) = Σ_{t∈q} [ tf-idf(t,q) / √(Σ_{q_i∈q} tf-idf²(q_i,q)) ] · [ tf-idf(t,d) / √(Σ_{d_i∈d} tf-idf²(d_i,d)) ]**

This is the **NLP-textbook framing** of tf-idf: it extends `d2fbbb962`'s IR-book
*unnormalized* overlap `Score(q,d) = Σ tf-idf_{t,d}` to the **cosine-normalized**
tf-idf score, using the same cosine primitive `ddc396092` grounds from Ch.5
[c1008a26d]. SLP3 Ch.11 is also where the book's "classic method based on cosines of
sparse tf-idf vectors" is contrasted with modern dense BERT retrievers [c1008a26d].

## Contrast — association weighting vs. term-salience weighting

The two formula families weight *different* count matrices for *different* purposes,
and conflating them is a common error this contrast guards against:

- **PMI/PPMI** weight a **word-context (word-word) co-occurrence** matrix to measure
  **association** — how much more often two items co-occur than chance predicts
  [cc475631e][c8860abb2]. The reference distribution is **independence**
  (`P(x)·P(y)` / `#(w)·#(c)`); the question is "do these two words belong together?"
  The signed log-ratio, clipped to PPMI on the unobserved/negative tail, is the
  weighting that word2vec implicitly factorizes [c8860abb2].
- **tf-idf** weights a **term-document** matrix to measure **salience** — how
  characteristic a term is *of a document* relative to the collection [c1008a26d].
  Its two factors answer different questions than PMI: tf (within-document
  frequency, log-damped) and idf (cross-document rarity, `log N/df_t`). The product
  is highest for terms frequent in few documents, and feeds a cosine *document
  ranking*, not a word-association score [c1008a26d].

Both happen to use a logarithm and both fix a `log 0` / undefined-at-zero problem
(PPMI by `max(·,0)` on `log 0 = −∞` cells [c8860abb2]; tf by the
`count(t,d) > 0` guard [c1008a26d]), but the matrices, reference quantities, and
downstream uses are distinct: **association on word-context counts** versus **term
salience on term-document counts**.

## Provenance note

Every load-bearing formula traces to one of the three named primaries — the
computational-linguistics origin of PMI (Church & Hanks 1990, *Computational
Linguistics* 16(1), ACL J90-1003) [cc475631e]; the peer-reviewed paper that defines
PMI/PPMI empirically and proves the SGNS↔shifted-PMI result (Levy & Goldberg,
NeurIPS 2014) [c8860abb2]; and the official textbook chapter defining tf/idf/tf-idf
and the tf-idf cosine score (SLP3 3rd ed., draft of Jan 6 2026, Ch.11) [c1008a26d].
No blog or aggregator is cited. Equation numbers (Church-Hanks's Fano definition;
Levy-Goldberg Eqs. 7, 10, 11; SLP3 Eqs. 11.4–11.9) are the sources' own.

**Conversion fidelity.** All three sources are PDF→markdown conversions that
squashed whitespace and mangled inline math; formulas were recovered by
whitespace-insensitive search and are reported in their canonical form above. The
recoveries are clean and unambiguous: the Church-Hanks `I(x,y) = log₂[P(x,y)/(P(x)P(y))]`,
Levy-Goldberg Eqs. 10/11/7, and SLP3 Eqs. 11.4–11.9 were each legible in the
converted text (with spacing removed). No formula above is a guess; where a source
itself is lossy on a given relation, it is not reported as exact. (The Levy-Goldberg
equation labels "(9)"/"(10)" appear adjacent to the PMI text in the conversion; the
PMI empirical estimator is the source's Eq. 10 per its own prose ordering.)

## Gaps found

- **BM25 defining formula is still ungrounded in NLP framing.** SLP3 Ch.11 names
  BM25 as the common tf-idf variant but its full saturation/length-normalization
  formula was not extracted here; a focused BM25-from-Ch.11 finding would complete
  the §11.1.2 term-weighting trio (tf-idf grounded, BM25 named-only) [c1008a26d].
- **PPMI context-distribution smoothing (PPMI_α) is unaddressed.** Levy & Goldberg
  and later work discuss context-distribution smoothing / `k`-shift tuning of PPMI;
  only the base `max(PMI,0)` clip is grounded here. A source defining the smoothed
  variant remains uningested.
- **The SGNS sigmoid/logistic objective itself remains garbled.** `ddc396092`
  already flagged that SLP3 Ch.5's SGNS loss was lost in conversion; Levy-Goldberg
  give the local objective (Eq. 5 region) that the `w⃗·c⃗ = PMI − log k` optimum
  derives from, but a clean rendering of that per-pair loss was not extracted here.
