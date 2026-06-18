# open-research-system — Phase 1 Research Spike Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the knowledge corpus for a source-of-truth on AI-assisted research — catalog the field (17 categories), gather best sources, synthesize, and graph-model it — so the eventual system architecture (Phase 2) emerges from evidence.

**Architecture:** A single content repo. `RESEARCH-CATALOG.md` is the contract (taxonomy + sources + phases). Two shell scripts feed the corpus: `scripts/ingest.sh` (markitdown convert local files) and `scripts/gather.sh` (drive the crawl4ai deep-research workflow per topic). Gathered material lands in `docs/NN-topic/`, gets distilled into `docs/findings/` + `SYNTHESIS.md`, then graphify produces the relational model (god nodes/nodes/edges). All context-heavy processing goes through context-mode; converted/gathered bytes never enter the working context raw.

**Tech Stack:** Markdown, Bash, `markitdown` CLI (`~/.local/bin/markitdown`, prints to stdout by default), crawl4ai helpers (`~/.venvs/crawl4ai/bin/python` + `search.py` → `[{url,title,snippet}]` JSON + `fetch_md.py` → markdown stdout), graphify skill (`/graphify <path>`), context-mode MCP. Script tests use a **plain-bash assert harness** (no `bats` dependency — it is not installed). Python 3.12 available via the crawl4ai venv.

**Cross-check status (verified 2026-06-17):** all tool paths exist; `bats` MISSING (tests use plain bash); gather fetch logic uses a helper file `scripts/_fetch_results.py` (no heredoc/stdin collision).

**Reference:** Sibling repo `/Users/joshua/Documents/GitHub/open-job-system` for tone/shape of `RESEARCH-CATALOG.md`, `GRAPH_REPORT.md`, topic dirs.

**Spec:** `docs/superpowers/specs/2026-06-17-open-research-system-design.md`

---

## File Structure

**Created:**
- `README.md` — repo purpose, spike status, navigation
- `.gitignore` — ignore `.graphify/` caches, `.DS_Store`, ingest binaries
- `RESEARCH-CATALOG.md` — 17-category taxonomy + sources + research phases
- `SYNTHESIS.md` — cross-topic distilled findings (grows during spike)
- `ingest/.gitkeep` — drop-zone for local files
- `docs/01-methodology-epistemics/README.md` … `docs/17-specs-standards/README.md` — 17 topic dirs, each with a stub README defining scope + a `sources/` subdir
- `docs/findings/.gitkeep` — per-topic synthesized findings
- `docs/diagrams/.gitkeep`
- `scripts/ingest.sh` — markitdown wrapper
- `scripts/gather.sh` — crawl4ai workflow wrapper
- `scripts/_fetch_results.py` — fetch each search result URL → markdown (called by gather.sh)
- `scripts/lib.sh` — shared helpers (slugify, topic-dir resolution)
- `tests/test_ingest.sh`, `tests/test_gather.sh`, `tests/test_catalog.sh` — plain-bash script + structural tests
- `graphify-out/.gitkeep` — graphify report destination

**Note on commits:** This repo's owner commits only when asked, but this plan is itself the authorization to commit per-task (frequent small commits). Use Conventional Commits, selective staging (never `git add -A`). No co-author trailer.

---

## Task 1: Repo scaffolding

**Files:**
- Create: `.gitignore`, `README.md`, `ingest/.gitkeep`, `docs/findings/.gitkeep`, `docs/diagrams/.gitkeep`, `graphify-out/.gitkeep`
- Create: `tests/test_catalog.sh` (structure linter, used now + later)

- [ ] **Step 1: Write the structure linter test (failing)**

Create `tests/test_catalog.sh`:

```bash
#!/usr/bin/env bash
# Structural lint for the spike repo. Exit non-zero on any missing piece.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0
check() { if eval "$2"; then echo "ok: $1"; else echo "MISS: $1"; fail=1; fi; }

# Top-level files
for f in README.md .gitignore RESEARCH-CATALOG.md SYNTHESIS.md; do
  check "$f exists" "[ -f '$ROOT/$f' ]"
done

# Required dirs
for d in ingest docs docs/findings docs/diagrams scripts graphify-out tests; do
  check "$d/ exists" "[ -d '$ROOT/$d' ]"
done

# 17 topic dirs
topics=(01-methodology-epistemics 02-statistical-causal-inference 03-decision-frameworks \
04-applied-research-playbooks 05-ai-deep-research-systems 06-rag-retrieval \
07-agentic-orchestration 08-grounding-truth 09-knowledge-compilation-graphs \
10-context-prompt-engineering 11-research-pipeline-engineering 12-tooling-landscape \
13-reference-systems-case-studies 14-papers 15-textbooks-longform \
16-evaluation-benchmarks 17-specs-standards)
for t in "${topics[@]}"; do
  check "docs/$t/README.md" "[ -f '$ROOT/docs/$t/README.md' ]"
  check "docs/$t/sources/" "[ -d '$ROOT/docs/$t/sources' ]"
done

# RESEARCH-CATALOG must reference all 17 topic slugs
if [ -f "$ROOT/RESEARCH-CATALOG.md" ]; then
  for t in "${topics[@]}"; do
    check "catalog mentions $t" "grep -q '$t' '$ROOT/RESEARCH-CATALOG.md'"
  done
fi

[ "$fail" -eq 0 ] && echo "ALL OK" || echo "LINT FAILED"
exit "$fail"
```

