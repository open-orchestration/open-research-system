[Skip to main content](https://mlflow.org/docs/latest/ml/#__docusaurus_skipToContent_fallback)
[ ![MLflow Logo](https://mlflow.org/docs/latest/images/logo-light.svg)![MLflow Logo](https://mlflow.org/docs/latest/images/logo-dark.svg) ](https://mlflow.org/docs/latest/)
[Machine Learning](https://mlflow.org/docs/latest/ml/)
  * [LLMs & Agents](https://mlflow.org/docs/latest/genai/)
  * [Machine Learning](https://mlflow.org/docs/latest/ml/)


[API Reference](https://mlflow.org/docs/latest/api_reference/index.html)[Self-Hosting](https://mlflow.org/docs/latest/self-hosting/)[Community](https://mlflow.org/docs/latest/community/)
[GitHub](https://github.com/mlflow/mlflow)
Search
  * [Overview](https://mlflow.org/docs/latest/ml/)
  * [Getting Started](https://mlflow.org/docs/latest/ml/getting-started/)
  * [Machine Learning](https://mlflow.org/docs/latest/ml/traditional-ml/)
    * [Traditional ML](https://mlflow.org/docs/latest/ml/traditional-ml/)
    * [Deep Learning](https://mlflow.org/docs/latest/ml/deep-learning/)
  * [Build ](https://mlflow.org/docs/latest/ml/tracking/)
    * [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/)
    * [MLflow Model](https://mlflow.org/docs/latest/ml/model/)
    * [MLflow Datasets](https://mlflow.org/docs/latest/ml/dataset/)
  * [Evaluate](https://mlflow.org/docs/latest/ml/evaluation/)
  * [Deploy](https://mlflow.org/docs/latest/ml/model-registry/)
  * [Team Collaboration](https://mlflow.org/docs/latest/self-hosting/)
  * [API References](https://mlflow.org/docs/latest/api_reference/python_api/index.html)
  * [MLflow 3 Migration Guide](https://mlflow.org/docs/latest/ml/mlflow-3/)
  * [More](https://github.com/mlflow/mlflow/blob/master/CONTRIBUTING.md)


  * [](https://mlflow.org/docs/latest/)
  * Overview


On this page
# MLflow: AI Engineering Platform for LLMs, Agents, & Models
MLflow is the largest open source **AI engineering platform for agents, LLMs, and ML models**. MLflow enables teams of all sizes to debug, evaluate, monitor, and optimize production-quality AI applications while controlling costs and managing access to models and data. With over 30 million monthly downloads, thousands of organizations rely on MLflow each day to ship AI to production with confidence.
MLflow's comprehensive feature set for agents and LLM applications includes production-grade [observability](https://mlflow.org/docs/latest/genai/tracing/), [evaluation](https://mlflow.org/docs/latest/genai/eval-monitor/), [prompt management](https://mlflow.org/docs/latest/genai/prompt-registry/), an [AI Gateway](https://mlflow.org/docs/latest/genai/governance/ai-gateway/) for managing costs and model access, and more. Learn more at [MLflow for LLMs and Agents](https://mlflow.org/docs/latest/genai/).
For machine learning (ML) model development, MLflow provides [experiment tracking](https://mlflow.org/docs/latest/ml/tracking/quickstart/), [model evaluation capabilities](https://mlflow.org/docs/latest/ml/evaluation/), a [production model registry](https://mlflow.org/docs/latest/ml/model-registry/), and [model deployment tools](https://mlflow.org/docs/latest/ml/deployment/).
## Getting Started with MLflow for ML Models[​](https://mlflow.org/docs/latest/ml/#getting-started-with-mlflow-for-ml-models "Direct link to Getting Started with MLflow for ML Models")
This page covers MLflow's tools for **traditional machine learning and deep learning** : ML experiment tracking, model versioning, model deployment, and model evaluation. If you're building agents and LLM applications, see [MLflow for LLMs and Agents](https://mlflow.org/docs/latest/genai/).
If this is your first time exploring MLflow for MLOps, the tutorials and guides here are a great place to start.
### [Quickstart A quick guide to learn the basics of MLflow for MLOps by training a simple scikit-learn model Start learning →](https://mlflow.org/docs/latest/ml/getting-started/quickstart/)### [MLflow for Agents & LLMs A walkthrough of MLflow's Agent and LLM capabilities, including tracing, evaluation, and prompt management Start building →](https://mlflow.org/docs/latest/genai/getting-started/connect-environment/)### [Deep Learning Guide A hands-on tutorial on how to use MLflow for ML to track deep learning model training with PyTorch Start training →](https://mlflow.org/docs/latest/ml/getting-started/deep-learning/)
## MLflow for ML Models: Core Capabilities[​](https://mlflow.org/docs/latest/ml/#mlflow-for-ml-models-core-capabilities "Direct link to MLflow for ML Models: Core Capabilities")
MLflow for ML Models provides comprehensive support for traditional machine learning and deep learning workflows. From experiment tracking and model versioning to deployment and monitoring, MLflow streamlines every aspect of the ML lifecycle. Whether you're working with scikit-learn models, training deep neural networks, or managing complex ML pipelines, MLflow provides the tools you need to build reliable, scalable machine learning systems.
Explore the MLflow's machine learning capabilities and integrations below to enhance your ML development workflow!
  * Tracking & Experiments
  * Model Registry
  * Model Deployment
  * ML Library Integrations
  * Model Evaluation


### Track experiments and manage your ML development[​](https://mlflow.org/docs/latest/ml/#track-experiments-and-manage-your-ml-development "Direct link to Track experiments and manage your ML development")
#### Core Features[​](https://mlflow.org/docs/latest/ml/#core-features "Direct link to Core Features")
**MLflow Tracking** provides comprehensive experiment logging, parameter tracking, metrics visualization, and artifact management.
**Key Benefits:**
  * **Experiment Organization** : Track and compare multiple model experiments
  * **Metric Visualization** : Built-in plots and charts for model performance
  * **Artifact Storage** : Store models, plots, and other files with each run
  * **Collaboration** : Share experiments and results across teams


#### Guides[​](https://mlflow.org/docs/latest/ml/#guides "Direct link to Guides")
[Getting Started with Tracking](https://mlflow.org/docs/latest/ml/tracking/quickstart/)
[Advanced Tracking Features](https://mlflow.org/docs/latest/ml/tracking/tracking-api/)
[Autologging for Popular Libraries](https://mlflow.org/docs/latest/ml/tracking/autolog/)
![MLflow Tracking](https://mlflow.org/docs/latest/assets/images/tracking-metrics-ui-temp-ffc0da57b388076730e20207dbd7f9c4.png)
### Manage model versions and lifecycle[​](https://mlflow.org/docs/latest/ml/#manage-model-versions-and-lifecycle "Direct link to Manage model versions and lifecycle")
#### Core Features[​](https://mlflow.org/docs/latest/ml/#core-features-1 "Direct link to Core Features")
**MLflow Model Registry** provides centralized model versioning, stage management, and model lineage tracking.
**Key Benefits:**
  * **Version Control** : Track model versions with automatic lineage
  * **Stage Management** : Promote models through staging, production, and archived stages
  * **Collaboration** : Team-based model review and approval workflows
  * **Model Discovery** : Search and discover models across your organization


#### Guides[​](https://mlflow.org/docs/latest/ml/#guides-1 "Direct link to Guides")
[Model Registry Introduction](https://mlflow.org/docs/latest/ml/model-registry/)
![MLflow Model Registry](https://mlflow.org/docs/latest/assets/images/oss_registry_3_overview-daec63473b4d7bbf47c559600bf5c35d.png)
### Deploy models to production environments[​](https://mlflow.org/docs/latest/ml/#deploy-models-to-production-environments "Direct link to Deploy models to production environments")
#### Core Features[​](https://mlflow.org/docs/latest/ml/#core-features-2 "Direct link to Core Features")
**MLflow Deployment** supports multiple deployment targets including REST APIs, cloud platforms, and edge devices.
**Key Benefits:**
  * **Multiple Targets** : Deploy to local servers, cloud platforms, or containerized environments
  * **Model Serving** : Built-in REST API serving with automatic input validation
  * **Batch Inference** : Support for batch scoring and offline predictions
  * **Production Ready** : Scalable deployment options for enterprise use


#### Guides[​](https://mlflow.org/docs/latest/ml/#guides-2 "Direct link to Guides")
[Model Deployment Overview](https://mlflow.org/docs/latest/ml/deployment/)
[Local Model Serving](https://mlflow.org/docs/latest/ml/deployment/deploy-model-locally/)
[Cloud Deployment Options](https://mlflow.org/docs/latest/ml/deployment/deploy-model-to-sagemaker/)
[Modal Deployment](https://mlflow.org/docs/latest/ml/deployment/deploy-model-to-modal/)
![MLflow Deployment](https://mlflow.org/docs/latest/assets/images/mlflow-deployment-overview-f0b56bbb6d5689f022a5cff47f16f832.png)
### Explore Native MLflow ML Library Integrations[​](https://mlflow.org/docs/latest/ml/#explore-native-mlflow-ml-library-integrations "Direct link to Explore Native MLflow ML Library Integrations")
[![Scikit-learn](https://mlflow.org/docs/latest/ml/)](https://mlflow.org/docs/latest/ml/traditional-ml/sklearn/)
Scikit-learn
[![XGBoost](https://mlflow.org/docs/latest/assets/images/xgboost-logo-34eb19cd705f245f4c29ca879b417b96.svg)](https://mlflow.org/docs/latest/ml/traditional-ml/xgboost/)
XGBoost
[![TensorFlow](https://mlflow.org/docs/latest/ml/)](https://mlflow.org/docs/latest/ml/deep-learning/tensorflow/)
TensorFlow
[![PyTorch](https://mlflow.org/docs/latest/ml/)](https://mlflow.org/docs/latest/ml/deep-learning/pytorch/)
PyTorch
[![Keras](https://mlflow.org/docs/latest/ml/)](https://mlflow.org/docs/latest/ml/deep-learning/keras/)
Keras
[![Spark MLlib](https://mlflow.org/docs/latest/ml/)](https://mlflow.org/docs/latest/ml/traditional-ml/sparkml/)
Spark MLlib
### Evaluate and validate your ML models[​](https://mlflow.org/docs/latest/ml/#evaluate-and-validate-your-ml-models "Direct link to Evaluate and validate your ML models")
#### Core Features[​](https://mlflow.org/docs/latest/ml/#core-features-3 "Direct link to Core Features")
**MLflow Evaluation** provides comprehensive model validation tools, automated metrics calculation, and model comparison capabilities.
**Key Benefits:**
  * **Automated Metrics** : Built-in evaluation metrics for classification, regression, and more
  * **Custom Evaluators** : Create custom evaluation functions for domain-specific metrics
  * **Model Comparison** : Compare multiple models and versions side-by-side
  * **Validation Datasets** : Track evaluation datasets and ensure reproducible results


#### Guides[​](https://mlflow.org/docs/latest/ml/#guides-3 "Direct link to Guides")
Learn how to [evaluate your ML models](https://mlflow.org/docs/latest/ml/evaluation/) with MLflow
Discover [custom evaluation metrics](https://mlflow.org/docs/latest/ml/evaluation/#custom-metrics--visualizations) and functions
Compare models with [MLflow Model Validation](https://mlflow.org/docs/latest/ml/evaluation/#model-validation)
![MLflow Evaluation](https://mlflow.org/docs/latest/assets/images/evaluate_metrics-bee252801c0dd3bc77ff472f8e7d4a48.png)
## Running MLflow for ML Models Anywhere[​](https://mlflow.org/docs/latest/ml/#running-mlflow-for-ml-models-anywhere "Direct link to Running MLflow for ML Models Anywhere")
MLflow can be used in a variety of environments, including your local environment, on-premises clusters, cloud platforms, and managed services. Being an open-source platform, MLflow is **vendor-neutral** ; whether you're building AI agents, LLM applications, or ML models, you have access to MLflow's core capabilities — tracing, evaluation, experiment tracking, deployment, and more.
[![Databricks Logo](https://mlflow.org/docs/latest/ml/)](https://docs.databricks.com/aws/en/mlflow3/genai/)[![Amazon SageMaker Logo](https://mlflow.org/docs/latest/ml/)](https://aws.amazon.com/sagemaker-ai/experiments/)[![Azure Machine Learning Logo](https://mlflow.org/docs/latest/assets/images/azure-ml-logo-92b5684b6330ac456815e6dc3233bbd8.png)](https://learn.microsoft.com/en-us/azure/machine-learning/concept-mlflow?view=azureml-api-2)[![Nebius Logo](https://mlflow.org/docs/latest/ml/)](https://nebius.com/services/managed-mlflow)[![Kubernetes Logo](https://mlflow.org/docs/latest/assets/images/kubernetes-logo-0728374966fe59ee08e213e966513d00.png)](https://mlflow.org/docs/latest/ml/tracking/)
[Next Getting Started with MLflow for ML](https://mlflow.org/docs/latest/ml/getting-started/)
  * [Getting Started with MLflow for ML Models](https://mlflow.org/docs/latest/ml/#getting-started-with-mlflow-for-ml-models)
  * [MLflow for ML Models: Core Capabilities](https://mlflow.org/docs/latest/ml/#mlflow-for-ml-models-core-capabilities)
    * [Track experiments and manage your ML development](https://mlflow.org/docs/latest/ml/#track-experiments-and-manage-your-ml-development)
    * [Manage model versions and lifecycle](https://mlflow.org/docs/latest/ml/#manage-model-versions-and-lifecycle)
    * [Deploy models to production environments](https://mlflow.org/docs/latest/ml/#deploy-models-to-production-environments)
    * [Explore Native MLflow ML Library Integrations](https://mlflow.org/docs/latest/ml/#explore-native-mlflow-ml-library-integrations)
    * [Evaluate and validate your ML models](https://mlflow.org/docs/latest/ml/#evaluate-and-validate-your-ml-models)
  * [Running MLflow for ML Models Anywhere](https://mlflow.org/docs/latest/ml/#running-mlflow-for-ml-models-anywhere)


© 2025 MLflow Project, a Series of LF Projects, LLC.
[Components](https://mlflow.org)
[Releases](https://mlflow.org/releases)
[Blog](https://mlflow.org/blog)
[Docs](https://mlflow.org/docs/latest/)
[Ambassador Program](https://mlflow.org/ambassadors)

