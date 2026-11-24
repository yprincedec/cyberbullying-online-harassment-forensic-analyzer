# Privacy, Ethics, and Human Review

## Scope

The project is an educational classifier and forensic-style record prototype. It is not a production content moderation system, law-enforcement tool, legal evidence platform, or psychological risk assessment.

## Data minimization

- Do not commit the full Jigsaw dataset or raw comment exports.
- Avoid placing raw comments in screenshots, public reports, issue descriptions, or sample output files.
- Use synthetic examples for unit tests and documentation.
- Share only the minimum data needed for debugging or demonstration.
- Restrict access to any local evidence CSV containing raw text.

## Human review

A prediction is a model output, not a finding about a person's intent or character. Human reviewers should consider the full conversation, quoted speech, sarcasm, context, language variety, and platform-specific policy before acting.

Do not automatically ban, punish, report, or make legal conclusions about a user based only on these model outputs.

## Bias and performance

The source dataset is English-centric and reflects its own annotation choices. Model errors may vary across dialects, identity terms, quoted content, and rare labels. Evaluate false positives and false negatives rather than relying on a single aggregate score.

## Evidence integrity

SHA-256 can help detect changes to fields included in the digest. It does not prove:
- who created or submitted the original comment;
- the time or location of the original event;
- the authenticity of the source;
- that the record was not altered before hashing;
- a formal legal chain of custody.

A production evidence workflow would require controlled collection, authenticated access, trusted timestamps, immutable storage, audit logs, documented retention, and legal/privacy review.

## Reporting

Describe the model as a research prototype. Disclose dataset limitations, evaluation conditions, error patterns, and whether the notebook was fully rerun. Never present heuristic severity bands as validated threat categories.
