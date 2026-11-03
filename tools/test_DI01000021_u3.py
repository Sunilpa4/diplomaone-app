"""Validation for Mathematics-I (DI01000021) Unit 3 "Vectors".

Run from the repo root:  python3 -m unittest tools.test_DI01000021_u3 -v
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

UNIT = json.loads((SUBJ_DIR / "unit3.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]


def norm(a):
    return math.sqrt(dot(a, a))


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


class MathUnit3(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 3)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (3, 9, 20))
        self.assertEqual((spec["hours"], spec["weightage"]), (9, 20))
        self.assertEqual(UNIT["title"]["en"], "Vectors")
        self.assertEqual(spec["file"], "unit3.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["3"], 14)
        self.assertEqual(UNIT["tabs"], TABS)

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 6)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"]), 30)
        self.assertEqual(len(UNIT["diagrams"]), 7)
        self.assertEqual(len(UNIT["numericals"]), 26)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 22)
        self.assertEqual(len(UNIT["exam_questions"]), 15)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 12)
        self.assertEqual(UNIT["lesson_count"], 15)
        self.assertEqual(UNIT["answered_practice_count"], 15)

    def test_03_syllabus_coverage(self):
        for word in ["scalar", "vector", "triangle law", "parallelogram", "magnitude", "direction cosine",
                     "scalar product", "vector product", "dot product", "cross product", "angle between",
                     "projection", "work done", "moment of force", "perpendicular", "parallelogram law"]:
            self.assertTrue(word in TEXT, f"unit 3 misses: {word}")
        for topic in ["addition", "subtraction", "properties", "right-hand rule"]:
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

    def test_05_magnitude_and_algebra(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        a = [3, -4, 12]
        self.assertEqual(norm(a), 13)
        self.assertIn("13 units", ans["v1n1"])
        b = [2, 3, -6]
        self.assertEqual(norm(b), 7)
        self.assertIn("a-hat = (2i + 3j - 6k)/7", ans["v1n2"])
        c = [1, 2, 2]
        self.assertEqual(norm(c), 3)
        dcs = [x / norm(c) for x in c]
        self.assertEqual(dcs, [1 / 3, 2 / 3, 2 / 3])
        self.assertAlmostEqual(sum(x * x for x in dcs), 1.0, places=12)
        self.assertIn("cos α = 1/3", ans["v1n3"])
        # addition / subtraction
        p, q = [2, 3, -1], [1, -2, 4]
        self.assertEqual([x + y for x, y in zip(p, q)], [3, 1, 3])
        self.assertAlmostEqual(norm([3, 1, 3]), math.sqrt(19), places=12)
        self.assertEqual([x - y for x, y in zip(p, q)], [1, 5, -5])
        self.assertAlmostEqual(norm([1, 5, -5]), math.sqrt(51), places=12)
        self.assertIn("√19", ans["v1n4"])
        self.assertIn("√51", ans["v1n4"])

    def test_06_dot_products_and_angles(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        a = [2, -1, 1]
        b = [1, 1, 2]
        self.assertEqual(dot(a, b), 3)
        self.assertAlmostEqual(dot(a, b) / (norm(a) * norm(b)), 0.5, places=12)
        self.assertIn("θ = 60°", ans["v1n5"])
        self.assertEqual(dot([1, 2, 3], [4, -5, 6]), 12)
        self.assertIn("12", ans["v1n6"])
        # angle 79 degrees case
        u, v = [2, 2, -1], [6, -3, 2]
        self.assertEqual((norm(u), norm(v)), (3.0, 7.0))
        cos = dot(u, v) / (norm(u) * norm(v))
        self.assertAlmostEqual(cos, 4 / 21, places=12)
        self.assertAlmostEqual(math.degrees(math.acos(cos)), 79.0, places=1)
        self.assertIn("79", ans["v1n7"])
        # perpendicularity
        self.assertAlmostEqual(2 - 2 * 2.5 + 3, 0, places=12)
        self.assertIn("λ = 5/2", ans["v1n8"])
        # projection
        self.assertAlmostEqual(dot([3, 1, -2], [1, 1, 1]) / math.sqrt(3), 1.1547, places=4)
        self.assertIn("2/√3", ans["v1n9"])
        # angle from dot product only
        self.assertAlmostEqual(math.degrees(math.acos(6 / 12)), 60.0, places=9)

    def test_07_cross_products_and_areas(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        a = [2, 1, 3]
        b = [1, -2, 1]
        cr = cross(a, b)
        self.assertEqual(cr, [7, 1, -5])
        self.assertAlmostEqual(norm(cr), 5 * math.sqrt(3), places=12)
        self.assertIn("7i + j - 5k", ans["v1n10"].replace("−", "-"))
        # perpendicularity of the cross product
        self.assertEqual(dot(cr, a), 0)
        self.assertEqual(dot(cr, b), 0)
        # parallelogram area
        self.assertAlmostEqual(norm(cr), 8.6602, places=3)
        self.assertIn("5√3", ans["v1n11"])
        # triangle from three points
        A, B, C = [1, 1, 1], [2, 3, 4], [4, 2, 3]
        ab = [B[i] - A[i] for i in range(3)]
        ac = [C[i] - A[i] for i in range(3)]
        cr2 = cross(ab, ac)
        self.assertEqual(cr2, [1, 7, -5])
        self.assertAlmostEqual(0.5 * norm(cr2), 5 * math.sqrt(3) / 2, places=12)
        self.assertIn("5√3/2", ans["v1n12"])
        # unit perpendicular
        cr3 = cross([1, 1, 0], [0, 1, 1])
        self.assertEqual(cr3, [1, -1, 1])
        self.assertAlmostEqual(norm(cr3), math.sqrt(3), places=12)
        self.assertIn("(i - j + k)/√3", ans["v1n13"].replace("−", "-"))
        # identity |a x b|^2 + (a.b)^2 = |a|^2|b|^2
        self.assertAlmostEqual(norm(cross([3, 0, 0], [0, 4, 0])) ** 2 + dot([3, 0, 0], [0, 4, 0]) ** 2, 144, places=9)

    def test_08_applications(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        # work done
        self.assertEqual(dot([3, 2, -1], [2, -1, 3]), 1)
        self.assertIn("1 J", ans["v1n14"])
        self.assertAlmostEqual(20 * 5 * math.cos(math.radians(60)), 50, places=9)
        self.assertIn("50 J", ans["v1n15"])
        self.assertEqual(dot([1, 1, 1], [3, 4, 0]), 7)
        self.assertIn("7 J", ans["v1n24"])
        # moment about origin
        r, F = [3, -1, 2], [2, 1, -1]
        M = cross(r, F)
        self.assertEqual(M, [-1, 7, 5])
        self.assertAlmostEqual(norm(M), 5 * math.sqrt(3), places=12)
        self.assertIn("-i + 7j + 5k", ans["v1n16"])
        self.assertEqual(dot(M, r), 0)
        self.assertEqual(dot(M, F), 0)
        # moment about a point
        r2 = [2, 3, 0]
        M2 = cross(r2, [1, 2, 0])
        self.assertEqual(M2, [0, 0, 1])
        self.assertIn("M = k", ans["v1n17"])
        self.assertAlmostEqual(40 * 0.5, 20, places=9)
        self.assertIn("20 N·m", ans["v1n18"])
        # moment magnitude  sqrt(83)
        M3 = cross([2, 3, 1], [1, -1, 2])
        self.assertEqual(M3, [7, -3, -5])
        self.assertAlmostEqual(norm(M3), math.sqrt(83), places=12)
        self.assertIn("√83", ans["v1n25"])

    def test_09_mixed_numericals(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        # |a+b| = |a-b| implies perpendicular
        a, b = [1, 2], [2, -1]
        self.assertEqual(dot(a, b), 0)
        self.assertAlmostEqual(norm([a[0] + b[0], a[1] + b[1]]), norm([a[0] - b[0], a[1] - b[1]]), places=12)
        self.assertIn("perpendicular", ans["v1n19"].lower())
        # linear combination
        a3, b3 = [1, -2, 3], [2, 1, -1]
        comb = [2 * a3[i] - 3 * b3[i] for i in range(3)]
        self.assertEqual(comb, [-4, -7, 9])
        self.assertAlmostEqual(norm(comb), math.sqrt(146), places=12)
        self.assertIn("√146", ans["v1n20"])
        # vector of given magnitude
        self.assertEqual([6, 8], [3 * 10 / 5, 4 * 10 / 5])
        self.assertAlmostEqual(norm([6, 8]), 10, places=12)
        self.assertIn("6i + 8j", ans["v1n21"])
        # AB, distance, midpoint
        P, Q = [1, 2, 3], [3, 4, 5]
        self.assertEqual([Q[i] - P[i] for i in range(3)], [2, 2, 2])
        self.assertAlmostEqual(norm([2, 2, 2]), 2 * math.sqrt(3), places=12)
        self.assertIn("(2, 3, 4)", ans["v1n22"])
        # angle from given dot
        self.assertAlmostEqual(math.degrees(math.acos(6 / (3 * 4))), 60.0, places=9)
        self.assertIn("60°", ans["v1n23"])
        # |a x b| from identity
        self.assertAlmostEqual(math.sqrt(144 - 36), 6 * math.sqrt(3), places=12)
        self.assertIn("6√3", ans["v1n26"])

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
        self.assertTrue(practice["title"]["en"].startswith("6."))
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
            unit = json.loads((out / "units/DI01000021_u3.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 7)
            subject = json.loads((out / "subjects/DI01000021.json").read_text(encoding="utf-8"))
            self.assertIn(3, subject["available_units"])
            self.assertEqual(subject["available_units"], sorted(subject["available_units"]))
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            branches = catalog["branches"]
            self.assertEqual(sum(1 for b in branches if "DI01000021" in b["semesters"].get("1", [])), len(branches))
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
