# AI Usage & Development Transparency

This document explains where AI assistance fits into the development of the Cyberbullying & Online Harassment Forensic Analyzer. AI is used as a support tool for learning, planning, coding assistance, debugging, review, and documentation. It is not treated as the project owner or as proof that an experiment succeeded.

## 1. Why AI Assistance Was Used

The project combines several areas that are easy to get wrong when implemented independently:
- multi-label NLP classification;
- high-dimensional sparse text features;
- imbalanced target labels;
- classical machine learning and a recurrent neural network;
- evaluation across six separate labels;
- structured evidence records and cryptographic integrity checks.

AI assistance helps break the work into understandable stages, explain unfamiliar concepts, review implementation decisions, and identify likely technical risks. The developer remains responsible for running, understanding, validating, and presenting the work.

## 2. Areas of AI Assistance

| Development stage | How AI assistance can help | What must be checked by the developer |
|---|---|---|
| Project planning | Break the project into EDA, NLP, modelling, evaluation, and evidence phases | The phases match the actual notebook and deliverables |
| Dataset understanding | Explain the six Jigsaw labels and multi-label structure | Column names, row counts, label values, and source terms |
| Data validation | Suggest checks for missing values, duplicates, and required columns | Actual checks against the downloaded dataset |
| EDA | Suggest useful label, length, and frequency analyses | Graphs and counts produced by a real run |
| NLP feature engineering | Explain TF-IDF, tokenization, vocabulary limits, and padding | Fit/transform order and preprocessing behaviour |
| Model design | Explain One-vs-Rest Logistic Regression, Linear SVM, and BiLSTM | Correct estimator setup, training completion, and comparable splits |
| Debugging | Interpret errors and suggest targeted fixes | The corrected cell runs in a fresh runtime |
| Evaluation | Explain precision, recall, F1, micro averaging, and class imbalance | Metrics are calculated from the correct predictions and targets |
| Forensic records | Review evidence IDs, severity rules, canonical serialization, and SHA-256 checks | Hash covers the intended fields and tampering tests behave as expected |
| Documentation | Improve README, methodology, limitations, and setup instructions | Documentation never claims unimplemented or unverified features |

## 3. Concrete Technical Review Priorities

AI-assisted review is particularly useful for checking the following failure modes:

### Data leakage
A text vectorizer learns vocabulary and inverse-document-frequency weights from the text it is fitted on. Fitting TF-IDF before splitting can allow information from the held-out test text to influence feature construction. The corrected notebook splits raw comments first, fits TF-IDF on training text, and transforms test text using that fitted vectorizer.

### Multi-label evaluation
The six labels are not mutually exclusive. Evaluation must compare each label independently and use a clearly stated averaging method. A single accuracy value would hide important errors and class imbalance.

### Neural-network reproducibility
A BiLSTM result depends on tokenization, vocabulary size, sequence length, threshold, train/validation split, random seeds, TensorFlow version, and training configuration. A score must not be copied from an earlier run and presented as a fresh result.

### Evidence integrity
Hashing only the comment text would not protect the predicted labels or severity field. The evidence hash should be calculated from a canonical representation of the full intended record, with stable key ordering and consistent value types. The stored digest itself must not be included in the payload being hashed.

### Claims and scope
AI-generated text can overstate what a notebook implements. The project therefore distinguishes an implemented notebook workflow from planned work. No interactive dashboard, production moderation service, or legal chain-of-custody system is claimed.

## 4. What AI Does Not Do

AI assistance does not:
- independently verify the source dataset or its licensing terms;
- guarantee that code is correct or secure;
- run the user's Google Colab session or overcome Colab account/session limits;
- prove that a model is accurate, fair, or suitable for real-world moderation;
- validate the severity bands as legal or safety classifications;
- create real experimental results without an actual completed run;
- replace human review of flagged content.

## 5. Developer Verification Responsibilities

Before accepting AI-assisted code, the developer should:
1. Read the code and understand its purpose.
2. Confirm variable names and column assumptions against the actual dataset.
3. Run the relevant cells and inspect warnings and exceptions.
4. Test edge cases such as blank comments, missing values, and malformed records.
5. Verify train/test separation and avoid fitting transformations on held-out data.
6. Reproduce all reported model metrics.
7. Test record hashing after CSV export and reload.
8. Keep the README, resume, and project report aligned with implemented functionality.

## 6. Disclosure of Results

The repository deliberately does not publish a current model leaderboard until the corrected notebook has been run from a fresh runtime and the results have been captured. A previously recorded score is not a substitute for a reproducible current evaluation.

## 7. Example AI-Assisted Workflow

A responsible workflow for a new project phase is:

1. **Ask:** request an explanation or implementation proposal for one specific task.
2. **Review:** inspect the assumptions, edge cases, and dependencies in the proposal.
3. **Implement:** add the code to the notebook or source module.
4. **Run:** execute it on the actual project data.
5. **Validate:** check outputs, metrics, and tests independently.
6. **Document:** record the final implementation and any limitations.
7. **Commit:** save the verified change to GitHub.

## 8. Transparency Statement

AI assistance is used to support development and learning. The final project decisions, code review, execution, validation, interpretation, and submission remain the developer's responsibility. AI-generated suggestions and unexecuted code are not represented as verified project results.
