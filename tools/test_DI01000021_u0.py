"""Validation for Mathematics-I (DI01000021) Unit 0 "Start Mathematics From Zero".

Run from the repo root:  python3 -m unittest tools.test_DI01000021_u0 -v
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
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000021 import SUBJ_DIR, DIAG_DIR, TABS  # noqa: E402
from notes_workshop import audit_svg, text_width  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit0.json").read_text(encoding="utf-8"))
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


class MathUnit0(unittest.TestCase):
    def test_01_syllabus_identity_and_scheme(self):
        self.assertEqual((SUBJ["code"], SUBJ["semester"], SUBJ["syllabus_year"]), ("DI01000021", 1, "2024-25"))
        self.assertEqual(SUBJ["branch"], "common")
        self.assertTrue(SUBJ["common_to_all_branches"])
        self.assertEqual(SUBJ["category"], "Basic Science (BSC)")
        self.assertEqual(SUBJ["teaching"], {"lecture": 3, "tutorial": 1, "practical": 0})
        self.assertEqual(SUBJ["exam"], {"theory_ese": 70, "theory_pa": 30, "practical_pa": 0,
                                        "practical_ese": 0, "total": 100, "credits": 4})
        official = [u for u in SUBJ["units"] if u["official"]]
        self.assertEqual([u["no"] for u in official], [1, 2, 3, 4, 5])
        self.assertEqual([u["hours"] for u in official], [9, 12, 9, 8, 7])
        self.assertEqual([u["weightage"] for u in official], [23, 20, 20, 20, 17])
        self.assertEqual(sum(u["hours"] for u in official), 45)
        self.assertEqual(sum(u["weightage"] for u in official), 100)
        self.assertEqual(SUBJ["theory_marks_by_unit"], {"1": 16, "2": 14, "3": 14, "4": 14, "5": 12})
        self.assertEqual(sum(SUBJ["theory_marks_by_unit"].values()), 70)
        self.assertEqual(len(SUBJ["course_outcomes"]), 5)
        self.assertEqual(SUBJ["practicals"], [])
        self.assertEqual(SUBJ["theory_rbt_percent"],
                         {"remember": 27, "understand": 39, "apply": 34, "analyze": 0,
                          "evaluate": 0, "create": 0})
        self.assertEqual(len(SUBJ["prerequisites"]), 7)
        self.assertIn("2024-25", (ROOT / "tools/syllabus_DI01000021.txt").read_text(encoding="utf-8"))

    def test_02_foundation_unit_is_installed_but_not_official(self):
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (0, 0, 0))
        self.assertFalse(UNIT["official"])
        self.assertTrue(UNIT["foundation"])
        self.assertEqual(UNIT["title"]["en"], SUBJ["units"][0]["title"]["en"])
        self.assertEqual(SUBJ["units"][0]["no"], 0)
        self.assertEqual(SUBJ["units"][0]["file"], "unit0.json")
        self.assertEqual(SUBJ["foundation_unit"]["no"], 0)
        self.assertNotIn("0", SUBJ["theory_marks_by_unit"], "the foundation chapter carries no GTU marks")
        # every official unit is advertised once its JSON is on the shelf
        for spec in SUBJ["units"][1:]:
            self.assertEqual(spec["file"], f"unit{spec['no']}.json")
            self.assertTrue((SUBJ_DIR / spec["file"]).is_file(), spec["file"])
        self.assertEqual(UNIT["tabs"], TABS)

    def test_03_english_only(self):
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

        walk(SUBJ)
        walk(UNIT)
        self.assertEqual(SUBJ["languages"], ["en"])

    def test_04_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 9)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"]), 45)
        self.assertEqual(len(UNIT["diagrams"]), 6)
        self.assertEqual(len(UNIT["numericals"]), 22)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 21)
        self.assertEqual(len(UNIT["exam_questions"]), 14)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 15)
        self.assertEqual(UNIT["lesson_count"], 31)
        self.assertEqual(UNIT["answered_practice_count"], 14)
        self.assertEqual(UNIT["content_kind"], "theory")

    def test_05_foundation_coverage(self):
        for word in ["absolute value", "fractions", "lcm", "gcd", "prime factorisation", "bodmas", "indices",
                     "surd", "standard form", "factorise", "difference of squares", "simultaneous",
                     "quadratic formula", "discriminant", "sets", "ratio", "percentage change", "mean",
                     "quadrant", "distance", "midpoint", "slope", "five-step", "error log", "exam strategy"]:
            self.assertTrue(word in TEXT, f"the foundation chapter misses: {word}")
        # every official prerequisite from the syllabus is taught here ("Factorization" is written
        # "factorisation" in the notes, so compare with z folded to s)
        norm = lambda t: t.lower().replace("z", "s")  # noqa: E731
        body = norm(TEXT)
        for pre in SUBJ["prerequisites"]:
            key = norm(pre).split(" of ")[-1].split(" and ")[0]
            self.assertTrue(any(norm(w) in body for w in (pre, key, key.rstrip("s"))),
                            f"prerequisite not covered: {pre}")

    def test_06_numericals_recompute(self):
        ans = {n["id"]: n["a"]["en"].replace("−", "-") for n in UNIT["numericals"]}

        # n1: signs
        self.assertEqual(-3 + 7 - (-2), 6)
        self.assertIn("6", ans["m0n1"])
        # n2: fractions added over the LCM
        total = Fraction(5, 6) + Fraction(3, 4)
        self.assertEqual(total, Fraction(19, 12))
        self.assertIn("19/12", ans["m0n2"])
        self.assertIn("1 7/12", ans["m0n2"])
        # n3: division flips the second fraction
        self.assertEqual(Fraction(2, 3) / Fraction(4, 9), Fraction(3, 2))
        self.assertIn("3/2", ans["m0n3"])
        # n4: gcd/lcm of 48 and 180
        self.assertEqual(math.gcd(48, 180), 12)
        self.assertEqual(48 * 180 // math.gcd(48, 180), 720)
        self.assertIn("720", ans["m0n4"])
        # n5: 15 % of 240
        self.assertAlmostEqual(0.15 * 240, 36, places=9)
        self.assertAlmostEqual(240 * 1.15, 276, places=9)
        self.assertIn("276", ans["m0n5"])
        # n6: BODMAS
        self.assertEqual(8 + 2 * (5 - 3) ** 2, 16)
        self.assertIn("16", ans["m0n6"])
        # n7: indices
        self.assertAlmostEqual(2 ** 3 * 2 ** -5 / 2 ** -1, 0.5, places=12)
        self.assertIn("1/2", ans["m0n7"])
        # n8: surds
        self.assertAlmostEqual(math.sqrt(72) - math.sqrt(18), 3 * math.sqrt(2), places=12)
        self.assertAlmostEqual(3 * math.sqrt(2), 4.2426, places=4)
        self.assertIn("4.243", ans["m0n8"])
        # n9: standard form
        self.assertAlmostEqual(3.6e4 * 2.5e3, 9.0e7, delta=1)
        self.assertIn("9.0 × 10⁷", ans["m0n9"])
        # n10: substitution with a negative value
        x = -2
        self.assertEqual(2 * x ** 2 - 3 * x + 1, 15)
        self.assertIn("15", ans["m0n10"])
        # n11: expansion checked numerically at three points
        for v in (-3, 1, 4):
            self.assertEqual((v + 3) * (v - 5), v * v - 2 * v - 15)
        self.assertIn("x² - 2x - 15", ans["m0n11"])
        # n12: factorisation and roots of 2x² + 7x − 15
        roots = sorted([(-7 + math.sqrt(169)) / 4, (-7 - math.sqrt(169)) / 4])
        self.assertEqual(roots, [-5, 1.5])
        self.assertAlmostEqual(sum(roots), -7 / 2, places=9)
        self.assertAlmostEqual(roots[0] * roots[1], -15 / 2, places=9)
        self.assertIn("3/2", ans["m0n12"])
        self.assertIn("-5", ans["m0n12"])
        # n13: one-variable equation
        self.assertEqual(3 * (11 - 2), 2 * 11 + 5)
        self.assertIn("x = 11", ans["m0n13"])
        # n14: simultaneous equations
        x, y = 3, 2
        self.assertEqual((2 * x + 3 * y, x - y), (12, 1))
        self.assertIn("x = 3, y = 2", ans["m0n14"])
        # n15: pens and pencils
        p, q = 20, 10
        self.assertEqual((3 * p + 2 * q, 2 * p + 3 * q), (80, 70))
        self.assertIn("₹20", ans["m0n15"])
        self.assertIn("₹10", ans["m0n15"])
        # n16: negative discriminant
        self.assertEqual((-4) ** 2 - 4 * 3 * 5, -44)
        self.assertIn("-44", ans["m0n16"])
        self.assertIn("no real", ans["m0n16"])
        # n17: rectangle word problem
        self.assertEqual(7 * (7 + 5), 84)
        self.assertEqual((-12) * (-12 + 5), 84)
        self.assertIn("7 m × 12 m", ans["m0n17"])
        # n18: ratio shares
        shares = [4500 * k // 9 for k in (2, 3, 4)]
        self.assertEqual(shares, [1000, 1500, 2000])
        self.assertEqual(sum(shares), 4500)
        for s in ("1,000", "1,500", "2,000"):
            self.assertIn(s, ans["m0n18"])
        # n19: percentage change both ways
        self.assertAlmostEqual((920 - 800) / 800 * 100, 15, places=9)
        self.assertAlmostEqual((800 - 920) / 920 * 100, -13.0435, places=4)
        self.assertIn("13.04", ans["m0n19"])
        # n20: distance, midpoint, slope
        self.assertEqual(math.hypot(6 - 2, 6 - 3), 5)
        self.assertEqual(((2 + 6) / 2, (3 + 6) / 2), (4, 4.5))
        self.assertAlmostEqual((6 - 3) / (6 - 2), 0.75, places=12)
        self.assertIn("4.5", ans["m0n20"])
        self.assertIn("0.75", ans["m0n20"])
        # n21: set operations
        A, B = {1, 2, 3, 4}, {3, 4, 5}
        self.assertEqual(len(A | B), 5)
        self.assertEqual(len(A | B), len(A) + len(B) - len(A & B))
        self.assertEqual(A - B, {1, 2})
        self.assertIn("{3, 4}", ans["m0n21"])
        # n22: mean before and after the next test
        marks = [62, 78, 85, 55]
        self.assertEqual(sum(marks) / len(marks), 70)
        self.assertEqual((sum(marks) + 90) / 5, 74)
        self.assertIn("70", ans["m0n22"])
        self.assertIn("74", ans["m0n22"])

    def test_07_diagrams_valid_and_referenced(self):
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

    def test_08_diagram_text_fits_the_canvas(self):
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

    def test_09_links_resolve_both_ways(self):
        num_ids = {n["id"] for n in UNIT["numericals"]}
        used = {e for s in UNIT["notes"] for it in s["items"] for e in it.get("examples", [])}
        self.assertEqual(used, num_ids, "every numerical should be reachable from a card")
        for item in (it for s in UNIT["notes"] for it in s["items"]):
            for e in item.get("examples", []):
                self.assertIn(e, num_ids)
            if item.get("diagram"):
                self.assertIn(item["diagram"], {d["id"] for d in UNIT["diagrams"]})

    def test_10_practice_matches_exam_questions(self):
        practice = UNIT["notes"][-1]
        self.assertTrue(practice["title"]["en"].startswith("9."))
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4))
            self.assertGreater(len(item["body"]["en"]), 200, "model answer is too thin")
        self.assertTrue(UNIT["question_marks_are_suggested"])
        self.assertIn("not official past papers", UNIT["question_provenance"])
        self.assertIn("no official", UNIT["assessment_note"]["en"].lower())

    def test_11_html_is_balanced_and_clean(self):
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

    def test_12_equation_tab_is_a_formula_sheet(self):
        for group in UNIT["equations"]:
            self.assertTrue(group["items"])
            for item in group["items"]:
                self.assertLess(len(item["f"]), 60, "an equation 'f' should stay a one-line formula or rule")
                self.assertTrue(item["terms"]["en"])

    def test_13_export_carries_the_foundation_unit(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=180)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI01000021_u0.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 6)
            self.assertEqual(unit["tabs"], TABS)
            self.assertFalse(unit["official"])
            subject = json.loads((out / "subjects/DI01000021.json").read_text(encoding="utf-8"))
            self.assertIn(0, subject["available_units"])
            self.assertEqual(len(subject["units"]), 6)
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            self.assertEqual(catalog["subjects"]["DI01000021"]["status"], "available")
            self.assertEqual(catalog["subjects"]["DI01000021"]["units"], 6)
            # a "Branch: All" subject must appear in semester 1 of every branch
            branches = catalog["branches"]
            listed = [b["key"] for b in branches if "DI01000021" in b["semesters"].get("1", [])]
            self.assertEqual(len(listed), len(branches), f"missing in: {set(b['key'] for b in branches) - set(listed)}")
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)

    def test_14_expansion_does_not_disturb_existing_units(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                           cwd=ROOT, check=True, capture_output=True, timeout=180)
            self.assertGreaterEqual(len(list((out / "units").glob("*_u*.json"))), 295)
            before = (out / "units/DI04000041_u1.json").read_bytes()
            subprocess.run([sys.executable, "tools/build_DI01000021_u0.py"], cwd=ROOT,
                           check=True, capture_output=True, timeout=180)
            out2 = Path(td) / "data2"
            subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out2)],
                           cwd=ROOT, check=True, capture_output=True, timeout=180)
            self.assertEqual((out2 / "units/DI04000041_u1.json").read_bytes(), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
