# Project Roadmap

This roadmap separates implemented notebook functionality from planned improvements. Items are not considered complete until implemented, tested, and documented.

## Current Repository State

- [x] Corrected 64-cell Colab notebook committed.
- [x] ZIP upload and train.csv discovery logic included.
- [x] Required dataset columns validated.
- [x] Raw comments split before TF-IDF fitting.
- [x] Logistic Regression, Linear SVM, and BiLSTM training workflows included in the notebook.
- [x] Per-label and aggregate evaluation code included.
- [x] Evidence record generation and project-defined severity rule included.
- [x] SHA-256 hashing and CSV reload verification code included.
- [ ] Full notebook rerun from a fresh runtime after the corrections.
- [ ] Fresh model metrics captured and reviewed.
- [ ] Original project report PDF added after its source file is recovered and checked.

## Priority 1 — Reproducible Model Evaluation

- Run all notebook cells in a clean Colab runtime.
- Save the actual classification reports and model comparison table.
- Record environment versions, random seeds, split settings, and threshold.
- Inspect per-label precision/recall, especially rare labels.
- Add a concise results report only after the run succeeds.

**Acceptance criteria:** all cells complete without errors, outputs are tied to the same split, and reported metrics can be reproduced.

## Priority 2 — Stronger Validation

- Add repeated-seed evaluation or cross-validation where computationally feasible.
- Consider iterative multi-label stratification to better preserve label prevalence.
- Tune thresholds on a validation set rather than the held-out test set.
- Include macro-F1 and per-label precision/recall alongside micro-F1.
- Inspect false positives and false negatives using privacy-safe examples.

**Acceptance criteria:** evaluation decisions are documented and the final test set is not used for threshold tuning.

## Priority 3 — Better Forensic Triage

- Replace count-only severity with a transparent label-aware review policy.
- Ensure a threat prediction can trigger review independently of the number of other labels.
- Add human-review status and reviewer notes only if the workflow has appropriate privacy controls.
- Document the difference between prediction confidence and real-world risk.

**Acceptance criteria:** every severity rule is explicit, tested, and described as a heuristic rather than a legal finding.

## Priority 4 — Integrity and Audit Improvements

- Add tests for modified comment text, labels, severity, and evidence IDs.
- Define canonical field types and missing-value handling.
- Consider an export manifest containing file hash, row count, creation time, software version, and model version.
- For real evidence workflows, use authenticated logs, trusted timestamps, restricted access, and immutable storage.

**Acceptance criteria:** tampering tests detect changes to every protected field and documentation clearly states what the hash does not prove.

## Priority 5 — Maintainable Source Code

- Refactor notebook logic into importable modules.
- Add type hints, docstrings, configuration objects, and unit tests.
- Keep the notebook as an orchestration and explanation layer.
- Add a small synthetic test dataset so tests do not require the full Jigsaw dataset.

**Acceptance criteria:** helper modules and notebook produce consistent outputs and tests run without downloading the dataset.

## Priority 6 — Explainability and Fairness

- Review false positives across dialects, identity terms, and quoted speech.
- Add error-analysis examples with private or harmful text redacted where possible.
- Compare label-level performance across relevant slices only where lawful, ethical, and supported by the data.
- Document dataset limitations and avoid treating model scores as objective truth.

**Acceptance criteria:** limitations and error patterns are included in the report; no unsupported fairness claim is made.

## Priority 7 — Dashboard / Deployment (Future Work)

- Build an interactive dashboard only after model and evidence logic are stable.
- Add a human-in-the-loop review flow.
- Add model/version metadata and clear warnings.
- Do not expose raw comment text publicly or log it unnecessarily.

**Acceptance criteria:** a working, tested application exists before the README or resume claims dashboard/deployment functionality.
