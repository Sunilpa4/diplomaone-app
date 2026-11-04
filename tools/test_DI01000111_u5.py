"""Validation for Engineering Graphics (DI01000111) Unit 5 - Orthographic Projections.

Run from the repo root:  python3 -m unittest tools.test_DI01000111_u5 -v
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

UNIT = json.loads((SUBJ_DIR / "unit5.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
SPEC = next(u for u in SUBJ["units"] if u["no"] == 5)

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


class EngineeringGraphicsUnit5(unittest.TestCase):
    def test_01_unit_matches_the_syllabus(self):
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (5, 6, 20))
        self.assertEqual((SPEC["hours"], SPEC["weightage"], SPEC["theory_marks"]), (6, 20, 14))
        self.assertEqual(UNIT["title"]["en"], "Orthographic Projections")
        self.assertEqual(SPEC["file"], "unit5.json")
        self.assertEqual(UNIT["course_outcomes"], ["CO4"])
        self.assertEqual(UNIT["languages"], ["en"])
        self.assertEqual(UNIT["practical_numbers"], [5])

    def test_02_all_three_clauses_are_taught(self):
        tagged = {it.get("syllabus_item") for s in UNIT["notes"][:-1] for it in s["items"]}
        self.assertEqual(tagged, {"5.1", "5.2", "5.3"})
        text = " ".join(strip_html(it["body"]["en"]).lower() for it in TEACHING)
        for topic in ("first-angle", "front view", "top view", "side view", "hidden", "centre "
                      "line", "pictorial", "free-hand", "semicircle", "pentagon", "hexagon"):
            self.assertIn(topic, text, f"missing topic: {topic}")

    def test_03_the_unit_is_english_only(self):
        self.assertEqual(SUBJ["languages"], ["en"])
        raw = (SUBJ_DIR / "unit5.json").read_text(encoding="utf-8")
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
        self.assertEqual(len(long_prose), len(set(long_prose)),
                         "a paragraph is repeated word for word")

    def test_05_cards_are_written_as_constructions(self):
        self.assertEqual(len(TEACHING), 6)
        for it in TEACHING:
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<h4>"), 2, f"thin card: {it['h']['en']}")
            self.assertGreaterEqual(len(strip_html(body)), 900, f"short card: {it['h']['en']}")
            self.assertIn("<ol>", body, f"no numbered construction: {it['h']['en']}")
            self.assertGreaterEqual(body.count("<li>"), 4, f"fewer than four steps: {it['h']['en']}")
            self.assertTrue(it.get("diagram"), f"no figure: {it['h']['en']}")
            assert_balanced(self, body, it["h"]["en"])
            self.assertFalse([w for w in FILLER if w in body.lower()], f"filler in {it['h']['en']}")

    def test_06_every_diagram_exists_and_is_linked(self):
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

    def test_07_diagram_labels_are_measured(self):
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

    def test_08_solved_problems_are_step_by_step(self):
        self.assertEqual(len(PROBLEMS), len(UNIT["exam_questions"]))
        self.assertGreaterEqual(len(PROBLEMS), 6)
        for i, it in enumerate(PROBLEMS, 1):
            self.assertTrue(it["h"]["en"].startswith(f"Problem {i}."), it["h"]["en"])
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<li>"), 4, it["h"]["en"])
            self.assertIn("<h4>", body, it["h"]["en"])
            self.assertGreaterEqual(len(strip_html(body)), 600, it["h"]["en"])
            assert_balanced(self, body, it["h"]["en"])
        self.assertEqual(UNIT["answered_practice_count"], len(PROBLEMS))

    def test_09_the_view_arithmetic_is_right(self):
        text = " ".join(strip_html(it["body"]["en"]) for it in PROBLEMS)
        # pyramid: slant edge from half diagonal
        slant = math.sqrt(50 ** 2 + 20 ** 2 + 20 ** 2)
        self.assertAlmostEqual(slant, 57.45, places=2)
        self.assertIn("57.4", text)
        # hexagon and pentagon proportions used in the sketch card
        self.assertAlmostEqual(math.sqrt(3), 1.732, places=3)
        self.assertAlmostEqual(2 * math.cos(math.radians(18)), 1.902, places=3)
        self.assertAlmostEqual(2 * math.sin(math.radians(36)), 1.176, places=3)
        self.assertAlmostEqual(0.866 * 50, 43.3, places=1)
        teaching = " ".join(strip_html(it["body"]["en"]) for it in TEACHING)
        for token in ("1.732", "1.176", "0.866", "108"):
            self.assertIn(token, teaching, f"missing {token}")

    def test_10_first_angle_rules_are_stated(self):
        text = " ".join(strip_html(it["body"]["en"]) for it in TEACHING).lower()
        for phrase in ("below", "to the right", "height", "width", "depth", "dashed", "centre line",
                       "mitre"):
            self.assertIn(phrase, text, f"missing: {phrase}")
        self.assertIn("first-angle", text)

    def test_11_formulae_and_viva_are_complete(self):
        names = [i["name"]["en"] for g in UNIT["equations"] for i in g["items"]]
        self.assertGreaterEqual(len(names), 8)
        for wanted in ("First angle layout", "Shared dimensions", "Depth transfer",
                       "Cylinder standing", "Cone standing", "Square pyramid"):
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

    def test_12_the_unit_is_registered_and_marked_available(self):
        self.assertEqual(SUBJ["units"][4]["title"]["en"], UNIT["title"]["en"])
        self.assertEqual(SUBJ["units"][4]["file"], "unit5.json")
        self.assertEqual(UNIT["official"], True)
        self.assertTrue(UNIT["question_marks_are_suggested"])
        self.assertIn("not official", UNIT["question_provenance"].lower())
        self.assertTrue(UNIT["sources"])
        for s in UNIT["sources"]:
            self.assertTrue(s["url"].startswith("http"), s)
        self.assertEqual(UNIT["lesson_count"], len(TEACHING))

    def test_13_preview_and_shelf_page_exist(self):
        for rel in ("preview/workshop/DI01000111_u5.html", "preview/DI01000111_unit5_preview.html"):
            self.assertTrue((ROOT / rel).is_file(), rel)
        html = (ROOT / "preview/workshop/DI01000111_u5.html").read_text(encoding="utf-8")
        self.assertIn("Engineering Graphics", html)
        self.assertNotIn("\u0a80", html)


if __name__ == "__main__":
    unittest.main(verbosity=2)
