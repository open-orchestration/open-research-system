# Findings — Applied Research Playbooks

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- Market sizing is a *layered* drill-down: TAM (total revenue if 100% share, no constraints) → SAM (the slice you can actually serve) → SOM (the share you can realistically capture) — each layer narrows theoretical potential toward an achievable target. — [TAM SAM SOM: The Comprehensive Guide to Strategic Market Sizing](https://www.linkedin.com/pulse/tam-sam-som-comprehensive-guide-strategic-market-sizing-mohidul-alam-cjefc)
- TAM is defined as "the total revenue opportunity available to a product or service if it could achieve 100% market share with no constraints" — explicitly the theoretical maximum, to be discounted, not reported as a forecast. — [TAM SAM SOM: The Comprehensive Guide to Strategic Market Sizing](https://www.linkedin.com/pulse/tam-sam-som-comprehensive-guide-strategic-market-sizing-mohidul-alam-cjefc)
- Cohort retention analysis groups users by a shared starting point (e.g. signup month) and tracks what fraction stay active over later periods — it "reveals patterns that average metrics miss" because aggregate numbers blend distinct groups together. — [What Is Cohort Retention Analysis: Essential Metrics Guide](https://amplitude.com/explore/analytics/cohort-retention-analysis)
- Retention is read as a product-health signal: high cohort retention indicates strong product-market fit and makes acquisition spend pay back, while declining curves flag onboarding, product-experience, or customer-success problems. — [Cohort Retention Analysis: Guide & Best Practices](https://count.co/metric/cohort-retention-analysis)
- Combining cohort analysis with segmentation (demographics) exposes heterogeneity that a single retention curve hides — e.g. retention differs measurably by gender and generation across cohorts. — [Unpacking Retail Customer Retention Through Cohort Analysis](https://link.springer.com/chapter/10.1007/978-3-032-08243-5_14)
- The cross-cutting methodological lesson: never trust a blended average — disaggregate by entry cohort and segment so opposing sub-trends don't cancel out into a misleading mean. — [What Is Cohort Retention Analysis: Essential Metrics Guide](https://amplitude.com/explore/analytics/cohort-retention-analysis)

## Convergent vs contested
- **Convergent:** Both playbook families (market sizing, cohort/retention) share one principle — decompose a headline number into structured layers/segments before drawing conclusions (TAM→SAM→SOM; aggregate→cohort→segment). Averages mislead; structure reveals.
- **Contested / open:** Retention "benchmarks" are acknowledged to be industry-relative with no universal target. Market-sizing top-down vs bottom-up estimation tradeoffs are asserted but not adjudicated in the gathered material.

## Implications for the system (Phase 2)
- Bake "decompose before you conclude" into synthesis: when the system reports a quantity (market size, a rate, a trend), it should present the layered/segmented breakdown and flag when a single aggregate could be hiding opposing sub-trends.
- Offer reusable playbook *templates* (market-sizing funnel, cohort table) the agent can instantiate for applied questions, with explicit assumptions surfaced at each layer (a TAM is a labeled ceiling, not a forecast).

## Gaps found → re-scan
- This topic is badly skewed: 4 of 5 sources are cohort/retention and 1 is TAM/SAM/SOM. The catalog title also names **competitive analysis, trend detection, and A/B-testing methodology**, none of which were gathered. Sources are also marketing-blog tier (FasterCapital, LinkedIn, vendor blogs), weaker than the peer-reviewed Springer chapter. Deep-dive queries: "competitive analysis frameworks (Porter five forces, SWOT, competitor teardown)", "trend detection / signal-vs-noise methodology", and "A/B test design: hypothesis, sample size, guardrail metrics, sequential testing".
