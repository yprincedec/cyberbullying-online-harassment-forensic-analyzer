# Methodology

## 1. Task Formulation

Let each comment be a text sample (x_i). Each sample has a target vector:

[
y_i = [y_{i1}, y_{i2}, ldots, y_{i6}], quad y_{ij} in {0,1}
]

The six binary targets represent toxic, severe toxic, obscene, threat, insult, and identity hate. Multiple entries in the vector may be 1, so the task is multi-label classification rather than mutually exclusive multi-class classification.

## 2. Dataset Validation

The notebook loads the labelled training file and checks that the identifier, comment text, and all six label columns exist. It inspects the shape, data types, missing values, and duplicate rows.

Dataset checks should be repeated for every downloaded copy. A dataset's familiar published row count is a reference point, not a substitute for validating the actual file.

## 3. Exploratory Analysis

The notebook studies:
- positive example counts by label;
- number of positive labels per comment;
- comment character length and word count;
- frequent alphabetic terms after lowercasing and basic stop-word filtering;
- relationships between predicted toxicity labels in the evidence output.

These analyses describe the sample. They do not establish why a comment was written or whether it constitutes a real-world threat.

## 4. Train/Test Separation and TF-IDF

Raw comments and their target vectors are split before fitting the TF-IDF vectorizer. The vectorizer learns its vocabulary and inverse-document-frequency statistics from the training comments only. The test comments are transformed using the fitted training vectorizer.

TF-IDF represents a term using its frequency in a document and its inverse frequency across the training corpus. The notebook limits the feature vocabulary to 10,000 features.

## 5. Classical Models

### One-vs-Rest Logistic Regression
A separate binary Logistic Regression estimator is trained for each label. This is a practical baseline for sparse text features. Regularization helps control model complexity.

### One-vs-Rest Linear SVM
A separate Linear Support Vector Classifier is trained for each label. Linear SVMs are useful for high-dimensional sparse text because they can learn effective linear decision boundaries.

Both classical approaches are evaluated on the same held-out text split.

## 6. BiLSTM Model

The deep-learning path tokenizes the training text, caps the vocabulary at 20,000 tokens, converts comments to integer sequences, and pads/truncates sequences to a maximum length of 200.

A Bidirectional LSTM reads each sequence in forward and backward directions. The output layer has six sigmoid units, one per label. Binary cross-entropy is used for the multi-label target vector.

The notebook trains for three epochs with a batch size of 128 and uses a validation fraction from the training data. These are experimental settings, not a claim that the configuration is optimal.

The current notebook uses a fixed binary decision threshold when converting predicted probabilities to labels. Any threshold change must be documented and applied consistently.

## 7. Evaluation

For each label, calculate precision, recall, and F1-score. Also calculate micro-averaged metrics for an aggregate view. Per-label reporting is essential because the classes are imbalanced and rare labels can be obscured by a single aggregate score.

For a binary label:

[
Precision = \frac{TP}{TP+FP}, \quad
Recall = \frac{TP}{TP+FN}
]

[
F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision+Recall}
]

Zero-division handling should be stated. Compare models only when they use the same held-out rows, label definitions, and thresholding policy.

## 8. Evidence Record Construction

For each held-out comment, create a record with:
- generated evidence ID;
- original comment text;
- six predicted binary labels;
- total predicted positive-label count;
- severity band;
- SHA-256 digest.

The record uses model predictions, not the ground-truth labels, for its toxicity fields. This is important when interpreting the evidence table.

## 9. Severity Heuristic

The notebook maps the number of predicted positive labels to a project-defined band:
- zero → Non-Toxic;
- one → Low;
- two or three → Medium;
- four or more → High.

This is a simple count heuristic. It is not a validated risk score. In particular, a single threat prediction may warrant review even though the count-based rule assigns Low. A future version should introduce label-aware triage and human review.

## 10. SHA-256 Integrity Design

The notebook builds a canonical payload from the evidence ID, original comment, six predicted labels, toxicity count, and severity. It serializes the payload with stable key ordering and compact JSON separators, encodes it as UTF-8, and computes SHA-256.

The stored digest is compared with a newly calculated digest. After CSV export, the CSV is reloaded and the same verification is repeated.

This design detects changes to the fields included in the payload. It does not provide a trusted timestamp, prove source authenticity, protect against a malicious actor who can rewrite both the record and digest, or create a formal chain of custody. A production system would need authenticated event logging, access controls, trusted timestamping, immutable storage, and documented evidence handling.

## 11. Reproducibility

Record the dataset version, train/test split, random seed, TF-IDF configuration, model hyperparameters, tokenizer settings, sequence length, epochs, batch size, threshold, library versions, and evaluation outputs. Re-run all notebook cells from a fresh runtime before publishing final metrics.
