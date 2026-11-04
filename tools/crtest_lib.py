"""Shared validation for the Chemical Reaction Engineering (DI05005031) units.

`unit_suite(number, expect)` returns a unittest.TestCase that checks one unit against the same rule
book every time:

  * identity and syllabus numbers (hours, weightage, marks, course outcome)
  * every text node bilingual, with real Gujarati in the "gu" value
  * figures listed, present, referenced by a card and inside their canvas
  * formulas, viva and solved numericals of the expected size
  * balanced HTML bodies with no script/style/image and no leaked Python dicts
  * the derivation-first promise: every teaching card carries an algebra block

The per-unit expectation dictionary keeps the numbers honest - if a unit silently loses a card or a
figure, its own file fails instead of passing with a smaller count.
"""
import json
import re
import sys
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from subject_DI05005031 import SUBJ_DIR, DIAG_DIR, SUBJECT  # noqa: E402
from notes_workshop import audit_svg  # noqa: E402

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")
GUJARATI = re.compile(r"[\u0a80-\u0aff]")
FILLER = ("lorem", "todo", "tbd", "xxx", "placeholder", "[insert", "coming soon")

EXPECT = {
    1: dict(sections=8, teaching=7, problems=6, figures=6, eq_groups=5, eq_items=16, viva=12,
            hours=7, weightage=15, marks=10, co="CO1"),
    2: dict(sections=6, teaching=6, problems=6, figures=5, eq_groups=4, eq_items=12, viva=12,
            hours=8, weightage=17, marks=12, co="CO2"),
    3: dict(sections=6, teaching=7, problems=6, figures=6, eq_groups=5, eq_items=18, viva=12,
            hours=9, weightage=20, marks=14, co="CO3"),
    4: dict(sections=6, teaching=9, problems=6, figures=9, eq_groups=5, eq_items=18, viva=12,
            hours=11, weightage=24, marks=17, co="CO4"),
    5: dict(sections=7, teaching=6, problems=6, figures=6, eq_groups=5, eq_items=16, viva=12,
            hours=11, weightage=24, marks=17, co="CO5"),
}


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


def balanced(html):
    stack = []
    for m in TAG_RE.finditer(html):
        tag, selfclose = m.group(1).lower(), m.group(2) == "/"
        if tag in VOID or selfclose:
            continue
        if m.group(0).startswith("</"):
            if not stack or stack[-1] != tag:
                return f"stray </{tag}>"
            stack.pop()
        else:
            stack.append(tag)
    return None if not stack else f"unclosed {stack}"


