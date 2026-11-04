"""Cross-unit guard for Communication Skills in English (DI01000031), Semester 1, all branches.

The per-unit tests check the content inside one unit; this file checks the promises that span the
whole subject: the syllabus totals, the tagging of every sub-clause, the literature requirement
(summaries and Q&A), the shelf index, and the publisher contract that broke the maths publish.

Run from the repo root:  python3 -m unittest tools.test_english_coverage -v
"""
import base64
import gzip
import hashlib
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

CODE = "DI01000031"
PATH = ROOT / "content/common/sem1/DI01000031"
APP_TABS = {"notes", "programs", "diagrams", "flowcharts", "algorithms", "syntax", "equations",
            "numericals", "viva", "exam"}

SUBJECT = json.loads((PATH / "subject.json").read_text(encoding="utf-8"))
UNITS = {no: json.loads((PATH / f"unit{no}.json").read_text(encoding="utf-8")) for no in (1, 2, 3, 4)}


def plain(markup):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"</?[a-zA-Z][^>]*>", " ", markup))).strip()


def unit_text(unit):
    parts = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "en" and isinstance(v, str):
                    parts.append(plain(v))
                else:
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(unit)
    return " ".join(parts).lower()


class EnglishCoverage(unittest.TestCase):
    def test_01_subject_metadata_matches_the_pdf(self):
        self.assertEqual(SUBJECT["code"], CODE)
        self.assertEqual(SUBJECT["semester"], 1)
        self.assertEqual(SUBJECT["branch"], "common")
        self.assertTrue(SUBJECT["common_to_all_branches"])
        self.assertEqual(SUBJECT["languages"], ["en"])
        self.assertEqual(SUBJECT["total_hours"], 30)
        self.assertEqual(sum(u["hours"] for u in SUBJECT["units"]), 30)
        self.assertEqual([u["no"] for u in SUBJECT["units"]], [1, 2, 3, 4])
        self.assertEqual(sum(SUBJECT["theory_marks_by_unit"].values()), 70)
        self.assertEqual(sum(SUBJECT["theory_rbt_marks"].values()), 70)
        self.assertEqual(SUBJECT["exam"],
                         {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20,
                          "practical_ese": 30, "total": 150, "credits": 3})
        self.assertEqual(SUBJECT["teaching"], {"lecture": 2, "tutorial": 0, "practical": 2})
        self.assertEqual(len(SUBJECT["course_outcomes"]), 5)
        self.assertEqual(len(SUBJECT["official_practicals"]), 10)

    def test_02_every_unit_file_matches_the_syllabus(self):
        for no, unit in UNITS.items():
            spec = next(u for u in SUBJECT["units"] if u["no"] == no)
            self.assertEqual(unit["title"], spec["title"])
            self.assertEqual(unit["hours"], spec["hours"])
            self.assertEqual(unit["weightage"], spec["weightage"])
            self.assertEqual(unit["subject"], CODE)
            self.assertEqual(unit["unit"], no)
            self.assertEqual(unit["course_outcomes"], [spec["course_outcome"]])
            self.assertEqual(set(unit["tabs"]) <= APP_TABS, True, f"unit {no} has an unknown tab")
            self.assertNotIn("numericals", unit["tabs"])

    def test_03_every_sub_clause_is_tagged(self):
        expected = {"1": ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"],
                    "2": ["2.1", "2.2", "2.3", "2.4", "2.5"],
                    "3": ["3.1", "3.2", "3.3"],
                    "4": ["4.1", "4.2"]}
        for no, unit in UNITS.items():
            tags = [it["syllabus_item"] for s in unit["notes"][:-1] for it in s["items"]]
            for clause in expected[str(no)]:
                self.assertIn(clause, tags, f"unit {no} has no card for {clause}")
            self.assertTrue(all(t.startswith(f"{no}.") for t in tags), (no, tags))

    def test_04_syllabus_topics_are_actually_taught(self):
        checks = {
            1: ["sender", "encoding", "channel", "decoding", "receiver", "noise", "feedback",
                "upward", "downward", "verbal", "non-verbal", "visual", "interpersonal",
                "intrapersonal", "extra personal", "mass", "barrier"],
            2: ["noun", "pronoun", "adjective", "adverb", "preposition", "conjunction",
                "interjection", "present perfect", "past perfect", "future simple", "can", "could",
                "may", "might", "must", "shall", "will", "should", "would", "ought to", "need",
                "svo", "sva", "svc"],
            3: ["the leopard", "ruskin bond", "after twenty years", "o. henry", "stopping by woods",
                "robert frost"],
            4: ["inquiry", "reply to", "order", "complaint", "paragraph", "festivals", "environment",
                "famous personalit", "sport", "friends and family"],
        }
        for no, words in checks.items():
            text = unit_text(UNITS[no])
            for word in words:
                self.assertIn(word, text, f"unit {no} never teaches: {word}")

    def test_05_literature_has_summary_and_questions(self):
        unit = UNITS[3]
        cards = [it for s in unit["notes"][:-1] for it in s["items"]]
        summaries = [it for it in cards if "Summary" in it["body"]["en"]]
        self.assertGreaterEqual(len(summaries), 9, "the three texts need full summaries")
        stanza_cards = [it for it in cards if "Stanza" in it["h"]["en"]]
        self.assertEqual(len(stanza_cards), 4, "the poem needs one card per stanza")
        answers = [it for it in unit["notes"][-1]["items"]]
        self.assertGreaterEqual(len(answers), 12, "the literature unit needs a full Q&A set")
        for item in answers:
            self.assertGreater(len(plain(item["body"]["en"])), 300)

    def test_06_grammar_and_writing_stay_example_driven(self):
        # The user's rule: only the literature unit gets long prose; the rest teaches by example.
        for no in (1, 2, 4):
            unit = UNITS[no]
            for s in unit["notes"][:-1]:
                for item in s["items"]:
                    body = item["body"]["en"]
                    hay = body + item["h"]["en"]
                    self.assertTrue("xample" in hay or "Model" in hay or "Worked" in hay,
                                    f"unit {no} card without an example or a model")
                    self.assertNotIn("<blockquote", body)

    def test_07_practice_pairs_with_exam_questions(self):
        for no, unit in UNITS.items():
            practice = unit["notes"][-1]["items"]
            exam = unit["exam_questions"]
            self.assertEqual(len(practice), len(exam), f"unit {no}")
            self.assertEqual(len(practice), unit["answered_practice_count"])
            for i, (item, q) in enumerate(zip(practice, exam), 1):
                self.assertEqual(item["h"]["en"], f"Practice {i}. {q['q']['en'].replace('Practice: ', '')}")
                self.assertTrue(q["marks"] in (3, 4, 5))

    def test_08_shelf_lists_all_four_units(self):
        index = (ROOT / "preview/workshop/index.html").read_text(encoding="utf-8")
        manifest = json.loads((ROOT / "preview/workshop/manifest.json").read_text(encoding="utf-8"))
        for no in (1, 2, 3, 4):
            self.assertIn(f"{CODE}_u{no}.html", index, f"unit {no} is not on the shelf index")
            self.assertTrue((ROOT / f"preview/workshop/{CODE}_u{no}.html").is_file())
        registered = [u for u in manifest["units"] if u.get("code") == CODE]
        self.assertEqual(sorted(u["unit"] for u in registered), [1, 2, 3, 4])

    def test_09_export_and_publisher_contract(self):
        payload = (ROOT / "tools/publisher_payloads/hardware.b64").read_text().strip()
        helper = json.loads(gzip.decompress(base64.b64decode(payload)))["helper"]
        self.assertIn("common_to_all_branches", helper,
                      "the publisher helper must understand common subjects")

        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=300)
            self.assertEqual(r.returncode, 0, r.stderr)
            subject = json.loads((out / f"subjects/{CODE}.json").read_text(encoding="utf-8"))
            self.assertEqual(subject["available_units"], [1, 2, 3, 4])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            self.assertEqual(catalog["subjects"][CODE]["status"], "available")
            branches = {b["key"] for b in catalog["branches"]}
            carriers = {b["key"] for b in catalog["branches"]
                        if CODE in b.get("semesters", {}).get("1", [])}
            self.assertEqual(carriers, branches,
                             "a common subject must be listed in semester 1 of every branch")
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)

    def test_10_english_only_content(self):
        for no, unit in UNITS.items():
            text = json.dumps(unit, ensure_ascii=False)
            self.assertNotIn('"gu"', text, f"unit {no} carries a gu key")
            self.assertIsNone(re.search(r"[\u0a80-\u0aff\u0900-\u097f]", text),
                              f"unit {no} carries Indic script")


if __name__ == "__main__":
    unittest.main(verbosity=2)
