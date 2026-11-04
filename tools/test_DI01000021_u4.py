"""Validation for Mathematics-I (DI01000021) Unit 4 "Coordinate Geometry".

Run from the repo root:  python3 -m unittest tools.test_DI01000021_u4 -v
"""
import hashlib
import json
import math
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

from subject_DI01000021 import SUBJ_DIR, DIAG_DIR, TABS  # noqa: E402
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
ANS = {n["id"]: strip_html(n["a"]["en"]).replace("−", "-") for n in UNIT["numericals"]}


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


class MathUnit4(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 4)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (4, 8, 20))
        self.assertEqual((spec["hours"], spec["weightage"]), (8, 20))
        self.assertEqual(UNIT["title"]["en"], "Coordinate Geometry")
        self.assertEqual(spec["file"], "unit4.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["4"], 14)
        self.assertEqual(UNIT["tabs"], TABS)

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 6)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"]), 28)
        self.assertEqual(len(UNIT["diagrams"]), 7)
        self.assertEqual(len(UNIT["numericals"]), 26)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 20)
        self.assertEqual(len(UNIT["exam_questions"]), 15)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 14)
        self.assertEqual(UNIT["lesson_count"], 13)
        self.assertEqual(UNIT["answered_practice_count"], 15)

    def test_03_syllabus_coverage(self):
        for word in ["straight line", "slope", "intercept", "general form", "parallel", "perpendicular",
                     "angle between", "distance", "circle", "centre", "radius", "tangent", "normal"]:
            self.assertTrue(word in TEXT, f"unit 4 misses: {word}")
        for topic in ["rise", "two-point", "acute", "centre-radius form", "length of a tangent"]:
            self.assertIn(topic, TEXT)

    def test_04_english_only(self):
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

        walk(UNIT)
        self.assertEqual(UNIT["languages"], ["en"])

    def test_05_slope_and_line_forms(self):
        # slope from two points
        m = (11 - 3) / (6 - 2)
        self.assertEqual(m, 2)
        self.assertIn("m = 2", ANS["cg1n1"])
        # two-point form through (1, 2) and (3, 8)
        self.assertEqual((8 - 2) / (3 - 1), 3)
        self.assertIn("3x - y - 1 = 0", ANS["cg1n2"])
        # perpendicular slope
        self.assertAlmostEqual(-1 / (4 / 3), -3 / 4)
        self.assertIn("-3/4", ANS["cg1n3"])
        # point-slope with a fractional slope
        self.assertIn("x - 2y + 8 = 0", ANS["cg1n4"])
        # intercept form: x/3 + y/(-4) = 1  ->  4x - 3y = 12
        self.assertEqual(3 * 4, 12)
        self.assertIn("4x - 3y = 12", ANS["cg1n5"])
        # general -> slope-intercept and intercept form
        self.assertIn("y = -(3/4)x + 3", ANS["cg1n6"])
        self.assertIn("x/4 + y/3 = 1", ANS["cg1n6"])
        # parallel family keeps the coefficients, changes the constant
        self.assertIn("3x - 4y - 18 = 0", ANS["cg1n7"])
        # perpendicular family swaps and flips
        self.assertIn("3x - 2y + 1 = 0", ANS["cg1n8"])

    def test_06_parallel_perpendicular_and_angle(self):
        # parallel: 2x + 3y = 5 and 4x + 6y = 11
        self.assertEqual((2 / 4, 3 / 6), (0.5, 0.5))
        self.assertNotAlmostEqual(5 / 11, 0.5)
        self.assertIn("parallel", ANS["cg1n11"].lower())
        # perpendicular test in general form
        self.assertEqual(3 * 4 + 4 * (-3), 0)
        self.assertIn("perpendicular", ANS["cg1n12"].lower())
        # tan(theta) = |(m1 - m2)/(1 + m1 m2)| for m = 2, -1
        tan_t = abs((2 - (-1)) / (1 + 2 * (-1)))
        self.assertEqual(tan_t, 3)
        self.assertAlmostEqual(math.degrees(math.atan(tan_t)), 71.57, places=2)
        self.assertIn("71.57", ANS["cg1n9"])
        # 3x - y + 4 = 0 (m = 3) with x + 2y - 5 = 0 (m = -1/2)
        m1, m2 = 3.0, -0.5
        tan_u = abs((m1 - m2) / (1 + m1 * m2))
        self.assertAlmostEqual(tan_u, 7.0, places=12)
        self.assertAlmostEqual(math.degrees(math.atan(tan_u)), 81.87, places=2)
        self.assertIn("81.87", ANS["cg1n10"])

    def test_07_distances(self):
        # point to line
        d = abs(3 * 2 + 4 * 3 - 5) / math.hypot(3, 4)
        self.assertAlmostEqual(d, 2.6, places=12)
        self.assertIn("2.6", ANS["cg1n22"])
        # between parallel lines
        d2 = abs(5 - 15) / math.hypot(3, 4)
        self.assertEqual(d2, 2)
        self.assertIn("2 units", ANS["cg1n23"])

    def test_08_circles(self):
        # centre-radius form and its expansion
        self.assertIn("(x - 2)² + (y + 3)² = 25", ANS["cg1n13"])
        self.assertIn("x² + y² - 4x + 6y - 12 = 0", ANS["cg1n13"])
        # general form -> centre and radius, g = -3, f = 4, c = -11
        g, f, c = -3.0, 4.0, -11.0
        self.assertEqual(((-g), (-f)), (3, -4))
        self.assertEqual(math.sqrt(g * g + f * f - c), 6)
        self.assertIn("Centre (3, -4)", ANS["cg1n14"])
        self.assertIn("radius 6", ANS["cg1n14"])
        # diameter ends
        mid = ((1 + 5) / 2, (2 + 8) / 2)
        self.assertEqual(mid, (3, 5))
        self.assertAlmostEqual(((5 - 1) ** 2 + (8 - 2) ** 2) / 4, 13, places=12)
        self.assertIn("(x - 3)² + (y - 5)² = 13", ANS["cg1n15"])
        # point on a circle fixes k
        k = (12 + 6 - 4 - 9) / 2
        self.assertEqual(k, 2.5)
        self.assertIn("k = 5/2", ANS["cg1n16"])
        # circle through the three axis points of a 3-4-5 right triangle
        self.assertAlmostEqual(math.hypot(2, 1.5), 2.5, places=12)
        self.assertIn("x² + y² - 4x - 3y = 0", ANS["cg1n25"])

    def test_09_tangent_and_normal(self):
        # xx1 + yy1 = a^2
        self.assertIn("3x + 4y = 25", ANS["cg1n17"])
        self.assertIn("2x + 3y = 13", ANS["cg1n18"])
        # slope form of the tangent: y = mx +- a sqrt(1 + m^2)
        off = 5 * math.sqrt(1 + (3 / 4) ** 2)
        self.assertEqual(off, 25 / 4)
        self.assertIn("3x - 4y ± 25 = 0", ANS["cg1n19"])
        # normal to x^2 + y^2 = 25 at (3, 4) passes through the centre
        self.assertEqual(4 * 3 - 3 * 4, 0)
        self.assertIn("4x - 3y = 0", ANS["cg1n20"])
        # length of tangent from (5, 1)
        self.assertEqual(math.sqrt(25 + 1 - 25), 1)
        self.assertIn("1 unit", ANS["cg1n21"])
        # y = mx + c tangent to x^2 + y^2 = 25 with m = 2
        c_abs = 5 * math.sqrt(1 + 4)
        self.assertAlmostEqual(c_abs, math.sqrt(125), places=12)
        self.assertIn("±5√5", ANS["cg1n26"])

    def test_10_mixed_and_practice(self):
        # line parallel to the join of (1, 1) and (4, 5) through (2, 3)
        self.assertEqual((5 - 1) / (4 - 1), 4 / 3)
        self.assertIn("4x - 3y + 1 = 0", ANS["cg1n24"])
        practice = {i + 1: strip_html(it["body"]["en"]).replace("−", "-")
                    for i, it in enumerate(UNIT["notes"][-1]["items"])}
        # practice 1: through (0, 5) and (3, 11)
        self.assertEqual((11 - 5) / (3 - 0), 2)
        self.assertIn("2x - y + 5 = 0", practice[1])
        # practice 2
        self.assertIn("3x + y - 10 = 0", practice[2])
        # practice 3: intercepts -2 and 5
        self.assertIn("5x - 2y + 10 = 0", practice[3])
        # practice 5: perpendicular to 4x - 3y + 7 = 0 through (3, -1)
        self.assertEqual(4 * 3 + (-3) * 4, 0)
        self.assertIn("3x + 4y - 5 = 0", practice[5])
        # practice 6: angle between 2x - y + 3 = 0 (m = 2) and x + 3y - 2 = 0 (m = -1/3)
        tan_p = abs((2 + 1 / 3) / (1 - 2 / 3))
        self.assertAlmostEqual(math.degrees(math.atan(tan_p)), 81.87, places=2)
        self.assertIn("81.87", practice[6])
        # practice 7: distance between 4x + 3y - 9 = 0 and 4x + 3y + 6 = 0
        self.assertEqual(abs(-9 - 6) / math.hypot(4, 3), 3)
        self.assertIn("3 units", practice[7])
        # practice 8: centre and radius
        self.assertIn("(-2, 3)", practice[8].replace("Centre (-2, 3)", "(-2, 3)"))
        self.assertIn("5", practice[8])
        # practice 9: centre (-1, 2) through (3, 5)
        self.assertEqual((3 + 1) ** 2 + (5 - 2) ** 2, 25)
        self.assertIn("x² + y² + 2x - 4y - 20 = 0", practice[9])
        # practice 10 / 11
        self.assertIn("5x + 12y = 169", practice[10])
        self.assertIn("3x + 4y = 0", practice[11])
        # practice 12: tangency of 3x + 4y + k = 0 to x^2 + y^2 = 25
        self.assertEqual(abs(-25) / 5, 5)
        self.assertIn("±25", practice[12])
        # practice 13: tangent length from (7, 1) to x^2 + y^2 - 4x + 2y - 4 = 0
        self.assertEqual(math.sqrt(49 + 1 - 4 * 7 + 2 * 1 - 4), math.sqrt(20))
        self.assertIn("2√5", practice[13])
        # practice 14: centre (2, 0) through (2, 3)
        self.assertIn("(x - 2)² + y² = 9", practice[14])
        self.assertIn("y = 3", practice[14])
        # practice 15
        self.assertIn("3x + 2y - 11 = 0", practice[15])

    def test_11_diagrams_valid_and_referenced(self):
        listed = {d["id"] for d in UNIT["diagrams"]}
        used = {it["diagram"] for s in UNIT["notes"] for it in s["items"] if it.get("diagram")}
        self.assertEqual(listed, used)
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

    def test_12_diagram_text_fits_the_canvas(self):
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

    def test_13_links_resolve_both_ways(self):
        num_ids = {n["id"] for n in UNIT["numericals"]}
        used = {e for s in UNIT["notes"] for it in s["items"] for e in it.get("examples", [])}
        self.assertEqual(used, num_ids, "every numerical should be reachable from a card")

    def test_14_practice_matches_exam_questions(self):
        practice = UNIT["notes"][-1]
        self.assertTrue(practice["title"]["en"].startswith("6."))
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4))
            self.assertGreater(len(item["body"]["en"]), 170, "model answer is too thin")
        self.assertTrue(UNIT["question_marks_are_suggested"])

    def test_15_html_is_balanced_and_clean(self):
        for si, section in enumerate(UNIT["notes"]):
            for ii, item in enumerate(section["items"]):
                body = (item.get("body") or {}).get("en", "")
                assert_balanced(self, body, f"notes {si}/{ii}")
                for bad in ("<script", "<style", "<img", "href="):
                    self.assertNotIn(bad, body)
        for n in UNIT["numericals"]:
            assert_balanced(self, n["a"]["en"], f"numerical {n['id']}")
        for g in UNIT["equations"] + UNIT["viva"]:
            for e in g["items"]:
                assert_balanced(self, (e.get("terms") or e.get("a"))["en"], "equations/viva")

    def test_16_export_carries_the_unit(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=180)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI01000021_u4.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 7)
            subject = json.loads((out / "subjects/DI01000021.json").read_text(encoding="utf-8"))
            self.assertIn(4, subject["available_units"])
            self.assertEqual(subject["available_units"], sorted(subject["available_units"]))
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            branches = catalog["branches"]
            self.assertEqual(sum(1 for b in branches if "DI01000021" in b["semesters"].get("1", [])), len(branches))
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
