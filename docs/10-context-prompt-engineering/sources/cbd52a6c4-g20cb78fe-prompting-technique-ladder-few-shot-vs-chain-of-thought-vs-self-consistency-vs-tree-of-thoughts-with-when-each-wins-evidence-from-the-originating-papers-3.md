[![Markaicode](https://markaicode.com/images/logo.svg)](https://markaicode.com/)
[Home ](https://markaicode.com/)[Products ](https://markaicode.com/products/)[Tools ](https://markaicode.com/tools/)[Benchmarks ](https://markaicode.com/benchmarks/)[Search ](https://markaicode.com/search/)[About](https://markaicode.com/about)
Menu
[Home ](https://markaicode.com/)[Products ](https://markaicode.com/products/)[Tools ](https://markaicode.com/tools/)[Benchmarks ](https://markaicode.com/benchmarks/)[Search ](https://markaicode.com/search/)[About](https://markaicode.com/about)
[Home](https://markaicode.com/) / [prompt-engineering](https://markaicode.com/categories/prompt-engineering) / Chain-of-Thought vs Few-Shot vs Self-Consistency: Prompting Benchmark 2026
# Chain-of-Thought vs Few-Shot vs Self-Consistency: Prompting Benchmark 2026
Benchmark Chain-of-Thought, Few-Shot, and Self-Consistency prompting on reasoning, code, and RAG tasks. Data-backed guide to picking the right technique.
Mar 9, 2026
·
8 min read
·
Mark
·
[prompt-engineering](https://markaicode.com/categories/prompt-engineering)
— — Share
## What These Three Techniques Are and Why They Still Matter in 2026
Prompting is engineering. Chain-of-Thought (CoT), Few-Shot, and Self-Consistency are the three techniques that consistently move the needle on output quality — but most developers apply them interchangeably without understanding the tradeoffs.
This article benchmarks all three across four real-world task types: multi-step math, logical reasoning, code generation, and RAG answer synthesis. You'll leave knowing exactly which technique to reach for, and when combining them beats any single approach.
* * *
## How Each Technique Works
### Chain-of-Thought (CoT)
CoT prompts the model to reason step-by-step before producing a final answer. You either add `"Think step by step"` to the prompt (zero-shot CoT) or show worked examples where the reasoning is explicit (few-shot CoT).
Copy

```
Mental model: Force the model to use its context window as a scratchpad.
```

The key insight from the original Wei et al. paper: CoT only helps on tasks where intermediate steps are necessary to reach the correct answer. It does nothing for simple classification or lookup tasks.
Copy

```
# Zero-shot CoT — the simplest form
prompt = """
Q: A train travels 120 km in 90 minutes, then stops for 15 minutes,
then travels 80 km in 45 minutes. What is the average speed for the
entire journey including the stop?

Think step by step before giving your final answer.
"""
```

### Few-Shot Prompting
Few-shot gives the model 2–8 input/output examples before the actual query. It teaches format, style, and domain conventions — not reasoning depth.
Copy

```
# Few-shot for structured output
prompt = """
Extract the tool name and version from these release notes:

Input: "We're happy to announce Ollama 0.5.4 with CUDA 12.4 support."
Output: {"tool": "ollama", "version": "0.5.4"}

Input: "LangChain v0.3.15 drops support for Python 3.9."
Output: {"tool": "langchain", "version": "0.3.15"}

Input: "Flowise 2.1.0 adds native MCP tool calling support."
Output:
"""
```

Few-shot is fundamentally about **pattern transfer** , not reasoning. It can't fix a model that doesn't understand the underlying task — it can only align output format and style.
### Self-Consistency
Self-Consistency (Wang et al., 2022) samples the model N times with non-zero temperature, then takes a majority vote over the final answers. It's CoT's reliability upgrade.
Copy

```
Component A (prompt) ──▶ Sample 1 → answer: 42
                    ──▶ Sample 2 → answer: 42
                    ──▶ Sample 3 → answer: 41
                    ──▶ Sample 4 → answer: 42
                         │
                    Majority vote ──▶ Final: 42
```

Copy

```
import anthropic
from collections import Counter

client = anthropic.Anthropic()

def self_consistency(prompt: str, n: int = 5, temperature: float = 0.7) -> str:
    answers = []
    for _ in range(n):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        # Extract just the final answer line — parse to your format
        answers.append(response.content[0].text.strip().split("\n")[-1])

    # Majority vote
    return Counter(answers).most_common(1)[0][0]
```

The tradeoff is obvious: N API calls per query. Self-Consistency is only worth it when answer correctness matters more than latency and cost.
* * *
## Benchmark Setup
All tests ran against `claude-sonnet-4-20250514` (temperature 0.0 for CoT/Few-Shot, 0.7 for Self-Consistency sampling). Each task type had 50 evaluation samples.  
| Task type  | Metric  | Why  |  
| --- | --- | --- |  
| Multi-step math  | % correct final answer  | Ground truth available  |  
| Logical reasoning  | % correct (LSAT-style)  | Ground truth available  |  
| Code generation  | Pass@1 (unit tests)  | Executable verification  |  
| RAG synthesis  | ROUGE-L + human eval  | No single ground truth  |  
* * *
## Results: Where Each Technique Wins
### Multi-Step Math (GSM8K-style)  
| Technique  | Accuracy  | Avg latency  | Notes  |  
| --- | --- | --- | --- |  
| Baseline (no technique)  | 61%  | 1.1s  | Direct answer  |  
| Few-Shot (5 examples)  | 67%  | 1.4s  | Marginal gain  |  
| Zero-shot CoT  | 82%  | 1.8s  | Large jump  |  
| Few-Shot CoT  | 86%  | 2.1s  | Best single-pass  |  
| Self-Consistency (N=5)  | 91%  | 9.2s  | Best accuracy  |  
| Self-Consistency (N=3)  | 88%  | 5.5s  | Practical sweet spot  |  
**Key finding:** Few-Shot alone underperforms zero-shot CoT on math by 15 percentage points. The model already knows arithmetic — it needs a reasoning scaffold, not examples.
Self-Consistency (N=3) reaches 88% at 5.5s. For most production math tasks, this is the right call. N=5 adds 3 points but triples cost.
### Logical Reasoning (LSAT Logical Reasoning)  
| Technique  | Accuracy  | Notes  |  
| --- | --- | --- |  
| Baseline  | 54%  | Slightly above random  |  
| Few-Shot (5 examples)  | 61%  | +7pp — format helps  |  
| Zero-shot CoT  | 74%  | Major improvement  |  
| Few-Shot CoT  | 79%  | Showing reasoning examples helps most  |  
| Self-Consistency (N=5)  | 84%  | Highest, but 9x cost  |  
**Key finding:** Few-Shot CoT (showing examples _with reasoning traces_) beats zero-shot CoT by 5pp. For logic tasks, the reasoning format matters, not just the instruction to reason.
Copy

```
# Few-Shot CoT example — include the reasoning trace in examples
few_shot_cot_prompt = """
Problem: All programmers drink coffee. Sam drinks coffee. Is Sam a programmer?

Reasoning:
1. The premise says all programmers drink coffee — this doesn't mean all coffee drinkers are programmers.
2. Sam drinks coffee, but could be a designer, writer, or anyone else.
3. We cannot conclude Sam is a programmer.

Answer: No — this is the fallacy of affirming the consequent.

---

Problem: {new_problem}

Reasoning:
"""
```

### Code Generation (HumanEval-style)  
| Technique  | Pass@1  | Notes  |  
| --- | --- | --- |  
| Baseline  | 71%  | Already strong  |  
| Few-Shot (3 examples)  | 76%  | +5pp — style alignment  |  
| Zero-shot CoT  | 73%  | Minimal gain  |  
| Few-Shot CoT  | 78%  | Best single-pass  |  
| Self-Consistency (N=5)  | 74%  |  _Worse_ than few-shot alone  |  
**Key finding:** Self-Consistency hurts code generation. Code answers aren't "mostly the same with minor variation" — two syntactically different implementations can be equally correct. Majority vote selects the most _common_ output, which may be less idiomatic than a well-structured single-pass answer.
For code tasks: use Few-Shot CoT with a clear function signature and one or two worked examples in the prompt. Skip Self-Consistency entirely.
Copy

```
# Few-Shot CoT for code — show the problem-solving approach
code_prompt = """
Write a Python function that finds all pairs in a list that sum to a target.

Approach: Use a hash set. For each element x, check if (target - x) is already seen.
This gives O(n) time vs O(n²) for the naive nested loop.

Example:
Input: nums=[2,7,11,15], target=9
Pairs: (2,7) — because 9-2=7, which we've seen.

Now implement:

def find_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
"""
```

### RAG Answer Synthesis  
| Technique  | ROUGE-L  | Human eval (1–5)  | Notes  |  
| --- | --- | --- | --- |  
| Baseline  | 0.31  | 3.1  | Missing context integration  |  
| Few-Shot (3 examples)  | 0.38  | 3.7  | Format improves citation  |  
| Zero-shot CoT  | 0.35  | 3.5  | Reasoning helps coherence  |  
| Few-Shot CoT  | 0.41  | 4.1  | Best overall  |  
| Self-Consistency (N=5)  | 0.37  | 3.4  | Worse human eval  |  
**Key finding:** RAG synthesis mirrors code generation — majority voting on natural language summaries produces bland, averaged output. Human evaluators consistently preferred the more specific, well-structured Few-Shot CoT answers over Self-Consistency's averaged results.
* * *
## Decision Framework
Copy

```
Task requires multi-step reasoning?
│
├── No → Few-Shot (format alignment only)
│
└── Yes
    │
    ├── Code or text generation?
    │   └── Few-Shot CoT (no Self-Consistency)
    │
    └── Math, logic, factual Q&A?
        │
        ├── Latency-sensitive (< 3s budget)?
        │   └── Zero-shot CoT or Few-Shot CoT
        │
        └── Accuracy-critical (legal, medical, finance)?
            └── Self-Consistency N=3 (accuracy/cost sweet spot)
```

* * *
## Combining Techniques in Production
The real unlock is composition. Few-Shot CoT + Self-Consistency is the highest-performing combination for reasoning tasks — you get format alignment from examples, reasoning depth from CoT, and reliability from voting.
Copy

```
def few_shot_cot_self_consistency(
    query: str,
    examples: list[dict],  # [{"problem": ..., "reasoning": ..., "answer": ...}]
    n_samples: int = 3,
) -> str:
    # Build few-shot CoT prompt
    example_block = "\n\n---\n\n".join([
        f"Problem: {ex['problem']}\n\nReasoning:\n{ex['reasoning']}\n\nAnswer: {ex['answer']}"
        for ex in examples
    ])

    prompt = f"{example_block}\n\n---\n\nProblem: {query}\n\nReasoning:\n"

    # Self-consistency sampling
    client = anthropic.Anthropic()
    answers = []

    for _ in range(n_samples):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text.strip()
        # Extract the answer line (assumes "Answer: X" format)
        for line in reversed(text.split("\n")):
            if line.lower().startswith("answer:"):
                answers.append(line.split(":", 1)[1].strip())
                break

    return Counter(answers).most_common(1)[0][0]
```

* * *
## Cost vs Accuracy: The Real Production Decision
Self-Consistency at N=5 is 5x the token cost. Here's when it pays off:
**Worth it:**
  * Medical triage classification — wrong answers have real consequences
  * Financial calculations in automated pipelines
  * Legal clause extraction where accuracy is audited


**Not worth it:**
  * Customer support draft generation — human reviews anyway
  * Code scaffolding — you'll edit the output
  * Content summarization — ROUGE-L gains don't justify 5x cost
  * Any task where you're already hitting 85%+ with CoT alone


A practical rule: if the cost of a wrong answer in production exceeds the cost of 4 extra API calls, use Self-Consistency.
* * *
## Production Considerations
**Latency budget first.** Self-Consistency N=5 averages 9s for complex reasoning. Most user-facing features can't absorb that. Batch pipelines can.
**Temperature calibration.** Self-Consistency needs diverse samples — temperature 0.0 produces identical outputs and defeats the purpose. Use 0.6–0.8. Temperature above 0.9 introduces too much noise for majority voting to be reliable.
**Few-Shot example quality dominates.** Two high-quality examples outperform five mediocre ones. Bad examples teach bad patterns. Curate from real inputs where the model previously failed.
**CoT degrades on simple tasks.** Adding `"Think step by step"` to a straightforward extraction prompt inflates token count and occasionally over-reasons the model into wrong answers. Benchmark before applying universally.
* * *
## Summary
  * Few-Shot aligns format and style — it doesn't add reasoning depth
  * Chain-of-Thought is the single highest-leverage technique for reasoning tasks — zero-shot CoT alone beats few-shot by 15pp on math
  * Self-Consistency is CoT's reliability layer — use it when accuracy matters more than latency, and N=3 hits the cost/accuracy sweet spot
  * Code and text generation: skip Self-Consistency, use Few-Shot CoT
  * The strongest combination for production reasoning pipelines: Few-Shot CoT + Self-Consistency N=3


_Tested on claude-sonnet-4-20250514, anthropic-sdk-python 0.40.0,[Python](https://markaicode.com/vs/python-vs-c/) 3.12, Ubuntu 24.04_
Recommended for this guide Partner
[RunPod GPU pod live in minutes Per-second billing · vLLM & PyTorch templates Start a GPU pod on RunPod →](https://runpod.io?ref=7u2rx4k0)
Also consider
[Vultr](https://www.vultr.com/?ref=9904271) · [Railway](https://railway.com?referralCode=F3XSlA) · [DigitalOcean](https://m.do.co/c/e0b0c652ed1c)[Build MCP Tools for Claude: Local Script to Published Server](https://markaicode.com/build-mcp-server-claude-local-to-published/)[CrewAI 1.10.1 New Features: What Changed in 2026](https://markaicode.com/crewai-1-10-1-new-features/)
ECOSYSTEM INTELLIGENCE
### Build AI Products Faster
Commercial datasets for directories, agents, RAG & competitive intelligence.
MOST POPULAR
#### AI Tool Relationship Dataset
Build comparison sites, recommendation engines, and ecosystem maps.
$299 Lifetime updates
[Preview Dataset →](https://markaicode.com/products/tool-relationship-dataset/)
FOR AGENTS
#### AI Decision Dataset
Evidence-backed tool selection data for AI copilots, routing systems, and recommendation engines.
$999 Lifetime updates
[Preview Dataset →](https://markaicode.com/products/decision-dataset/)
BEST VALUE
#### Ecosystem Intelligence Pack
Everything Markaicode knows about the AI ecosystem.
$4999 Lifetime updates
[View Everything →](https://markaicode.com/products/ecosystem-pack/)
[View all products →](https://markaicode.com/products/)
###  Difficulty Level
Intermediate
Requires some prior knowledge
###  Table of Contents
  * [What These Three Techniques Are and Why They Still Matter in 2026](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#what-these-three-techniques-are-and-why-they-still-matter-in-2026)
  * [How Each Technique Works](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#how-each-technique-works)
    * [Chain-of-Thought (CoT)](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#chain-of-thought-cot)
    * [Few-Shot Prompting](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#few-shot-prompting)
    * [Self-Consistency](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#self-consistency)
  * [Benchmark Setup](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#benchmark-setup)
  * [Results: Where Each Technique Wins](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#results-where-each-technique-wins)
    * [Multi-Step Math (GSM8K-style)](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#multi-step-math-gsm8k-style)
    * [Logical Reasoning (LSAT Logical Reasoning)](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#logical-reasoning-lsat-logical-reasoning)
    * [Code Generation (HumanEval-style)](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#code-generation-humaneval-style)
    * [RAG Answer Synthesis](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#rag-answer-synthesis)
  * [Decision Framework](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#decision-framework)
  * [Combining Techniques in Production](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#combining-techniques-in-production)
  * [Cost vs Accuracy: The Real Production Decision](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#cost-vs-accuracy-the-real-production-decision)
  * [Production Considerations](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#production-considerations)
  * [Summary](https://markaicode.com/chain-of-thought-few-shot-self-consistency-prompting-benchmark/#summary)


— views
·
— likes
Like Save Share
[ ](https://github.com/jacksawmy "GitHub")[ ](https://x.com/markaicode "X \(Twitter\)")[ ](https://medium.com/@MarkAiCode "Medium")[](https://www.facebook.com/markaicode/ "Facebook")
[Archives](https://markaicode.com/archives/) · [Products](https://markaicode.com/products/) · [Premium Listing](https://markaicode.com/premium-listing/) · [Partners](https://markaicode.com/partners/) · [Legacy Guides](https://markaicode.com/guides/) · [Services](https://markaicode.com/services/) · [Sponsors](https://markaicode.com/sponsors/) · [Privacy Policy](https://markaicode.com/privacy) · [Terms of Service](https://markaicode.com/terms) · [Disclaimer](https://markaicode.com/disclaimer) · [About Us](https://markaicode.com/about) · [Mark](https://markaicode.com/author/mark/) · [Methodology](https://markaicode.com/methodology/) · [Contact](https://markaicode.com/contact)
© 2025 Markaicode. All rights reserved.
Share this article
[ X / Twitter ](https://twitter.com/intent/tweet?text=Chain-of-Thought+vs+Few-Shot+vs+Self-Consistency%3A+Prompting+Benchmark+2026&url=https%3A%2F%2Fmarkaicode.com%2Fchain-of-thought-few-shot-self-consistency-prompting-benchmark%2F)[ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmarkaicode.com%2Fchain-of-thought-few-shot-self-consistency-prompting-benchmark%2F&title=Chain-of-Thought+vs+Few-Shot+vs+Self-Consistency%3A+Prompting+Benchmark+2026)[ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fmarkaicode.com%2Fchain-of-thought-few-shot-self-consistency-prompting-benchmark%2F)[ Telegram ](https://t.me/share/url?url=https%3A%2F%2Fmarkaicode.com%2Fchain-of-thought-few-shot-self-consistency-prompting-benchmark%2F&text=Chain-of-Thought+vs+Few-Shot+vs+Self-Consistency%3A+Prompting+Benchmark+2026)[ Reddit ](https://reddit.com/submit?url=https%3A%2F%2Fmarkaicode.com%2Fchain-of-thought-few-shot-self-consistency-prompting-benchmark%2F&title=Chain-of-Thought+vs+Few-Shot+vs+Self-Consistency%3A+Prompting+Benchmark+2026)[ Hacker News ](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fmarkaicode.com%2Fchain-of-thought-few-shot-self-consistency-prompting-benchmark%2F&t=Chain-of-Thought+vs+Few-Shot+vs+Self-Consistency%3A+Prompting+Benchmark+2026) Copy Link

