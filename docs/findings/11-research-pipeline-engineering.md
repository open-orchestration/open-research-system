# Findings — Research-Pipeline Engineering

**Question:** What does this category teach for building an AI research system?

> **Source-set note:** This topic's sources skew heavily to MLflow (3 of 5 are MLflow.org or MLflow-centric, with significant site-navigation chrome rather than prose). Claims below are the substantive signal extracted; lessons are framed by analogy from ML pipelines to a research pipeline, since no source covers AI-research pipelines directly.

## Key claims (cited)
- An experiment-tracking layer should reliably log parameters, metrics, artifacts, code, and dependencies for every run, so any experiment can be restored accurately — this reproducibility is the basis for confident governance — [ML Experiment Tracking | MLflow AI Platform](https://mlflow.org/classical-ml/experiment-tracking)
- Auto-logging (e.g. `mlflow.autolog()`) captures hyperparameters, metrics, and artifacts from common libraries with no manual instrumentation, lowering the cost of tracking enough that it can be the default rather than an opt-in — [ML Experiment Tracking | MLflow AI Platform](https://mlflow.org/classical-ml/experiment-tracking)
- A model registry plus version tags/aliases (e.g. `client.set_model_version_tag(..., key="validation_status", value="approved")`) lets you gate deployment on validation state and filter to only approved versions — i.e., promotion is a metadata-driven decision, not an ad-hoc copy — [ML Model Versioning and Experiment Tracking with MLflow](https://dasroot.net/posts/2026/02/ml-model-versioning-experiment-tracking-mlflow/)
- Reproducibility requires versioning data, not just models: teams must track dataset iterations alongside model iterations to manage change smoothly and reproduce results — [MLflow Data Versioning: Techniques, Tools & Best Practices](https://lakefs.io/blog/mlflow-data-versioning/)
- For large-scale data versioning, lakeFS adds a Git-like layer (commit, branch, merge) over an object store such as S3, using zero-copy clones to maintain dataset versions without duplicating data — scaling to billions of files without the storage blow-up of naive snapshots — [MLflow Data Versioning: Techniques, Tools & Best Practices](https://lakefs.io/blog/mlflow-data-versioning/)
- Tracking config should be environment-portable: pointing the tracking URI at a remote backend (e.g. an Azure ML workspace) centralizes all run logs and integrates the pipeline with the surrounding platform/CI-CD — [ML Model Versioning and Experiment Tracking with MLflow](https://dasroot.net/posts/2026/02/ml-model-versioning-experiment-tracking-mlflow/)
- A pipeline is a staged lifecycle (track → evaluate → register → deploy), and the same platform increasingly spans classical ML and LLM/agent applications (observability, evaluations, prompt registry, AI gateway) — so research-pipeline tooling should treat LLM runs as first-class tracked artifacts — [ML Pipeline Orchestration: A Practical Guide for Engineers - MLflow](https://mlflow.org/articles/ml-pipeline-orchestration-a-practical-guide-for-engineers/)

## Convergent vs contested
- **Convergent:** Reproducibility is the central goal; achieve it by logging params/metrics/artifacts/code/deps per run, versioning data and models together, and promoting via registry metadata. Auto-logging should be the default.
- **Contested / open:** The right data-versioning tool is unsettled — MLflow tracks data references but is not itself a scalable data-version store, so a Git-like layer (lakeFS) or DVC is bolted on; which to use depends on scale. No source addresses versioning of *non-deterministic LLM outputs / prompts* as a research artifact in depth.

## Implications for the system (Phase 2)
- Make every research run a tracked, reproducible unit: log the query, prompts/params, retrieved sources, intermediate findings, metrics (faithfulness/coverage from topic 08), and the final report as artifacts — restorable end-to-end.
- Version the source corpus and the knowledge graph (topic 09) as data, not just the report; use a Git-like data layer (lakeFS/DVC) with zero-copy clones for scale rather than snapshot duplication.
- Use a registry with validation-status tags to gate "publishable" reports/configs, mirroring model promotion.
- Centralize tracking behind a remote backend so runs are comparable across environments and wired into CI/CD.

## Gaps found → re-scan
- Sources are MLflow-dominated and chrome-heavy; little independent coverage of orchestration tools (Airflow, Dagflow, Prefect, Kubeflow) or of pipelines purpose-built for LLM/agent research. Re-scan: "research pipeline orchestration Airflow Prefect Dagster LLM agent reproducibility durable execution".
- No coverage of caching/idempotency for expensive LLM stages or of prompt/output versioning as research artifacts. Re-scan: "prompt versioning output provenance caching idempotent LLM pipeline stage".
