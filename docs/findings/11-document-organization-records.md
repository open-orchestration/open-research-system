# Document Organization & Records Discipline

Survey of 11 sources on filing systems, document management, legal e-discovery (ESI) protocols, and
file-organization method — gathered to inform the research system's **corpus & provenance layer**: how
gathered sources and produced findings get named, tagged, stored, retrieved, and made defensible.
Sources in `docs/11-research-pipeline-engineering/sources/doc-organization/`.

## Core thesis

Manual organization does not scale, and legal-grade production is the defensibility model. Two threads:

1. **Placement-first organization breaks.** Folder hierarchies are unmanageable past ~10k files (nesting
   5–6 deep, inconsistent naming, search-time > use-time); tag systems decay because tagging demands even
   more per-file decisions and humans aren't consistent ("2024-Q4" vs "Q4-2024", "Acme" vs "Acme Corp").
   The lesson for our corpus: **auto-assign metadata at ingest and make retrieval search-first**, do not
   rely on a human placing files in the right folder or tagging reliably. (thedrive.ai)
2. **Defensibility = stable IDs + consistent naming + preserved metadata + audit trail.** The legal/ESI
   world has already solved "prove where this came from and that it wasn't altered" — that's exactly our
   provenance requirement, with case law behind it.

## What the ESI / legal sources add (authoritative tier)

`uscourts-final-esi-protocol.md` (federal ESI protocol) and `ediscoveryllc` (case commentary):

- **Naming conventions from the outset** are mandated so related artifacts cross-reference cleanly
  (the protocol's example: audio files, monitoring logs, and transcripts share a convention so each call
  ties to its log + transcript). → Our `sources/`, `findings/`, and citation IDs should share one
  naming scheme so a claim ties back to its source file mechanically.
- **Bates numbering = a unique, stable per-unit label** stamped on every page/document. → This is our
  per-statement citation-ID requirement, restated: every retrievable unit needs a durable ID assigned at
  ingest, independent of where it's stored or its filename.
- **Format triad with metadata-fidelity tradeoffs:** native / TIFF+separate-OCR-text / searchable-PDF;
  the protocol explicitly notes some processing "may result in the loss or alteration of some metadata."
  → Store the original/native form alongside the extracted text; track which transforms are lossy.
- **A protocol agreed up front prevents disputes later** — the "ESI protocol saved the day" case turned
  on having the production format/search-term scope fixed in advance. → Decide the corpus schema (IDs,
  naming, metadata fields, retention) before bulk ingest, not after.

## What DMS vs filing-systems add (mid tier)

- **DMS = metadata + tags + full-text search + version control + role-based access + audit trail +
  retention policy** (pericent). This is the feature checklist for a research corpus store. Phased
  adoption: assess → digitize/structure → train → policy → continuous audit.
- **Classic filing taxonomies** (aurora): alphabetic / numeric / chronological / geographic / subject.
  Our corpus already uses **subject** (17 topics) + **chronological** (gather dates) — a deliberate
  two-axis scheme, which the sources endorse over single-axis filing.
- **Filing best practices that map to automation:** consistent naming, regular audits to remove
  duplicates, backups, secure sensitive files, *document the filing procedure itself*. Dedup + retention
  + a written schema are the ones worth encoding.

## Medical chronology software (domain analog)

`chronicle-medical-chronology-software.md` — closest analog to our extraction pipeline: AI ingests
1,500-page record sets, **extracts dates/diagnoses/providers/treatments → emits a structured timeline
with source citations + auto Bates numbering**. This is precisely our extract→structure→cite loop applied
to records. Manual review is retained only for ambiguous/complex entries — a human-in-the-loop pattern
matching the deep-research findings. (Vendor-comparison tier; treat feature claims as marketing.)

## Consumer file-organization method (low tier, but two strong models)

- The **"present-me vs future-me" split** (yt zkHWJRTIr5E): organize for two users at once — the one
  filing (wants minimal effort) and the one retrieving later (wants findability). The tension between
  cheap-to-file and easy-to-retrieve *is* the corpus design tradeoff in miniature.

- **The Matt Buyer "File by Category" lifecycle model** (yt D8OsqxH6MKI) — the most transferable scheme
  in this batch, despite the consumer framing:
  - **Categories beat alphabetical** because they shrink retrieval from 26 arbitrary classifications to
    ~10 intentional choices. The stated deciding factor is **trust**: *if you trust digital retrieval is
    reliable, the lower-fidelity layer becomes irrelevant.* → retrieval reliability is the whole game;
    matches thedrive's search-first conclusion and our search-first delta.
  - **A time-axis facet inside every category** (his three tabs), which is really a document *lifecycle*:
    - **information** (policies, reference) = *future / may-need*
    - **statements** (current period only) = *present*
    - **records** (vital, look-back) = *past*
  - **Retention is encoded in the structure, not bolted on:** each lifecycle bucket has its own cadence —
    statements graduate to archive on a fixed cycle (his: yearly, post-tax-day), reference is pruned
    as-needed, records ~never. Discard a graduated item only if it's reliably retrievable elsewhere.
  - **Don't over-organize the archive** — transfer wholesale by period; a later lookup is bounded to one
    period's worth of items, so deep archival structure buys nothing.
  - **Spend organizing energy on the active set, not the archive.**
- Category-based home filing also in NYT Wirecutter + elegantsi: stable top-level categories + retention
  + a secure copy. Reinforces "few stable categories beat deep nesting."

## Deltas for our process (Phase-2)

- **Assign a durable per-unit ID (Bates-analog) + auto-extract metadata at ingest** — before any
  filing/folder decision; retrieval is search-first over that metadata, not folder-navigation.
- **One naming convention spanning sources ↔ findings ↔ citations** so cross-reference is mechanical.
- **Keep native + extracted forms; flag lossy transforms** in provenance.
- **Fix the corpus schema (IDs, naming, metadata fields, retention, dedup) up front** — the ESI lesson:
  agreeing the protocol before production is what makes it defensible.
- **Audit trail + retention policy** as first-class corpus features, not afterthoughts.
- **Add a lifecycle-state facet orthogonal to subject** (Buyer model): tag every corpus item
  `reference | active | archived` and drive retention off it — active items graduate to archived on a
  cycle, archived items are stored coarsely (by period, not re-indexed deep), and pruning is allowed only
  when the item is reliably retrievable elsewhere. Keeps the *active working set* small, which is where
  retrieval quality actually matters.

## Source-quality caveats

- Authoritative: uscourts ESI protocol, ediscoveryllc case commentary.
- Mid: pericent (DMS vendor-adjacent), aurora (training glossary).
- Low / intuition-only: NYT Wirecutter + elegantsi (consumer), thedrive + chronicle (vendor blogs —
  good concepts, self-interested claims), the two YouTube transcripts (auto-captions, unverified, consumer).
- **Theme placement:** staged under topic 11 (pipeline engineering) as a cross-cutting *corpus/records*
  concern. It is large enough it may warrant its own catalog topic (#18 "Records / corpus organization &
  provenance") — flagged for a catalog decision.
