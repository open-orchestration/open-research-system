# Findings — Specs & Standards

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- Citation Style Language (CSL) is the de-facto open standard for formatting citations and bibliographies: an open XML-based language with a community repository of 10,000+ free styles, and it is the formatting engine behind Zotero, Mendeley, Papers and other reference managers — so emitting CSL means interoperating with the whole reference-management ecosystem. — [Citation Style Language](https://citationstyles.org/)
- CSL separates two concerns the system must keep distinct: style/locale files (`.csl`, RELAX NG-validated XML; styles are either "independent" defining all rules, or "dependent" inheriting from a parent) describe *formatting*, while a separate JSON data model holds the *bibliographic metadata* fed to the processor. — [Citation Style Language (CSL) — Metadata Standards Index](https://msi.dublincore.org/standards/csl/)
- The bibliographic-metadata interchange format is `csl-data.json` (the CSL-JSON input model originated by citeproc-js), with `csl-citation.json` for citations — these JSON schemas, not BibTeX, are the modern machine-readable carrier for reference data into a CSL processor. — [GitHub - dhimmel/csl-schema: Citation Style Language schema](https://github.com/dhimmel/csl-schema)
- Rendering is done by interchangeable CSL processor implementations — citeproc-js, citeproc-py, citeproc-rs — against the same style + locale + CSL-JSON inputs, so the system can pick a processor in its own language without changing the data contract. — [Citation Style Language (CSL) — Metadata Standards Index](https://msi.dublincore.org/standards/csl/)
- The CSL 1.0.2 specification is the authoritative, versioned spec for the processing model and style schema, hosted at docs.citationstyles.org — the document to conform to when generating styles. — [CSL 1.0.2 Specification — Citation Style Language](https://docs.citationstyles.org/en/stable/specification.html)
- For web-publishing the report itself, Schema.org's `citation` property is the standard for marking up a reference from one CreativeWork to another (value: CreativeWork or Text), giving search-engine-discoverable citation metadata distinct from CSL's print-formatting role. — [citation — Schema.org Property](https://schema.org/citation)

## Convergent vs contested
- **Convergent:** CSL is the unambiguous standard for citation formatting, with a clean separation of style (XML/RELAX NG) from data (CSL-JSON) from processor (citeproc-*). Schema.org `citation` is the orthogonal standard for web-discoverable reference markup. The two are complementary, not competing.
- **Contested / open:** CSL-JSON vs BibTeX as the internal reference data model — the gathered sources establish CSL-JSON as the modern processor input but do not directly compare it to BibTeX (no BibTeX source was gathered), so the trade-off is unresolved here.

## Implications for the system (Phase 2)
- Adopt CSL-JSON (`csl-data.json` schema) as the internal canonical representation for every gathered source's bibliographic metadata; it is the format every CSL processor consumes and the cleanest interop point with Zotero/Mendeley.
- Render bibliographies/in-text citations by selecting a CSL style and running a citeproc processor in the system's language (citeproc-py / citeproc-js / citeproc-rs) — keep formatting fully data-driven and style-swappable rather than hard-coding one citation format.
- When publishing the report as HTML, emit Schema.org `citation` markup so references are machine-discoverable, layered on top of the CSL-formatted human-readable bibliography.

## Gaps found → re-scan
- Sources skew heavily to CSL (4 of 5). Missing entirely: BibTeX format spec, MADR / ADR (architecture-decision-record) templates, and the Model Context Protocol (MCP) specification — all named as relevant standards but not gathered. MCP in particular is cited by the reference systems (topic 13) as the agent-integration backbone and deserves its own spec source.
- The CSL 1.0.2 spec source is a 123-byte stub (link only, no body). Targeted re-scan: fetch full bodies of the CSL 1.0.2 spec, the MCP specification (modelcontextprotocol.io / spec), a BibTeX field reference, and a MADR ADR template.
