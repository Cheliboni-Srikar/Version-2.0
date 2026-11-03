import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))
from study_space_adviser import advise

FULL = {"quiet", "power", "open_A", "quiet_A", "power_A"}

class AdviserBehaviour(unittest.TestCase):
    def test_full_case_records_both_dependencies(self):
        facts, trace, message = advise(FULL)
        self.assertIn("recommend_A", facts)
        self.assertEqual([t[0] for t in trace], ["R4", "R5"])
        self.assertIn("needs_quiet_power", trace[1][1])

    def test_each_required_input_is_necessary(self):
        for missing in FULL:
            with self.subTest(missing=missing):
                facts, _, _ = advise(FULL - {missing})
                self.assertNotIn("recommend_A", facts)

    def test_missing_availability_is_unknown_not_closed(self):
        facts, trace, message = advise(FULL - {"open_A"})
        self.assertIn("needs_quiet_power", facts)
        self.assertNotIn("closed_A", facts)
        self.assertEqual([t[0] for t in trace], ["R4"])
        self.assertIn("unknown", message)

    def test_known_closed_is_distinct_from_unknown(self):
        facts, _, message = advise((FULL - {"open_A"}) | {"closed_A"})
        self.assertNotIn("recommend_A", facts)
        self.assertIn("known closed", message)

    def test_conflict_rejected(self):
        with self.assertRaisesRegex(ValueError, "Conflicting status"):
            advise(FULL | {"closed_A"})

    def test_update_discards_old_recommendation(self):
        first, _, _ = advise(FULL)
        second, _, _ = advise((FULL - {"open_A"}) | {"closed_A"})
        self.assertIn("recommend_A", first)
        self.assertNotIn("recommend_A", second)
        self.assertEqual(FULL, {"quiet", "power", "open_A", "quiet_A", "power_A"})

    def test_derived_fact_cannot_be_injected(self):
        with self.assertRaisesRegex(ValueError, "Unexpected input"):
            advise({"recommend_A"})

if __name__ == "__main__":
    unittest.main()
