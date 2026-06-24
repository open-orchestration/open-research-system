---
id: ddc396092
topic: 15-textbooks-longform
title: "Vector semantics grounded: the distributional hypothesis, cosine similarity, and dense (word2vec) embeddings from SLP3 Ch.5"
status: draft
---

# Vector semantics grounded: the distributional hypothesis, cosine similarity, and dense (word2vec) embeddings

A prior 15 finding (`d2fbbb962`) explicitly flagged cosine similarity as
**ungrounded** in this corpus: the ingest that was supposed to deliver the SLP3
vector-semantics chapter instead delivered the *Neural Networks* chapter, so the
cosine formula, the distributional hypothesis, and the move to dense embeddings
had no primary definition to rest on. That gap is named in the root SYNTHESIS and
in `d2fbbb962`'s own "Gaps found" section. This finding closes it by grounding
vector semantics directly on the genuine chapter: **SLP3 (Jurafsky & Martin,
*Speech and Language Processing*, 3rd ed., draft of January 6, 2026), Chapter 5
"Embeddings"** [c52f288b7]. Every load-bearing claim below is taken from that
chapter; no secondary source is cited.

A scope correction matters for trust. This 2026 draft is titled "Embeddings" and
its numbering has shifted from older SLP3 editions. In this chapter the chapter
itself **defers tf-idf to its Chapter 11** and treats **PPMI only in passing** (as
the weighting under which word2vec is an implicit matrix factorization) — neither
tf-idf nor PPMI is given a defining formula here [c52f288b7]. So the durable,
primary-grounded contribution of *this* chapter is: the distributional hypothesis,
the count-based co-occurrence matrices, the **cosine** metric (fully defined), the
sparse-vs-dense distinction, and **word2vec / skip-gram with negative sampling**.
The cosine grounding — the specifically-named open item — is the centerpiece.

## Sub-questions

1. **Method** — what is the distributional hypothesis, and how does it license
   representing word meaning as a vector of co-occurrence counts?
2. **Method** — how does the chapter define cosine similarity, and *why* must the
   dot product be normalized by vector length?
3. **Evidence** — what do count-based vectors look like (word-context vs
   term-document matrices), and why are they sparse?
4. **Method / bridge** — what do dense embeddings buy over sparse count vectors,
   and how does word2vec/skip-gram learn them?
5. **Scope** — what does this chapter *not* define (tf-idf, PPMI), and where does
   it defer them?

## Method — the distributional hypothesis

The chapter roots vector semantics in the **distributional hypothesis**: the idea
that words occurring in similar contexts tend to have similar meanings, i.e. "a
link between similarity in how words are distributed and similarity in what they
mean" [c52f288b7]. It attributes the hypothesis to 1950s linguists — Joos (1950),
Harris (1954), and Firth (1957) — who observed that synonyms such as *oculist* and
*eye-doctor* tended to occur in the same environment (e.g. near *eye* or
*examined*) [c52f288b7]. The chapter quotes Joos's formulation that a morpheme's
meaning is "by definition the set of conditional probabilities of its occurrence in
context with all other morphemes," and Firth's slogan that "you shall know a word
by the company it keeps" lineage; it also cites Wittgenstein's "the meaning of a
word is its use in the language" as philosophical underpinning [c52f288b7].

This hypothesis is what licenses the move to vectors: if meaning is distribution,
then a vector recording *what a word co-occurs with* is a representation of its
meaning [c52f288b7].

## Method — cosine similarity and why length-normalization matters

This is the named ungrounded item, so the definition is given in the chapter's own
terms. The chapter starts from the **dot product** as a similarity measure between
two vectors: orthogonal vectors (no shared dimensions) have a dot product of 0,
"representing their strong dissimilarity" [c52f288b7].

The chapter then states the problem with the *raw* dot product directly: "it favors
long vectors." It explains why — the dot product is higher if a vector is longer,
with higher values in each dimension, and **more frequent words have longer
vectors** because they co-occur with more words and accumulate higher co-occurrence
values. So the raw dot product is inflated for frequent words, which is not what a
similarity metric should reward [c52f288b7]. The chapter defines **vector length**
as the square root of the sum of the squares of the vector's components (the
Euclidean norm, eq. 5.8) [c52f288b7].

The fix is to **normalize the dot product by the lengths of the two vectors** —
divide the dot product by the product of the two vectors' lengths — to get "a
metric that tells us how similar two words are regardless of their frequency"
[c52f288b7]. The chapter notes this normalized dot product is identical to the
**cosine of the angle between the two vectors**, following from the geometric
definition of the dot product, `a·b = |a||b|cos θ`, so dividing through by `|a||b|`
leaves `cos θ` (eq. 5.9) [c52f288b7]. The **cosine similarity** metric between two
vectors *v* and *w* is therefore their dot product divided by the product of their
lengths [c52f288b7]. The load-bearing "why normalize" answer: cosine strips out the
frequency/magnitude effect so that similarity reflects *direction* (the pattern of
co-occurrence) rather than how often the words happen to appear [c52f288b7].

## Evidence — count-based vectors: word-context and term-document matrices

