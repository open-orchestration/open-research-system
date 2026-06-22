# DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents
[Mingxuan Du](https://deepresearch-bench.github.io/)1, [Benfeng Xu](https://deepresearch-bench.github.io/)1,2, [Chiwei Zhu](https://deepresearch-bench.github.io/)1,  [Xiaorui Wang](https://deepresearch-bench.github.io/)2,  [Zhendong Mao](https://deepresearch-bench.github.io/)1
1University of Science and Technology of China, 2Metastone Technology, Beijing, China
[ Paper ](https://deepresearch-bench.github.io/static/papers/deepresearch-bench.pdf) [ arXiv ](https://arxiv.org/abs/2506.11763) [ Leaderboard ](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard) [ Code ](https://github.com/Ayanami0730/deep_research_bench) [ Data ](https://deepresearch-bench.github.io/)
![DeepResearch Bench Performance Overview](https://deepresearch-bench.github.io/static/images/experiment_comparison.png)
##  DeepResearch Bench provides a comprehensive evaluation framework for Deep Research Agents across 22 distinct research fields. 
## Abstract
**Deep Research Agents (DRAs)** currently represent one of the most widely used categories of LLM-based agents. By autonomously orchestrating multistep web exploration, targeted retrieval, and higher-order synthesis, they transform vast amounts of online information into analyst-grade, citation-rich reports--compressing hours of manual desk research into minutes. 
However, a comprehensive benchmark for systematically evaluating the capabilities of these agents remains absent. To bridge this gap, we present **DeepResearch Bench** , a benchmark consisting of 100 **PhD-level** research tasks, each meticulously crafted by domain experts across 22 distinct fields. 
Since evaluating the multifaceted capabilities of DRAs is a complex and labor intensive endeavor, we propose two novel evaluation methodologies designed to achieve strong alignment with human judgment. One is **a reference-based method with adaptive criteria** to assess the quality of generated research reports. The other framework is introduced to evaluate an agent's information retrieval and collection capabilities by assessing its effective citation count and overall citation accuracy. 
We are open-sourcing DeepResearch Bench and key components of these frameworks to accelerate the development of practical LLM-based agents. 
## Overview of Benchmark Construction
To comprehensively evaluate Deep Research Agents, we invited 100+ domain experts to create challenging research tasks that reflect real-world demands. This resulted in DeepResearch Bench, a benchmark consisting of 100 PhD-level research tasks--50 in Chinese and 50 in English--spanning 22 distinct fields. 
We designed two complementary evaluation frameworks to assess different aspects of DRA capabilities: **RACE** (Reference-based Adaptive Criteria-driven Evaluation framework with Dynamic Weighting) for evaluating the quality of generated research reports, and **FACT** (Framework for Factual Abundance and Citation Trustworthiness) for assessing information retrieval effectiveness and citation accuracy. These frameworks work together to provide a comprehensive evaluation of deep research agents' performance. 
![DeepResearch Bench Framework Overview](https://deepresearch-bench.github.io/static/images/framework.png)
## Topic Distribution Analysis
To ensure our benchmark reflects real-world research needs, we analyzed 96,147 raw user queries from interactions with web search-enabled LLM Chatbot. After filtering for queries that require deep research capabilities--involving multiple rounds of web searches, information gathering, and synthesis--we identified 44,019 relevant queries. We then employed DeepSeek-V3-0324 to classify these queries into 22 distinct topic domains. 
The resulting distribution reveals that Science & Technology and Business & Finance represent the highest proportions of deep research queries. This distribution directly guided our benchmark construction, ensuring that the 100 tasks in DeepResearch Bench maintain the same topical balance as observed in real-world usage patterns. 
![Topic Distribution](https://deepresearch-bench.github.io/static/images/query_distribution.png)
## Professional Research Tasks
Each task in DeepResearch Bench was meticulously crafted by domain experts--PhD holders or senior practitioners with over five years of relevant experience. These tasks are designed to test the upper limits of DRAs' capabilities, requiring sophisticated multi-step reasoning, comprehensive information synthesis, and nuanced domain understanding. 
The tasks span diverse research scenarios, from technical analysis in emerging technologies to comprehensive market research and scientific literature reviews, ensuring a thorough evaluation of agents' versatility across different research contexts. 
![Example Tasks from DeepResearch Bench](https://deepresearch-bench.github.io/static/images/showcase.png)
## Main Results
We comprehensively evaluated four early-released Deep Research Agents alongside several leading LLMs with built-in web search capabilities. The evaluation employed both RACE and FACT frameworks to assess different aspects of agent performance.   
Table 1: Overall evaluation results of DeepResearch Bench. Bold denotes the highest score in each column for Deep Research Agents (and for LLM with Search Tools within their respective section). Underlined denotes the second highest.   
| Model  | RACE  | FACT  |  
| --- | --- | --- |  
| Overall  | Comp.  | Depth  | Inst.  | Read.  | C. Acc.  | E. Cit.  |  
| LLM with Search Tools  |  
| Claude-3.7-Sonnet w/Search  | **40.67**  | **38.99**  | **37.66**  | **45.77**  | 41.46  | _93.68_  | _32.48_  |  
| Claude-3.5-Sonnet w/Search  | 28.48  | 24.82  | 22.82  | 35.12  | 35.08  | **94.04**  | 9.78  |  
| Perplexity-Sonar-Reasoning-Pro(high)  | _40.22_  | _37.38_  | 36.11  | _45.66_  | **44.74**  | 39.36  | 8.35  |  
| Perplexity-Sonar-Reasoning(high)  | 40.18  | 37.14  | _36.73_  | 45.15  | _44.35_  | 48.67  | 11.34  |  
| Perplexity-Sonar-Pro(high)  | 38.93  | 36.38  | 34.26  | 44.70  | 43.35  | 78.66  | 14.74  |  
| Perplexity-Sonar(high)  | 34.54  | 30.95  | 27.51  | 42.33  | 41.60  | 74.42  | 8.67  |  
| Gemini-2.5-Pro-Grounding  | 35.12  | 34.06  | 29.79  | 41.67  | 37.16  | 81.81  | **32.88**  |  
| Gemini-2.5-Flash-Grounding  | 32.39  | 31.63  | 26.73  | 38.82  | 34.48  | 81.92  | 31.08  |  
| GPT-4o-Search-Preview(high)  | 35.10  | 31.99  | 27.57  | 43.17  | 41.23  | 88.41  | 4.79  |  
| GPT-4o-Mini-Search-Preview(high)  | 31.55  | 27.38  | 22.64  | 40.67  | 39.91  | 84.98  | 4.95  |  
| GPT-4.1 w/Search(high)  | 33.46  | 29.42  | 25.38  | 42.33  | 40.77  | 87.83  | 4.42  |  
| GPT-4.1-mini w/Search(high)  | 30.26  | 26.05  | 20.75  | 39.65  | 39.33  | 84.58  | 4.35  |  
| Deep Research Agent  |  
| Grok Deeper Search  | 40.24  | 37.97  | 35.37  | 46.30  | 44.05  | _83.59_  | 8.15  |  
| Perplexity Deep Research  | 42.25  | 40.69  | 39.39  | 46.40  | 44.28  | **90.24**  | 31.26  |  
| Gemini-2.5-Pro Deep Research  | **48.88**  | **48.53**  | **48.50**  | _49.18_  | **49.44**  | 81.44  | **111.21**  |  
| OpenAI Deep Research  | _46.98_  | _46.87_  | _45.25_  | **49.27**  | _47.14_  | 77.96  | _40.79_  |  
**RACE Framework Results:** Gemini-2.5-Pro Deep Research demonstrated leading overall performance (48.88) across all dimensions, with OpenAI Deep Research following closely (46.98). Notably, different models excelled in different dimensions--OpenAI Deep Research achieved the highest score in Instruction-Following (49.27), indicating that evaluation dimensions capture distinct capabilities. 
**FACT Framework Results:** Deep Research Agents significantly outperformed LLMs with Search Tools in terms of Effective Citations. Gemini-2.5-Pro Deep Research achieved an exceptional 111.21 average effective citations, demonstrating superior information gathering capabilities. However, Perplexity Deep Research showed the highest Citation Accuracy (90.24%), indicating stronger precision in source attribution. 
## Human Consistency
### Human Data Collection
We recruited 70+ annotators with Master's degrees and relevant domain expertise to gather human judgments. Using a custom interface, they evaluated reports across four dimensions and overall performance, guided only by basic scoring criteria to minimize bias. Each annotator was limited to three queries maximum to ensure diverse perspectives. For each of the 50 Chinese tasks from DeepResearch Bench, three domain-expert annotators independently scored reports generated by four distinct agents. 
### Evaluation Metrics
We designed four metrics to quantify different aspects of alignment between evaluation methods and human judgment:**i.Pairwise Agreement Rate (PAR)** measures how often our evaluation method's preferences match human experts' preferences when comparing pairs of reports.**ii.Overall Pearson Correlation (OPC)** quantifies the linear relationship between average model scores from our evaluation method and those from human experts.**iii.Filtered Average Pearson (FAP)** & **iv.Spearman Correlation (FAS)** provide more robust assessment by filtering out tasks with low expert agreement. 
### Comparison of Different Evaluation Methods
Given that existing evaluation methods are generally unsuitable for assessing deep research reports, we compared the human consistency of several RACE variants against a vanilla prompt baseline. The complete RACE framework achieved an overall score of 72.56%, significantly outperforming the vanilla baseline. Ablation studies revealed that removing the reference-based comparison caused the most significant performance drop, confirming that relative scoring against high-quality references is crucial for discriminative evaluation.   
Table 2: Comparison of human consistency scores across different evaluation methods. Prefixed with '-', indicating removal of specific components from the full framework. The best scores for each metric among automated methods are in bold.   
| Evaluation Method  | PAR  | OPC  | FAP  | FAS  | Overall Score  |  
| --- | --- | --- | --- | --- | --- |  
| Vanilla Prompt  | 58.89  | 98.89  | 40.30  | 43.75  | 60.46  |  
| **RACE(Full)**  | **71.33**  | 99.54  | **60.24**  | **59.12**  | **72.56**  |  
| - No Criteria Weights  | 70.67  | 99.62  | 59.83  | 56.27  | 71.60  |  
| - No Dim Weights  | 70.89  | 99.54  | 60.11  | 57.22  | 71.94  |  
| - No Weights  | 71.11  | **99.69**  | 59.46  | 58.17  | 72.11  |  
| - No Reference  | 66.56  | 97.46  | 57.51  | 51.23  | 68.19  |  
| Reverse Position  | 69.56  | 97.20  | 56.75  | 55.49  | 69.75  |  
| Static Criteria  | 68.33  | 98.73  | 57.86  | 57.70  | 70.65  |  
| Human Inter-Agreement  | 68.44  | -  | -  | -  | -  |  
### Comparison of Different Judge LLMs
We evaluated several leading proprietary LLMs as Judge LLMs within the RACE framework to balance performance and cost considerations.   
Table 3: Comparison of human consistency scores and average cost using different Judge LLMs within the RACE(Full) framework. The best for each metric are highlighted in bold.   
| Judge LLM  | PAR  | OPC  | FAP  | FAS  | Overall  | Avg. Cost ($)  |  
| --- | --- | --- | --- | --- | --- | --- |  
| Gemini 2.5 Pro Preview  | **71.33**  | **99.54**  | **60.24**  | 59.12  | **72.56**  | 0.13  |  
| o3  | 68.11  | 96.22  | 57.64  | 52.36  | 68.58  | 0.37  |  
| o4-mini  | 70.89  | 97.06  | 59.54  | 59.02  | 71.63  | **0.04**  |  
| Claude 3.7 Sonnet  | 70.78  | 96.53  | 58.22  | **63.61**  | 72.28  | 0.47  |  
Gemini 2.5 Pro Preview achieved the best overall performance score of 72.56% while maintaining a competitive average cost of $0.13 per query. Based on this comprehensive evaluation balancing performance and cost efficiency, we selected Gemini 2.5 Pro Preview as the Judge LLM in our final framework. 
## BibTeX

```
@article{du2025deepresearch,
  author    = {Mingxuan Du and Benfeng Xu and Chiwei Zhu and Xiaorui Wang and Zhendong Mao},
  title     = {DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents},
  journal   = {arXiv preprint},
  year      = {2025},
}
```

[ ](https://deepresearch-bench.github.io/) [ ](https://deepresearch-bench.github.io/)
This website is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). 
This website template is based on the [Nerfies project page](https://github.com/nerfies/nerfies.github.io). Please remember to remove the analytics code included in the header of the website. 

