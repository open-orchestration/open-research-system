[ Joshua Entrop 👋 ](https://www.joshua-entrop.com/)
  * [ Home](https://www.joshua-entrop.com/)
  * [ Blog](https://www.joshua-entrop.com/blog.html)
  * [ Publications](https://www.joshua-entrop.com/publications.html)
  * [ Talks](https://www.joshua-entrop.com/talks.html)
  * [ Software](https://www.joshua-entrop.com/software.html)


# The 3 rules of do-calculus
Pearl’s _do_ -calculus offers a comprehensive set of rules for identifying causal effects from a causal directed acyclic graph (DAG). Using those rules, one can identify causal effects even in situations in which the commonly applied back-door criteria does not hold. In this blog post, I demonstrate how you can use Pearl’s _do_ -calculus to identify causal effects based on various example DAGs. 
causal inference
Author
Joshua Philipp Entrop 
Published
February 10, 2024
Heads up; its more fun to read this blog post if you have seen directed acyclic graphs (DAGs) before, as this blog post won’t provide an introduction to DAGs.
When I started to read up on causal inference during the beginning of my PhD studies, I often got stuck on the assumption of exchanability, i.e., Rubin’s ignorability assumption: Yx⊥⊥X|Z. I understood what the assumption means in theory and I understood how to use DAGs to identify confounders and colliders. Intuitively, I understood how the ignorability assumption and DAGs are connected, but I did not understand how they are theoretically connected. I mean, there are usually no counterfactuals in a DAG so how can one use DAGs to reason about whether counterfactuals are independent of the treatment assignment X. One solution is to use singe world interventions graphs (SWIGs), but they never felt really natural to me. Pearl’s _do_ -calculus instead offers a very nice combination of DAGs and the ignorability in my opinion. Hence, I think it is worth taking a closer look at the rules of _do_ -calculus and how they combine the irgnorability assumption and DAGs.
Before we can dive into Pearl’s _do_ -calculus and look at some examples, we first need to introduce a bit of specific notation. First, let W, X, Y, and Z be a set of unique variables. Second, let G be a directed acyclic graph which is associated with a causal model, let GX― be a submodel of G in which we remove all arrows going into X, and let GX― be a submodel of G in which we remove all arrows going out of X. Third, let do(x) define an operator for intervening on x. For example, P(y|do(x′)) indicates the value of y if we would change the value of x to the value x′. Lastly, let X⊥⊥Y denote that X and Y are independent of each other.
In his book _Causality_ , Pearl defines the three rules of _do_ -calculus which can be used to identify causal effects with the help of DAGs. The overall aim of _do_ -calculus is to translate expression including _do_ -statements to expression only including observed data. This allows us to identify and later estimate a causal effect using our observed data. Put in other word, using _do_ -calculus, we can translate a causal expression into an expression only including associations which we then can estimate from our observed data. This allows us to interpret association as causation if certain assumptions are fulfilled. Something that previously was only allowed the devil of epidemiological research.
Now you’re ready for the three rules. Listing carefully.
**Rule 1** (Insertion/deletion of observations) P(y|do(x),z,w)=P(y|do(x),w) if Y⊥⊥Z|X,W in GX―
In words, this tells us that we can remove a variable z from our expression if z is independent of y, given x and potentially other variables w, in the DAG in which we remove all arrows going into x.
**Rule 2** (Action/observation exchange) P(y|do(x),do(z),w)=P(y|do(x),z,w) if Y⊥⊥Z|X,W in GX―,Z―
In word, this tells us that we can replace the action do(z) with the variable z observed in the data if y and z are independent, given x and potentially other variables w, in the DAG in which we remove the arrow going into x and out of z. Note that this rule is a generalisation of the back-door criteria which you might now from before. If we are only interested in one action, e.g., do(x) we can simplify rule 2 as follow:
P(y|do(x),w)=P(y|x,w) if Y⊥⊥X|W in GX― This now is pretty much an expression of the commonly known back-door criteria.
**Rule 3** (insertion/deletion of actions) P(y|do(x),do(z),w)=P(y|do(x),w) if Y⊥⊥Z|X,W in GX―,Z(W)―
where Z(W) is the set of Z-nodes that are not ancestors of any W-node in GX―.
Last but not least, rule 3 is probably the most complicated one. In words rule 3 tells us that we can remove an expression, e.g., do(y) from our expression if Y and Z are independent, given X and potentially other variables Z, in the graph were we remove all arrow going out of X and all nodes of Z that are not ancestors of W.
Let’s use these rules of _do_ -calculus for identifying causal effects in some example graphs.
![](https://www.joshua-entrop.com/pictures/3_rules_of_do_calculus_dag_1.png)
(a) A very simple DAG  [](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#fig-dag-a)
![](https://www.joshua-entrop.com/pictures/3_rules_of_do_calculus_dag_2.png)
(b) A DAG with a confounder (Z)  [](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#fig-dag-b)
![](https://www.joshua-entrop.com/pictures/3_rules_of_do_calculus_dag_3.png)
(c) A DAG with a collider (Z)  [](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#fig-dag-c)
![](https://www.joshua-entrop.com/pictures/3_rules_of_do_calculus_dag_4.png)
(d) A DAG with an unmeasured confounder (U)  [](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#fig-dag-d)
Figure 1: Some example DAGs that we will use throughout the blog post. 
The first example in [Figure 1 (a)](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#fig-dag-a) might seem trivial, but I thought it might be a smooth start. In this graph there are no arrows connecting X and Y in GX―, that is, if we remove all the arrows going out of X. Hence, X and Y are independent in GX―, which means that we can apply rule 2 of _do_ -calculus:
P(y|do(x))=P(y|x)
Success! Using _do_ -calculus we could replace all the _do_ -statements with observed variables, which now allows us to estimate the causal effect of changing X on Y based on our observed data. This was quite an easy example. But before we continue with the next example, let’s take a closer look at GX― again. The reason why we are interested in looking at the graph in which we remove all arrows going out from X is that we want to make sure that X is only affecting Y directly or through causes that are caused by X, i.e., we are interested in the total effect of X on Y. Thus, if we remove all arrows going out of X or going into Y, and we find that in this submodel there is no open causal path between X and Y, we can be sure, that in the whole model G, all causal paths between X and Y must be direct paths, i.e., paths that we want to include in our estimation.
[Figure 1 (b)](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#fig-dag-b) includes a classical example of confounding, in which the variable Z confounds the effect of X on Y. If we remove all arrows going out of X, we find that X is still associated with Y through the fork X←Z→Y. Hence, we cannot directly disentangle the direct effect of X on Y and the association between X and Y that is due to the confounding of Z. However, as stated in rule 2 we can also condition on other variables to render X and Y independent in GX―.
P(y|do(x))=∑zP(y|do(x),z)P(z)=∑zP(y|x,z)P(z)Rule 2: Y⊥⊥X|Z in GX―
Ok, let’s go through this in more detail. The first step we need to do is to condition our analysis on the variable Z. This renders X and Y independent in GX―. After this, we can now replace P(y|do(x),z) with P(y|x,z) as X and Y are independent when conditioning on Z.
[Figure 1 (c)](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#fig-dag-c) again is a more simple example. In this graph X and Y are independent in GX― because Z is a collider on the path X→Z←Y. Hence, we can just calculate P(y|do(x)) based on our observed data P(y|x).
[Figure 1 (d)](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#fig-dag-d) is a tricky one and in contrast to the graphs before, we cannot only rely on rule 2 in order to identify the causal effect of X on Y. Using only the back-door criteria would not allow us to identify the causal effect of X on Y in this graph, but using _do_ -calculus we actually can identify this effect. For this, let’s first take a look at the effect that we would like to estimate:
(1)P(y|do(x))=∑zP(y|do(x),z)P(z|x)
Unfortunately, we cannot estimate the first part of the right hand hand side directly using only observed data, but we can achieve this with the help of both rule 2 and 3.
(2)P(y|do(x),z)=P(y|do(x),do(y))Rule 2: Y⊥⊥Z in GX―Z―=P(y|do(y))Rule 3: Y⊥⊥X in GX―Z―=∑xP(y|x,z)P(x)Rule 2: Y⊥⊥Z|X in GZ―
Now, we yielded an expression for the first part of the right hand site that only includes observed variables. Let’s do the same for the second part of the right hand side in [Equation 1](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#eq-dag-d-1). Translating this part of the equation to an expression, only including observed variables, is actually a lot easier, as Y is a collider on the path X←U→Y←Z which renders Z and Y independent in GX―.
(3)P(z|do(x))=P(z|x)Rule 2: Z⊥⊥X in GX―
Now, we have all pieces that we need in order to translate [Equation 1](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#eq-dag-d-1) into an expression only including observed variables. Let’s substitute [Equation 1](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#eq-dag-d-1) with [Equation 2](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#eq-dag-d-2) and [Equation 3](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#eq-dag-d-3):
(4)P(y|do(x))=∑zP(z|x)∑x′P(y|x′,z)P(x′)
Please note that we used x′ in [Equation 4](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#eq-dag-d-4) in order to differentiate between the x in do(x) and the x observed in our dataset. The second part of [Equation 4](https://www.joshua-entrop.com/post/the_3_rules_of_do_calculus.html#eq-dag-d-4) means a summation over all observed values of X independent of the value that is chosen for do(x).
By the way, if you don’t want to buy Pearl’s causality book, but you’re still interested in reading more about _do_ -calculus, you can find a short introduction to _do_ -calculus by Pearl [here](https://arxiv.org/ftp/arxiv/papers/1210/1210.4852.pdf). This paper also links to some other interesting applications of _do_ -calculus including, e.g., [selection bias](https://ftp.cs.ucla.edu/pub/stat_ser/r381.pdf) and [transportability analysis.](https://ftp.cs.ucla.edu/pub/stat_ser/r372-a.pdf).
  * [Terms](https://www.joshua-entrop.com/terms.html)   
© Joshua Philipp Entrop 2025 



