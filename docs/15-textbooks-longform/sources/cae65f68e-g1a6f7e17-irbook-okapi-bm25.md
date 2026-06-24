[![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](bayesian-network-approaches-to-ir-1.html)
[![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](an-appraisal-and-some-extensions-1.html)
[![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](tree-structured-dependencies-between-terms-1.html)
[![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](contents-1.html)
[![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](index-1.html)

 **Next:** [Bayesian network approaches to](bayesian-network-approaches-to-ir-1.html)
 **Up:** [An appraisal and some](an-appraisal-and-some-extensions-1.html)
 **Previous:** [Tree-structured dependencies between terms](tree-structured-dependencies-between-terms-1.html)
   **[Contents](contents-1.html)**
   **[Index](index-1.html)**

## Okapi BM25: a non-binary model

The BIM was originally designed for short catalog records and abstracts of fairly consistent length, and it works reasonably in these contexts, but for modern full-text search collections, it seems clear that a model should pay attention to term frequency and document length, as in Chapter [6](scoring-term-weighting-and-the-vector-space-model-1.html#ch:tfidf) . The  *BM25 weighting scheme* , often called  *Okapi weighting* , after the system in which it was first implemented, was developed as a way of building a probabilistic model sensitive to these quantities while not introducing too many additional parameters into the model ([Spärck Jones et al., 2000](bibliography-1.html#sparckjones00probabilistic)). We will not develop the full theory behind the model here, but just present a series of forms that build up to the standard form now used for document scoring. The simplest score for document ![$d$](img354.png) is just idf weighting of the query terms present, as in Equation [76](probability-estimates-in-practice-1.html#prob-idf):

|  |  |
| --- | --- |
| ![\begin{displaymath} RSV_d = \sum_{t \in q} \log\frac{N}{\docf_t} \end{displaymath}](img768.png) | (84) |

Sometimes, an alternative version of  *idf* is used. If we start with the formula in Equation [75](probability-estimates-in-theory-1.html#smoothed-rf) but in the absence of relevance feedback information we estimate that ![$S = s = 0$](img769.png), then we get an alternative idf formulation as follows:

|  |  |
| --- | --- |
| ![\begin{displaymath} RSV_d = \sum_{t \in q} \log \frac{N - \docf_t + \frac{1}{2}}{\docf_t + \frac{1}{2}} \end{displaymath}](img770.png) | (85) |

This variant behaves slightly strangely: if a term occurs in over half the documents in the collection then this model gives a negative term weight, which is presumably undesirable. But, assuming the use of a stop list, this normally doesn't happen, and the value for each summand can be given a floor of 0.

We can improve on Equation [84](#bm25-1) by factoring in the frequency of each term and document length:

|  |  |
| --- | --- |
| ![\begin{displaymath} RSV_d = \sum_{t \in q} \log\left[\frac{N}{\docf_t}\right]\cd... ...mf_{td}} {k_1 ((1-b) + b\times (L_d/ L_{ave})) + \termf_{td}} \end{displaymath}](img771.png) | (86) |

Here, ![$\termf_{td}$](img772.png) is the frequency of term ![$t$](img67.png) in document ![$d$](img354.png), and ![$L_d$](img773.png) and ![$ L_{ave}$](img185.png) are the length of document ![$d$](img354.png) and the average document length for the whole collection.
The variable ![$k_1$](img774.png) is a positive tuning parameter that calibrates the document term frequency scaling. A ![$k_1$](img774.png) value of 0 corresponds to a binary model (no term frequency), and a large value corresponds to using raw term frequency. ![$b$](img137.png) is another tuning parameter (![$0 \le b \le 1$](img775.png)) which determines the scaling by document length: ![$b = 1$](img776.png) corresponds to fully scaling the term weight by the document length, while ![$b = 0$](img777.png) corresponds to no length normalization.

If the query is long, then we might also use similar weighting for query terms. This is appropriate if the queries are paragraph long information needs, but unnecessary for short queries.

|  |  |
| --- | --- |
| ![\begin{displaymath} RSV_d = \sum_{t\in q} \left[\log\frac{N}{\docf_t}\right] \cd... ...mf_{td}} \cdot \frac{(k_3 + 1)\termf_{tq}}{k_3 + \termf_{tq}} \end{displaymath}](img778.png) | (87) |

with ![$\termf_{tq}$](img779.png) being the frequency of term ![$t$](img67.png) in the query ![$q$](img161.png), and ![$k_3$](img780.png) being another positive tuning parameter that this time calibrates term frequency scaling of the query. In the equation presented, there is no length normalization of queries (it is as if ![$b = 0$](img777.png) here). Length normalization of the query is unnecessary because retrieval is being done with respect to a single fixed query. The tuning parameters of these formulas should ideally be set to optimize performance on a development test collection (see page [8.1](information-retrieval-system-evaluation-1.html#p:dev-test) ). That is, we can search for values of these parameters that maximize performance on a separate development test collection (either manually or with optimization methods such as grid search or something more advanced), and then use these parameters on the actual test collection. In the absence of such optimization, experiments have shown reasonable values are to set ![$k_1$](img774.png) and ![$k_3$](img780.png) to a value between 1.2 and 2 and ![$b = 0.75$](img781.png).

If we have relevance judgments available, then we can use the full form of smoothed-rf in place of the approximation
![$\log(N/\docf_t)$](img782.png) introduced in prob-idf:

|  |  |  |  |
| --- | --- | --- | --- |
| ![$\displaystyle RSV_d$](img783.png) | ![$\textstyle =$](img313.png) | ![$\displaystyle \sum_{t\in q} \log \left[\left[\frac{(\vert VR_t\vert + \frac{1}{... .../(N - \docf_t - \vert VR\vert + \vert VR_t\vert + \frac{1}{2})} \right]\right.$](img784.png) | (88) |
|  |  | ![$\displaystyle \left.\kern1.5em \times \frac{(k_1+1)\termf_{td}}{k_1((1-b) + b (... ...ve}))+\termf_{td}} \times \frac{(k_3 + 1)\termf_{tq}}{k_3 + \termf_{tq}}\right]$](img785.png) | (89) |

Here, ![$VR_t$](img748.png), ![$NVR_t$](img786.png), and ![$VR$](img600.png) are used as in Section [11.3.4](probabilistic-approaches-to-relevance-feedback-1.html#sec:probrf) . The first part of the expression reflects relevance feedback (or just idf weighting if no relevance information is available), the second implements document term frequency and document length scaling, and the third considers term frequency in the query.

Rather than just providing a term weighting method for terms in a user's query, relevance feedback can also involve augmenting the query (automatically or with manual review) with some (say, 10-20) of the top terms in the known-relevant documents as ordered by the relevance factor ![$\hat{c}_t$](img787.png) from Equation [75](probability-estimates-in-theory-1.html#smoothed-rf), and the above formula can then be used with such an augmented query vector ![$\vec{q}$](img572.png).

The BM25 term weighting formulas have been used quite widely and quite successfully across a range of collections and search tasks. Especially in the TREC evaluations, they performed well and were widely adopted by many groups. See [Spärck Jones et al. (2000)](bibliography-1.html#sparckjones00probabilistic) for extensive motivation and discussion of experimental results.

---

[![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](bayesian-network-approaches-to-ir-1.html)
[![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](an-appraisal-and-some-extensions-1.html)
[![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](tree-structured-dependencies-between-terms-1.html)
[![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](contents-1.html)
[![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](index-1.html)

 **Next:** [Bayesian network approaches to](bayesian-network-approaches-to-ir-1.html)
 **Up:** [An appraisal and some](an-appraisal-and-some-extensions-1.html)
 **Previous:** [Tree-structured dependencies between terms](tree-structured-dependencies-between-terms-1.html)
   **[Contents](contents-1.html)**
   **[Index](index-1.html)**

© 2008 Cambridge University Press
This is an automatically generated page. In case of formatting errors you may want to look at the [PDF edition](http://informationretrieval.org) of the book.
2009-04-07