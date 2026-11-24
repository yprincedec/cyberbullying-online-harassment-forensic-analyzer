# Cyberbullying & Online Harassment Forensic Analyzer

**A multi-label NLP classification and evidence-integrity project using the Jigsaw Toxic Comment dataset.**

This repository explores how machine-learning models can identify toxic language in online comments and how model outputs can be recorded in structured, tamper-evident evidence files for later review.

> **Research/portfolio prototype — not a production moderation, legal, or law-enforcement system.** Model predictions are probabilistic, can be wrong, and require human review.

## 1. Project at a Glance

| Area | Implementation |
|---|---|
| Problem | Identify potentially toxic or abusive online comments |
| Dataset | Jigsaw Toxic Comment Classification Challenge |
| Task | Multi-label text classification |
| Labels | toxic, severe_toxic, obscene, threat, insult, identity_hate |
| Text representation | TF-IDF for classical ML; token sequences for BiLSTM |
| Classical models | One-vs-Rest Logistic Regression and Linear SVM |
| Deep-learning model | Bidirectional LSTM (BiLSTM) |
| Evaluation | Per-label classification report, precision, recall, F1, model comparison |
| Evidence workflow | Evidence IDs, predicted labels, project-defined severity bands |
| Integrity | SHA-256 hash over a canonical structured evidence record |
| Export | CSV export and post-export hash verification |
| Environment | Python, Google Colab / Jupyter |

## 2. Why This Project Matters

Online comments can contain several kinds of harmful language at once. A single-label classifier would force each comment into only one category, even when it contains multiple forms of abuse. This project therefore uses a **multi-label** setup: each comment can receive zero, one, or several of the six Jigsaw labels.

The project has two distinct technical components:

1. **NLP and machine learning:** transform text into numerical features, train classifiers, and evaluate predictions.
2. **Forensic-style record handling:** preserve the model's output alongside the original comment, assign a stable evidence identifier, calculate a SHA-256 digest, export records, and verify that the exported records have not changed.

The hash component checks record integrity after hashing. It does not prove who wrote a comment, when it was originally published, or whether the input was authentic.

## 3. Dataset

The project uses the [Jigsaw Toxic Comment Classification Challenge dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data).

The labelled training file contains the comment identifier, comment text, and six binary target columns. The commonly distributed training file has 159,571 rows; verify the downloaded file's shape in the notebook rather than assuming every copy is identical.

### Target labels

| Label | Meaning in the dataset |
|---|---|
| `toxic` | General toxic language |
| `severe_toxic` | More severe toxic language |
| `obscene` | Obscene language |
| `threat` | Threatening language |
| `insult` | Insulting language |
| `identity_hate` | Identity-based hateful language |

The labels are not mutually exclusive. The dataset's annotations are the training targets, not a complete or universally applicable definition of harmful speech.

**Dataset handling:** download the dataset from Kaggle after accepting its terms. The dataset is intentionally not committed to this repository. Do not upload the full ZIP, raw comments, or other large/private data files to GitHub.

## 4. Workflow

### Phase A — Data loading and validation
- Upload the Jigsaw ZIP or `train.csv` in Google Colab.
- Extract the archive and locate `train.csv`.
- Check that the identifier, text, and six target columns exist.
- Inspect dimensions, data types, missing values, and duplicate rows.

### Phase B — Exploratory data analysis
- Count positive examples for each toxicity label.
- Examine how many labels are assigned to each comment.
- Calculate comment character length and word count.
- Review frequent words after basic normalization.
- Plot label counts, label-count distribution, text lengths, and frequent terms.

EDA is descriptive. Frequent words or label correlations do not establish causation or intent.

### Phase C — Text representation and split
- Keep the raw comment text as the model input.
- Split the rows into training and held-out test subsets.
- Fit the TF-IDF vectorizer on training comments only.
- Transform the held-out comments with the already-fitted vectorizer.

This order is important: fitting TF-IDF on the full dataset would allow information from the held-out text distribution to influence feature construction.

### Phase D — Model training
The notebook compares three approaches:

- **One-vs-Rest Logistic Regression:** trains one binary classifier per label and provides a strong, interpretable classical baseline.
- **One-vs-Rest Linear SVM:** learns a linear decision boundary for each label and is commonly effective for sparse, high-dimensional text features.
- **BiLSTM:** tokenizes the text, pads sequences to a fixed length, and learns contextual sequence representations in both directions.

The BiLSTM uses a neural embedding and recurrent sequence model. Its results should be compared using the same held-out rows and clearly stated thresholds.

### Phase E — Evaluation
The notebook reports precision, recall, and F1-score, including per-label reports and aggregate comparisons.

- **Precision:** among predicted positives, how many were correct?
- **Recall:** among actual positives, how many were found?
- **F1-score:** harmonic mean of precision and recall.
- **Micro average:** aggregates label-level decisions before calculating the metric; frequent labels influence it more.
- **Per-label scores:** expose weak performance on rare labels that can be hidden by an aggregate score.

