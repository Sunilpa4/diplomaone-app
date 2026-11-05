"""Unit 1 tests for Engineering Materials Science DI01000181.

The shared rule book lives in mattest_lib; this file pins what Unit 1 is responsible for: the four
families, the five bonds, the three cells with their computed packing fractions, the density that
follows from a cell edge, and a tensile test whose numbers agree with its own curve.
"""
import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mattest_lib import unit_suite, strip_html  # noqa: E402
from subject_DI01000181 import SUBJ_DIR  # noqa: E402

Unit1 = unit_suite(1)

UNIT = json.loads((SUBJ_DIR / "unit1.json").read_text(encoding="utf-8"))
CARDS = [it for s in UNIT["notes"][:-1] for it in s["items"]]
BODY = strip_html(" ".join(it["h"]["en"] + " " + it["body"]["en"] for it in CARDS))
PROBLEMS = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))


class Unit1Specific(unittest.TestCase):
    def test_20_material_families(self):
        for name in ("metals", "ceramics", "polymers", "composites", "semiconductors",
                     "smart materials"):
            self.assertIn(name, BODY.lower(), f"missing family: {name}")

    def test_21_five_bonds(self):
        for name in ("electrovalent", "covalent", "coordinate", "hydrogen", "metallic"):
            self.assertIn(name, BODY.lower(), f"missing bond: {name}")

    def test_22_three_cells_and_their_numbers(self):
        self.assertAlmostEqual(math.pi * math.sqrt(3) / 8, 0.6802, delta=0.0002)
        self.assertAlmostEqual(math.pi / (3 * math.sqrt(2)), 0.7405, delta=0.0002)
        for token in ("bcc", "fcc", "hcp", "0.68", "0.74", "coordination"):
            self.assertIn(token, BODY.lower())

    def test_23_atoms_per_cell(self):
        self.assertEqual(8 * 1 / 8 + 1, 2)
        self.assertEqual(8 * 1 / 8 + 6 * 1 / 2, 4)
        self.assertIn("8 x 1/8 + 1 = 2", BODY)
        self.assertIn("6 x 1/2 = 4", BODY)

    def test_24_density_from_the_cell(self):
        rho_fe = 2 * 55.85 / (6.022e23 * (2.866e-8) ** 3)
        self.assertAlmostEqual(rho_fe, 7.877, delta=0.005)
        rho_cu = 4 * 63.55 / (6.022e23 * (3.615e-8) ** 3)
        self.assertAlmostEqual(rho_cu, 8.934, delta=0.01)
        self.assertIn("7.88", BODY)
        self.assertIn("8.94", BODY)

    def test_25_atoms_per_mm3(self):
        n_v = 2 / (2.866e-7) ** 3
        self.assertAlmostEqual(n_v / 1e19, 8.50, delta=0.02)
        self.assertIn("8.5e19", PROBLEMS)

    def test_26_tensile_test_numbers(self):
        a0 = math.pi * 12.5 ** 2 / 4
        self.assertAlmostEqual(a0, 122.72, delta=0.01)
        self.assertAlmostEqual(40000 / a0, 326, delta=0.5)
        self.assertAlmostEqual(62000 / a0, 505, delta=0.5)
        self.assertAlmostEqual(100 * (62.5 - 50) / 50, 25, delta=1e-9)
        self.assertIn("326 MPa", PROBLEMS)
        self.assertIn("25 %", PROBLEMS)

    def test_27_thermal_and_electrical(self):
        self.assertAlmostEqual(11.7e-6 * 20000 * 35, 8.19, delta=0.01)
        self.assertAlmostEqual(1.72e-8 * 100 / 2.5e-6, 0.688, delta=0.001)
        self.assertAlmostEqual(2.82e-8 * 100 / 2.5e-6, 1.128, delta=0.001)
        self.assertIn("8.19 mm", PROBLEMS)
        self.assertIn("0.688 ohm", PROBLEMS)

    def test_28_composite_rule_of_mixtures(self):
        e = 0.6 * 230 + 0.4 * 3.5
        rho = 0.6 * 1.8 + 0.4 * 1.2
        self.assertAlmostEqual(e, 139.4, delta=0.05)
        self.assertAlmostEqual(rho, 1.56, delta=0.001)
        self.assertAlmostEqual((e / rho) / (200 / 7.85), 3.51, delta=0.02)
        self.assertIn("139", PROBLEMS)

    def test_29_specific_strength_values(self):
        for uts, rho, val in ((450, 7.85, 57), (310, 2.70, 115), (950, 4.43, 214),
                              (700, 1.60, 438)):
            self.assertAlmostEqual(uts / rho, val, delta=1)
        self.assertIn("438", BODY)

    def test_30_tabs_and_thin_parts(self):
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "viva", "exam"])
        for bad in ("? no", "rather:", "tbd", "状态"):
            self.assertNotIn(bad, (BODY + PROBLEMS).lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
