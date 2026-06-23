# Reproducible tracking is docs-anchored; index freshness is a blog-relayed engineering pattern

status: draft
topic: 11-research-pipeline-engineering

The operational backbone of a research engine has two halves, and the corpus
supports them unevenly. The experiment-tracking half rests on MLflow's own
official documentation, which specifies a concrete reproducibility model — runs,
parameters, metrics, artifacts, datasets, and a model registry. The
indexing-freshness half rests entirely on practitioner blogs (Medium, dev.to,
and a vendor site); those sources converge on a coherent engineering pattern for
incremental re-index, change detection, and freshness, but none is authoritative
documentation. This finding keeps the two halves at different evidentiary
weights: what MLflow tracking provides is stated by its docs; what incremental
indexing requires is relayed from blogs and attributed as such.

## What reproducible tracking provides (docs-anchored)

MLflow Tracking is defined by its official documentation as "an API and UI for
logging parameters, code versions, metrics, and output files when running your
machine learning code and for later visualizing the results," exposed through
Python, REST, R, and Java APIs [c69be1c5c]. The unit of reproducibility is the
**run** — an execution of a piece of code that records metadata (metrics,
parameters, start and end times) and artifacts (output files such as model
weights and images) [c69be1c5c]. Runs are grouped into **experiments** for a
specific task, and can be searched by parameter or metric value [c69be1c5c].

Where that state lives is also specified. A **backend store** persists per-run
metadata (run ID, start/end times, parameters, metrics), supporting either
file-system or database backends such as PostgreSQL; a separate **artifact
store** persists large outputs (model weights, images, Parquet files) locally by
default or in object stores such as Amazon S3 or Azure Blob Storage [c69be1c5c].
An optional standalone **MLflow Tracking Server** exposes REST APIs over those
stores and can govern access control and versioning [c69be1c5c]. Logged models
are addressable by a `models:/<model_id>` URI, and registered models by
`models:/<model-name>/<model-version>` via the Model Registry [c69be1c5c].

MLflow's own overview frames the same capabilities at the platform level:
experiment tracking, model versioning, deployment, and evaluation for the ML
lifecycle [c4780274d]. It describes the **Model Registry** as centralized model
versioning with automatic lineage and stage management, promoting models through
staging, production, and archived stages [c4780274d]. These two official sources
are the load-bearing anchor for every claim above about what tracking provides.

Practitioner write-ups relay the same model in less authoritative form: a
markaicode tutorial frames MLflow as experiment tracking plus model versioning
for LLM and production workflows [ca6ba2e55], and a letsdatascience post frames
it as experiment tracking and ML-lifecycle management [cfabd5e1b]. These are
attributed as blog summaries; they corroborate but do not extend the docs.

## What index freshness requires (blog-relayed, not docs-anchored)

No official documentation for indexing-pipeline orchestration appears in this
corpus. The three indexing sources are a Medium post [c9cd9a883], a dev.to
article [c84b2680a], and a vendor blog at synthmetric.com [ccd7354d5]. They are
treated as a convergent practitioner consensus, not as a primary specification.

Their shared pattern is to avoid full re-indexing. The dev.to source names the
"traditional approach" — delete the whole collection, reload, re-chunk, and
re-embed everything — as inefficient: it wastes work on unchanged documents,
re-spends embedding API calls, fails to detect deletions, and degrades as the
corpus grows [c84b2680a]. The alternative the sources converge on is
**incremental indexing**, which reprocesses only changed content. Its building
blocks, as described across the three: a **change-detection layer** (file
timestamps, database change streams, message queues, or event-driven pipelines)
[c9cd9a883]; **document versioning** by content hash, where a changed hash
signals changed content [c9cd9a883]; and **chunk-level indexing** that updates
only affected chunks of a document [c9cd9a883]. The dev.to implementation
realizes this with a **Record Manager** it explicitly calls a "ledger" tracking
File Path → Hash → Timestamp → Status for what has been indexed [c84b2680a].

Update cadence is presented as a trade-off rather than a single answer. The
sources contrast **event-driven** triggering (webhooks or CDC, lowest latency)
against **scheduled** batch updates (cron, simpler and more predictable), and
note a hybrid of the two [ccd7354d5]; one source adds a **delta-index**
architecture that keeps a stable main index plus a small recent-updates index
and searches both [c9cd9a883]. Freshness itself is framed as a goal to be set
per content class, with **drift** — when the index no longer reflects source
truth or retrieval usefulness — detected via lightweight checksums and field
hashes, periodic sampling against the source, and retrieval-quality metrics, and
with re-index priority driven by business criticality, access frequency, and
change magnitude [ccd7354d5]. These are sensible engineering heuristics; because
they rest only on blogs, they are reported as relayed practice, not as
established requirements.

## The tension: full reproducibility and perfect freshness both cost

Both halves carry an explicit cost axis. Reproducible tracking is cheap to start
— MLflow logs to a local `mlruns` directory with no server or database
configured [c69be1c5c] — but the docs show that team-scale reproducibility pulls
in a database backend, an object-store artifact store, and a standalone tracking
server with access control [c69be1c5c], i.e. real operational surface. On the
indexing side, the staleness-versus-re-index-cost trade is the entire point of
the blog pattern: full re-indexing is correct but wasteful [c84b2680a], so the
sources spend effort detecting the minimal change set [c9cd9a883] and
prioritizing which drift to chase first [ccd7354d5]. The honest reading is that
neither perfect reproducibility nor perfect freshness is free; both are bought
incrementally against operational cost.

## Mapping onto this engine's ledger / corpus / graph pipeline

This engine already embodies the tracked-run and indexing-ledger patterns in its
own state, which lets the mapping be concrete rather than aspirational. Its
`state.json` corpus is a list of per-source entries each carrying a stable `id`,
a `lifecycle` status, source and extracted paths, a `lossy` flag, and an
`ingested_at` timestamp — structurally the same idea as the dev.to indexing
ledger's File Path → Hash → Timestamp → Status [c84b2680a], and as MLflow's
backend store keyed by run ID with start/end times [c69be1c5c]. A corpus entry
is to this engine what a run is to MLflow: the addressable, metadata-bearing unit
of reproducibility.

The strongest adoptable pattern from the docs-anchored half is **content-keyed
change detection plus selective re-index**: the engine's per-source ledger
already records ingestion timestamps and a lossy flag, and adding a content hash
per source would let it detect when an upstream document changed and re-extract
only that source — exactly the hash-versioning and changed-only reprocessing the
indexing blogs describe [c9cd9a883] [c84b2680a]. The drift-prioritization
heuristics (criticality, access frequency, change magnitude) [ccd7354d5] map onto
deciding which corpus sources to refresh first when the budget for re-ingestion
is limited. From the MLflow side, the registry's stage promotion through
staging/production/archived with lineage [c4780274d] is the analogue of this
engine's draft → finding promotion: a finding is a versioned artifact whose
lineage back to its cited corpus ids should be as traceable as a registered
model's lineage to its run. The caveat is provenance-symmetric with the rest of
this finding: the registry analogy is docs-anchored [c4780274d], the
incremental-refresh analogy is blog-relayed [c9cd9a883] [c84b2680a] [ccd7354d5],
and the engine should weight adoption accordingly.
