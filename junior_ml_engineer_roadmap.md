# Junior ML Engineer Roadmap (1–2 Years)

> A structured month-by-month plan to go from ML beginner to job-ready Junior ML Engineer.
> 
> **Prerequisite:** Complete the Python + DSA roadmap first (see ROADMAP.md — 10 weeks).
> **This roadmap assumes** you're comfortable with Python, OOP, DSA basics, NumPy, Pandas, Git, and SQL.

---

## Phase 0: Math & Stats Foundations (Month 0)

> Complete this BEFORE starting ML. Skip topics you're already comfortable with.

### Week 1–2: Linear Algebra
- Vectors, matrices, matrix multiplication
- Dot product, transpose, inverse
- Eigenvalues & eigenvectors (intuition, not proofs)
- Why it matters: every ML model is matrix math under the hood

### Week 3: Calculus for ML
- Derivatives & partial derivatives
- Chain rule (this IS backpropagation)
- Gradient: direction of steepest ascent
- You don't need to be a math wizard — just understand what gradients mean

### Week 4: Probability & Statistics
- Mean, median, mode, variance, standard deviation
- Probability distributions: normal, uniform, Bernoulli, Poisson
- Bayes' theorem
- Hypothesis testing, p-values, confidence intervals
- Correlation vs causation

**Resources:**
- 3Blue1Brown: Essence of Linear Algebra (YouTube — best visual intro)
- 3Blue1Brown: Essence of Calculus
- Khan Academy: Statistics & Probability
- StatQuest with Josh Starmer (YouTube — ML-focused stats)

**Self-test:** Can you explain what a gradient is, multiply two matrices, and interpret a p-value? If yes, move on.

---

## Phase 1: ML Foundations (Months 1–3)

### Month 1 — Supervised Learning Core

**Week 1–2: Linear Models**
- Linear Regression (simple & multiple)
- Gradient Descent (batch, stochastic, mini-batch)
- Cost functions (MSE, MAE)
- Regularization: L1 (Lasso), L2 (Ridge), ElasticNet
- Bias-variance tradeoff

**Week 3–4: Classification**
- Logistic Regression
- Decision Trees & Random Forests
- Support Vector Machines (SVM)
- Evaluation metrics: accuracy, precision, recall, F1, AUC-ROC, confusion matrix
- Cross-validation (k-fold, stratified)

**Production mindset from Day 1:**
- For every model you build, ask: "How would I deploy this? How would I know if it breaks?"
- Log your experiments (even informally) — this habit pays off later

**Projects:**
- Predict house prices (regression)
- Classify spam emails (classification)

**Resources:**
- Andrew Ng's ML Specialization (Coursera) — Course 1
- Scikit-learn documentation & tutorials
- "Hands-On ML with Scikit-Learn" by Aurélien Géron — Chapters 1–6

---

### Month 2 — EDA, Statistics & Feature Engineering

**Week 1: Exploratory Data Analysis (EDA)**
- Summary statistics & distributions
- Visualizing data: histograms, box plots, scatter plots, pair plots
- Identifying outliers & anomalies
- Correlation matrices & heatmaps
- Telling a story with data — EDA is how you understand your problem

**Week 2: Unsupervised Learning**
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN
- PCA (Principal Component Analysis)
- t-SNE for visualization

**Week 3–4: Feature Engineering**
- Handling missing data (imputation strategies)
- Encoding categorical variables (one-hot, label, target encoding)
- Feature scaling (standardization, normalization)
- Feature selection (correlation, mutual information, recursive elimination)
- Handling imbalanced datasets (SMOTE, class weights, under/oversampling)

**Projects:**
- Full EDA notebook on a messy real-world dataset (Kaggle)
- Customer segmentation using clustering
- Build a feature engineering pipeline

**Resources:**
- Kaggle Learn: Data Visualization + Feature Engineering courses
- Scikit-learn preprocessing docs
- "Storytelling with Data" by Cole Nussbaumer Knaflic (for EDA communication)

---

### Month 3 — Ensemble Methods & Model Selection

**Week 1–2: Ensemble Techniques**
- Bagging (Random Forest in depth)
- Boosting: AdaBoost, Gradient Boosting
- XGBoost, LightGBM, CatBoost
- Stacking & blending

