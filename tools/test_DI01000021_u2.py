"""Validation for Mathematics-I (DI01000021) Unit 2 "Trigonometry".

Run from the repo root:  python3 -m unittest tools.test_DI01000021_u2 -v
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

UNIT = json.loads((SUBJ_DIR / "unit2.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")
D2R = math.pi / 180


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


class MathUnit2(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 2)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (2, 12, 20))
        self.assertEqual((spec["hours"], spec["weightage"]), (12, 20))
        self.assertEqual(UNIT["title"]["en"], "Trigonometry")
        self.assertEqual(spec["file"], "unit2.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["2"], 14)
        self.assertEqual(UNIT["tabs"], TABS)
        self.assertTrue(UNIT["official"])

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 9)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"]), 39)
        self.assertEqual(len(UNIT["diagrams"]), 8)
        self.assertEqual(len(UNIT["numericals"]), 26)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 22)
        self.assertEqual(len(UNIT["exam_questions"]), 15)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 14)
        self.assertEqual(UNIT["lesson_count"], 24)
        self.assertEqual(UNIT["answered_practice_count"], 15)

    def test_03_syllabus_coverage(self):
        for word in ["degree", "radian", "arc length", "sector", "astc", "allied", "compound angle",
                     "multiple angle", "submultiple", "double angle", "half-angle", "triple-angle",
                     "amplitude", "period", "phase", "sum and factor", "inverse trigonometric",
                     "principal range"]:
            self.assertTrue(word in TEXT, f"unit 2 misses: {word}")
        # all seven official topics of unit 2 must be visible
        for topic in ["units of angles", "trigonometric functions", "graphs of sine and cosine",
                      "periodic", "inverse"]:
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

    def test_05_measurement_recompute(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        self.assertAlmostEqual(135 * D2R, 3 * math.pi / 4, places=12)
        self.assertIn("3π/4", ans["t1n1"])
        self.assertIn("150°", ans["t1n1"])
        # arc and sector, r = 7, theta = 60 degrees
        self.assertAlmostEqual(7 * math.pi / 3, 7.33, places=2)
        self.assertAlmostEqual(0.5 * 49 * math.pi / 3, 25.66, places=2)
        self.assertIn("7.33", ans["t1n2"])
        self.assertIn("25.66", ans["t1n2"])
        # wheel: 300 rpm, r = 0.30 m
        omega = 300 * 2 * math.pi / 60
        self.assertAlmostEqual(omega, 31.416, places=3)
        self.assertAlmostEqual(0.30 * omega, 9.4248, places=3)
        self.assertIn("31.42", ans["t1n3"])
        self.assertIn("9.42", ans["t1n3"])

    def test_06_triangle_and_identities(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        # sin theta = 3/5 in Q II
        self.assertAlmostEqual(math.sqrt(1 - 9 / 25), 0.8)
        self.assertIn("-4/5", ans["t1n4"])
        self.assertIn("-3/4", ans["t1n4"])
        # sin30 cos60 + cos30 sin60 = sin 90
        value = math.sin(30 * D2R) * math.cos(60 * D2R) + math.cos(30 * D2R) * math.sin(60 * D2R)
        self.assertAlmostEqual(value, 1.0, places=12)
        self.assertIn("<b>1.</b>", ans["t1n5"])
        # sin^2 30 + cos^2 60 + tan^2 45
        self.assertAlmostEqual(0.25 + 0.25 + 1, 1.5, places=12)
        self.assertIn("3/2", ans["t1n6"])
        # allied angles
        self.assertAlmostEqual(math.sin(150 * D2R), 1 / 2, places=12)
        self.assertAlmostEqual(math.cos(240 * D2R), -1 / 2, places=12)
        self.assertAlmostEqual(math.tan(315 * D2R), -1, places=12)
        self.assertAlmostEqual(math.sin(-330 * D2R), 1 / 2, places=12)
        self.assertIn("1/2, -1/2, -1 and 1/2", ans["t1n8"])

    def test_07_compound_and_multiple_recompute(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        exact = (math.sqrt(6) + math.sqrt(2)) / 4
        self.assertAlmostEqual(math.sin(75 * D2R), exact, places=12)
        self.assertAlmostEqual(math.cos(15 * D2R), exact, places=12)
        self.assertIn("(√6 + √2)/4", ans["t1n9"])
        self.assertAlmostEqual(math.tan(75 * D2R), 2 + math.sqrt(3), places=12)
        self.assertIn("2 + √3", ans["t1n11"])
        # given ratios: sin(A+B) = 63/65
        sinA, cosA = 3 / 5, 4 / 5
        cosB, sinB = 5 / 13, 12 / 13
        self.assertAlmostEqual(sinA * cosB + cosA * sinB, 63 / 65, places=12)
        self.assertIn("63/65", ans["t1n12"])
        # double angle
        self.assertAlmostEqual(2 * sinA * cosA, 24 / 25, places=12)
        self.assertAlmostEqual(1 - 2 * sinA ** 2, 7 / 25, places=12)
        self.assertIn("24/25", ans["t1n13"])
        self.assertIn("7/25", ans["t1n13"])
        self.assertAlmostEqual(2 * (0.5 ** 2) - 1, -0.5, places=12)
        self.assertIn("-1/2", ans["t1n14"])
        # half angle
        self.assertAlmostEqual(math.sin(15 * D2R), math.sqrt(2 - math.sqrt(3)) / 2, places=12)
        self.assertIn("√(2 - √3)/2", ans["t1n15"])
        # triple angle
        self.assertAlmostEqual(3 * 0.5 - 4 * 0.125, 1.0, places=12)
        self.assertIn("= 1", ans["t1n16"])

    def test_08_graphs_and_periodicity(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        self.assertAlmostEqual(2 * math.pi / 3, 2.0944, places=4)
        self.assertAlmostEqual(2 * math.pi / 0.5, 4 * math.pi, places=12)
        self.assertAlmostEqual(math.pi / 2, 1.5708, places=4)
        self.assertIn("2π/3", ans["t1n17"])
        self.assertIn("4π", ans["t1n17"])
        self.assertIn("π/2", ans["t1n17"])
        # amplitude / period / range
        self.assertEqual(abs(3), 3)
        self.assertAlmostEqual(2 * math.pi / 2, math.pi, places=12)
        self.assertIn("π/6", ans["t1n18"])
        self.assertIn("-3 to 3", ans["t1n18"])
        # 2 + 3 cos x
        self.assertEqual(max(2 + 3 * math.cos(x / 10) for x in range(0, 63)), 5)
        self.assertAlmostEqual(min(2 + 3 * math.cos(x / 10) for x in range(0, 63)), -1, places=2)
        self.assertIn("Maximum 5, minimum -1", ans["t1n19"])

    def test_09_sum_product_and_inverse(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        # sin 75 + sin 15
        self.assertAlmostEqual(math.sin(75 * D2R) + math.sin(15 * D2R), math.sqrt(6) / 2, places=12)
        self.assertIn("√6/2", ans["t1n20"])
        # 2 sin 40 cos 20
        self.assertAlmostEqual(2 * math.sin(40 * D2R) * math.cos(20 * D2R),
                               math.sin(60 * D2R) + math.sin(20 * D2R), places=12)
        self.assertIn("1.208", ans["t1n21"])
        # (sinA + sin3A)/(cosA + cos3A) = tan 2A
        for a in (10, 20, 35):
            lhs = (math.sin(a * D2R) + math.sin(3 * a * D2R)) / (math.cos(a * D2R) + math.cos(3 * a * D2R))
            self.assertAlmostEqual(lhs, math.tan(2 * a * D2R), places=10)
        self.assertIn("tan 2A", ans["t1n22"])
        # principal values
        self.assertAlmostEqual(math.asin(0.5), math.pi / 6, places=12)
        self.assertAlmostEqual(math.acos(-0.5), 2 * math.pi / 3, places=12)
        self.assertAlmostEqual(math.atan(1), math.pi / 4, places=12)
        self.assertIn("2π/3", ans["t1n23"])
        # composition outside the principal range
        self.assertAlmostEqual(math.asin(math.sin(5 * math.pi / 6)), math.pi / 6, places=12)
        self.assertIn("π/6", ans["t1n24"])
        # arctan sum
        self.assertAlmostEqual(math.atan(1) + math.atan(2) + math.atan(3), math.pi, places=12)
        self.assertIn("π", ans["t1n25"])
        # tower height
        self.assertAlmostEqual(50 * math.tan(30 * D2R), 28.8675, places=3)
        self.assertIn("28.87", ans["t1n26"])

    def test_10_diagrams_valid_and_referenced(self):
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

    def test_11_diagram_text_fits_the_canvas(self):
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

    def test_12_links_resolve_both_ways(self):
        num_ids = {n["id"] for n in UNIT["numericals"]}
        used = {e for s in UNIT["notes"] for it in s["items"] for e in it.get("examples", [])}
        self.assertEqual(used, num_ids, "every numerical should be reachable from a card")

    def test_13_practice_matches_exam_questions(self):
        practice = UNIT["notes"][-1]
        self.assertTrue(practice["title"]["en"].startswith("9."))
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4))
            self.assertGreater(len(item["body"]["en"]), 170, "model answer is too thin")
        self.assertTrue(UNIT["question_marks_are_suggested"])

    def test_14_html_is_balanced_and_clean(self):
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

    def test_15_export_carries_the_unit(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=180)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI01000021_u2.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 8)
            subject = json.loads((out / "subjects/DI01000021.json").read_text(encoding="utf-8"))
            self.assertIn(2, subject["available_units"])
            self.assertEqual(subject["available_units"], sorted(subject["available_units"]))
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            branches = catalog["branches"]
            self.assertEqual(sum(1 for b in branches if "DI01000021" in b["semesters"].get("1", [])), len(branches))
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
