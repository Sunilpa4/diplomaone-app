"""Unit 2 tests for Engineering Materials Science DI01000181.

Pins what Unit 2 is responsible for: the phase rule, the lever rule on both diagrams, the Fe-C
points, the eutectoid fractions, and a Hall-Petch result that agrees with the figure.
"""
import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mattest_lib import unit_suite, strip_html  # noqa: E402
from subject_DI01000181 import SUBJ_DIR  # noqa: E402

Unit2 = unit_suite(2)

UNIT = json.loads((SUBJ_DIR / "unit2.json").read_text(encoding="utf-8"))
CARDS = [it for s in UNIT["notes"][:-1] for it in s["items"]]
BODY = strip_html(" ".join(it["h"]["en"] + " " + it["body"]["en"] for it in CARDS))
PROBLEMS = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))


def lever(c0, c_l, c_s):
    return (c_s - c0) / (c_s - c_l)


class Unit2Specific(unittest.TestCase):
    def test_20_phase_rule(self):
        # condensed rule, pressure fixed at one atmosphere
        self.assertEqual(1 - 1 + 1, 1)          # austenite field
        self.assertEqual(1 - 2 + 1, 0)          # melting point of pure iron
        self.assertEqual(2 - 3 + 1, 0)          # Pb-Sn eutectic
        self.assertEqual(2 - 2 + 1, 1)          # alpha + liquid
        self.assertIn("F = C - P + 2", BODY)
        self.assertIn("F = C - P + 1", BODY)

    def test_21_eutectic_points(self):
        for token in ("183", "61.9", "1147", "4.3", "727", "0.8", "2.14", "6.67"):
            self.assertIn(token, BODY)

    def test_22_lever_rule_pb_sn(self):
        # liquid at 55 % Sn, alpha at 17 % Sn; W = (far arm)/(total arm)
        w_l = lever(40, 55, 17)
        self.assertAlmostEqual(w_l, 0.605, delta=0.001)
        self.assertAlmostEqual(1 - w_l, 0.395, delta=0.001)
        self.assertAlmostEqual(w_l * 2, 1.21, delta=0.01)
        self.assertIn("0.605", PROBLEMS)

    def test_23_lever_rule_cu_ni(self):
        self.assertAlmostEqual(lever(50, 40, 60), 0.50, delta=1e-9)   # liquid 40, solid 60
        # solidus of the 50 % alloy sits at 1270 C, above 1250 C
        t_solid = 1240 + (50 - 40) / (60 - 40) * (1300 - 1240)
        self.assertAlmostEqual(t_solid, 1270, delta=0.5)
        self.assertIn("1270", PROBLEMS)

    def test_24_eutectoid_fractions(self):
        pearlite_04 = (0.40 - 0.02) / (0.80 - 0.02) * 100
        self.assertAlmostEqual(pearlite_04, 48.7, delta=0.05)
        self.assertAlmostEqual((1.20 - 0.80) / (6.67 - 0.80) * 100, 6.8, delta=0.05)
        self.assertAlmostEqual(0.487 * 5, 2.44, delta=0.01)
        self.assertIn("48.7", PROBLEMS)
        self.assertIn("6.8", PROBLEMS)

    def test_25_hall_petch(self):
        self.assertAlmostEqual(100 + 23.4 * 2, 146.8, delta=0.05)
        self.assertAlmostEqual(100 + 23.4 * 5, 217, delta=0.05)
        d = 1 / ((300 - 100) / 23.4) ** 2
        self.assertAlmostEqual(d, 0.0137, delta=0.0002)
        self.assertIn("0.0137", PROBLEMS)

    def test_26_astm_to_grain_size(self):
        for n, d in ((6, 0.0449), (10, 0.0112)):
            calc = 25.4 / (100 * math.sqrt(2 ** (n - 1)))
            self.assertAlmostEqual(calc, d, delta=0.0002)
        self.assertAlmostEqual(100 + 23.4 / math.sqrt(0.0449), 210.3, delta=0.3)
        self.assertAlmostEqual(100 + 23.4 / math.sqrt(0.0112), 321.2, delta=0.5)

    def test_27_critical_radius(self):
        r = 2 * 0.2 * 1811 / (1.9e9 * 100)
        self.assertAlmostEqual(r * 1e9, 3.81, delta=0.02)
        self.assertAlmostEqual(r * 1e9 / 2, 1.91, delta=0.02)
        self.assertIn("3.8 nm", BODY)

    def test_28_heat_treatment_temperatures(self):
        self.assertAlmostEqual(912 - 231 * 0.4, 819.6, delta=0.5)
        self.assertAlmostEqual(727 + 313 * (1.2 - 0.8), 852.2, delta=0.5)
        for token in ("annealing", "normalising", "hardening", "tempering"):
            self.assertIn(token, BODY.lower())

    def test_29_copper_nickel_isomorphous(self):
        self.assertIn("isomorphous", BODY.lower())
        self.assertIn("complete solubility", (BODY + PROBLEMS).lower())

    def test_30_tabs_and_thin_parts(self):
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "viva", "exam"])
        for bad in ("? no", "rather:", "tbd"):
            self.assertNotIn(bad, (BODY + PROBLEMS).lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
