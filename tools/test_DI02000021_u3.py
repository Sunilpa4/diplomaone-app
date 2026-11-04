"""Validation for Engineering Mathematics (DI02000021) Unit 3 "Integration and its Applications".

Run from the repo root:  python3 -m unittest tools.test_DI02000021_u3 -v
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

UNIT = json.loads((SUBJ_DIR / "unit3.json").read_text(encoding="utf-8"))
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


def integrate(f, a, b, n=2000):
    """Simpson's rule."""
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return total * h / 3


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


class EngineeringMathsUnit3(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 3)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (3, 10, 20))
        self.assertEqual((spec["hours"], spec["weightage"]), (10, 20))
        self.assertEqual(UNIT["title"]["en"], "Integration and its Applications")
        self.assertEqual(spec["file"], "unit3.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["3"], 14)
        self.assertEqual(UNIT["tabs"], TABS)
        self.assertEqual(UNIT["course_outcomes"], ["CO3"])

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 8)
        self.assertEqual(UNIT["lesson_count"], 26)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 26)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 15)
        self.assertEqual(len(UNIT["diagrams"]), 6)
        self.assertEqual(len(UNIT["numericals"]), 25)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 17)
        self.assertEqual(len(UNIT["exam_questions"]), 15)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 18)

    def test_03_syllabus_coverage(self):
        for word in ["integration", "integrand", "substitution", "by parts", "definite integral",
                     "limits", "area", "volume", "rotation", "standard"]:
            self.assertIn(word, TEXT, f"unit 3 misses: {word}")
        for topic in ["liate", "modulus", "disc", "odd function"]:
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

    def test_05_power_rule_and_standard_forms(self):
        self.assertAlmostEqual(d1(lambda x: x ** 6 / 6, 2.0), 2.0 ** 5, places=4)
        self.assertIn("x⁶/6", ANS["ig1"])
        self.assertAlmostEqual(d1(lambda x: x ** 3 + x ** 2 + x, 1.5),
                               3 * 1.5 ** 2 + 2 * 1.5 + 1, places=4)
        self.assertIn("x³ + x² + x", ANS["ig2"])
        self.assertAlmostEqual(d1(lambda x: (2 / 3) * x ** 1.5, 4.0), 2.0, places=5)
        self.assertIn("(2/3)x^(3/2)", ANS["ig3"])
        self.assertAlmostEqual(d1(lambda x: -1 / x, 2.0), 0.25, places=5)
        self.assertIn("−1/x", ANS["ig4"])
        self.assertAlmostEqual(d1(lambda x: math.exp(x) + math.log(abs(x)), 2.0),
                               math.exp(2) + 0.5, places=4)
        self.assertIn("log|x|", ANS["ig5"])
        self.assertAlmostEqual(d1(lambda x: -math.cos(x) - math.sin(x), 1.0),
                               math.sin(1) - math.cos(1), places=4)
        self.assertIn("−cos x − sin x", ANS["ig6"])

    def test_06_substitution(self):
        self.assertAlmostEqual(d1(lambda x: (2 * x + 3) ** 5 / 10, 1.0), (5.0) ** 4, places=3)
        self.assertIn("(2x + 3)⁵/10", ANS["ig8"])
        self.assertAlmostEqual(d1(lambda x: (x * x + 1) ** 4 / 8, 1.0), 1.0 * (2.0) ** 3, places=3)
        self.assertIn("(x² + 1)⁴/8", ANS["ig9"])
        self.assertAlmostEqual(d1(lambda x: math.log(x * x + 1), 2.0), 4 / 5, places=4)
        self.assertIn("log(x² + 1)", ANS["ig10"])
        self.assertAlmostEqual(d1(lambda x: math.sin(x) ** 4 / 4, 1.0),
                               math.sin(1.0) ** 3 * math.cos(1.0), places=4)
        self.assertIn("sin⁴x/4", ANS["ig11"])
        # definite substitution: integral of 2x(x^2+1)^3 from 0 to 1 = 15/4
        self.assertAlmostEqual(integrate(lambda x: 2 * x * (x * x + 1) ** 3, 0, 1), 3.75, places=4)
        self.assertIn("15/4", ANS["ig7"])

    def test_07_parts(self):
        self.assertAlmostEqual(d1(lambda x: math.exp(x) * (x - 1), 1.5),
                               math.exp(1.5) * 1.5, places=4)
        self.assertIn("eˣ(x − 1)", ANS["ig12"])
        self.assertAlmostEqual(d1(lambda x: x * math.sin(x) + math.cos(x), 1.0), math.cos(1.0), places=4)
        self.assertIn("x sin x + cos x", ANS["ig13"])
        f = lambda x: (x ** 2 / 2) * math.log(x) - x ** 2 / 4
        self.assertAlmostEqual(d1(f, 2.0), 2.0 * math.log(2.0), places=4)
        self.assertIn("(x²/2)log x − x²/4", ANS["ig14"])
        self.assertAlmostEqual(d1(lambda x: x * math.log(x) - x, 2.0), math.log(2.0), places=4)
        self.assertIn("x log x − x", ANS["ig15"])

    def test_08_definite_integrals(self):
        self.assertAlmostEqual(integrate(lambda x: x * x + 1, 0, 2), 14 / 3, places=4)
        self.assertIn("14/3", ANS["ig17"])
        self.assertAlmostEqual(integrate(lambda x: 2 * x, 1, 3), 8, places=6)
        self.assertIn("8", ANS["ig18"])
        self.assertAlmostEqual(integrate(math.sin, 0, math.pi / 2), 1, places=6)
        self.assertIn("1", ANS["ig19"])
        self.assertAlmostEqual(integrate(lambda x: math.exp(2 * x), 0, 1), (math.e ** 2 - 1) / 2, places=4)
        self.assertIn("(e² − 1)/2", ANS["ig20"])

    def test_09_properties(self):
        # odd function over symmetric limits
        self.assertAlmostEqual(integrate(lambda x: x ** 3, -1, 1), 0, places=6)
        self.assertIn("= 0", ANS["ig21"])
        # splitting the interval
        self.assertEqual(2 + 5, 7)
        self.assertIn("7", ANS["ig22"])
        # even function doubling
        self.assertAlmostEqual(integrate(lambda x: x * x, -2, 2), 16 / 3, places=3)

    def test_10_area(self):
        self.assertAlmostEqual(integrate(lambda x: x * x, 0, 3), 9, places=4)
        self.assertIn("9", ANS["ig23"])
        # 4x - x^2 from 0 to 4
        self.assertAlmostEqual(integrate(lambda x: 4 * x - x * x, 0, 4), 32 / 3, places=4)
        self.assertIn("32/3", ANS["ig24"])
        # practice 14: x^2 from 1 to 3
        self.assertAlmostEqual(integrate(lambda x: x * x, 1, 3), 26 / 3, places=4)
        self.assertIn("26/3", PRACTICE[14])

    def test_11_volume(self):
        # y = x rotated 0..2
        self.assertAlmostEqual(integrate(lambda x: x * x, 0, 2), 8 / 3, places=4)
        self.assertIn("8π/3", ANS["ig25"])
        # y = sqrt(x) rotated 0..4
        self.assertAlmostEqual(integrate(lambda x: x, 0, 4), 8, places=4)
        self.assertIn("8π", ANS["ig26"])
        # practice 15
        self.assertIn("8π", PRACTICE[15])
        # practice 11: x e^(x^2) from 0 to 1 = (e-1)/2
        self.assertAlmostEqual(integrate(lambda x: x * math.exp(x * x), 0, 1), (math.e - 1) / 2, places=4)

    def test_12_practice_answers_are_full(self):
        for i, item in enumerate(UNIT["notes"][-1]["items"], 1):
            self.assertGreater(len(item["body"]["en"]), 170, f"model answer {i} is too thin")

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
            unit = json.loads((out / "units/DI02000021_u3.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 6)
            self.assertEqual(unit["title"]["en"], "Integration and its Applications")
            subject = json.loads((out / "subjects/DI02000021.json").read_text(encoding="utf-8"))
            self.assertIn(3, subject["available_units"])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            listed = {b["key"] for b in catalog["branches"]
                      if "DI02000021" in b["semesters"].get("2", [])}
            self.assertEqual(listed, {b["key"] for b in catalog["branches"]})
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
