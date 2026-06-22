# Extraction method and community structure are the cost-fidelity levers when compiling a source-of-truth knowledge-graph corpus

status: draft

## Scope

Three peer-style primary sources on knowledge-graph (KG) construction plus
community detection over source-of-truth corpora: an arXiv system paper on
efficient KG construction/retrieval for large-scale RAG [c0ec9aa64], an arXiv
paper on community-structured KG retrieval for fact-checking [c0cf2d36b], and a
NAACL 2025 long paper on KG-guided RAG [c520aee3f]. The finding isolates the two
design levers these sources actually measure — how triples are extracted, and
how graph community/centrality structure is exploited — and what each costs in
fidelity. It is deliberately narrow: it does not restate the broader
GraphRAG/Leiden/hybrid-routing material already in the topic finding.

## Sub-questions

1. **Construction method** — what extraction techniques do these papers use, and what is the cost/fidelity trade between LLM-based and non-LLM extraction?
2. **Community-detection / centrality technique** — how is community structure computed and exploited, and what does the resulting graph look like structurally?
3. **Evidence & limitations** — what is measured against a vector baseline, and where do the authors themselves say the approach breaks?
4. **Application to a source-of-truth corpus** — what carries over to a system whose own graph layer does extraction → build → community detection → centrality (god-node) analysis?

## Key claims (cited)

### Construction method — extraction is a tunable cost lever, not a fixed LLM dependency

- Triple extraction does not have to use an LLM: one system offers a triple
  extractor that can switch between commercial LLMs (GPT-4o, Sonnet) and a
  dependency-parser approach, choosing per dataset based on a cost calculation,
  and in that paper the authors run the dependency-parser path [c0ec9aa64].
- The dependency-parser path uses SpaCy's parser and is described as
  **domain-agnostic** — applicable across domains without domain-specific
  training or customization — chosen for industrial-grade speed and open-ended
  information extraction [c0ec9aa64].
- The construction pipeline is explicitly engineered for corpus hygiene: an
  EntityRelationNormalizer deduplicates variant spellings of the same
  entity/relation into one and standardizes names for graph-DB compatibility,
  and a RelationEntityFilter supports schema-guided construction by
  post-filtering extracted entities/relations to a pre-defined schema
  [c0ec9aa64].
- A second source extracts relations with REBEL (a seq2seq model trained on
  Wikipedia) rather than a general LLM, building an entity graph G=(E,R) with
  entities as nodes and relations as edges [c0cf2d36b].

### Community-detection / centrality technique — Louvain modularity over the entity graph

- Community detection uses the **Louvain algorithm**, which optimizes
  modularity — a scalar in [-1, 1] measuring link density inside communities
  versus between them — by starting with each node as its own community and
  iteratively merging to maximize modularity gain until no further improvement
  is possible [c0cf2d36b].
- The resulting graph is structurally multi-hop and hub-skewed. The
  fact-checking KG reaches up to 48,630 nodes and 202,455 edges, with average
  shortest-path length 4.03–4.28 and diameter 13–17 across the top-δ% community
  subsets — i.e. several hops separate typical node pairs [c0cf2d36b]. The
  large-scale RAG KG reports 39,155 nodes at an average node degree of 1.52 but
  a **highest degree of 236** — a heavy-tailed degree distribution where a few
  nodes dominate connectivity [c0ec9aa64].
- A third design uses the KG not to cluster but to **expand and organize**
  retrieval: after semantic-based retrieval produces seed chunks, fact-level KG
  relationships drive a chunk-expansion step and a chunk-organization step, to
  improve the diversity and coherence of retrieved context [c520aee3f].

### Evidence & limitations — measured gains over a vector baseline, with author-stated failure modes

- Against dense vector retrieval on a domain corpus, both GraphRAG variants
  (GPT-4o-extracted and dependency-graph-extracted) show **at least 12% higher
  context-precision**, reduce the No-Coverage rate by 32%, and raise Full
  Coverage by at least 19% [c0ec9aa64].
- Crucially for the cost lever: the dependency-graph variant **retains 94% of
  the GPT-4o variant's context-precision performance** [c0ec9aa64] — most of the
  fidelity is reachable without per-triple LLM calls.
- Community structure helps over no-retrieval and flat semantic retrieval in
  fact-checking: a No-Retrieval baseline scored 39.79% accuracy and Semantic
  Retrieval 43.84%, while the community-structured method surpassed all
  baselines (and a triple-formatted KAPING baseline actually *declined* to
  39.41%, indicating raw triple-formatted context can hurt) [c0cf2d36b].
- The authors are explicit about the dominant failure mode:
  CommunityKG-RAG's effectiveness "heavily relies on the quality of entity
  recognition"; because REBEL is Wikipedia-trained, applying it to text very
  different from Wikipedia "might hinder performance," and LM-based entity
  recognition risks introducing hallucinations [c0cf2d36b]. Construction is also
  computationally heavy, but communities can be **pre-computed and reused**,
  making the operational/query phase lightweight [c0cf2d36b].

### Application to a source-of-truth corpus

- The extraction lever generalizes: for a controlled source-of-truth corpus, a
  schema-guided, normalized, deduplicated extraction pipeline [c0ec9aa64]
  matters more than raw extractor choice, because downstream community detection
  and centrality inherit any entity-recognition error directly [c0cf2d36b].
- Pre-computing community structure once and reusing it [c0cf2d36b] matches an
  engine whose graph layer runs Louvain/community detection as a build-time pass
  and then serves queries against the cached partition; the heavy-tailed degree
  distribution (max degree 236 vs avg 1.52) [c0ec9aa64] is the empirical basis
  for surfacing a small set of high-degree hub ("god") nodes as the corpus's
  load-bearing concepts.

## Provenance

All three load-bearing sources are primary/peer-reviewed: two arXiv research
papers with full methods and result tables [c0ec9aa64, c0cf2d36b] and one
NAACL 2025 long paper [c520aee3f]. No vendor-marketing or SEO-blog source backs
any claim here. The strongest quantitative claims (the 94% retention, the ≥12%
context-precision gain, the degree/path statistics, the Louvain modularity
definition) all rest on the two arXiv papers' own reported evaluations;
[c520aee3f] is cited only at the abstract level (method description) since the
corpus capture of that source is the ACL landing page plus abstract.

## Open questions / gaps

- [c520aee3f]'s corpus entry is the ACL landing page + abstract only — its
  HotpotQA result magnitudes and the chunk-expansion algorithm detail are not in
  the captured text. Re-scan to fetch the full PDF body for concrete numbers.
- All three internal evaluations are author-run on their own datasets (CCM,
  MOCHEG, HotpotQA); no independent third-party reproduction is in-corpus.
- Centrality is only implied (degree distribution) — none of the three sources
  evaluates a god-node / centrality-ranking step directly, so the engine's
  god-node surfacing rests on structural plausibility, not a measured result.
- The accuracy/coverage gains are reported on a single domain corpus each;
  whether the ≥12% context-precision gain holds on heterogeneous source-of-truth
  corpora is untested in these sources.
