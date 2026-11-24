"""Evaluation helpers for multi-label toxicity classification."""

from __future__ import annotations

from typing import Any

import pandas as pd
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score


def evaluate_multilabel(
    y_true: Any,
    y_pred: Any,
    label_names: list[str],
) -> tuple[dict[str, float], pd.DataFrame, str]:
    """Return micro metrics, per-label metrics, and a text classification report."""
    micro = {
        "precision_micro": float(
            precision_score(y_true, y_pred, average="micro", zero_division=0)
        ),
        "recall_micro": float(
            recall_score(y_true, y_pred, average="micro", zero_division=0)
        ),
        "f1_micro": float(
            f1_score(y_true, y_pred, average="micro", zero_division=0)
        ),
        "f1_macro": float(
            f1_score(y_true, y_pred, average="macro", zero_division=0)
        ),
    }

    per_label = pd.DataFrame(
        {
            "label": label_names,
            "precision": precision_score(
                y_true, y_pred, average=None, zero_division=0
            ),
            "recall": recall_score(
                y_true, y_pred, average=None, zero_division=0
            ),
            "f1": f1_score(
                y_true, y_pred, average=None, zero_division=0
            ),
        }
    )

    report = classification_report(
        y_true,
        y_pred,
        target_names=label_names,
        zero_division=0,
    )
    return micro, per_label, report
