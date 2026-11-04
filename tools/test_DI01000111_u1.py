"""Validation for Engineering Graphics (DI01000111) Unit 1 - English only.

Run from the repo root:  python3 -m unittest tools.test_DI01000111_u1 -v
"""
import json
import math
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000111 import SUBJ_DIR, DIAG_DIR, SUBJECT  # noqa: E402
from notes_workshop import audit_svg, text_width  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit1.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
SPEC = next(u for u in SUBJ["units"] if u["no"] == 1)

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")
GUJARATI = re.compile(r"[\u0a80-\u0aff]")
FILLER = ("lorem", "todo", "tbd", "xxx", "placeholder", "[insert", "coming soon")


def strip_html(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def nodes(obj, out=None):
    out = [] if out is None else out
    if isinstance(obj, dict):
        if "en" in obj and isinstance(obj["en"], str):
            out.append(obj)
        else:
            for v in obj.values():
                nodes(v, out)
    elif isinstance(obj, list):
        for v in obj:
            nodes(v, out)
    return out


NODES = nodes(UNIT)
CARDS = [it for s in UNIT["notes"] for it in s["items"]]
TEACHING = [it for s in UNIT["notes"][:-1] for it in s["items"]]
PROBLEMS = UNIT["notes"][-1]["items"]


def assert_balanced(tc, html, where):
    stack = []
    for m in TAG_RE.finditer(html):
        tag, selfclose = m.group(1).lower(), m.group(2) == "/"
        if tag in VOID or selfclose:
            continue
        if m.group(0).startswith("</"):
            tc.assertTrue(stack and stack[-1] == tag, f"{where}: stray </{tag}>")
            if stack:
                stack.pop()
        else:
            stack.append(tag)
    tc.assertFalse(stack, f"{where}: unclosed {stack}")


class EngineeringGraphicsUnit1(unittest.TestCase):
    def test_01_unit_matches_the_syllabus(self):
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (1, 4, 10))
        self.assertEqual((SPEC["hours"], SPEC["weightage"], SPEC["theory_marks"]), (4, 10, 7))
        self.assertEqual(UNIT["title"]["en"], "Introduction to Engineering Graphics")
        self.assertEqual(SPEC["file"], "unit1.json")
        self.assertEqual(UNIT["course_outcomes"], ["CO1"])
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "viva", "exam"])
        self.assertEqual(UNIT["languages"], ["en"])

    def test_02_subject_scheme_is_copied_from_the_pdf(self):
        self.assertEqual(SUBJ["code"], "DI01000111")
        self.assertEqual(SUBJ["name"]["en"], "Engineering Graphics")
        self.assertEqual(SUBJ["semester"], 1)
        self.assertEqual(SUBJ["category"], "Engineering Science (ESC-01)")
        self.assertEqual(SUBJ["teaching"], {"lecture": 2, "tutorial": 0, "practical": 2})
        self.assertEqual(SUBJ["exam"], {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20,
                                        "practical_ese": 30, "total": 150, "credits": 3})
        self.assertEqual(SUBJ["total_hours"], 30)
        self.assertEqual(len(SUBJ["units"]), 6)
        self.assertEqual(sum(u["hours"] for u in SUBJ["units"]), 30)
        self.assertEqual(sum(u["weightage"] for u in SUBJ["units"]), 100)
        self.assertEqual(sum(u["theory_marks"] for u in SUBJ["units"]), 70)
        self.assertEqual([u["theory_marks"] for u in SUBJ["units"]], [7, 14, 14, 7, 14, 14])
        self.assertEqual(len(SUBJ["course_outcomes"]), 5)
        self.assertEqual(len(SUBJ["official_practicals"]), 7)
        self.assertEqual(SUBJ["source_pdf_sha256"],
                         "c88b56fd4567b334c37c0b9314a04d7bfe79e9331c97444dd1136025a25c170a")

    def test_03_the_unit_is_english_only(self):
        self.assertEqual(SUBJ["languages"], ["en"])
        with open(SUBJ_DIR / "unit1.json", encoding="utf-8") as f:
            raw = f.read()
        self.assertFalse(GUJARATI.search(raw), "Gujarati script found in an English-only subject")

        def no_gu(obj):
            if isinstance(obj, dict):
                self.assertNotIn("gu", obj, f"a 'gu' key survived: {list(obj)[:4]}")
                for v in obj.values():
                    no_gu(v)
            elif isinstance(obj, list):
                for v in obj:
                    no_gu(v)
        no_gu(UNIT)
        self.assertGreater(len(NODES), 80)

    def test_04_no_empty_or_duplicated_text_nodes(self):
        for n in NODES:
            self.assertTrue(n["en"].strip(), "empty text node")
        long_prose = [n["en"] for n in NODES if len(n["en"]) > 200]
        self.assertEqual(len(long_prose), len(set(long_prose)), "a paragraph is repeated word for word")

    def test_05_every_gtu_clause_is_taught(self):
        tagged = {it.get("syllabus_item") for s in UNIT["notes"][:-1] for it in s["items"]}
        self.assertEqual(tagged, {"1.1", "1.2", "1.3"})
        for clause in ("1.1", "1.2", "1.3"):
            self.assertGreaterEqual(len([1 for it in TEACHING if it.get("syllabus_item") == clause]),
                                    1)

    def test_06_cards_are_written_as_constructions(self):
        self.assertGreaterEqual(len(TEACHING), 6)
        for it in TEACHING:
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<h4>"), 2, f"thin card: {it['h']['en']}")
            self.assertGreaterEqual(len(strip_html(body)), 700, f"short card: {it['h']['en']}")
            self.assertIn("<ol>", body, f"no numbered construction: {it['h']['en']}")
            self.assertGreaterEqual(body.count("<li>"), 4, f"fewer than four steps: {it['h']['en']}")
            assert_balanced(self, body, it["h"]["en"])
            self.assertFalse([w for w in FILLER if w in body.lower()], f"filler in {it['h']['en']}")

    def test_07_the_required_ideas_are_present(self):
        text = " ".join(strip_html(it["body"]["en"]).lower() for it in TEACHING)
        for phrase in ("bis sp 46", "title block", "filing margin", "representative fraction",
                       "extension line", "arrowhead", "datum", "plain scale", "diagonal scale",
                       "regular polygon", "central angle", "across flats", "across corners",
                       "general method", "0.414", "1.732"):
            self.assertIn(phrase, text, f"missing: {phrase}")  # noqa: E501

    def test_08_every_diagram_exists_and_is_linked(self):
        listed = {d["id"] for d in UNIT["diagrams"]}
        self.assertEqual(len(listed), 6)
        linked = {it["diagram"] for it in CARDS if it.get("diagram")}
        self.assertEqual(listed, linked, "a diagram is listed but not shown in a card")
        for d in UNIT["diagrams"]:
            self.assertTrue(d["title"]["en"].strip())
            self.assertTrue(d["caption"]["en"].strip())
            path = DIAG_DIR / f"{d['id']}.svg"
            self.assertTrue(path.is_file(), f"missing SVG {path.name}")
            problems = []
            audit_svg(path, problems)
            self.assertFalse(problems, problems)
            raw = path.read_text(encoding="utf-8")
            self.assertIn('viewBox="0 0 360', raw)
            for bad in ("<script", "<style", "<image", "href="):
                self.assertNotIn(bad, raw)

    def test_09_diagram_labels_are_measured(self):
        for d in UNIT["diagrams"]:
            raw = (DIAG_DIR / f"{d['id']}.svg").read_text(encoding="utf-8")
            self.assertLess(len(d["title"]["en"]), 52, "title longer than the canvas allows")
            for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*font-size="([\d.]+)"'
                                 r'(?:[^>]*font-weight="([^"]+))?"[^>]*>([^<]+)</text>', raw):
                x, size, weight, txt = (float(m.group(1)), float(m.group(3)), m.group(4), m.group(5))
                bold = weight in ("bold", "700")
                width = text_width(txt, size, bold)
                anchor = "middle" if 'text-anchor="middle"' in m.group(0) else (
                    "end" if 'text-anchor="end"' in m.group(0) else "start")
                left = x - width / 2 if anchor == "middle" else (x - width if anchor == "end" else x)
                self.assertGreaterEqual(left, 0.5, f"{d['id']}: '{txt}' off the left edge")
                self.assertLessEqual(left + width, 359.5, f"{d['id']}: '{txt}' off the right edge")

    def test_10_solved_problems_are_step_by_step(self):
        self.assertEqual(len(PROBLEMS), len(UNIT["exam_questions"]))
        self.assertGreaterEqual(len(PROBLEMS), 7)
        for i, it in enumerate(PROBLEMS, 1):
            self.assertTrue(it["h"]["en"].startswith(f"Problem {i}."), it["h"]["en"])
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<li>"), 4, it["h"]["en"])
            self.assertIn("<h4>", body, it["h"]["en"])
            self.assertGreaterEqual(len(strip_html(body)), 600, it["h"]["en"])
            assert_balanced(self, body, it["h"]["en"])
        self.assertEqual(UNIT["answered_practice_count"], len(PROBLEMS))

    def test_11_the_numbers_in_the_solutions_are_right(self):
        text = " ".join(strip_html(it["body"]["en"]) for it in PROBLEMS)
        # plain scale: (1/50) x 6000 mm = 120 mm, six metres, 3.7 m = 74 mm
        self.assertAlmostEqual(6000 / 50, 120, places=6)
        self.assertAlmostEqual(3.7 * 20, 74, places=6)
        self.assertIn("120 mm", text)
        self.assertIn("74 mm", text)
        # pentagon of 40 mm side: R = s / (2 sin 36)
        self.assertAlmostEqual(40 / (2 * math.sin(math.radians(36))), 34.03, places=2)
        self.assertIn("34.03", text)
        self.assertAlmostEqual(360 / 5, 72, places=6)
        self.assertAlmostEqual((5 - 2) * 180 / 5, 108, places=6)
        # hexagon AF 60: R = 60 / 1.732, AC = 2 R, side = R
        self.assertAlmostEqual(60 / 1.732, 34.64, places=2)
        self.assertAlmostEqual(2 * 60 / 1.732, 69.28, places=2)
        self.assertIn("34.64", text)
        self.assertIn("69.3", text)
        # octagon in a 60 mm square: side 0.414 a, corner trim 0.293 a
        self.assertAlmostEqual(0.4142 * 60, 24.85, places=2)
        self.assertAlmostEqual(0.293 * 60, 17.58, places=2)
        self.assertIn("24.85", text)
        self.assertIn("17.6", text)
        # heptagon in a 70 mm circle
        self.assertAlmostEqual(70 * math.sin(math.radians(180 / 7)), 30.37, places=2)
        self.assertIn("30.37", text)
        self.assertAlmostEqual(360 / 7, 51.43, places=2)

    def test_12_formulae_and_viva_are_complete(self):
        names = [i["name"]["en"] for g in UNIT["equations"] for i in g["items"]]
        self.assertGreaterEqual(len(names), 12)
        for wanted in ("Representative fraction", "Length of the scale", "Central angle",
                       "Side from the diameter", "Interior angle", "Pentagon circumradius",
                       "Hexagon, across flats and corners", "Octagon in a square", "Line thickness",
                       "Arrowhead proportion"):
            self.assertIn(wanted, names)
        for g in UNIT["equations"]:
            self.assertTrue(g["title"]["en"].strip())
            for i in g["items"]:
                self.assertTrue(i["f"].strip())
                self.assertGreater(len(strip_html(i["terms"]["en"])), 30, i["name"]["en"])
        viva = [i for g in UNIT["viva"] for i in g["items"]]
        self.assertGreaterEqual(len(viva), 14)
        for v in viva:
            self.assertGreater(len(strip_html(v["a"]["en"])), 120, v["q"]["en"])

    def test_13_the_unit_is_registered_and_marked_available(self):
        self.assertEqual(SUBJ["units"][0]["title"]["en"], UNIT["title"]["en"])
        self.assertEqual(SUBJ["units"][0]["file"], "unit1.json")
        self.assertFalse([u for u in SUBJ["units"] if u["no"] == 1 and u["file"] != "unit1.json"])
        self.assertEqual(UNIT["official"], True)
        self.assertEqual(UNIT["practical_numbers"], [1])
        self.assertTrue(UNIT["question_marks_are_suggested"])
        self.assertIn("not official", UNIT["question_provenance"].lower())
        self.assertTrue(UNIT["sources"])
        for s in UNIT["sources"]:
            self.assertTrue(s["url"].startswith("http"), s)
        self.assertEqual(UNIT["lesson_count"], len(TEACHING))

    def test_14_preview_and_shelf_page_exist(self):
        self.assertTrue((ROOT / "preview/workshop/DI01000111_u1.html").is_file())
        html = (ROOT / "preview/workshop/DI01000111_u1.html").read_text(encoding="utf-8")
        self.assertIn("Engineering Graphics", html)
        self.assertNotIn("\u0a80", html)


if __name__ == "__main__":
    unittest.main(verbosity=2)
