"""Validation for Engineering Mathematics (DI02000021) Unit 5 "Complex Numbers".

Run from the repo root:  python3 -m unittest tools.test_DI02000021_u5 -v
"""
import cmath
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

UNIT = json.loads((SUBJ_DIR / "unit5.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")

OMEGA = complex(-0.5, math.sqrt(3) / 2)


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


def close(testcase, got, want, places=6, msg=""):
    testcase.assertAlmostEqual(got.real, complex(want).real, places=places, msg=msg)
    testcase.assertAlmostEqual(got.imag, complex(want).imag, places=places, msg=msg)


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


class EngineeringMathsUnit5(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 5)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (5, 7, 17))
        self.assertEqual((spec["hours"], spec["weightage"]), (7, 17))
        self.assertEqual(UNIT["title"]["en"], "Complex Numbers")
        self.assertEqual(spec["file"], "unit5.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["5"], 12)
        self.assertEqual(UNIT["tabs"], TABS)
        self.assertEqual(UNIT["course_outcomes"], ["CO5"])

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 8)
        self.assertEqual(UNIT["lesson_count"], 26)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"][:-1]), 26)
        self.assertEqual(len(UNIT["notes"][-1]["items"]), 15)
        self.assertEqual(len(UNIT["diagrams"]), 5)
        self.assertEqual(len(UNIT["numericals"]), 20)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 18)
        self.assertEqual(len(UNIT["exam_questions"]), 15)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 18)

    def test_03_syllabus_coverage(self):
        for word in ["complex number", "argand", "conjugate", "modulus", "inverse", "argument",
                     "polar form", "de moivre", "square root", "cube roots of unity"]:
            self.assertIn(word, TEXT, f"unit 5 misses: {word}")
        for word in ["i² = −1", "cis", "ω"]:
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

    def test_05_powers_and_algebra(self):
        close(self, 1j ** 15, -1j)
        self.assertIn("−i", ANS["cm1"])
        close(self, (5 - 2j) + (-3 + 4j), 2 + 2j)
        close(self, (3 + 2j) * (4 - 5j), 22 - 7j)
        self.assertIn("22 − 7i", ANS["cm4"])
        close(self, (1 + 2j) / (3 - 4j), complex(-0.2, 0.4))
        self.assertIn("−1/5", ANS["cm5"])
        close(self, (1 + 1j) ** 6, -8j)
        self.assertIn("−8i", ANS["cm20"])

    def test_06_conjugate_modulus_inverse(self):
        z = 3 - 4j
        close(self, z.conjugate(), 3 + 4j)
        self.assertAlmostEqual(abs(z), 5.0, places=9)
        self.assertAlmostEqual((z * z.conjugate()).real, 25.0, places=9)
        close(self, 1 / z, (3 + 4j) / 25)
        self.assertIn("z̄ = 3 + 4i", ANS["cm6"])

    def test_07_argument_and_polar_form(self):
        # cm7: -1 + i√3
        z7 = -1 + 1j * math.sqrt(3)
        self.assertAlmostEqual(abs(z7), 2.0, places=9)
        self.assertAlmostEqual(cmath.phase(z7), 2 * math.pi / 3, places=9)
        self.assertIn("2 cis (2π/3)", ANS["cm7"])
        # cm8: 1 + i
        z8 = 1 + 1j
        self.assertAlmostEqual(abs(z8), math.sqrt(2), places=9)
        self.assertAlmostEqual(cmath.phase(z8), math.pi / 4, places=9)
        close(self, cmath.rect(abs(z8), cmath.phase(z8)), z8)
        # cm9: -3 - 3i
        z9 = -3 - 3j
        self.assertAlmostEqual(abs(z9), 3 * math.sqrt(2), places=9)
        self.assertAlmostEqual(cmath.phase(z9), -3 * math.pi / 4, places=9)
        # practice 7: 2 + 2√3 i = 4 cis π/3
        z_p7 = 2 + 2j * math.sqrt(3)
        self.assertAlmostEqual(abs(z_p7), 4.0, places=9)
        self.assertAlmostEqual(cmath.phase(z_p7), math.pi / 3, places=9)

    def test_08_de_moivre_powers(self):
        close(self, (1 + 1j) ** 8, 16 + 0j, places=6)
        self.assertIn("16", ANS["cm10"])
        close(self, (1 - 1j * math.sqrt(3)) ** 6, 64 + 0j, places=6)
        self.assertIn("64", ANS["cm11"])
        close(self, (math.sqrt(3) + 1j) ** 4, -8 + 8j * math.sqrt(3), places=6)
        self.assertIn("−8 + 8√3 i", ANS["cm12"])
        # practice 8 and 9 and 10
        close(self, (1 - 1j) ** 6, 8j)
        close(self, (1 + 1j * math.sqrt(3)) ** 6, 64 + 0j, places=6)
        close(self, (1 - 1j) ** 4, -4 + 0j)

    def test_09_roots(self):
        for target, root in ((3 + 4j, 2 + 1j), (8 - 6j, 3 - 1j), (-5 + 12j, 2 + 3j),
                             (8 + 6j, 3 + 1j), (-15 - 8j, 1 - 4j)):
            close(self, root * root, target, places=6)
            close(self, cmath.sqrt(target), root, places=6)
        self.assertIn("±(2 + i)", ANS["cm13"])
        self.assertIn("±(3 − i)", ANS["cm14"])
        self.assertIn("±(2 + 3i)", ANS["cm15"])
        roots16 = [cmath.rect(2, k * math.pi / 2) for k in range(4)]
        for want in (2, 2j, -2, -2j):
            self.assertTrue(any(abs(r - want) < 1e-9 for r in roots16))
        self.assertIn("−2i", ANS["cm19"])

    def test_10_cube_roots_of_unity(self):
        self.assertAlmostEqual(abs(OMEGA), 1.0, places=9)
        close(self, OMEGA ** 3, 1 + 0j)
        close(self, 1 + OMEGA + OMEGA ** 2, 0 + 0j)
        close(self, OMEGA * OMEGA, OMEGA.conjugate(), places=9)
        # cm17 and cm18 and practice 14
        close(self, (1 + OMEGA ** 2) ** 3, -1 + 0j)
        close(self, (1 + OMEGA - OMEGA ** 2) ** 3, -8 + 0j)
        self.assertIn("−8", ANS["cm18"])
        # practice 15: cube roots of 27
        for k in range(3):
            root = cmath.rect(3, 2 * k * math.pi / 3)
            close(self, root ** 3, 27 + 0j, places=6)

    def test_11_practice_answers_are_full(self):
        for i, item in enumerate(UNIT["notes"][-1]["items"], 1):
            self.assertGreater(len(item["body"]["en"]), 170, f"model answer {i} is too thin")

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
        self.assertTrue(practice["title"]["en"].startswith("8."))
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4))
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

    def test_17_exam_questions_are_answerable(self):
        for q in UNIT["exam_questions"]:
            text = q["q"]["en"].lower()
            self.assertTrue(text.startswith("practice:"), text)
            self.assertGreater(len(text), 15)
        self.assertEqual(len({q["q"]["en"] for q in UNIT["exam_questions"]}), 15)

    def test_18_export_carries_the_unit(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=180)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI02000021_u5.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 5)
            self.assertEqual(unit["title"]["en"], "Complex Numbers")
            subject = json.loads((out / "subjects/DI02000021.json").read_text(encoding="utf-8"))
            self.assertIn(5, subject["available_units"])
            self.assertEqual(subject["available_units"], [1, 2, 3, 4, 5])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            listed = {b["key"] for b in catalog["branches"]
                      if "DI02000021" in b["semesters"].get("2", [])}
            self.assertEqual(listed, {b["key"] for b in catalog["branches"]})
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
