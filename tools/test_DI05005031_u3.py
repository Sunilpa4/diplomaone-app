"""Unit 3 tests for Chemical Reaction Engineering DI05005031.

The shared rule book lives in crtest_lib; this file pins the arithmetic of the batch data: the worked
table of section 3.1 must give the same order and k by all three methods, the pressure example must
close on itself, and the half-life and integrated laws must agree with the numericals.
"""
import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from crtest_lib import unit_suite, strip_html  # noqa: E402
from subject_DI05005031 import SUBJ_DIR  # noqa: E402

Unit3 = unit_suite(3)

UNIT = json.loads((SUBJ_DIR / "unit3.json").read_text(encoding="utf-8"))
BODY = strip_html(" ".join(it["body"]["en"] for s in UNIT["notes"] for it in s["items"]))
PROBLEMS = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))


class Unit3Specific(unittest.TestCase):
    def test_20_three_methods_are_taught(self):
        for token in ("differential method", "integral method", "half-life method"):
            self.assertIn(token, BODY.lower())
        self.assertIn("ln(-ra) = ln k + n ln ca".replace("ra", "ra"), BODY.lower())

    def test_21_constant_volume_and_expansion(self):
        for token in ("ca = ca0 (1 - x)", "expansion factor", "eps"):
            self.assertIn(token.lower(), BODY.lower())
        self.assertIn("t = ca0 x integral", BODY.lower())

    def test_22_pressure_relations(self):
        for token in ("pa = pa0 (1 - x)", "2 pa0 - p", "ca = pa / (r t)", "inert"):
            self.assertIn(token.lower(), BODY.lower())

    def test_23_integrated_laws(self):
        for token in ("ln(ca0/ca) = k t", "1/ca - 1/ca0 = k t", "1/ca^2 - 1/ca0^2 = 2 k t",
                      "ca^(1-n) - ca0^(1-n) = (n-1) k t"):
            self.assertIn(token.lower(), BODY.lower())

    def test_24_worked_data_is_self_consistent(self):
        """The 3.1 table must satisfy second order kinetics with k = 0.05, as printed."""
        table = [(0, 1.00), (5, 0.80), (13.3, 0.60), (30, 0.40), (60, 0.25)]
        k = 0.05
        for t, ca in table:
            self.assertAlmostEqual(1 / ca, 1 / 1.00 + k * t, delta=0.02)
        # and the first order plot must NOT be straight, or the card would be teaching nonsense
        first_order_steps = [(0.22 / 5), (0.51 - 0.22) / 8.3, (0.92 - 0.51) / 16.7]
        self.assertGreater(first_order_steps[0], 1.6 * first_order_steps[-1])

    def test_25_half_life_law(self):
        for n, factor in ((0, 2.0), (1, 1.0), (2, 0.5)):
            ratio = (0.8 / 0.4) ** (1 - n)
            self.assertAlmostEqual(ratio, factor, delta=1e-9)
        # the numericals quote 25, 50 and 100 min at 0.80, 0.40 and 0.20 mol/L
        for t, ca in ((25, 0.80), (50, 0.40), (100, 0.20)):
            self.assertAlmostEqual(t * ca, 20.0, delta=0.01)

    def test_26_pressure_example_closes(self):
        p0, p = 1.00, 1.60
        pa = 2 * p0 - p
        self.assertAlmostEqual(pa, 0.40, delta=1e-9)
        self.assertAlmostEqual(1 - pa / p0, 0.60, delta=1e-9)
        ca0 = 1.0e5 / (8.314 * 500)
        self.assertAlmostEqual(ca0, 24.06, delta=0.05)
        self.assertAlmostEqual(ca0 * 0.40, 9.62, delta=0.05)
        k = -math.log(0.40) / 20
        self.assertAlmostEqual(k, 0.0458, delta=1e-4)

    def test_27_numericals_are_worked_and_asked(self):
        practice = UNIT["notes"][-1]["items"]
        exam = UNIT["exam_questions"]
        self.assertEqual(len(practice), len(exam))
        for item, q in zip(practice, exam):
            self.assertIn(q["q"]["en"][:60], item["body"]["en"])
            self.assertIn(f"Question ({q['marks']} marks)", item["body"]["en"])
            self.assertIn("પ્રશ્ન (" + str(q["marks"]) + " marks)", item["body"]["gu"])
        self.assertEqual([q["marks"] for q in exam], [6, 7, 8, 6, 7, 7])

    def test_28_printed_answers(self):
        for token in ("0.0462", "0.50 l mol-1 min-1", "0.049", "0.050 l mol-1 min-1", "0.0458",
                      "0.0625"):
            self.assertIn(token, PROBLEMS.lower(), f"missing worked number {token}")

    def test_29_no_broken_working(self):
        """Guards against the '... ? no: ...' notes that a draft leaves behind."""
        for bad in ("? no", "rather:", "... /20?", "tbd"):
            self.assertNotIn(bad, BODY.lower())
            self.assertNotIn(bad, PROBLEMS.lower())

    def test_30_hours_and_marks(self):
        subj = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
        spec = next(u for u in subj["units"] if u["no"] == 3)
        self.assertEqual((spec["hours"], spec["weightage"]), (9, 20))
        self.assertEqual(UNIT["theory_marks"], 14)



if __name__ == "__main__":
    unittest.main(verbosity=2)
