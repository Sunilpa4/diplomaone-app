"""Validation for Engineering Mathematics (DI02000021) Unit 4 "Differential Equations".

Run from the repo root:  python3 -m unittest tools.test_DI02000021_u4 -v
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

UNIT = json.loads((SUBJ_DIR / "unit4.json").read_text(encoding="utf-8"))
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
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def assert_balanced(testcase, markup, where):
    stack = []
    for m in TAG_RE.finditer(markup):
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


class EngineeringMathsUnit4(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 4)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (4, 7, 17))
        self.assertEqual((spec["hours"], spec["weightage"]), (7, 17))
        self.assertEqual(UNIT["title"]["en"], "Differential Equations")
        self.assertEqual(spec["file"], "unit4.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["4"], 12)
        self.assertEqual(UNIT["tabs"], TABS)
        self.assertEqual(UNIT["course_outcomes"], ["CO4"])

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 8)
        self.assertEqual(UNIT["lesson_count"], 26)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 26)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 15)
        self.assertEqual(len(UNIT["diagrams"]), 5)
        self.assertEqual(len(UNIT["numericals"]), 22)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 17)
        self.assertEqual(len(UNIT["exam_questions"]), 15)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 18)

    def test_03_syllabus_coverage(self):
        for word in ["differential equation", "order", "degree", "variable separable",
                     "integrating factor", "linear", "general solution", "particular solution"]:
            self.assertIn(word, TEXT, f"unit 4 misses: {word}")
        for word in ["cooling", "growth", "decay", "initial condition"]:
            self.assertIn(word, TEXT)

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

    def test_05_order_and_degree(self):
        self.assertIn("order is 2", ANS["de1"])
        self.assertIn("degree 1", ANS["de1"])
        self.assertIn("degree is 3", ANS["de2"])
        self.assertIn("order is 3", ANS["de3"])
        self.assertIn("degree is 1", ANS["de3"])

    def test_06_verification_and_formation(self):
        # y = e^(2x) solves y' - 2y = 0
        self.assertAlmostEqual(d1(lambda x: math.exp(2 * x), 0.7) - 2 * math.exp(1.4), 0, places=4)
        # y = A cos x + B sin x solves y'' + y = 0
        y = lambda x: 2.0 * math.cos(x) - 1.5 * math.sin(x)
        self.assertAlmostEqual(d1(lambda x: d1(y, x, 1e-4), 1.1, 1e-4) + y(1.1), 0, places=3)
        # x y' - 2y = 0 comes from y = c x^2
        self.assertAlmostEqual(1.7 * d1(lambda x: 3 * x * x, 1.7) - 2 * 3 * 1.7 ** 2, 0, places=4)
        # y' = 2y comes from y = a e^(2x)
        self.assertAlmostEqual(d1(lambda x: 4 * math.exp(2 * x), 0.4) - 2 * 4 * math.exp(0.8), 0,
                               places=4)

    def test_07_separable_solutions(self):
        # dy/dx = x/y from y^2 = x^2 + c
        f = lambda x: math.sqrt(x * x + 5)
        self.assertAlmostEqual(d1(f, 1.3), 1.3 / f(1.3), places=5)
        self.assertIn("y² = x² + c", ANS["de8"])
        # dy/dx = x^2/y from y^2 = 2x^3/3 + c
        g = lambda x: math.sqrt(2 * x ** 3 / 3 + 4)
        self.assertAlmostEqual(d1(g, 1.1), 1.1 ** 2 / g(1.1), places=5)
        self.assertIn("2x³/3", ANS["de9"])
        # dy/dx = (1+y^2)/(1+x^2) from tan^-1 y = tan^-1 x + c
        h = lambda x: math.tan(math.atan(x) + 0.3)
        self.assertAlmostEqual(d1(h, 1.0), (1 + h(1.0) ** 2) / 2, places=4)
        self.assertIn("tan⁻¹y = tan⁻¹x + c", ANS["de10"])
        # dy/dx = 2xy from y = C e^(x^2)
        k = lambda x: 2.5 * math.exp(x * x)
        self.assertAlmostEqual(d1(k, 0.6), 2 * 0.6 * k(0.6), places=4)
        self.assertIn("C e^(x²)", ANS["de11"])
        # dy/dx = y/x from y = Cx
        self.assertAlmostEqual(d1(lambda x: 3 * x, 2.0), 3 * 2.0 / 2.0, places=6)
        self.assertIn("y = Cx", ANS["de12"])

    def test_08_exponential_and_trigonometric_forms(self):
        # dy/dx = e^(x+y) from -e^(-y) = e^x + c
        C = 2.5
        y = lambda x: -math.log(C - math.exp(x))
        self.assertAlmostEqual(d1(y, -0.5), math.exp(x_val := -0.5) * math.exp(y(-0.5)), places=4)
        self.assertIn("−e^(−y) = eˣ + c", ANS["de13"])
        # dy/dx = x(y^2+1) with y(0)=1 from tan^-1 y = x^2/2 + pi/4
        t = lambda x: math.tan(x * x / 2 + math.pi / 4)
        self.assertAlmostEqual(d1(t, 0.8), 0.8 * (1 + t(0.8) ** 2), places=4)
        self.assertAlmostEqual(t(0.0), 1.0, places=6)

    def test_09_initial_conditions(self):
        y = lambda x: math.exp(math.sin(x))
        self.assertAlmostEqual(d1(y, 0.9), y(0.9) * math.cos(0.9), places=5)
        self.assertAlmostEqual(y(0.0), 1.0, places=9)
        self.assertIn("y = e^(sin x)", ANS["de14"])
        self.assertAlmostEqual(math.tan(math.pi / 4), 1.0, places=9)
        self.assertIn("tan(x²/2 + π/4)", ANS["de15"])

    def test_10_growth_decay_and_cooling(self):
        k = math.log(2) / 5
        self.assertAlmostEqual(math.exp(5 * k), 2.0, places=9)
        self.assertIn("0.1386", ANS["de16"])
        kc = math.log(2) / 10
        T = lambda t: 20 + 80 * math.exp(-kc * t)
        self.assertAlmostEqual(T(10), 60, places=6)
        self.assertAlmostEqual(d1(T, 4.0), -kc * (T(4.0) - 20), places=4)
        self.assertIn("0.0693", ANS["de17"])
        # practice 13: T(0)=90, room 30, T(5)=70
        kp = math.log(1.5) / 5
        Tp = lambda t: 30 + 60 * math.exp(-kp * t)
        self.assertAlmostEqual(Tp(5), 70, places=6)
        self.assertAlmostEqual(Tp(0), 90, places=9)
        self.assertAlmostEqual(kp, 0.0811, places=4)
        # practice 14: N = 1000 * 2^(t/3)
        N = lambda t: 1000 * 2 ** (t / 3)
        self.assertAlmostEqual(N(3) / N(0), 2, places=9)
        self.assertAlmostEqual(N(9), 8000, places=6)

    def _check_linear(self, y, P, Q, x):
        self.assertAlmostEqual(d1(y, x) + P(x) * y(x), Q(x), places=4)

    def test_11_linear_solutions(self):
        self._check_linear(lambda x: 2 + 3 * math.exp(-2 * x), lambda x: 2.0, lambda x: 4.0, 1.1)
        self.assertIn("y = 2 + c e^(−2x)", ANS["de18"])
        self._check_linear(lambda x: math.exp(x) / 2 + 3 * math.exp(-x), lambda x: 1.0,
                           lambda x: math.exp(x), 0.9)
        self.assertIn("y = eˣ/2 + c e^(−x)", ANS["de19"])
        self._check_linear(lambda x: x * x / 4 + 2 / (x * x), lambda x: 2 / x, lambda x: x, 1.4)
        self.assertIn("y = x²/4 + c/x²", ANS["de20"])
        y21 = lambda x: math.sin(x) + 2.0 * math.cos(x)
        self._check_linear(y21, lambda x: math.tan(x), lambda x: 1 / math.cos(x), 1.0)
        self.assertIn("y = sin x + c cos x", ANS["de21"])

    def test_12_linear_in_x(self):
        # dx/dy + x = y from x = y - 1 + c e^(-y)
        x_of_y = lambda y: y - 1 + 2 * math.exp(-y)
        self.assertAlmostEqual(d1(x_of_y, 1.2) + x_of_y(1.2), 1.2, places=4)
        self.assertIn("x = y − 1 + c e^(−y)", ANS["de22"])
        # practice 15: dx/dy + 2x = y
        x15 = lambda y: y / 2 - 0.25 + 1.5 * math.exp(-2 * y)
        self.assertAlmostEqual(d1(x15, 1.0) + 2 * x15(1.0), 1.0, places=4)
        self.assertIn("y/2 − 1/4", PRACTICE[15])

    def test_13_practice_solutions_are_correct(self):
        # practice 5: dy/dx = x/y, y(0)=3
        y5 = lambda x: math.sqrt(x * x + 9)
        self.assertAlmostEqual(d1(y5, 1.5), 1.5 / y5(1.5), places=5)
        self.assertAlmostEqual(y5(0), 3.0, places=9)
        # practice 6: y = Cx solves y' = y/x
        self.assertAlmostEqual(d1(lambda x: 4 * x, 1.0), 4.0, places=6)
        # practice 7: y = tan(atan x + c)
        h = lambda x: math.tan(math.atan(x) - 0.2)
        self.assertAlmostEqual(d1(h, 1.2), (1 + h(1.2) ** 2) / (1 + 1.44), places=4)
        # practice 8: y = 2 e^(sin x)
        y8 = lambda x: 2 * math.exp(math.sin(x))
        self.assertAlmostEqual(d1(y8, 0.5), y8(0.5) * math.cos(0.5), places=5)
        self.assertAlmostEqual(y8(0), 2.0, places=9)
        # practice 9: y = 2 + c e^(-3x)
        self._check_linear(lambda x: 2 + 1.5 * math.exp(-3 * x), lambda x: 3.0, lambda x: 6.0, 0.8)
        # practice 10: y = x^3/4 + c/x  solves y' + y/x = x^2
        self._check_linear(lambda x: x ** 3 / 4 + 2 / x, lambda x: 1 / x, lambda x: x * x, 1.3)
        # practice 11: y = x^3/2 + cx  solves x y' - y = x^3
        y11 = lambda x: x ** 3 / 2 + 3 * x
        self.assertAlmostEqual(1.4 * d1(y11, 1.4) - y11(1.4), 1.4 ** 3, places=4)
        # practice 12: y = 1 + c e^(-x^2)  solves y' + 2xy = 2x
        y12 = lambda x: 1 + 2 * math.exp(-x * x)
        self.assertAlmostEqual(d1(y12, 0.9) + 2 * 0.9 * y12(0.9), 1.8, places=4)

    def test_14_practice_answers_are_full(self):
        for i, item in enumerate(UNIT["notes"][-1]["items"], 1):
            self.assertGreater(len(item["body"]["en"]), 170, f"model answer {i} is too thin")

    def test_15_diagrams_valid_and_referenced(self):
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

    def test_16_diagram_text_fits_the_canvas(self):
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

    def test_17_links_practice_and_html(self):
        num_ids = {n["id"] for n in UNIT["numericals"]}
        used = {e for s in UNIT["notes"] for it in s["items"] for e in it.get("examples", [])}
        self.assertEqual(used, num_ids, "every numerical should be reachable from a card")

        practice = UNIT["notes"][-1]
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4))
        self.assertTrue(UNIT["question_marks_are_suggested"])

        for si, section in enumerate(UNIT["notes"]):
            for ii, item in enumerate(section["items"]):
                body = (item.get("body") or {}).get("en", "")
                assert_balanced(self, body, f"notes {si}/{ii}")
                for bad in ("<script", "<style", "<img", "href="):
                    self.assertNotIn(bad, body)
        for n in UNIT["numericals"]:
            assert_balanced(self, n["a"]["en"], f"numerical {n['id']}")

    def test_18_export_carries_the_unit(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=180)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI02000021_u4.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 5)
            self.assertEqual(unit["title"]["en"], "Differential Equations")
            subject = json.loads((out / "subjects/DI02000021.json").read_text(encoding="utf-8"))
            self.assertIn(4, subject["available_units"])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            listed = {b["key"] for b in catalog["branches"]
                      if "DI02000021" in b["semesters"].get("2", [])}
            self.assertEqual(listed, {b["key"] for b in catalog["branches"]})
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
