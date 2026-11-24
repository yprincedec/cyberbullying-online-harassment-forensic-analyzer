"""Reusable helpers for project-defined evidence records.

These utilities provide integrity checks over selected record fields. They do not
authenticate the source, establish a trusted timestamp, or create legal chain
of custody.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any, Iterable, Mapping

DEFAULT_LABELS = (
    "toxic",
    "severe_toxic",
    "obscene",
    "threat",
    "insult",
    "identity_hate",
)


def assign_severity(toxicity_count: int) -> str:
    """Map a predicted-label count to the notebook's heuristic severity band."""
    count = int(toxicity_count)
    if count < 0 or count > len(DEFAULT_LABELS):
        raise ValueError("toxicity_count must be between 0 and 6")
    if count == 0:
        return "Non-Toxic"
    if count == 1:
        return "Low"
    if count <= 3:
        return "Medium"
    return "High"


def canonical_evidence_payload(
    record: Mapping[str, Any],
    labels: Iterable[str] = DEFAULT_LABELS,
) -> dict[str, Any]:
    """Build a stable, typed payload from the fields protected by the digest."""
    label_names = tuple(labels)
    missing = [name for name in label_names if name not in record]
    required = ("evidence_id", "comment_text", "toxicity_count", "severity")
    missing.extend(name for name in required if name not in record)
    if missing:
        raise KeyError(f"Missing evidence fields: {sorted(set(missing))}")

    return {
        "evidence_id": str(record["evidence_id"]),
        "comment_text": str(record["comment_text"]),
        "toxicity_labels": {
            name: int(record[name]) for name in label_names
        },
        "toxicity_count": int(record["toxicity_count"]),
        "severity": str(record["severity"]),
    }


def generate_evidence_hash(
    record: Mapping[str, Any],
    labels: Iterable[str] = DEFAULT_LABELS,
) -> str:
    """Return SHA-256 for the canonical evidence payload."""
    payload = canonical_evidence_payload(record, labels)
    canonical = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def verify_evidence_hash(
    record: Mapping[str, Any],
    labels: Iterable[str] = DEFAULT_LABELS,
) -> bool:
    """Compare the stored evidence_hash with a freshly computed digest."""
    if "evidence_hash" not in record:
        raise KeyError("Missing evidence_hash")
    return str(record["evidence_hash"]) == generate_evidence_hash(record, labels)
