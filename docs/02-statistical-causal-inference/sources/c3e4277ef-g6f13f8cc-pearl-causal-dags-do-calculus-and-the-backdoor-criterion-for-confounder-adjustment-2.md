[Skip to content](https://towardsdatascience.com/causal-effects-via-dags-801df31da794/#wp--skip-link--target)
[![Towards Data Science](https://towardsdatascience.com/wp-content/uploads/2025/02/TDS-Vector-Logo.svg)](https://towardsdatascience.com/)
Publish AI, ML & data-science insights to a global community of data professionals.
Sign in
[Submit an Article](https://contributor.insightmediagroup.io/)
  * [Latest](https://towardsdatascience.com/latest/)
  * [Editor’s Picks](https://towardsdatascience.com/tag/editors-pick/)
  * [Deep Dives](https://towardsdatascience.com/tag/deep-dives/)
  * [Newsletter](https://towardsdatascience.com/tag/the-variable/)
* * *
  * [Write For TDS](https://towardsdatascience.com/submissions/)
[![Towards Data Science](https://towardsdatascience.com/wp-content/uploads/2025/02/TDS-Vector-Logo.svg)](https://towardsdatascience.com/)


Toggle Mobile Navigation
  * [LinkedIn](https://www.linkedin.com/company/towards-data-science/?originalSubdomain=ca)
  * [X](https://x.com/TDataScience)


Toggle Search
Search
[ Data Science ](https://towardsdatascience.com/category/data-science/)
# Causal Effects via DAGs
Breaking down the Back and Front Door Criteria 
[Shaw Talebi](https://towardsdatascience.com/author/shawhin/)
Nov 28, 2022
10 min read
Share 
This is the 4th article in a series on [causal effects](https://shawhin.medium.com/understanding-causal-effects-37a054b2ec3b). In the [last article](https://medium.com/towards-data-science/causal-effects-via-the-do-operator-5415aefc834a) of this series, we explored the question of **identifiability**. In other words, _can the causal effect be evaluated from the given data?_ There we saw a systematic 3-step process to express any causal effect given a causal model where all variables are observed. The problem, however, becomes much more interesting when we have **unmeasured confounders**. In this article, I discuss two quick-and-easy graphical criteria for evaluating causal effects.
* * *
## **Identifiability**
Identifiability is a central question in causal analysis i.e. _can the causal effect be evaluated from the given data?_ In the [previous blog](https://medium.com/towards-data-science/causal-effects-via-the-do-operator-5415aefc834a) _**,**_ we saw a systematic 3-step process for answering this question for so-called **Markovian causal models**. These causal models satisfy two conditions: 1) no cycles and 2) no unmeasured noise terms that simultaneously cause two or more variables. This type of model can be represented by a **directed cyclic graph** i.e. a **DAG**. Examples of Markovian and non-Markovian DAGs are shown below.
![Simple examples of non-Markovian and Markovian DAGs. Image by author.](https://towardsdatascience.com/wp-content/uploads/2022/11/1qjyUmsQXCIhrprBgXKtqOg.png)Simple examples of non-Markovian and Markovian DAGs. Image by author.
The Markov condition is important because it guarantees identifiability. In other words, **if our causal model is Markovian, then the causal effect is always identifiable** [[1](https://ftp.cs.ucla.edu/pub/stat_ser/R\[2\]\(https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2836213/pdf/ijb1203.pdf\)90-A.pdf), 2]. While this is a powerful insight, it is also restrictive because we may be interested in causal models that are not Markovian.
For example, a Markovian model could become non-Markovian if there is an unmeasured confounder. We saw an example of this in the [previous blog](https://medium.com/towards-data-science/causal-effects-via-the-do-operator-5415aefc834a). The same example is shown in the figure below.
![Example of how a Markovian model can become non-Markovian. Image by author.](https://towardsdatascience.com/wp-content/uploads/2022/11/1n5q8xlft7-KVfoZNuNkmVA.png)Example of how a Markovian model can become non-Markovian. Image by author.
We start with the Markovian model on the far left. Then suppose Jimmy forgot to turn on the Z2 sensor, so we have no observations for the variable Z2. This situation is depicted by the model in the middle. Here we have an unobserved variable (Z2) with two children (Z3 and Y).
We can equivalently represent this situation by removing the unobserved variable from the DAG and connecting its two child nodes with a bi-directed edge [[1](https://ftp.cs.ucla.edu/pub/stat_ser/R290-A.pdf)]. Intuitively, the bi-directed edge represents the statistical dependence between Z3 and Y via Z2, but without observations of Z2, this will appear as a spurious association between the two in our data.
Note that the two right-most causal models are not Markovian. The middle one has an unmeasured noise term that simultaneously causes two variables, and the far right one has a cycle. **Although these models are not Markovian, the causal effect of X on Y is indeed identifiable** (more on that later).
> [**Causal Effects via the Do-operator**](https://towardsdatascience.com/causal-effects-via-the-do-operator-5415aefc834a)
## **3 Rules of Do-Calculus**
In the general case, the question of identifiability can always be answered using the **Rules of Do-Calculus** [[3](https://faculty.sites.iastate.edu/jtian/files/inline-files/tian-shpitser-2009.pdf), [4](http://arxiv.org/abs/1210.4852)]. These are **3 rules we can use to manipulate interventional distributions** —in other words, expressing probabilities that include the do-operator in terms of probabilities that do not include the do-operator.
A key point is that **this set of rules is complete** , which means that if identifiability cannot be established with these 3 rules, then **the causal effect is not identifiable**.
**Rules of Do-Calculus** – Given X, Y, Z, and W are arbitrary disjoint sets of variables in a causal model G, the Rules of Do-Calculus are given below.
![3 Rules of Do-Calculus \[4\]. Image by author.](https://towardsdatascience.com/wp-content/uploads/2022/11/1EnmzQz60S2ahlCTniQmmkQ.png)3 Rules of Do-Calculus [[4](http://arxiv.org/abs/1210.4852)]. Image by author.
Although these rules are concise and complete, there is a lot to chew on here. For example, looking at rule 1, we can ignore the set of variables W only if Y and Z are conditionally independent in the graph obtained by deleting all the incoming arrows to the nodes in X.
Without a strong intuition for these rules and associated concepts, applying them to problems can be slow and challenging. That is where two quick and easy tests for identifiability can help.
## **2 Quick-and-Easy Graphical Criteria**
While the Rules of Do-Calculus give us a complete set of operations for evaluating causal effects, using them in practice can be difficult for complicated DAGs. To help with this difficulty, we can turn to 2 practical graphical criteria for evaluating identifiability: the **Back Door Criterion (BDC)** and the **Front Door Criterion (FDC).**
Unlike the rules of do-calculus, these criteria are not complete. Meaning even if they are not satisfied, the causal effect may still be identifiable. Their key utility, however, is they serve as practical tests we can readily apply to answer causal questions before resorting to the Rules of Do-Calculus.
### **1) Back Door Criterion**
The Back Door Criterion (BDC) is a relatively quick-and-easy test to evaluate if a set of nodes is sufficient to answer the question of identifiability. In other words, it tells us what variables we need to measure to calculate a particular causal effect.
Before defining the BDC, we first must arm ourselves with two key concepts: a **back-door path** and **blocking.**
A **back-door path** between 2 nodes (say X and Y) is **any path that starts with an arrow pointing into X** and terminates at Y [[3](https://faculty.sites.iastate.edu/jtian/files/inline-files/tian-shpitser-2009.pdf)]. For example, these are all the back door paths in the graph below.
  * **X** <- Z1 -> Z3 -> **Y**
  * **X** <- Z1 -> Z3 <- Z2 -> **Y**
  * **X** <- Z3 -> **Y**
  * **X** <- Z3 <- Z2 -> **Y**

![Example DAG to evaluate Back Door Criterion. Image by author.](https://towardsdatascience.com/wp-content/uploads/2022/11/1dVaOeTdkpk0pr0LkSPF8kg.png)Example DAG to evaluate Back Door Criterion. Image by author.
Notice that we ignore the arrowheads when constructing back-door paths (except, of course, for the one pointing into X). The intuition behind back door paths is they carry spurious associations between [2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2836213/pdf/ijb1203.pdf) variables [2].
The 2nd key concept here is that of **blocking** [[3](https://faculty.sites.iastate.edu/jtian/files/inline-files/tian-shpitser-2009.pdf)]. A path p is said to be blocked by a set of nodes {Z_i} if and only if,
  1. p contains a chain A -> B -> C or a fork A <- B -> C, such that B is an element in {Z_i} – _This is what we might intuitively think of as blocking_
  2. p contains a collider (i.e. an inverted fork) A -> B <- C, such that B and any of its descendants are not in {Z _i}_ — No node in {Z _i} creates a spurious statistical association (Berkson’s Paradox)_


We can now combine these concepts to define the back door criterion [[3](https://faculty.sites.iastate.edu/jtian/files/inline-files/tian-shpitser-2009.pdf)].
**Back Door Criterion –** A set of nodes {Z_i} satisfy the BDC relative to (X, Y) if,
  1. No node is a descendant of X (i.e. {Z_i} exclusively sit in back-door paths)
  2. {Z_i} blocks every back door path between X and Y


Applying the BDC to the above graph, we can see that three sets of nodes satisfy this criterion [[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2836213/pdf/ijb1203.pdf)].
  * {Z1, Z3}
  * {Z2, Z3}
  * {Z1, Z2, Z3}


Notice the set **{Z3} does not satisfy the BDC** because it is a collider and thus does not satisfy our definition of blocking from before.
The sets **** {Z1, Z3}, {Z2, Z3}, and {Z1, Z2, Z3} are called** sufficient set**s (also admissible sets). They** tell us which variables to measur**e to calculate unbiased causal effects between X and Y. We can express the interventional distribution using the following equation whenever the BDC is satisfied.
![Interventional distribution expressed in terms of observational distributions when Back Door Criterion is satisfied. Image by author.](https://towardsdatascience.com/wp-content/uploads/2022/11/1ifnuA7xBQuKD6_Xbya_jjw.png)Interventional distribution expressed in terms of observational distributions when Back Door Criterion is satisfied. Image by author.
### **Note on Propensity Score Methods**
A key point connecting the back door criterion to the Propensity Score (PS) methods we saw in an [earlier blog](https://medium.com/towards-data-science/propensity-score-5c\[2\]\(https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2836213/pdf/ijb1203.pdf\)9c480130c) is **Propensity Score methods fail when the back door criterion is not satisfied** [2]. In other words, if the variables used to derive a propensity score do not make up a sufficient set, they may introduce bias into the causal effect estimate.
While one may (naively) think the more variables used in the PS model, the better, this can backfire [[5](https://ftp.cs.ucla.edu/pub/stat_ser/r348.pdf)]. In some cases, like with variable Z3 in the above DAG, including particular variables may increase propensity score matching bias [[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2836213/pdf/ijb1203.pdf)].
> [**Causal Effects via Propensity Scores**](https://towardsdatascience.com/propensity-score-5c29c480130c)
### **2) Front Door Criterion**
Another quick-and-easy test we can use to evaluate identifiability is the **Front Door criterion** **(FDC)** [[3](https://faculty.sites.iastate.edu/jtian/files/inline-files/tian-shpitser-2009.pdf)]. A set of nodes {Z_i} satisfy the FDC relative to (X, Y) if
  1. {Z_i} intercepts all directed paths from X to Y
  2. All back door paths from X to {Z_i} are blocked by the empty set
  3. All back door paths from {Z_i} to Y are blocked by X


Let’s look at another example. Consider the DAG below.
![Example DAG to evaluate Front Door Criterion. Image by author.](https://towardsdatascience.com/wp-content/uploads/2022/11/1hytJ-bBJZDql82jm_ZpClQ.png)Example DAG to evaluate Front Door Criterion. Image by author.
We can first seek a set of variables that satisfies **condition 1**. To do that, we enumerate all the directed paths from X and Y. In this case, there are only 3.
  * X -> Z1 -> Y
  * X -> Z2 -> Y
  * X -> Z2 -> Y


From this, we can see {Z1, Z2} satisfies condition 1. But we aren’t done yet. We need to check whether this set satisfied the FDC by checking it against conditions 2 and 3.
To check **condition 2,** we need to look at all the back door paths from X to every node in {Z1, Z2}.
**X and Z1**
  * X <- Z3 -> Y <- Z1
  * X <- Z5 -> Z3 -> Y <- Z1


**X and Z2**
  * X <- Z3 -> Y <- Z2
  * X <- Z5 -> Z3 -> Y <- Z2
  * X <- Z5 -> Z3 -> Y <- Z4 <- Z2


We can see that all **these paths are blocked** because they include a collider Y.
Then finally, we check **condition 3** by looking at all the back door paths between every variable in {Z1, Z2} and Y.
**Z1 and Y**
  * Z1 <- X <- Z3 -> Y
  * Z1 <- X <- Z5 -> Z3 -> Y
  * Z1 <- X -> Z2 -> Y
  * Z1 <- X -> Z2 <- Z4 -> Y


**Z2 and Y**
  * Z2 <- X <- Z3 -> Y
  * Z2 <- X <- Z5 -> Z3 -> Y
  * Z2 <- X -> Z1 -> Y


And indeed, we see that all these paths are blocked by X. Thus, we conclude that in order to estimate the causal effect of X and Y, we need only measure variables X, Y, Z1, and Z2. We can do this using the equation below, which expresses the interventional distribution P(Y|do(x)) in terms of observational distributions, including X, Y, Z1, and Z2
![Interventional distribution expressed in terms of observational distributions when Front Door Criterion is satisfied. Image by author.](https://towardsdatascience.com/wp-content/uploads/2022/11/1BOHiLpq9TJCOZl2a7wt_Tw.png)Interventional distribution expressed in terms of observational distributions when Front Door Criterion is satisfied. Image by author.
Notice for each variable in {Z_i}, we sum over all possible values of variable X. Writing things out a little more explicitly for the above example we have.
![Interventional distribution for the FDC example DAG given above. Image by author.](https://towardsdatascience.com/wp-content/uploads/2022/11/1oxZGjt1VGMVlZo1QCpe3tw.png)Interventional distribution for the FDC example DAG given above. Image by author.
## Key Points:
  * **Identifiability** is concerned with answering the question: _can the causal effect be evaluated from the given data?_
  * The **3 Rules of Do-Calculus** gives us a complete set of operations to evaluate identifiability.
  * We can also evaluate identifiability via two quick-and-easy graphical tests: the **Back Door Criterion** and the **Front Door Criterion.**


### What’s next?
> [**Causal Effects via Regression**](https://towardsdatascience.com/causal-effects-via-regression-28cb58a2fffc)
* * *
👉 **More on Causality** : [Causal Effects Overview](https://shawhin.medium.com/understanding-causal-effects-37a054b2ec3b) | [Causality: Intro](https://towardsdatascience.com/causality-an-introduction-f8a3f6ac4c4a) | [Causal Inference](https://towardsdatascience.com/causal-inference-962ae97cefda) | [Causal Discovery](https://towardsdatascience.com/causal-discovery-6858f9af6dcb)
## Resources
**Connect** : [My website](https://shawhintalebi.com/) | [Book a call](https://calendly.com/shawhintalebi)
**Socials** : [YouTube 🎥 ](https://www.youtube.com/channel/UCa9gErQ9AE5jT2DZLjXBIdA) | [LinkedIn](https://www.linkedin.com/in/shawhintalebi/) | [Twitter](https://twitter.com/ShawhinT)
**Support** : [Buy me a coffee](https://www.buymeacoffee.com/shawhint?source=about_page-------------------------------------) ☕️
> [**Get FREE access to every new story I write**](https://shawhin.medium.com/subscribe)
* * *
[[1](https://ftp.cs.ucla.edu/pub/stat_ser/R290-A.pdf)] Tian, J., & Pearl, J. (2002). A General Identification Condition for Causal Effects. _Proceedings of the Eighteenth National Conference on Artificial Intelligence_. [www.aaai.org](http://www.aaai.org)
[[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2836213/pdf/ijb1203.pdf)] Pearl, J. (2010). The International Journal of Biostatistics: An Introduction to Causal Inference. _The International Journal of Biostatistics_ , _6_(2), Article 7. <https://doi.org/10.2202/1557-4679.1203>
[[3](https://faculty.sites.iastate.edu/jtian/files/inline-files/tian-shpitser-2009.pdf)] Tian, J., & Shpitser, I. (n.d.). _On Identifying Causal Effects_.
[[4](https://arxiv.org/abs/1210.4852\))] Pearl, J. (2012). The Do-Calculus Revisited. _Proceedings of the Twenty-Eight Conference on Uncertainty in Artificial Intelligence_ , _August_ , 4–11. <http://arxiv.org/abs/1210.4852>
[[5](https://ftp.cs.ucla.edu/pub/stat_ser/r348.pdf)] Pearl, J. (2009). _Myth, Confusion, and Science in Causal Analysis_.
* * *
Written By
Shaw Talebi
[See all from Shaw Talebi](https://towardsdatascience.com/author/shawhin/)
[Causal Effects](https://towardsdatascience.com/tag/causal-effects/), [Causal Inference](https://towardsdatascience.com/tag/causal-inference/), [Causality](https://towardsdatascience.com/tag/causality/), [Data Science](https://towardsdatascience.com/tag/data-science/), [Directed Acyclic Graph](https://towardsdatascience.com/tag/directed-acyclic-graph/)
Share This Article
  * [ Share on Facebook  ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Ftowardsdatascience.com%2Fcausal-effects-via-dags-801df31da794%2F&title=Causal%20Effects%20via%20DAGs)
  * [ Share on LinkedIn  ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Ftowardsdatascience.com%2Fcausal-effects-via-dags-801df31da794%2F&title=Causal%20Effects%20via%20DAGs)
  * [ Share on X  ](https://x.com/share?url=https%3A%2F%2Ftowardsdatascience.com%2Fcausal-effects-via-dags-801df31da794%2F&text=Causal%20Effects%20via%20DAGs)


Towards Data Science is a community publication. Submit your insights to reach our global audience and earn through the TDS Author Payment Program.
[Write for TDS](https://towardsdatascience.com/questions-96667b06af5/)
## Related Articles
  * ![](https://towardsdatascience.com/wp-content/uploads/2024/08/0c09RmbCCpfjAbSMq.png)
## [Implementing Convolutional Neural Networks in TensorFlow](https://towardsdatascience.com/implementing-convolutional-neural-networks-in-tensorflow-bc1c4f00bd34/)
[ Artificial Intelligence ](https://towardsdatascience.com/category/artificial-intelligence/)
Step-by-step code guide to building a Convolutional Neural Network 
[Shreya Rao](https://towardsdatascience.com/author/shreya-rao/)
August 20, 2024
6 min read
  * ![Photo by davisuko on Unsplash](https://towardsdatascience.com/wp-content/uploads/2024/08/1bAABgtZtAIG5YW1oEjW3pA-scaled.jpeg)
## [Hands-on Time Series Anomaly Detection using Autoencoders, with Python](https://towardsdatascience.com/hands-on-time-series-anomaly-detection-using-autoencoders-with-python-7cd893bbc122/)
[ Data Science ](https://towardsdatascience.com/category/data-science/)
Here’s how to use Autoencoders to detect signals with anomalies in a few lines of… 
[Piero Paialunga](https://towardsdatascience.com/author/piero-paialunga/)
August 21, 2024
12 min read
  * ## [Solving a Constrained Project Scheduling Problem with Quantum Annealing](https://towardsdatascience.com/solving-a-constrained-project-scheduling-problem-with-quantum-annealing-d0640e657a3b/)
[ Data Science ](https://towardsdatascience.com/category/data-science/)
Solving the resource constrained project scheduling problem (RCPSP) with D-Wave’s hybrid constrained quadratic model (CQM) 
[Luis Fernando PÉREZ ARMAS, Ph.D.](https://towardsdatascience.com/author/luisfernandopa1212/)
August 20, 2024
29 min read
  * ![](https://towardsdatascience.com/wp-content/uploads/2023/02/1VEUgT5T4absnTqBMOEuNig.png)
## [Back To Basics, Part Uno: Linear Regression and Cost Function](https://towardsdatascience.com/back-to-basics-part-uno-linear-regression-cost-function-and-gradient-descent-590dcb3eee46/)
[ Data Science ](https://towardsdatascience.com/category/data-science/)
An illustrated guide on essential machine learning concepts 
[Shreya Rao](https://towardsdatascience.com/author/shreya-rao/)
February 3, 2023
6 min read
  * ![](https://towardsdatascience.com/wp-content/uploads/2024/08/1kM8tfYcdaoccB1HX71YDig.png)
## [Must-Know in Statistics: The Bivariate Normal Projection Explained](https://towardsdatascience.com/must-know-in-statistics-the-bivariate-normal-projection-explained-ace7b2f70b5b/)
[ Data Science ](https://towardsdatascience.com/category/data-science/)
Derivation and practical examples of this powerful concept 
[Luigi Battistoni](https://towardsdatascience.com/author/lu-battistoni/)
August 14, 2024
7 min read
  * ![Photo by Alex Geerts on Unsplash](https://towardsdatascience.com/wp-content/uploads/2020/11/0BF38u2sw4WQdaMLS-scaled.jpg)
## [Our Columns](https://towardsdatascience.com/our-columns-53501f74c86d/)
[ Data Science ](https://towardsdatascience.com/category/data-science/)
Columns on TDS are carefully curated collections of posts on a particular idea or category… 
[TDS Editors](https://towardsdatascience.com/author/towardsdatascience/)
November 14, 2020
4 min read
  * ![Image created by authors with GPT-4o](https://towardsdatascience.com/wp-content/uploads/2024/08/1vilI3Q4nlwqsAQLq3TOzSA.jpg)
## [Optimizing Marketing Campaigns with Budgeted Multi-Armed Bandits](https://towardsdatascience.com/optimizing-marketing-campaigns-with-budgeted-multi-armed-bandits-a65fccd61878/)
[ Data Science ](https://towardsdatascience.com/category/data-science/)
With demos, our new solution, and a video 
[Vadim Arzamasov](https://towardsdatascience.com/author/vadim-arzamasov/)
August 16, 2024
10 min read


  * [YouTube](https://www.youtube.com/c/TowardsDataScience)
  * [X](https://x.com/TDataScience)
  * [LinkedIn](https://www.linkedin.com/company/towards-data-science/?originalSubdomain=ca)
  * [Threads](https://www.threads.net/@towardsdatascience)
  * [Bluesky](https://bsky.app/profile/towardsdatascience.com)


[![Towards Data Science](https://towardsdatascience.com/wp-content/uploads/2025/02/TDS-Vector-Logo.svg)](https://towardsdatascience.com/)
Your home for data science and Al. The world’s leading publication for data science, data analytics, data engineering, machine learning, and artificial intelligence professionals. 
©  Insight Media Group, LLC 2026 
Subscribe to Our Newsletter 
  * [Write For TDS](https://towardsdatascience.com/questions-96667b06af5/)
  * [About](https://towardsdatascience.com/about-towards-data-science-d691af11cc2f/)
  * [Advertise](https://contact.towardsdatascience.com/advertise-with-towards-data-science)
  * [Privacy Policy](https://towardsdatascience.com/privacy-policy/)
  * [Terms of Use](https://towardsdatascience.com/website-terms-of-use/)


Some areas of this page may shift around if you resize the browser window. Be sure to check heading and document order.

