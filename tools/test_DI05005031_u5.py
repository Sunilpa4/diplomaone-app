"""Unit 5 tests for Chemical Reaction Engineering DI05005031.

The shared rule book lives in crtest_lib; this file pins what makes Unit 5 different: the three design
equations must be derived from one balance, the CSTR/PFR comparison must agree with the plot, and the
space time and holding time must be told apart with real gas numbers.
"""
import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from crtest_lib import unit_suite, strip_html  # noqa: E402
from subject_DI05005031 import SUBJ_DIR  # noqa: E402

Unit5 = unit_suite(5)

UNIT = json.loads((SUBJ_DIR / "unit5.json").read_text(encoding="utf-8"))
CARDS = [it for s in UNIT["notes"][:-1] for it in s["items"]]
BODY = strip_html(" ".join(it["h"]["en"] + " " + it["body"]["en"] for it in CARDS))
PROBLEMS = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))


class Unit5Specific(unittest.TestCase):
    def test_20_performance_equation_is_derived(self):
        body = CARDS[0]["body"]["en"]
        for token in ("in - out + generation = accumulation", "NA0 dX/dt", "FA0 dX/dV"):
            self.assertIn(token, body)

    def test_21_constant_density_is_stated(self):
        body = CARDS[1]["body"]["en"]
        self.assertIn("CA = CA0 (1 - X)", body)
        self.assertIn("1 + eps X", body)

    def test_22_all_three_reactors_are_taught(self):
        for token in ("batch reactor is designed in time", "steady state", "plug flow",
                      "space velocity", "holding time"):
            self.assertIn(token, BODY.lower())

    def test_23_first_order_yardsticks(self):
        self.assertAlmostEqual(0.8 / 0.2, 4.0, delta=1e-9)
        self.assertAlmostEqual(math.log(5), 1.6094, delta=1e-4)
        self.assertAlmostEqual(4.0 / math.log(5), 2.485, delta=0.005)
        self.assertIn("2.5", BODY)

    def test_24_two_cstrs_in_series(self):
        k_tau = 1 / 0.2 ** 0.5 - 1
        self.assertAlmostEqual(k_tau, 1.236, delta=0.001)
        self.assertAlmostEqual((1 + k_tau) ** 2, 5.0, delta=0.01)
        self.assertIn("1.236", BODY)

    def test_25_batch_numbers(self):
        t = math.log(10) / 0.03
        self.assertAlmostEqual(t, 76.75, delta=0.02)
        self.assertEqual(int(1440 // (t + 25)), 14)
        self.assertAlmostEqual(14 * 1.5 * 2.0 * 0.9, 37.8, delta=0.05)
        self.assertIn("37.8", PROBLEMS)

    def test_26_space_time_and_holding_time(self):
        self.assertAlmostEqual(2.4 / 0.8, 3.0, delta=1e-9)
        self.assertAlmostEqual(1 / 0.05, 20.0, delta=1e-9)
        v = 0.8 * (2 / 6) * (400 / 350)
        self.assertAlmostEqual(v, 0.3048, delta=0.001)
        self.assertAlmostEqual(2.4 / v, 7.87, delta=0.02)
        self.assertIn("7.9 min", PROBLEMS)

    def test_27_second_order_ratio(self):
        r_cstr = 1.2 * 0.75 / (0.02 * 1.44 * 0.0625) * 0.5
        self.assertAlmostEqual(r_cstr, 250.0, delta=0.5)
        v_pfr = 0.5 * 0.75 / (0.02 * 1.2 * 0.25)
        self.assertAlmostEqual(v_pfr, 62.5, delta=0.1)
        self.assertAlmostEqual(r_cstr / v_pfr, 4.0, delta=0.01)

    def test_28_reactor_choice_numbers(self):
        v_cstr = 3.0 * 9.0 / 0.15
        self.assertAlmostEqual(v_cstr, 180.0, delta=0.5)
        v_pfr = 3.0 * math.log(10) / 0.15
        self.assertAlmostEqual(v_pfr, 46.05, delta=0.1)
        k_tau2 = (1 / 0.10) ** 0.5 - 1
        v_train = 2 * 3.0 * k_tau2 / 0.15
        self.assertAlmostEqual(v_train, 86.5, delta=0.2)
        for token in ("180 m3", "86.5 m3", "46.1 m3"):
            self.assertIn(token, PROBLEMS)

    def test_28b_two_tank_train_and_recovery(self):
        k_tau = (1 / 0.15) ** 0.5 - 1
        self.assertAlmostEqual(k_tau, 1.5826, delta=0.001)
        v_train = 2 * 4.0 * k_tau / 0.20
        self.assertAlmostEqual(v_train, 63.3, delta=0.2)
        self.assertIn("63 m3", PROBLEMS)
        v_hit = 3 * ((1 / 0.15) ** (1 / 3) - 1) / 0.20 * 4.0
        self.assertAlmostEqual(v_hit, 52.9, delta=0.2)
        recover = (113.3 - v_hit) / (113.3 - 37.9)
        self.assertAlmostEqual(recover, 0.80, delta=0.01)
        self.assertIn("80 % of the volume saving", PROBLEMS)

    def test_29_figs_and_no_broken_text(self):
        self.assertEqual(len(UNIT["diagrams"]), 7)
        for d in UNIT["diagrams"]:
            raw = (SUBJ_DIR / "diagrams" / Path(d["file"]).name).read_text(encoding="utf-8")
            self.assertIn("<svg", raw)
        for bad in ("? no", "rather:", "tbd", "状态", "None of that"):
            self.assertNotIn(bad.lower(), BODY.lower())

    def test_30_hours_and_marks(self):
        subj = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
        spec = next(u for u in subj["units"] if u["no"] == 5)
        self.assertEqual((spec["hours"], spec["weightage"]), (11, 24))
        self.assertEqual(UNIT["theory_marks"], 17)


if __name__ == "__main__":
    unittest.main(verbosity=2)