- [ ] **Step 2: Run it to verify it fails**

Run: `bash tests/test_catalog.sh`
Expected: many `MISS:` lines, ends `LINT FAILED`, exit 1.

- [ ] **Step 3: Create `.gitignore`**

```gitignore
.DS_Store
.graphify/
graphify-out/cache/
ingest/*
!ingest/.gitkeep
*.pdf
*.docx
*.xlsx
*.pptx
```

- [ ] **Step 4: Create `README.md`**

```markdown
# open-research-system

Definitive source-of-truth for **AI-assisted research → decisions → actionable knowledge**.

> **Status:** Phase 1 — research spike. Cataloging the field, gathering sources,
> synthesizing. The system itself (template, scaffolder, agents) is Phase 2, built
> from what this spike learns. Sibling repo: `open-job-system`.

## Layout
- `RESEARCH-CATALOG.md` — the 17-category taxonomy, sources to mine, research phases.
- `docs/NN-topic/` — gathered source material per category.
- `docs/findings/` — synthesized, cited findings.
- `SYNTHESIS.md` — cross-topic distillation.
- `ingest/` — drop local files (PDF/docx/…); `scripts/ingest.sh` converts them.
- `scripts/gather.sh` — drives the crawl4ai deep-research workflow per topic.
- `graphify-out/` — relational model of the corpus (god nodes/nodes/edges).

## Quickstart
1. Drop files into `ingest/`, run `scripts/ingest.sh`.
2. Gather a topic: `scripts/gather.sh 06-rag-retrieval "advanced RAG architectures 2025"`.
3. Synthesize into `docs/findings/` and `SYNTHESIS.md`.
4. Run graphify; review `graphify-out/GRAPH_REPORT.md`.
```

- [ ] **Step 5: Create placeholder keeps and empty SYNTHESIS**

```bash
mkdir -p ingest docs/findings docs/diagrams scripts graphify-out tests
touch ingest/.gitkeep docs/findings/.gitkeep docs/diagrams/.gitkeep graphify-out/.gitkeep
printf '# Synthesis\n\n_Cross-topic distilled findings. Populated during the spike._\n' > SYNTHESIS.md
```

- [ ] **Step 6: Create the 17 topic dirs with stub READMEs**