def unit_suite(number, expect=None):
    expect = expect or EXPECT[number]
    unit = json.loads((SUBJ_DIR / f"unit{number}.json").read_text(encoding="utf-8"))
    subj = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
    spec = next(u for u in subj["units"] if u["no"] == number)
    nodes = text_nodes(unit)
    cards = [it for s in unit["notes"] for it in s["items"]]
    teaching = [it for s in unit["notes"][:-1] for it in s["items"]]
    problems = unit["notes"][-1]["items"]

    class Suite(unittest.TestCase):
        def test_01_identity(self):
            self.assertEqual(unit["subject"], "DI05005031")
            self.assertEqual(unit["unit"], number)
            self.assertEqual(unit["format"], "notes")
            self.assertTrue(unit["official"])
            for key in ("notes", "diagrams", "equations", "viva", "exam_questions", "sources"):
                self.assertIn(key, unit)
            self.assertEqual(unit["course_outcomes"], [expect["co"]])

        def test_02_syllabus_numbers(self):
            self.assertEqual(unit["title"], spec["title"])
            self.assertEqual((unit["hours"], unit["weightage"], unit["theory_marks"]),
                             (expect["hours"], expect["weightage"], expect["marks"]))
            self.assertEqual((spec["hours"], spec["weightage"]), (expect["hours"],
                                                                  expect["weightage"]))

        def test_03_bilingual(self):
            self.assertEqual(unit["languages"], ["en", "gu"])
            self.assertTrue(nodes)
            for n in nodes:
                self.assertTrue(n["en"].strip(), f"empty en: {n}")
                self.assertTrue(n["gu"].strip(), f"missing gu for {n['en'][:50]!r}")
                self.assertFalse(GUJARATI.search(n["en"]), f"Gujarati in en: {n['en'][:60]!r}")
                if len(n["gu"]) >= 20:
                    self.assertTrue(GUJARATI.search(n["gu"]),
                                    f"gu is not Gujarati: {n['gu'][:60]!r}")

        def test_04_no_filler(self):
            for n in nodes:
                low = (n["en"] + " " + n["gu"]).lower()
                for bad in FILLER:
                    self.assertNotIn(bad, low, f"filler '{bad}' in {n['en'][:50]!r}")

        def test_05_counts(self):
            self.assertEqual(len(unit["notes"]), expect["sections"])
            self.assertEqual(len(teaching), expect["teaching"])
            self.assertEqual(len(problems), expect["problems"])
            self.assertEqual(unit["lesson_count"], len(cards))
            self.assertEqual(unit["answered_practice_count"], len(problems))
            for sec in unit["notes"]:
                self.assertTrue(sec["title"]["en"] and sec["title"]["gu"])

        def test_06_figures(self):
            listed = {d["id"] for d in unit["diagrams"]}
            self.assertEqual(len(listed), expect["figures"])
            referenced = {it["diagram"] for it in cards if it.get("diagram")}
            self.assertEqual(listed, referenced,
                             "every figure must be shown by a card, and every card figure must exist")
            problems_found = []
            for d in unit["diagrams"]:
                path = DIAG_DIR / Path(d["file"]).name
                self.assertTrue(path.is_file(), f"missing {path}")
                self.assertTrue(d["title"]["gu"].strip())
                self.assertTrue(d["caption"]["gu"].strip())
                audit_svg(path, problems_found)
            self.assertEqual(problems_found, [])

        def test_07_svg_canvas(self):
            for d in unit["diagrams"]:
                raw = (DIAG_DIR / Path(d["file"]).name).read_text(encoding="utf-8")
                root = ET.fromstring(raw)
                vb = (root.get("viewBox") or "").split()
                self.assertEqual(len(vb), 4)
                self.assertAlmostEqual(float(vb[2]), 360, delta=0.01)
                for bad in ("<image", "foreignObject", "javascript:"):
                    self.assertNotIn(bad, raw)

        def test_08_formulas(self):
            self.assertEqual(len(unit["equations"]), expect["eq_groups"])
            total = 0
            for group in unit["equations"]:
                self.assertTrue(group["title"]["gu"].strip())
                for item in group["items"]:
                    total += 1
                    self.assertGreaterEqual(len(item["f"]), 4)
                    self.assertRegex(item["f"], r"[=:~]|->", f"formula looks empty: {item['f']!r}")
                    self.assertTrue(item["name"]["gu"].strip())
                    self.assertTrue(item["terms"]["gu"].strip())
            self.assertEqual(total, expect["eq_items"])

        def test_09_viva(self):
            total = sum(len(g["items"]) for g in unit["viva"])
            self.assertEqual(total, expect["viva"])
            for group in unit["viva"]:
                self.assertTrue(group["title"]["gu"].strip())
                for item in group["items"]:
                    self.assertGreater(len(strip_html(item["q"]["en"])), 15)
                    self.assertGreater(len(strip_html(item["a"]["en"])), 60)
                    self.assertGreater(len(strip_html(item["a"]["gu"])), 40)

        def test_10_exam_questions(self):
            self.assertEqual(len(unit["exam_questions"]), expect["problems"])
            marks = 0
            for q in unit["exam_questions"]:
                self.assertTrue(q["q"]["en"].strip() and q["q"]["gu"].strip())
                self.assertGreaterEqual(q["marks"], 4)
                marks += q["marks"]
            self.assertLessEqual(marks, 45, "suggested marks far above a revision set")

        def test_11_html(self):
            for it in cards:
                for lang in ("en", "gu"):
                    html = it["body"][lang]
                    self.assertNotIn("{'en'", html)
                    self.assertNotIn('{"en"', html)
                    for bad in ("<script", "<style", "<img", "javascript:"):
                        self.assertNotIn(bad, html)
                    problem = balanced(html)
                    self.assertIsNone(problem, f"{problem} in {lang} of {it['h']['en'][:40]}")
                    self.assertGreater(len(strip_html(html)), 120)

        def test_12_derivations(self):
            for it in teaching:
                self.assertIn('class="math"', it["body"]["en"],
                              f"card without a derivation: {it['h']['en'][:50]}")
                self.assertIn("=", it["body"]["en"])

        def test_13_numericals_are_worked(self):
            for p in problems:
                en = strip_html(p["body"]["en"])
                gu = strip_html(p["body"]["gu"])
                self.assertGreater(len(en), 300)
                self.assertGreater(len(gu), 250)
                self.assertIn("=", p["body"]["en"])

        def test_14_sources_and_note(self):
            self.assertGreaterEqual(len(unit["sources"]), 3)
            for s in unit["sources"]:
                self.assertTrue(s["url"].startswith("https://"))
            self.assertIn("150", unit["assessment_note"]["en"])
            self.assertIn("150", unit["assessment_note"]["gu"])
            self.assertIn("not official", unit["question_provenance"])

        def test_15_subject(self):
            self.assertEqual(subj["code"], "DI05005031")
            self.assertEqual(subj["languages"], ["en", "gu"])
            self.assertEqual(subj["exam"]["total"], 150)
            self.assertEqual(sum(subj["theory_marks_by_unit"].values()), 70)
            self.assertEqual(len(subj["official_practicals"]), 15)
            self.assertEqual(spec["file"], f"unit{number}.json")

    Suite.__name__ = f"CRTUnit{number}"
    Suite.__qualname__ = f"CRTUnit{number}"
    return Suite
