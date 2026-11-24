import unittest

from src.forensic_integrity import (
    assign_severity,
    generate_evidence_hash,
    verify_evidence_hash,
)


class ForensicIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.record = {
            "evidence_id": "EVD-00001",
            "comment_text": "Example comment for a unit test.",
            "toxic": 1,
            "severe_toxic": 0,
            "obscene": 0,
            "threat": 0,
            "insult": 1,
            "identity_hate": 0,
            "toxicity_count": 2,
            "severity": "Medium",
        }
        self.record["evidence_hash"] = generate_evidence_hash(self.record)

    def test_severity_bands(self):
        self.assertEqual(assign_severity(0), "Non-Toxic")
        self.assertEqual(assign_severity(1), "Low")
        self.assertEqual(assign_severity(2), "Medium")
        self.assertEqual(assign_severity(3), "Medium")
        self.assertEqual(assign_severity(4), "High")
        self.assertEqual(assign_severity(6), "High")

    def test_invalid_severity_count(self):
        with self.assertRaises(ValueError):
            assign_severity(7)

    def test_original_record_verifies(self):
        self.assertTrue(verify_evidence_hash(self.record))

    def test_modified_comment_fails_verification(self):
        changed = dict(self.record)
        changed["comment_text"] = "Changed comment"
        self.assertFalse(verify_evidence_hash(changed))

    def test_modified_label_fails_verification(self):
        changed = dict(self.record)
        changed["toxic"] = 0
        self.assertFalse(verify_evidence_hash(changed))

    def test_modified_severity_fails_verification(self):
        changed = dict(self.record)
        changed["severity"] = "High"
        self.assertFalse(verify_evidence_hash(changed))


if __name__ == "__main__":
    unittest.main()
