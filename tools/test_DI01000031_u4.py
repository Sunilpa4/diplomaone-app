"""Validation for Communication Skills in English (DI01000031) Unit 4 "Techniques of Writing".

Run from the repo root:  python3 -m unittest tools.test_DI01000031_u4 -v
"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000031 import SUBJ_DIR, DIAG_DIR, TABS  # noqa: E402
from notes_workshop import audit_svg, text_width  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit4.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")


def strip_html(html):
    return re.sub(r"<[^>]+>", " ", html)


def all_text(obj):
    out = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "en" and isinstance(v, str):
                    out.append(strip_html(v))
                else:
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(obj)
    return re.sub(r"\s+", " ", " ".join(out)).lower()


TEXT = all_text(UNIT)
CARDS = [it for s in UNIT["notes"][:-1] for it in s["items"]]
PRACTICE = [re.sub(r"\s+", " ", strip_html(it["body"]["en"]))
            for it in UNIT["notes"][-1]["items"]]


def assert_balanced(testcase, html, where):
    stack = []
    for m in TAG_RE.finditer(html):
        tag, selfclose = m.group(1).lower(), m.group(2) == "/"
        if tag in VOID or selfclose:
            continue
        if m.group(0).startswith("</"):
            testcase.assertTrue(stack and stack[-1] == tag, f"{where}: stray </{tag}>")
            if stack:
                stack.pop()
        else:
            stack.append(tag)
    testcase.assertFalse(stack, f"{where}: unclosed {stack}")


def words(html):
    return len(re.sub(r"<[^>]+>", " ", html).split())


class EnglishUnit4(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 4)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (4, 8, 20))
        self.assertEqual((spec["hours"], spec["weightage"]), (8, 20))
        self.assertEqual(UNIT["title"]["en"], "Techniques of Writing")
        self.assertEqual(spec["file"], "unit4.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["4"], 14)
        self.assertEqual(UNIT["tabs"], TABS)
        self.assertEqual(UNIT["course_outcomes"], ["CO4"])

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 4)
        self.assertEqual(UNIT["lesson_count"], 18)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 18)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 13)
        self.assertEqual(len(UNIT["diagrams"]), 3)
        self.assertEqual(len(UNIT["exam_questions"]), 13)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 12)
        self.assertEqual(UNIT["answered_practice_count"], 13)
        self.assertNotIn("numericals", UNIT, "this subject has no numerical tab")

    def test_03_syllabus_coverage(self):
        for word in ["subject", "salutation", "signature", "inquiry", "reply", "order", "complaint",
                     "paragraph", "topic sentence", "concluding sentence", "festival", "environment",
                     "famous personalit", "sport", "friends and family", "linker"]:
            self.assertIn(word, TEXT, f"unit 4 misses: {word}")

    def test_04_both_clauses_are_tagged(self):
        tags = [it.get("syllabus_item") for it in CARDS]
        self.assertEqual(tags.count("4.1"), 10)
        self.assertEqual(tags.count("4.2"), 8)
        self.assertEqual(len(tags), 18)

    def test_05_english_only(self):
        def walk(o):
            if isinstance(o, dict):
                self.assertNotIn("gu", o)
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
            elif isinstance(o, str):
                self.assertNotRegex(o, r"[\u0a80-\u0aff]")
                self.assertNotRegex(o, r"[\u0900-\u097f]")

        walk(UNIT)
        self.assertEqual(UNIT["languages"], ["en"])

    def test_06_every_card_models_the_skill(self):
        for i, item in enumerate(CARDS, 1):
            body = item["body"]["en"]
            self.assertGreater(len(strip_html(body)), 500, f"card {i} is too thin to teach from")
            for bad in ("TODO", "Lorem", "TBD"):
                self.assertNotIn(bad, body)
        # the four e-mail types each carry a complete model with a subject line
        for kind in ("inquiry", "reply", "order", "complaint"):
            model = next(it for it in CARDS if kind in it["h"]["en"].lower())
            self.assertIn("Subject:", model["body"]["en"], f"{kind}: model has no subject line")
            self.assertIn("Dear", model["body"]["en"], f"{kind}: model has no salutation")
            self.assertIn("Regards", model["body"]["en"], f"{kind}: model has no closing")

    def test_07_model_paragraphs_are_about_150_words(self):
        models = [it for it in CARDS if it["h"]["en"].startswith("3.") and "Model" in it["h"]["en"]]
        self.assertEqual(len(models), 5)
        for item in models:
            body = item["body"]["en"]
            start = body.index("<h4>The paragraph")
            end = body.index("Why it works")
            count = words(body[start:end])
            self.assertGreater(count, 130, f"{item['h']['en']} is shorter than a paragraph")
            self.assertLess(count, 200, f"{item['h']['en']} is longer than a paragraph")

    def test_08_diagrams_valid_and_referenced(self):
        listed = {d["id"] for d in UNIT["diagrams"]}
        used = {it["diagram"] for s in UNIT["notes"] for it in s["items"] if it.get("diagram")}
        self.assertEqual(listed, used, "every diagram must be linked from a card and vice versa")
        problems = []
        for d in UNIT["diagrams"]:
            path = DIAG_DIR / f"{d['id']}.svg"
            self.assertTrue(path.is_file(), path)
            raw = path.read_text(encoding="utf-8")
            for bad in ("<script", "<style", "<marker", "<foreignObject", "<image", "href="):
                self.assertNotIn(bad, raw)
            root = ET.fromstring(raw)
            w, h = map(float, root.get("viewBox").split()[2:])
            self.assertEqual(w, 360)
            self.assertGreater(h, 100)
            audit_svg(path, problems)
        self.assertEqual(problems, [])

    def test_09_diagram_text_fits_the_canvas(self):
        for d in UNIT["diagrams"]:
            root = ET.fromstring((DIAG_DIR / f"{d['id']}.svg").read_text(encoding="utf-8"))
            for node in root.iter("{http://www.w3.org/2000/svg}text"):
                txt = "".join(node.itertext())
                if not txt:
                    continue
                size = float(node.get("font-size", "12"))
                bold = (node.get("font-weight") or "normal") == "bold"
                self.assertLess(text_width(txt, size, bold), 360 - 2,
                                f"{d['id']}: {txt!r} is wider than the canvas")

    def test_10_practice_matches_exam_questions(self):
        practice = UNIT["notes"][-1]
        self.assertTrue(practice["title"]["en"].startswith("4."))
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4, 5))
            self.assertGreater(len(item["body"]["en"]), 300, f"model answer {i} is too thin")
        self.assertTrue(UNIT["question_marks_are_suggested"])

    def test_11_answers_are_usable_models(self):
        joined = " ".join(PRACTICE).lower()
        for word in ["subject:", "dear", "regards", "topic sentence", "concluding"]:
            self.assertIn(word, joined, f"practice answers never show {word}")
        long_answers = [a for a in PRACTICE if words(a) >= 90]
        self.assertGreaterEqual(len(long_answers), 7, "too few full-length model answers")

    def test_12_html_is_balanced_and_clean(self):
        for si, section in enumerate(UNIT["notes"]):
            for ii, item in enumerate(section["items"]):
                body = (item.get("body") or {}).get("en", "")
                assert_balanced(self, body, f"notes {si}/{ii}")
                for bad in ("<script", "<style", "<img", "href=", "<iframe"):
                    self.assertNotIn(bad, body)
        for g in UNIT["equations"] + UNIT["viva"]:
            for e in g["items"]:
                assert_balanced(self, (e.get("terms") or e.get("a"))["en"], "equations/viva")

    def test_13_export_carries_the_unit(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=300)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI01000031_u4.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 3)
            self.assertEqual(unit["title"]["en"], "Techniques of Writing")
            subject = json.loads((out / "subjects/DI01000031.json").read_text(encoding="utf-8"))
            self.assertIn(4, subject["available_units"])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            self.assertEqual(catalog["subjects"]["DI01000031"]["status"], "available")
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
