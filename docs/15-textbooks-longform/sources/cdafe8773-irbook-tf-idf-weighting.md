[ ![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](https://nlp.stanford.edu/IR-book/html/htmledition/the-vector-space-model-for-scoring-1.html) [ ![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) [ ![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html) [ ![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html) [ ![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)   
**Next:** [The vector space model](https://nlp.stanford.edu/IR-book/html/htmledition/the-vector-space-model-for-scoring-1.html) **Up:** [Term frequency and weighting](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) **Previous:** [Inverse document frequency](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html) **[Contents](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html)** **[Index](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)**   
  

##  Tf-idf weighting
We now combine the definitions of term frequency and inverse document frequency, to produce a composite weight for each term in each document. The  _tf-idf_ weighting scheme assigns to term ![$t$](https://nlp.stanford.edu/IR-book/html/htmledition/img67.png) a weight in document ![$d$](https://nlp.stanford.edu/IR-book/html/htmledition/img354.png) given by 
  
  
|  ![\\begin{displaymath}
\\mbox{tf-idf}_{t,d} = \\mbox{tf}_{t,d} \\times \\mbox{idf}_t.
\\end{displaymath}](https://nlp.stanford.edu/IR-book/html/htmledition/img406.png)  |  (22)  |  
| --- | --- |  
  

In other words,  ![$\\mbox{tf-idf}_{t,d}$](https://nlp.stanford.edu/IR-book/html/htmledition/img407.png) assigns to term ![$t$](https://nlp.stanford.edu/IR-book/html/htmledition/img67.png) a weight in document ![$d$](https://nlp.stanford.edu/IR-book/html/htmledition/img354.png) that is 
  1. highest when ![$t$](https://nlp.stanford.edu/IR-book/html/htmledition/img67.png) occurs many times within a small number of documents (thus lending high discriminating power to those documents); 
  2. lower when the term occurs fewer times in a document, or occurs in many documents (thus offering a less pronounced relevance signal); 
  3. lowest when the term occurs in virtually all documents. 


At this point, we may view each document as a  _vector_ with one component corresponding to each term in the dictionary, together with a weight for each component that is given by ([22](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html#eqn:tfidf)). For dictionary terms that do not occur in a document, this weight is zero. This vector form will prove to be crucial to scoring and ranking; we will develop these ideas in Section [6.3](https://nlp.stanford.edu/IR-book/html/htmledition/the-vector-space-model-for-scoring-1.html#sec:docvectors) . As a first step, we introduce the _overlap score measure_ : the score of a document ![$d$](https://nlp.stanford.edu/IR-book/html/htmledition/img354.png) is the sum, over all query terms, of the number of times each of the query terms occurs in ![$d$](https://nlp.stanford.edu/IR-book/html/htmledition/img354.png). We can refine this idea so that we add up not the number of occurrences of each query term ![$t$](https://nlp.stanford.edu/IR-book/html/htmledition/img67.png) in ![$d$](https://nlp.stanford.edu/IR-book/html/htmledition/img354.png), but instead the tf-idf weight of each term in ![$d$](https://nlp.stanford.edu/IR-book/html/htmledition/img354.png).   
  
|  ![\\begin{displaymath}
\\mbox{Score}\(q,d\)=\\sum_{t\\in q} \\mbox{tf-idf}_{t,d}.
\\end{displaymath}](https://nlp.stanford.edu/IR-book/html/htmledition/img408.png)  |  (23)  |  
| --- | --- |  
  

In Section [6.3](https://nlp.stanford.edu/IR-book/html/htmledition/the-vector-space-model-for-scoring-1.html#sec:docvectors) we will develop a more rigorous form of Equation [23](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html#eqn:docscore). 
**Exercises.**
  * Why is the idf of a term always finite? 
  * What is the idf of a term that occurs in every document? Compare this with the use of stop word lists. 
  * Consider the table of term frequencies for 3 documents denoted Doc1, Doc2, Doc3 in Figure [6.9](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html#fig:tfgraph) .   
**Figure 6.9:** Table of tf values for Exercise [6.2.2](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html#ex:tfidf).  
| ![\\begin{figure}\\begin{tabular}{\\vert\\vert l\\vert r\\vert r\\vert r\\vert\\vert}
\\hlin...
...rance & 0 & 33 & 29 \\\\
best & 14 & 0 & 17 \\\\
\\hline
\\end{tabular}
\\end{figure}](https://nlp.stanford.edu/IR-book/html/htmledition/img409.png) |  
| --- |  
Compute the tf-idf weights for the terms car, auto, insurance, best, for each document, using the idf values from Figure [6.8](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html#fig:figureidf) . 
  * Can the tf-idf weight of a term in a document exceed 1? 
  * How does the base of the logarithm in ([21](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html#eqn:idf)) affect the score calculation in ([23](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html#eqn:docscore))? How does the base of the logarithm affect the relative scores of two documents on a given query? 
  * If the logarithm in ([21](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html#eqn:idf)) is computed base 2, suggest a simple approximation to the idf of a term. 


* * *
[ ![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](https://nlp.stanford.edu/IR-book/html/htmledition/the-vector-space-model-for-scoring-1.html) [ ![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) [ ![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html) [ ![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html) [ ![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)   
**Next:** [The vector space model](https://nlp.stanford.edu/IR-book/html/htmledition/the-vector-space-model-for-scoring-1.html) **Up:** [Term frequency and weighting](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) **Previous:** [Inverse document frequency](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html) **[Contents](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html)** **[Index](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)** © 2008 Cambridge University Press  
This is an automatically generated page. In case of formatting errors you may want to look at the [PDF edition](http://informationretrieval.org) of the book.  
2009-04-07 

