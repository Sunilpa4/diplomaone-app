"""Unit 3 tests for Engineering Materials Science DI01000181.

Pins what Unit 3 is responsible for: the steel and cast-iron carbon boundary, the strength and
ductility trade-off in plain carbon steel, the carbon equivalent, the copper and aluminium alloy
numbers, and the six solved numericals re-derived from their own data.
"""
import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mattest_lib import unit_suite, strip_html  # noqa: E402
from subject_DI01000181 import SUBJ_DIR  # noqa: E402

Unit3 = unit_suite(3)

UNIT = json.loads((SUBJ_DIR / "unit3.json").read_text(encoding="utf-8"))
CARDS = [it for s in UNIT["notes"][:-1] for it in s["items"]]
BODY = strip_html(" ".join(it["h"]["en"] + " " + it["body"]["en"] for it in CARDS))
PROBLEMS = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))


class Unit3Specific(unittest.TestCase):
    def test_20_family_split(self):
        # 2.14 % C is the steel / cast-iron boundary on the Fe-Fe3C diagram
        self.assertAlmostEqual(2.14 - 0.80, 1.34, delta=0.001)
        for token in ("2.14", "steel", "cast iron", "non-ferrous"):
            self.assertIn(token, BODY.lower())

    def test_21_metals_against_non_metals(self):
        for token in ("malleable", "ductile", "lustre", "metalloids"):
            self.assertIn(token, BODY.lower())
        self.assertIn("non-metal", BODY.lower())

    def test_22_plain_carbon_trade_off(self):
        # strength rises and elongation falls as carbon rises, 0.10 to 1.20 % C
        pair = ((0.10, 400, 30), (0.20, 450, 27), (0.40, 600, 20),
                (0.80, 800, 10), (1.20, 900, 5))
        strengths = [p[1] for p in pair]
        elongations = [p[2] for p in pair]
        self.assertEqual(strengths, sorted(strengths))
        self.assertEqual(elongations, sorted(elongations, reverse=True))
        self.assertAlmostEqual(900 / 400, 2.25, delta=0.01)
        self.assertAlmostEqual(30 / 5, 6.0, delta=0.001)
        for c, uts, elong in pair:
            self.assertIn(f"{c:.2f}", BODY)
            self.assertIn(str(uts), BODY)

    def test_23_pearlite_from_carbon(self):
        # the same eutectoid lever rule as Unit 2, restated for a 0.10 % C steel
        pearlite = (0.10 - 0.02) / (0.78) * 100
        self.assertAlmostEqual(pearlite, 10.3, delta=0.1)
        self.assertAlmostEqual(pearlite + 12.8, 23.1, delta=0.15)
        self.assertIn("12.8", BODY)

    def test_24_stainless_needs_chromium(self):
        # 12 % Cr is the passive-film threshold; 18/8 is the austenitic family
        self.assertEqual(18 + 8, 26)
        self.assertGreater(18, 12)
        for token in ("12", "18/8", "passive"):
            self.assertIn(token, BODY)
        self.assertIn("austenitic", BODY.lower())
        self.assertIn("martensitic", BODY.lower())

    def test_25_carbon_equivalent(self):
        grey = 3.4 + (2.1 + 0.3) / 3
        ductile = 3.6 + (2.4 + 0.05) / 3
        self.assertAlmostEqual(grey, 4.20, delta=0.005)
        self.assertAlmostEqual(ductile, 4.42, delta=0.005)
        self.assertAlmostEqual(4.3 - grey, 0.10, delta=0.01)
        self.assertAlmostEqual(ductile - 4.3, 0.12, delta=0.01)
        self.assertIn("4.20", PROBLEMS)
        self.assertIn("4.42", PROBLEMS)

    def test_26_brass_density_rule_of_mixtures(self):
        v_cu, v_zn = 70 / 8.96, 30 / 7.14
        rho = 100 / (v_cu + v_zn)
        self.assertAlmostEqual(rho, 8.32, delta=0.01)
        self.assertAlmostEqual(1 / rho, 0.70 / 8.96 + 0.30 / 7.14, delta=1e-9)
        self.assertAlmostEqual((rho - 8.53) / 8.53 * 100, -2.4, delta=0.05)
        self.assertIn("2.5 % low", PROBLEMS)
        self.assertTrue(8.96 > rho > 7.14)
        self.assertIn("8.32", PROBLEMS)

    def test_27_foundry_charge_and_cost(self):
        charge = 250 / 0.97
        self.assertAlmostEqual(charge, 257.7, delta=0.1)
        per_kg = 0.70 * 820 + 0.30 * 280
        self.assertAlmostEqual(per_kg, 658.0, delta=0.05)
        cost = charge * per_kg
        self.assertAlmostEqual(cost / 1000, 169.5, delta=0.5)
        self.assertAlmostEqual(cost / 250, 678.0, delta=1.0)
        self.assertIn("257.7", PROBLEMS)
        self.assertIn("658", PROBLEMS)

    def test_28_steel_to_aluminium_bracket(self):
        m_steel = 7.85 * 260 / 1000
        m_al = 2.70 * 260 / 1000
        self.assertAlmostEqual(m_steel, 2.041, delta=0.002)
        self.assertAlmostEqual(m_al, 0.702, delta=0.002)
        self.assertAlmostEqual((m_steel - m_al) / m_steel * 100, 65.6, delta=0.1)
        self.assertAlmostEqual(310 / 450, 0.689, delta=0.002)
        self.assertAlmostEqual(450 / 7.85, 57.3, delta=0.1)
        self.assertAlmostEqual(310 / 2.70, 114.8, delta=0.2)
        self.assertAlmostEqual(115 / 57, 2.0, delta=0.05)
        self.assertIn("65.6", PROBLEMS)

    def test_29_copper_against_brass_wire(self):
        a = 2.5e-6
        r_cu = 1.72e-8 * 30 / a
        r_brass = 6.40e-8 * 30 / a
        self.assertAlmostEqual(r_cu, 0.2064, delta=1e-4)
        self.assertAlmostEqual(r_brass, 0.7680, delta=1e-4)
        self.assertAlmostEqual(16 ** 2 * r_cu, 52.8, delta=0.1)
        self.assertAlmostEqual(16 ** 2 * r_brass, 196.6, delta=0.2)
        self.assertAlmostEqual(r_brass / r_cu, 3.72, delta=0.01)
        self.assertAlmostEqual(6.40e-8 / 1.72e-8, 3.72, delta=0.01)
        self.assertIn("0.206", PROBLEMS)
        self.assertIn("196.6", PROBLEMS)

    def test_30_weight_to_atomic_percent(self):
        n_cu, n_zn = 70 / 63.55, 30 / 65.38
        total = n_cu + n_zn
        self.assertAlmostEqual(n_cu / total * 100, 70.6, delta=0.1)
        self.assertAlmostEqual(n_zn / total * 100, 29.4, delta=0.1)
        g = [88 / 63.55, 10 / 118.71, 2 / 65.38]
        g_total = sum(g)
        self.assertAlmostEqual(g[0] / g_total * 100, 92.3, delta=0.1)
        self.assertAlmostEqual(g[1] / g_total * 100, 5.6, delta=0.1)
        self.assertAlmostEqual(g[2] / g_total * 100, 2.0, delta=0.1)
        self.assertAlmostEqual(sum(g) / g_total * 100, 100.0, delta=0.05)
        self.assertIn("70.6", PROBLEMS)
        self.assertIn("92.3", PROBLEMS)

    def test_31_structure_and_tabs(self):
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "viva", "exam"])
        self.assertEqual(UNIT["hours"], 8)
        self.assertEqual(UNIT["weightage"], 17)
        self.assertEqual(UNIT["theory_marks"], 12)
        self.assertEqual(UNIT["course_outcomes"], ["CO3"])
        self.assertEqual(UNIT["practical_numbers"], [1, 3])
        self.assertEqual(len(UNIT["notes"]), 6)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 6)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 9)
        self.assertEqual(len(UNIT["diagrams"]), 7)
        self.assertEqual(len(UNIT["equations"]), 5)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 16)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 12)
        for bad in ("? no", "rather:", "tbd"):
            self.assertNotIn(bad, (BODY + PROBLEMS).lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
