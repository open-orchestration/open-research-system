---
id: da2a65c0c
topic: 11-research-pipeline-engineering
title: LlamaIndex's IngestionPipeline gives the index-freshness mechanism a doc anchor — per-(node+transformation) caching and docstore hash dedup/upserts
status: draft
---

# LlamaIndex's IngestionPipeline is the doc anchor for incremental ingestion

A prior finding [d470b6824] split the operational backbone of a research engine
into two halves at different evidentiary weights: a docs-anchored
reproducible-tracking half (MLflow) and an index-freshness / incremental-reindex
half that rested only on practitioner blogs. That title flags the gap directly —
"index freshness is a blog-relayed engineering pattern." This finding closes that
specific gap with one piece of official framework documentation: LlamaIndex's
"Ingestion Pipeline" page, which documents a concrete, shipped mechanism for
incremental ingestion — per-(node+transformation) caching and a docstore-backed
document-management layer that dedups by content hash and handles upserts and
duplicate-skipping [c86c66bc5]. It does not re-argue [d470b6824]'s
reproducible-tracking half; it upgrades the freshness claims from blog-relayed
consensus to one framework's documented behavior, while keeping honest about what
a single framework's docs do and do not establish.

## How the pipeline avoids recomputing transformations on unchanged inputs

An `IngestionPipeline` applies a sequence of `Transformations` to input data, and
the resulting nodes are either returned or inserted into a vector database
[c86c66bc5]. The freshness-relevant mechanism is its cache: each
node+transformation pair is hashed and cached, so subsequent runs with the same
node+transformation combination reuse the cached result instead of recomputing
the transformation [c86c66bc5]. The reuse is conditional on the cache being
persisted — the docs state the saving applies "if the cache is persisted"
[c86c66bc5].

That cache is a first-class, storable object. A pipeline can `persist` and load
its cache locally, and the cache can be cleared when it grows too large
[c86c66bc5]. Beyond local storage, the docs list remote cache backends —
`RedisCache`, `MongoDBCache`, and `FirestoreCache` — wired through an
`IngestionCache` configured with a backend and a collection name [c86c66bc5].
This is the documented answer to "don't re-embed unchanged content": the caching
is keyed on the (node, transformation) hash, so an unchanged node skips the
expensive transformation (including embedding) on re-run.

## How the docstore decides a document is a duplicate versus an update

Caching alone does not detect that an upstream document changed; that is the job
of the separate **document management** layer. Attaching a `docstore` to the
pipeline enables it, and it uses `document.doc_id` (or `node.ref_doc_id`) as the
grounding identity [c86c66bc5]. Mechanically, the docstore stores a map of
`doc_id` -> `document_hash` and actively looks for duplicate documents
[c86c66bc5]. The decision branches on whether a vector store is also attached
[c86c66bc5]:

- With a vector store attached: if a duplicate `doc_id` is detected and its hash
  has **changed**, the document is re-processed and **upserted**; if the
  duplicate `doc_id` is detected and the hash is **unchanged**, the node is
  **skipped** [c86c66bc5].
- With no vector store attached: the pipeline checks all existing hashes for each
  node; if a duplicate is found the node is skipped, otherwise it is processed
  [c86c66bc5].

So the hash is the change signal — same `doc_id` with a changed hash means
"update, re-embed and upsert"; same `doc_id` with an unchanged hash means "skip,
already current." This is the same content-hash-as-change-signal idea
[d470b6824] relayed from blogs (changed hash signals changed content), now stated
by a framework's own docs rather than inferred from practitioner write-ups.

## What document management requires, and its documented limit

Document management is not on by default — it must be enabled by attaching a
`docstore` (the docs show `SimpleDocumentStore()` as the in-memory option)
[c86c66bc5]. Its capability also depends on whether a vector store is present, and
the docs state the limit plainly: "If we do not attach a vector store, we can
only check for and remove duplicate inputs" [c86c66bc5]. In other words, without
a vector store the layer dedups inputs but cannot perform the
re-process-and-upsert update path — the full incremental-update behavior
(detect-changed-then-upsert) requires both a docstore and a vector store
attached. The docs do not enumerate further `docstore` strategy options on this
page beyond the duplicate/upsert/skip behavior described above, so no additional
strategy variants are asserted here.

Separately, the pipeline's `run` method can be parallelized by setting
`num_workers`, which distributes batches of nodes across processors via
`multiprocessing.Pool` [c86c66bc5]. That is a throughput knob, not a freshness
mechanism, but it is part of the same documented pipeline surface.

## Scope: one framework's mechanism, not a vendor-neutral freshness spec

This is precise and bounded. What [c86c66bc5] establishes is **LlamaIndex's
official mechanism** for incremental ingestion and index freshness: cache reuse
keyed on node+transformation hashes, plus docstore document management that
dedups by `doc_id` -> `document_hash` and upserts on hash change. It is one
framework's documented behavior, not a universal change-data-capture (CDC) or
index-freshness standard. The blog-relayed half of [d470b6824] described a
broader design space — event-driven versus scheduled triggering, delta-index
architectures, drift detection via checksums and retrieval-quality metrics — and
those remain blog-relayed; this doc covers only the dedup/upsert/cache mechanism,
not trigger cadence or drift detection. A vendor-neutral CDC / index-freshness
**specification** (as opposed to any single framework's docs) is still absent
from the corpus and stays an open gap.

The honest mapping onto this engine: its per-source corpus ledger already carries
a stable `id` and an `ingested_at` timestamp [d470b6824]; the directly adoptable
pattern from [c86c66bc5] is the `doc_id` -> `document_hash` map as an explicit
change signal — adding a content hash per source would let the engine detect a
changed upstream document and re-extract only that source, exactly the
hash-keyed skip/re-process behavior the LlamaIndex docstore implements
[c86c66bc5]. That refines [d470b6824]'s blog-relayed "add a content hash per
source" suggestion by giving it a documented reference implementation, without
claiming the engine must adopt LlamaIndex itself.
