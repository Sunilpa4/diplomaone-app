"""Cross-subject guard for the two mathematics subjects (DI01000021 and DI02000021).

The per-unit test files check the mathematics inside one unit; this file checks the promises that
span a whole subject: syllabus coverage, the practice/exam pairing, link integrity, subject totals
and the fact that both subjects are offered in every branch.

Run from the repo root:  python3 -m unittest tools.test_maths_coverage -v
"""
import html
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

SUBJECTS = {
    "DI01000021": (ROOT / "content/common/sem1/DI01000021", 1, list(range(0, 6))),
    "DI02000021": (ROOT / "content/common/sem2/DI02000021", 2, list(range(1, 6))),
}


def load_subject(code):
    path, semester, unit_nos = SUBJECTS[code]
    subject = json.loads((path / "subject.json").read_text(encoding="utf-8"))
    units = {}
    for no in unit_nos:
        f = path / f"unit{no}.json"
        units[no] = json.loads(f.read_text(encoding="utf-8")) if f.is_file() else None
    return subject, units


def plain(markup):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"</?[a-zA-Z][^>]*>", " ", markup))).strip()


class MathsCoverage(unittest.TestCase):
    def test_01_subject_metadata(self):
        for code, (_path, semester, unit_nos) in SUBJECTS.items():
            subject, units = load_subject(code)
            self.assertEqual(subject["code"], code)
            self.assertEqual(subject["branch"], "common")
            self.assertTrue(subject["common_to_all_branches"],
                            f"{code} must be offered to every branch")
            self.assertEqual(subject["semester"], semester)
            self.assertEqual(subject["languages"], ["en"])
            self.assertEqual(sorted(units), unit_nos)
            for no, unit in units.items():
                self.assertIsNotNone(unit, f"{code} unit {no} is missing")

    def test_02_every_syllabus_item_has_a_card(self):
        for code in SUBJECTS:
            subject, units = load_subject(code)
            for no, unit in units.items():
                spec = next(u for u in subject["units"] if u["no"] == no)
                tags = {it["syllabus_item"] for s in unit["notes"][:-1] for it in s["items"]
                        if it.get("syllabus_item")}
                expected = ({f"{no}.{i}" for i in range(1, len(spec["topics"]) + 1)}
                            if no else {f"foundation:{i}" for i in range(1, len(spec["topics"]) + 1)})
                self.assertEqual(tags, expected,
                                 f"{code} unit {no} covers {sorted(tags)} but the syllabus lists "
                                 f"{len(spec['topics'])} items")
                for s in unit["notes"][:-1]:
                    for it in s["items"]:
                        self.assertTrue(it.get("syllabus_item"),
                                        f"{code} u{no}: card {it['h']['en']!r} has no syllabus tag")

    def test_03_subject_totals_match_the_scheme(self):
        for code in SUBJECTS:
            subject, units = load_subject(code)
            hours = sum(u["hours"] for u in units.values())
            weight = sum(u["weightage"] for u in units.values())
            marks = sum(subject["theory_marks_by_unit"].values())
            self.assertEqual(subject.get("total_hours", hours), hours, f"{code} hours")
            self.assertEqual(hours, 45, f"{code} must total 45 teaching hours")
            self.assertEqual(weight, 100, f"{code} weightages must add to 100 %")
            self.assertEqual(marks, subject["exam"]["theory_ese"], f"{code} marks")
            self.assertEqual(marks, 70)

    def test_04_practice_answers_match_the_exam_list(self):
        for code in SUBJECTS:
            _subject, units = load_subject(code)
            for no, unit in units.items():
                practice = unit["notes"][-1]
                self.assertIn("practice", practice["title"]["en"].lower(),
                              f"{code} u{no}: last section is not the practice section")
                self.assertEqual(len(practice["items"]), len(unit["exam_questions"]),
                                 f"{code} u{no}: practice and exam lists differ")
                for i, (item, exam) in enumerate(zip(practice["items"], unit["exam_questions"]), 1):
                    question = exam["q"]["en"].replace("Practice: ", "")
                    self.assertEqual(item["h"]["en"], f"Practice {i}. {question}",
                                     f"{code} u{no}: pairing broken at {i}")
                    self.assertGreater(len(item["body"]["en"]), 170,
                                       f"{code} u{no}: model answer {i} is too thin")
                self.assertTrue(unit["question_marks_are_suggested"])
                for exam in unit["exam_questions"]:
                    self.assertIsInstance(exam["marks"], int)
                    self.assertGreater(exam["marks"], 0)

    def test_05_numericals_and_diagrams_are_all_reachable(self):
        for code in SUBJECTS:
            path, _sem, _nos = SUBJECTS[code]
            _subject, units = load_subject(code)
            for no, unit in units.items():
                ids = {n["id"] for n in unit["numericals"]}
                used = {e for s in unit["notes"][:-1] for it in s["items"]
                        for e in it.get("examples", [])}
                self.assertEqual(used - ids, set(), f"{code} u{no}: unknown example ids")
                self.assertEqual(ids - used, set(), f"{code} u{no}: numericals no card links to")
                self.assertEqual(len(ids), len(unit["numericals"]), f"{code} u{no}: duplicate ids")

                diagrams = {d["id"]: d["file"] for d in unit["diagrams"]}
                drawn = {it["diagram"] for s in unit["notes"] for it in s["items"]
                         if it.get("diagram")}
                self.assertEqual(drawn - set(diagrams), set(), f"{code} u{no}: missing diagram")
                self.assertEqual(set(diagrams) - drawn, set(), f"{code} u{no}: unused diagram")
                for did, rel in diagrams.items():
                    self.assertTrue((path / rel).is_file(), f"{code} u{no}: {rel} not on disk")
                for n in unit["numericals"]:
                    self.assertTrue(plain(n["a"]["en"]), f"{code} u{no}: {n['id']} has no answer")

    def test_06_no_unit_is_a_stub(self):
        for code in SUBJECTS:
            _subject, units = load_subject(code)
            for no, unit in units.items():
                if no == 0:
                    continue  # foundation unit: no marks, so judge it more loosely
                self.assertGreaterEqual(len(unit["notes"]), 6, f"{code} u{no}: too few sections")
                self.assertGreaterEqual(len(unit["numericals"]), 18, f"{code} u{no}: few numericals")
                self.assertGreaterEqual(sum(len(g["items"]) for g in unit["viva"]), 12,
                                        f"{code} u{no}: few viva questions")
                self.assertGreaterEqual(sum(len(g["items"]) for g in unit["equations"]), 10,
                                        f"{code} u{no}: thin formula sheet")
                self.assertGreaterEqual(len(unit["diagrams"]), 5, f"{code} u{no}: few diagrams")
                self.assertTrue(unit["learning_outcomes"])
                self.assertTrue(unit["assessment_note"]["en"])

    def test_07_export_lists_both_subjects_in_every_branch(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=240)
            self.assertEqual(r.returncode, 0, r.stderr)
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            branches = catalog["branches"]
            self.assertGreaterEqual(len(branches), 20)
            for b in branches:
                self.assertIn("DI01000021", b["semesters"].get("1", []),
                              f"{b['key']} is missing Mathematics-I in semester 1")
                self.assertIn("DI02000021", b["semesters"].get("2", []),
                              f"{b['key']} is missing Engineering Mathematics in semester 2")
            for code, (_p, _s, unit_nos) in SUBJECTS.items():
                subj = json.loads((out / f"subjects/{code}.json").read_text(encoding="utf-8"))
                self.assertEqual(subj["available_units"], unit_nos, code)

    def test_09_exporter_satisfies_the_publisher_contract(self):
        """The publisher refuses a subject that is not listed under its branch/semester.

        A common subject ("branch": "common") owns no branch entry, so it must appear in the
        semester of every branch instead. This is exactly what broke the publish run of PR #6.
        """
        import base64
        import gzip

        payload = (ROOT / "tools/publisher_payloads/hardware.b64").read_text().strip()
        helper = json.loads(gzip.decompress(base64.b64decode(payload)))["helper"]
        self.assertIn("common_to_all_branches", helper,
                      "the publisher helper must understand common subjects")

        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=240)
            self.assertEqual(r.returncode, 0, r.stderr)
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            by_key = {b["key"]: b for b in catalog["branches"]}
            for path in sorted((out / "subjects").glob("*.json")):
                subj = json.loads(path.read_text(encoding="utf-8"))
                semester = str(subj["semester"])
                carriers = [b["key"] for b in catalog["branches"]
                            if subj["code"] in b.get("semesters", {}).get(semester, [])]
                if subj.get("common_to_all_branches") or subj.get("branch") == "common":
                    self.assertEqual(sorted(carriers), sorted(by_key),
                                     f"{subj['code']} is common but not listed in every branch")
                else:
                    self.assertIn(subj["code"],
                                  by_key[subj["branch"]]["semesters"].get(semester, []),
                                  f"{subj['code']}: register branch/semester in the exporter")
                self.assertIn(subj["code"], catalog["subjects"])

    def test_08_maths_index_lists_every_unit(self):
        page = ROOT / "preview/workshop/maths.html"
        self.assertTrue(page.is_file(), "run python3 tools/maths_index.py")
        text = page.read_text(encoding="utf-8")
        for code, (_p, _s, unit_nos) in SUBJECTS.items():
            for no in unit_nos:
                self.assertIn(f'href="{code}_u{no}.html"', text, f"{code} unit {no} is not listed")
                self.assertTrue((ROOT / f"preview/workshop/{code}_u{no}.html").is_file(),
                                f"{code}_u{no}.html is not on the shelf")


if __name__ == "__main__":
    unittest.main(verbosity=2)