**Week 3: Model Selection & Tuning**
- Hyperparameter tuning: GridSearch, RandomSearch, Bayesian Optimization (Optuna)
- Pipeline construction with Scikit-learn
- Model persistence (joblib, pickle)
- Experiment tracking basics (MLflow or W&B)

**Week 4: Model Explainability (New — Critical for 2026)**
- SHAP (SHapley Additive exPlanations) — understand feature importance
- LIME (Local Interpretable Model-agnostic Explanations)
- Feature importance plots
- Why it matters: interviewers ask "How do you explain this model to a stakeholder?"

**Projects:**
- Kaggle competition: Tabular Playground Series (aim for top 30%)
- End-to-end ML pipeline with experiment tracking
- Explainability report: SHAP analysis on your best model

**Resources:**
- XGBoost documentation
- MLflow quickstart guide
- SHAP documentation & tutorials

---

## Phase 2: Deep Learning (Months 4–6)

### ⚡ Parallel Track: DSA & Coding Practice (Continues from Python Phase)

> You already completed 2 weeks of DSA fundamentals in the Python roadmap.
> Now continue as a daily habit alongside deep learning — 30–45 min/day.

**Month 4–6:** LeetCode Easy/Medium (3–4 per week)
- Build on your DSA foundation (arrays, strings, hash maps, trees, BFS/DFS)
- Add: sliding window, binary search variations, graph problems
- Focus on patterns, not memorizing solutions

**Month 7–9:** LeetCode Medium (3–4 per week)
- Dynamic programming basics
- Advanced tree/graph problems
- Practice explaining your approach out loud

**Month 10–12:** LeetCode Medium + ML-specific coding
- Implement ML algorithms from scratch (linear regression, k-means, decision tree)
- Timed practice sessions (45 min per problem)
- Mock interview format

**Target:** 50+ problems solved by Month 11, comfortable with easy/medium

---

### Month 4 — Neural Network Fundamentals

**Week 1–2: Core Concepts**
- Perceptrons & multi-layer networks
- Activation functions (ReLU, sigmoid, tanh, softmax)
- Backpropagation (understand the math)
- Loss functions (cross-entropy, MSE)
- Optimizers: SGD, Adam, RMSprop, learning rate scheduling

**Week 3–4: Practical Deep Learning**
- PyTorch basics: tensors, autograd, nn.Module, DataLoader
- Training loop: forward pass → loss → backward → update
- Regularization: dropout, batch normalization, early stopping
- GPU training basics

**Projects:**
- MNIST digit classifier from scratch in PyTorch
- Fashion-MNIST with custom architecture

**Resources:**
- fast.ai Practical Deep Learning — Part 1 (Lessons 1–3)
- PyTorch official tutorials
- 3Blue1Brown: Neural Networks series (YouTube)

---

### Month 5 — CNNs & Computer Vision Basics

**Week 1–2: Convolutional Neural Networks**
- Convolution, pooling, stride, padding
- Classic architectures: LeNet, AlexNet, VGG, ResNet
- Transfer learning & fine-tuning pretrained models
- Data augmentation techniques

**Week 3–4: Practical CV**
- Image classification on custom datasets
- Object detection concepts (YOLO, SSD overview)
- Using torchvision & pretrained models
- Grad-CAM for model interpretability

**Projects:**
- Image classifier on a custom dataset (collect your own images)
- Transfer learning: fine-tune ResNet on a domain-specific task

**Resources:**
- fast.ai Part 1 (Lessons 4–7)
- CS231n lecture notes (Stanford)

---

### Month 6 — NLP, Transformers & GenAI/LLMs

