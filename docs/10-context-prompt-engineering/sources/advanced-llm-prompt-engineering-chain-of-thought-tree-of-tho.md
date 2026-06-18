# Advanced LLM Prompt Engineering: Chain-of-Thought, Tree-of-Thought ...

Source: https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en

[Skip to content](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#main-content)[ChaosAndOrder](https://www.youngju.dev/)
[Blog](https://www.youngju.dev/blog)[Tags](https://www.youngju.dev/tags)[Projects](https://www.youngju.dev/projects)[Tools](https://www.youngju.dev/tools)[Explore](https://www.youngju.dev/explore)[About](https://www.youngju.dev/about)
  1. [Home](https://www.youngju.dev/)
  2. /
  3. [Blog](https://www.youngju.dev/blog)
  4. /
  5. blog
  6. /
  7. Advanced LLM Prompt Engineering: Chain-of-Thought, Tree-of-Thought, ReAct, and Few-Shot Pattern Practical Guide

Published on
    2026년 3월 12일 목요일
# Advanced LLM Prompt Engineering: Chain-of-Thought, Tree-of-Thought, ReAct, and Few-Shot Pattern Practical Guide
[🇰🇷KO한국어](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced "한국어")🇺🇸ENEnglish[🇯🇵JA日本語](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.ja "日本語")
[Split View](https://www.youngju.dev/split/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced)[필사 모드](https://www.youngju.dev/transcribe/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en)[✨Start Quiz](https://www.youngju.dev/quiz/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced) 

Authors
    
  * ![avatar](https://www.youngju.dev/static/images/avatar.jpg) 

Name
    Youngju Kim 

Twitter
    [@fjvbn20031](https://twitter.com/fjvbn20031)


  * [Introduction](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#introduction)
  * [Prompting Technique Taxonomy](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompting-technique-taxonomy)
  * [Zero-shot and Few-shot Prompting](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#zero-shot-and-few-shot-prompting)
    * [Zero-shot Prompting](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#zero-shot-prompting)
    * [Few-shot Prompting](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#few-shot-prompting)
  * [Chain-of-Thought (CoT) Prompting](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#chain-of-thought-cot-prompting)
    * [Core Principle](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#core-principle)
    * [Zero-shot CoT](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#zero-shot-cot)
  * [Self-Consistency Decoding](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#self-consistency-decoding)
  * [Tree-of-Thought (ToT) Framework](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#tree-of-thought-tot-framework)
    * [Core Idea](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#core-idea)
  * [ReAct: Synergizing Reasoning and Acting](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#react-synergizing-reasoning-and-acting)
    * [Core Principle](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#core-principle-1)
  * [Structured Output Prompting](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#structured-output-prompting)
  * [Prompt Chaining](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompt-chaining)
  * [Prompting Technique Performance Comparison](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompting-technique-performance-comparison)
    * [Benchmark Results](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#benchmark-results)
    * [Technique Selection Guide](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#technique-selection-guide)
  * [Common Anti-patterns](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#common-anti-patterns)
    * [Anti-pattern 1: Excessive Instructions](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#anti-pattern-1-excessive-instructions)
    * [Anti-pattern 2: Ambiguous Output Format](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#anti-pattern-2-ambiguous-output-format)
    * [Anti-pattern 3: Context Window Waste](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#anti-pattern-3-context-window-waste)
  * [Production Optimization](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#production-optimization)
    * [Prompt Version Management](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompt-version-management)
    * [Cost Optimization Strategy](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#cost-optimization-strategy)
    * [Caching Strategy](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#caching-strategy)
  * [Operational Considerations](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#operational-considerations)
    * [Prompt Injection Defense](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompt-injection-defense)
    * [Failure Cases and Recovery](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#failure-cases-and-recovery)
    * [Evaluation Pipeline](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#evaluation-pipeline)
  * [Conclusion](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#conclusion)
  * [References](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#references)


![LLM Prompt Engineering Advanced Techniques](https://www.youngju.dev/static/images/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.png)
##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#introduction)Introduction
Prompt engineering is a core technology for maximizing the latent capabilities of LLMs. The Chain-of-Thought paper published by Wei et al. in 2022 proved that "including reasoning processes in prompts dramatically improves the model's reasoning ability," establishing prompt engineering as an independent research field.
Subsequently, advanced techniques such as Self-Consistency, Tree-of-Thought, and ReAct emerged in succession, expanding the scope of LLM applications far beyond simple question-answer patterns to complex reasoning, planning, and external tool utilization. In particular, the ReAct pattern has become the core architecture of most AI agent frameworks (LangChain, AutoGen, etc.).
This article systematically covers the theoretical background, key paper findings, Python implementation code, performance comparisons, anti-patterns, and production optimization strategies for each prompting technique.
##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompting-technique-taxonomy)Prompting Technique Taxonomy
Prompting techniques can be classified as follows:  
| Category  | Technique  | Core Idea  | Paper  |  
| --- | --- | --- | --- |  
| Basic  | Zero-shot  | Perform with instructions only, no examples  | -  |  
| Basic  | Few-shot  | Provide a few examples  | Brown et al. 2020  |  
| Reasoning Enhancement  | Chain-of-Thought  | Generate intermediate reasoning steps  | Wei et al. 2022  |  
| Reasoning Enhancement  | Zero-shot CoT  | Add a single phrase: "Let's think step by step"  | Kojima et al. 2022  |  
| Ensemble  | Self-Consistency  | Multi-path sampling + majority voting  | Wang et al. 2022  |  
| Search  | Tree-of-Thought  | Tree-structured reasoning path exploration  | Yao et al. 2023  |  
| Agent  | ReAct  | Reasoning + Acting + Observation loop  | Yao et al. 2022  |  
| Structured  | Structured Output  | Enforce JSON/XML format output  | -  |  
| Composition  | Prompt Chaining  | Task decomposition + sequential execution  | -  |  
##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#zero-shot-and-few-shot-prompting)Zero-shot and Few-shot Prompting
###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#zero-shot-prompting)Zero-shot Prompting
The most basic approach where the model performs a task using only instructions without examples. With recent performance improvements in large models (GPT-4, Claude 3.5, etc.), many tasks can achieve sufficient performance with Zero-shot alone.

```
from openai import OpenAI

client = OpenAI()

def zero_shot_classification(text: str) -> str:
    """Zero-shot text classification"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a text classifier. "
                    "Classify the given text into one of the following categories: "
                    "Technology, Business, Science, Sports, Entertainment. "
                    "Respond with only the category name."
                )
            },
            {"role": "user", "content": text}
        ],
        temperature=0,
        max_tokens=20,
    )
    return response.choices[0].message.content.strip()

```

###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#few-shot-prompting)Few-shot Prompting
Few-shot prompting includes a small number of input-output examples in the prompt to help the model learn patterns. It was systematically presented in the GPT-3 paper by Brown et al. (2020) and is particularly effective for tasks requiring consistent output formats.

```
def few_shot_entity_extraction(text: str) -> str:
    """Few-shot named entity extraction"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Extract named entities from the given text in the specified format."
            },
            {
                "role": "user",
                "content": "Samsung Electronics announced the Galaxy S25 series at CES 2025 in Las Vegas."
            },
            {
                "role": "assistant",
                "content": (
                    "- Organization: Samsung Electronics\n"
                    "- Product: Galaxy S25\n"
                    "- Event: CES 2025\n"
                    "- Location: Las Vegas"
                )
            },
            {
                "role": "user",
                "content": "Elon Musk revealed that Tesla will open a new Gigafactory in Austin, Texas in March 2026."
            },
            {
                "role": "assistant",
                "content": (
                    "- Person: Elon Musk\n"
                    "- Organization: Tesla\n"
                    "- Facility: Gigafactory\n"
                    "- Location: Austin, Texas\n"
                    "- Date: March 2026"
                )
            },
            {"role": "user", "content": text}
        ],
        temperature=0,
    )
    return response.choices[0].message.content

# Few-shot example selection strategy
class FewShotSelector:
    """Dynamic few-shot example selector"""
    def __init__(self, examples, embedding_model="text-embedding-3-small"):
        self.examples = examples
        self.client = OpenAI()
        self.embedding_model = embedding_model
        self._precompute_embeddings()

    def _precompute_embeddings(self):
        """Precompute embeddings for all examples"""
        texts = [ex["input"] for ex in self.examples]
        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=texts
        )
        self.embeddings = [r.embedding for r in response.data]

    def select(self, query: str, k: int = 3) -> list:
        """Select k most similar examples to the query"""
        query_emb = self.client.embeddings.create(
            model=self.embedding_model,
            input=[query]
        ).data[0].embedding

        # Compute cosine similarity
        import numpy as np
        similarities = []
        for emb in self.embeddings:
            sim = np.dot(query_emb, emb) / (
                np.linalg.norm(query_emb) * np.linalg.norm(emb)
            )
            similarities.append(sim)

        # Select top k
        top_indices = np.argsort(similarities)[-k:][::-1]
        return [self.examples[i] for i in top_indices]

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#chain-of-thought-cot-prompting)Chain-of-Thought (CoT) Prompting
###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#core-principle)Core Principle
The Chain-of-Thought paper by Wei et al. (2022) demonstrated that including intermediate reasoning steps in prompts dramatically improves the complex reasoning ability of LLMs. Key findings include:
  * **540B parameter PaLM** model improved GSM8K (math problems) accuracy from 17.9% to **58.1%**
  * CoT is an **emergent ability** that manifests only when the model is sufficiently large (100B+)
  * Just 8 CoT examples surpassed GPT-3 (fine-tuned) + verifier performance



```
def chain_of_thought_math(problem: str) -> dict:
    """Chain-of-Thought math problem solving"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a math tutor. Solve problems step by step.\n"
                    "Show your reasoning clearly before giving the final answer.\n"
                    "Format: Step 1, Step 2, ..., Final Answer: [number]"
                )
            },
            {
                "role": "user",
                "content": (
                    "A store has 45 apples. They sell 1/3 of them in the morning "
                    "and 2/5 of the remaining in the afternoon. "
                    "How many apples are left?"
                )
            },
            {
                "role": "assistant",
                "content": (
                    "Step 1: Calculate apples sold in the morning.\n"
                    "Morning sales = 45 * (1/3) = 15 apples\n\n"
                    "Step 2: Calculate remaining apples after morning.\n"
                    "Remaining = 45 - 15 = 30 apples\n\n"
                    "Step 3: Calculate apples sold in the afternoon.\n"
                    "Afternoon sales = 30 * (2/5) = 12 apples\n\n"
                    "Step 4: Calculate final remaining apples.\n"
                    "Final remaining = 30 - 12 = 18 apples\n\n"
                    "Final Answer: 18"
                )
            },
            {"role": "user", "content": problem}
        ],
        temperature=0,
    )

    answer_text = response.choices[0].message.content
    # Extract final answer
    import re
    match = re.search(r"Final Answer:\s*(\d+)", answer_text)
    final_answer = int(match.group(1)) if match else None

    return {
        "reasoning": answer_text,
        "answer": final_answer,
        "tokens_used": response.usage.total_tokens,
    }

```

###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#zero-shot-cot)Zero-shot CoT
Kojima et al. (2022) discovered that simply adding the phrase **"Let's think step by step"** achieves CoT effects without requiring separate examples. This is extremely practical as it eliminates the need for crafting examples.

```
def zero_shot_cot(problem: str) -> str:
    """Zero-shot Chain-of-Thought"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": f"{problem}\n\nLet's think step by step."
            }
        ],
        temperature=0,
    )
    return response.choices[0].message.content

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#self-consistency-decoding)Self-Consistency Decoding
**Self-Consistency** by Wang et al. (2022) replaces CoT's single greedy decoding with sampling multiple reasoning paths and determining the final answer through majority voting. It achieved **+17.9%** accuracy improvement over CoT on GSM8K.

```
import collections
import re

def self_consistency(problem: str, num_samples: int = 5) -> dict:
    """Self-Consistency decoding"""
    answers = []
    reasoning_paths = []

    for i in range(num_samples):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Solve the math problem step by step. "
                        "End with 'Final Answer: [number]'"
                    )
                },
                {"role": "user", "content": problem}
            ],
            temperature=0.7,  # Higher temperature for diverse reasoning paths
            max_tokens=500,
        )

        text = response.choices[0].message.content
        reasoning_paths.append(text)

        # Extract answer
        match = re.search(r"Final Answer:\s*(\d+)", text)
        if match:
            answers.append(int(match.group(1)))

    # Majority voting
    if answers:
        counter = collections.Counter(answers)
        majority_answer = counter.most_common(1)[0][0]
        confidence = counter.most_common(1)[0][1] / len(answers)
    else:
        majority_answer = None
        confidence = 0.0

    return {
        "answer": majority_answer,
        "confidence": confidence,
        "all_answers": answers,
        "num_samples": num_samples,
        "answer_distribution": dict(counter) if answers else {},
    }

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#tree-of-thought-tot-framework)Tree-of-Thought (ToT) Framework
###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#core-idea)Core Idea
**Tree-of-Thought (ToT)** by Yao et al. (2023) extends CoT into a tree structure that simultaneously explores multiple reasoning paths. Key findings include:
  * **Game of 24 task** : GPT-4 + CoT achieved 4% success rate -> ToT achieved **74%**
  * Systematic exploration of reasoning paths using BFS/DFS strategies
  * The LLM itself evaluates each path, expanding only promising ones



```
from dataclasses import dataclass
from typing import Optional

@dataclass
class ThoughtNode:
    """ToT thought node"""
    content: str
    score: float = 0.0
    children: list = None
    parent: Optional['ThoughtNode'] = None
    depth: int = 0

    def __post_init__(self):
        if self.children is None:
            self.children = []

class TreeOfThought:
    """Tree-of-Thought Framework"""
    def __init__(self, model="gpt-4o", max_depth=3, branching_factor=3):
        self.client = OpenAI()
        self.model = model
        self.max_depth = max_depth
        self.branching_factor = branching_factor

    def generate_thoughts(self, problem: str, current_thought: str) -> list:
        """Generate possible next thoughts from current state"""
        prompt = (
            f"Problem: {problem}\n\n"
            f"Current reasoning so far:\n{current_thought}\n\n"
            f"Generate {self.branching_factor} different possible next steps "
            f"for solving this problem. "
            f"Format each as 'Step N: [reasoning]' separated by '---'"
        )
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )
        text = response.choices[0].message.content
        thoughts = [t.strip() for t in text.split("---") if t.strip()]
        return thoughts[:self.branching_factor]

    def evaluate_thought(self, problem: str, thought_path: str) -> float:
        """Evaluate the promise of a thought path on a 0-1 scale"""
        prompt = (
            f"Problem: {problem}\n\n"
            f"Reasoning path:\n{thought_path}\n\n"
            f"Evaluate this reasoning path on a scale of 0.0 to 1.0:\n"
            f"- 1.0: Correct and complete solution\n"
            f"- 0.7-0.9: On the right track, promising\n"
            f"- 0.4-0.6: Partially correct but uncertain\n"
            f"- 0.0-0.3: Wrong approach or contains errors\n\n"
            f"Respond with only the score (e.g., 0.8)"
        )
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=10,
        )
        try:
            score = float(response.choices[0].message.content.strip())
            return min(max(score, 0.0), 1.0)
        except ValueError:
            return 0.5

    def solve_bfs(self, problem: str) -> dict:
        """BFS-based ToT search"""
        root = ThoughtNode(content="", depth=0)
        current_level = [root]
        best_solution = None
        best_score = 0.0

        for depth in range(self.max_depth):
            next_level = []
            for node in current_level:
                # Generate child thoughts
                thought_path = self._get_path(node)
                children_thoughts = self.generate_thoughts(problem, thought_path)

                for thought in children_thoughts:
                    full_path = f"{thought_path}\n{thought}" if thought_path else thought
                    score = self.evaluate_thought(problem, full_path)

                    child = ThoughtNode(
                        content=thought,
                        score=score,
                        parent=node,
                        depth=depth + 1
                    )
                    node.children.append(child)
                    next_level.append(child)

                    if score > best_score:
                        best_score = score
                        best_solution = full_path

            # Keep only top branching_factor nodes (beam search)
            next_level.sort(key=lambda n: n.score, reverse=True)
            current_level = next_level[:self.branching_factor]

        return {
            "solution": best_solution,
            "score": best_score,
            "depth_explored": self.max_depth,
        }

    def _get_path(self, node: ThoughtNode) -> str:
        """Return the full thought path up to the node"""
        path = []
        current = node
        while current and current.content:
            path.append(current.content)
            current = current.parent
        return "\n".join(reversed(path))

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#react-synergizing-reasoning-and-acting)ReAct: Synergizing Reasoning and Acting
###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#core-principle-1)Core Principle
**ReAct** by Yao et al. (2022) is a framework where LLMs alternate between reasoning and acting to leverage external tools. Through the Thought-Action-Observation loop, it reduces hallucination and generates verifiable results.  
| Component  | Role  | Example  |  
| --- | --- | --- |  
| Thought  | Analyze current state and plan next action  | "The user asked for 2024 revenue, so I need to query the DB"  |  
| Action  | Call external tool  | search("2024 revenue report"), calculate("150 * 1.1")  |  
| Observation  | Observe tool execution result  | "2024 revenue confirmed at 15 billion"  |  

```
import json
from typing import Callable

class ReActAgent:
    """ReAct pattern-based agent"""

    def __init__(self, model="gpt-4o"):
        self.client = OpenAI()
        self.model = model
        self.tools = {}
        self.max_iterations = 10

    def register_tool(self, name: str, func: Callable, description: str):
        """Register external tool"""
        self.tools[name] = {
            "function": func,
            "description": description,
        }

    def _build_system_prompt(self) -> str:
        """Build system prompt"""
        tool_descriptions = "\n".join([
            f"- {name}: {info['description']}"
            for name, info in self.tools.items()
        ])

        return (
            "You are a helpful assistant that solves problems step by step.\n"
            "You have access to the following tools:\n"
            f"{tool_descriptions}\n\n"
            "For each step, respond in the following format:\n"
            "Thought: [your reasoning about what to do next]\n"
            "Action: [tool_name(argument)]\n\n"
            "After receiving an observation, continue with another Thought.\n"
            "When you have the final answer, respond with:\n"
            "Thought: [final reasoning]\n"
            "Final Answer: [your answer]\n\n"
            "IMPORTANT: Use exactly one Action per step. "
            "Wait for the Observation before proceeding."
        )

    def run(self, query: str) -> dict:
        """Execute ReAct loop"""
        messages = [
            {"role": "system", "content": self._build_system_prompt()},
            {"role": "user", "content": query},
        ]

        steps = []

        for iteration in range(self.max_iterations):
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=500,
            )
            assistant_msg = response.choices[0].message.content

            # Check for Final Answer
            if "Final Answer:" in assistant_msg:
                final_answer = assistant_msg.split("Final Answer:")[-1].strip()
                steps.append({
                    "type": "final",
                    "content": assistant_msg,
                })
                return {
                    "answer": final_answer,
                    "steps": steps,
                    "iterations": iteration + 1,
                }

            # Parse and execute Action
            import re
            action_match = re.search(r"Action:\s*(\w+)\((.+?)\)", assistant_msg)
            if action_match:
                tool_name = action_match.group(1)
                tool_arg = action_match.group(2).strip("'\"")

                steps.append({
                    "type": "thought_action",
                    "content": assistant_msg,
                    "tool": tool_name,
                    "argument": tool_arg,
                })

                # Execute tool
                if tool_name in self.tools:
                    try:
                        observation = self.tools[tool_name]["function"](tool_arg)
                    except Exception as e:
                        observation = f"Error: {str(e)}"
                else:
                    observation = f"Error: Tool '{tool_name}' not found"

                steps.append({
                    "type": "observation",
                    "content": str(observation),
                })

                # Add to message history
                messages.append({"role": "assistant", "content": assistant_msg})
                messages.append({
                    "role": "user",
                    "content": f"Observation: {observation}"
                })
            else:
                # If no Action, add to history and continue
                messages.append({"role": "assistant", "content": assistant_msg})
                messages.append({
                    "role": "user",
                    "content": "Please continue with an Action or provide the Final Answer."
                })

        return {
            "answer": "Max iterations reached",
            "steps": steps,
            "iterations": self.max_iterations,
        }

# Usage example
def create_research_agent():
    """Create a research agent"""
    agent = ReActAgent()

    # Register tools
    def search(query):
        # In practice, this would call a search API
        return f"Search results for '{query}': [simulated results]"

    def calculate(expression):
        return str(eval(expression))

    def get_current_date():
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")

    agent.register_tool("search", search, "Search the web for information")
    agent.register_tool("calculate", calculate, "Evaluate a math expression")
    agent.register_tool("get_date", lambda _: get_current_date(), "Get current date")

    return agent

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#structured-output-prompting)Structured Output Prompting
In production environments, LLM outputs must be received in structured formats (JSON, XML, etc.) that can be programmatically processed.

```
from pydantic import BaseModel, Field
from typing import Literal

# Structured output using Pydantic models
class SentimentResult(BaseModel):
    """Sentiment analysis result schema"""
    sentiment: Literal["positive", "negative", "neutral"]
    confidence: float = Field(ge=0.0, le=1.0)
    key_phrases: list[str]
    reasoning: str

def structured_sentiment_analysis(text: str) -> SentimentResult:
    """Perform sentiment analysis with structured output"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "Analyze the sentiment of the given text. "
                    "Respond in JSON format with the following fields:\n"
                    "- sentiment: 'positive', 'negative', or 'neutral'\n"
                    "- confidence: float between 0.0 and 1.0\n"
                    "- key_phrases: list of key phrases that influenced the sentiment\n"
                    "- reasoning: brief explanation of the analysis"
                )
            },
            {"role": "user", "content": text}
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )

    result = json.loads(response.choices[0].message.content)
    return SentimentResult(**result)

# Function Calling-based structuring
def function_calling_extraction(text: str) -> dict:
    """Information extraction using Function Calling"""
    tools = [
        {
            "type": "function",
            "function": {
                "name": "extract_meeting_info",
                "description": "Extract meeting information from text",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Meeting date in YYYY-MM-DD format"
                        },
                        "time": {
                            "type": "string",
                            "description": "Meeting time in HH:MM format"
                        },
                        "participants": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of participants"
                        },
                        "agenda": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Meeting agenda items"
                        },
                        "location": {
                            "type": "string",
                            "description": "Meeting location or meeting link"
                        }
                    },
                    "required": ["date", "time", "participants"]
                }
            }
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Extract meeting info: {text}"}],
        tools=tools,
        tool_choice={"type": "function", "function": {"name": "extract_meeting_info"}},
    )

    tool_call = response.choices[0].message.tool_calls[0]
    return json.loads(tool_call.function.arguments)

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompt-chaining)Prompt Chaining
A technique that decomposes complex tasks into multiple prompt stages and executes them sequentially. Each stage's output becomes the next stage's input.

```
class PromptChain:
    """Prompt Chaining Framework"""

    def __init__(self, model="gpt-4o"):
        self.client = OpenAI()
        self.model = model
        self.steps = []
        self.results = {}

    def add_step(self, name: str, prompt_template: str, depends_on: list = None):
        """Add a step to the chain"""
        self.steps.append({
            "name": name,
            "prompt_template": prompt_template,
            "depends_on": depends_on or [],
        })

    def run(self, initial_input: str) -> dict:
        """Execute the entire chain"""
        self.results["input"] = initial_input

        for step in self.steps:
            # Construct prompt with dependent step results
            prompt = step["prompt_template"]
            prompt = prompt.replace("INPUT", self.results.get("input", ""))
            for dep in step["depends_on"]:
                prompt = prompt.replace(
                    f"RESULT_{dep.upper()}",
                    self.results.get(dep, "")
                )

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
            )

            self.results[step["name"]] = response.choices[0].message.content

        return self.results

# Usage example: Technical document summarize + translate + keyword extraction
def create_document_pipeline():
    """Document processing pipeline"""
    chain = PromptChain()

    chain.add_step(
        name="summary",
        prompt_template=(
            "Summarize the following technical document in 3-5 bullet points:\n\n"
            "INPUT"
        )
    )

    chain.add_step(
        name="translation",
        prompt_template=(
            "Translate the following summary to Korean:\n\n"
            "RESULT_SUMMARY"
        ),
        depends_on=["summary"]
    )

    chain.add_step(
        name="keywords",
        prompt_template=(
            "Extract 5-10 technical keywords from the following summary. "
            "Format as a comma-separated list:\n\n"
            "RESULT_SUMMARY"
        ),
        depends_on=["summary"]
    )

    return chain

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompting-technique-performance-comparison)Prompting Technique Performance Comparison
###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#benchmark-results)Benchmark Results  
| Technique  | GSM8K (Math)  | HotpotQA (QA)  | Game of 24  | Token Cost  |  
| --- | --- | --- | --- | --- |  
| Zero-shot  | 17.9%  | 28.7%  | -  | 1x  |  
| Few-shot  | 33.0%  | 35.2%  | -  | 1.5x  |  
| Zero-shot CoT  | 40.7%  | 33.8%  | -  | 1.5x  |  
| Few-shot CoT  | 58.1%  | 42.1%  | 4%  | 2x  |  
| Self-Consistency (k=40)  | 76.0%  | 47.3%  | -  | 40x  |  
| Tree-of-Thought  | -  | -  | 74%  | 10-50x  |  
| ReAct  | -  | 40.2%  | -  | 3-5x  |  
###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#technique-selection-guide)Technique Selection Guide

```
# Prompting technique selection decision tree
decision_tree:
  simple_classification:
    recommended: 'Zero-shot or Few-shot'
    reason: 'Simple classification does not require advanced techniques'

  math_reasoning:
    recommended: 'CoT + Self-Consistency'
    reason: 'Most stable performance for mathematical reasoning'

  multi_step_search:
    recommended: 'ReAct'
    reason: 'Tool utilization possible when external information is needed'

  creative_problem_solving:
    recommended: 'Tree-of-Thought'
    reason: 'Suitable for creative problems with large search spaces'

  production_api:
    recommended: 'Few-shot + Structured Output'
    reason: 'Consistency and parsability are paramount'

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#common-anti-patterns)Common Anti-patterns
###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#anti-pattern-1-excessive-instructions)Anti-pattern 1: Excessive Instructions

```
# BAD: Too many instructions confuse the model
bad_prompt = """
You are an expert data scientist with 20 years of experience.
You must always be accurate and never hallucinate.
You should think carefully before answering.
Make sure your answer is complete and comprehensive.
Consider all edge cases and potential issues.
Be concise but thorough.
Use technical language but also be accessible.
Format your response nicely.
Include examples when appropriate.
Double-check your work before responding.

Question: What is the capital of France?
"""

# GOOD: Concise and specific instructions
good_prompt = """
Answer the following geography question with just the city name.
Question: What is the capital of France?
"""

```

###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#anti-pattern-2-ambiguous-output-format)Anti-pattern 2: Ambiguous Output Format

```
# BAD: Output format is unclear
bad_format = "Analyze this data and give me insights."

# GOOD: Clear output format specification
good_format = """
Analyze the following sales data and provide:
1. Top 3 insights (one sentence each)
2. Trend direction: "increasing", "decreasing", or "stable"
3. Recommended actions (bulleted list, max 3 items)

Respond in JSON format with keys: insights, trend, actions.
"""

```

###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#anti-pattern-3-context-window-waste)Anti-pattern 3: Context Window Waste

```
# BAD: Repeating the same long system prompt for each request
def bad_batch_processing(items):
    """Repeats identical long system prompt for every request"""
    results = []
    for item in items:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": VERY_LONG_SYSTEM_PROMPT},
                {"role": "user", "content": item},
            ]
        )
        results.append(response.choices[0].message.content)
    return results

# GOOD: Optimize with batch processing
def good_batch_processing(items):
    """Process multiple items at once"""
    combined = "\n---\n".join([f"Item {i+1}: {item}" for i, item in enumerate(items)])
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "Process each item below and return results "
                    "in JSON array format."
                )
            },
            {"role": "user", "content": combined},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#production-optimization)Production Optimization
###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompt-version-management)Prompt Version Management

```
import hashlib
from datetime import datetime

class PromptRegistry:
    """Prompt version management system"""

    def __init__(self):
        self.prompts = {}
        self.history = []

    def register(self, name: str, template: str, version: str = None) -> str:
        """Register and version manage prompts"""
        content_hash = hashlib.md5(template.encode()).hexdigest()[:8]
        version = version or f"v{len(self.history) + 1}_{content_hash}"

        entry = {
            "name": name,
            "version": version,
            "template": template,
            "hash": content_hash,
            "created_at": datetime.now().isoformat(),
        }

        self.prompts[name] = entry
        self.history.append(entry)
        return version

    def get(self, name: str) -> str:
        """Return the currently active prompt"""
        if name not in self.prompts:
            raise KeyError(f"Prompt '{name}' not registered")
        return self.prompts[name]["template"]

    def get_version(self, name: str) -> str:
        """Return current prompt version"""
        return self.prompts[name]["version"]

```

###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#cost-optimization-strategy)Cost Optimization Strategy

```
class CostOptimizer:
    """LLM API cost optimization"""

    # Per-model pricing (per 1M tokens, approximate as of March 2026)
    PRICING = {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
        "claude-3-5-sonnet": {"input": 3.00, "output": 15.00},
        "claude-3-5-haiku": {"input": 0.80, "output": 4.00},
    }

    @staticmethod
    def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
        """Estimate cost"""
        pricing = CostOptimizer.PRICING.get(model, {})
        input_cost = (input_tokens / 1_000_000) * pricing.get("input", 0)
        output_cost = (output_tokens / 1_000_000) * pricing.get("output", 0)
        return input_cost + output_cost

    @staticmethod
    def select_model(task_complexity: str) -> str:
        """Select model based on task complexity"""
        model_map = {
            "simple": "gpt-4o-mini",       # Classification, extraction, etc.
            "moderate": "gpt-4o-mini",      # Tasks requiring CoT
            "complex": "gpt-4o",            # Complex reasoning, code generation
            "critical": "gpt-4o",           # Tasks where accuracy is top priority
        }
        return model_map.get(task_complexity, "gpt-4o-mini")

```

###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#caching-strategy)Caching Strategy

```
import hashlib
import json
from functools import lru_cache

class PromptCache:
    """Prompt response caching"""

    def __init__(self, cache_backend="memory"):
        self.cache = {}
        self.hits = 0
        self.misses = 0

    def _make_key(self, model: str, messages: list, temperature: float) -> str:
        """Generate cache key"""
        content = json.dumps({
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()

    def get(self, model: str, messages: list, temperature: float):
        """Look up response in cache"""
        if temperature > 0:
            # Do not cache non-deterministic responses
            return None

        key = self._make_key(model, messages, temperature)
        result = self.cache.get(key)
        if result:
            self.hits += 1
        else:
            self.misses += 1
        return result

    def set(self, model: str, messages: list, temperature: float, response: str):
        """Store response in cache"""
        if temperature > 0:
            return
        key = self._make_key(model, messages, temperature)
        self.cache[key] = response

    def stats(self) -> dict:
        """Cache statistics"""
        total = self.hits + self.misses
        return {
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": self.hits / total if total > 0 else 0,
            "cache_size": len(self.cache),
        }

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#operational-considerations)Operational Considerations
###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#prompt-injection-defense)Prompt Injection Defense
The most important security issue in production environments is prompt injection. User input can bypass system prompts to induce unintended behavior.

```
def sanitize_user_input(user_input: str) -> str:
    """Sanitize user input"""
    # 1. Detect system prompt bypass attempts
    injection_patterns = [
        "ignore previous instructions",
        "ignore all instructions",
        "disregard the above",
        "forget your instructions",
        "you are now",
        "new instruction:",
        "system prompt:",
    ]

    lower_input = user_input.lower()
    for pattern in injection_patterns:
        if pattern in lower_input:
            return "[BLOCKED: Potential prompt injection detected]"

    # 2. Limit input length
    max_length = 4000
    if len(user_input) > max_length:
        user_input = user_input[:max_length] + "... [truncated]"

    return user_input

```

###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#failure-cases-and-recovery)Failure Cases and Recovery

```
# Common failure scenarios
failure_scenarios:
  rate_limiting:
    symptom: '429 Too Many Requests'
    cause: 'API call limit exceeded'
    recovery:
      - 'Apply exponential backoff'
      - 'Implement request queue for traffic smoothing'
      - 'Rotate multiple API keys'

  hallucination:
    symptom: 'Model generates non-existent information'
    cause: 'Insufficient context or excessive temperature'
    recovery:
      - 'Lower temperature to 0'
      - 'Provide grounding material via RAG pipeline'
      - 'Add output verification layer'

  format_failure:
    symptom: 'JSON parsing failure'
    cause: 'Model does not follow requested format'
    recovery:
      - 'Use response_format parameter'
      - 'Enforce format with Few-shot examples'
      - 'Retry on failure with clearer instructions'

  context_overflow:
    symptom: 'Context window exceeded error'
    cause: 'Input tokens exceed model limit'
    recovery:
      - 'Summarize or chunk input text'
      - 'Remove unnecessary Few-shot examples'
      - 'Switch to a model with longer context'

```

###  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#evaluation-pipeline)Evaluation Pipeline

```
class PromptEvaluator:
    """Prompt A/B test evaluator"""

    def __init__(self):
        self.results = []

    def evaluate(self, test_cases: list, prompt_a: str, prompt_b: str) -> dict:
        """Comparative evaluation of two prompts"""
        scores_a = []
        scores_b = []

        for case in test_cases:
            # Execute Prompt A
            result_a = self._run_prompt(prompt_a, case["input"])
            score_a = self._score(result_a, case["expected"])
            scores_a.append(score_a)

            # Execute Prompt B
            result_b = self._run_prompt(prompt_b, case["input"])
            score_b = self._score(result_b, case["expected"])
            scores_b.append(score_b)

        import numpy as np
        return {
            "prompt_a_avg": np.mean(scores_a),
            "prompt_b_avg": np.mean(scores_b),
            "prompt_a_std": np.std(scores_a),
            "prompt_b_std": np.std(scores_b),
            "winner": "A" if np.mean(scores_a) > np.mean(scores_b) else "B",
            "improvement": abs(np.mean(scores_a) - np.mean(scores_b)),
            "num_cases": len(test_cases),
        }

    def _run_prompt(self, prompt: str, input_text: str) -> str:
        """Execute prompt"""
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": input_text},
            ],
            temperature=0,
        )
        return response.choices[0].message.content

    def _score(self, result: str, expected: str) -> float:
        """Score result (0-1)"""
        # Simple string similarity-based scoring
        result_lower = result.lower().strip()
        expected_lower = expected.lower().strip()

        if result_lower == expected_lower:
            return 1.0
        elif expected_lower in result_lower:
            return 0.8
        else:
            return 0.0

```

##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#conclusion)Conclusion
Prompt engineering has evolved from simple text crafting into an engineering discipline that understands and leverages the reasoning mechanisms of LLMs. Starting from Chain-of-Thought's simple idea of "show me the reasoning steps," it has expanded to Self-Consistency's ensemble strategy, Tree-of-Thought's systematic search, and ReAct's tool utilization pattern.
In production environments, not only technique performance but also cost, latency, consistency, and security (prompt injection defense) must be holistically considered. The most important thing is selecting the right technique for the task characteristics and continuously improving through systematic evaluation pipelines.
As LLMs' baseline reasoning capabilities improve in the future, the relative advantages of individual prompting techniques may change, but the fundamental principle of prompt engineering -- "understanding how the model reasons and guiding it" -- will remain unchanged.
##  [](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en#references)References
  * [Wei, J., et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. NeurIPS 2022.](https://arxiv.org/abs/2201.11903)
  * [Wang, X., et al. (2022). Self-Consistency Improves Chain of Thought Reasoning in Language Models. ICLR 2023.](https://arxiv.org/abs/2203.11171)
  * [Yao, S., et al. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. NeurIPS 2023.](https://arxiv.org/abs/2305.10601)
  * [Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. ICLR 2023.](https://arxiv.org/abs/2210.03629)
  * [Kojima, T., et al. (2022). Large Language Models are Zero-Shot Reasoners.](https://arxiv.org/abs/2205.11916)
  * [DAIR.AI Prompt Engineering Guide](https://www.promptingguide.ai/)
  * [OpenAI Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
  * [Anthropic Prompt Engineering Documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)


[Discuss on Twitter](https://mobile.twitter.com/search?q=https%3A%2F%2Fwww.youngju.dev%2Fblog%2Fllm%2F2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en) • [View on GitHub](https://github.com/fjvbn2003/yj-next-blog2/blob/main/data/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced.en.mdx)
Load Comments
## Tags
[llm](https://www.youngju.dev/tags/llm)[prompt-engineering](https://www.youngju.dev/tags/prompt-engineering)[chain-of-thought](https://www.youngju.dev/tags/chain-of-thought)[tree-of-thought](https://www.youngju.dev/tags/tree-of-thought)[react](https://www.youngju.dev/tags/react)[few-shot](https://www.youngju.dev/tags/few-shot)[2026-03](https://www.youngju.dev/tags/2026-03)
## Related Articles
  * ### [LLM 프롬프트 엔지니어링 고급 기법: Chain-of-Thought·Tree-of-Thought·ReAct·Few-Shot 패턴 실전 가이드 2026년 3월 12일](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced)
  * ### [Advanced Prompt Engineering 완전 가이드 2025: CoT, ToT, Self-Consistency, 메타프롬프팅 2026년 4월 14일](https://www.youngju.dev/blog/culture/2026-04-14-advanced-prompt-engineering-techniques-optimization-guide-2025)
  * ### [LLM 프롬프트 엔지니어링 고급 기법: Chain-of-Thought·ReAct·Tree of Thoughts 실전 적용 2026년 3월 10일](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced)


## Previous Article
[ELK 스택 기반 로그 수집·분석 파이프라인: Elasticsearch·Fluentd·Kibana 프로덕션 구축과 최적화](https://www.youngju.dev/blog/observability/2026-03-12-elk-stack-elasticsearch-fluentd-kibana-log-pipeline)
## Next Article
[LLM 추론 서빙 프레임워크 비교: TensorRT-LLM vs vLLM vs SGLang 프로덕션 배포 전략](https://www.youngju.dev/blog/llm/2026-03-12-llm-inference-serving-tensorrt-llm-vllm-sglang-comparison)
[← Back to the blog](https://www.youngju.dev/blog)
mailMail[githubGitHub](https://github.com/fjvbn2003)[facebookFacebook](https://www.facebook.com/profile.php?id=100010923780547)[youtubeYoutube](https://youtube.com/channel/UC1VM2Zl33X70KJsDLixv_SQ)[linkedinLinkedin](https://www.linkedin.com/in/%EC%98%81%EC%A3%BC-%EA%B9%80-2303b8214/?originalSubdomain=kr)[twitterTwitter](https://twitter.com/fjvbn20031)
Youngju Kim
• 
© 2026
• 
[Chaos and Order](https://www.youngju.dev/)
[Tailwind Nextjs Theme](https://github.com/timlrx/tailwind-nextjs-starter-blog)
[Home](https://www.youngju.dev/)[Blog](https://www.youngju.dev/blog)[Tags](https://www.youngju.dev/tags)[Projects](https://www.youngju.dev/projects)[Tools](https://www.youngju.dev/tools)[Explore](https://www.youngju.dev/explore)[About](https://www.youngju.dev/about)

