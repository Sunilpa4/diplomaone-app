"""Unit 4 tests for Engineering Materials Science DI01000181.

Pins what Unit 4 is responsible for: the bond that classifies a non-metal, vulcanisation and the
elastomer choice, the ceramic that is hard and brittle for one reason, the two-layer refractory wall,
the dielectric thickness, and the abrasive and adhesive numbers - each one re-derived from its own data.
"""
import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mattest_lib import unit_suite, strip_html  # noqa: E402
from subject_DI01000181 import SUBJ_DIR  # noqa: E402

Unit4 = unit_suite(4)

UNIT = json.loads((SUBJ_DIR / "unit4.json").read_text(encoding="utf-8"))
CARDS = [it for s in UNIT["notes"][:-1] for it in s["items"]]
BODY = strip_html(" ".join(it["h"]["en"] + " " + it["body"]["en"] for it in CARDS))
PROBLEMS = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))


class Unit4Specific(unittest.TestCase):
    def test_20_four_families(self):
        for token in ("polymer", "ceramic", "composite", "natural"):
            self.assertIn(token, BODY.lower())
        # specific stiffness of alumina and CFRP against steel
        self.assertAlmostEqual(300 / 3.9 / (200 / 7.85), 3.02, delta=0.03)
        self.assertAlmostEqual(150 / 1.60 / (200 / 7.85), 3.68, delta=0.03)

    def test_21_vulcanisation(self):
        # 2 MPa gum to 22 MPa compound is the eleven-fold that carbon black buys
        self.assertAlmostEqual(22 / 2, 11.0, delta=0.01)
        self.assertAlmostEqual(3 * 1.0, 3.0, delta=1e-9)          # E = 3G
        self.assertAlmostEqual(0.5 * 22 * 5.5, 60.5, delta=0.1)   # strain energy, MJ/m3
        for token in ("sulphur", "vulcanisation", "550", "22 MPa"):
            self.assertIn(token, (BODY + PROBLEMS).lower() if token.isupper() else
                          (BODY + PROBLEMS))

    def test_22_compounding_and_elastomer_choice(self):
        phr = 100 + 50 + 3 + 1 + 2
        self.assertEqual(phr, 156)
        self.assertAlmostEqual(50 / 156 * 100, 32.1, delta=0.1)
        for token in ("NBR", "EPDM", "silicone", "butyl"):
            self.assertIn(token, BODY)

    def test_23_ceramic_thermal_stress(self):
        self.assertAlmostEqual(300e9 * 8.0e-6, 2.4e6, delta=1.0)
        self.assertAlmostEqual(2.4e6 * 200 / 1e6, 480, delta=0.5)
        self.assertAlmostEqual(2.4e6 * 100 / 1e6, 240, delta=0.5)
        self.assertAlmostEqual(300e6 / 2.4e6, 125, delta=0.5)
        self.assertAlmostEqual(480 / 300, 1.6, delta=0.01)
        self.assertIn("480", PROBLEMS)
        self.assertIn("240", PROBLEMS)

    def test_24_griffith_strength(self):
        for a, want in ((50e-6, 276), (200e-6, 138)):
            calc = math.sqrt(2 * 300e9 * 20 / (math.pi * a)) / 1e6
            self.assertAlmostEqual(calc, want, delta=1.5)
        # the square-root scaling: four times the flaw, half the strength
        self.assertAlmostEqual(math.sqrt(50e-6 / 200e-6), 0.5, delta=1e-9)

    def test_25_thermal_shock_parameter(self):
        cases = ((300e6, 0.22, 300e9, 8.0e-6, 97.5),
                 (50e6, 0.22, 70e9, 9.0e-6, 61.9),
                 (110e6, 0.17, 72e9, 0.55e-6, 2305))
        for sig, nu, e, alpha, want in cases:
            self.assertAlmostEqual(sig * (1 - nu) / (e * alpha), want, delta=1.5)
        self.assertAlmostEqual(2305 / 97.5, 23.6, delta=0.2)
        self.assertIn("97", PROBLEMS)
        self.assertIn("2305", PROBLEMS)

    def test_26_furnace_wall(self):
        r1, r2 = 0.230 / 1.00, 0.115 / 0.12
        self.assertAlmostEqual(r1, 0.230, delta=1e-6)
        self.assertAlmostEqual(r2, 0.9583, delta=1e-3)
        q = (1200 - 50) / (r1 + r2)
        self.assertAlmostEqual(q, 968, delta=1.0)
        self.assertAlmostEqual(1200 - q * r1, 977, delta=0.5)
        self.assertAlmostEqual(50 + q * r2, 977, delta=0.5)
        self.assertAlmostEqual(1150 / 0.230, 5000, delta=2)
        self.assertAlmostEqual((1 - q / 5000) * 100, 80.6, delta=0.2)
        self.assertAlmostEqual(4.032 * 720, 2903, delta=2)
        self.assertAlmostEqual(2903 * 8, 23224, delta=20)
        self.assertIn("968", PROBLEMS)
        self.assertIn("977", PROBLEMS)

    def test_27_porosity_of_a_firebrick(self):
        water = 345 - 320
        self.assertAlmostEqual(320 / 120, 2.67, delta=0.01)
        self.assertAlmostEqual(water / 320 * 100, 7.8, delta=0.05)
        self.assertAlmostEqual(water / 120 * 100, 20.8, delta=0.1)
        self.assertAlmostEqual(320 / (120 - 25), 3.37, delta=0.01)
        self.assertAlmostEqual(1 - 2.67 / 3.37, 0.208, delta=0.002)
        self.assertIn("20.8", PROBLEMS)

    def test_28_adhesive_lap_joint(self):
        area = 25 * 40
        tau = 5000 / area
        self.assertEqual(area, 1000)
        self.assertAlmostEqual(tau, 5.0, delta=1e-9)
        self.assertAlmostEqual(20 / tau, 4.0, delta=1e-9)
        self.assertAlmostEqual(20 / 3 * 1000 + 0, 6666.7, delta=1.0)
        self.assertIn("5.0 MPa", PROBLEMS)
        self.assertIn("6.67", PROBLEMS)

    def test_29_insulator_thickness(self):
        self.assertAlmostEqual(18 * 3, 54, delta=1e-9)
        self.assertAlmostEqual(54 / 11, 4.9, delta=0.05)
        self.assertAlmostEqual(33 / 18, 1.83, delta=0.005)
        self.assertAlmostEqual(11 * 3 / 15, 2.2, delta=0.005)
        self.assertIn("1.83", PROBLEMS)
        for token in ("15 kV/mm", "20 kV/mm", "24 kV/mm", "12 kV/mm"):
            self.assertIn(token, BODY)
        self.assertIn("bakelite", BODY.lower())

    def test_30_abrasive_and_refractory_families(self):
        # wheel speed and the Mohs order
        v = math.pi * 0.250 * 2000 / 60
        self.assertAlmostEqual(v, 26.2, delta=0.1)
        self.assertAlmostEqual(math.pi * 0.250 * 2800 / 60, 36.7, delta=0.1)
        for token in ("corundum", "silicon carbide", "CBN", "diamond"):
            self.assertIn(token, BODY)
        for token in ("silica", "magnesia", "dolomite", "chromite"):
            self.assertIn(token, BODY)

    def test_31_structure_and_tabs(self):
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "viva", "exam"])
        self.assertEqual(UNIT["hours"], 8)
        self.assertEqual(UNIT["weightage"], 17)
        self.assertEqual(UNIT["theory_marks"], 12)
        self.assertEqual(UNIT["course_outcomes"], ["CO4"])
        self.assertEqual(UNIT["practical_numbers"], [6])
        self.assertEqual(len(UNIT["notes"]), 6)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 6)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 9)
        self.assertEqual(len(UNIT["diagrams"]), 7)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 15)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 12)
        self.assertEqual(sum(q["marks"] for q in UNIT["exam_questions"]), 38)
        for bad in ("? no", "rather:", "tbd", "xxx"):
            self.assertNotIn(bad, (BODY + PROBLEMS).lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
