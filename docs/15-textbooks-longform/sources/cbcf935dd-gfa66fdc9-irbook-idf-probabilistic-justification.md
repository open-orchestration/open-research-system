[![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](probability-estimates-in-practice-1.html)
[![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](the-binary-independence-model-1.html)
[![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](deriving-a-ranking-function-for-query-terms-1.html)
[![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](contents-1.html)
[![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](index-1.html)

 **Next:** [Probability estimates in practice](probability-estimates-in-practice-1.html)
 **Up:** [The Binary Independence Model](the-binary-independence-model-1.html)
 **Previous:** [Deriving a ranking function](deriving-a-ranking-function-for-query-terms-1.html)
   **[Contents](contents-1.html)**
   **[Index](index-1.html)**

## Probability estimates in theory

For each term ![$t$](img67.png), what would these ![$c_t$](img721.png) numbers look like for the whole collection? odds-ratio-ct-contingency gives a contingency table of counts of documents in the collection, where ![$\docf_t$](img726.png) is the number of documents that contain term ![$t$](img67.png):

![\begin{example} \begin{tabular}[t]{\vert cc\vert cc\vert c\vert} \hline & docum... ...\\ \hline & Total & $S$\ & $N-S$\ & $N$\ \\ \hline \end{tabular} \end{example}](img727.png)

Using this, ![$p_t = s/S$](img728.png) and
![$u_t = (\docf_t-s)/(N-S)$](img729.png) and

|  |  |
| --- | --- |
| ![\begin{displaymath} c_t = K(N,\docf_t,S,s) = \log\frac{s/(S-s)}{(\docf_t-s)/((N-\docf_t)-(S-s))} \end{displaymath}](img730.png) | (74) |

To avoid the possibility of zeroes (such as if every or no relevant
document has a particular term) it is fairly standard to  *add ![$\frac{1}{2}$](img731.png)* to each of the quantities in the center 4 terms of odds-ratio-ct-contingency, and then to adjust the marginal counts (the totals) accordingly (so, the bottom right cell totals ![$N+2$](img732.png)). Then we have:

|  |  |
| --- | --- |
| ![\begin{displaymath} \hat{c}_t = K(N,\docf_t,S,s) = \log\frac{(s+\frac{1}{2})/(S-... ...1}{2})} {(\docf_t-s+\frac{1}{2})/(N-\docf_t-S+s+\frac{1}{2})} \end{displaymath}](img733.png) | (75) |

Adding ![$\frac{1}{2}$](img731.png) in this way is a simple form of
smoothing. For trials with categorical outcomes (such as
noting the presence or absence of a term),
one way to estimate the probability of
an event from data is simply to count the number of times an
event occurred divided by the total number of trials.
This is referred to as the  *relative frequency* of the event.
Estimating the
probability as the relative frequency is the  *maximum
likelihood estimate* (or
 *MLE* ),
because this value
makes the observed data maximally likely. However, if we
simply use the MLE, then the probability given to events we
happened to see is usually too high, whereas other
events may be completely unseen and giving them as a
probability estimate their relative frequency of 0 is both
an underestimate, and normally breaks our models, since
anything multiplied by 0 is 0. Simultaneously decreasing
the estimated
probability of seen events and increasing the probability of
unseen events is referred to as  *smoothing* . One
simple way of smoothing is to
 *add a number ![$\alpha$](img524.png)*
to each
of the observed counts. These  *pseudocounts*
correspond to the use of a uniform distribution over the vocabulary as a  *Bayesian
prior* , following
Equation [59](review-of-basic-probability-theory-1.html#eqn:bayesrule). We initially assume a uniform
distribution over events, where the size of ![$\alpha$](img524.png) denotes
the strength of our belief in uniformity, and we then update
the probability based on observed events. Since our belief
in uniformity is weak, we use
![$\alpha = \frac{1}{2}$](img734.png). This
is a form of  *maximum a posteriori* ( *MAP* )
estimation, where we choose the most likely point value for
probabilities based on the prior and the observed evidence,
following Equation [59](review-of-basic-probability-theory-1.html#eqn:bayesrule). We will further discuss
methods of smoothing estimated counts to give probability
models in Section [12.2.2](estimating-the-query-generation-probability-1.html#sec:prob-smoothing) (page [![[*]](http://nlp.stanford.edu/IR-book/html/icons/crossref.png)](estimating-the-query-generation-probability-1.html#p:prob-smoothing)); the simple method of
 *adding ![$\frac{1}{2}$](img731.png)*
to each observed count will do for now.

---

[![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](probability-estimates-in-practice-1.html)
[![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](the-binary-independence-model-1.html)
[![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](deriving-a-ranking-function-for-query-terms-1.html)
[![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](contents-1.html)
[![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](index-1.html)

 **Next:** [Probability estimates in practice](probability-estimates-in-practice-1.html)
 **Up:** [The Binary Independence Model](the-binary-independence-model-1.html)
 **Previous:** [Deriving a ranking function](deriving-a-ranking-function-for-query-terms-1.html)
   **[Contents](contents-1.html)**
   **[Index](index-1.html)**

© 2008 Cambridge University Press
This is an automatically generated page. In case of formatting errors you may want to look at the [PDF edition](http://informationretrieval.org) of the book.
2009-04-07