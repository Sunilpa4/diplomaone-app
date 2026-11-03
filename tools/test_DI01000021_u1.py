"""Validation for Mathematics-I (DI01000021) Unit 1 "Determinant and Function".

Run from the repo root:  python3 -m unittest tools.test_DI01000021_u1 -v
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

UNIT = json.loads((SUBJ_DIR / "unit1.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")


def det3(m):
    """Independent third-order determinant by cofactor expansion (no shortcuts)."""
    def minor(r, c):
        rows = [i for i in range(3) if i != r]
        cols = [j for j in range(3) if j != c]
        a, b = m[rows[0]][cols[0]], m[rows[0]][cols[1]]
        c2, d = m[rows[1]][cols[0]], m[rows[1]][cols[1]]
        return a * d - b * c2

    total = 0
    for c in range(3):
        total += ((-1) ** c) * m[0][c] * minor(0, c)
    return total


def cramer3(m, rhs):
    def replace(col):
        return [[rhs[i] if j == col else m[i][j] for j in range(3)] for i in range(3)]

    D = det3(m)
    return [det3(replace(k)) / D for k in range(3)]


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


class MathUnit1(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 1)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (1, 9, 23))
        self.assertEqual((spec["hours"], spec["weightage"]), (9, 23))
        self.assertEqual(UNIT["title"]["en"], "Determinant and Function")
        self.assertEqual(UNIT["title"]["en"], spec["title"]["en"])
        self.assertEqual(spec["file"], "unit1.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["1"], 16)
        self.assertEqual(UNIT["tabs"], TABS)
        self.assertTrue(UNIT["official"])

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 7)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"]), 32)
        self.assertEqual(len(UNIT["diagrams"]), 7)
        self.assertEqual(len(UNIT["numericals"]), 25)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 23)
        self.assertEqual(len(UNIT["exam_questions"]), 14)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 14)
        self.assertEqual(UNIT["lesson_count"], 18)
        self.assertEqual(UNIT["answered_practice_count"], 14)

    def test_03_syllabus_coverage(self):
        for word in ["determinant", "second order", "third order", "minor", "cofactor", "cramer",
                     "area of a triangle", "collinear", "domain", "codomain", "range", "even", "odd",
                     "piecewise", "logarithm", "change of base", "product law", "quotient law", "power law",
                     "common logarithm", "natural logarithm", "asymptote"]:
            self.assertTrue(word in TEXT, f"unit 1 misses: {word}")

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

    def test_05_determinants_recompute(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        # n1, n2: second order
        self.assertEqual(3 * 4 - 5 * 2, 2)
        self.assertIn("<b>2.</b>", ans["m1n1"])
        self.assertEqual((-4) * (-2) - 7 * 3, -13)
        self.assertIn("-13", ans["m1n2"])
        # n3: variable entry
        self.assertEqual(4 * 4 - 2 * 3, 10)
        self.assertEqual((-4) * (-4) - 2 * 3, 10)
        self.assertIn("±4", ans["m1n3"])
        # n4, n5: third order by independent cofactor expansion
        self.assertEqual(det3([[1, 2, 3], [4, 5, 6], [7, 8, 10]]), -3)
        self.assertIn("-3", ans["m1n4"])
        self.assertEqual(det3([[2, -1, 3], [0, 4, -2], [5, 1, 0]]), -46)
        self.assertIn("-46", ans["m1n5"])
        # n6: cofactors of a 3x3
        A = [[2, 3, 1], [4, 0, 5], [1, 2, 3]]
        self.assertEqual(det3(A), -33)
        cof = {}
        for i in range(3):
            for j in range(3):
                rows = [r for r in range(3) if r != i]
                cols = [c for c in range(3) if c != j]
                m = A[rows[0]][cols[0]] * A[rows[1]][cols[1]] - A[rows[0]][cols[1]] * A[rows[1]][cols[0]]
                cof[f"C{i+1}{j+1}"] = ((-1) ** (i + j)) * m
        self.assertEqual(cof, {"C11": -10, "C12": -7, "C13": 8, "C21": -7, "C22": 5,
                               "C23": -1, "C31": 15, "C32": -6, "C33": -12})
        for v in ("-10", "-7", "15", "-12"):
            self.assertIn(v, ans["m1n6"])
        self.assertIn("-33", ans["m1n6"])
        # n7: Cramer 2x2
        D = 2 * (-1) - 3 * 1
        Dx = 12 * (-1) - 3 * 1
        Dy = 2 * 1 - 12 * 1
        self.assertEqual((D, Dx / D, Dy / D), (-5, 3, 2))
        self.assertIn("x = 3, y = 2", ans["m1n7"])
        # n8: Cramer 3x3
        M = [[1, 1, 1], [1, -1, 1], [2, 1, -1]]
        self.assertEqual(det3(M), 6)
        self.assertEqual(cramer3(M, [6, 2, 1]), [1, 2, 3])
        self.assertIn("x = 1, y = 2, z = 3", ans["m1n8"])
        # n9, n10: area and collinearity
        area = abs(1 * (6 - 2) + 4 * (2 - 2) + 7 * (2 - 6)) / 2
        self.assertEqual(area, 12)
        self.assertIn("12 square units", ans["m1n9"])
        self.assertEqual(abs(1 * (6 - 10) + 3 * (10 - 2) + 5 * (2 - 6)), 0)
        self.assertIn("collinear", ans["m1n10"].lower())

    def test_06_functions_recompute(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        f = lambda x: 2 * x ** 2 - 3 * x + 1  # noqa: E731
        self.assertEqual([f(0), f(2), f(-1)], [1, 3, 6])
        self.assertIn("6", ans["m1n11"])
        # domain answers
        self.assertIn("x ≠ 3", ans["m1n12"])
        self.assertIn("[2, ∞)", ans["m1n12"])
        # completing the square
        self.assertEqual(min(x * x - 4 * x + 7 for x in range(-10, 20)), 3)
        self.assertIn("[3, ∞)", ans["m1n13"])
        # piecewise
        piece = lambda x: x + 1 if x < 0 else x * x  # noqa: E731
        self.assertEqual([piece(-2), piece(0), piece(3)], [-1, 0, 9])
        self.assertIn("-1, 0 and 9", ans["m1n14"])
        # even/odd
        g = lambda x: x ** 3 - x  # noqa: E731
        self.assertTrue(all(g(-x) == -g(x) for x in range(1, 6)))
        h = lambda x: x * x + x  # noqa: E731
        self.assertFalse(all(h(-x) == h(x) for x in range(1, 6)))
        self.assertFalse(all(h(-x) == -h(x) for x in range(1, 6)))
        self.assertIn("odd", ans["m1n15"])

    def test_07_logarithms_recompute(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}
        self.assertEqual([math.log2(32), math.log(1 / 27, 3), math.log10(1000), math.log(1, 5)],
                         [5, -3, 3, 0])
        for v in ("5", "-3", "3", "0"):
            self.assertIn(v, ans["m1n16"])
        # a^(3/2) = 8
        self.assertAlmostEqual(8 ** (2 / 3), 4, places=12)
        self.assertIn("a = 4", ans["m1n17"])
        # expansion of log(3x^2/y)
        self.assertIn("log 3 + 2 log x - log y", ans["m1n18"])
        # condensing
        self.assertAlmostEqual(2 * math.log10(3) + math.log10(4) - math.log10(6), math.log10(6), places=12)
        self.assertIn("log 6", ans["m1n19"])
        # log 72 from log 2 and log 3
        value = 3 * 0.3010 + 2 * 0.4771
        self.assertAlmostEqual(value, 1.8572, places=4)
        self.assertAlmostEqual(math.log10(72), 1.8573, places=4)
        self.assertIn("1.8572", ans["m1n20"])
        # change of base
        self.assertAlmostEqual(math.log(8, 4), 1.5, places=12)
        self.assertIn("3/2", ans["m1n21"])
        # solving
        self.assertEqual(math.log2(32), 5)
        self.assertEqual(2 ** 4 - 3, 13)
        self.assertIn("x = 13", ans["m1n22"])
        # pH
        self.assertAlmostEqual(-math.log10(1e-4), 4, places=12)
        self.assertIn("pH = 4", ans["m1n23"])
        # doubling
        self.assertEqual(20 * math.log2(8), 60)
        self.assertIn("60 minutes", ans["m1n24"])
        # reciprocal property
        self.assertAlmostEqual(math.log2(8) * math.log(2, 8), 1.0, places=12)
        self.assertIn("logₐ b · log_b a = 1", ans["m1n25"])

    def test_08_diagrams_valid_and_referenced(self):
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

    def test_09_diagram_text_fits_the_canvas(self):
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

    def test_10_links_resolve_both_ways(self):
        num_ids = {n["id"] for n in UNIT["numericals"]}
        used = {e for s in UNIT["notes"] for it in s["items"] for e in it.get("examples", [])}
        self.assertEqual(used, num_ids, "every numerical should be reachable from a card")
        for item in (it for s in UNIT["notes"] for it in s["items"]):
            for e in item.get("examples", []):
                self.assertIn(e, num_ids)

    def test_11_practice_matches_exam_questions(self):
        practice = UNIT["notes"][-1]
        self.assertTrue(practice["title"]["en"].startswith("7."))
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4))
            self.assertGreater(len(item["body"]["en"]), 180, "model answer is too thin")
        self.assertTrue(UNIT["question_marks_are_suggested"])
        self.assertIn("not official past papers", UNIT["question_provenance"])

    def test_12_html_is_balanced_and_clean(self):
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

    def test_13_equation_tab_is_a_formula_sheet(self):
        for group in UNIT["equations"]:
            self.assertTrue(group["items"])
            for item in group["items"]:
                self.assertLess(len(item["f"]), 60, "an equation 'f' should stay a one-line formula")
                self.assertTrue(item["terms"]["en"])

    def test_14_export_carries_the_unit(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=180)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI01000021_u1.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 7)
            self.assertEqual(unit["tabs"], TABS)
            subject = json.loads((out / "subjects/DI01000021.json").read_text(encoding="utf-8"))
            self.assertIn(1, subject["available_units"])
            self.assertEqual(subject["available_units"], sorted(subject["available_units"]))
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            self.assertEqual(catalog["subjects"]["DI01000021"]["status"], "available")
            branches = catalog["branches"]
            listed = [b["key"] for b in branches if "DI01000021" in b["semesters"].get("1", [])]
            self.assertEqual(len(listed), len(branches))
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
