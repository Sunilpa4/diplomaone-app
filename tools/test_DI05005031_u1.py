"""Validation for Chemical Reaction Engineering (DI05005031) Unit 1 - bilingual.

Run from the tools directory:  python3 -m unittest test_DI05005031_u1 -v
"""
import json
import re
import sys
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI05005031 import SUBJ_DIR, DIAG_DIR, SUBJECT  # noqa: E402
from notes_workshop import audit_svg  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit1.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
SPEC = next(u for u in SUBJ["units"] if u["no"] == 1)

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")
GUJARATI = re.compile(r"[\u0a80-\u0aff]")
FILLER = ("lorem", "todo", "tbd", "xxx", "placeholder", "[insert", "coming soon")


def strip_html(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def text_nodes(obj, out=None):
    out = [] if out is None else out
    if isinstance(obj, dict):
        if "en" in obj and isinstance(obj.get("en"), str):
            out.append(obj)
        else:
            for v in obj.values():
                text_nodes(v, out)
    elif isinstance(obj, list):
        for v in obj:
            text_nodes(v, out)
    return out


NODES = text_nodes(UNIT)
CARDS = [it for s in UNIT["notes"] for it in s["items"]]
TEACHING = [it for s in UNIT["notes"][:-1] for it in s["items"]]
PROBLEMS = UNIT["notes"][-1]["items"]


class Unit1(unittest.TestCase):
    def test_01_unit_file_and_identity(self):
        self.assertEqual(UNIT["subject"], "DI05005031")
        self.assertEqual(UNIT["unit"], 1)
        self.assertTrue(UNIT["official"])
        self.assertEqual(UNIT["format"], "notes")
        for key in ("notes", "diagrams", "equations", "viva", "exam_questions", "sources"):
            self.assertIn(key, UNIT)

    def test_02_matches_the_syllabus(self):
        self.assertEqual(UNIT["title"], SPEC["title"])
        self.assertEqual(UNIT["hours"], SPEC["hours"])
        self.assertEqual(UNIT["weightage"], SPEC["weightage"])
        self.assertEqual(UNIT["theory_marks"], SPEC["theory_marks"])
        self.assertEqual((UNIT["hours"], UNIT["weightage"], UNIT["theory_marks"]), (7, 15, 10))

    def test_03_every_text_is_bilingual(self):
        self.assertEqual(UNIT["languages"], ["en", "gu"])
        self.assertTrue(NODES, "no text nodes found")
        for n in NODES:
            self.assertTrue(n.get("en", "").strip(), f"empty en: {n}")
            self.assertTrue(n.get("gu", "").strip(), f"empty gu for: {n['en'][:50]!r}")
            self.assertFalse(GUJARATI.search(n["en"]),
                             f"Gujarati inside en: {n['en'][:60]!r}")
            if len(n["gu"]) >= 20:
                self.assertTrue(GUJARATI.search(n["gu"]),
                                f"gu is not Gujarati: {n['gu'][:60]!r}")

    def test_04_no_filler_text(self):
        for n in NODES:
            low = (n["en"] + " " + n["gu"]).lower()
            for bad in FILLER:
                self.assertNotIn(bad, low, f"filler '{bad}' in: {n['en'][:60]!r}")

    def test_05_sections_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 8)
        self.assertEqual(len(TEACHING), 7)
        self.assertEqual(len(PROBLEMS), 6)
        self.assertEqual(UNIT["lesson_count"], len(CARDS))
        self.assertEqual(UNIT["answered_practice_count"], len(PROBLEMS))
        for sec in UNIT["notes"]:
            self.assertTrue(sec["title"]["en"] and sec["title"]["gu"])
            self.assertTrue(sec["items"])

    def test_06_diagrams_present_and_used(self):
        listed = {d["id"] for d in UNIT["diagrams"]}
        self.assertEqual(len(listed), 6)
        referenced = {it["diagram"] for it in CARDS if it.get("diagram")}
        self.assertEqual(listed, referenced, "every figure must be shown by a card and vice versa")
        problems = []
        for d in UNIT["diagrams"]:
            path = DIAG_DIR / Path(d["file"]).name
            self.assertTrue(path.is_file(), f"missing {path}")
            self.assertTrue(d["title"]["gu"].strip())
            self.assertTrue(d["caption"]["gu"].strip())
            audit_svg(path, problems)
        self.assertEqual(problems, [])

    def test_07_svgs_are_clean(self):
        for d in UNIT["diagrams"]:
            raw = (DIAG_DIR / Path(d["file"]).name).read_text(encoding="utf-8")
            root = ET.fromstring(raw)
            vb = root.get("viewBox").split()
            self.assertEqual(len(vb), 4)
            self.assertAlmostEqual(float(vb[2]), 360, delta=0.01)
            for bad in ("<image", "foreignObject", "javascript:"):
                self.assertNotIn(bad, raw)

    def test_08_formulas(self):
        self.assertEqual(len(UNIT["equations"]), 5)
        total = 0
        for group in UNIT["equations"]:
            self.assertTrue(group["title"]["gu"].strip())
            for item in group["items"]:
                total += 1
                self.assertTrue(item["f"].strip())
                self.assertGreaterEqual(len(item["f"]), 6, f"formula too short: {item['f']!r}")
                self.assertRegex(item["f"], r"[=:~]|->", f"formula looks empty: {item['f']!r}")
                for key in ("name", "terms"):
                    self.assertTrue(item[key]["en"].strip())
                    self.assertTrue(item[key]["gu"].strip())
        self.assertEqual(total, 16)

    def test_09_viva(self):
        self.assertEqual(len(UNIT["viva"]), 4)
        total = sum(len(g["items"]) for g in UNIT["viva"])
        self.assertEqual(total, 12)
        for group in UNIT["viva"]:
            self.assertTrue(group["title"]["gu"].strip())
            for item in group["items"]:
                self.assertGreater(len(strip_html(item["q"]["en"])), 15)
                self.assertGreater(len(strip_html(item["a"]["en"])), 60)
                self.assertGreater(len(strip_html(item["a"]["gu"])), 40)

    def test_10_exam_questions(self):
        self.assertEqual(len(UNIT["exam_questions"]), 6)
        marks = 0
        for q in UNIT["exam_questions"]:
            self.assertTrue(q["q"]["en"].strip() and q["q"]["gu"].strip())
            self.assertIn(q["marks"], (4, 5, 6, 7))
            marks += q["marks"]
        # The numericals carry suggested marks, not official ones: the whole revision set may be
        # larger than the unit's 10 theory marks, but not absurdly so.
        self.assertLessEqual(marks, 40, "practice marks far above the unit")

    def test_11_bodies_are_valid_html(self):
        for it in CARDS:
            for lang in ("en", "gu"):
                html = it["body"][lang]
                self.assertNotIn("{'en'", html)
                self.assertNotIn('{"en"', html)
                for bad in ("<script", "<style", "<img", "javascript:"):
                    self.assertNotIn(bad, html)
                stack = []
                for m in TAG_RE.finditer(html):
                    tag, selfclose = m.group(1).lower(), m.group(2) == "/"
                    if tag in VOID or selfclose:
                        continue
                    if m.group(0).startswith("</"):
                        self.assertTrue(stack and stack[-1] == tag,
                                        f"stray </{tag}> in {lang} of {it['h']['en'][:40]}")
                        stack.pop()
                    else:
                        stack.append(tag)
                self.assertEqual(stack, [], f"unclosed tags in {lang} of {it['h']['en'][:40]}")
                self.assertGreater(len(strip_html(html)), 120)

    def test_12_derivations_are_shown(self):
        """The unit promises derivation-first writing: every card must show its algebra."""
        for it in TEACHING:
            html = it["body"]["en"]
            self.assertIn('class="math"', html,
                          f"card without a derivation block: {it['h']['en'][:50]}")
            self.assertIn("=", html)

    def test_13_solved_numbers(self):
        text = " ".join(strip_html(p["body"]["en"]) for p in PROBLEMS)
        for value in ("1.667", "3.2", "1.875", "55.3", "1.09", "52.9"):
            self.assertIn(value, text, f"worked value {value} missing from the numericals")
        gu = " ".join(strip_html(p["body"]["gu"]) for p in PROBLEMS)
        self.assertGreater(len(gu), 1200)

    def test_14_sources_and_notes(self):
        self.assertEqual(len(UNIT["sources"]), 4)
        for s in UNIT["sources"]:
            self.assertTrue(s["url"].startswith("https://"))
        self.assertIn("150", UNIT["assessment_note"]["en"])
        self.assertIn("150", UNIT["assessment_note"]["gu"])
        self.assertIn("not official", UNIT["question_provenance"])

    def test_15_subject_registration(self):
        self.assertEqual(SUBJ["code"], "DI05005031")
        self.assertEqual(SUBJ["semester"], 5)
        self.assertEqual(SUBJ["branch"], "chemical")
        self.assertEqual(SUBJ["languages"], ["en", "gu"])
        self.assertEqual(SUBJ["exam"]["total"], 150)
        self.assertEqual(SUBJ["exam"]["credits"], 4)
        self.assertEqual(sum(SUBJ["theory_marks_by_unit"].values()), 70)
        self.assertEqual(SUBJ["units"][0]["file"], "unit1.json")
        self.assertEqual(len(SUBJ["official_practicals"]), 15)


if __name__ == "__main__":
    unittest.main(verbosity=2)
