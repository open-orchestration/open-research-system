# Findings — Textbooks & Long-form References

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- Manning, Raghavan & Schütze's *Introduction to Information Retrieval* (Cambridge, 2008) is the canonical, free, full-text textbook for the retrieval foundations underneath any RAG/search layer — indexing, term weighting, ranked retrieval, and IR evaluation. It is the standard reference, available online in full. — [Introduction to Information Retrieval | Cambridge](https://www.cambridge.org/highereducation/books/introduction-to-information-retrieval/669D108D20F556C5C30957D63B5AB65C)
- The complete book PDF is openly hosted by Stanford NLP, so the system's retrieval design can cite primary IR theory (tf-idf, the vector space model, evaluation of ranked retrieval) directly rather than secondary blog summaries. — [PDF Introduction to Information Retrieval — Stanford University](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)
- The same authoritative text is mirrored across Google Books and Cambridge's higher-education platform, confirming it as the field's settled long-form reference for IR rather than a single-vendor view. — [Introduction to Information Retrieval — Christopher D. Manning (Google Books)](https://books.google.com/books/about/Introduction_to_Information_Retrieval.html?id=t1PoSh4uwVcC)

## Convergent vs contested
- **Convergent:** For this topic there is effectively one canonical work — *Introduction to Information Retrieval* — appearing across three independent hosts (Cambridge, Stanford, Google Books). The foundations it covers (ranked retrieval, tf-idf, precision/recall/nDCG-style evaluation) are uncontested and directly underpin the BM25-plus-dense hybrid retrieval the reference systems (topic 13) prescribe.
- **Contested / open:** None surfaced within the gathered sources; the topic is thin and single-source by nature. The book predates dense/neural retrieval, so its coverage of embeddings-based retrieval is a known limitation to supplement from the papers (topic 14) and RAG topics.

## Implications for the system (Phase 2)
- Use *Introduction to Information Retrieval* as the citable theoretical backbone for the retrieval subsystem — term weighting, the vector space model, and the standard IR evaluation metrics (precision/recall/MAP) that the eval harness (topic 16) reuses.
- Pin the Stanford open PDF as the authoritative source link in design docs so retrieval-design rationale traces to primary theory, not blog posts.
- Pair the classical IR foundation with the dense/neural retrieval literature (topics 6/14) to cover the embeddings era the textbook does not.

## Gaps found → re-scan
- One of five sources is an Amazon-ad redirect (a DuckDuckGo `y.js` sponsored link to amazon.com), not a real reference — discard it; it carries no citable content.
- Topic is effectively single-title. Targeted re-scan for genuine long-form breadth: Russell & Norvig *AIMA* (agents/search), Jurafsky & Martin *Speech and Language Processing* (NLP/retrieval/LLMs), and a research-methods textbook on evidence synthesis — to give the system a broader textbook foundation than IR alone.
