"""Unit 4 tests for Chemical Reaction Engineering DI05005031.

The shared rule book lives in crtest_lib; this file pins what makes Unit 4 different: every reactor
must be taught as construction plus working, every figure must be an equipment figure that is named in
its card, and the numerical answers must close on themselves.
"""
import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from crtest_lib import unit_suite, strip_html  # noqa: E402
from subject_DI05005031 import SUBJ_DIR  # noqa: E402

Unit4 = unit_suite(4)

UNIT = json.loads((SUBJ_DIR / "unit4.json").read_text(encoding="utf-8"))
CARDS = [it for s in UNIT["notes"][:-1] for it in s["items"]]
BODY = strip_html(" ".join(it["h"]["en"] + " " + it["body"]["en"] for it in CARDS))
PROBLEMS = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))


class Unit4Specific(unittest.TestCase):
    def test_20_every_reactor_has_construction_and_working(self):
        equipment = [c for c in CARDS if c.get("diagram") and c["diagram"] != "u4_models"]
        self.assertEqual(len(equipment), 8, "one card per piece of equipment")
        for card in equipment:
            body = card["body"]["en"]
            self.assertGreaterEqual(body.count("<li>"), 5, f"thin parts list: {card['h']['en']}")
            self.assertIn("Construction: what it is made of", body,
                          f"no construction list: {card['h']['en']}")
            self.assertIn("Working: step by step", body, f"no working steps: {card['h']['en']}")

    def test_21_the_nine_reactors_are_named(self):
        for name in ("batch reactor", "semi-batch", "cstr", "tubular", "fixed bed", "fluidised",
                     "slurry", "bubble column", "spray tower", "trickle bed"):
            self.assertIn(name, BODY.lower(), f"missing reactor: {name}")

    def test_22_ideal_models_are_defined(self):
        for token in ("perfect mixing", "plug flow", "steady state"):
            self.assertIn(token, BODY.lower())

    def test_23_design_equations(self):
        for token in ("v = fa0 x / (-ra)", "v = fa0 x integral", "t = na0 x integral",
                      "tau = v/v0"):
            self.assertIn(token.lower(), BODY.lower())

    def test_24_cstr_against_pfr_numbers(self):
        k_tau_cstr = 0.9 / 0.1
        k_tau_pfr = math.log(10)
        self.assertAlmostEqual(k_tau_cstr / k_tau_pfr, 3.908, delta=0.005)
        self.assertIn("3.9", BODY)

    def test_25_batch_numerical(self):
        self.assertAlmostEqual(math.log(1 / 0.05) / 0.02, 149.8, delta=0.1)
        self.assertEqual(int(1440 // 180), 8)
        self.assertAlmostEqual(8 * 1.9, 15.2, delta=0.01)
        self.assertIn("15.2", PROBLEMS)

    def test_26_cstr_train(self):
        k_tau = 1 / 0.20 ** 0.5 - 1
        self.assertAlmostEqual(k_tau, 1.236, delta=0.001)
        tau = k_tau / 0.25
        self.assertAlmostEqual(tau, 4.944, delta=0.005)
        self.assertAlmostEqual(2 * 7.2 * tau, 71.2, delta=0.2)
        x1 = k_tau / (1 + k_tau)
        self.assertAlmostEqual(x1 + (1 - x1) * x1, 0.80, delta=0.001)

    def test_27_bed_and_fluidisation_numbers(self):
        self.assertAlmostEqual(250 / 600, 0.4167, delta=0.001)
        area = math.pi * 0.36 / 4
        self.assertAlmostEqual(0.4167 / area, 1.474, delta=0.005)
        umf = (1e-4) ** 2 * 2498.8 * 9.81 / (1650 * 1.8e-5)
        self.assertAlmostEqual(umf, 8.25e-3, delta=5e-5)
        self.assertAlmostEqual(0.050 / umf, 6.06, delta=0.05)
        h = 40 / (2500 * math.pi * 0.09 / 4 * 0.55)
        self.assertAlmostEqual(h, 0.4116, delta=0.002)
        self.assertIn("0.41 m", PROBLEMS)

    def test_28_figures_are_equipment(self):
        self.assertEqual(len(UNIT["diagrams"]), 9)
        for d in UNIT["diagrams"]:
            raw = (SUBJ_DIR / "diagrams" / Path(d["file"]).name).read_text(encoding="utf-8")
            self.assertGreater(raw.count("<circle"), 2, f"{d['id']} has no drawn parts")

    def test_29_no_broken_working(self):
        for bad in ("? no", "rather:", "tbd", "status", "状态"):
            self.assertNotIn(bad, BODY.lower())
            self.assertNotIn(bad, PROBLEMS.lower())

    def test_30_hours_and_marks(self):
        subj = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
        spec = next(u for u in subj["units"] if u["no"] == 4)
        self.assertEqual((spec["hours"], spec["weightage"]), (11, 24))
        self.assertEqual(UNIT["theory_marks"], 17)


if __name__ == "__main__":
    unittest.main(verbosity=2)
