"""Validation for Engineering Graphics (DI01000111) Unit 2 - Engineering Curves.

Run from the repo root:  python3 -m unittest tools.test_DI01000111_u2 -v
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

UNIT = json.loads((SUBJ_DIR / "unit2.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
SPEC = next(u for u in SUBJ["units"] if u["no"] == 2)

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


class EngineeringGraphicsUnit2(unittest.TestCase):
    def test_01_unit_matches_the_syllabus(self):
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (2, 5, 20))
        self.assertEqual((SPEC["hours"], SPEC["weightage"], SPEC["theory_marks"]), (5, 20, 14))
        self.assertEqual(UNIT["title"]["en"], "Engineering Curves")
        self.assertEqual(SPEC["file"], "unit2.json")
        self.assertEqual(UNIT["course_outcomes"], ["CO2"])
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "viva", "exam"])
        self.assertEqual(UNIT["languages"], ["en"])
        self.assertEqual(UNIT["practical_numbers"], [2])

    def test_02_both_syllabus_clauses_and_all_five_topics_are_taught(self):
        tagged = {it.get("syllabus_item") for s in UNIT["notes"][:-1] for it in s["items"]}
        self.assertEqual(tagged, {"2.1", "2.2"})
        text = " ".join(strip_html(it["body"]["en"]).lower() for it in TEACHING)
        for topic in ("conic", "ellipse", "parabola", "hyperbola", "cycloid",
                      "involute", "spiral", "tangent", "normal"):
            self.assertIn(topic, text, f"missing topic: {topic}")

    def test_03_the_unit_is_english_only(self):
        self.assertEqual(SUBJ["languages"], ["en"])
        raw = (SUBJ_DIR / "unit2.json").read_text(encoding="utf-8")
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
        self.assertGreater(len(NODES), 90)

    def test_04_no_empty_or_duplicated_text_nodes(self):
        for n in NODES:
            self.assertTrue(n["en"].strip(), "empty text node")
        long_prose = [n["en"] for n in NODES if len(n["en"]) > 200]
        self.assertEqual(len(long_prose), len(set(long_prose)),
                         "a paragraph is repeated word for word")

    def test_05_cards_are_written_as_constructions(self):
        self.assertEqual(len(TEACHING), 7)
        for it in TEACHING:
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<h4>"), 2, f"thin card: {it['h']['en']}")
            self.assertGreaterEqual(len(strip_html(body)), 800, f"short card: {it['h']['en']}")
            self.assertIn("<ol>", body, f"no numbered construction: {it['h']['en']}")
            self.assertGreaterEqual(body.count("<li>"), 5, f"fewer than five steps: {it['h']['en']}")
            self.assertTrue(it.get("diagram"), f"no figure: {it['h']['en']}")
            assert_balanced(self, body, it["h"]["en"])
            self.assertFalse([w for w in FILLER if w in body.lower()], f"filler in {it['h']['en']}")

    def test_06_the_construction_words_of_every_curve_are_present(self):
        text = " ".join(strip_html(it["body"]["en"]).lower() for it in TEACHING)
        for phrase in ("focus", "directrix", "eccentricity", "locus", "major axis", "minor axis",
                       "concentric", "ordinate", "asymptote", "rectangular hyperbola",
                       "rolling", "base line", "involute", "pitch", "french curve",
                       "tangent", "normal", "instantaneous centre"):
            self.assertIn(phrase, text, f"missing: {phrase}")

    def test_07_every_diagram_exists_and_is_linked(self):
        listed = {d["id"] for d in UNIT["diagrams"]}
        self.assertEqual(len(listed), 7)
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

    def test_08_diagram_labels_are_measured(self):
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

    def test_09_solved_problems_are_step_by_step(self):
        self.assertEqual(len(PROBLEMS), len(UNIT["exam_questions"]))
        self.assertGreaterEqual(len(PROBLEMS), 7)
        for i, it in enumerate(PROBLEMS, 1):
            self.assertTrue(it["h"]["en"].startswith(f"Problem {i}."), it["h"]["en"])
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<li>"), 4, it["h"]["en"])
            self.assertIn("<h4>", body, it["h"]["en"])
            self.assertGreaterEqual(len(strip_html(body)), 700, it["h"]["en"])
            assert_balanced(self, body, it["h"]["en"])
        self.assertEqual(UNIT["answered_practice_count"], len(PROBLEMS))

    def test_10_the_eccentricities_and_axes_are_right(self):
        text = " ".join(strip_html(it["body"]["en"]) for it in PROBLEMS)
        # ellipse 100 x 60: c = sqrt(50^2 - 30^2) = 40, foci 80 apart, e = 0.8, focal sum 100
        self.assertAlmostEqual(math.sqrt(50 ** 2 - 30 ** 2), 40, places=6)
        self.assertAlmostEqual(40 / 50, 0.8, places=6)
        self.assertEqual(2 * 40, 80)
        self.assertEqual(2 * 50, 100)
        self.assertIn("0.8", text)
        self.assertIn("80 mm", text)
        # ellipse from a = 50 and c = 30: b = 40, minor axis 80
        self.assertAlmostEqual(math.sqrt(2500 - 900), 40, places=6)
        self.assertIn("minor axis is 80 mm", text)
        # parabola base 100, height 60: 4a = 41.67, a = 10.4, h(25) = 45
        self.assertAlmostEqual(100 ** 2 / (4 * 60), 41.67, places=2)
        self.assertIn("41.7", text)
        self.assertIn("10.4", text)
        self.assertAlmostEqual(60 * (1 - (25 / 50) ** 2), 45, places=6)
        self.assertAlmostEqual(60 * (1 - (10 / 50) ** 2), 57.6, places=6)
        self.assertAlmostEqual(60 * (1 - (30 / 50) ** 2), 38.4, places=6)
        # rectangular hyperbola through (40, 30)
        self.assertEqual(40 * 30, 1200)
        self.assertEqual(60 * 20, 1200)
        self.assertIn("1200", text)

    def test_11_the_curve_lengths_are_right(self):
        text = " ".join(strip_html(it["body"]["en"]) for it in PROBLEMS)
        # cycloid r = 25
        self.assertAlmostEqual(2 * math.pi * 25, 157.08, places=2)
        self.assertAlmostEqual(2 * math.pi * 25 / 12, 13.09, places=2)
        self.assertIn("157.1", text)
        self.assertIn("13.1", text)
        self.assertEqual(2 * 25, 50)
        # involute r = 20 over twelve steps
        self.assertAlmostEqual(2 * math.pi * 20, 125.66, places=2)
        self.assertAlmostEqual(2 * math.pi * 20 / 12, 10.47, places=2)
        self.assertIn("125.7", text)
        self.assertIn("10.5", text)
        # spiral R = 60 over 1.5 turns: pitch 40, eighteen rays of 3.33 mm
        self.assertAlmostEqual(60 / 1.5, 40, places=6)
        self.assertAlmostEqual(60 / 18, 3.33, places=2)
        self.assertIn("pitch", text.lower())
        self.assertIn("40 mm", text)

    def test_12_formulae_and_viva_are_complete(self):
        names = [i["name"]["en"] for g in UNIT["equations"] for i in g["items"]]
        self.assertGreaterEqual(len(names), 12)
        for wanted in ("Eccentricity", "Ellipse: foci and eccentricity", "Parabola",
                       "Rectangular hyperbola", "Cycloid", "Epicycloid and hypocycloid",
                       "Involute of a circle", "Archimedean spiral"):
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
        self.assertEqual(SUBJ["units"][1]["title"]["en"], UNIT["title"]["en"])
        self.assertEqual(SUBJ["units"][1]["file"], "unit2.json")
        self.assertEqual(UNIT["official"], True)
        self.assertTrue(UNIT["question_marks_are_suggested"])
        self.assertIn("not official", UNIT["question_provenance"].lower())
        self.assertTrue(UNIT["sources"])
        for s in UNIT["sources"]:
            self.assertTrue(s["url"].startswith("http"), s)
        self.assertEqual(UNIT["lesson_count"], len(TEACHING))

    def test_14_preview_and_shelf_page_exist(self):
        for rel in ("preview/workshop/DI01000111_u2.html", "preview/DI01000111_unit2_preview.html"):
            self.assertTrue((ROOT / rel).is_file(), rel)
        html = (ROOT / "preview/workshop/DI01000111_u2.html").read_text(encoding="utf-8")
        self.assertIn("Engineering Graphics", html)
        self.assertNotIn("\u0a80", html)
        self.assertEqual(UNIT["notes"][0]["title"]["en"][0], "1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
