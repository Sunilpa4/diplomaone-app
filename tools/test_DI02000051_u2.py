"""Validation for Environmental Sustainability (DI02000051) Unit 2, English + Gujarati.

Run from the repo root:  python3 -m unittest tools.test_DI02000051_u2 -v
"""
import json
import math
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI02000051 import SUBJ_DIR, DIAG_DIR, SUBJECT  # noqa: E402
from notes_workshop import audit_svg, text_width  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit2.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
SPEC = next(u for u in SUBJ["units"] if u["no"] == 2)

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")
GUJARATI = re.compile(r"[\u0a80-\u0aff]")
FILLER = ("lorem", "todo", "tbd", "xxx", "placeholder", "[insert", "coming soon")


def strip_html(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def nodes(obj, out=None):
    out = [] if out is None else out
    if isinstance(obj, dict):
        if "en" in obj and "gu" in obj and isinstance(obj["en"], str):
            out.append(obj)
        else:
            for v in obj.values():
                nodes(v, out)
    elif isinstance(obj, list):
        for v in obj:
            nodes(v, out)
    return out


NODES = nodes(UNIT)
CARDS = [it for s in UNIT["notes"] for it in s["items"]]
TEACHING = [it for s in UNIT["notes"][:-1] for it in s["items"]]
PRACTICE = UNIT["notes"][-1]["items"]


def assert_balanced(tc, html, where):
    stack = []
    for m in TAG_RE.finditer(html):
        tag, selfclose = m.group(1).lower(), m.group(2) == "/"
        if tag in VOID or selfclose:
            continue
        if m.group(0).startswith("</"):
            tc.assertTrue(stack and stack[-1] == tag, f"{where}: stray </{tag}>")
            if stack:
                stack.pop()
        else:
            stack.append(tag)
    tc.assertFalse(stack, f"{where}: unclosed {stack}")


class EnvironmentalUnit2(unittest.TestCase):
    def test_01_unit_matches_the_syllabus(self):
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (2, 7, 25))
        self.assertEqual((SPEC["hours"], SPEC["weightage"], SPEC["theory_marks"]), (7, 25, 17))
        self.assertEqual(UNIT["title"]["en"], "Waste Management and Pollution Control")
        self.assertEqual(SPEC["file"], "unit2.json")
        self.assertEqual(UNIT["course_outcomes"], ["CO2"])
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "numericals", "viva", "exam"])

    def test_02_subject_scheme_is_copied_from_the_pdf(self):
        self.assertEqual(SUBJ["code"], "DI02000051")
        self.assertEqual(SUBJ["branch"], "common")
        self.assertTrue(SUBJ["common_to_all_branches"])
        self.assertEqual(SUBJ["semester"], 2)
        self.assertEqual(SUBJ["category"], "Engineering Science (ESC)")
        self.assertEqual(SUBJ["teaching"], {"lecture": 2, "tutorial": 0, "practical": 0})
        self.assertEqual(SUBJ["exam"]["theory_ese"], 70)
        self.assertEqual(SUBJ["exam"]["theory_pa"], 30)
        self.assertEqual(SUBJ["exam"]["total"], 100)
        self.assertEqual(SUBJ["exam"]["credits"], 2)
        self.assertEqual(SUBJ["total_hours"], 30)
        self.assertEqual(sum(u["hours"] for u in SUBJ["units"]), 30)
        self.assertEqual(sum(u["weightage"] for u in SUBJ["units"]), 100)
        self.assertEqual(sum(u["theory_marks"] for u in SUBJ["units"]), 70)
        self.assertEqual(len(SUBJ["course_outcomes"]), 5)
        self.assertEqual(SUBJ["official_practicals"], [])
        self.assertEqual(SUBJ["source_pdf_sha256"],
                         "4d965bae1e7a2bc0e64bfebf2cd74fc5de59204228abcc767a9bd0ffc583c821")

    def test_03_every_node_is_bilingual(self):
        self.assertGreater(len(NODES), 100)
        with_gu = [n for n in NODES if GUJARATI.search(n["gu"])]
        self.assertGreaterEqual(len(with_gu) / len(NODES), 0.85, "unit is not fully bilingual")
        for n in NODES:
            self.assertTrue(n["en"].strip() and n["gu"].strip())
            if not GUJARATI.search(n["gu"]):
                self.assertEqual(n["en"], n["gu"], f"untranslated: {n['gu'][:60]}")

    def test_04_gujarati_is_not_a_copy_of_english(self):
        prose = [n for n in NODES if len(n["en"]) > 60]
        self.assertTrue(prose)
        self.assertFalse([n for n in prose if n["en"] == n["gu"]],
                         "a long English passage was copied into the Gujarati field")

    def test_05_every_gtu_clause_is_taught(self):
        tagged = {it.get("syllabus_item") for s in UNIT["notes"][:-1] for it in s["items"]}
        self.assertEqual(tagged, {"2.1", "2.2", "2.3", "2.4", "2.5"})
        # each clause of the syllabus text is represented by a card with that tag
        for clause in ("2.1", "2.2", "2.3", "2.4", "2.5"):
            self.assertGreaterEqual(len([1 for it in TEACHING if it.get("syllabus_item") == clause]),
                                    1)

    def test_06_cards_have_the_lecture_note_shape(self):
        self.assertGreaterEqual(len(TEACHING), 9)
        for it in TEACHING:
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<h4>"), 3, f"thin card: {it['h']['en']}")
            self.assertGreater(len(strip_html(body)), 600, f"short card: {it['h']['en']}")
            self.assertIn("<h4>", it["body"]["gu"])
            assert_balanced(self, body, it["h"]["en"])
            assert_balanced(self, it["body"]["gu"], it["h"]["gu"])
            self.assertFalse([w for w in FILLER if w in body.lower()], f"filler in {it['h']['en']}")

    def test_07_the_required_ideas_are_present(self):
        text = " ".join(strip_html(it["body"]["en"]).lower() for it in TEACHING)
        for phrase in ("bod", "cod", "tss", "turbidity", "cyclone", "electrostatic",
                       "activated sludge", "leachate", "decibel", "microplastic", "e-waste"):
            self.assertIn(phrase, text, f"missing: {phrase}")
        gu = " ".join(strip_html(it["body"]["gu"]) for it in TEACHING)
        for phrase in ("સાયક્લોન", "એક્ટિવેટેડ સ્લજ", "લીચેટ", "માઇક્રોપ્લાસ્ટિક", "ઇ-કચરો", "ઘોંઘાટ"):
            self.assertIn(phrase, gu, f"missing in Gujarati: {phrase}")

    def test_08_every_diagram_exists_and_is_linked(self):
        listed = {d["id"] for d in UNIT["diagrams"]}
        self.assertEqual(len(listed), 6)
        linked = {it["diagram"] for it in CARDS if it.get("diagram")}
        self.assertEqual(listed, linked, "a diagram is listed but not shown in a card")
        for d in UNIT["diagrams"]:
            self.assertEqual(d["title"]["en"], d["title"]["en"].strip())
            self.assertTrue(d["caption"]["gu"].strip())
            path = DIAG_DIR / f"{d['id']}.svg"
            self.assertTrue(path.is_file(), f"missing SVG {path.name}")
            problems = []
            audit_svg(path, problems)
            self.assertFalse(problems, problems)
            raw = path.read_text(encoding="utf-8")
            self.assertIn('viewBox="0 0 360', raw)
            for bad in ("<script", "<style", "<image", "href="):
                self.assertNotIn(bad, raw)

    def test_09_diagram_labels_are_measured(self):
        """Re-measure every label with the app font; nothing may overflow the 360 px canvas."""
        for d in UNIT["diagrams"]:
            raw = (DIAG_DIR / f"{d['id']}.svg").read_text(encoding="utf-8")
            self.assertLess(len(d["title"]["en"]), 52, "title longer than the canvas allows")
            for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*font-size="([\d.]+)"'
                                 r'(?:[^>]*font-weight="([^"]+)")?[^>]*>([^<]+)</text>', raw):
                x, y, size, weight = float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)
                txt = m.group(5)
                bold = weight in ("bold", "700")
                width = text_width(txt, size, bold)
                anchor = "middle" if 'text-anchor="middle"' in m.group(0) else (
                    "end" if 'text-anchor="end"' in m.group(0) else "start")
                left = x - width / 2 if anchor == "middle" else (x - width if anchor == "end" else x)
                self.assertGreaterEqual(left, 0.5, f"{d['id']}: '{txt}' off the left edge")
                self.assertLessEqual(left + width, 359.5, f"{d['id']}: '{txt}' off the right edge")

    def test_10_numericals_are_solved_and_answered(self):
        nums = UNIT["numericals"]
        self.assertEqual(len(nums), 10)
        for n in nums:
            self.assertTrue(n["id"].startswith("u2n"))
            self.assertIn("<h4>Step-by-step solution</h4>", n["a"]["en"])
            self.assertIn("<h4>જવાબ</h4>", n["a"]["gu"])
            self.assertIn(n["answer"]["en"], n["a"]["en"])
            self.assertIn(n["answer"]["gu"], n["a"]["gu"])

    def test_11_numerical_values_are_recomputed(self):
        got = {n["id"]: n["answer"]["en"] for n in UNIT["numericals"]}
        self.assertEqual(got["u2n01"], "300 mg/L")
        self.assertAlmostEqual((8.0 - 3.0) / (5 / 300), 300, places=6)
        self.assertEqual(got["u2n02"], "350 mg/L")
        self.assertAlmostEqual((10.0 - 6.5) * 0.25 * 8000 / 20, 350, places=6)
        self.assertIn("0.60", got["u2n03"])
        self.assertAlmostEqual(240 / 400, 0.6, places=6)
        self.assertEqual(got["u2n04"], "521 mg/L")
        self.assertAlmostEqual((0.4521 - 0.4000) * 1000 / 0.1, 521, places=1)
        self.assertIn("73 dB", got["u2n05"])
        self.assertIn("74.8 dB", got["u2n05"])
        self.assertAlmostEqual(70 + 10 * math.log10(2), 73.01, places=2)
        self.assertAlmostEqual(70 + 10 * math.log10(3), 74.77, places=2)
        self.assertIn("82.4 dB", got["u2n06"])
        self.assertAlmostEqual(10 * math.log10((4 * 10 ** 8.5 + 4 * 10 ** 7.5) / 8), 82.4, places=1)
        self.assertIn("225 t", got["u2n07"])
        self.assertIn("34 ha", got["u2n07"])
        self.assertAlmostEqual(500_000 * 0.45 / 1000, 225, places=6)
        self.assertAlmostEqual(225 * 365 * 20 / 0.6 / 8 / 10_000, 34.2, places=1)
        self.assertEqual(got["u2n08"], "95 %")
        self.assertAlmostEqual((12 - 0.6) / 12 * 100, 95, places=6)
        self.assertIn("7.2 t", got["u2n09"])
        self.assertAlmostEqual(225 * 0.08 * 0.4, 7.2, places=6)
        self.assertAlmostEqual(225 * 0.08 * 0.6, 10.8, places=6)
        self.assertIn("3.2 kg", got["u2n10"])
        self.assertAlmostEqual(1_200_000 * 0.03 * 0.3 / 1000, 10.8, places=3)
        self.assertAlmostEqual(10_800 * 0.3 / 1000, 3.24, places=2)

    def test_12_equations_and_viva_are_complete(self):
        names = [i["name"]["en"] for g in UNIT["equations"] for i in g["items"]]
        self.assertGreaterEqual(len(names), 8)
        self.assertIn("BOD by dilution", names)
        self.assertIn("Equivalent level", names)
        for g in UNIT["equations"]:
            self.assertTrue(g["title"]["gu"].strip())
            for i in g["items"]:
                self.assertTrue(i["f"].strip())
                self.assertTrue(i["terms"]["gu"].strip())
        viva = [i for g in UNIT["viva"] for i in g["items"]]
        self.assertGreaterEqual(len(viva), 14)
        for v in viva:
            self.assertGreater(len(strip_html(v["a"]["en"])), 80, v["q"]["en"])
            self.assertTrue(GUJARATI.search(v["a"]["gu"]), v["q"]["en"])

    def test_13_practice_questions_have_model_answers(self):
        self.assertEqual(len(UNIT["exam_questions"]), len(PRACTICE))
        self.assertGreaterEqual(len(PRACTICE), 12)
        self.assertEqual(UNIT["answered_practice_count"], len(PRACTICE))
        self.assertEqual(UNIT["lesson_count"], len(TEACHING))
        for q, it in zip(UNIT["exam_questions"], PRACTICE):
            self.assertTrue(it["h"]["en"].startswith(f"Practice {PRACTICE.index(it) + 1}."))
            self.assertTrue(q["q"]["en"].startswith("Practice: "))
            self.assertIn(q["marks"], (3, 4, 5))
            body = it["body"]
            self.assertGreaterEqual(len(strip_html(body["en"])), 270, it["h"]["en"])
            self.assertGreaterEqual(len(strip_html(body["gu"])), 260, it["h"]["gu"])
            self.assertTrue(GUJARATI.search(body["gu"]))
            assert_balanced(self, body["en"], it["h"]["en"])
            assert_balanced(self, body["gu"], it["h"]["gu"])

    def test_14_the_unit_is_registered_and_marked_available(self):
        self.assertEqual(SUBJ["units"][1]["title"]["en"], UNIT["title"]["en"])
        self.assertEqual(SUBJECT["code"], "DI02000051")
        self.assertEqual(len(SUBJECT["units"]), 5)
        self.assertFalse([u for u in SUBJ["units"] if u["no"] == 2 and u["file"] != "unit2.json"])
        self.assertEqual(UNIT["official"], True)
        self.assertEqual(UNIT["practical_numbers"], [])
        self.assertTrue(UNIT["question_marks_are_suggested"])
        self.assertIn("not official", UNIT["question_provenance"].lower())
        self.assertTrue(UNIT["sources"])
        for s in UNIT["sources"]:
            self.assertTrue(s["url"].startswith("http"), s)


if __name__ == "__main__":
    unittest.main(verbosity=2)
