[ ![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](https://nlp.stanford.edu/IR-book/html/htmledition/assessing-relevance-1.html) [ ![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html) [ ![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-unranked-retrieval-sets-1.html) [ ![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html) [ ![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)   
**Next:** [Assessing relevance](https://nlp.stanford.edu/IR-book/html/htmledition/assessing-relevance-1.html) **Up:** [Evaluation in information retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html) **Previous:** [Evaluation of unranked retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-unranked-retrieval-sets-1.html) **[Contents](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html)** **[Index](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)**   
  

#    
Evaluation of ranked retrieval results   
**Figure 8.2:** Precision/recall graph.  
| ![\\includegraphics\[totalheight=3in\]{PrecisionRecall.eps}](https://nlp.stanford.edu/IR-book/html/htmledition/img532.png) |  
| --- |  
Precision, recall, and the F measure are set-based measures. They are computed using unordered sets of documents. We need to extend these measures (or to define new measures) if we are to evaluate the ranked retrieval results that are now standard with search engines. In a ranked retrieval context, appropriate sets of retrieved documents are naturally given by the top ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png) retrieved documents. For each such set, precision and recall values can be plotted to give a  _precision-recall curve_ , such as the one shown in Figure [8.2](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:precision-recall) . Precision-recall curves have a distinctive saw-tooth shape: if the ![$\(k+1\)^{th}$](https://nlp.stanford.edu/IR-book/html/htmledition/img533.png) document retrieved is nonrelevant then recall is the same as for the top ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png) documents, but precision has dropped. If it is relevant, then both precision and recall increase, and the curve jags up and to the right. It is often useful to remove these jiggles and the standard way to do this is with an interpolated precision: the  _interpolated precision_ ![$p_{interp}$](https://nlp.stanford.edu/IR-book/html/htmledition/img534.png) at a certain recall level ![$r$](https://nlp.stanford.edu/IR-book/html/htmledition/img28.png) is defined as the highest precision found for any recall level ![$r' \\ge r$](https://nlp.stanford.edu/IR-book/html/htmledition/img535.png):   
  
| ![\\begin{displaymath}
p_{interp}\(r\) = \\max_{r' \\ge r} p\(r'\)
\\end{displaymath}](https://nlp.stanford.edu/IR-book/html/htmledition/img536.png)  |  (42)  |  
| --- | --- |  
  

The justification is that almost anyone would be prepared to look at a few more documents if it would increase the percentage of the viewed set that were relevant (that is, if the precision of the larger set is higher). Interpolated precision is shown by a thinner line in Figure [8.2](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:precision-recall) . With this definition, the interpolated precision at a recall of 0 is well-defined (Exercise [8.4](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#ex:interp-prec) ). 
  
  
| Recall  | Interp.  |  
| --- | --- |  
|   | Precision  |  
| 0.0  | 1.00  |  
| 0.1  | 0.67  |  
| 0.2  | 0.63  |  
| 0.3  | 0.55  |  
| 0.4  | 0.45  |  
| 0.5  | 0.41  |  
| 0.6  | 0.36  |  
| 0.7  | 0.29  |  
| 0.8  | 0.13  |  
| 0.9  | 0.10  |  
| 1.0  | 0.08  |  
Calculation of 11-point Interpolated Average Precision.This is for the precision-recall curve shown in Figure [8.2](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:precision-recall) .
  

Examining the entire precision-recall curve is very informative, but there is often a desire to boil this information down to a few numbers, or perhaps even a single number. The traditional way of doing this (used for instance in the first 8 TREC Ad Hoc evaluations) is the  _11-point interpolated average precision_ . For each information need, the interpolated precision is measured at the 11 recall levels of 0.0, 0.1, 0.2, ..., 1.0. For the precision-recall curve in Figure [8.2](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:precision-recall) , these 11 values are shown in Table [8.1](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#tab:11-point) . For each recall level, we then calculate the arithmetic mean of the interpolated precision at that recall level for each information need in the test collection. A composite precision-recall curve showing 11 points can then be graphed. Figure [8.3](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:trec-11-point) shows an example graph of such results from a representative good system at TREC 8. 
![\\includegraphics{PrecisionRecall11point.eps}](https://nlp.stanford.edu/IR-book/html/htmledition/img537.png) Averaged 11-point precision/recall graph across 50 queries for a representative TREC system.The Mean Average Precision for this system is 0.2553. 
In recent years, other measures have become more common. Most standard among the TREC community is  _Mean Average Precision_ (MAP), which provides a single-figure measure of quality across recall levels. Among evaluation measures, MAP has been shown to have especially good discrimination and stability. For a single information need, Average Precision is the average of the precision value obtained for the set of top ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png) documents existing after each relevant document is retrieved, and this value is then averaged over information needs. That is, if the set of relevant documents for an information need ![$q_j \\in Q$](https://nlp.stanford.edu/IR-book/html/htmledition/img538.png) is  ![$\\{d_1,
\\ldots d_{m_j}\\}$](https://nlp.stanford.edu/IR-book/html/htmledition/img539.png) and ![$R_{jk}$](https://nlp.stanford.edu/IR-book/html/htmledition/img540.png) is the set of ranked retrieval results from the top result until you get to document ![$d_k$](https://nlp.stanford.edu/IR-book/html/htmledition/img541.png), then   
  
| ![\\begin{displaymath}
\\mbox{MAP}\(Q\) = \\frac{1}{\\vert Q\\vert} \\sum_{j=1}^{\\vert Q\\vert} \\frac{1}{m_j}
\\sum_{k=1}^{m_j} \\mbox{Precision}\(R_{jk}\)
\\end{displaymath}](https://nlp.stanford.edu/IR-book/html/htmledition/img542.png)  |  (43)  |  
| --- | --- |  
  

When a relevant document is not retrieved at all,[![\[*\]](http://nlp.stanford.edu/IR-book/html/icons/footnote.png)](https://nlp.stanford.edu/IR-book/html/htmledition/footnode.html#foot10755)the precision value in the above equation is taken to be 0. For a single information need, the average precision approximates the area under the uninterpolated precision-recall curve, and so the MAP is roughly the average area under the precision-recall curve for a set of queries. 
Using MAP, fixed recall levels are not chosen, and there is no interpolation. The MAP value for a test collection is the arithmetic mean of average precision values for individual information needs. (This has the effect of weighting each information need equally in the final reported number, even if many documents are relevant to some queries whereas very few are relevant to other queries.) Calculated MAP scores normally vary widely across information needs when measured within a single system, for instance, between 0.1 and 0.7. Indeed, there is normally more agreement in MAP for an individual information need across systems than for MAP scores for different information needs for the same system. This means that a set of test information needs must be large and diverse enough to be representative of system effectiveness across different queries. 
The above measures factor in precision at all recall levels. For many prominent applications, particularly web search, this may not be germane to users. What matters is rather how many good results there are on the first page or the first three pages. This leads to measuring precision at fixed low levels of retrieved results, such as 10 or 30 documents. This is referred to as ``Precision at ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png)'', for example ``Precision at 10''. It has the advantage of not requiring any estimate of the size of the set of relevant documents but the disadvantages that it is the least stable of the commonly used evaluation measures and that it does not average well, since the total number of relevant documents for a query has a strong influence on precision at ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png). 
An alternative, which alleviates this problem, is  _R-precision_ . It requires having a set of known relevant documents ![$Rel$](https://nlp.stanford.edu/IR-book/html/htmledition/img543.png), from which we calculate the precision of the top ![$Rel$](https://nlp.stanford.edu/IR-book/html/htmledition/img543.png) documents returned. (The set ![$Rel$](https://nlp.stanford.edu/IR-book/html/htmledition/img543.png) may be incomplete, such as when ![$Rel$](https://nlp.stanford.edu/IR-book/html/htmledition/img543.png) is formed by creating relevance judgments for the pooled top ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png) results of particular systems in a set of experiments.) R-precision adjusts for the size of the set of relevant documents: A perfect system could score 1 on this metric for each query, whereas, even a perfect system could only achieve a precision at 20 of 0.4 if there were only 8 documents in the collection relevant to an information need. Averaging this measure across queries thus makes more sense. This measure is harder to explain to naive users than Precision at ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png) but easier to explain than MAP. If there are ![$\\vert Rel\\vert$](https://nlp.stanford.edu/IR-book/html/htmledition/img544.png) relevant documents for a query, we examine the top ![$\\vert Rel\\vert$](https://nlp.stanford.edu/IR-book/html/htmledition/img544.png) results of a system, and find that ![$r$](https://nlp.stanford.edu/IR-book/html/htmledition/img28.png) are relevant, then by definition, not only is the precision (and hence R-precision) ![$r/\\vert Rel\\vert$](https://nlp.stanford.edu/IR-book/html/htmledition/img545.png), but the recall of this result set is also ![$r/\\vert Rel\\vert$](https://nlp.stanford.edu/IR-book/html/htmledition/img545.png). Thus, R-precision turns out to be identical to the  _break-even point_ , another measure which is sometimes used, defined in terms of this equality relationship holding. Like Precision at ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png), R-precision describes only one point on the precision-recall curve, rather than attempting to summarize effectiveness across the curve, and it is somewhat unclear why you should be interested in the break-even point rather than either the best point on the curve (the point with maximal F-measure) or a retrieval level of interest to a particular application (Precision at ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png)). Nevertheless, R-precision turns out to be highly correlated with MAP empirically, despite measuring only a single point on the curve.   
**Figure 8.4:** The ROC curve corresponding to the precision-recall curve in Figure [8.2](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:precision-recall) .  
|  ![\\includegraphics{ROC-curve.eps}](https://nlp.stanford.edu/IR-book/html/htmledition/img546.png) . |  
| --- |  
Another concept sometimes used in evaluation is an  _ROC curve_ . (``ROC'' stands for ``Receiver Operating Characteristics'', but knowing that doesn't help most people.) An ROC curve plots the true positive rate or sensitivity against the false positive rate or ( ![$1 - \\mbox{specificity}$](https://nlp.stanford.edu/IR-book/html/htmledition/img547.png)). Here,  _sensitivity_ is just another term for recall. The false positive rate is given by ![$fp/\(fp+tn\)$](https://nlp.stanford.edu/IR-book/html/htmledition/img548.png). Figure [8.4](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:ROC-curve) shows the ROC curve corresponding to the precision-recall curve in Figure [8.2](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:precision-recall) . An ROC curve always goes from the bottom left to the top right of the graph. For a good system, the graph climbs steeply on the left side. For unranked result sets,  _specificity_ , given by ![$tn/\(fp + tn\)$](https://nlp.stanford.edu/IR-book/html/htmledition/img549.png), was not seen as a very useful notion. Because the set of true negatives is always so large, its value would be almost 1 for all information needs (and, correspondingly, the value of the false positive rate would be almost 0). That is, the ``interesting'' part of Figure [8.2](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:precision-recall) is  ![$0 < \\mbox{recall} < 0.4$](https://nlp.stanford.edu/IR-book/html/htmledition/img550.png), a part which is compressed to a small corner of Figure [8.4](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html#fig:ROC-curve) . But an ROC curve could make sense when looking over the full retrieval spectrum, and it provides another way of looking at the data. In many fields, a common aggregate measure is to report the area under the ROC curve, which is the ROC analog of MAP. Precision-recall curves are sometimes loosely referred to as ROC curves. This is understandable, but not accurate. 
A final approach that has seen increasing adoption, especially when employed with machine learning approaches to ranking svm-ranking is measures of  _cumulative gain_ , and in particular  _normalized discounted cumulative gain_ ( _NDCG_ ). NDCG is designed for situations of non-binary notions of relevance (cf. Section [8.5.1](https://nlp.stanford.edu/IR-book/html/htmledition/critiques-and-justifications-of-the-concept-of-relevance-1.html#sec:relevance) ). Like precision at ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png), it is evaluated over some number ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png) of top search results. For a set of queries ![$Q$](https://nlp.stanford.edu/IR-book/html/htmledition/img146.png), let ![$R\(j,d\)$](https://nlp.stanford.edu/IR-book/html/htmledition/img551.png) be the relevance score assessors gave to document ![$d$](https://nlp.stanford.edu/IR-book/html/htmledition/img354.png) for query ![$j$](https://nlp.stanford.edu/IR-book/html/htmledition/img9.png). Then,   
  
| ![\\begin{displaymath}
\\mbox{NDCG}\(Q, k\) = \\frac{1}{\\vert Q\\vert} \\sum_{j=1}^{\\vert Q\\vert} Z_{kj} \\sum_{m=1}^{k}
\\frac{2^{R\(j,m\)}-1}{\\log_2\(1+m\)},
\\end{displaymath}](https://nlp.stanford.edu/IR-book/html/htmledition/img552.png)  |  (44)  |  
| --- | --- |  
  

where ![$Z_{kj}$](https://nlp.stanford.edu/IR-book/html/htmledition/img553.png) is a normalization factor calculated to make it so that a perfect ranking's NDCG at ![$k$](https://nlp.stanford.edu/IR-book/html/htmledition/img20.png) for query ![$j$](https://nlp.stanford.edu/IR-book/html/htmledition/img9.png) is 1. For queries for which ![$k' < k$](https://nlp.stanford.edu/IR-book/html/htmledition/img554.png) documents are retrieved, the last summation is done up to ![$k'$](https://nlp.stanford.edu/IR-book/html/htmledition/img555.png). 
**Exercises.**
  * What are the possible values for interpolated precision at a recall level of 0? 
  * Must there always be a break-even point between precision and recall? Either show there must be or give a counter-example. 
  * What is the relationship between the value of ![$F_1$](https://nlp.stanford.edu/IR-book/html/htmledition/img522.png) and the break-even point? 
  * The  _Dice coefficient_ of two sets is a measure of their intersection scaled by their size (giving a value in the range 0 to 1):   
  
| ![\\begin{displaymath}
\\mbox{Dice}\(X,Y\) = \\frac{2\\vert X\\cap Y\\vert}{\\vert X\\vert + \\vert Y\\vert}
\\end{displaymath}](https://nlp.stanford.edu/IR-book/html/htmledition/img556.png)  |  (45)  |  
| --- | --- |  
  

Show that the balanced F-measure (![$F_1$](https://nlp.stanford.edu/IR-book/html/htmledition/img522.png)) is equal to the Dice coefficient of the retrieved and relevant document sets. 
  * Consider an information need for which there are 4 relevant documents in the collection. Contrast two systems run on this collection. Their top 10 results are judged for relevance as follows (the leftmost item is the top ranked search result): 
> | System 1  |   | R  | N  | R  | N  | N  |   | N  | N  | N  | R  | R  |  
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
> | System 2  |   | N  | R  | N  | N  | R  |   | R  | R  | N  | N  | N  |  
    1. What is the MAP of each system? Which has a higher MAP? 
    2. Does this result intuitively make sense? What does it say about what is important in getting a good MAP score? 
    3. What is the R-precision of each system? (Does it rank the systems the same as MAP?) 
  * The following list of Rs and Ns represents relevant (R) and nonrelevant (N) returned documents in a ranked list of 20 documents retrieved in response to a query from a collection of 10,000 documents. The top of the ranked list (the document the system thinks is most likely to be relevant) is on the left of the list. This list shows 6 relevant documents. Assume that there are 8 relevant documents in total in the collection. 
> | R  | R  | N  | N  | N  |   | N  | N  | N  | R  | N  |   | R  | N  | N  | N  | R  |   | N  | N  | N  | N  | R  |  
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
    1. What is the precision of the system on the top 20? 
    2. What is the F![$_1$](https://nlp.stanford.edu/IR-book/html/htmledition/img26.png) on the top 20? 
    3. What is the uninterpolated precision of the system at 25% recall? 
    4. What is the interpolated precision at 33% recall? 
    5. Assume that these 20 documents are the complete result set of the system. What is the MAP for the query? 
Assume, now, instead, that the system returned the entire 10,000 documents in a ranked list, and these are the first 20 results returned.  

f.
    What is the largest possible MAP that this system could have?  

g.
    What is the smallest possible MAP that this system could have?  

h.
    In a set of experiments, only the top 20 results are evaluated by hand. The result in (e) is used to approximate the range (f)-(g). For this example, how large (in absolute terms) can the error for the MAP be by calculating (e) instead of (f) and (g) for this query? 


* * *
[ ![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](https://nlp.stanford.edu/IR-book/html/htmledition/assessing-relevance-1.html) [ ![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html) [ ![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-unranked-retrieval-sets-1.html) [ ![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html) [ ![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)   
**Next:** [Assessing relevance](https://nlp.stanford.edu/IR-book/html/htmledition/assessing-relevance-1.html) **Up:** [Evaluation in information retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html) **Previous:** [Evaluation of unranked retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-unranked-retrieval-sets-1.html) **[Contents](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html)** **[Index](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)** © 2008 Cambridge University Press  
This is an automatically generated page. In case of formatting errors you may want to look at the [PDF edition](http://informationretrieval.org) of the book.  
2009-04-07 

