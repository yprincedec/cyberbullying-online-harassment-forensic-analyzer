# Data Dictionary

## Source Training Dataset

The labelled Jigsaw training CSV is expected to contain the following fields.

| Field | Type | Description |
|---|---|---|
| `id` | String | Source comment identifier supplied by the dataset |
| `comment_text` | String | Original comment text |
| `toxic` | Binary integer | General toxic-language target |
| `severe_toxic` | Binary integer | Severe-toxic target |
| `obscene` | Binary integer | Obscene-language target |
| `threat` | Binary integer | Threat-language target |
| `insult` | Binary integer | Insult target |
| `identity_hate` | Binary integer | Identity-hate target |

The six target fields are independent binary labels. They are not mutually exclusive.

## Derived EDA Fields

| Field | Description |
|---|---|
| `label_count` | Number of positive ground-truth labels for a source comment; used during EDA |
| `text_length` | Number of characters in the comment |
| `word_count` | Number of whitespace-separated tokens in the comment |

These are notebook analysis fields and should not be confused with model predictions.

## Forensic Evidence Output

| Field | Description |
|---|---|
| `comment_text` | Original held-out comment text associated with the prediction |
| `evidence_id` | Generated sequential identifier such as `EVD-00001` |
| `toxic` | Predicted binary toxic label |
| `severe_toxic` | Predicted binary severe-toxic label |
| `obscene` | Predicted binary obscene label |
| `threat` | Predicted binary threat label |
| `insult` | Predicted binary insult label |
| `identity_hate` | Predicted binary identity-hate label |
| `toxicity_count` | Sum of the six predicted binary labels |
| `severity` | Project-defined count-based severity band |
| `evidence_hash` | SHA-256 digest of the canonical record payload |

The evidence table contains predicted labels, not ground-truth targets. The hash payload covers the evidence ID, comment text, six predicted labels, toxicity count, and severity. The digest field itself is excluded from its own payload.

## Interpretation Notes

- A predicted 0 is not proof that a comment is harmless.
- A predicted 1 is not proof of intent, identity, or a policy violation.
- The severity field is a triage heuristic and not a legal or clinical classification.
- Raw comment text can contain harmful or personal content. Keep exports private and share only carefully reviewed, minimal samples.