For each topic slug, create `docs/<slug>/sources/.gitkeep` and `docs/<slug>/README.md` using this template (fill `<TITLE>` and `<ONE-LINE SCOPE>` from Task 2's catalog content):

```markdown
# <TITLE>

**Scope:** <ONE-LINE SCOPE>

**Status:** not started · breadth-scan · deep-dive · synthesized

## Sub-topics
- (filled from RESEARCH-CATALOG.md)

## Sources gathered
- (links + `sources/` files appear here as gathered)

## Key findings
- (promoted to `docs/findings/` when synthesized)
```

- [ ] **Step 7: Re-run linter (topic checks pass, catalog checks still fail)**

Run: `bash tests/test_catalog.sh`
Expected: all dir/topic `ok:`; `MISS: RESEARCH-CATALOG.md exists` + `catalog mentions …` still fail (catalog written in Task 2).

- [ ] **Step 8: Commit**

```bash
git add .gitignore README.md SYNTHESIS.md ingest/.gitkeep docs tests/test_catalog.sh graphify-out/.gitkeep
git commit -m "feat: scaffold research-spike repo structure"
```

---

## Task 2: RESEARCH-CATALOG.md (the contract)

**Files:**
- Create: `RESEARCH-CATALOG.md`

- [ ] **Step 1: Write the catalog**

Create `RESEARCH-CATALOG.md`. Use this exact skeleton; each category MUST have **Scope**, **Sub-topics**, **Sources to mine**, **Priority** (P0 core / P1 / P2). Real seed sources are given — add more during the breadth scan.

````markdown
# open-research-system — Research Catalog

**Purpose:** Taxonomy of the field "how to do AI-assisted research → decisions →
actionable knowledge", the sources to mine per area, and the phased research plan.
This is the contract the spike executes against. Topic slugs match `docs/NN-*` dirs.

## Categories

### 01-methodology-epistemics  (P0)
**Scope:** How research itself should be done (human + AI): framing → search → eval →
synthesis → verification, including primary/qualitative methods.
**Sub-topics:** question/objective framing; search strategy & query formulation; source
credibility/authority/currency; bias detection; claim extraction & cross-referencing;
synthesis & sense-making; verification/contradiction resolution; confidence/evidence
weighting; primary & qualitative methods (interviews, surveys, ethnography, sampling,
triangulation); knowledge management (Zettelkasten, evergreen notes).
**Sources to mine:** Booth "Craft of Research"; Cochrane Handbook (systematic review);
PRISMA; "How to Read a Paper" (Greenhalgh); Zettelkasten / Ahrens "How to Take Smart
Notes"; Andy Matuschak evergreen notes.
**Priority:** P0

### 02-statistical-causal-inference  (P1)
**Scope:** Quantitative spine for defensible decisions.
**Sub-topics:** significance/p-values & misconceptions; effect size; confidence
intervals; Bayesian vs frequentist; hypothesis testing; regression; time-series;
causal inference; experimental design & power analysis; Monte Carlo.
**Sources to mine:** Gelman "Statistical Rethinking"/McElreath; Pearl "Book of Why";
"Statistics Done Wrong"; Cohen power analysis; ASA statement on p-values.
**Priority:** P1

### 03-decision-frameworks  (P0)
**Scope:** Turning findings into recorded, defensible decisions.
**Sub-topics:** MADR/ADR; decision matrices (weighted criteria); Analysis of Competing
Hypotheses (ACH); cost-benefit; SWOT; risk modeling; stress/scenario/sensitivity
analysis; go/no-go & ship/no-ship gates.
**Sources to mine:** MADR (adr.github.io / madr.dev); Michael Nygard "Documenting
Architecture Decisions"; Heuer "Psychology of Intelligence Analysis" (ACH); decision
matrix / Pugh matrix references.
**Priority:** P0

### 04-applied-research-playbooks  (P2)
**Scope:** Concrete research genres with their own methods.
**Sub-topics:** competitive teardown; market/TAM sizing; trend & weak-signal detection;
cohort/retention; A/B experimentation; idea validation; SEO/intent; systematic
literature review.
**Sources to mine:** Porter "Competitive Strategy"; "Lean Analytics"; Trustworthy
Online Controlled Experiments (Kohavi); jobs-to-be-done literature.
**Priority:** P2

### 05-ai-deep-research-systems  (P0)
**Scope:** Existing AI systems that do research end-to-end — to teardown.
**Sub-topics:** deep-research agents (OpenAI/Google/Anthropic Deep Research); STORM
(Stanford); GPT-Researcher; Perplexity / Elicit-class; open-source clones & their
architectures.
**Sources to mine:** STORM paper + repo (stanford-oval/storm); GPT-Researcher
(assafelovic/gpt-researcher); OpenAI/Google/Anthropic Deep Research write-ups; Elicit
methodology posts.
**Priority:** P0

### 06-rag-retrieval  (P0)
**Scope:** Retrieval architectures powering research systems.
**Sub-topics:** naive→advanced RAG; GraphRAG; agentic RAG; embeddings; vector stores;
hybrid (BM25 + dense) search; rerankers; chunking; context management.
**Sources to mine:** Microsoft GraphRAG (paper + repo); "Retrieval-Augmented
Generation" (Lewis 2020); Anthropic Contextual Retrieval; LlamaIndex/LangChain RAG
docs; reranker papers (Cohere/ColBERT).
**Priority:** P0

### 07-agentic-orchestration  (P0)
**Scope:** Coordinating agents/loops to execute research.
**Sub-topics:** planner-worker; fan-out/verify; debate/critique loops; multi-agent
patterns; loop-engineering (iterate-until-dry); reward/policy design (RL: exploration,
PPO/offline/inverse); shared context/state stores; orchestration patterns
(sequential/parallel/pipeline/map-reduce/hierarchical).
**Sources to mine:** Anthropic "Building effective agents" + multi-agent research
system post; LangGraph docs; AutoGen; ReAct paper; Reflexion; CRAG; Self-RAG.
**Priority:** P0

### 08-grounding-truth  (P0)
**Scope:** Making outputs faithful and checkable.
**Sub-topics:** citation/attribution; hallucination mitigation; LLM-as-judge;
evaluation of research outputs; faithfulness metrics; research-output quality/style
auditing (anti-AI-isms).
**Sources to mine:** "LLM-as-a-judge" survey; RAGAS; TruLens; FActScore; attribution
papers (RARR); Anthropic/OpenAI eval cookbooks.
**Priority:** P0

### 09-knowledge-compilation-graphs  (P0)
**Scope:** Turning findings into a queryable source-of-truth.
**Sub-topics:** source-of-truth maintenance; normative docs; knowledge-graph
construction (god nodes / nodes / edges); community detection & centrality; synthesis→
decision pipelines; retrieval-optimized knowledge stores.
**Sources to mine:** graphify skill (`~/.claude/skills/graphify`); GraphRAG community
detection; knowledge-graph construction surveys; PKG / Roam/Obsidian graph models.
**Priority:** P0

### 10-context-prompt-engineering  (P1)
**Scope:** Prompt/context techniques for research tasks.
**Sub-topics:** context engineering; CoT/ToT/ReAct; constitutional/role-based;
long-context vs RAG trade-offs; token/context compression; output parsing.
**Sources to mine:** Anthropic prompt engineering + context engineering guides; "Chain
of Thought" (Wei); "Tree of Thoughts"; DSPy.
**Priority:** P1

### 11-research-pipeline-engineering  (P2)
**Scope:** Ops layer for repeatable research pipelines.
**Sub-topics:** data pipelines/ETL; experiment tracking; model registry/lineage; drift
& retraining; reproducibility infra.
**Sources to mine:** "Designing Data-Intensive Applications" (relevant chapters);
MLflow/W&B docs; dvc; reproducibility checklists.
**Priority:** P2

### 12-tooling-landscape  (P1)
**Scope:** Frameworks and tools to build with.
**Sub-topics:** orchestration frameworks (LangGraph, LlamaIndex, DSPy, AutoGen); search
APIs; scrapers (crawl4ai); converters (markitdown); MCP / agent-tool integration.
**Sources to mine:** crawl4ai (unclecode/crawl4ai); markitdown (microsoft/markitdown);
MCP spec (modelcontextprotocol.io); LangGraph/LlamaIndex/DSPy docs.
**Priority:** P1

### 13-reference-systems-case-studies  (P1)
**Scope:** Concrete systems to teardown beyond #5.
**Sub-topics:** open-source research agents; production write-ups; postmortems.
**Sources to mine:** engineering blogs (Anthropic, Perplexity); notable GitHub repos.
**Priority:** P1

### 14-papers  (P1)
**Scope:** Canonical papers underpinning the field.
**Sub-topics:** RAG, agents, retrieval, eval, KG papers.
**Sources to mine:** arXiv (RAG/agents/eval); collect per-topic during deep dives.
**Priority:** P1

### 15-textbooks-longform  (P2)
**Scope:** Long-form references for depth.
**Sub-topics:** research methods texts; ML/IR textbooks.
**Sources to mine:** "Introduction to Information Retrieval" (Manning); research-methods
textbooks.
**Priority:** P2

### 16-evaluation-benchmarks  (P1)
**Scope:** How research-system quality is measured.
**Sub-topics:** research-QA benchmarks; faithfulness/groundedness metrics; agent
benchmarks.
**Sources to mine:** RAGAS; TruthfulQA; HotpotQA / multi-hop QA; GAIA; BrowseComp.
**Priority:** P1

### 17-specs-standards  (P2)
**Scope:** Interop & format standards.
**Sub-topics:** citation formats (BibTeX/CSL); schema.org; ADR formats; MCP schema.
**Sources to mine:** CSL spec; schema.org; MADR schema; MCP spec.
**Priority:** P2

## Research Phases
1. **Breadth scan** — one gather pass per category (P0 first), capture canonical sources.
2. **Deep dives** — P0 categories full-text gather + ingest (start: 05, 06, 07, 09).
3. **Synthesize** — per-topic findings → `docs/findings/`, roll up into `SYNTHESIS.md`.
4. **Graph** — graphify the corpus, surface god nodes, flag gaps, re-scan as needed.
````

- [ ] **Step 2: Back-fill each topic README's Sub-topics from the catalog**

For each `docs/<slug>/README.md`, copy that category's Sub-topics line into the "Sub-topics" section and set the Scope.

- [ ] **Step 3: Run the linter — all pass**

Run: `bash tests/test_catalog.sh`
Expected: every line `ok:`, ends `ALL OK`, exit 0.

- [ ] **Step 4: Commit**

```bash
git add RESEARCH-CATALOG.md docs
git commit -m "feat: add 17-category research catalog and topic stubs"
```

---

## Task 3: `scripts/ingest.sh` (markitdown wrapper)

**Files:**
- Create: `scripts/lib.sh`, `scripts/ingest.sh`, `tests/test_ingest.sh`

- [ ] **Step 1: Write `scripts/lib.sh` (shared helpers)**

```bash
#!/usr/bin/env bash
# Shared helpers for spike scripts.
set -euo pipefail

slugify() { echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'; }

# Resolve a topic arg (slug or NN prefix) to its docs dir; echo path or exit 1.
resolve_topic_dir() {
  local root="$1" arg="$2" match
  match=$(find "$root/docs" -maxdepth 1 -type d -name "*${arg}*" | grep -E '/[0-9]{2}-' | head -1)
  [ -n "$match" ] || { echo "no topic dir matches '$arg'" >&2; return 1; }
  echo "$match"
}

MARKITDOWN="${MARKITDOWN:-$HOME/.local/bin/markitdown}"
```

- [ ] **Step 2: Write the failing plain-bash test**

Create `tests/test_ingest.sh`:

```bash
#!/usr/bin/env bash
# Plain-bash test harness for ingest.sh (no bats dependency).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
pass=0; fail=0
ok(){ echo "ok: $1"; pass=$((pass+1)); }
no(){ echo "FAIL: $1"; fail=$((fail+1)); }

# Case 1: errors with no files in ingest/
TMP="$(mktemp -d)"; mkdir -p "$TMP/ingest" "$TMP/docs/06-rag-retrieval/sources"
touch "$TMP/ingest/.gitkeep"
out="$(env REPO_ROOT="$TMP" bash "$ROOT/scripts/ingest.sh" 2>&1)"; rc=$?
{ [ "$rc" -ne 0 ] && [[ "$out" == *"no files"* ]]; } && ok "errors with empty ingest" || no "should error on empty ingest (rc=$rc out=$out)"
rm -rf "$TMP"

# Case 2: converts a file into the target topic's sources/
TMP="$(mktemp -d)"; mkdir -p "$TMP/ingest" "$TMP/docs/06-rag-retrieval/sources"
printf 'hello world' > "$TMP/ingest/note.md"
out="$(env REPO_ROOT="$TMP" MARKITDOWN="cat" bash "$ROOT/scripts/ingest.sh" 06-rag-retrieval 2>&1)"; rc=$?
{ [ "$rc" -eq 0 ] && [ -f "$TMP/docs/06-rag-retrieval/sources/note.md" ]; } && ok "converts into topic sources" || no "should write note.md (rc=$rc out=$out)"
rm -rf "$TMP"

echo "--- ingest: $pass passed, $fail failed ---"
[ "$fail" -eq 0 ]
```

- [ ] **Step 3: Run it to verify it fails**

Run: `bash tests/test_ingest.sh`
Expected: both cases `FAIL` — `scripts/ingest.sh` does not exist yet.

- [ ] **Step 4: Write `scripts/ingest.sh`**

```bash
#!/usr/bin/env bash
# Convert every file in ingest/ to markdown via markitdown, into a topic's sources/.
# Usage: ingest.sh [topic]   (topic defaults to docs/findings staging if omitted)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ROOT="${REPO_ROOT:-$(cd "$HERE/.." && pwd)}"

shopt -s nullglob
files=("$ROOT"/ingest/*)
real=(); for f in "${files[@]}"; do [ "$(basename "$f")" = ".gitkeep" ] || real+=("$f"); done
[ "${#real[@]}" -gt 0 ] || { echo "no files in ingest/" >&2; exit 1; }

if [ "${1:-}" ]; then dest="$(resolve_topic_dir "$ROOT" "$1")/sources"; else dest="$ROOT/docs/findings"; fi
mkdir -p "$dest"

for f in "${real[@]}"; do
  base="$(basename "${f%.*}")"
  # markitdown prints markdown to stdout; redirect to the destination. stderr carries
  # a harmless pydub/ffmpeg warning we discard.
  "$MARKITDOWN" "$f" > "$dest/${base}.md" 2>/dev/null
  echo "ingested: $f -> $dest/${base}.md"
done
echo "Done. Index with context-mode before reading; do not raw-read."
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `bash tests/test_ingest.sh`
Expected: `ingest: 2 passed, 0 failed`, exit 0. (Test stubs `MARKITDOWN=cat` so no real markitdown needed.)

- [ ] **Step 6: Commit**

```bash
git add scripts/lib.sh scripts/ingest.sh tests/test_ingest.sh
git commit -m "feat: add markitdown ingest script with tests"
```

---

## Task 4: `scripts/gather.sh` (crawl4ai workflow wrapper)

**Files:**
- Create: `scripts/_fetch_results.py`, `scripts/gather.sh`, `tests/test_gather.sh`

- [ ] **Step 1: Write the fetch helper `scripts/_fetch_results.py`**

A real file (not an inline heredoc) — reads the search-results JSON from a path arg and
fetches each URL to markdown. Runs under the crawl4ai venv python, so `sys.executable`
is that interpreter; `fetch_md.py` is invoked with it.

```python
#!/usr/bin/env python
"""Fetch each search result to markdown. Usage: _fetch_results.py <search.json> <out_dir> <fetch_md.py>"""
import json, sys, subprocess, re, pathlib

search_json, out_dir, fetch = sys.argv[1], sys.argv[2], sys.argv[3]
py = sys.executable
data = json.loads(pathlib.Path(search_json).read_text())
for r in data:
    url = r.get("url")
    if not url:
        continue
    slug = re.sub(r"[^a-z0-9]+", "-", (r.get("title") or url).lower())[:60].strip("-") or "src"
    dest = pathlib.Path(out_dir) / f"{slug}.md"
    try:
        md = subprocess.run([py, fetch, url], capture_output=True, text=True, timeout=120).stdout
        dest.write_text(f"# {r.get('title','')}\n\nSource: {url}\n\n{md}")
        print(f"fetched: {url} -> {dest}")
    except Exception as e:  # noqa: BLE001 - log and continue per-URL
        print(f"FAIL {url} {e}", file=sys.stderr)
```

- [ ] **Step 2: Write the failing plain-bash test**

Create `tests/test_gather.sh`:

```bash
#!/usr/bin/env bash
# Plain-bash test harness for gather.sh (no bats dependency).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
pass=0; fail=0
ok(){ echo "ok: $1"; pass=$((pass+1)); }
no(){ echo "FAIL: $1"; fail=$((fail+1)); }

mkroot(){ local t; t="$(mktemp -d)"; mkdir -p "$t/docs/06-rag-retrieval/sources"; echo "$t"; }

# Case 1: errors without a query
TMP="$(mkroot)"
out="$(env REPO_ROOT="$TMP" bash "$ROOT/scripts/gather.sh" 06-rag-retrieval 2>&1)"; rc=$?
{ [ "$rc" -ne 0 ] && [[ "$out" == *"query"* ]]; } && ok "errors without query" || no "should error w/o query (rc=$rc out=$out)"
rm -rf "$TMP"

# Case 2: errors on unknown topic
TMP="$(mkroot)"
out="$(env REPO_ROOT="$TMP" bash "$ROOT/scripts/gather.sh" 99-nope "q" 2>&1)"; rc=$?
{ [ "$rc" -ne 0 ] && [[ "$out" == *"no topic dir"* ]]; } && ok "errors on unknown topic" || no "should error unknown topic (rc=$rc out=$out)"
rm -rf "$TMP"

# Case 3: dry-run prints the search command for a valid topic+query (no network)
TMP="$(mkroot)"
out="$(env REPO_ROOT="$TMP" DRY_RUN=1 bash "$ROOT/scripts/gather.sh" 06-rag-retrieval "advanced RAG" 2>&1)"; rc=$?
{ [ "$rc" -eq 0 ] && [[ "$out" == *"search.py"* ]] && [[ "$out" == *"advanced RAG"* ]]; } && ok "dry-run prints search cmd" || no "dry-run failed (rc=$rc out=$out)"
rm -rf "$TMP"

echo "--- gather: $pass passed, $fail failed ---"
[ "$fail" -eq 0 ]
```

- [ ] **Step 3: Run it to verify it fails**

Run: `bash tests/test_gather.sh`
Expected: cases FAIL — `scripts/gather.sh` does not exist yet.

- [ ] **Step 4: Write `scripts/gather.sh`**

```bash
#!/usr/bin/env bash
# Gather sources for a topic via crawl4ai (search + fetch), off the harness web path.
# Usage: gather.sh <topic> "<query>"
# Env: DRY_RUN=1 prints commands instead of running. N=<int> results (default 8).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ROOT="${REPO_ROOT:-$(cd "$HERE/.." && pwd)}"

topic="${1:-}"; query="${2:-}"
[ -n "$topic" ] || { echo "usage: gather.sh <topic> <query>" >&2; exit 2; }
dir="$(resolve_topic_dir "$ROOT" "$topic")" || exit 1
[ -n "$query" ] || { echo "missing query" >&2; exit 2; }

N="${N:-8}"
PY="$HOME/.venvs/crawl4ai/bin/python"
SEARCH="$HOME/.venvs/crawl4ai/search.py"
FETCH="$HOME/.venvs/crawl4ai/fetch_md.py"
out="$dir/sources"; mkdir -p "$out"
search_cmd="$PY $SEARCH \"$query\" $N"

if [ "${DRY_RUN:-}" = "1" ]; then
  echo "would run: $search_cmd"
  echo "would fetch each result via: $PY $HERE/_fetch_results.py <search.json> $out $FETCH"
  exit 0
fi

echo "searching: $query"
results_file="$out/_search_$(slugify "$query").json"
"$PY" "$SEARCH" "$query" "$N" > "$results_file"
# Fetch each URL to markdown via the helper file (no stdin/heredoc collision).
# Large output stays on disk — index with context-mode, do not raw-read.
"$PY" "$HERE/_fetch_results.py" "$results_file" "$out" "$FETCH"
echo "Gathered into $out. Index with context-mode; synthesize into docs/findings/."
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `bash tests/test_gather.sh`
Expected: `gather: 3 passed, 0 failed`, exit 0 (dry-run + error paths need no network).

- [ ] **Step 6: Commit**

```bash
git add scripts/_fetch_results.py scripts/gather.sh tests/test_gather.sh
git commit -m "feat: add crawl4ai gather script with tests"
```

---

## Task 5: Execute the breadth scan (P0 categories)

This task produces real gathered content. It is procedural, not TDD — verification is presence + a context-mode index, never raw-reading gathered bytes into context.

**Files:**
- Modify: `docs/05-…`, `docs/06-…`, `docs/07-…`, `docs/08-…`, `docs/09-…` (P0) `sources/` + README status

- [ ] **Step 1: Gather each P0 topic**

For topics `05-ai-deep-research-systems 06-rag-retrieval 07-agentic-orchestration 08-grounding-truth 09-knowledge-compilation-graphs`, run a gather using the catalog's "Sources to mine" as query seeds, e.g.:

```bash
scripts/gather.sh 05-ai-deep-research-systems "STORM Stanford GPT-Researcher deep research agent architecture"
scripts/gather.sh 06-rag-retrieval "advanced RAG GraphRAG agentic RAG hybrid search reranking 2025"
scripts/gather.sh 07-agentic-orchestration "building effective agents multi-agent research planner worker ReAct Reflexion"
scripts/gather.sh 08-grounding-truth "LLM as judge RAGAS faithfulness citation attribution hallucination evaluation"
scripts/gather.sh 09-knowledge-compilation-graphs "knowledge graph construction GraphRAG community detection centrality"
```

- [ ] **Step 2: Index gathered output via context-mode**

For each topic's `sources/`, index it so it's searchable without raw reads:

```
ctx_index path="docs/06-rag-retrieval/sources"
```
(repeat per P0 topic). Verify with a `ctx_search` query per topic.

- [ ] **Step 3: Update each P0 topic README**

Set `**Status:** breadth-scan`, list the gathered source links under "Sources gathered" (titles + URLs, pulled from the `_search_*.json` — process with `ctx_execute_file`, do not paste raw page bodies).

- [ ] **Step 4: Commit (per topic, keep diffs small)**

```bash
git add docs/06-rag-retrieval
git commit -m "research: breadth-scan gather for rag-retrieval"
```
Repeat for each P0 topic.

- [ ] **Step 5: Repeat breadth scan for P1/P2 topics**

Same procedure for the remaining 12 categories, one commit each. P1 before P2.

---

## Task 6: Synthesize findings

**Files:**
- Create: `docs/findings/<slug>.md` per scanned topic
- Modify: `SYNTHESIS.md`

- [ ] **Step 1: Per-topic finding doc**

For each scanned topic, create `docs/findings/<slug>.md` using context-mode over that topic's indexed sources (derive the answer; never raw-read). Template:

```markdown
# Findings — <TITLE>

**Question:** what does this category teach for building a research system?

## Key claims (cited)
- <claim> — [source title](url)

## Convergent vs contested
- Convergent: …
- Contested / open: …

## Implications for the system (Phase 2)
- …

## Gaps found → re-scan
- …
```

- [ ] **Step 2: Roll up into SYNTHESIS.md**

Replace `SYNTHESIS.md` body with cross-topic distillation: the load-bearing patterns that recur across categories (e.g. retrieve→verify→synthesize loops, citation-first generation, graph-structured knowledge), each linking to the per-topic finding docs.

- [ ] **Step 3: Commit**

```bash
git add docs/findings SYNTHESIS.md
git commit -m "research: synthesize per-topic findings and cross-topic distillation"
```

---

## Task 7: graphify the corpus

**Files:**
- Create: `graphify-out/GRAPH_REPORT.md` (generated)

- [ ] **Step 1: Run graphify over the repo**

graphify is a Claude Code **skill**, not a CLI. Invoke it on the repo root with the
directed flag so edge direction (source→target) is preserved for the relational model:

```
/graphify . --directed
```

It ingests `RESEARCH-CATALOG.md`, `docs/`, `SYNTHESIS.md` and builds the graph (nodes =
topics/sources/findings; edges = cites/supports/informs; god nodes via community
detection + centrality). Outputs land in `.graphify/` (caches, gitignored) and
`graphify-out/` incl. `GRAPH_REPORT.md` (committed).

- [ ] **Step 2: Verify god nodes surfaced**

Open `graphify-out/GRAPH_REPORT.md`; confirm it names god nodes (the highest-centrality concepts/sources). Query the graph for "what do most findings reference?" to sanity-check.

- [ ] **Step 3: Record graph read in SYNTHESIS.md**

Add a "Graph reading" section to `SYNTHESIS.md`: list the god nodes and what their centrality implies for Phase-2 architecture (the load-bearing concepts the system must be built around).

- [ ] **Step 4: Commit**

```bash
git add graphify-out/GRAPH_REPORT.md SYNTHESIS.md
git commit -m "research: graphify corpus and record god-node reading"
```

---

## Task 8: Phase-2 requirements seed

**Files:**
- Create: `docs/PHASE-2-REQUIREMENTS.md`

- [ ] **Step 1: Distill requirements from the synthesis**

Create `docs/PHASE-2-REQUIREMENTS.md`: a short, evidence-backed list of what the real research system must do, each requirement citing the finding(s) that justify it. Revisit Appendix A of the spec (working hypothesis) and mark each item confirmed / revised / dropped based on the spike.

```markdown
# Phase 2 — Requirements (seeded from the spike)

## Confirmed by evidence
- <requirement> — basis: docs/findings/<slug>.md

## Revised from the working hypothesis
- <hypothesis item> → <revision> — basis: …

## Dropped
- <item> — why

## Open questions for Phase-2 brainstorming
- …
```

- [ ] **Step 2: Run the structure linter once more**

Run: `bash tests/test_catalog.sh`
Expected: `ALL OK`, exit 0.

- [ ] **Step 3: Commit**

```bash
git add docs/PHASE-2-REQUIREMENTS.md
git commit -m "docs: seed Phase 2 requirements from spike findings"
```

---

## Self-Review

**Spec coverage:**
- §3 layout → Task 1 (scaffold) + Task 2 (catalog). ✓
- §4 17 categories → Task 2 catalog + topic READMEs. ✓
- §5 gather engine (crawl4ai + markitdown + context-mode) → Task 3 (ingest) + Task 4 (gather) + Task 5 (execute, with context-mode indexing). ✓
- §6 synthesis & graph → Task 6 + Task 7. ✓
- §7 research phases → Task 5 (breadth/deep) + Task 6 + Task 7. ✓
- §8 DoD → Task 2 (catalog), Task 5 (breadth scan), Task 6 (synthesis), Task 7 (graphify god nodes), Task 8 (phase-2 seed). ✓

**Placeholder scan:** Content tasks (5–8) are inherently generative; each gives exact procedure, real query seeds, and concrete templates with verification — no "TBD"/"handle edge cases". Scripts fully specified with tests. ✓

**Type/name consistency:** `resolve_topic_dir`/`slugify`/`MARKITDOWN` defined in `lib.sh` (Task 3) and reused in `gather.sh` (Task 4). `gather.sh` calls `scripts/_fetch_results.py` with args `(search.json, out_dir, fetch_md.py)` matching the helper's `sys.argv[1..3]`. Topic slugs identical across linter (Task 1), catalog (Task 2), and gather examples (Task 5). `test_catalog.sh` created Task 1, reused Tasks 2 & 8. ✓

**Environment cross-check (verified 2026-06-17):**
- Tool paths all exist: `markitdown`, crawl4ai venv `python`/`search.py`/`fetch_md.py`, `deep-research-crawl4ai.js`, graphify skill. ✓
- `search.py` emits `[{url,title,snippet}]`; `_fetch_results.py` parses exactly those keys. ✓
- `markitdown` prints to stdout by default → ingest's `> dest` redirect is correct. ✓
- `bats` NOT installed → all script tests rewritten as plain-bash harnesses (zero deps). ✓
- Fixed: original gather fetch used `python -` + heredoc + piped stdin (stdin collision) and off-by-one argv; replaced with `scripts/_fetch_results.py` reading JSON from a file path. ✓
- graphify is a `/graphify <path>` skill (not CLI); Task 7 uses `/graphify . --directed`. ✓
