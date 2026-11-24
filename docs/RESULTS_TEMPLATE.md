# Experiment Results — Template

> Do not fill this page with estimated, remembered, or AI-generated scores. Complete it only from a successful run of the committed notebook.

## Run metadata

| Field | Value |
|---|---|
| Run date | TODO |
| Dataset source/version | TODO |
| Training file row count | TODO |
| Python version | TODO |
| TensorFlow version | TODO |
| scikit-learn version | TODO |
| Runtime (CPU/GPU) | TODO |
| Random seed | TODO |
| Train/test split | TODO |
| TF-IDF maximum features | 10,000 (notebook setting; verify run) |
| BiLSTM vocabulary / sequence length | TODO |
| Prediction threshold | TODO |

## Model comparison

| Model | Precision (micro) | Recall (micro) | F1 (micro) | F1 (macro) |
|---|---:|---:|---:|---:|
| One-vs-Rest Logistic Regression | TODO | TODO | TODO | TODO |
| One-vs-Rest Linear SVM | TODO | TODO | TODO | TODO |
| BiLSTM | TODO | TODO | TODO | TODO |

## Per-label metrics

| Label | Model | Precision | Recall | F1 |
|---|---|---:|---:|---:|
| toxic | TODO | TODO | TODO | TODO |
| severe_toxic | TODO | TODO | TODO | TODO |
| obscene | TODO | TODO | TODO | TODO |
| threat | TODO | TODO | TODO | TODO |
| insult | TODO | TODO | TODO | TODO |
| identity_hate | TODO | TODO | TODO | TODO |

## Evidence integrity checks

| Check | Result |
|---|---|
| Evidence rows exported | TODO |
| Evidence rows reloaded | TODO |
| Hashes valid | TODO |
| Hashes invalid | TODO |
| Deliberate tampering test | TODO |

## Error analysis

Describe representative false positives and false negatives without publishing personal or sensitive comment content. Explain where context, dialect, sarcasm, quotation, or label imbalance may affect predictions.

## Interpretation

Summarize what the metrics do and do not demonstrate. Do not claim the model detects intent, determines legal threats, or is suitable for automatic moderation.

## Reproduction instructions

Record the notebook commit, dataset version, runtime settings, and exact steps needed to reproduce the result.
