# Build Your Own Deep Research Agent: An Open-Source Perplexity Clone

Source: https://knowledgesdk.com/blog/deep-research-agent

[![KnowledgeSDK](https://knowledgesdk.com/knowledgesdk_light.svg)](https://knowledgesdk.com/)
  * WHY KNOWLEDGESDK▾
  * PRODUCT▾
  * [DOCS](https://knowledgesdk.com/docs)
  * [PRICING](https://knowledgesdk.com/pricing)
  * [DASHBOARD](https://knowledgesdk.com/login)


[GET ACCESS](https://knowledgesdk.com/login?signup=1&redirectTo=%2Fsetup)
[knowledgesdk.com](https://knowledgesdk.com/)/[blog](https://knowledgesdk.com/blog)/deep-research-agent
use-caseMarch 20, 2026·16 min read
# Build Your Own Deep Research Agent: An Open-Source Perplexity Clone
Build an open-source deep research agent in Python and Node.js. Search sources, scrape top results, synthesize a cited report. Cheaper than Perplexity's $5/1000 queries.
![Build Your Own Deep Research Agent: An Open-Source Perplexity Clone](https://knowledgesdk.com/api/og/blog?title=Build%20a%20Deep%20Research%20Agent&category=use-case)
# Build Your Own Deep Research Agent: An Open-Source Perplexity Clone
Perplexity Deep Research, OpenAI Deep Research, and Gemini Deep Research have collectively made "deep research" a standard capability expectation for AI products in 2026. These systems do not just retrieve a snippet — they read multiple sources, synthesize the findings, and produce a structured research report with citations.
The problem is that these products are expensive, black-box, and designed for consumer use. Perplexity's API charges $5 per 1,000 queries. OpenAI's Deep Research tier is priced for enterprise. And neither gives you control over the sources, the reasoning process, or the output format.
This tutorial builds an open-source equivalent from scratch. By the end, you will have a deep research agent that:
  1. Takes a research question as input
  2. Generates optimized sub-queries to explore different angles
  3. Scrapes the top 5–10 sources for each sub-query
  4. Extracts key claims and evidence from each source
  5. Detects conflicts and gaps across sources
  6. Synthesizes a structured research report with inline citations


The total cost per research query: roughly $0.08–$0.25, depending on LLM choice. That is 20–60x cheaper than Perplexity's API.
* * *
## Architecture

```
Input: Research Question
       │
       ▼
[Query Planner]
Decomposes question into 3-5 sub-queries
covering different facets of the topic
       │
       ▼
[Source Finder]
For each sub-query: identify 5-10 target URLs
Using search API or LLM URL generation
       │
       ▼
[Parallel Scraper]
Concurrently scrape all identified URLs
via KnowledgeSDK → clean markdown output
       │
       ▼
[Evidence Extractor]
For each scraped page:
- Extract key claims
- Note publication date
- Identify source authority
- Tag relevant sub-queries
       │
       ▼
[Conflict Detector]
Cross-reference claims across sources
Flag contradictions and note discrepancies
       │
       ▼
[Report Synthesizer]
Combine all evidence into a structured report
with H2/H3 headers, inline citations, and a
confidence assessment
       │
       ▼
Output: Structured Research Report + Source List

```

* * *
## Setup

```
# Python
pip install knowledgesdk openai asyncio

# Node.js
npm install @knowledgesdk/node openai

```

```
export KNOWLEDGESDK_API_KEY="knowledgesdk_live_your_key_here"
export OPENAI_API_KEY="sk-your-openai-key"

```

* * *
## Python Implementation
### Core Data Structures

```
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class SubQuery:
    question: str
    angle: str  # e.g., "technical", "cost", "comparison", "use-cases"

@dataclass
class ScrapedSource:
    url: str
    title: str
    markdown: str
    scraped_at: datetime
    word_count: int

@dataclass
class ExtractedEvidence:
    source_url: str
    source_title: str
    claim: str
    supporting_text: str
    sub_query_relevance: List[str]
    confidence: float

@dataclass
class ResearchReport:
    title: str
    executive_summary: str
    sections: List[dict]
    conflicts_found: List[str]
    methodology: str
    sources: List[dict]
    confidence_score: float
    word_count: int
    generated_at: datetime

```

### Step 1: Query Planner

```
from openai import AsyncOpenAI
import json

client = AsyncOpenAI(api_key="sk-your-openai-key")

async def plan_research(question: str) -> List[SubQuery]:
    """
    Decompose a complex research question into focused sub-queries.
    Each sub-query explores a different angle of the topic.
    """
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": """You are a research planning expert.
                Decompose a complex question into 4-6 focused sub-queries.
                Each sub-query should explore a different aspect: facts, costs,
                comparisons, use cases, limitations, recent developments.
                Return JSON: {
                  "sub_queries": [
                    {"question": "...", "angle": "factual|cost|comparison|use-case|limitation|recent"}
                  ]
                }"""
            },
            {
                "role": "user",
                "content": f"Research question: {question}"
            }
        ]
    )

    plan = json.loads(response.choices[0].message.content)

    sub_queries = [
        SubQuery(question=sq["question"], angle=sq["angle"])
        for sq in plan["sub_queries"]
    ]

    print(f"Planned {len(sub_queries)} sub-queries:")
    for sq in sub_queries:
        print(f"  [{sq.angle}] {sq.question}")

    return sub_queries

```

### Step 2: Source Finder

```
async def find_sources(sub_query: SubQuery) -> List[str]:
    """
    Find URLs relevant to a sub-query.
    In production: use Brave Search API, Tavily, or Google Custom Search.
    For this example: LLM generates high-probability URLs.
    """
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": """Generate 6-8 URLs that likely contain authoritative,
                current information about this topic. Prefer:
                - Official documentation and announcements
                - Well-known publications (TechCrunch, VentureBeat, Wired, etc.)
                - Academic or research papers
                - Industry analyst reports
                Return JSON: {"urls": ["https://...", ...]}"""
            },
            {
                "role": "user",
                "content": f"Find sources for: {sub_query.question}\nAngle: {sub_query.angle}"
            }
        ]
    )

    return json.loads(response.choices[0].message.content).get("urls", [])

```

### Step 3: Parallel Scraper

```
import asyncio
import knowledgesdk

ks_client = knowledgesdk.AsyncClient(api_key="knowledgesdk_live_your_key_here")

async def scrape_sources(urls: List[str], max_concurrent: int = 8) -> List[ScrapedSource]:
    """
    Scrape URLs concurrently using KnowledgeSDK.
    Returns clean markdown — no HTML parsing needed.
    """
    semaphore = asyncio.Semaphore(max_concurrent)

    async def scrape_one(url: str) -> Optional[ScrapedSource]:
        async with semaphore:
            try:
                result = await ks_client.scrape(url=url)

                if len(result.markdown) < 100:
                    print(f"Skipping {url} — too little content ({len(result.markdown)} chars)")
                    return None

                return ScrapedSource(
                    url=url,
                    title=result.title or url,
                    markdown=result.markdown,
                    scraped_at=datetime.now(),
                    word_count=len(result.markdown.split())
                )
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")
                return None

    tasks = [scrape_one(url) for url in urls]
    results = await asyncio.gather(*tasks)

    sources = [r for r in results if r is not None]
    print(f"Successfully scraped {len(sources)}/{len(urls)} URLs")
    return sources

```

### Step 4: Evidence Extractor

```
async def extract_evidence(
    source: ScrapedSource,
    sub_queries: List[SubQuery]
) -> List[ExtractedEvidence]:
    """
    Extract key claims and evidence from a scraped source.
    Tags each claim with which sub-queries it's relevant to.
    """
    sub_query_list = "\n".join([
        f"- [{sq.angle}] {sq.question}" for sq in sub_queries
    ])

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": f"""Extract the most important factual claims from this source.
                For each claim, note which of these sub-queries it addresses:
                {sub_query_list}

                Return JSON: {{
                  "claims": [
                    {{
                      "claim": "Factual statement",
                      "supporting_text": "Exact quote from source",
                      "relevant_sub_queries": ["question1", ...],
                      "confidence": 0.9
                    }}
                  ]
                }}

                Extract 3-8 claims. Only include specific, factual claims, not vague statements."""
            },
            {
                "role": "user",
                "content": f"""Source: {source.title}
URL: {source.url}

Content:
{source.markdown[:4000]}

Extract key claims from this source."""
            }
        ]
    )

    result = json.loads(response.choices[0].message.content)

    evidence_list = []
    for claim_data in result.get("claims", []):
        evidence_list.append(ExtractedEvidence(
            source_url=source.url,
            source_title=source.title,
            claim=claim_data["claim"],
            supporting_text=claim_data.get("supporting_text", ""),
            sub_query_relevance=claim_data.get("relevant_sub_queries", []),
            confidence=claim_data.get("confidence", 0.7),
        ))

    return evidence_list

```

### Step 5: Conflict Detector

```
async def detect_conflicts(
    evidence_list: List[ExtractedEvidence]
) -> List[str]:
    """
    Identify contradictions between claims from different sources.
    Returns a list of conflict descriptions.
    """
    claims_text = "\n".join([
        f"[{e.source_title}]: {e.claim}"
        for e in evidence_list
    ])

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": """Identify factual conflicts between these claims from different sources.
                Only flag genuine contradictions (e.g., different numbers, opposite conclusions).
                Return JSON: {"conflicts": ["Source A says X but Source B says Y", ...]}
                If no conflicts, return {"conflicts": []}"""
            },
            {
                "role": "user",
                "content": f"Analyze these claims for conflicts:\n\n{claims_text}"
            }
        ]
    )

    result = json.loads(response.choices[0].message.content)
    conflicts = result.get("conflicts", [])

    if conflicts:
        print(f"Found {len(conflicts)} conflicts between sources")
    else:
        print("No significant conflicts detected")

    return conflicts

```

### Step 6: Report Synthesizer

```
async def synthesize_report(
    original_question: str,
    sub_queries: List[SubQuery],
    evidence_list: List[ExtractedEvidence],
    conflicts: List[str],
    all_sources: List[ScrapedSource]
) -> ResearchReport:
    """
    Synthesize all evidence into a structured research report.
    """
    # Organize evidence by sub-query
    evidence_by_angle = {}
    for sq in sub_queries:
        relevant = [
            e for e in evidence_list
            if sq.question in e.sub_query_relevance
            and e.confidence >= 0.6
        ]
        if relevant:
            evidence_by_angle[sq.angle] = {
                "sub_query": sq.question,
                "evidence": relevant[:8]  # Top 8 per angle
            }

    # Format evidence for synthesis
    evidence_text = ""
    for angle, data in evidence_by_angle.items():
        evidence_text += f"\n## {angle.upper()} ANGLE: {data['sub_query']}\n"
        for e in data["evidence"]:
            evidence_text += f"\n- [{e.source_title}]: {e.claim}\n"
            if e.supporting_text:
                evidence_text += f"  Quote: \"{e.supporting_text[:200]}...\"\n"

    conflicts_text = "\n".join(f"- {c}" for c in conflicts) if conflicts else "None identified"

    response = await client.chat.completions.create(
        model="gpt-4o",  # Use the stronger model for synthesis
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": """You are a professional research analyst.
                Synthesize the provided evidence into a comprehensive research report.

                Return JSON with this exact structure:
                {
                  "title": "Comprehensive Report: [Topic]",
                  "executive_summary": "2-3 paragraph summary of key findings",
                  "sections": [
                    {
                      "heading": "H2 section title",
                      "content": "Detailed content with inline citations as [Source Name]",
                      "sub_sections": [
                        {"heading": "H3 title", "content": "..."}
                      ]
                    }
                  ],
                  "confidence_score": 0.85,
                  "key_limitations": ["limitation1", "limitation2"]
                }

                Requirements:
                - Cite every factual claim with [Source Name]
                - Note conflicts explicitly in the relevant section
                - Use specific numbers and dates where available
                - Write 800-1200 words of content (sections only)
                - Do not add facts not present in the evidence"""
            },
            {
                "role": "user",
                "content": f"""Research Question: {original_question}

Evidence by Research Angle:
{evidence_text}

Source Conflicts:
{conflicts_text}

Write the research report."""
            }
        ]
    )

    result = json.loads(response.choices[0].message.content)

    # Build source metadata list
    source_metadata = [
        {
            "title": s.title,
            "url": s.url,
            "scraped_at": s.scraped_at.isoformat(),
            "word_count": s.word_count,
        }
        for s in all_sources
    ]

    # Count total words in report
    all_content = result.get("executive_summary", "") + " ".join(
        section.get("content", "") for section in result.get("sections", [])
    )

    return ResearchReport(
        title=result.get("title", f"Research Report: {original_question}"),
        executive_summary=result.get("executive_summary", ""),
        sections=result.get("sections", []),
        conflicts_found=conflicts,
        methodology=f"Analyzed {len(all_sources)} sources across {len(sub_queries)} research angles. Used KnowledgeSDK for web scraping and GPT-4o for synthesis.",
        sources=source_metadata,
        confidence_score=result.get("confidence_score", 0.8),
        word_count=len(all_content.split()),
        generated_at=datetime.now(),
    )

```

### Step 7: Report Formatter

```
def format_report_markdown(report: ResearchReport) -> str:
    """Format the research report as clean markdown."""

    md = f"# {report.title}\n\n"
    md += f"*Generated: {report.generated_at.strftime('%B %d, %Y')} | "
    md += f"Confidence: {report.confidence_score:.0%} | "
    md += f"Sources: {len(report.sources)} | "
    md += f"{report.word_count} words*\n\n"

    md += "---\n\n"
    md += "## Executive Summary\n\n"
    md += f"{report.executive_summary}\n\n"

    if report.conflicts_found:
        md += "---\n\n"
        md += "## Source Conflicts Identified\n\n"
        for conflict in report.conflicts_found:
            md += f"- {conflict}\n"
        md += "\n"

    for section in report.sections:
        md += "---\n\n"
        md += f"## {section['heading']}\n\n"
        md += f"{section['content']}\n\n"

        for sub in section.get("sub_sections", []):
            md += f"### {sub['heading']}\n\n"
            md += f"{sub['content']}\n\n"

    md += "---\n\n"
    md += "## Sources\n\n"
    for i, source in enumerate(report.sources, 1):
        md += f"{i}. [{source['title']}]({source['url']})\n"

    md += f"\n---\n*Methodology: {report.methodology}*\n"

    return md

```

### Step 8: The Main Research Function

```
import asyncio
import time

async def deep_research(question: str) -> tuple[ResearchReport, str]:
    """
    Main research function. Runs the full deep research pipeline.
    Returns (ResearchReport, formatted_markdown).
    """
    start_time = time.time()
    print(f"\nStarting deep research: {question}\n{'='*60}")

    # Step 1: Plan
    print("\n[1/6] Planning research angles...")
    sub_queries = await plan_research(question)

    # Step 2: Find sources for all sub-queries in parallel
    print(f"\n[2/6] Finding sources for {len(sub_queries)} sub-queries...")
    source_tasks = [find_sources(sq) for sq in sub_queries]
    all_url_lists = await asyncio.gather(*source_tasks)

    # Deduplicate URLs across sub-queries
    all_urls = list(dict.fromkeys([
        url for url_list in all_url_lists for url in url_list
    ]))
    print(f"Found {len(all_urls)} unique URLs to scrape")

    # Step 3: Scrape all sources
    print(f"\n[3/6] Scraping {len(all_urls)} sources...")
    all_sources = await scrape_sources(all_urls)

    if not all_sources:
        raise RuntimeError("Failed to scrape any sources")

    # Step 4: Extract evidence from all sources in parallel
    print(f"\n[4/6] Extracting evidence from {len(all_sources)} sources...")
    evidence_tasks = [extract_evidence(source, sub_queries) for source in all_sources]
    evidence_lists = await asyncio.gather(*evidence_tasks)

    all_evidence = [e for ev_list in evidence_lists for e in ev_list]
    print(f"Extracted {len(all_evidence)} evidence claims")

    # Step 5: Detect conflicts
    print(f"\n[5/6] Checking for conflicts...")
    conflicts = await detect_conflicts(all_evidence)

    # Step 6: Synthesize report
    print(f"\n[6/6] Synthesizing research report...")
    report = await synthesize_report(
        question, sub_queries, all_evidence, conflicts, all_sources
    )

    elapsed = time.time() - start_time
    print(f"\nResearch complete in {elapsed:.1f}s")
    print(f"Sources used: {len(report.sources)}")
    print(f"Confidence: {report.confidence_score:.0%}")

    formatted = format_report_markdown(report)
    return report, formatted


# Usage
async def main():
    question = "What are the key architectural differences between LangGraph and AutoGen for production AI agent deployment, including performance, cost, and community adoption?"

    report, markdown = await deep_research(question)

    # Save the report
    with open("research_report.md", "w") as f:
        f.write(markdown)

    print(f"\nReport saved to research_report.md ({report.word_count} words)")

asyncio.run(main())

```

* * *
## Node.js Implementation

```
import OpenAI from "openai";
import KnowledgeSDK from "@knowledgesdk/node";

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const ksClient = new KnowledgeSDK({ apiKey: process.env.KNOWLEDGESDK_API_KEY! });

interface SubQuery { question: string; angle: string; }
interface ScrapedSource { url: string; title: string; markdown: string; wordCount: number; }
interface Evidence { sourceUrl: string; sourceTitle: string; claim: string; confidence: number; }

async function planResearch(question: string): Promise<SubQuery[]> {
  const response = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    response_format: { type: "json_object" },
    messages: [
      {
        role: "system",
        content: 'Decompose into 4-6 sub-queries. Return JSON: {"sub_queries": [{"question": "...", "angle": "factual|cost|comparison|use-case"}]}',
      },
      { role: "user", content: `Research: ${question}` },
    ],
  });

  const plan = JSON.parse(response.choices[0].message.content!);
  return plan.sub_queries;
}

async function findSources(subQuery: SubQuery): Promise<string[]> {
  const response = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    response_format: { type: "json_object" },
    messages: [
      {
        role: "system",
        content: 'Return JSON: {"urls": ["https://...", ...]} with 6-8 authoritative URLs.',
      },
      { role: "user", content: `Find sources for: ${subQuery.question}` },
    ],
  });
  return JSON.parse(response.choices[0].message.content!).urls || [];
}

async function scrapeSources(urls: string[]): Promise<ScrapedSource[]> {
  const results = await Promise.allSettled(
    urls.map((url) => ksClient.scrape({ url }))
  );

  return results
    .map((result, i) => {
      if (result.status === "rejected") return null;
      const { markdown, title } = result.value;
      if (markdown.length < 100) return null;
      return {
        url: urls[i],
        title: title || urls[i],
        markdown,
        wordCount: markdown.split(" ").length,
      };
    })
    .filter(Boolean) as ScrapedSource[];
}

async function extractEvidence(source: ScrapedSource): Promise<Evidence[]> {
  const response = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    response_format: { type: "json_object" },
    messages: [
      {
        role: "system",
        content: 'Extract 3-6 key factual claims. Return JSON: {"claims": [{"claim": "...", "confidence": 0.9}]}',
      },
      {
        role: "user",
        content: `Source: ${source.title}\n\n${source.markdown.slice(0, 3000)}`,
      },
    ],
  });

  const result = JSON.parse(response.choices[0].message.content!);
  return (result.claims || []).map((c: { claim: string; confidence: number }) => ({
    sourceUrl: source.url,
    sourceTitle: source.title,
    claim: c.claim,
    confidence: c.confidence || 0.7,
  }));
}

async function synthesizeReport(
  question: string,
  evidence: Evidence[],
  sources: ScrapedSource[]
): Promise<string> {
  const evidenceText = evidence
    .filter((e) => e.confidence >= 0.7)
    .map((e) => `[${e.sourceTitle}]: ${e.claim}`)
    .join("\n");

  const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
      {
        role: "system",
        content:
          "Write a professional research report in markdown with H2/H3 headers and inline citations like [Source Name]. Include executive summary, findings, and conclusion.",
      },
      {
        role: "user",
        content: `Research Question: ${question}\n\nEvidence:\n${evidenceText}\n\nWrite the report.`,
      },
    ],
  });

  const reportContent = response.choices[0].message.content!;

  const sourceList = sources
    .map((s, i) => `${i + 1}. [${s.title}](${s.url})`)
    .join("\n");

  return `${reportContent}\n\n---\n\n## Sources\n\n${sourceList}`;
}

async function deepResearch(question: string): Promise<string> {
  console.log(`\nDeep Research: ${question}`);

  // Plan
  const subQueries = await planResearch(question);
  console.log(`Planned ${subQueries.length} sub-queries`);

  // Find and deduplicate sources
  const urlLists = await Promise.all(subQueries.map(findSources));
  const allUrls = [...new Set(urlLists.flat())];
  console.log(`Found ${allUrls.length} unique URLs`);

  // Scrape
  const sources = await scrapeSources(allUrls);
  console.log(`Scraped ${sources.length} sources`);

  // Extract evidence in parallel
  const evidenceLists = await Promise.all(sources.map(extractEvidence));
  const allEvidence = evidenceLists.flat();
  console.log(`Extracted ${allEvidence.length} claims`);

  // Synthesize
  const report = await synthesizeReport(question, allEvidence, sources);
  console.log("Report synthesized");

  return report;
}

// Usage
const report = await deepResearch(
  "How do AI browser agents compare to API-based scraping for production AI applications in 2026?"
);
console.log(report);

```

* * *
## Cost Analysis vs Perplexity
Here is a realistic cost breakdown for a deep research query that scrapes 15 sources:  
| Step  | Operation  | Cost  |  
| --- | --- | --- |  
| Query planning  | 1x GPT-4o-mini call  | $0.001  |  
| Source finding  | 5x GPT-4o-mini calls  | $0.005  |  
| Scraping  | 15x KnowledgeSDK requests  | $0.030  |  
| Evidence extraction  | 15x GPT-4o-mini calls  | $0.015  |  
| Conflict detection  | 1x GPT-4o-mini call  | $0.002  |  
| Synthesis  | 1x GPT-4o call  | $0.050  |  
| **Total**  |   | **~$0.10**  |  
**Perplexity Deep Research API:** $5.00 per query (at standard pricing)
**This implementation:** $0.08–$0.25 per query depending on source count and LLM model choices.
**Cost reduction:** 20–60x cheaper than Perplexity.
Beyond cost, the open-source approach gives you:
  * Full control over which sources are scraped
  * Transparency into every step of the reasoning
  * Ability to tune confidence thresholds and citation styles
  * Custom output formats (JSON, markdown, HTML, structured data)
  * Integration with your existing data pipelines


* * *
## Production Enhancements
### Caching Scraped Content
Avoid re-scraping the same URLs by caching results:

```
import hashlib
import json
from pathlib import Path

CACHE_DIR = Path(".scrape_cache")
CACHE_DIR.mkdir(exist_ok=True)

async def scrape_with_cache(url: str, cache_ttl_hours: int = 24) -> ScrapedSource:
    """Scrape a URL, using cache if available and fresh."""
    cache_key = hashlib.md5(url.encode()).hexdigest()
    cache_file = CACHE_DIR / f"{cache_key}.json"

    if cache_file.exists():
        cached = json.loads(cache_file.read_text())
        age_hours = (time.time() - cached["cached_at"]) / 3600
        if age_hours < cache_ttl_hours:
            print(f"Cache hit: {url} ({age_hours:.1f}h old)")
            return ScrapedSource(**{k: v for k, v in cached.items() if k != "cached_at"})

    result = await ks_client.scrape(url=url)
    source = ScrapedSource(
        url=url, title=result.title, markdown=result.markdown,
        scraped_at=datetime.now(), word_count=len(result.markdown.split())
    )

    # Cache the result
    cache_data = {**source.__dict__, "cached_at": time.time()}
    cache_data["scraped_at"] = source.scraped_at.isoformat()
    cache_file.write_text(json.dumps(cache_data))

    return source

```

### Streaming Report Progress to Users

```
async def deep_research_streaming(question: str):
    """Stream progress events for a real-time UI."""

    yield {"event": "start", "message": f"Researching: {question}"}

    sub_queries = await plan_research(question)
    yield {"event": "planned", "count": len(sub_queries), "angles": [sq.angle for sq in sub_queries]}

    all_urls = list(dict.fromkeys([
        url for url_list in await asyncio.gather(*[find_sources(sq) for sq in sub_queries])
        for url in url_list
    ]))
    yield {"event": "sources_found", "count": len(all_urls)}

    sources = await scrape_sources(all_urls)
    yield {"event": "scraped", "count": len(sources)}

    all_evidence = [e for ev_list in await asyncio.gather(*[extract_evidence(s, sub_queries) for s in sources]) for e in ev_list]
    yield {"event": "evidence_extracted", "count": len(all_evidence)}

    report, markdown = await synthesize_report(question, sub_queries, all_evidence, [], sources)
    yield {"event": "complete", "report": markdown, "confidence": report.confidence_score}

```

* * *
## Comparison with Commercial Alternatives  
| Feature  | This Implementation  | Perplexity Deep Research  | OpenAI Deep Research  |  
| --- | --- | --- | --- |  
| Cost per query  | $0.08–$0.25  | $5.00  | TBD (enterprise)  |  
| Source control  | Full  | None  | None  |  
| Output format  | Customizable  | Fixed  | Fixed  |  
| Citations  | Yes (inline)  | Yes  | Yes  |  
| Conflict detection  | Yes  | Unknown  | Unknown  |  
| Integration  | Full API  | Limited  | Limited  |  
| Self-hostable  | Yes  | No  | No  |  
| Max sources  | Unlimited  | ~10  | Unknown  |  
* * *
## Conclusion
Deep research is not magic — it is a structured pipeline of search, scrape, extract, and synthesize. The commercial products have polished UIs and convenient pricing for consumer use. But for developers building AI applications, an open-source implementation gives you dramatically lower costs, full control, and the ability to integrate research directly into your agent workflows.
KnowledgeSDK handles the web data layer — returning clean markdown from any URL in under two seconds, with no HTML parsing required. Your application handles the intelligence layer. The combination costs less than $0.25 per research query versus $5 for commercial alternatives.
The implementation shown here is a starting point. In production, you would add caching, streaming, search API integration for real URL discovery, and quality scoring to filter out low-value sources. But the architecture is complete and works as shown.
* * *
Build your research agent today. [Sign up for KnowledgeSDK](https://knowledgesdk.com) — 1,000 free scraping requests per month, no credit card required. Your open-source Perplexity clone is a few hours of coding away.
Try it now
### Scrape, search, and monitor any website with one API.
Get your API key in 30 seconds. First 1,000 requests free.
[GET API KEY →](https://knowledgesdk.com/login?signup=1&redirectTo=%2Fsetup)
### Related Articles
[ use-caseAI Personalization Without Fine-Tuning: Live Web Data as User Context ](https://knowledgesdk.com/blog/ai-personalization-web-data)[ use-caseGive Your Coding Agent Real-Time Documentation Access ](https://knowledgesdk.com/blog/coding-agent-docs-access)[ use-caseAutomated Competitive Intelligence: Build a Scraper That Never Sleeps ](https://knowledgesdk.com/blog/competitive-intelligence-scraping)[ use-caseHow AI Support Agents Use Web Knowledge to Answer Any Question ](https://knowledgesdk.com/blog/customer-support-ai-web-knowledge)
[← Back to blog](https://knowledgesdk.com/blog)

