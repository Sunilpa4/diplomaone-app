"""Validation for Cloud Computing (DI04000041) Unit 1.

Run from the repo root:  python3 -m unittest tools.test_DI04000041_u1 -v
"""
import json
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI04000041 import SUBJ_DIR, DIAG_DIR, TABS  # noqa: E402
from notes_workshop import audit_svg, text_width  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit1.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")


def strip_html(html):
    return re.sub(r"<[^>]+>", " ", html)


def all_text(obj):
    """Every English string in the unit, HTML stripped - the greppable corpus."""
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


class CloudUnit1(unittest.TestCase):
    def test_01_syllabus_identity_and_scheme(self):
        self.assertEqual((SUBJ["code"], SUBJ["semester"], SUBJ["syllabus_year"]),
                         ("DI04000041", 4, "2025-26"))
        self.assertEqual(SUBJ["category"], "Professional Elective - I")
        self.assertEqual(SUBJ["teaching"], {"lecture": 3, "tutorial": 0, "practical": 2})
        self.assertEqual(SUBJ["exam"], {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20,
                                        "practical_ese": 30, "total": 150, "credits": 4})
        self.assertEqual([u["hours"] for u in SUBJ["units"]], [6, 10, 9, 10, 10])
        self.assertEqual([u["weightage"] for u in SUBJ["units"]], [17, 23, 19, 24, 17])
        self.assertEqual(sum(u["hours"] for u in SUBJ["units"]), 45)
        self.assertEqual(sum(u["weightage"] for u in SUBJ["units"]), 100)
        self.assertEqual(len(SUBJ["course_outcomes"]), 5)
        self.assertEqual(len(SUBJ["practicals"]), 15)
        self.assertEqual(SUBJ["theory_rbt_percent"],
                         {"remember": 42, "understand": 58, "apply": 0, "analyze": 0,
                          "evaluate": 0, "create": 0})
        self.assertIn("2025-26", (ROOT / "tools/syllabus_DI04000041.txt").read_text(encoding="utf-8"))

    def test_02_unit_one_installed_and_listed(self):
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (1, 6, 17))
        self.assertEqual(UNIT["title"]["en"], SUBJ["units"][0]["title"]["en"])
        self.assertEqual(SUBJ["units"][0]["file"], "unit1.json")
        self.assertIsNone(SUBJ["units"][1]["file"], "unit 2 must not be advertised before it exists")
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
        self.assertEqual(len(UNIT["notes"]), 8)
        self.assertEqual(sum(len(s["items"]) for s in UNIT["notes"]), 32)
        self.assertEqual(len(UNIT["diagrams"]), 7)
        self.assertEqual(len(UNIT["numericals"]), 8)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["viva"]), 23)
        self.assertEqual(len(UNIT["exam_questions"]), 12)
        self.assertEqual(sum(len(g["items"]) for g in UNIT["equations"]), 17)
        self.assertEqual(UNIT["lesson_count"], 20)
        self.assertEqual(UNIT["answered_practice_count"], 12)

    def test_05_unit_one_syllabus_coverage(self):
        for word in ["definition", "central ideas", "characteristics", "challenges", "novel applications",
                     "security risks", "advantages and disadvantages", "on-demand self-service",
                     "broad network access", "resource pooling", "rapid elasticity", "measured service",
                     "multi-tenancy", "vendor lock-in", "data-residency", "shared responsibility",
                     "green-hydrogen", "predictive maintenance", "misconfiguration", "egress"]:
            self.assertTrue(word in TEXT, f"unit 1 misses: {word}")

    def test_06_characteristics_are_complete_and_attributed(self):
        for char in ["On-demand self-service", "Broad network access", "Resource pooling",
                     "Rapid elasticity", "Measured service"]:
            self.assertIn(char.lower(), TEXT)
        self.assertIn("four out of five is hosting", TEXT)
        self.assertIn('not the same as "unlimited"', TEXT)
        self.assertEqual([d["title"]["en"] for d in UNIT["diagrams"]].count("Five essential characteristics"), 1)

    def test_07_numericals_recompute(self):
        answers = {n["id"]: n["a"]["en"] for n in UNIT["numericals"]}
        # n1: 99.9 % of a 365-day year
        year = 525_600
        self.assertAlmostEqual(0.001 * year, 525.6, places=6)
        self.assertIn("525.6", answers["cc1n1"])
        self.assertIn("8.76", answers["cc1n1"])
        # n2: 99.95 % of a 30-day month
        month = 43_200
        self.assertAlmostEqual(0.0005 * month, 21.6, places=6)
        self.assertIn("21.6", answers["cc1n2"])
        # n3: the five-row table
        for pct, expected in ((0.01, "432"), (0.005, "216"), (0.001, "43.2"), (0.0005, "21.6"), (0.0001, "4.32")):
            self.assertAlmostEqual(pct * month, float(expected), places=6)
            self.assertIn(expected, answers["cc1n3"])
        # n4: break-even
        self.assertEqual(90_000 / (8_000 - 3_000), 18)
        self.assertIn("18 months", answers["cc1n4"])
        # n5: 4 TB growing 25 % for two years at 1.50 per GB-month
        volume_tb = 4 * 1.25 ** 2
        self.assertAlmostEqual(volume_tb, 6.25)
        self.assertEqual(round(volume_tb * 1000 * 1.50), 9375)
        self.assertIn("9,375", answers["cc1n5"])
        # n6: 1.5 TB egress at 4.20 per GB
        self.assertEqual(round(1500 * 4.20), 6300)
        self.assertEqual(round(1500 * 4.20 * 12), 75600)
        self.assertIn("6,300", answers["cc1n6"])
        self.assertIn("75,600", answers["cc1n6"])
        # n7: consolidation with 40 % headroom
        used = 8 * 8 * 0.12
        self.assertAlmostEqual(used, 7.68)
        self.assertEqual(-(-used * 1.4 // 1) >= 10.75, True)
        self.assertIn("7.68", answers["cc1n7"])
        self.assertIn("12 vCPU", answers["cc1n7"])
        # n8: telemetry
        per_day = 2000 * 1440
        self.assertEqual(per_day, 2_880_000)
        self.assertAlmostEqual(per_day * 8 / 1e6, 23.04, places=6)
        self.assertAlmostEqual(per_day * 8 * 30 / 1e6, 691.2, places=6)
        self.assertAlmostEqual(0.6912 * 1.50, 1.0368, places=4)
        self.assertIn("23.04 MB", answers["cc1n8"])
        self.assertIn("691.2 MB", answers["cc1n8"])

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
        # independent re-check of the widest label of every diagram, with the real font metrics
        for d in UNIT["diagrams"]:
            root = ET.fromstring((DIAG_DIR / f"{d['id']}.svg").read_text(encoding="utf-8"))
            for node in root.iter("{http://www.w3.org/2000/svg}text"):
                txt = "".join(node.itertext())
                if not txt:
                    continue
                size = float(node.get("font-size", "12"))
                bold = (node.get("font-weight") or "normal") == "bold"
                self.assertLess(text_width(txt, size, bold), 360 - 2, f"{d['id']}: {txt!r} is wider than the canvas")

    def test_10_links_resolve_both_ways(self):
        num_ids = {n["id"] for n in UNIT["numericals"]}
        used_examples = {e for s in UNIT["notes"] for it in s["items"] for e in it.get("examples", [])}
        self.assertEqual(used_examples, num_ids, "every numerical should be reachable from a card")
        for card in (it for s in UNIT["notes"] for it in s["items"]):
            if "examples" in card:
                for e in card["examples"]:
                    self.assertIn(e, num_ids)

    def test_11_practice_matches_exam_questions(self):
        practice = UNIT["notes"][-1]
        self.assertEqual(practice["title"]["en"].startswith("8."), True)
        self.assertEqual(len(practice["items"]), len(UNIT["exam_questions"]))
        for i, (item, exam) in enumerate(zip(practice["items"], UNIT["exam_questions"]), 1):
            question = exam["q"]["en"].replace("Practice: ", "")
            self.assertEqual(item["h"]["en"], f"Practice {i}. {question}")
            self.assertIn(exam["marks"], (3, 4, 7))
            self.assertGreater(len(item["body"]["en"]), 200, "model answer is too thin")
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
                assert_balanced(self, (e.get("terms") or e.get("a"))["en"], "reference/viva")

    def test_13_equation_tab_is_a_formula_sheet(self):
        for group in UNIT["equations"]:
            self.assertTrue(group["items"])
            for item in group["items"]:
                self.assertLess(len(item["f"]), 60, "an equation 'f' should stay a one-line formula or rule")
                self.assertTrue(item["terms"]["en"])

    def test_14_export_carries_the_unit(self):
        import subprocess
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            r = subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                               cwd=ROOT, text=True, capture_output=True, timeout=120)
            self.assertEqual(r.returncode, 0, r.stderr)
            unit = json.loads((out / "units/DI04000041_u1.json").read_text(encoding="utf-8"))
            self.assertEqual(len(unit["svgs"]), 7)
            self.assertEqual(unit["tabs"], TABS)
            subject = json.loads((out / "subjects/DI04000041.json").read_text(encoding="utf-8"))
            self.assertEqual(subject["available_units"], [1])
            catalog = json.loads((out / "catalog.json").read_text(encoding="utf-8"))
            self.assertEqual(catalog["subjects"]["DI04000041"]["status"], "available")
            self.assertEqual(catalog["subjects"]["DI04000041"]["units"], 5)
            computer = next(b for b in catalog["branches"] if b["key"] == "computer")
            self.assertIn("DI04000041", computer["semesters"]["4"])
            # every hash in the catalog must match the bytes on disk
            for rel, wanted in catalog["files"].items():
                self.assertEqual(__import__("hashlib").sha1((out / rel).read_bytes()).hexdigest()[:12], wanted)

    def test_15_expansion_does_not_disturb_existing_units(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "data"
            import subprocess
            subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out)],
                           cwd=ROOT, check=True, capture_output=True, timeout=120)
            units = list((out / "units").glob("*_u*.json"))
            self.assertGreaterEqual(len(units), 294)
            before = (out / "units/DI05007021_u1.json").read_bytes()
            # rebuilding this subject must not touch another subject's bytes
            subprocess.run([sys.executable, "tools/build_DI04000041_u1.py"], cwd=ROOT,
                           check=True, capture_output=True, timeout=120)
            out2 = Path(td) / "data2"
            subprocess.run([sys.executable, "tools/export_app_content.py", "--out", str(out2)],
                           cwd=ROOT, check=True, capture_output=True, timeout=120)
            self.assertEqual((out2 / "units/DI05007021_u1.json").read_bytes(), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