**Week 1: Sequence Models & Transformers**
- RNNs, LSTMs, GRUs (overview — understand the concepts, don't go deep, market has moved on)
- Attention mechanism (Bahdanau, Luong)
- Word embeddings: Word2Vec, GloVe
- "Attention Is All You Need" — understand the Transformer architecture
- Self-attention, multi-head attention, positional encoding
- BERT (encoder), GPT (decoder) — architecture differences
- Tokenization (BPE, WordPiece, SentencePiece)

**Week 2: LLMs & GenAI (Critical for 2026 Market)**
- How LLMs work: pretraining, instruction tuning, RLHF
- Prompt engineering: zero-shot, few-shot, chain-of-thought
- RAG (Retrieval-Augmented Generation): why, when, how
- Vector databases: Pinecone, Chroma, FAISS
- LangChain / LlamaIndex basics

**Week 3: Fine-tuning & Practical LLM Work**
- Fine-tuning with LoRA / QLoRA (parameter-efficient)
- Hugging Face: Transformers, Datasets, PEFT libraries
- Evaluating LLM outputs (BLEU, ROUGE, human eval, LLM-as-judge)
- AI agents & tool use (overview)
- Cost & latency considerations for LLM deployment

**Projects:**
- Sentiment analysis using BERT (Hugging Face)
- Build a RAG chatbot over your own documents
- Fine-tune a small LLM (e.g., Llama/Mistral) on a custom task with LoRA

**Resources:**
- Hugging Face NLP Course (free)
- Jay Alammar's "The Illustrated Transformer"
- Andrej Karpathy's "Let's build GPT" (YouTube)
- LangChain documentation
- fast.ai Part 2

---

## Phase 3: MLOps & Production Skills (Months 7–9)

> ⚠️ **2026 Reality Check:** MLOps is THE #1 hiring differentiator.
> Companies say "the model is only 10–20% of the ML lifecycle."
> Interviewers now test: monitoring, drift, rollback, pipeline design, operational tradeoffs.
> "Simple but robust > Fancy but fragile" — this is the 2026 mindset.

### Month 7 — Data Engineering, Pipelines & Orchestration

**Week 1–2: Data Handling at Scale**
- SQL for ML: advanced queries, window functions, CTEs (deepen what you learned in Python Phase)
- Working with large datasets: chunking, Dask, Polars
- Data versioning with DVC
- Basic ETL concepts
- Data quality: validation with Great Expectations or Pandera

**Week 3–4: ML Pipelines & Orchestration**
- Scikit-learn Pipelines (end-to-end)
- Pipeline orchestration: Airflow or Prefect (pick one)
- Feature stores concept (Feast overview)
- Reproducibility: random seeds, environment management, pinned dependencies
- CI/CD for ML: automated testing, model validation gates

**Projects:**
- Build a reproducible ML pipeline with DVC + Git
- Automated data validation pipeline
- Simple Airflow DAG that trains → evaluates → logs a model

**Resources:**
- DVC documentation
- Apache Airflow tutorials
- "Designing ML Systems" by Chip Huyen — Chapters 1–5

---

### Month 8 — Model Deployment & Cloud

**Week 1–2: Serving Models**
- REST APIs with FastAPI (you covered basics in Python Phase — go deeper now)
- Model serialization (ONNX, TorchScript, joblib)
- Model optimization: quantization (INT8, GPTQ), pruning, distillation basics
- Docker for ML (you covered basics in Python Phase — now containerize ML models)
- CI/CD for ML: GitHub Actions → build → test → deploy
- Model versioning & rollback strategies
- Kubernetes basics (overview — understand pods, deployments, services)

**Week 3–4: Cloud Deployment (Pick AWS or GCP)**

AWS Track:
- S3 — store datasets, models, artifacts
- EC2 / Lambda — compute for training & inference
- IAM — permissions & security basics
- SageMaker — managed training, endpoints, batch transform
- ECR — container registry for Docker images
- CloudWatch — logging & monitoring
- Cost management — spot instances, right-sizing, billing alerts

GCP Track:
- GCS — storage
- Compute Engine / Cloud Functions — compute
- IAM — permissions
- Vertex AI — managed ML platform
- Artifact Registry — containers
- Cloud Monitoring — logging
- Cost management — preemptible VMs, budgets

**Both tracks cover:**
- Batch vs real-time inference tradeoffs
- Load testing basics (Locust or k6)
- Infrastructure as code concepts (Terraform overview)

**Projects:**
- Deploy a model as a REST API with FastAPI + Docker + CI/CD
- Deploy to cloud with a simple frontend
- Set up a complete training → serving pipeline on your chosen cloud

**Resources:**
- FastAPI documentation
- Docker for Data Science tutorials
- Made With ML — MLOps section
- Your chosen cloud provider's ML documentation & free tier

---

### Month 9 — Monitoring, LLMOps & ML System Design

**Week 1: Model Monitoring & Drift Detection**
- Data drift & concept drift — what they are, how to detect them
- Model performance monitoring in production
- Logging & alerting for ML systems
- A/B testing for models
- Tools: Evidently AI, Whylogs, or custom dashboards

**Week 2: LLMOps (New — Critical for 2026)**
- Monitoring LLM outputs: hallucination detection, quality scoring
- Prompt versioning & management
- RAG pipeline monitoring: retrieval quality, context relevance
- Cost tracking for LLM inference
- Guardrails & safety filters
- Evaluating LLM systems in production (automated evals)

**Week 3: AI Ethics & Responsible AI (New — Increasingly Tested)**
- Bias detection & mitigation in ML models
- Fairness metrics (demographic parity, equalized odds)
- Model explainability in production (SHAP, LIME — applied)
- AI safety basics: alignment, robustness
- Compliance considerations (EU AI Act overview, data privacy)
- When to NOT use ML — knowing the limits

**Week 4: ML System Design (Interview-Critical)**
- End-to-end ML system design patterns
- Practice designing these systems:
  - Recommendation system (e.g., Netflix/Spotify)
  - Fraud detection system (e.g., Stripe)
  - Search ranking system (e.g., Google)
  - LLM-powered chatbot with RAG
- When to use ML vs heuristics
- Technical debt in ML systems (Google's "Hidden Technical Debt" paper)
- Cost-performance tradeoffs
- Operational tradeoff conversations (batch vs streaming, latency vs throughput, explainability vs performance)

**Projects:**
- Add monitoring + drift detection to your deployed model
- Design doc: ML system for a real-world problem (write it like a real design doc)
- Build a simple LLM evaluation pipeline

**Resources:**
- "Designing ML Systems" by Chip Huyen — Chapters 6–11
- Evidently AI documentation
- "ML System Design Interview" by Ali Aminian
- Google's "Hidden Technical Debt in ML Systems" paper

---

## Phase 4: Portfolio, Soft Skills & Job Prep (Months 10–12)

### Month 10 — Portfolio Projects

Build 2–3 strong portfolio projects that demonstrate:

| Project | Skills Shown |
|---|---|
| End-to-end ML app (deployed + monitored) | Full pipeline, deployment, monitoring, API |
| RAG / LLM application | GenAI skills, vector DBs, prompt engineering, LLMOps |
| Kaggle competition (top 20%) | Model building, feature engineering, explainability |
| Open-source contribution | Collaboration, code quality, Git workflow |

Pick 2–3 from above. Each project should have:
- Clean GitHub repo with README
- Problem statement & approach explanation
- Results with metrics
- Deployed demo (if applicable)
- Blog post explaining what you built and learned
- Monitoring/observability component (this sets you apart in 2026)

---

### Month 11 — Interview Preparation

**Technical:**
- ML theory questions (bias-variance, overfitting, regularization, metrics)
- Coding: LeetCode easy/medium (you should have 50+ done by now from parallel track)
- ML system design: recommendation system, fraud detection, search ranking, RAG chatbot
- MLOps questions: "How would you monitor this?", "What's your rollback strategy?", "How do you detect drift?"
- LLM-specific questions: RAG architecture, fine-tuning decisions, prompt engineering, hallucination handling
- Take-home assignments: practice end-to-end ML tasks with time constraints

**Behavioral & Soft Skills (Underrated but Critical):**
- STAR method for project discussions
- Explain your projects clearly to non-technical people — practice this weekly
- Know your resume deeply — every bullet point
- Practice "operational tradeoff conversations" — interviewers love these in 2026
- Write about what you've learned (blog, LinkedIn) — shows communication skills

**Resources:**
- "Ace the Data Science Interview" by Nick Singh
- ML interview repos on GitHub (khangich/machine-learning-interview)
- System design: "ML System Design Interview" by Ali Aminian
- InterviewNode blog (excellent for understanding what recruiters want)

---

### Month 12 — Job Search & Networking

- Apply to 5–10 positions per week
- Tailor resume for each role (highlight relevant projects + production skills)
- Network: LinkedIn, ML meetups, Discord communities, Twitter/X
- Contribute to open source for visibility
- Write blog posts about your projects and learnings
- Practice mock interviews (Pramp, interviewing.io)
- Target roles: ML Engineer, AI Engineer, Applied Scientist, MLOps Engineer

---

## Daily Habits Throughout the Roadmap

> See `daily_routine_plan.md` for the full daily schedule with checklists and phase-specific routines.

| Activity | Time |
|---|---|
| Study / courses | 1–2 hours |
| Coding practice (LeetCode from Month 4+) | 30–45 min |
| Read papers / blogs | 15–30 min |
| Build projects | 1–2 hours (weekends heavy) |
| Explain something you learned (to a friend, blog, or rubber duck) | 10 min |

---

## Key Tools to Master

```
Already covered in Python Phase:
  Python, NumPy, Pandas, Matplotlib, Seaborn, FastAPI, Docker, pytest, Git, SQL

New in ML Phase:
  ML Libraries:    Scikit-learn, XGBoost, LightGBM
  Deep Learning:   PyTorch (primary), basics of TensorFlow
  Data:            Polars (for large datasets)
  Visualization:   Plotly (interactive)
  NLP/LLMs:        Hugging Face Transformers, LangChain, FAISS/Chroma
  MLOps:           MLflow, DVC, Airflow/Prefect, Evidently AI
  Explainability:  SHAP, LIME
  Cloud:           AWS (S3, EC2, SageMaker, IAM) or GCP equivalent
  Dev Tools:       Linux CLI, Jupyter, VS Code
```

---

## Milestones Checklist

**Math & Foundations:**
- [ ] Can explain gradients, matrix multiplication, Bayes' theorem
- [ ] Complete Andrew Ng's ML Specialization
- [ ] Complete fast.ai Part 1

**Deep Learning & NLP:**
- [ ] Finish Hugging Face NLP Course
- [ ] Build and fine-tune a model with LoRA
- [ ] Build a RAG application

**MLOps & Production:**
- [ ] Deploy a model as a REST API with CI/CD
- [ ] Deploy a model to cloud (AWS/GCP)
- [ ] Set up model monitoring with drift detection
- [ ] Build an ML pipeline with orchestration (Airflow/Prefect)
- [ ] Write an ML system design doc

**Explainability & Ethics:**
- [ ] Generate SHAP explanations for a model
- [ ] Explain a model's decisions to a non-technical person
- [ ] Identify and mitigate bias in a dataset

**Portfolio & Career:**
- [ ] Score top 30% in a Kaggle competition
- [ ] Build 3 portfolio projects on GitHub (at least 1 deployed + monitored)
- [ ] Contribute to an open-source ML project
- [ ] Complete 50+ LeetCode problems
- [ ] Write 3+ blog posts about your projects
- [ ] Do 5+ mock interviews
- [ ] Get your first ML Engineer offer 🎯

---

## Common Mistakes to Avoid

1. **Spending too long on theory** — Build things early and often
2. **Skipping software engineering** — Production ML is 80% engineering
3. **Ignoring deployment & monitoring** — A model in a notebook isn't a product
4. **Only doing courses, no projects** — Projects > certificates
5. **Not learning Git properly** — Non-negotiable for any engineering role
6. **Chasing every new tool** — Master fundamentals first, then specialize
7. **Neglecting communication skills** — You'll need to explain models to non-ML people
8. **Cramming LeetCode at the end** — Start early, do a little daily
9. **Ignoring GenAI/LLMs** — The market demands these skills now
10. **Skipping math foundations** — You'll hit a wall in deep learning without them
11. **Treating MLOps as optional** — It's THE #1 hiring differentiator in 2026
12. **Not practicing ML system design** — Every serious interview has this round
13. **Building models without explainability** — "Why does your model predict this?" is a standard question

---

## What's Next After Junior?

Once you land your first role, focus on:
- Owning end-to-end ML systems
- Learning MLOps deeply (you have the foundation now)
- Picking a specialization (NLP, CV, RecSys, etc.)
- Reading research papers in your domain
- Mentoring others
- Contributing to AI ethics and responsible AI practices

> This leads to the **Mid-Level ML Engineer** stage (2–4 years).

---

*Roadmap created: March 11, 2026 | Updated: March 13, 2026*
*Research sources: NerdLevelTech AI Career Roadmap 2026, InterviewNode MLOps & Production ML analysis, IterAI ML Roadmap 2025*
