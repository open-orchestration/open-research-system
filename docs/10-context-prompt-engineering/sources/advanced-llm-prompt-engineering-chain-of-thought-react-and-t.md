# Advanced LLM Prompt Engineering: Chain-of-Thought, ReAct, and Tree of ...

Source: https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en

[Skip to content](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#main-content)[ChaosAndOrder](https://www.youngju.dev/)
[Blog](https://www.youngju.dev/blog)[Tags](https://www.youngju.dev/tags)[Projects](https://www.youngju.dev/projects)[Tools](https://www.youngju.dev/tools)[Explore](https://www.youngju.dev/explore)[About](https://www.youngju.dev/about)
  1. [Home](https://www.youngju.dev/)
  2. /
  3. [Blog](https://www.youngju.dev/blog)
  4. /
  5. blog
  6. /
  7. Advanced LLM Prompt Engineering: Chain-of-Thought, ReAct, and Tree of Thoughts in Practice

Published on
    2026년 3월 10일 화요일
# Advanced LLM Prompt Engineering: Chain-of-Thought, ReAct, and Tree of Thoughts in Practice
[🇰🇷KO한국어](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced "한국어")🇺🇸ENEnglish[🇯🇵JA日本語](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.ja "日本語")
[Split View](https://www.youngju.dev/split/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced)[필사 모드](https://www.youngju.dev/transcribe/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en)[✨Start Quiz](https://www.youngju.dev/quiz/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced) 

Authors
    
  * ![avatar](https://www.youngju.dev/static/images/avatar.jpg) 

Name
    Youngju Kim 

Twitter
    [@fjvbn20031](https://twitter.com/fjvbn20031)


  * [Introduction](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#introduction)
  * [Fundamental Principles of Prompt Engineering](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#fundamental-principles-of-prompt-engineering)
    * [1. Clarity](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#1-clarity)
    * [2. Structure](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#2-structure)
    * [3. Constraints](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#3-constraints)
    * [4. Iteration](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#4-iteration)
  * [Few-shot Prompting Strategies](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#few-shot-prompting-strategies)
  * [Chain-of-Thought (CoT) Deep Dive](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#chain-of-thought-cot-deep-dive)
    * [Zero-shot CoT](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#zero-shot-cot)
    * [Few-shot CoT](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#few-shot-cot)
    * [Advanced CoT Variants](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#advanced-cot-variants)
  * [ReAct Framework Implementation](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#react-framework-implementation)
  * [Self-Consistency Sampling](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#self-consistency-sampling)
  * [Tree of Thoughts (ToT)](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#tree-of-thoughts-tot)
  * [Structured Output (JSON Mode, Function Calling)](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#structured-output-json-mode-function-calling)
    * [JSON Mode Usage](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#json-mode-usage)
    * [Function Calling Pattern](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#function-calling-pattern)
  * [Production Prompt Management Strategies](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#production-prompt-management-strategies)
    * [Version Control](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#version-control)
    * [A/B Testing](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#ab-testing)
    * [Guardrails](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#guardrails)
    * [Prompt Template System](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#prompt-template-system)
  * [Prompt Evaluation Methodology](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#prompt-evaluation-methodology)
  * [Technique Comparison Table](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#technique-comparison-table)
  * [Production Checklist](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#production-checklist)
  * [Conclusion](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#conclusion)


![LLM Prompt Engineering](https://www.youngju.dev/static/images/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.png)
##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#introduction)Introduction
Prompt engineering is a core discipline for maximizing LLM performance. It has evolved beyond simply asking questions into a systematic engineering field that designs how models reason and respond. Starting with Google's Chain-of-Thought paper in 2022, a series of advanced prompting techniques -- ReAct, Self-Consistency, Tree of Thoughts -- have emerged to dramatically improve LLM reasoning capabilities.
This article analyzes the theoretical foundations and mechanics of each technique, provides Python implementation code, and covers practical strategies for applying them in production environments. We also address structured output (JSON Mode, Function Calling), prompt template management, and evaluation methodologies.
##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#fundamental-principles-of-prompt-engineering)Fundamental Principles of Prompt Engineering
Effective prompt design requires understanding four core principles.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#1-clarity)1. Clarity
Avoid ambiguous instructions and specify concrete requirements. Instead of "Write a good article," use "Write a 500-word introduction for a technical blog post. The target audience is junior developers, and use analogies to explain concepts."
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#2-structure)2. Structure
Clearly separate the Role, Context, Instruction, and Output Format within your prompt.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#3-constraints)3. Constraints
Specify output length, format, tone, and restrictions to guide responses in the desired direction.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#4-iteration)4. Iteration
Prompts are never perfect on the first try. Analyze outputs and continuously refine and optimize.
##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#few-shot-prompting-strategies)Few-shot Prompting Strategies
Few-shot prompting includes a small number of input-output examples in the prompt so the model learns the desired pattern. It can achieve 15-25% accuracy improvement over zero-shot prompting and is especially effective for tasks requiring consistent output formatting.

```
from openai import OpenAI

client = OpenAI()

def few_shot_sentiment_analysis(text: str) -> str:
    """Sentiment analysis using few-shot prompting"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Analyze the sentiment of the given text and classify it as positive, negative, or neutral."
            },
            # Few-shot example 1
            {"role": "user", "content": "This product is amazing! Fast shipping and great quality."},
            {"role": "assistant", "content": "Sentiment: Positive\nReason: Contains positive expressions like 'amazing', 'fast', 'great quality'"},
            # Few-shot example 2
            {"role": "user", "content": "The delivery was extremely late and the product had scratches."},
            {"role": "assistant", "content": "Sentiment: Negative\nReason: Describes negative experiences with 'extremely late', 'had scratches'"},
            # Few-shot example 3
            {"role": "user", "content": "It's an average product. Fair for the price."},
            {"role": "assistant", "content": "Sentiment: Neutral\nReason: Balanced evaluation with 'average', 'fair'"},
            # Actual analysis target
            {"role": "user", "content": text}
        ],
        temperature=0.0
    )
    return response.choices[0].message.content

```

**Few-shot Design Tips** :
  * 3-5 examples is optimal. Too many waste context; too few fail to establish the pattern
  * Ensure diversity in examples: positive/negative/neutral, short/long sentences
  * Include edge cases in your examples
  * Example ordering can affect results, so consider randomizing placement


##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#chain-of-thought-cot-deep-dive)Chain-of-Thought (CoT) Deep Dive
Chain-of-Thought was proposed in 2022 by Wei et al. at Google. It guides LLMs to explicitly generate intermediate reasoning steps before arriving at a final answer. It has been shown to improve accuracy by 40-60% on complex reasoning tasks.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#zero-shot-cot)Zero-shot CoT
The simplest form -- just append "Let's think step by step" to your prompt.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#few-shot-cot)Few-shot CoT
Provides examples that include the reasoning process to induce more sophisticated step-by-step thinking.

```
def chain_of_thought_math(problem: str) -> str:
    """Math problem solving using Chain-of-Thought"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a math tutor who solves problems step by step. "
                    "Explain each step clearly and present the final answer."
                )
            },
            # CoT example with reasoning process
            {
                "role": "user",
                "content": "A cafe has 23 customers. 12 more arrived in the morning, and 8 left in the afternoon. How many customers are in the cafe now?"
            },
            {
                "role": "assistant",
                "content": (
                    "Let me solve this step by step.\n\n"
                    "Step 1: Identify the initial count\n"
                    "- Customers initially in the cafe: 23\n\n"
                    "Step 2: Calculate morning change\n"
                    "- 12 more arrived: 23 + 12 = 35\n\n"
                    "Step 3: Calculate afternoon change\n"
                    "- 8 customers left: 35 - 8 = 27\n\n"
                    "Final Answer: There are 27 customers in the cafe now."
                )
            },
            {"role": "user", "content": problem}
        ],
        temperature=0.0
    )
    return response.choices[0].message.content

```

###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#advanced-cot-variants)Advanced CoT Variants
  * **Auto-CoT** : Automatically samples diverse questions and generates reasoning chains to construct demonstrations
  * **Layered CoT** : Splits reasoning into multiple passes, allowing review and correction at each stage
  * **Trace-of-Thought** : Optimized for smaller models (~7B parameters), creates subproblems to improve arithmetic reasoning


##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#react-framework-implementation)ReAct Framework Implementation
ReAct (Reasoning + Acting), proposed by Yao et al. in 2022, is a framework where LLMs iterate through **Thought** , **Action** , and **Observation** loops while interacting with external tools to solve problems. It significantly reduces hallucinations on HotpotQA and achieved a 34% higher success rate than prior methods on the ALFWorld benchmark.

```
import json
import requests
from openai import OpenAI

client = OpenAI()

# Tool definitions
def search_wikipedia(query: str) -> str:
    """Wikipedia search tool"""
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 3
    }
    resp = requests.get(url, params=params)
    results = resp.json().get("query", {}).get("search", [])
    if not results:
        return "No search results found."
    return "\n".join([r["title"] + ": " + r["snippet"] for r in results])


def calculator(expression: str) -> str:
    """Safe arithmetic calculator"""
    allowed_chars = set("0123456789+-*/.(). ")
    if all(c in allowed_chars for c in expression):
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Calculation error: {e}"
    return "Contains disallowed characters."


TOOLS = {
    "search_wikipedia": search_wikipedia,
    "calculator": calculator,
}


def react_agent(question: str, max_steps: int = 5) -> str:
    """Agent implementing the ReAct pattern"""
    system_prompt = """You are a ReAct agent. Respond in the following format:

Thought: Analyze the current situation and reason about what to do next.
Action: Provide the tool and input in JSON format.
Observation: Review the tool execution result.
... (repeat as needed)
Final Answer: Present the final answer.

Available tools:
- search_wikipedia: Search Wikipedia (input: search query)
- calculator: Arithmetic calculation (input: math expression)"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

    for step in range(max_steps):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.0
        )
        assistant_msg = response.choices[0].message.content

        # Exit if Final Answer is present
        if "Final Answer:" in assistant_msg:
            return assistant_msg.split("Final Answer:")[-1].strip()

        # Parse and execute Action
        if "Action:" in assistant_msg:
            action_line = assistant_msg.split("Action:")[-1].strip()
            try:
                action_data = json.loads(action_line.split("\n")[0])
                tool_name = action_data.get("tool", "")
                tool_input = action_data.get("input", "")

                if tool_name in TOOLS:
                    observation = TOOLS[tool_name](tool_input)
                else:
                    observation = f"Unknown tool: {tool_name}"
            except json.JSONDecodeError:
                observation = "Failed to parse Action"

            messages.append({"role": "assistant", "content": assistant_msg})
            messages.append({
                "role": "user",
                "content": f"Observation: {observation}"
            })

    return "Reached maximum steps without generating an answer."

```

**Benefits of ReAct** :
  * Transparent reasoning process makes debugging and auditing straightforward
  * External tool integration significantly mitigates hallucination issues
  * Widely adopted as the foundational architecture for agent systems


##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#self-consistency-sampling)Self-Consistency Sampling
Self-Consistency, proposed by Wang et al. (2022), is a decoding strategy that generates multiple reasoning paths for the same prompt and selects the final answer through majority voting. When combined with CoT, it achieved accuracy improvements of 17.9% on GSM8K and 12.2% on AQuA.
The core idea is simple: complex problems typically have multiple valid solution paths, and if these converge on the same answer, that answer is likely correct.

```
from collections import Counter
from openai import OpenAI

client = OpenAI()


def self_consistency_solve(
    question: str,
    num_samples: int = 5,
    temperature: float = 0.7
) -> dict:
    """Improved reasoning accuracy through Self-Consistency sampling"""
    system_prompt = (
        "Solve the math problem step by step. "
        "On the last line, write the answer in the format 'Answer: [number]'."
    )
    answers = []
    reasoning_paths = []

    for i in range(num_samples):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            temperature=temperature  # Generate diverse reasoning paths
        )
        content = response.choices[0].message.content
        reasoning_paths.append(content)

        # Extract answer
        for line in content.split("\n"):
            if line.strip().startswith("Answer:"):
                answer = line.split("Answer:")[-1].strip()
                answers.append(answer)
                break

    # Majority voting
    if not answers:
        return {"final_answer": "Failed to extract answer", "confidence": 0.0}

    counter = Counter(answers)
    most_common = counter.most_common(1)[0]
    confidence = most_common[1] / len(answers)

    return {
        "final_answer": most_common[0],
        "confidence": confidence,
        "vote_distribution": dict(counter),
        "num_samples": num_samples,
        "reasoning_paths": reasoning_paths
    }


# Usage example
result = self_consistency_solve(
    "A school has 450 students. 60% are boys, and 25% of boys wear glasses. "
    "How many boys wear glasses?",
    num_samples=7
)
print(f"Final answer: {result['final_answer']}")
print(f"Confidence: {result['confidence']:.1%}")
print(f"Vote distribution: {result['vote_distribution']}")

```

**Self-Consistency Optimization Tips** :
  * Set temperature in the 0.5-0.9 range to balance diversity and quality
  * 5-10 samples is cost-effective for most applications
  * Universal Self-Consistency (USC) extends the technique to free-form text generation


##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#tree-of-thoughts-tot)Tree of Thoughts (ToT)
Tree of Thoughts, proposed by Yao et al. (2023), extends CoT by exploring and evaluating multiple reasoning paths in a tree structure. On the Game of 24 task, GPT-4's CoT accuracy was 4%, which jumped to 74% with ToT.
Core components of ToT:
  * **Thought Decomposition** : Breaking the problem into intermediate thought steps
  * **Thought Generator** : Generating candidate thoughts at each node (sampling or proposing)
  * **State Evaluator** : Assessing the promise of each thought state
  * **Search Algorithm** : BFS (breadth-first) or DFS (depth-first) traversal



```
from openai import OpenAI
from typing import List

client = OpenAI()


def generate_thoughts(problem: str, current_state: str, n: int = 3) -> List[str]:
    """Generate possible next thoughts from the current state"""
    prompt = f"""Problem: {problem}
Reasoning so far: {current_state}

Propose {n} possible next reasoning steps from this state.
Each step should represent a different approach.
Format:
1. [First approach]
2. [Second approach]
3. [Third approach]"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    content = response.choices[0].message.content
    thoughts = []
    for line in content.split("\n"):
        line = line.strip()
        if line and line[0].isdigit() and "." in line:
            thoughts.append(line.split(".", 1)[1].strip())
    return thoughts[:n]


def evaluate_thought(problem: str, thought_path: str) -> float:
    """Evaluate the promise of a reasoning path on a 0-1 scale"""
    prompt = f"""Problem: {problem}
Reasoning path: {thought_path}

Evaluate how likely this reasoning path is to reach the correct answer.
Provide a score between 0.0 (not promising at all) and 1.0 (very promising).
Respond with only the numeric score."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    try:
        score = float(response.choices[0].message.content.strip())
        return min(max(score, 0.0), 1.0)
    except ValueError:
        return 0.5


def tree_of_thoughts_bfs(
    problem: str,
    max_depth: int = 3,
    beam_width: int = 2
) -> str:
    """BFS-based Tree of Thoughts implementation"""
    # Initial state
    current_states = [("", 1.0)]  # (reasoning path, score)

    for depth in range(max_depth):
        all_candidates = []

        for state, _ in current_states:
            # Generate candidate thoughts from each state
            thoughts = generate_thoughts(problem, state)

            for thought in thoughts:
                new_path = f"{state}\nStep {depth+1}: {thought}" if state else f"Step 1: {thought}"
                score = evaluate_thought(problem, new_path)
                all_candidates.append((new_path, score))

        # Select top candidates by beam_width
        all_candidates.sort(key=lambda x: x[1], reverse=True)
        current_states = all_candidates[:beam_width]

        print(f"Depth {depth+1}: Best score = {current_states[0][1]:.2f}")

    # Generate final answer
    best_path = current_states[0][0]
    final_prompt = f"""Problem: {problem}
Reasoning path: {best_path}

Based on the reasoning above, write the final answer."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": final_prompt}],
        temperature=0.0
    )
    return response.choices[0].message.content

```

**Considerations When Using ToT** :
  * API call count grows exponentially, so costs must be carefully managed
  * Overkill for simple problems. Best suited for complex planning, creative writing, and puzzle-solving
  * Tune beam_width and max_depth according to problem complexity


##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#structured-output-json-mode-function-calling)Structured Output (JSON Mode, Function Calling)
In production environments, LLM outputs must be processed programmatically. As of 2026, major LLM providers support native structured output, and combining them with validation libraries like Pydantic enables robust pipelines.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#json-mode-usage)JSON Mode Usage

```
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List, Optional

client = OpenAI()


class CodeReview(BaseModel):
    """Code review result schema"""
    file_path: str = Field(description="File path under review")
    severity: str = Field(description="Severity: critical, warning, info")
    category: str = Field(description="Category: security, performance, style, logic")
    line_number: Optional[int] = Field(description="Line number")
    message: str = Field(description="Review comment")
    suggestion: str = Field(description="Suggested improvement code")


class CodeReviewResult(BaseModel):
    """Overall code review result"""
    reviews: List[CodeReview]
    summary: str = Field(description="Review summary")
    overall_score: int = Field(description="Overall score (1-10)")


def structured_code_review(code: str, language: str = "python") -> CodeReviewResult:
    """Code review with structured output"""
    response = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    f"You are a senior {language} developer. "
                    "Review the given code and provide feedback in a structured format."
                )
            },
            {"role": "user", "content": f"Please review the following code:\n\n{code}"}
        ],
        response_format=CodeReviewResult
    )
    return response.choices[0].message.parsed

```

###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#function-calling-pattern)Function Calling Pattern
Function Calling enables LLMs to invoke predefined functions, allowing reliable integration with external systems.

```
import json
from openai import OpenAI

client = OpenAI()

# Tool schema definition
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Retrieves the current price of a stock",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock symbol (e.g., AAPL, GOOGL)"
                    },
                    "currency": {
                        "type": "string",
                        "enum": ["USD", "KRW", "JPY"],
                        "description": "Display currency"
                    }
                },
                "required": ["symbol"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_alert",
            "description": "Sets up a stock price alert",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {"type": "string"},
                    "target_price": {"type": "number"},
                    "direction": {
                        "type": "string",
                        "enum": ["above", "below"]
                    }
                },
                "required": ["symbol", "target_price", "direction"]
            }
        }
    }
]


def function_calling_agent(user_message: str) -> str:
    """Agent using Function Calling"""
    messages = [
        {
            "role": "system",
            "content": "You are a financial assistant that provides stock information."
        },
        {"role": "user", "content": user_message}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    msg = response.choices[0].message

    # Handle Function Calls
    if msg.tool_calls:
        for tool_call in msg.tool_calls:
            func_name = tool_call.function.name
            func_args = json.loads(tool_call.function.arguments)

            # Execute function (mock data here)
            if func_name == "get_stock_price":
                result = json.dumps({
                    "symbol": func_args["symbol"],
                    "price": 185.50,
                    "change": "+2.3%"
                })
            elif func_name == "create_alert":
                result = json.dumps({
                    "status": "success",
                    "alert_id": "alert_12345"
                })
            else:
                result = json.dumps({"error": "Unknown function"})

            messages.append(msg)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

        # Generate final response
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return final_response.choices[0].message.content

    return msg.content

```

##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#production-prompt-management-strategies)Production Prompt Management Strategies
Managing prompts effectively in production requires the same level of engineering practices as managing code.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#version-control)Version Control
Separate prompts into dedicated files and manage them with Git. Record the rationale and performance impact for each change.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#ab-testing)A/B Testing
When deploying a new prompt, apply it to a subset of traffic and compare performance. Monitor accuracy, latency, and cost simultaneously.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#guardrails)Guardrails
Implement safeguards such as prompt injection defense, output validation, and harmful content filtering.
###  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#prompt-template-system)Prompt Template System

```
from dataclasses import dataclass, field
from typing import Dict, Any
from datetime import datetime


@dataclass
class PromptTemplate:
    """Prompt template management class"""
    name: str
    version: str
    template: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def render(self, **kwargs) -> str:
        """Render final prompt with variable substitution"""
        result = self.template
        for key, value in kwargs.items():
            placeholder = f"__{key.upper()}__"
            result = result.replace(placeholder, str(value))
        return result


# Prompt registry
class PromptRegistry:
    def __init__(self):
        self._templates: Dict[str, PromptTemplate] = {}

    def register(self, template: PromptTemplate):
        key = f"{template.name}:{template.version}"
        self._templates[key] = template

    def get(self, name: str, version: str = "latest") -> PromptTemplate:
        if version == "latest":
            candidates = [
                v for k, v in self._templates.items()
                if k.startswith(f"{name}:")
            ]
            return max(candidates, key=lambda t: t.version)
        return self._templates[f"{name}:{version}"]


# Usage example
registry = PromptRegistry()
registry.register(PromptTemplate(
    name="code_review",
    version="2.1",
    template=(
        "You are a senior __LANGUAGE__ developer.\n"
        "Review the following code.\n\n"
        "Review criteria:\n"
        "- Security vulnerabilities\n"
        "- Performance issues\n"
        "- Code style\n\n"
        "Code:\n__CODE__"
    ),
    metadata={"model": "gpt-4o", "temperature": 0.0}
))

```

##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#prompt-evaluation-methodology)Prompt Evaluation Methodology
A systematic evaluation pipeline is needed to objectively measure prompt effectiveness.
**Evaluation Metrics** :  
| Metric  | Description  | Measurement Method  |  
| --- | --- | --- |  
| Accuracy  | Match rate with correct answers  | Automated comparison or LLM-as-Judge  |  
| Consistency  | Output variability for same input  | Standard deviation across multiple runs  |  
| Latency  | Time to response  | API call time measurement  |  
| Cost  | Token consumption-based cost  | Input/output token count tracking  |  
| Safety  | Rate of harmful content generation  | Safety classifier application  |  
| Format Compliance  | Adherence to specified output format  | Schema validation  |  
**LLM-as-Judge Pattern** : For free-form text where automated evaluation is difficult, use a separate LLM as an evaluator to score quality. Specifying evaluation criteria as a rubric and having the evaluator LLM use CoT improves evaluation accuracy.
##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#technique-comparison-table)Technique Comparison Table  
| Technique  | Core Principle  | Accuracy Gain  | API Calls  | Best For  | Complexity  |  
| --- | --- | --- | --- | --- | --- |  
| Zero-shot  | Direct question  | Baseline  | 1  | Simple tasks  | Low  |  
| Few-shot  | Example-based learning  | +15-25%  | 1  | Format consistency  | Low  |  
| Zero-shot CoT  | Step-by-step reasoning  | +20-40%  | 1  | Math, logic  | Low  |  
| Few-shot CoT  | Reasoning examples  | +40-60%  | 1  | Complex reasoning  | Medium  |  
| ReAct  | Reasoning+action loop  | Task-dependent  | Multiple  | Tool usage  | Medium  |  
| Self-Consistency  | Majority voting  | +10-18%  | 5-10  | Reasoning accuracy  | Medium  |  
| Tree of Thoughts  | Tree search  | +70% (specific tasks)  | Multiple  | Planning, puzzles  | High  |  
| Structured Output  | Schema enforcement  | 100% format  | 1  | Data extraction  | Low  |  
##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#production-checklist)Production Checklist
Review the following items before deploying prompts to production.
  1. **Technique Selection** : Have you chosen a technique matching the task complexity? Using ToT for simple tasks is wasteful
  2. **Example Quality** : Are Few-shot examples diverse and accurate? Do they include edge cases?
  3. **CoT Usage** : Are you inducing step-by-step thinking for tasks that require reasoning?
  4. **Output Format** : Are you using JSON Mode or Function Calling for tasks needing structured output?
  5. **Cost Management** : Have you estimated API costs and set budgets when using Self-Consistency or ToT?
  6. **Evaluation Pipeline** : Do you have an automated evaluation system to measure the effect of prompt changes?
  7. **Guardrails** : Are prompt injection defense and output validation logic implemented?
  8. **Version Control** : Are prompts managed with Git with tracked change history?
  9. **Monitoring** : Are you monitoring accuracy, latency, and cost in real-time?
  10. **Fallback Strategy** : Do you have fallback strategies (simpler prompts, default values, etc.) for prompt failures?


##  [](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en#conclusion)Conclusion
Prompt engineering is not just about "asking good questions" -- it is an engineering discipline for systematically eliciting reasoning capabilities from LLMs. Inducing step-by-step reasoning with Chain-of-Thought, integrating external tools with ReAct, boosting reliability with Self-Consistency, and exploring complex problems with Tree of Thoughts -- understanding the principles of these techniques and applying them where they fit is the key.
While reasoning-native models like o1 and o3 are internalizing some of these techniques, the fundamental principles of prompt design and production management strategies remain essential. Managing prompts like code, ensuring quality with evaluation pipelines, and building a culture of continuous improvement are the keys to successful production LLM systems.
[Discuss on Twitter](https://mobile.twitter.com/search?q=https%3A%2F%2Fwww.youngju.dev%2Fblog%2Fllm%2F2026-03-10-llm-prompt-engineering-cot-react-advanced.en) • [View on GitHub](https://github.com/fjvbn2003/yj-next-blog2/blob/main/data/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en.mdx)
Load Comments
## Tags
[llm](https://www.youngju.dev/tags/llm)[prompt-engineering](https://www.youngju.dev/tags/prompt-engineering)[chain-of-thought](https://www.youngju.dev/tags/chain-of-thought)[react-prompting](https://www.youngju.dev/tags/react-prompting)[tree-of-thoughts](https://www.youngju.dev/tags/tree-of-thoughts)[2026-03](https://www.youngju.dev/tags/2026-03)
## Related Articles
  * ### [LLM 프롬프트 엔지니어링 고급 기법: Chain-of-Thought·ReAct·Tree of Thoughts 실전 적용 2026년 3월 10일](https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced)
  * ### [LLM 프롬프트 엔지니어링 고급 기법: Chain-of-Thought·Tree-of-Thought·ReAct·Few-Shot 패턴 실전 가이드 2026년 3월 12일](https://www.youngju.dev/blog/llm/2026-03-12-llm-prompt-engineering-cot-tot-react-few-shot-advanced)
  * ### [Advanced Prompt Engineering 완전 가이드 2025: CoT, ToT, Self-Consistency, 메타프롬프팅 2026년 4월 14일](https://www.youngju.dev/blog/culture/2026-04-14-advanced-prompt-engineering-techniques-optimization-guide-2025)


## Previous Article
[Grafana Loki 로그 관리 완전 가이드: LogQL 쿼리·수집 파이프라인·알림 설정](https://www.youngju.dev/blog/observability/2026-03-10-grafana-loki-log-management-logql)
## Next Article
[Kubernetes RBAC 심층 가이드: Role·ClusterRole·OPA Gatekeeper로 구현하는 최소 권한 접근제어](https://www.youngju.dev/blog/kubernetes/2026-03-10-kubernetes-rbac-opa-gatekeeper-access-control)
[← Back to the blog](https://www.youngju.dev/blog)
mailMail[githubGitHub](https://github.com/fjvbn2003)[facebookFacebook](https://www.facebook.com/profile.php?id=100010923780547)[youtubeYoutube](https://youtube.com/channel/UC1VM2Zl33X70KJsDLixv_SQ)[linkedinLinkedin](https://www.linkedin.com/in/%EC%98%81%EC%A3%BC-%EA%B9%80-2303b8214/?originalSubdomain=kr)[twitterTwitter](https://twitter.com/fjvbn20031)
Youngju Kim
• 
© 2026
• 
[Chaos and Order](https://www.youngju.dev/)
[Tailwind Nextjs Theme](https://github.com/timlrx/tailwind-nextjs-starter-blog)
[Home](https://www.youngju.dev/)[Blog](https://www.youngju.dev/blog)[Tags](https://www.youngju.dev/tags)[Projects](https://www.youngju.dev/projects)[Tools](https://www.youngju.dev/tools)[Explore](https://www.youngju.dev/explore)[About](https://www.youngju.dev/about)

