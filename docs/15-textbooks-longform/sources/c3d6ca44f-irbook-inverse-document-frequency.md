[ ![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html) [ ![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) [ ![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) [ ![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html) [ ![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)   
**Next:** [Tf-idf weighting](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html) **Up:** [Term frequency and weighting](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) **Previous:** [Term frequency and weighting](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) **[Contents](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html)** **[Index](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)**   
  

##    
Inverse document frequency 
Raw term frequency as above suffers from a critical problem: all terms are considered equally important when it comes to assessing relevancy on a query. In fact certain terms have little or no discriminating power in determining relevance. For instance, a collection of documents on the auto industry is likely to have the term auto in almost every document. To this end, we introduce a mechanism for attenuating the effect of terms that occur too often in the collection to be meaningful for relevance determination. An immediate idea is to scale down the term weights of terms with high _collection frequency,_ defined to be the total number of occurrences of a term in the collection. The idea would be to reduce the ![$\\mbox{tf}$](https://nlp.stanford.edu/IR-book/html/htmledition/img401.png) weight of a term by a factor that grows with its collection frequency. 
Instead, it is more commonplace to use for this purpose the  _document frequency_ ![$\\mbox{df}_t$](https://nlp.stanford.edu/IR-book/html/htmledition/img402.png), defined to be the number of documents in the collection that contain a term ![$t$](https://nlp.stanford.edu/IR-book/html/htmledition/img67.png). This is because in trying to discriminate between documents for the purpose of scoring it is better to use a document-level statistic (such as the number of documents containing a term) than to use a collection-wide statistic for the term.   
**Figure 6.7:** Collection frequency (cf) and document frequency (df) behave differently, as in this example from the Reuters collection.  
| ![\\begin{figure}\\begin{tabular}{\\vert l\\vert l\\vert l\\vert}
\\hline
% after \\\\ : ...
...10422 & 8760\\\\
insurance & 10440 & 3997 \\\\
\\hline
\\end{tabular}
\\end{figure}](https://nlp.stanford.edu/IR-book/html/htmledition/img403.png) |  
| --- |  
The reason to prefer df to cf is illustrated in Figure [6.7](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html#fig:cfdf) , where a simple example shows that collection frequency (cf) and document frequency (df) can behave rather differently. In particular, the cf values for both try and insurance are roughly equal, but their df values differ significantly. Intuitively, we want the few documents that contain insurance to get a higher boost for a query on insurance than the many documents containing try get from a query on try. 
How is the document frequency df of a term used to scale its weight? Denoting as usual the total number of documents in a collection by ![$N$](https://nlp.stanford.edu/IR-book/html/htmledition/img62.png), we define the  _inverse document frequency_ of a term ![$t$](https://nlp.stanford.edu/IR-book/html/htmledition/img67.png) as follows: 
  
  
|  ![\\begin{displaymath}
\\mbox{idf}_t = \\log {N\\over \\mbox{df}_t}.
\\end{displaymath}](https://nlp.stanford.edu/IR-book/html/htmledition/img404.png)  |  (21)  |  
| --- | --- |  
  

Thus the idf of a rare term is high, whereas the idf of a frequent term is likely to be low. Figure [6.8](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html#fig:figureidf) gives an example of idf's in the Reuters collection of 806,791 documents; in this example logarithms are to the base 10. In fact, as we will see in Exercise [6.2.2](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html#ex:logbase) , the precise base of the logarithm is not material to ranking. We will give on page [11.3.3](https://nlp.stanford.edu/IR-book/html/htmledition/probability-estimates-in-practice-1.html#p:justificationofidf) a justification of the particular form in Equation [21](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html#eqn:idf). 
![\\begin{figure}
% latex2html id marker 7963
\\par
\\begin{tabular}{\\vert\\vert l\\ver...
...quencies in the Reuters collection of 806,791 documents.}
\\par
\\par
\\end{figure}](https://nlp.stanford.edu/IR-book/html/htmledition/img405.png)
* * *
[ ![next](http://nlp.stanford.edu/IR-book/html/icons/next.png)](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html) [ ![up](http://nlp.stanford.edu/IR-book/html/icons/up.png)](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) [ ![previous](http://nlp.stanford.edu/IR-book/html/icons/prev.png)](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) [ ![contents](http://nlp.stanford.edu/IR-book/html/icons/contents.png)](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html) [ ![index](http://nlp.stanford.edu/IR-book/html/icons/index.png)](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)   
**Next:** [Tf-idf weighting](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html) **Up:** [Term frequency and weighting](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) **Previous:** [Term frequency and weighting](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) **[Contents](https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html)** **[Index](https://nlp.stanford.edu/IR-book/html/htmledition/index-1.html)** © 2008 Cambridge University Press  
This is an automatically generated page. In case of formatting errors you may want to look at the [PDF edition](http://informationretrieval.org) of the book.  
2009-04-07 

