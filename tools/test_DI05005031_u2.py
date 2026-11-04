"""Unit 2 tests for Chemical Reaction Engineering DI05005031.

The shared rule book lives in crtest_lib; this file adds the unit-2 arithmetic: the numbers printed in
the cards, the solved numericals and the exam questions must agree with each other, and the Arrhenius
derivation must actually be present (the unit exists to derive it, not to quote it).
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from crtest_lib import unit_suite, strip_html  # noqa: E402

Unit2 = unit_suite(2)

import json  # noqa: E402
from subject_DI05005031 import SUBJ_DIR  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit2.json").read_text(encoding="utf-8"))
BODY = strip_html(" ".join(it["body"]["en"] for s in UNIT["notes"] for it in s["items"]))


class Unit2Specific(unittest.TestCase):
    def test_20_rate_law_split(self):
        self.assertIn("k(T)", BODY)
        self.assertIn("f(C)", BODY)
        self.assertIn("two factors", BODY)

    def test_21_arrhenius_derivation(self):
        flat = BODY.lower()
        self.assertIn("van't hoff", flat)
        self.assertIn("d ln k / dt", flat)
        self.assertIn("integrate with ea constant", flat)
        self.assertIn("boltzmann", flat)
        self.assertIn("a = z x p", flat)

    def test_22_ea_numbers(self):
        worked = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))
        everything = BODY + " " + worked
        for token in ("55.3", "51 kj/mol", "2.0 x 10^4", "91", "500 k"):
            self.assertIn(token.lower(), everything.lower(), f"missing worked number {token}")

    def test_23_units_table(self):
        for k in ("mol m-3 s-1", "s-1", "m3 mol-1 s-1", "(mol m-3)^(1-n) s-1"):
            self.assertIn(k, BODY)

    def test_24_chain_mechanism(self):
        for token in ("[br.]", "[hbr]", "1.5", "kt [br.]^2"):
            self.assertIn(token.lower(), BODY.lower())

    def test_25_pseudo_first_order(self):
        self.assertIn("pseudo first order", BODY.lower())
        self.assertIn("k'", BODY)

    def test_26_questions_match_numericals(self):
        practice = UNIT["notes"][-1]["items"]
        exam = UNIT["exam_questions"]
        self.assertEqual(len(practice), len(exam))
        for item, q in zip(practice, exam):
            self.assertIn(q["q"]["en"][:60], item["body"]["en"])
            self.assertIn(f"Question ({q['marks']} marks)", item["body"]["en"])
            self.assertIn("પ્રશ્ન (" + str(q["marks"]) + " marks)", item["body"]["gu"])
            self.assertIn(q["q"]["gu"][:40], item["body"]["gu"])

    def test_27_marks_are_sane(self):
        marks = [q["marks"] for q in UNIT["exam_questions"]]
        self.assertEqual(sum(marks), 41)
        for m in marks:
            self.assertIn(m, (6, 7, 8))

    def test_28_hours_add_up(self):
        subj = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
        # the printed syllabus gives 7 + 8 + 9 + 11 + 11 = 46 h but totals the subject as 45 h
        self.assertEqual(sum(u["hours"] for u in subj["units"]), 46)
        self.assertEqual(sum(u["weightage"] for u in subj["units"]), 100)
        self.assertEqual(subj["exam"]["theory_ese"] + subj["exam"]["theory_pa"]
                         + subj["exam"]["practical_pa"] + subj["exam"]["practical_ese"], 150)


if __name__ == "__main__":
    unittest.main(verbosity=2)
