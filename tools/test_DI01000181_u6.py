"""Unit 6 tests for Engineering Materials Science DI01000181.

Pins the numbers of the last unit: embodied energy and what recycling saves, the payback distance of a
lighter part, the 1500 kg of an electric car, the 96S2P pack, the 400 W module and its 1.6 kWh a day,
the CO2 of a kilometre and the value of press shop scrap - every figure re-derived from its own data.
"""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mattest_lib import unit_suite, strip_html  # noqa: E402
from subject_DI01000181 import SUBJ_DIR  # noqa: E402

Unit6 = unit_suite(6)

UNIT = json.loads((SUBJ_DIR / "unit6.json").read_text(encoding="utf-8"))
CARDS = [it for s in UNIT["notes"][:-1] for it in s["items"]]
BODY = strip_html(" ".join(it["h"]["en"] + " " + it["body"]["en"] for it in CARDS))
PROBLEMS = strip_html(" ".join(it["body"]["en"] for it in UNIT["notes"][-1]["items"]))


class Unit6Specific(unittest.TestCase):
    def test_20_embodied_energy_table(self):
        self.assertAlmostEqual(170 / 8, 21.25, delta=0.01)
        self.assertAlmostEqual((1 - 8 / 170) * 100, 95.3, delta=0.1)
        self.assertAlmostEqual((1 - 10 / 25) * 100, 60.0, delta=0.01)
        self.assertAlmostEqual((1 - 12 / 15) * 100, 20.0, delta=0.01)
        self.assertAlmostEqual((1 - 40 / 80) * 100, 50.0, delta=0.01)
        for token in ("170", "8 MJ", "5 %", "500"):
            self.assertIn(token, BODY)

    def test_21_lightweight_mass_and_energy(self):
        mass = 12 * (2.70 / 7.85) * 1.5
        self.assertAlmostEqual(mass, 6.19, delta=0.01)
        self.assertAlmostEqual(12 - mass, 5.81, delta=0.01)
        self.assertAlmostEqual((12 - mass) / 12 * 100, 48.4, delta=0.2)
        extra = mass * 170 - 12 * 25
        self.assertAlmostEqual(extra, 752, delta=1)
        mixed = 0.6 * 8 + 0.4 * 170
        self.assertAlmostEqual(mixed, 72.8, delta=0.05)
        self.assertAlmostEqual(mass * mixed - 300, 151, delta=1)
        self.assertIn("752", PROBLEMS)

    def test_22_payback_distance(self):
        saving_kwh_100km = 0.4 * 0.0581
        self.assertAlmostEqual(saving_kwh_100km, 0.02324, delta=1e-5)
        per_km_kj = saving_kwh_100km / 100 * 3600
        self.assertAlmostEqual(per_km_kj, 0.8366, delta=0.002)
        self.assertAlmostEqual(752 / (per_km_kj / 1000), 898900, delta=3000)
        self.assertAlmostEqual(151 / (per_km_kj / 1000), 180500, delta=1500)
        self.assertIn("900 000 km", PROBLEMS)
        self.assertIn("180 000 km", PROBLEMS)

    def test_23_electric_car_masses(self):
        rows = {"steel": 675, "aluminium": 300, "battery": 225, "polymer": 180, "copper": 75,
                "glass": 45}
        self.assertEqual(sum(rows.values()), 1500)
        self.assertAlmostEqual(675 / 1500 * 100, 45.0, delta=0.1)
        self.assertAlmostEqual(225 / 1500 * 100, 15.0, delta=0.1)
        self.assertAlmostEqual(35 / 0.225, 155.6, delta=0.5)
        self.assertAlmostEqual(75 / 23, 3.26, delta=0.02)
        self.assertIn("675 kg", BODY)
        self.assertIn("15 %", BODY)

    def test_24_pack_from_cells(self):
        v = 96 * 3.7
        self.assertAlmostEqual(v, 355.2, delta=0.05)
        ah = 2 * 50
        self.assertAlmostEqual(v * ah / 1000, 35.5, delta=0.03)
        cells = 192 * 0.9
        self.assertAlmostEqual(cells, 172.8, delta=0.01)
        self.assertAlmostEqual(35500 / cells, 205.4, delta=0.5)
        self.assertAlmostEqual(35500 / 236, 150.4, delta=0.5)
        self.assertAlmostEqual(cells / 236 * 100, 73.2, delta=0.3)
        self.assertAlmostEqual(35.5 / 0.15, 236.7, delta=0.5)
        self.assertIn("237 km", PROBLEMS)

    def test_25_cell_energy_and_voltage(self):
        self.assertAlmostEqual(3.7 * 50, 185, delta=1e-9)
        self.assertAlmostEqual(35500 / 192, 184.9, delta=0.5)
        for chem in ("LFP", "NMC", "140", "220"):
            self.assertIn(chem, BODY)

    def test_26_solar_module(self):
        peak = 1000 * 2 * 0.20
        self.assertAlmostEqual(peak, 400, delta=1e-9)
        daily = 0.4 * 5 * 0.8
        self.assertAlmostEqual(daily, 1.6, delta=1e-9)
        self.assertAlmostEqual(4 / daily, 2.5, delta=1e-9)
        self.assertAlmostEqual(3 * 2, 6, delta=1e-9)
        self.assertAlmostEqual(3 * 1.6 * 365, 1752, delta=1)
        self.assertAlmostEqual(1752 * 0.71, 1244, delta=2)
        self.assertAlmostEqual(4 / (1 * 0.2 * 5 * 0.8), 5.0, delta=1e-9)
        self.assertIn("400 W", BODY)
        self.assertIn("1.28 kWh", BODY)

    def test_27_ev_and_petrol_carbon(self):
        self.assertAlmostEqual(0.15 * 0.71 * 1000, 106.5, delta=0.2)
        self.assertAlmostEqual(0.06 * 2.31 * 1000, 138.6, delta=0.2)
        self.assertAlmostEqual(107 * 15000 / 1000, 1605, delta=2)
        self.assertAlmostEqual(139 * 15000 / 1000, 2085, delta=2)
        self.assertAlmostEqual((2085 - 1605), 480, delta=2)
        self.assertIn("107 g/km", PROBLEMS)
        self.assertIn("139 g/km", PROBLEMS)

    def test_28_specific_strength(self):
        pairs = (("steel", 450, 7.85, 57), ("aluminium", 310, 2.70, 115),
                 ("magnesium", 200, 1.74, 115), ("GFRP", 300, 1.90, 158))
        for _, uts, rho, claim in pairs:
            self.assertAlmostEqual(uts / rho, claim, delta=1.5)
        self.assertAlmostEqual(1500 / 1.60, 938, delta=1)
        self.assertAlmostEqual(1500 / 1.60 / (450 / 7.85), 16.4, delta=0.2)
        self.assertIn("938", BODY)

    def test_29_scrap_recovery(self):
        output = 500 * 2000 / 1000
        self.assertAlmostEqual(output, 1000, delta=1e-9)
        sheet = 1000 / 0.82
        self.assertAlmostEqual(sheet, 1219.5, delta=1)
        scrap = sheet - 1000
        self.assertAlmostEqual(scrap, 219.5, delta=1)
        recovered = scrap * 0.92
        self.assertAlmostEqual(recovered, 202.0, delta=1)
        self.assertAlmostEqual(recovered * 1000 * 32 / 1e5, 64.6, delta=0.3)
        per_part = 2.5 / 0.82
        self.assertAlmostEqual(per_part, 3.05, delta=0.01)
        self.assertAlmostEqual(per_part * 55 - (per_part - 2.5) * 32 * 0.92, 151.5, delta=1)
        self.assertIn("202", PROBLEMS)

    def test_30_recycling_saving_of_one_part(self):
        self.assertAlmostEqual(20 * 170, 3400, delta=1e-9)
        self.assertAlmostEqual(20 * 8, 160, delta=1e-9)
        self.assertAlmostEqual(20 * 11.5, 230, delta=1e-9)
        self.assertAlmostEqual(20 * 0.5, 10, delta=1e-9)
        self.assertAlmostEqual(20 * 4, 80, delta=1e-9)
        self.assertAlmostEqual((3400 - 160) / 3600, 0.9, delta=0.01)
        self.assertIn("220 kg", PROBLEMS)

    def test_31_tabs_and_counts(self):
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "viva", "exam"])
        self.assertEqual(UNIT["hours"], 6)
        self.assertEqual(UNIT["weightage"], 15)
        self.assertEqual(UNIT["theory_marks"], 10)
        self.assertEqual(UNIT["course_outcomes"], ["CO6"])
        self.assertEqual(UNIT["practical_numbers"], [7])
        self.assertEqual(len(UNIT["notes"]), 6)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 6)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 8)
        self.assertEqual(len(UNIT["diagrams"]), 6)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 14)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 12)
        self.assertEqual(sum(q["marks"] for q in UNIT["exam_questions"]), 34)
        for bad in ("? no", "rather:", "tbd", "xxx"):
            self.assertNotIn(bad, (BODY + PROBLEMS).lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
