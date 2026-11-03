"""Validation for Engineering Mathematics (DI02000021) Unit 1 "Matrices".

Run from the repo root:  python3 -m unittest tools.test_DI02000021_u1 -v
"""
import hashlib
import json
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

UNIT = json.loads((SUBJ_DIR / "unit1.json").read_text(encoding="utf-8"))
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
ANS = {n["id"]: re.sub(r"\s+", " ", strip_html(n["a"]["en"])) for n in UNIT["numericals"]}
PRACTICE = {i + 1: re.sub(r"\s+", " ", strip_html(it["body"]["en"]))
            for i, it in enumerate(UNIT["notes"][-1]["items"])}


# ---------------------------------------------------------------- tiny matrix maths
def mul(a, b):
    assert len(a[0]) == len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def adj2(m):
    return [[m[1][1], -m[0][1]], [-m[1][0], m[0][0]]]


def minor(m, i, j):
    return [[m[r][c] for c in range(3) if c != j] for r in range(3) if r != i]


def det3(m):
    return sum((-1) ** j * m[0][j] * det2(minor(m, 0, j)) for j in range(3))


def cof3(m):
    return [[(-1) ** (i + j) * det2(minor(m, i, j)) for j in range(3)] for i in range(3)]


def transpose(m):
    return [list(r) for r in zip(*m)]


def inv3(m):
    d = det3(m)
    assert d != 0
    return [[round(x / d, 10) for x in row] for row in transpose(cof3(m))]


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


