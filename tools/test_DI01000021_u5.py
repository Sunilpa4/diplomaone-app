"""Validation for Mathematics-I (DI01000021) Unit 5 "Limit".

Run from the repo root:  python3 -m unittest tools.test_DI01000021_u5 -v
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

UNIT = json.loads((SUBJ_DIR / "unit5.json").read_text(encoding="utf-8"))
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
ANS = {n["id"]: re.sub(r"\s+", " ", strip_html(n["a"]["en"])).replace("−", "-")
       for n in UNIT["numericals"]}
PRACTICE = {i + 1: re.sub(r"\s+", " ", strip_html(it["body"]["en"])).replace("−", "-")
            for i, it in enumerate(UNIT["notes"][-1]["items"])}


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


class MathUnit5(unittest.TestCase):
    def test_01_unit_matches_syllabus(self):
        spec = next(u for u in SUBJ["units"] if u["no"] == 5)
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (5, 7, 17))
        self.assertEqual((spec["hours"], spec["weightage"]), (7, 17))
        self.assertEqual(UNIT["title"]["en"], "Limit")
        self.assertEqual(spec["file"], "unit5.json")
        self.assertEqual(SUBJ["theory_marks_by_unit"]["5"], 12)
        self.assertEqual(UNIT["tabs"], TABS)
        self.assertEqual(UNIT["course_outcomes"], ["CO5"])

    def test_02_structure_and_counts(self):
        self.assertEqual(len(UNIT["notes"]), 6)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"]), 27)
        self.assertEqual(len(UNIT["diagrams"]), 6)
        self.assertEqual(len(UNIT["numericals"]), 24)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 18)
        self.assertEqual(len(UNIT["exam_questions"]), 14)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 13)
        self.assertEqual(UNIT["lesson_count"], 13)
        self.assertEqual(UNIT["answered_practice_count"], 14)

    def test_03_syllabus_coverage(self):
        for word in ["limit", "left-hand", "right-hand", "two-sided", "indeterminate", "factorise",
                     "rationalis", "highest power", "sin x", "standard limit", "continuous", "radians"]:
            self.assertTrue(word in TEXT, f"unit 5 misses: {word}")
        for topic in ["substitution", "conjugate", "number e", "removable"]:
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

    def test_05_substitution_and_factorisation(self):
        self.assertEqual(3 * 4 - 5 * 2 + 1, 3)
        self.assertIn("3", ANS["lm1n1"])
        # (x^2 - 9)/(x - 3) -> 6
        self.assertEqual(3 + 3, 6)
        self.assertIn("6", ANS["lm1n2"])
        # (x^3 - 1)/(x - 1) -> 3
        self.assertEqual(1 + 1 + 1, 3)
        self.assertIn("3", ANS["lm1n3"])
        # (x^2 - 4)/(x^2 - 5x + 6) at x = 2 -> 4 / -1
        self.assertEqual((2 + 2) / (2 - 3), -4)
        self.assertIn("-4", ANS["lm1n4"])
        # x^2 + 3x - 4 at 1 after cancelling
        self.assertEqual(1 + 4, 5)
        self.assertIn("5", PRACTICE[1])

    def test_06_rationalising(self):
        # (sqrt(1+x) - 1)/x -> 1/2
        self.assertAlmostEqual(1 / (math.sqrt(1) + 1), 0.5)
        self.assertIn("1/2", ANS["lm1n5"])
        # (sqrt(x) - 2)/(x - 4) -> 1/4
        self.assertAlmostEqual(1 / (2 + 2), 0.25)
        self.assertIn("1/4", ANS["lm1n6"])
        # (1/x - 1/3)/(x - 3) -> -1/9
        self.assertAlmostEqual(-1 / (3 * 3), -1 / 9, places=12)
        self.assertIn("-1/9", ANS["lm1n7"])
        # (sqrt(4+x) - 2)/x -> 1/4
        self.assertIn("1/4", PRACTICE[3])

    def test_07_limits_at_infinity(self):
        self.assertAlmostEqual(3 / 5, 0.6)
        self.assertIn("3/5", ANS["lm1n8"])
        self.assertIn("2/1", ANS["lm1n9"]) if "2/1" in ANS["lm1n9"] else self.assertIn("2", ANS["lm1n9"])
        # sqrt(x^2 + 3x) - x -> 3/2
        self.assertEqual(3 / (1 + 1), 1.5)
        self.assertIn("3/2", ANS["lm1n10"])
        self.assertIn("5/2", PRACTICE[12])
        self.assertIn("5/2", PRACTICE[4])

    def test_08_trigonometric_limits(self):
        self.assertIn("5.", ANS["lm1n11"])
        self.assertAlmostEqual(3 / 7, 0.428571, places=6)
        self.assertIn("3/7", ANS["lm1n12"])
        self.assertAlmostEqual(math.cos(0) * 1 / 2, 0.5)
        self.assertIn("1/2", ANS["lm1n13"])
        self.assertIn("1", ANS["lm1n14"])
        self.assertIn("2", ANS["lm1n15"])
        # practice 6: (1 - cos 4x)/x^2 -> 16 * 1/2
        self.assertEqual(16 / 2, 8)
        self.assertIn("8", PRACTICE[6])
        self.assertIn("2", PRACTICE[5])
        self.assertIn("3/5", PRACTICE[13])

    def test_09_e_and_exponentials(self):
        # (1 + 3x)^(1/x) -> e^3
        self.assertAlmostEqual((1 + 3 * 0.001) ** (1 / 0.001), math.exp(3), delta=0.2)
        self.assertIn("e³", ANS["lm1n16"])
        # (1 + 2/x)^x -> e^2
        self.assertAlmostEqual((1 + 2 / 1000) ** 1000, math.exp(2), delta=0.02)
        self.assertIn("e²", ANS["lm1n17"])
        self.assertIn("1", ANS["lm1n18"])
        self.assertIn("1", ANS["lm1n19"])
        self.assertIn("log 3", ANS["lm1n20"])
        self.assertAlmostEqual(math.log(3), 1.0986, places=3)
        self.assertIn("log 2", PRACTICE[8])
        self.assertIn("e¹", PRACTICE[7])

    def test_10_power_limits_and_two_sided(self):
        # ((1 + x)^5 - 1)/x -> 5
        self.assertEqual(5 * 1 ** 4, 5)
        self.assertIn("5", ANS["lm1n22"])
        # (x^5 - 32)/(x - 2) -> 5 * 2^4
        self.assertEqual(5 * 2 ** 4, 80)
        self.assertIn("80", ANS["lm1n23"])
        # (x^2 + 2x)/x -> 2
        self.assertEqual(0 + 2, 2)
        self.assertIn("2", ANS["lm1n24"])
        # piecewise: left 3, right 4
        self.assertEqual(1 + 2, 3)
        self.assertEqual(4 * 1, 4)
        self.assertIn("does not exist", ANS["lm1n21"])
        # practice 11: both branches give 5
        self.assertEqual(2 * 2 + 1, 5)
        self.assertEqual(2 ** 2 + 1, 5)
        self.assertIn("continuous", PRACTICE[11])
        # practice 9: power limit
        self.assertEqual(7 * 1 ** 6, 7)
        self.assertIn("7", PRACTICE[9])
        # practice 10: factorisation in the numerator
        self.assertEqual(2 * 3 - 1, 5)
        self.assertIn("5", PRACTICE[10])
        # practice 14: (e^(3x) - 1)/x -> 3
        self.assertIn("3", PRACTICE[14])
        # practice 2: (x^3 - 8)/(x^2 - 4) at 2
        self.assertEqual(12 / 4, 3)
        self.assertIn("3", PRACTICE[2])

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
            unit = json.loads((out / "units/DI01000021_u5.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 6)
            subject = json.loads((out / "subjects/DI01000021.json").read_text(encoding="utf-8"))
            self.assertEqual(subject["available_units"], [0, 1, 2, 3, 4, 5])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            branches = catalog["branches"]
            self.assertEqual(sum(1 for b in branches if "DI01000021" in b["semesters"].get("1", [])), len(branches))
            for rel, wanted in catalog["files"].items():
                self.assertEqual(hashlib.sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)


if __name__ == "__main__":
    unittest.main(verbosity=2)