Because the labels are imbalanced, accuracy alone is not a sufficient evaluation measure. Report the split strategy, random seed, threshold, and averaging method with any published score.

### Phase F — Forensic-style evidence generation
For each held-out comment, the notebook creates a record containing:
- a generated evidence identifier;
- the original comment text;
- six model-predicted binary labels;
- the count of predicted positive labels;
- a project-defined severity band;
- a SHA-256 digest of a canonical representation of the structured record.

The current severity rule is a simple count-based triage heuristic:
- 0 predicted labels → Non-Toxic
- 1 predicted label → Low
- 2–3 predicted labels → Medium
- 4–6 predicted labels → High

These bands are **project-defined categories only**. They are not clinically, legally, or operationally validated threat levels. A single threat prediction may require human attention even if the count-based band is Low.

### Phase G — Integrity and export
- Recalculate a record's digest and compare it with the stored digest.
- Export the evidence dataframe to CSV.
- Reload the CSV and verify hashes again.

A matching hash indicates that the fields included in the canonical hash payload match the hashed version. A mismatch indicates a change or serialization inconsistency that should be investigated. SHA-256 alone does not provide trusted timestamps, chain of custody, source authentication, or non-repudiation.

## 5. Repository Structure

```text
.
├── README.md
├── AI_USAGE.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── Cyberbullying_Project_Fixed.ipynb
├── src/
│   ├── evaluation.py
│   └── forensic_integrity.py
├── tests/
│   └── test_forensic_integrity.py
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── METHODOLOGY.md
│   └── PROJECT_ROADMAP.md
├── reports/
└── outputs/
```

The notebook is the main end-to-end learning workflow. The `src/` modules provide reusable helper functions; they are not yet a replacement for every notebook cell.

## 6. Run the Project

### Option A — Google Colab
1. Open `notebooks/Cyberbullying_Project_Fixed.ipynb` on GitHub.
2. Select **Open in Colab** (or download the notebook and upload it to Colab).
3. Start a fresh runtime.
4. Upload the Kaggle Jigsaw dataset ZIP when prompted.
5. Run the notebook from top to bottom.
6. Review the model reports, evidence summary, and hash verification output.

The BiLSTM section can require substantial RAM/GPU time. If a Colab session limit is reached, wait for capacity or use a smaller experimental sample for debugging only. Do not report sample-run metrics as full-dataset results.

### Option B — Local Python environment
Use Python 3.10+ and install the dependencies:

```bash
git clone https://github.com/yprincedec/cyberbullying-online-harassment-forensic-analyzer.git
cd cyberbullying-online-harassment-forensic-analyzer
python -m venv .venv
```

Activate the environment and run:

```bash
pip install -r requirements.txt
jupyter notebook
```

The notebook's dataset upload cell uses Google Colab's upload interface. For local execution, replace that cell with a local path to the extracted `train.csv`.

### Run the helper tests

```bash
python -m unittest discover -s tests -v
```

## 7. Reproducibility Checklist

Before publishing results:
- [ ] Record dataset source and file version.
- [ ] Record dataset row count and required-column validation.
- [ ] Record train/test split strategy and random seed.
- [ ] Confirm TF-IDF is fitted only on training text.
- [ ] Record vectorizer settings and vocabulary size.
- [ ] Record BiLSTM tokenizer vocabulary, sequence length, epochs, batch size, and threshold.
- [ ] Report per-label precision, recall, and F1.
- [ ] State whether aggregate metrics are micro, macro, or weighted.
- [ ] Run the complete notebook from a fresh runtime.
- [ ] Confirm CSV export/reload hash checks pass.
- [ ] Keep generated metrics and charts tied to the exact notebook run.

No benchmark table is published here yet because the full corrected notebook has not been freshly rerun end-to-end in a clean runtime.

## 8. Known Limitations and Responsible Use

- Jigsaw labels reflect the dataset's annotation scheme and may not generalize to every platform, language, community, or cultural context.
- The dataset is English-centric; performance on other languages and dialects is not established.
- Rare labels, especially threat-related labels, can have limited examples and unstable metrics.
- Text-only models may miss sarcasm, quotation, reclaimed language, conversation context, and target identity.
- False positives can unfairly flag benign or contextually appropriate speech; false negatives can miss harmful content.
- The count-based severity rule treats the number of predicted categories as a proxy for triage and can understate the importance of a single threat label.
- Hash verification detects changes to hashed fields; it does not authenticate the original source or establish a legal chain of custody.
- The notebook is not an interactive dashboard or deployed moderation service.

Use outputs for research and human-reviewed triage only. Do not automatically punish, ban, report, or make legal conclusions about a person from model predictions.

## 9. Roadmap

See [docs/PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md) for the planned validation, explainability, fairness, dashboard, and deployment work.

## 10. Author

**Prince Yadav**  
M.Sc. Computer Science, University of Delhi

GitHub: [@yprincedec](https://github.com/yprincedec)

## License

This repository's original code and documentation are released under the MIT License. The Jigsaw dataset remains subject to its own source terms; see Kaggle for details.
