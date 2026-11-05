"""Unit 5 tests for Engineering Materials Science DI01000181.

Pins what Unit 5 is responsible for: the surface zone and the finish that is bought, Faraday's law
for plating, the coating thicknesses, the oil numbers from Walther, the paint quantity from solids
and the corrosion cell - every figure re-derived from its own data.
"""
import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mattest_lib import unit_suite, strip_html  # noqa: E402
from subject_DI01000181 import SUBJ_DIR  # noqa: E402

Unit5 = unit_suite(5)

UNIT = json.loads((SUBJ_DIR / "unit5.json").read_text(encoding="utf-8"))
CARDS = [it for s in UNIT["notes"][:-1] for it in s["items"]]
BODY = strip_html(" ".join(it["h"]["en"] + " " + it["body"]["en"] for it in CARDS))
PROBLEMS = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))


def walther(nu40, nu100):
    def z(nu):
        return math.log10(math.log10(nu + 0.7))

    t1, t2 = math.log10(313.15), math.log10(373.15)
    b = (z(nu40) - z(nu100)) / (t2 - t1)
    return z(nu40) + b * t1, b


def nu_at(a, b, temp_c):
    lg = a - b * math.log10(temp_c + 273.15)
    return 10 ** (10 ** lg) - 0.7


class Unit5Specific(unittest.TestCase):
    def test_20_surface_zone(self):
        # the outer 10 % of the radius carries 19 % of the bending moment
        self.assertAlmostEqual((1 - 0.9 ** 2) * 100, 19.0, delta=0.01)
        self.assertAlmostEqual((1 - 0.99 ** 2) * 100, 1.99, delta=0.01)
        for token in ("nitriding", "galvanising", "shot peening", "phosphate"):
            self.assertIn(token, BODY.lower())

    def test_21_turned_roughness(self):
        ra = (0.20 ** 2) / (32 * 0.8) * 1000
        self.assertAlmostEqual(ra, 1.5625, delta=0.001)
        self.assertAlmostEqual((0.10 ** 2) / (32 * 0.8) * 1000, 0.3906, delta=0.001)
        self.assertAlmostEqual(1.5625 / 0.3906, 4.0, delta=0.01)
        self.assertIn("1.56 micron", BODY)

    def test_22_faraday_plating(self):
        self.assertAlmostEqual(58.7 / (2 * 96500) * 3600, 1.095, delta=0.002)
        current = 300 * 0.5
        self.assertAlmostEqual(current, 150, delta=1e-9)
        volume = 0.5 * 20e-6                     # m3
        mass = volume * 8900                     # kg
        self.assertAlmostEqual(mass * 1000, 89.0, delta=0.05)
        t = mass * 2 * 96500 / (0.0587 * current * 0.95)
        self.assertAlmostEqual(t, 2053, delta=2)
        self.assertAlmostEqual(t / 60, 34.2, delta=0.1)
        self.assertIn("34", PROBLEMS)

    def test_23_plating_rate_per_minute(self):
        # 300 A/m2 at 95 % gives 11.7 micron in 20 minutes, so 20 micron takes 34 minutes
        thick = (0.0587 * 300 * 1200 * 0.95) / (2 * 96500 * 8900) * 1e6
        self.assertAlmostEqual(thick, 11.7, delta=0.05)
        self.assertAlmostEqual(20 / 11.7 * 20, 34.2, delta=0.2)
        self.assertIn("11.7", BODY)

    def test_24_corrosion_rate_from_mass_loss(self):
        area = 2 * (50 * 25 + 50 * 3 + 25 * 3) / 100      # cm2
        self.assertAlmostEqual(area, 29.5, delta=1e-9)
        hours = 90 * 24
        cr = 87.6 * 1200 / (7.85 * area * hours)
        self.assertAlmostEqual(cr, 0.210, delta=0.002)
        self.assertAlmostEqual(cr * 10, 2.10, delta=0.02)
        self.assertIn("0.21", PROBLEMS)

    def test_25_corrosion_current_rate(self):
        rate = (0.0558 * 0.1) / (2 * 96500 * 7850)      # m/s
        self.assertAlmostEqual(rate * 1000 * 3.156e7, 0.116, delta=0.002)
        self.assertIn("0.116", BODY)

    def test_26_sacrificial_anode(self):
        current = 20e-3 * 2.5
        self.assertAlmostEqual(current, 0.05, delta=1e-9)
        seconds = 2 * 365 * 24 * 3600
        mass = 65.4 * current * seconds / (2 * 96500)
        self.assertAlmostEqual(mass, 1069, delta=3)
        self.assertAlmostEqual(mass / 0.90, 1188, delta=6)
        self.assertAlmostEqual(mass / 1000, 1.07, delta=0.01)
        self.assertIn("1.07 kg", PROBLEMS)

    def test_27_cell_voltages(self):
        self.assertAlmostEqual(0.76 + 0.34, 1.10, delta=1e-9)
        self.assertAlmostEqual(0.76 - 0.44, 0.32, delta=1e-9)
        for token in ("1.10 V", "0.32 V"):
            self.assertIn(token, BODY)

    def test_28_walther_viscosity(self):
        a, b = walther(68, 8.6)
        self.assertAlmostEqual(a, 9.377, delta=0.003)
        self.assertAlmostEqual(b, 3.651, delta=0.003)
        self.assertAlmostEqual(nu_at(a, b, 60), 28.7, delta=0.3)
        self.assertTrue(8.6 < nu_at(a, b, 60) < 68)
        self.assertAlmostEqual(nu_at(a, b, 40), 68, delta=0.5)
        self.assertAlmostEqual(nu_at(a, b, 100), 8.6, delta=0.1)
        self.assertIn("28.7", PROBLEMS)

    def test_29_viscosity_index_curves(self):
        # a VI 70 and a VI 150 oil that are both 10 cSt at 100 C
        a1, b1 = walther(150, 10)
        a2, b2 = walther(68, 10)
        self.assertAlmostEqual(nu_at(a1, b1, 30), 316, delta=6)
        self.assertAlmostEqual(nu_at(a2, b2, 30), 110, delta=3)
        self.assertAlmostEqual(nu_at(a1, b1, 100), 10, delta=0.2)
        self.assertAlmostEqual(nu_at(a2, b2, 100), 10, delta=0.2)
        self.assertGreater(nu_at(a1, b1, 30), nu_at(a2, b2, 30))
        self.assertIn("300 cSt", BODY)

    def test_30_paint_quantities(self):
        wft = 75 * 100 / 60
        self.assertAlmostEqual(wft, 125, delta=1e-9)
        litres = 120 * 125e-6 * 1000
        self.assertAlmostEqual(litres, 15.0, delta=0.02)
        self.assertAlmostEqual(litres * 1.15, 17.25, delta=0.02)
        self.assertAlmostEqual(17.25 * 1.4, 24.15, delta=0.03)
        self.assertAlmostEqual(17.25 * 450, 7762.5, delta=1)
        self.assertAlmostEqual(10 * 60 / 75, 8.0, delta=1e-9)
        self.assertAlmostEqual(120 / 8, 15.0, delta=1e-9)
        self.assertIn("17.25", PROBLEMS)

    def test_31_corrosion_allowance_and_structure(self):
        self.assertAlmostEqual((6.0 - 4.5) / 0.25, 6.0, delta=1e-9)
        self.assertAlmostEqual(4.5 + 0.25 * 12, 7.5, delta=1e-9)
        self.assertAlmostEqual(1.5 / 12, 0.125, delta=1e-9)
        self.assertIn("7.5 mm", PROBLEMS)
        # the film parameter of the oil card
        self.assertAlmostEqual(1.2 / math.sqrt(0.4 ** 2 + 0.3 ** 2), 2.4, delta=1e-9)
        self.assertIn("2.4", BODY)

    def test_32_tabs_and_counts(self):
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "viva", "exam"])
        self.assertEqual(UNIT["hours"], 10)
        self.assertEqual(UNIT["weightage"], 17)
        self.assertEqual(UNIT["theory_marks"], 12)
        self.assertEqual(UNIT["course_outcomes"], ["CO5"])
        self.assertEqual(UNIT["practical_numbers"], [5])
        self.assertEqual(len(UNIT["notes"]), 6)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 6)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 9)
        self.assertEqual(len(UNIT["diagrams"]), 8)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 17)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 12)
        self.assertEqual(sum(q["marks"] for q in UNIT["exam_questions"]), 39)
        for bad in ("? no", "rather:", "tbd", "xxx"):
            self.assertNotIn(bad, (BODY + PROBLEMS).lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