class EngineeringMathsUnit1(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 1)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (1, 10, 23))
        self.assertEqual((spec["hours"], spec["weightage"]), (10, 23))
        self.assertEqual(UNIT["title"]["en"], "Matrices")
        self.assertEqual(spec["file"], "unit1.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["1"], 16)
        self.assertEqual(SUBJ["code"], "DI02000021")
        self.assertEqual(SUBJ["semester"], 2)
        self.assertEqual(UNIT["tabs"], TABS)
        self.assertEqual(UNIT["course_outcomes"], ["CO1"])

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 7)
        self.assertEqual(UNIT["lesson_count"], 26)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 26)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 15)
        self.assertEqual(len(UNIT["diagrams"]), 6)
        self.assertEqual(len(UNIT["numericals"]), 24)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 18)
        self.assertEqual(len(UNIT["exam_questions"]), 15)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 21)

    def test_03_syllabus_coverage(self):
        for word in ["matrix", "order", "transpose", "diagonal", "identity", "scalar",
                     "symmetric", "singular", "adjoint", "inverse", "cofactor", "minor",
                     "cramer", "determinant", "simultaneous", "row", "column"]:
            self.assertIn(word, TEXT, f"unit 1 misses: {word}")
        for topic in ["triangular", "skew-symmetric", "inconsistent", "dependent"]:
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

    def test_05_order_equality_and_construction(self):
        self.assertIn("2 × 3", ANS["mm1n1"])
        self.assertIn("a₁₃ = 3", ANS["mm1n1"])
        self.assertIn("a₂₂ = 5", ANS["mm1n1"])
        self.assertIn("x = 4", ANS["mm1n2"])
        self.assertIn("y = 6", ANS["mm1n2"])
        built = [[2 * i + j for j in (1, 2, 3)] for i in (1, 2)]
        self.assertEqual(built, [[3, 4, 5], [5, 6, 7]])
        for value in ("3", "4", "5", "6", "7"):
            self.assertIn(value, ANS["mm1n3"])

    def test_06_addition_scalar_and_transpose(self):
        a = [[1, 2, 3], [4, 5, 6]]
        b = [[6, 5, 4], [3, 2, 1]]
        self.assertEqual([[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(a, b)],
                         [[7, 7, 7], [7, 7, 7]])
        self.assertEqual([[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(a, b)],
                         [[-5, -3, -1], [1, 3, 5]])
        self.assertEqual(transpose(a), [[1, 4], [2, 5], [3, 6]])
        self.assertIn("3 × 2", ANS["mm1n4"])
        # 4A
        self.assertEqual([[4 * v for v in row] for row in [[0.5, 3], [-1, 0.25]]],
                         [[2, 12], [-4, 1]])
        # 3A - 2B
        three_a = [[3 * v for v in row] for row in [[2, -1], [3, 0]]]
        two_b = [[2 * v for v in row] for row in [[1, 4], [-2, 5]]]
        self.assertEqual([[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(three_a, two_b)],
                         [[4, -11], [13, -10]])
        # A + A transpose is symmetric
        m = [[1, 2], [3, 4]]
        s = [[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(m, transpose(m))]
        self.assertEqual(s, transpose(s))
        self.assertIn("5", ANS["mm1n8"])

    def test_07_products(self):
        a = [[1, 2], [3, 4]]
        b = [[2, 0], [1, 3]]
        self.assertEqual(mul(a, b), [[4, 6], [10, 12]])
        self.assertEqual(mul(b, a), [[2, 4], [10, 14]])
        self.assertIn("AB ≠ BA", ANS["mm1n10"])
        big_a = [[1, 2, 3], [4, 5, 6]]
        big_b = [[1, 0], [2, 1], [0, 3]]
        self.assertEqual(mul(big_a, big_b), [[5, 11], [14, 23]])
        self.assertIn("2 × 2", ANS["mm1n11"])
        # A² - 3A + 2I
        m = [[2, 1], [1, 0]]
        sq = mul(m, m)
        self.assertEqual(sq, [[5, 2], [2, 1]])
        poly = [[sq[i][j] - 3 * m[i][j] + (2 if i == j else 0) for j in range(2)] for i in range(2)]
        self.assertEqual(poly, [[1, -1], [-1, 3]])
        # AB = O with non-zero factors
        z = mul([[1, 1], [1, 1]], [[1, -1], [-1, 1]])
        self.assertEqual(z, [[0, 0], [0, 0]])
        # A² with unknown entry
        k = 4
        m = [[1, 2], [3, k]]
        self.assertEqual(mul(m, m), [[7, 10], [15, 22]])

    def test_08_two_by_two_inverse(self):
        a = [[3, 1], [5, 2]]
        self.assertEqual(det2(a), 1)
        self.assertEqual(adj2(a), [[2, -1], [-5, 3]])
        self.assertEqual(mul(a, adj2(a)), [[1, 0], [0, 1]])
        b = [[2, 3], [1, 4]]
        self.assertEqual(det2(b), 5)
        self.assertEqual(adj2(b), [[4, -3], [-1, 2]])
        inv_b = [[v / 5 for v in row] for row in adj2(b)]
        self.assertEqual([[round(v, 10) for v in row] for row in mul(b, inv_b)],
                         [[1, 0], [0, 1]])
        self.assertIn("4/5", ANS["mm1n16"])
        # singular values
        for x in (4, -4):
            self.assertEqual(x * x - 2 * 8, 0)
        self.assertIn("x = 4 or x = −4", ANS["mm1n17"])

    def test_09_three_by_three(self):
        a = [[2, 1, 3], [0, 4, 1], [5, 2, 0]]
        self.assertEqual(det3(a), -59)
        self.assertIn("−59", ANS["mm1n18"])
        b = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
        self.assertEqual(det3(b), 1)
        adj_b = transpose(cof3(b))
        self.assertEqual(adj_b, [[-24, 18, 5], [20, -15, -4], [-5, 4, 1]])
        self.assertEqual(mul(b, adj_b), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        c = [[1, 1, 1], [1, 2, 3], [1, 4, 9]]
        self.assertEqual(det3(c), 2)
        inv_c = inv3(c)
        ident = mul([[int(v * 2) / 2 for v in row] for row in c],
                    [[round(v * 1.0, 10) for v in row] for row in inv_c])
        self.assertEqual(ident, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertIn("(1/2)", ANS["mm1n20"])

    def test_10_solving_two_equations(self):
        # Cramer: x + y = 7, 2x - y = 2
        d = det2([[1, 1], [2, -1]])
        dx = det2([[7, 1], [2, -1]])
        dy = det2([[1, 7], [2, 2]])
        self.assertEqual((d, dx, dy), (-3, -9, -12))
        self.assertEqual((dx / d, dy / d), (3, 4))
        self.assertIn("−9/−3 = 3", ANS["mm1n21"])
        self.assertIn("−12/−3 = 4", ANS["mm1n21"])
        # inverse method: 2x + y = 8, x + 3y = 9
        a = [[2, 1], [1, 3]]
        self.assertEqual(det2(a), 5)
        solution = mul([[v / 5 for v in row] for row in adj2(a)], [[8], [9]])
        self.assertEqual(solution, [[3], [2]])
        self.assertIn("x = 3 and y = 2", ANS["mm1n22"])
        # word problem
        a2 = [[1, 1], [1, -1]]
        sol = mul([[v / det2(a2) for v in row] for row in adj2(a2)], [[30], [8]])
        self.assertEqual(sol, [[19], [11]])
        self.assertIn("19 and 11", ANS["mm1n23"])
        # consistency
        self.assertEqual(det2([[2, 3], [4, 6]]), 0)
        self.assertEqual(det2([[7, 3], [14, 6]]), 0)
        self.assertNotEqual(det2([[7, 3], [20, 6]]), 0)
        self.assertIn("infinitely many", ANS["mm1n24"])
        self.assertIn("no solution", ANS["mm1n24"])

    def test_11_practice_answers_recompute(self):
        # practice 10: adjoint and inverse of [[4, 5], [2, 3]]
        a = [[4, 5], [2, 3]]
        self.assertEqual(det2(a), 2)
        self.assertEqual(adj2(a), [[3, -5], [-2, 4]])
        self.assertIn("(1/2)", PRACTICE[10])
        # practice 11: singular values of [[k, 3], [2, k - 1]] -> 3 and -2
        for k in (3, -2):
            self.assertEqual(k * (k - 1) - 6, 0)
        self.assertIn("k = 3 or k = −2", PRACTICE[11])
        # practice 12: adjoint of the 3x3 already checked above
        self.assertIn("−24", PRACTICE[12])
        # practice 7: AB and BA for the permutation-style matrices
        self.assertEqual(mul([[1, 2], [3, 4]], [[0, 1], [1, 0]]), [[2, 1], [4, 3]])
        self.assertEqual(mul([[0, 1], [1, 0]], [[1, 2], [3, 4]]), [[3, 4], [1, 2]])
        # practice 3: aij = i + 3j
        self.assertEqual([[i + 3 * j for j in (1, 2, 3)] for i in (1, 2)], [[4, 7, 10], [5, 8, 11]])
        # practice 5: 2A - 3B
        two_a = [[2 * v for v in r] for r in [[1, 2], [3, 4]]]
        three_b = [[3 * v for v in r] for r in [[0, 1], [2, -1]]]
        self.assertEqual([[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(two_a, three_b)],
                         [[2, 1], [0, 11]])
        # practice 6: A + A transpose for [[2, 3], [1, 4]]
        m = [[2, 3], [1, 4]]
        self.assertEqual([[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(m, transpose(m))],
                         [[4, 4], [4, 8]])

    def test_12_diagrams_valid_and_referenced(self):
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

    def test_13_diagram_text_fits_the_canvas(self):
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

    def test_14_links_resolve_both_ways(self):
        num_ids = {n["id"] for n in UNIT["numericals"]}
        used = {e for s in UNIT["notes"] for it in s["items"] for e in it.get("examples", [])}
        self.assertEqual(used, num_ids, "every numerical should be reachable from a card")

    def test_15_practice_matches_exam_questions(self):
        practice = UNIT["notes"][-1]
        self.assertTrue(practice["title"]["en"].startswith("7."))
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4))
            self.assertGreater(len(item["body"]["en"]), 170, f"model answer {i} is too thin")
        self.assertTrue(UNIT["question_marks_are_suggested"])

    def test_16_html_is_balanced_and_clean(self):
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

    def test_17_export_carries_the_unit(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=180)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI02000021_u1.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 6)
            self.assertEqual(unit["title"]["en"], "Matrices")
            subject = json.loads((out / "subjects/DI02000021.json").read_text(encoding="utf-8"))
            self.assertIn(1, subject["available_units"])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            self.assertEqual(catalog["subjects"]["DI02000021"]["status"], "available")
            listed = {b["key"] for b in catalog["branches"]
                      if "DI02000021" in b["semesters"].get("2", [])}
            self.assertEqual(listed, {"electrical", "robotics", "ic", "power"})
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
