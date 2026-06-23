[![geeksforgeeks](https://media.geeksforgeeks.org/gfg-gg-logo.svg)](https://www.geeksforgeeks.org/)
![search icon](https://media.geeksforgeeks.org/auth-dashboard-uploads/Property=Light---Default.svg)
  * Sign In
  * Courses
  * Tutorials
  * Interview Prep


  * [Python for Machine Learning](https://www.geeksforgeeks.org/machine-learning/python-for-machine-learning/)
  * [Machine Learning with R](https://www.geeksforgeeks.org/r-machine-learning/introduction-to-machine-learning-in-r/)
  * [Machine Learning Algorithms](https://www.geeksforgeeks.org/machine-learning/machine-learning-algorithms/)
  * [EDA](https://www.geeksforgeeks.org/data-analysis/what-is-exploratory-data-analysis/)
  * [Math for Machine Learning](https://www.geeksforgeeks.org/machine-learning/machine-learning-mathematics/)
  * [Machine Learning Interview Questions](https://www.geeksforgeeks.org/machine-learning/machine-learning-interview-questions/)
  * [ML Projects](https://www.geeksforgeeks.org/machine-learning/machine-learning-projects/)
  * [Deep Learning](https://www.geeksforgeeks.org/deep-learning/deep-learning-tutorial/)
  * [NLP](https://www.geeksforgeeks.org/nlp/natural-language-processing-nlp-tutorial/)
  * [Computer vision](https://www.geeksforgeeks.org/computer-vision/computer-vision/)


# Offline Evaluation Metrics in Information Retrieval
Last Updated : 23 Jul, 2025
Information Retrieval is the process of obtaining relevant information from a collection of resources. It is crucial to evaluate the performance of these systems to ensure they work effectively. Evaluating these systems' effectiveness is essential to ensure they meet user needs. While online metrics like click-through rates (CTR) and user satisfaction surveys are valuable, offline evaluation metrics offer a controlled, reproducible way to assess IR systems' performance without requiring real-time user interactions.
In this article, we will majorly cover three widely used metrics: Mean Average Precision (MAP), Normalized Discounted Cumulative Gain (NDCG), and Fall-Out. 
Table of Content
  * [Understanding Offline Evaluation Metrics](https://www.geeksforgeeks.org/machine-learning/offline-evaluation-metrics-in-information-retrieval/#understanding-offline-evaluation-metrics)
  * [Key Offline Evaluation Metrics](https://www.geeksforgeeks.org/machine-learning/offline-evaluation-metrics-in-information-retrieval/#key-offline-evaluation-metrics)
    * [1. Mean Average Precision (MAP)](https://www.geeksforgeeks.org/machine-learning/offline-evaluation-metrics-in-information-retrieval/#1-mean-average-precision-map)
    * [2. Normalized Discounted Cumulative Gain (NDCG)](https://www.geeksforgeeks.org/machine-learning/offline-evaluation-metrics-in-information-retrieval/#2-normalized-discounted-cumulative-gain-ndcg)
    * [3. Fall-Out](https://www.geeksforgeeks.org/machine-learning/offline-evaluation-metrics-in-information-retrieval/#3-fallout)
    * [4. Precision, Recall and F1 Score](https://www.geeksforgeeks.org/machine-learning/offline-evaluation-metrics-in-information-retrieval/#4-precision-recall-and-f1-score)
  * [Challenges and Limitations](https://www.geeksforgeeks.org/machine-learning/offline-evaluation-metrics-in-information-retrieval/#challenges-and-limitations)
  * [Applications and Use Cases](https://www.geeksforgeeks.org/machine-learning/offline-evaluation-metrics-in-information-retrieval/#applications-and-use-cases)


## ****Understanding Offline Evaluation Metrics****
Offline evaluation metrics are used to measure the performance of an IR system without requiring real-time user interaction. These metrics are typically derived from relevance judgments, where human judges assess the relevance of documents returned by the system in response to specific queries. The main advantage of offline metrics is that they provide a consistent and repeatable way to evaluate IR systems, allowing for comparison across different systems and configurations.
### Importance of Offline Evaluation Metrics
Offline evaluation is crucial in the IR domain for several reasons:
  * ****Controlled Environment:**** Offline evaluations occur in a controlled setting, eliminating the noise and variability of user behavior.
  * ****Reproducibility:**** Results can be replicated, making it easier to compare different algorithms or system versions.
  * ****Early Testing:**** New models or features can be evaluated before deployment, reducing risks in production environments.


## ****Key Offline Evaluation Metrics****
### 1. Mean Average Precision (MAP)
[Mean Average Precision (MAP)](https://www.geeksforgeeks.org/computer-vision/mean-average-precision-map-in-computer-vision/) is one of the most important evaluation metrics in information retrieval. This metric provides a single-figure measure of quality across different recall levels. It is primarily used when we want to assess the quality of a ranked list of documents. 
The MAP score is calculated as the mean of the average precision scores for each query. The formula for MAP is:
MAP = (1/Q) * Σ(q=1 to Q) Average Precision(q)
  * Where Q is the number of queries,
  * and Average Precision(q) is the average precision for a single query.


We can calculate the Mean Average Precision using the metrics provided by Scikit-learn:
  * To do this, we will first import the `average_precision_score()` function from `sklearn.metrics`. 
  * Next, we will create sample data for true relevance and predicted scores. 
  * Finally, we will pass these variables to the function and obtain the Mean Average Precision.

Python `

```
from sklearn.metrics import average_precision_score

y_true = [0, 0, 1, 1]
y_scores = [0.1, 0.4, 0.35, 0.8]
map_score = average_precision_score(y_true, y_scores)

print(f"Mean Average Precision: {map_score:.2f}")

```

`
Output:

```
Mean Average Precision: 0.83
```

### 2. Normalized Discounted Cumulative Gain (NDCG)
[Normalized Dscounted Cumulative Gain (NDCG](https://www.geeksforgeeks.org/machine-learning/normalized-discounted-cumulative-gain-multilabel-ranking-metrics-ml/)) is another important metric in assess the quaity of information retrieval systems. Using this metric we make sure that quality of ranking is good for search results. It evaluates the position of relevant documents in the result list, and gives weight to highly relevant documents so that it appear early in the search result list. 
The NDCG is calculated using the following formula:
NDCG = DCG / IDCG
where DCG (Discounted Cumulative Gain) is calculated as:
DCG_k = Σ(i=1 to k) (2^rel_i - 1) / log_2(i + 1)
and IDCG (Ideal Discounted Cumulative Gain) is the DCG value of the ideal ranking.
****To implement this metric we can again use the sklearn.metrics module:****
  * We will first import the ndcg_score function from sklearn.metrics and numpy library.
  * Next we will create a sample data for true relevance and predicted scores.
  * Next we will pass these variables into the ndcg_score() function. Finally we can print the result.

Python `

```
from sklearn.metrics import ndcg_score
import numpy as np

y_true = np.asarray([[0, 0, 1], [0, 1, 1]])
y_score = np.asarray([[0.1, 0.4, 0.35], [0.2, 0.6, 0.3]])
ndcg = ndcg_score(y_true, y_score)

print(f"Normalized Dscounted Cumulative Gain (NDCG): {ndcg:.2f}")

```

`
Output:

```
Normalized Dscounted Cumulative Gain (NDCG): 0.82
```

### 3. Fall-Out
Fall-Out is a metric that calculates the proportion of non-relevant documents displayed out of all non-relevant documents available. Essentially, it represents the probability of a non-relevant document being retrieved. The formula for the Fall-Out metric is:
Fall-Out = Number of Non-Relevant Documents Retrieved / Total Number of Non-Relevant Documents
_****If we have a lower Fall-Out rate, it means the IR system is performing better, as it suggests that fewer non-relevant documents are being retrieved.****_
To illustrate the calculation of Fall-Out, we will use the `confusion_matrix` function from the `sklearn.metrics` module. After importing that function, we will create sample data for true relevance and predicted relevance. Next, we will pass these variables into the `confusion_matrix` function and call `ravel()`, which will calculate the components needed for the Fall-Out calculation. Finally, we will calculate the Fall-Out Rate using the above formula and print the final result.
Python `

```
from sklearn.metrics import confusion_matrix

y_true = [0, 1, 1, 0, 0, 1, 0]
y_pred = [0, 1, 0, 0, 0, 1, 1]
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
fall_out = fp / (fp + tn)

print(f"Fall-Out Value: {fall_out:.2f}")

```

`
Output:

```
Fall-Out Value: 0.25
```

###  4. ****Precision, Recall and F1 Score****
  * [****Precision****](https://www.geeksforgeeks.org/machine-learning/precision-recall-curve-ml/) is the fraction of retrieved documents that are relevant to the user's query. It is calculated as:


\text{Precision} = \frac{| \\{ \text{Relevant Documents} \\} \cap \\{ \text{Retrieved Documents} \\} |}{| \\{ \text{Retrieved Documents} \\} |} 
  * ****Recall**** is the fraction of relevant documents that have been retrieved over the total amount of relevant documents. It is calculated as:


\text{Recall} = \frac{| \\{ \text{Relevant Documents} \\} \cap \\{ \text{Retrieved Documents} \\} |}{| \\{ \text{Relevant Documents} \\} |} 
Precision and recall are fundamental metrics, but they often need to be balanced against each other, as improving one can lead to a decrease in the other.
  * [****The F1 score****](https://www.geeksforgeeks.org/machine-learning/f1-score-in-machine-learning/) is the harmonic mean of precision and recall, providing a single metric that balances both. It is particularly useful when the distribution between relevant and irrelevant documents is uneven:


\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} 
## ****Challenges and Limitations****
While offline evaluation metrics provide valuable insights, they have limitations. 
  * For instance, precision and recall assume binary relevance, which may not capture the nuances of user satisfaction. 
  * Additionally, these metrics rely heavily on relevance judgments, which can be subjective and vary between judges. 
  * Metrics like NDCG attempt to address these issues by considering the order of relevance and graded relevance scores.


## ****Applications and Use Cases****
Offline evaluation metrics are widely used in various applications:
  * ****Search Engines**** : Metrics like MAP and NDCG are crucial for evaluating the effectiveness of search algorithms in returning relevant results.
  * ****Recommendation Systems**** : Precision@K and Recall@K are often used to assess how well a system recommends relevant items to users.
  * ****Academic Research**** : Researchers use these metrics to benchmark new algorithms against existing ones, ensuring advancements in IR technology.


## ****Conclusion****
Offline evaluation metrics are indispensable tools for assessing the performance of information retrieval systems. They provide a standardized way to measure and compare systems, ensuring they meet user needs and perform efficiently. While they have limitations, these metrics are continually evolving to better capture the complexities of user satisfaction and relevance. By understanding and applying these metrics, developers and researchers can create more effective and user-friendly IR systems.
Comment
[A](https://www.geeksforgeeks.org/user/adilnaib/)
[adilnaib](https://www.geeksforgeeks.org/user/adilnaib/)
0
Article Tags:
Article Tags:
[Machine Learning](https://www.geeksforgeeks.org/category/ai-ml-ds/machine-learning/)
[AI-ML-DS](https://www.geeksforgeeks.org/category/ai-ml-ds/)
[AI-ML-DS With Python](https://www.geeksforgeeks.org/tag/ai-ml-ds-python/)
### Explore
Machine Learning Basics
    * [Introduction4 min read](https://www.geeksforgeeks.org/machine-learning/introduction-machine-learning/)
    * [Types7 min read](https://www.geeksforgeeks.org/machine-learning/types-of-machine-learning/)
    * [ML Pipeline6 min read](https://www.geeksforgeeks.org/blogs/machine-learning-pipeline/)
    * [Applications2 min read](https://www.geeksforgeeks.org/machine-learning/machine-learning-introduction/)
Python for Machine Learning
    * [ML with Python3 min read](https://www.geeksforgeeks.org/machine-learning/machine-learning-with-python/)
    * [Numpy3 min read](https://www.geeksforgeeks.org/python/numpy-tutorial/)
    * [Pandas4 min read](https://www.geeksforgeeks.org/pandas/pandas-tutorial/)
    * [Data Preprocessing4 min read](https://www.geeksforgeeks.org/data-analysis/data-preprocessing-machine-learning-python/)
    * [EDA6 min read](https://www.geeksforgeeks.org/data-analysis/exploratory-data-analysis-in-python/)
Feature Engineering
    * [Feature Engineering4 min read](https://www.geeksforgeeks.org/machine-learning/what-is-feature-engineering/)
    * [Dimensionality Reduction3 min read](https://www.geeksforgeeks.org/machine-learning/dimensionality-reduction/)
    * [Feature Selection4 min read](https://www.geeksforgeeks.org/machine-learning/feature-selection-techniques-in-machine-learning/)
Supervised Learning
    * [Supervised Learning4 min read](https://www.geeksforgeeks.org/machine-learning/supervised-machine-learning/)
    * [Linear Regression10 min read](https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/)
    * [Logistic Regression9 min read](https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/)
    * [Decision Tree8 min read](https://www.geeksforgeeks.org/machine-learning/decision-tree-introduction-example/)
    * [Random Forest4 min read](https://www.geeksforgeeks.org/machine-learning/random-forest-algorithm-in-machine-learning/)
    * [KNN8 min read](https://www.geeksforgeeks.org/machine-learning/k-nearest-neighbours/)
    * [SVM9 min read](https://www.geeksforgeeks.org/machine-learning/support-vector-machine-algorithm/)
    * [Naive Bayes6 min read](https://www.geeksforgeeks.org/machine-learning/naive-bayes-classifiers/)
Unsupervised Learning
    * [Unsupervised Learning5 min read](https://www.geeksforgeeks.org/machine-learning/unsupervised-learning/)
    * [K means Clustering6 min read](https://www.geeksforgeeks.org/machine-learning/k-means-clustering-introduction/)
    * [Hierarchical Clustering6 min read](https://www.geeksforgeeks.org/machine-learning/hierarchical-clustering/)
    * [DBSCAN Clustering6 min read](https://www.geeksforgeeks.org/machine-learning/dbscan-clustering-in-ml-density-based-clustering/)
    * [Apriori Algorithm5 min read](https://www.geeksforgeeks.org/machine-learning/apriori-algorithm/)
    * [FP Growth Algorithm4 min read](https://www.geeksforgeeks.org/machine-learning/frequent-pattern-growth-algorithm/)
    * [ECLAT Algorithm5 min read](https://www.geeksforgeeks.org/machine-learning/ml-eclat-algorithm/)
    * [PCA6 min read](https://www.geeksforgeeks.org/data-analysis/principal-component-analysis-pca/)
Model Evaluation and Tuning
    * [Evaluation Metrics9 min read](https://www.geeksforgeeks.org/machine-learning/metrics-for-machine-learning-model/)
    * [Regularization5 min read](https://www.geeksforgeeks.org/machine-learning/regularization-in-machine-learning/)
    * [Cross Validation5 min read](https://www.geeksforgeeks.org/machine-learning/cross-validation-machine-learning/)
    * [Hyperparameter Tuning5 min read](https://www.geeksforgeeks.org/machine-learning/hyperparameter-tuning/)
    * [Underfitting and Overfitting3 min read](https://www.geeksforgeeks.org/machine-learning/underfitting-and-overfitting-in-machine-learning/)
    * [Bias and Variance6 min read](https://www.geeksforgeeks.org/machine-learning/bias-vs-variance-in-machine-learning/)
Advanced Techniques
    * [Reinforcement Learning8 min read](https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/)
    * [Semi-Supervised Learning5 min read](https://www.geeksforgeeks.org/machine-learning/ml-semi-supervised-learning/)
    * [Self-Supervised Learning5 min read](https://www.geeksforgeeks.org/machine-learning/self-supervised-learning-ssl/)
    * [Ensemble Learning6 min read](https://www.geeksforgeeks.org/machine-learning/a-comprehensive-guide-to-ensemble-learning/)
Machine Learning Practice
    * [Interview Questions15+ min read](https://www.geeksforgeeks.org/machine-learning/machine-learning-interview-questions/)
    * [ML Projects5 min read](https://www.geeksforgeeks.org/machine-learning/machine-learning-projects/)
Courses
    * [Data Science and ML Course2 min read](https://www.geeksforgeeks.org/courses/data-science-live)
    * [Generative AI Course2 min read](https://www.geeksforgeeks.org/courses/generative-ai-training-program)
    * [Explore GATE Course2 min read](https://www.geeksforgeeks.org/courses/category/gate)


[![GeeksforGeeks](https://media.geeksforgeeks.org/auth-dashboard-uploads/gfgFooterLogo.png)](https://www.geeksforgeeks.org/)
![location](https://media.geeksforgeeks.org/img-practice/Location-1685004904.svg)
Corporate & Communications Address:
A-143, 6th Floor, Sovereign Corporate Tower, Sector- 136, Noida, Uttar Pradesh (201305)
![location](https://media.geeksforgeeks.org/img-practice/Location-1685004904.svg)
Registered Address:
K 061, Tower K, Gulshan Vivante Apartment, Sector 137, Noida, Gautam Buddh Nagar, Uttar Pradesh, 201305
[](https://in.linkedin.com/company/geeksforgeeks)[](https://www.instagram.com/geeks_for_geeks/)[](https://twitter.com/geeksforgeeks)[](https://www.facebook.com/geeksforgeeks.org/)[](https://www.youtube.com/geeksforgeeksvideos)
[![GFG App on Play Store](https://media.geeksforgeeks.org/auth-dashboard-uploads/googleplay-%281%29.png)](https://geeksforgeeksapp.page.link/gfg-app)[![GFG App on App Store](https://media.geeksforgeeks.org/auth-dashboard-uploads/appstore-%281%29.png)](https://geeksforgeeksapp.page.link/gfg-app)
  * Company
  * [About Us](https://www.geeksforgeeks.org/about/)
  * [Legal](https://www.geeksforgeeks.org/legal/)
  * [Privacy Policy](https://www.geeksforgeeks.org/legal/privacy-policy/)
  * [Contact Us](https://www.geeksforgeeks.org/about/contact-us/)
  * [Advertise with us](https://www.geeksforgeeks.org/advertise-with-us/)
  * [GFG Corporate Solution](https://www.geeksforgeeks.org/gfg-corporate-solution/)
  * [Campus Training Program](https://www.geeksforgeeks.org/campus-training-program/)


  * Explore
  * [POTD](https://www.geeksforgeeks.org/problem-of-the-day)
  * [Job-A-Thon](https://practice.geeksforgeeks.org/events/rec/job-a-thon/)
  * [Blogs](https://www.geeksforgeeks.org/category/blogs/?type=recent)
  * [Nation Skill Up](https://www.geeksforgeeks.org/nation-skill-up/)


  * Tutorials
  * [Programming Languages](https://www.geeksforgeeks.org/computer-science-fundamentals/programming-language-tutorials/)
  * [DSA](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
  * [Web Technology](https://www.geeksforgeeks.org/web-tech/web-technology/)
  * [AI, ML & Data Science](https://www.geeksforgeeks.org/machine-learning/ai-ml-and-data-science-tutorial-learn-ai-ml-and-data-science/)
  * [DevOps](https://www.geeksforgeeks.org/devops/devops-tutorial/)
  * [CS Core Subjects](https://www.geeksforgeeks.org/gate/gate-exam-tutorial/)
  * [Interview Preparation](https://www.geeksforgeeks.org/aptitude/interview-corner/)
  * [Software and Tools](https://www.geeksforgeeks.org/websites-apps/software-and-tools-a-to-z-list/)


  * Courses
  * [ML and Data Science](https://www.geeksforgeeks.org/courses/category/machine-learning-data-science)
  * [DSA and Placements](https://www.geeksforgeeks.org/courses/category/dsa-placements)
  * [Web Development](https://www.geeksforgeeks.org/courses/category/development-testing)
  * [Programming Languages](https://www.geeksforgeeks.org/courses/category/programming-languages)
  * [DevOps & Cloud](https://www.geeksforgeeks.org/courses/category/cloud-devops)
  * [GATE](https://www.geeksforgeeks.org/courses/category/gate)
  * [Trending Technologies](https://www.geeksforgeeks.org/courses/category/trending-technologies/)


  * Videos
  * [DSA](https://www.geeksforgeeks.org/videos/category/sde-sheet/)
  * [Python](https://www.geeksforgeeks.org/videos/category/python/)
  * [Java](https://www.geeksforgeeks.org/videos/category/java-w6y5f4/)
  * [C++](https://www.geeksforgeeks.org/videos/category/c/)
  * [Web Development](https://www.geeksforgeeks.org/videos/category/web-development/)
  * [Data Science](https://www.geeksforgeeks.org/videos/category/data-science/)
  * [CS Subjects](https://www.geeksforgeeks.org/videos/category/cs-subjects/)


  * Preparation Corner
  * [Interview Corner](https://www.geeksforgeeks.org/interview-prep/interview-corner/)
  * [Aptitude](https://www.geeksforgeeks.org/aptitude/aptitude-questions-and-answers/)
  * [Puzzles](https://www.geeksforgeeks.org/aptitude/puzzles/)
  * [GfG 160](https://www.geeksforgeeks.org/courses/gfg-160-series)
  * [System Design](https://www.geeksforgeeks.org/system-design/system-design-tutorial/)


[@GeeksforGeeks, Sanchhaya Education Private Limited](https://www.geeksforgeeks.org/), [All rights reserved](https://www.geeksforgeeks.org/copyright-information/)
![](https://www.geeksforgeeks.org/machine-learning/offline-evaluation-metrics-in-information-retrieval/)

