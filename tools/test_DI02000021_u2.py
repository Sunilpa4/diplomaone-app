"""Validation for Engineering Mathematics (DI02000021) Unit 2 "Differentiation and its Applications".

Run from the repo root:  python3 -m unittest tools.test_DI02000021_u2 -v
"""
import hashlib
import html
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

from subject_DI02000021 import SUBJ_DIR, DIAG_DIR, TABS  # noqa: E402
from notes_workshop import audit_svg, text_width  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit2.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")


def strip_html(markup):
    return html.unescape(re.sub(r"</?[a-zA-Z][^>]*>", " ", markup))


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
ANS = {n["id"]: re.sub(r"\s+", " ", strip_html(n["a"]["en"])) for n in UNIT["numericals"]}
PRACTICE = {i + 1: re.sub(r"\s+", " ", strip_html(it["body"]["en"]))
            for i, it in enumerate(UNIT["notes"][-1]["items"])}


def d1(f, x, h=1e-6):
    """Five-point first derivative."""
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def d2(f, x, h=1e-4):
    """Second derivative by central differences."""
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


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


class EngineeringMathsUnit2(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 2)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (2, 11, 23))
        self.assertEqual((spec["hours"], spec["weightage"]), (11, 23))
        self.assertEqual(UNIT["title"]["en"], "Differentiation and its Applications")
        self.assertEqual(spec["file"], "unit2.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["2"], 16)
        self.assertEqual(UNIT["tabs"], TABS)
        self.assertEqual(UNIT["course_outcomes"], ["CO2"])

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 8)
        self.assertEqual(UNIT["lesson_count"], 26)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 26)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 16)
        self.assertEqual(len(UNIT["diagrams"]), 6)
        self.assertEqual(len(UNIT["numericals"]), 24)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 17)
        self.assertEqual(len(UNIT["exam_questions"]), 16)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 18)

    def test_03_syllabus_coverage(self):
        for word in ["derivative", "first principles", "product rule", "quotient rule", "chain rule",
                     "implicit", "parametric", "logarithmic differentiation", "second derivative",
                     "velocity", "acceleration", "maxima", "minima", "stationary"]:
            self.assertIn(word, TEXT, f"unit 2 misses: {word}")
        for topic in ["concave", "first principles", "cot x", "kinematics"]:
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

    def test_05_first_principles(self):
        self.assertAlmostEqual(d1(lambda x: x * x, 3), 6, places=4)
        self.assertAlmostEqual(d1(lambda x: math.sqrt(x), 4), 0.25, places=5)
        self.assertIn("2x", ANS["dd1"])
        self.assertIn("1/(2√x)", ANS["dd2"])

    def test_06_working_rules(self):
        poly = lambda x: 3 * x ** 2 - 5 * x + 2
        self.assertAlmostEqual(d1(poly, 2), 7, places=4)
        self.assertIn("6x − 5", ANS["dd3"])
        self.assertIn("7", ANS["dd3"])
        quart = lambda x: x ** 3 + 2 * x ** 2 - 7 * x + 1
        self.assertAlmostEqual(d1(quart, 1.5), 3 * 1.5 ** 2 + 4 * 1.5 - 7, places=4)
        self.assertIn("3x² + 4x − 7", ANS["dd4"])
        # product rule
        f = lambda x: x * x * (3 * x + 5)
        self.assertAlmostEqual(d1(f, 2), 9 * 4 + 10 * 2, places=4)
        self.assertIn("9x² + 10x", ANS["dd5"])
        g = lambda x: (x + 1) * (x * x + 3)
        self.assertAlmostEqual(d1(g, 1.3), 3 * 1.3 ** 2 + 2 * 1.3 + 3, places=4)
        self.assertIn("3x² + 2x + 3", ANS["dd6"])
        # quotient rule
        q = lambda x: (2 * x + 1) / (x - 1)
        self.assertAlmostEqual(d1(q, 2.5), -3 / (1.5 ** 2), places=4)
        self.assertIn("−3/(x − 1)²", ANS["dd7"])
        r = lambda x: x / (x * x + 1)
        self.assertAlmostEqual(d1(r, 0.7), (1 - 0.49) / (1.49 ** 2), places=4)
        self.assertIn("(1 − x²)/(x² + 1)²", ANS["dd8"])

    def test_07_chain_rule(self):
        f = lambda x: (3 * x + 2) ** 5
        self.assertAlmostEqual(d1(f, 0.5), 15 * (3 * 0.5 + 2) ** 4, places=2)
        self.assertIn("15(3x + 2)⁴", ANS["dd9"])
        self.assertAlmostEqual(d1(lambda x: math.sin(5 * x), 0.3), 5 * math.cos(1.5), places=4)
        self.assertIn("5 cos 5x", ANS["dd10"])
        self.assertAlmostEqual(d1(lambda x: math.exp(3 * x), 0.4) / math.exp(1.2), 3, places=4)
        self.assertIn("3e^(3x)", ANS["dd11"])
        self.assertAlmostEqual(d1(lambda x: math.sqrt(x * x + 1), 2), 2 / math.sqrt(5), places=4)
        self.assertIn("x/√(x² + 1)", ANS["dd12"])
        self.assertAlmostEqual(d1(lambda x: math.log(math.sin(x)), 1.0), 1 / math.tan(1.0), places=4)
        self.assertIn("cot x", ANS["dd13"])

    def test_08_implicit(self):
        # circle x^2 + y^2 = 25 at (3, 4): slope -3/4
        self.assertAlmostEqual(-3 / 4, -0.75)
        self.assertIn("−3/4", ANS["dd14"])
        self.assertIn("3x + 4y = 25", ANS["dd14"])
        # x^2 + xy + y^2 = 7 near (1, 2)?  1 + 2 + 4 = 7 yes
        def slope_at(x, y):
            return -(2 * x + y) / (x + 2 * y)

        def y_of(x):
            # solve y^2 + x y + (x^2 - 7) = 0 for the positive branch
            return (-x + math.sqrt(x * x - 4 * (x * x - 7))) / 2

        self.assertAlmostEqual(d1(y_of, 1.0), slope_at(1.0, y_of(1.0)), places=3)
        self.assertIn("−(2x + y)/(x + 2y)", ANS["dd15"])

    def test_09_parametric(self):
        # x = a t^2, y = 2 a t  -> slope 1/t
        a = 3.0
        t = 2.0
        dx = 2 * a * t
        dy = 2 * a
        self.assertAlmostEqual(dy / dx, 1 / t)
        self.assertIn("1/t", ANS["dd16"])
        # circle
        th = 0.7
        self.assertAlmostEqual((a * math.cos(th)) / (-a * math.sin(th)), -1 / math.tan(th))
        self.assertIn("−cot θ", ANS["dd17"])

    def test_10_logarithmic(self):
        f = lambda x: x ** x
        self.assertAlmostEqual(d1(f, 2.0, h=1e-5), (2.0 ** 2) * (1 + math.log(2.0)), delta=1e-3)
        self.assertIn("xˣ(1 + log x)", ANS["dd18"])
        g = lambda x: (1 + x) ** x
        self.assertAlmostEqual(d1(g, 1.5, h=1e-5),
                               (2.5 ** 1.5) * (math.log(2.5) + 1.5 / 2.5), delta=1e-3)
        self.assertIn("(1 + x)ˣ[log(1 + x) + x/(1 + x)]", ANS["dd19"])

    def test_11_second_derivative_and_kinematics(self):
        self.assertAlmostEqual(d2(lambda x: x ** 4, 2.0), 12 * 4, places=3)
        self.assertIn("12x²", ANS["dd20"])
        self.assertAlmostEqual(d2(lambda x: math.sin(3 * x), 1.0), -9 * math.sin(3.0), places=3)
        self.assertIn("−9 sin 3x", ANS["dd21"])
        s = lambda t: t ** 3 - 6 * t ** 2 + 8 * t - 4
        self.assertEqual(3 * 9 - 12 * 3 + 8, -1)
        self.assertEqual(6 * 3 - 12, 6)
        self.assertIn("−1 m/s", ANS["dd22"])
        self.assertIn("6 m/s²", ANS["dd22"])

    def test_12_maxima_and_minima(self):
        f = lambda x: x ** 3 - 3 * x + 2
        self.assertEqual(3 * 1 - 3, 0)
        self.assertLess(6 * -1, 0)
        self.assertGreater(6 * 1, 0)
        self.assertEqual(f(-1), 4)
        self.assertEqual(f(1), 0)
        self.assertIn("maximum at x = −1", ANS["dd23"])
        g = lambda x: 2 * x ** 3 - 9 * x ** 2 + 12 * x
        self.assertEqual(6 * 1 - 18 * 1 + 12, 0)
        self.assertEqual(6 * 4 - 18 * 2 + 12, 0)
        self.assertEqual(g(1), 5)
        self.assertEqual(g(2), 4)
        self.assertIn("maximum, value f(1) = 5", ANS["dd24"])
        # practice 16
        h = lambda x: x ** 3 - 6 * x ** 2 + 9 * x
        self.assertEqual(3 * 1 - 12 + 9, 0)
        self.assertEqual(h(1), 4)
        self.assertEqual(h(3), 0)
        self.assertIn("maximum, f(1) = 4", PRACTICE[16])

    def test_13_diagrams_valid_and_referenced(self):
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

    def test_14_diagram_text_fits_the_canvas(self):
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

    def test_15_links_resolve_both_ways(self):
        num_ids = {n["id"] for n in UNIT["numericals"]}
        used = {e for s in UNIT["notes"] for it in s["items"] for e in it.get("examples", [])}
        self.assertEqual(used, num_ids, "every numerical should be reachable from a card")

    def test_16_practice_matches_exam_questions(self):
        practice = UNIT["notes"][-1]
        self.assertTrue(practice["title"]["en"].startswith("8."))
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4))
            self.assertGreater(len(item["body"]["en"]), 170, f"model answer {i} is too thin")
        self.assertTrue(UNIT["question_marks_are_suggested"])

    def test_17_html_is_balanced_and_clean(self):
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

    def test_18_export_carries_the_unit(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=180)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI02000021_u2.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 6)
            self.assertEqual(unit["title"]["en"], "Differentiation and its Applications")
            subject = json.loads((out / "subjects/DI02000021.json").read_text(encoding="utf-8"))
            self.assertIn(2, subject["available_units"])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            listed = {b["key"] for b in catalog["branches"]
                      if "DI02000021" in b["semesters"].get("2", [])}
            self.assertEqual(listed, {b["key"] for b in catalog["branches"]})
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
