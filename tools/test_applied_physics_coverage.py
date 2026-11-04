"""Cross-unit guard for Applied Physics (DI01000121), Semester 1 for some branches and 2 for others.

The per-unit test checks one unit's content; this file checks the promises that span the subject:
the syllabus totals, the two-semester branch mapping, the bilingual rule, the shelf index and the
publisher contract (the helper must accept a subject whose semester depends on the branch).

Run from the repo root:  python3 -m unittest tools.test_applied_physics_coverage -v
"""
import base64
import gzip
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000121 import SEM1_BRANCHES, SEM2_BRANCHES, MISSING_BRANCHES  # noqa: E402

CODE = "DI01000121"
PATH = ROOT / "content/common/sem1/DI01000121"
SUBJECT = json.loads((PATH / "subject.json").read_text(encoding="utf-8"))
GUJARATI = re.compile(r"[\u0a80-\u0aff]")


def unit_files():
    return sorted(PATH.glob("unit*.json"))


class AppliedPhysicsCoverage(unittest.TestCase):
    def test_01_syllabus_totals(self):
        self.assertEqual(SUBJECT["code"], CODE)
        self.assertEqual(SUBJECT["total_hours"], 45)
        self.assertEqual(sum(u["hours"] for u in SUBJECT["units"]), 45)
        self.assertEqual(sum(u["weightage"] for u in SUBJECT["units"]), 100)
        self.assertEqual([u["hours"] for u in SUBJECT["units"]], [7, 8, 12, 8, 10])
        self.assertEqual([u["weightage"] for u in SUBJECT["units"]], [17, 14, 28, 17, 24])
        self.assertEqual(sum(SUBJECT["theory_marks_by_unit"].values()), 70)
        self.assertEqual(SUBJECT["exam"]["total"], 150)
        self.assertEqual(SUBJECT["exam"]["credits"], 4)
        self.assertEqual((SUBJECT["teaching"]["lecture"], SUBJECT["teaching"]["practical"]), (3, 2))
        self.assertEqual(SUBJECT["theory_rbt_percent"],
                         {"remember": 26, "understand": 37, "apply": 37,
                          "analyze": 0, "evaluate": 0, "create": 0})
        self.assertEqual(sum(SUBJECT["theory_rbt_marks"].values()), 70)
        self.assertEqual(len(SUBJECT["course_outcomes"]), 5)

    def test_02_practicals_are_the_official_fourteen(self):
        practicals = SUBJECT["official_practicals"]
        self.assertEqual(len(practicals), 14)
        self.assertEqual(sum(p["hours"] for p in practicals), 30)
        self.assertEqual([p["no"] for p in practicals], list(range(1, 15)))
        for p in practicals:
            self.assertTrue(GUJARATI.search(p["outcome"]["gu"]))
            self.assertIn(p["unit"], (1, 3, 4, 5))

    def test_03_two_semester_branch_map(self):
        self.assertEqual(SUBJECT["semesters"], [1, 2])
        self.assertEqual(SUBJECT["branches"], SEM1_BRANCHES + SEM2_BRANCHES)
        self.assertEqual(SUBJECT["semester_by_branch"],
                         {b: 1 for b in SEM1_BRANCHES} | {b: 2 for b in SEM2_BRANCHES})
        self.assertEqual(len(SUBJECT["branches"]), 10)
        # the PDF also prints Ceramic, Renewable Energy, Fabrication, Textile Design and
        # Mechanical (CAD/CAM); the app does not carry those branches yet, and that is recorded.
        for key in MISSING_BRANCHES:
            self.assertNotIn(key, SUBJECT["branches"])

    def test_04_exporter_lists_it_in_the_right_semester(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=300)
            self.assertEqual(r.returncode, 0, r.stderr[:2000])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            subject = json.loads((out / f"subjects/{CODE}.json").read_text(encoding="utf-8"))
            self.assertEqual(catalog["subjects"][CODE]["name"]["en"], "Applied Physics")
            self.assertEqual(catalog["subjects"][CODE]["languages"], ["en", "gu"])
            self.assertEqual(subject["semesters"], [1, 2])
            carriers = {}
            for b in catalog["branches"]:
                for sem, codes in b["semesters"].items():
                    if CODE in codes:
                        carriers[b["key"]] = int(sem)
            self.assertEqual(carriers, SUBJECT["semester_by_branch"])
            # a computer or electrical student does not take Applied Physics
            for other in ("computer", "it", "electrical", "ec", "aeronautical"):
                self.assertNotIn(other, carriers)

    def test_05_publisher_helper_understands_per_branch_semesters(self):
        payload = (ROOT / "tools/publisher_payloads/hardware.b64").read_text().strip()
        helper = json.loads(gzip.decompress(base64.b64decode(payload)))["helper"]
        self.assertIn("listed_branches", helper,
                      "the helper must accept a subject whose semester depends on the branch")
        self.assertIn("common_to_all_branches", helper)
        exported = json.loads((PATH / "subject.json").read_text(encoding="utf-8"))
        self.assertTrue(exported["branches"] and exported["semesters"])
        # the acceptance rule, run here so a broken BRANCH_SEMS fails in the test job
        from export_app_content import BRANCH_SEMS
        for branch in exported["branches"]:
            hits = [s for s in exported["semesters"]
                    if CODE in BRANCH_SEMS.get(branch, {}).get(s, [])]
            self.assertEqual(hits, [exported["semester_by_branch"][branch]],
                             f"{branch}: registered in {hits}")

    def test_06_every_built_unit_is_bilingual_and_tagged(self):
        files = unit_files()
        self.assertTrue(files, "no unit is built yet")
        for fp in files:
            unit = json.loads(fp.read_text(encoding="utf-8"))
            text = json.dumps(unit, ensure_ascii=False)
            self.assertIn('"gu"', text, f"{fp.name} carries no Gujarati")
            self.assertIn('"en"', text)
            spec = next(u for u in SUBJECT["units"] if u["no"] == unit["unit"])
            self.assertEqual(unit["title"], spec["title"])
            self.assertEqual((unit["hours"], unit["weightage"]),
                             (spec["hours"], spec["weightage"]))
            self.assertEqual(spec["file"], fp.name)
            tags = {i.get("syllabus_item") for s in unit["notes"][:-1] for i in s["items"]}
            expected = {t["en"].split()[0] + "." + t["en"].split()[1].split(".")[0].strip(".")
                        for t in spec["topics"]}
            self.assertTrue(tags, f"{fp.name}: no card carries a syllabus item")
            self.assertTrue(all(t.startswith(f"{unit['unit']}.") for t in tags),
                            f"{fp.name}: tags {sorted(tags)}")

    def test_07_unbuilt_units_are_still_honest(self):
        built = {json.loads(f.read_text(encoding="utf-8"))["unit"] for f in unit_files()}
        for spec in SUBJECT["units"]:
            if spec["no"] not in built:
                self.assertIsNone(spec["file"], f"unit {spec['no']} claims a file it does not have")

    def test_08_shelf_index(self):
        index = (ROOT / "preview/workshop/index.html").read_text(encoding="utf-8")
        manifest = json.loads((ROOT / "preview/workshop/manifest.json").read_text(encoding="utf-8"))
        registered = {u["unit"] for u in manifest["units"] if u.get("code") == CODE}
        self.assertTrue(registered)
        for no in registered:
            self.assertIn(f"{CODE}_u{no}.html", index)
            self.assertTrue((ROOT / f"preview/workshop/{CODE}_u{no}.html").is_file())


if __name__ == "__main__":
    unittest.main(verbosity=2)
