[![geeksforgeeks](https://media.geeksforgeeks.org/gfg-gg-logo.svg)](https://www.geeksforgeeks.org/)
![search icon](https://media.geeksforgeeks.org/auth-dashboard-uploads/Property=Light---Default.svg)
  * Sign In
  * Courses
  * Tutorials
  * Interview Prep


  * [Artificial Intelligence](https://www.geeksforgeeks.org/artificial-intelligence/artificial-intelligence/)
  * [Interview Questions](https://www.geeksforgeeks.org/artificial-intelligence/artificial-intelligenceai-interview-questions-and-answers/)
  * [Project Ideas](https://www.geeksforgeeks.org/artificial-intelligence/best-artificial-intelligence-project-ideas/)
  * [Search Algorithms](https://www.geeksforgeeks.org/machine-learning/search-algorithms-in-ai/)
  * [Local Search Algorithm](https://www.geeksforgeeks.org/artificial-intelligence/local-search-algorithm-in-artificial-intelligence/)
  * [Generative AI](https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/)
  * [Data Science](https://www.geeksforgeeks.org/data-science/data-science-for-beginners/)
  * [Machine Learning](https://www.geeksforgeeks.org/machine-learning/machine-learning/)
  * [Deep Learning](https://www.geeksforgeeks.org/deep-learning/deep-learning-tutorial/)
  * [ML-Projects](https://www.geeksforgeeks.org/machine-learning/machine-learning-projects/)


# Corrective Retrieval Augmented Generation (CRAG)
Last Updated : 9 Oct, 2025
CRAG improves [Retrieval-Augmented Generation](https://www.geeksforgeeks.org/nlp/what-is-retrieval-augmented-generation-rag/) by incorporating a self correction mechanism that evaluates and refines retrieved knowledge reducing errors and improving accuracy, while RAG retrieves documents and uses them to guide an LLM’s response. CRAG handles noisy, irrelevant or misleading data. It can be coupled with various RAG based approaches.
The technique is based upon a ****feedback loop**** that continuously evaluates the quality of retrieved documents and provides evaluation. 
![query](https://media.geeksforgeeks.org/wp-content/uploads/20250922105557397187/query.webp)Traditional RAG
## Why CRAG is Needed
Below are the key reasons why CRAG is important in improving traditional RAG systems:
  1. ****Irrelevant Retrieval:**** Filters out documents that look similar but don’t answer the query.
  2. ****Noise and Errors:**** Detects and removes outdated or low quality information.
  3. ****Hallucinations:**** Validates retrieved context to reduce made-up or incorrect answers.
  4. ****Reliability:**** Ensures accurate and contextually correct information, critical for sensitive fields.
  5. ****Ranking of Documents:**** Re-ranks documents so the most relevant ones are prioritized.
  6. ****Dynamic Knowledge:**** Checks that retrieved data is current and relevant.
  7. ****Bias Reduction:**** Validates beyond similarity scores to prevent retrieval bias.


> ****For example,**** when asking __“What do koalas eat?”__ , RAG might retrieve documents about eucalyptus leaves but also mix in texts about pandas eating bamboo or kangaroos grazing grass, which can confuse the answer. CRAG adds a corrective step that filters out these irrelevant documents, keeping only accurate content about koalas so the final response clearly states they primarily eat eucalyptus leaves.
## Working of CRAG
![pass_doc](https://media.geeksforgeeks.org/wp-content/uploads/20250922105707562097/pass_doc.webp)Corrective RAG 
The step by step working of CRAG is mentioned below :
****1. Input Query:**** The process begins with an input query like “What do koalas eat?”. 
****2. Retrieval (Vanilla RAG):**** The documents from knowledge base are selected based on their relevance to the input query.The retriever finds top K relevant documents based only on similarity.
****3. Retrieval Evaluator:**** The relevance and quality of each document concerning the input query is assessed. The evaluator assigns a relevance score to each document.
****4. Decision:**** Based on previous step, a decision is made.
  * ****Correct:**** If at least one document has a high relevance score then it is relevant and accurate.
  * ****Incorrect: I**** f all documents have low relevance scores then they are irrelevant or incorrect.
  * ****Ambiguous:**** If the relevance scores are neither low nor high then there is uncertainty about the overall quality.


****5. Corrective Step (if Correct):**** This ensures only the most accurate and context specific documents are kept.
  * ****Filter:**** Removes low quality or outdated documents.
  * ****Rerank:**** Combines similarity, quality and freshness to reorder docs.
  * ****Duplication:**** Prevents repeated or duplicated results.


6. ****Web Search (if Incorrect):**** If the documents areincorrect****,**** web search is conducted to retrieve additional relevant information from the internet to make the knowledge base dynamic.
****7. Combining Knowledge (if Ambiguous):**** If the documents areambiguous, it combines both internal knowledge from initial retrieval and external knowledge from web search.
****8. Answer Generation:**** The [LLM](https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/) uses uses only corrected, refined or newly retrieved information to generate more accurate and factual response.
> The process starts by retrieving documents then using a corrective step to check their relevance and accuracy to the input query.
## Implementation of CRAG 
The steps to implement Corrective RAG are mentioned below :
### Step 1: Importing Libraries
Installing the required libraries and packages for our model.
Python `

```
from collections import Counter
from math import sqrt
import re
from datetime import datetime

```

`

```
from collections import Counter
```


```
from math import sqrt
```

```
import re
```

```
from datetime import datetime
```

### Step 2: Sample Knowledge Base
Defining a knowledge base as a list of documents. 
Python `

```
KB = [
    {
        "id": "doc1",
        "text": "Koalas eat eucalyptus leaves as their primary food source.",
        "date": "2022-03-15",
        "source": "wildlife_journal",
        "quality": 0.9,
    },
    {
        "id": "doc2",
        "text": "Pandas eat mostly bamboo shoots and leaves.",
        "date": "2019-08-10",
        "source": "zoo_digest",
        "quality": 0.8,
    },
    {
        "id": "doc3",
        "text": "Kangaroos graze on grasses and shrubs.",
        "date": "2020-11-20",
        "source": "australia_fauna",
        "quality": 0.85,
    },
]

```

`

```
KB = [
```


```
    {
```

```
        "id": "doc1",
```

```
        "text": "Koalas eat eucalyptus leaves as their primary food source.",
```

```
        "date": "2022-03-15",
```

```
        "source": "wildlife_journal",
```

```
        "quality": 0.9,
```

```
    },
```

```
    {
```

```
        "id": "doc2",
```

```
        "text": "Pandas eat mostly bamboo shoots and leaves.",
```

```
        "date": "2019-08-10",
```

```
        "source": "zoo_digest",
```

```
        "quality": 0.8,
```

```
    },
```

```
    {
```

```
        "id": "doc3",
```

```
        "text": "Kangaroos graze on grasses and shrubs.",
```

```
        "date": "2020-11-20",
```

```
        "source": "australia_fauna",
```

```
        "quality": 0.85,
```

```
    },
```

```
]
```

### Step 3: Retriever (Vanilla RAG)
  * ****tokenize (text):**** Simple regex tokenizer lowercases words.
  * ****build_vocab (docs):**** Makes a vocabulary from tokens across docs and query.
  * ****vectorize (text, vocab):**** Builds a term frequency vector and L2 normalizes it (TF only).
  * ****cosine (a, b):**** Dot product of normalized vectors is equal to cosine similarity.
  * ****retrieve_top_k (query, kb, k):**** Builds vocab, vectorizes query and each document, computes similarity, returns top k.

Python `

```
WORD_RE = re.compile(r"[a-zA-Z0-9']+")

def tokenize(text):
    return [t.lower() for t in WORD_RE.findall(text)]

def build_vocab(docs):
    vocab = {}
    for d in docs:
        for w in set(tokenize(d["text"])):
            if w not in vocab:
                vocab[w] = len(vocab)
    return vocab

def vectorize(text, vocab):
    vec = [0.0] * len(vocab)
    for w, cnt in Counter(tokenize(text)).items():
        if w in vocab:
            vec[vocab[w]] = float(cnt)
    norm = sqrt(sum(x*x for x in vec))
    if norm > 0:
        vec = [x/norm for x in vec]
    return vec

def cosine(a, b):
    return sum(x*y for x,y in zip(a,b))

def retrieve_top_k(query, kb, k=3):
    vocab = build_vocab(kb + [{"text": query}])
    qv = vectorize(query, vocab)
    scores = []
    for d in kb:
        dv = vectorize(d["text"], vocab)
        scores.append((d, cosine(qv, dv)))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:k]

```

`

```
WORD_RE = re.compile(r"[a-zA-Z0-9']+")
```


```
​
```

```
def tokenize(text):
```

```
    return [t.lower() for t in WORD_RE.findall(text)]
```

```
​
```

```
def build_vocab(docs):
```

```
    vocab = {}
```

```
    for d in docs:
```

```
        for w in set(tokenize(d["text"])):
```

```
            if w not in vocab:
```

```
                vocab[w] = len(vocab)
```

```
    return vocab
```

```
​
```

```
def vectorize(text, vocab):
```

```
    vec = [0.0] * len(vocab)
```

```
    for w, cnt in Counter(tokenize(text)).items():
```

```
        if w in vocab:
```

```
            vec[vocab[w]] = float(cnt)
```

```
    norm = sqrt(sum(x*x for x in vec))
```

```
    if norm > 0:
```

```
        vec = [x/norm for x in vec]
```

```
    return vec
```

```
​
```

```
def cosine(a, b):
```

```
    return sum(x*y for x,y in zip(a,b))
```

```
​
```

```
def retrieve_top_k(query, kb, k=3):
```

```
    vocab = build_vocab(kb + [{"text": query}])
```

```
    qv = vectorize(query, vocab)
```

```
    scores = []
```

```
    for d in kb:
```

```
        dv = vectorize(d["text"], vocab)
```

```
        scores.append((d, cosine(qv, dv)))
```

```
    scores.sort(key=lambda x: x[1], reverse=True)
```

```
    return scores[:k]
```

### Step 4: Corrective Step (CRAG)
****corrective_filter_and_rerank (retrieved, min_quality=0.7):****
  * Drops documents whose quality < min_quality.
  * Computes a freshness score from document date (freshness = 1 / (1 + days/365), recent: score closer to 1.
  * Builds a combined score = 0.6 * sim + 0.3 * quality + 0.1 * freshness.
  * Sorts documents by combined score and returns them.

Python `

```
def corrective_filter_and_rerank(retrieved, min_quality=0.7):
    today = datetime.today()
    corrected = []
    for doc, sim in retrieved:
        if doc["quality"] < min_quality:
            continue
        
        ddate = datetime.strptime(doc["date"], "%Y-%m-%d")
        days = (today - ddate).days
        freshness = 1.0 / (1.0 + days/365.0)
        combined = 0.6*sim + 0.3*doc["quality"] + 0.1*freshness
        corrected.append((doc, combined))
    corrected.sort(key=lambda x: x[1], reverse=True)
    return corrected

```

`

```
def corrective_filter_and_rerank(retrieved, min_quality=0.7):
```


```
    today = datetime.today()
```

```
    corrected = []
```

```
    for doc, sim in retrieved:
```

```
        if doc["quality"] < min_quality:
```

```
            continue
```

```
        
```

```
        ddate = datetime.strptime(doc["date"], "%Y-%m-%d")
```

```
        days = (today - ddate).days
```

```
        freshness = 1.0 / (1.0 + days/365.0)
```

```
        combined = 0.6*sim + 0.3*doc["quality"] + 0.1*freshness
```

```
        corrected.append((doc, combined))
```

```
    corrected.sort(key=lambda x: x[1], reverse=True)
```

```
    return corrected
```

### Step 5: Answer Generator
****generate_answer (query, corrected):****
  * If no corrected docs then it returns a polite “no reliable info found.”
  * Otherwise it picks the top corrected doc and returns a simple answer. In the demo, if "koala" is in the query, return "Koalas primarily eat eucalyptus leaves".

Python `

```
def generate_answer(query, corrected):
    if not corrected:
        return "Sorry, no reliable info found."
    
    doc = corrected[0][0]
    if "koala" in query.lower():
        return "Koalas primarily eat eucalyptus leaves."
    return doc["text"]

```

`

```
def generate_answer(query, corrected):
```


```
    if not corrected:
```

```
        return "Sorry, no reliable info found."
```

```
    
```

```
    doc = corrected[0][0]
```

```
    if "koala" in query.lower():
```

```
        return "Koalas primarily eat eucalyptus leaves."
```

```
    return doc["text"]
```

### Step 6: Demo Run
  * ****Vanilla Retrieval:**** Shows top K docs with similarity scores.
  * ****After CRAG Correction:**** Shows reranked docs with combined score.
  * ****Final Answer:**** Generated answer.

Python `

```
if __name__ == "__main__":
    query = "What do koalas eat?"
    print("Query:", query)

    
    retrieved = retrieve_top_k(query, KB, k=3)
    print("\nVanilla Retrieval:")
    for d, s in retrieved:
        print(f"- {d['id']} (sim={s:.2f}, quality={d['quality']}, date={d['date']})")

    
    corrected = corrective_filter_and_rerank(retrieved, min_quality=0.7)
    print("\nAfter CRAG Correction:")
    for d, c in corrected:
        print(f"- {d['id']} (combined={c:.2f})")

    
    answer = generate_answer(query, corrected)
    print("\nFinal Answer:", answer)

```

`

```
if __name__ == "__main__":
```


```
    query = "What do koalas eat?"
```

```
    print("Query:", query)
```

```
​
```

```
    
```

```
    retrieved = retrieve_top_k(query, KB, k=3)
```

```
    print("\nVanilla Retrieval:")
```

```
    for d, s in retrieved:
```

```
        print(f"- {d['id']} (sim={s:.2f}, quality={d['quality']}, date={d['date']})")
```

```
​
```

```
    
```

```
    corrected = corrective_filter_and_rerank(retrieved, min_quality=0.7)
```

```
    print("\nAfter CRAG Correction:")
```

```
    for d, c in corrected:
```

```
        print(f"- {d['id']} (combined={c:.2f})")
```

```
​
```

```
    
```

```
    answer = generate_answer(query, corrected)
```

```
    print("\nFinal Answer:", answer)
```

****Output****
![CRAG-IM2](https://media.geeksforgeeks.org/wp-content/uploads/20250919155139248978/CRAG-IM2.png)Final Output
## Applications of CRAG 
Some key use cases are:
  1. ****Healthcare:**** In medicine, even a small retrieval errorcan be dangerous****.**** CRAG ensures that only validated, accurate and context specific medical information is passed to the LLM. For example, when a doctor asks “safe antibiotic dosage for children under 5,” CRAG filters out irrelevant studies or outdated dosage charts. 
  2. ****Government and Public Services:**** Policies, forms and regulations frequently change. Wrong retrieval can mislead citizens. For example, when a citizen asks “requirements for passport renewal,” CRAG provides the most recent official guidelines.
  3. ****Scientific Research:**** It is a vast domain which may contain irrelevant and low quality data. CRAG ensures credible, relevant and peer reviewed documents are sent to the LLM. For example, a researcher asks “latest AI advancements” CRAG avoids receiving irrelevant older papers from the 1990s.
  4. ****Customer Facing Applications:**** In real time user services, even small retrieval errors can harm customer trust and satisfaction. CRAG ensures that only latest information is delivered to users. For example, when a customer support bot is asked “how to return a defective phone,__”__ CRAG provides the latest return and refund rules.


> It is useful when accuracy and reliability matter more than speed because even small retrieval errors can misleading. 
## CRAG vs RAG
Comparison table of RAG vs CRAG (Corrective RAG):  
| Feature  | RAG (Retrieval-Augmented Generation)  | CRAG (Corrective Retrieval-Augmented Generation)  |  
| --- | --- | --- |  
| Core Idea  | Retrieve documents then generate using them as context  | Adds an evaluation and correction step before using retrieved documents  |  
| Handling Bad Retrieval  | No built-in self-check, relies on quality of retrieval  | Uses a retrieval evaluator to detect low quality docs and correct them  |  
| Correction Mechanism  | None  | Triggers corrective actions: filtering, re-retrieval, decomposition  |  
| Use of Web Search  | May use external sources but not inherently corrective  | Integrates large scale web search if retrieval fails or is ambiguous  |  
| Robustness to Hallucination  | Some risk of hallucination if retrieval is poor  | Some risk of hallucination if retrieval is poor  |  
## Advantages of CRAG
Some advantages of CRAG are as follows: 
  1. ****Improved Accuracy:**** It filters irrelevant or misleading information by incorporating self correction and evaluation steps. 
  2. ****High Reliability:**** It can assess retrieved data****,**** produce trustworthy answers when handling complex queries or dynamic information.
  3. ****Reduces Hallucinations:**** It validates retrievals, reducing the risk of inaccurate or misleading outputs passing through LLM.
  4. ****Domain Adaptability:**** It****c**** an be fine tuned for specialized fields like healthcare, education or finance for maximum precision.
  5. ****Multi Step Reasoning:**** It cleans input first making it easier for the LLM to form logical steps without confusion, hence model receives only the most relevant information.
  6. ****Optimized Question-Answer Mapping:**** It ensures retrieved documents are not just textually similar but relevant to the user’s intent.
  7. ****Explainability:**** It is easier to justify why certain documents were included or excluded because of the corrective step (filtering, reranking or validation).


## Challenges of CRAG
Some main challenges of CRAG (Corrective Retrieval-Augmented Generation) are:
  * ****Complex Architecture:**** The corrective step makes the system harder to build and maintain.
  * ****Scalability Issues:**** Large knowledge bases need more time and computing power.
  * ****Domain Dependence:**** A correction method may fail in specialized fields like law or medicine.
  * ****High Latency:**** Filtering and reranking slow down response time.
  * ****Over-Filtering:**** Important data may get removed during correction.
  * ****Bias Risk:**** Retrieved external data may contain misinformation.


Comment
[S](https://www.geeksforgeeks.org/user/subhasreeoee6/)
[subhasreeoee6](https://www.geeksforgeeks.org/user/subhasreeoee6/)
0
Article Tags:
Article Tags:
[Artificial Intelligence](https://www.geeksforgeeks.org/category/ai-ml-ds/artificial-intelligence/)
[Large Language Model(LLM)](https://www.geeksforgeeks.org/tag/large-language-modelllm/)
### Explore
Introduction to AI
    * [What is Artificial Intelligence (AI)4 min read](https://www.geeksforgeeks.org/artificial-intelligence/what-is-artificial-intelligence-ai/)
    * [Types of Artificial Intelligence (AI)4 min read](https://www.geeksforgeeks.org/artificial-intelligence/types-of-artificial-intelligence/)
    * [Types of AI Based on Functionalities3 min read](https://www.geeksforgeeks.org/artificial-intelligence/types-of-ai-based-on-functionalities/)
    * [Agents in AI7 min read](https://www.geeksforgeeks.org/artificial-intelligence/agents-artificial-intelligence/)
    * [Artificial intelligence vs Machine Learning vs Deep Learning3 min read](https://www.geeksforgeeks.org/artificial-intelligence/artificial-intelligence-vs-machine-learning-vs-deep-learning/)
    * [Problem Solving in Artificial Intelligence4 min read](https://www.geeksforgeeks.org/artificial-intelligence/problem-solving-in-artificial-intelligence/)
    * [Top 20 Applications of Artificial Intelligence (AI) in 202513 min read](https://www.geeksforgeeks.org/blogs/applications-of-ai/)
AI Concepts
    * [Search Algorithms in AI6 min read](https://www.geeksforgeeks.org/machine-learning/search-algorithms-in-ai/)
    * [Local Search Algorithm in Artificial Intelligence6 min read](https://www.geeksforgeeks.org/artificial-intelligence/local-search-algorithm-in-artificial-intelligence/)
    * [Adversarial Search Algorithms in Artificial Intelligence (AI)15+ min read](https://www.geeksforgeeks.org/artificial-intelligence/adversarial-search-algorithms/)
    * [Constraint Satisfaction Problems (CSP) in Artificial Intelligence10 min read](https://www.geeksforgeeks.org/artificial-intelligence/constraint-satisfaction-problems-csp-in-artificial-intelligence/)
    * [Knowledge Representation in AI4 min read](https://www.geeksforgeeks.org/artificial-intelligence/knowledge-representation-in-ai/)
    * [First-Order Logic in Artificial Intelligence3 min read](https://www.geeksforgeeks.org/artificial-intelligence/first-order-logic-in-artificial-intelligence/)
    * [Reasoning Mechanisms in AI5 min read](https://www.geeksforgeeks.org/artificial-intelligence/reasoning-mechanisms-in-ai/)
Machine Learning in AI
    * [Machine Learning Tutorial5 min read](https://www.geeksforgeeks.org/machine-learning/machine-learning/)
    * [Deep Learning Tutorial2 min read](https://www.geeksforgeeks.org/deep-learning/deep-learning-tutorial/)
    * [Natural Language Processing (NLP) Tutorial2 min read](https://www.geeksforgeeks.org/nlp/natural-language-processing-nlp-tutorial/)
    * [Computer Vision Tutorial3 min read](https://www.geeksforgeeks.org/computer-vision/computer-vision/)
Robotics and AI
    * [Artificial Intelligence in Robotics5 min read](https://www.geeksforgeeks.org/artificial-intelligence/artificial-intelligence-in-robotics/)
    * [What is Robotics Process Automation8 min read](https://www.geeksforgeeks.org/blogs/robotics-process-automation-an-introduction/)
    * [Automated Planning in AI8 min read](https://www.geeksforgeeks.org/artificial-intelligence/automated-planning-in-ai/)
    * [AI in Transportation8 min read](https://www.geeksforgeeks.org/artificial-intelligence/ai-in-transportation/)
    * [AI in Manufacturing : Revolutionizing the Industry6 min read](https://www.geeksforgeeks.org/artificial-intelligence/ai-in-manufacturing-revolutionizing-the-industry/)
Generative AI
    * [What is Generative AI6 min read](https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/)
    * [Generative Adversarial Network (GAN)10 min read](https://www.geeksforgeeks.org/deep-learning/generative-adversarial-network-gan/)
    * [Cycle Generative Adversarial Network (CycleGAN)5 min read](https://www.geeksforgeeks.org/machine-learning/cycle-generative-adversarial-network-cyclegan-2/)
    * [StyleGAN - Style Generative Adversarial Networks4 min read](https://www.geeksforgeeks.org/machine-learning/stylegan-style-generative-adversarial-networks/)
    * [Introduction to Generative Pre-trained Transformer (GPT)3 min read](https://www.geeksforgeeks.org/artificial-intelligence/introduction-to-generative-pre-trained-transformer-gpt/)
    * [BERT Model - NLP6 min read](https://www.geeksforgeeks.org/nlp/explanation-of-bert-model-nlp/)
    * [Generative AI Applications 7 min read](https://www.geeksforgeeks.org/artificial-intelligence/generative-ai-applications/)
AI Practice
    * [Top Artificial Intelligence(AI) Interview Questions and Answers15+ min read](https://www.geeksforgeeks.org/artificial-intelligence/artificial-intelligenceai-interview-questions-and-answers/)
    * [Top Generative AI and LLM Interview Question with Answer15+ min read](https://www.geeksforgeeks.org/artificial-intelligence/generative-ai-interview-question-with-answer/)
    * [30+ Best Artificial Intelligence Project Ideas with Source Code [2026 Updated]15+ min read](https://www.geeksforgeeks.org/artificial-intelligence/best-artificial-intelligence-project-ideas/)
Courses
    * [Generative AI Course2 min read](https://www.geeksforgeeks.org/courses/generative-ai-training-program)
    * [Data Science and ML Course2 min read](https://www.geeksforgeeks.org/courses/data-science-live)
    * [Data Analytics Course2 min read](https://www.geeksforgeeks.org/courses/data-analytics-training-program-excel-sql-python-powerbi)


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
![](https://www.geeksforgeeks.org/artificial-intelligence/corrective-retrieval-augmented-generation-crag/)