The chapter introduces the simplest embedding model as one built on a
**co-occurrence matrix**. It defines the **word-context matrix** (also termed the
word-word matrix): each row represents a word in the vocabulary and each column
records how often each other vocabulary word appears nearby, giving a `|V|×|V|`
matrix whose cells count how often the row (target) word and the column (context)
word co-occur nearby in a training corpus [c52f288b7].

It also describes the **term-document matrix** view, where documents are vectors
whose dimensionality equals `|V|` (the vocabulary size); the ordering of the numbers
indexes the dimensions along which documents vary, and two documents are similar to
the extent their vectors point the same way [c52f288b7]. The chapter is explicit
that these count vectors are computed over an entire corpus, not a single window,
and that the resulting vectors are **very long and sparse** — "mostly zeros, since
most words simply never occur in the context of others" [c52f288b7]. Sparsity is
the motivating defect that dense embeddings address.

## Method / bridge — dense embeddings and word2vec / skip-gram

The chapter motivates **dense vectors** by a concrete weakness of sparse count
vectors: in a sparse representation, dimensions for synonyms like *car* and
*automobile* are "distinct and unrelated," so sparse vectors may fail to capture the
similarity between a word neighbored by *car* and one neighbored by *automobile*
[c52f288b7]. Dense (short) vectors fold related dimensions together and "have even
more useful semantic properties" [c52f288b7].

The chapter then introduces **word2vec**, presenting **skip-gram with negative
sampling (SGNS)** as the specific algorithm [c52f288b7]. The key intuitions it
states:

- **Self-supervised classification, not counting.** Instead of counting how often
  each context word *c* occurs near a target word (e.g. *apricot*), word2vec trains
  a binary classifier on the task "Is word *c* likely to show up near *apricot*?"
  The classifier's prediction is not the goal — its **learned weights become the
  word embeddings** [c52f288b7].
- **Negative sampling.** Training needs negative examples. For each positive
  `(w, c_pos)` instance (a real target/context pair), SGNS creates *k* negative
  samples, each pairing the target *w* with a **noise word** `c_neg` — a random word
  from the lexicon constrained not to be *w*. Noise words are drawn according to a
  **weighted unigram probability** `p_α(w)`, with `α = 0.75` commonly used so that
  the weighting damps the dominance of very frequent words [c52f288b7].
- **Training objective.** The model uses stochastic gradient descent to learn
  embeddings that have a **high dot product with the embeddings of words that occur
  nearby** and a **low dot product with noise words** [c52f288b7].
- **Static embeddings.** word2vec produces *static* embeddings — one fixed vector
  per vocabulary word — in contrast to the dynamic *contextual* embeddings (e.g. the
  BERT family) the book defers to a later chapter, where a word's vector differs by
  context [c52f288b7].

The bridge back to cosine is explicit in the chapter's summary: **whether vectors
are sparse or dense, word and document similarity is computed by some function of
the dot product, and the cosine — a normalized dot product — is the most popular
such metric** [c52f288b7]. This is the same primitive `d2fbbb962` grounds for
ranked retrieval, now extended to the embedding setting.

## Scope — what this chapter does *not* define

For faithfulness: this 2026 "Embeddings" chapter **does not define tf-idf** — it
names the tf-idf model as a "more sophisticated variant" and explicitly says it will
introduce it in **Chapter 11** [c52f288b7]. It **does not define PMI or PPMI as a
weighting** either; PPMI appears only once, in the historical/bridging remark that
dense word2vec embeddings can be seen as an implicit factorization of a count matrix
with a particular **(PPMI) weighting** (Levy and Goldberg, 2014) [c52f288b7]. So
within this corpus, tf-idf-in-IR is grounded by the IR-book in `d2fbbb962`, and a
defining treatment of PPMI weighting is *still* not present in any ingested
chapter — it remains a genuine open gap (see below).

## Provenance note

Every definition above traces to the single primary source: SLP3 Ch.5 "Embeddings"
(draft of January 6, 2026) [c52f288b7]. Equation references (5.8 vector length, 5.9
cosine from the geometric dot-product identity) are the chapter's own numbering. The
source PDF was converted to markdown, which garbled some inline math tables; where a
formula was not legibly recoverable it is described in words faithfully rather than
reproduced as broken notation, and only legible relations (e.g. `a·b = |a||b|cos θ`)
are quoted.

## Gaps found

- PPMI weighting has no *defining* formula anywhere in the ingested corpus — Ch.5
  mentions it only as the implicit weighting behind word2vec, and the IR-book
  grounds tf/idf rather than PMI. A source defining PPMI is still missing.
- tf-idf in the NLP/embeddings sense is deferred by this chapter to its Ch.11, which
  is not ingested; the IR-book grounds tf-idf for retrieval but not the SLP3
  embeddings framing.
- The chapter's full SGNS objective (the sigmoid/logistic loss and the embedding
  update equations) is present in the source but garbled in conversion; a clean
  rendering of the loss is not yet grounded.
- Whether cosine remains the right similarity metric for *contextual* embeddings
  (BERT-family) versus static word2vec vectors is raised but deferred to a later
  chapter.
