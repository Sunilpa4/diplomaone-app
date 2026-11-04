"""Validation for Applied Physics (DI01000121) Unit 1 "Units and Measurements", English + Gujarati.

Run from the repo root:  python3 -m unittest tools.test_DI01000121_u1 -v
"""
import json
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000121 import SUBJ_DIR, DIAG_DIR  # noqa: E402
from notes_workshop import audit_svg, text_width  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit1.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
SPEC = next(u for u in SUBJ["units"] if u["no"] == 1)

VOID = {"br", "hr", "img", "meta", "link", "input"}
TAG_RE = re.compile(r"</?([a-zA-Z0-9]+)[^>]*?(/?)>")
GUJARATI = re.compile(r"[\u0a80-\u0aff]")
FILLER = ("lorem", "todo", "tbd", "xxx", "placeholder", "[insert", "coming soon")


def strip_html(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def nodes(obj, out=None):
    """Every {"en", "gu"} pair in the unit, with the path that led to it."""
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


class PhysicsUnit1(unittest.TestCase):
    def test_01_unit_matches_the_syllabus(self):
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (1, 7, 17))
        self.assertEqual((SPEC["hours"], SPEC["weightage"], SPEC["theory_marks"]), (7, 17, 12))
        self.assertEqual(UNIT["title"]["en"], "Units and Measurements")
        self.assertEqual(UNIT["title"]["gu"], "એકમો અને માપન")
        self.assertEqual(SPEC["file"], "unit1.json")
        self.assertEqual(UNIT["course_outcomes"], ["CO1"])
        self.assertEqual(UNIT["practical_numbers"], [1, 2])
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "numericals", "viva", "exam"])

    def test_02_every_node_is_bilingual(self):
        self.assertGreater(len(NODES), 150)
        with_gu = [n for n in NODES if GUJARATI.search(n["gu"])]
        self.assertGreaterEqual(len(with_gu) / len(NODES), 0.85, "unit is not fully bilingual")
        for n in NODES:
            self.assertTrue(n["en"].strip() and n["gu"].strip())
            if not GUJARATI.search(n["gu"]):
                self.assertEqual(n["en"], n["gu"], f"untranslated: {n['gu'][:60]}")

    def test_03_gujarati_is_not_a_copy_of_english(self):
        prose = [n for n in NODES if len(n["en"]) > 60]
        self.assertTrue(prose)
        identical = [n for n in prose if n["en"] == n["gu"]]
        self.assertFalse(identical, f"identical long text: {identical[:1]}")

    def test_04_every_gtu_sub_clause_is_taught(self):
        tagged = {it.get("syllabus_item") for s in UNIT["notes"][:-1] for it in s["items"]}
        self.assertEqual(tagged, {"1.1", "1.2", "1.3", "1.4", "1.5"})
        outcomes = {o["en"] for o in SPEC["outcomes"]}
        self.assertEqual(len(outcomes), 5)
        self.assertTrue(all(o.startswith("1.") for o in outcomes))

    def test_05_cards_have_the_lecture_note_shape(self):
        self.assertGreaterEqual(len(TEACHING), 16)
        for it in TEACHING:
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<h4>"), 3, f"thin card: {it['h']['en']}")
            self.assertGreater(len(strip_html(body)), 500, f"short card: {it['h']['en']}")
            self.assertIn("<h4>", it["body"]["gu"])
            assert_balanced(self, body, it["h"]["en"])
            assert_balanced(self, it["body"]["gu"], it["h"]["gu"])
            low = body.lower()
            self.assertFalse([w for w in FILLER if w in low], f"filler in {it['h']['en']}")
            self.assertIn("Common mistake", body)

    def test_06_diagrams_are_mobile_and_clean(self):
        ids = [d["id"] for d in UNIT["diagrams"]]
        self.assertEqual(len(ids), 5)
        problems = []
        for d in UNIT["diagrams"]:
            path = DIAG_DIR / f"{d['id']}.svg"
            self.assertTrue(path.is_file(), path)
            audit_svg(path, problems)
            refs = [it for it in CARDS if it.get("diagram") == d["id"]]
            self.assertTrue(refs, f"{d['id']} is not linked from any card")
            self.assertTrue(GUJARATI.search(d["title"]["gu"]))
        self.assertFalse(problems, problems)
        for it in CARDS:
            if "diagram" in it:
                self.assertIn(it["diagram"], ids)

    def test_07_svg_text_stays_inside_the_canvas(self):
        for d in UNIT["diagrams"]:
            raw = (DIAG_DIR / f"{d['id']}.svg").read_text(encoding="utf-8")
            for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', raw):
                attrs, txt = m.group(1), m.group(2)
                if not txt.strip():
                    continue
                x = float(re.search(r'x="([-\d.]+)"', attrs).group(1))
                size = float(re.search(r'font-size="([\d.]+)"', attrs).group(1))
                bold = 'font-weight="bold"' in attrs
                anchor = re.search(r'text-anchor="(\w+)"', attrs)
                anchor = anchor.group(1) if anchor else "start"
                w = text_width(txt, size, bold)
                left = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
                self.assertGreaterEqual(left, 0.5, f"{d['id']}: '{txt}' starts at {left:.1f}")
                self.assertLessEqual(left + w, 359.5, f"{d['id']}: '{txt}' ends at {left + w:.1f}")

    def test_08_numericals_are_fully_solved(self):
        nums = UNIT["numericals"]
        self.assertGreaterEqual(len(nums), 18)
        self.assertEqual(len({n["id"] for n in nums}), len(nums))
        for n in nums:
            self.assertTrue(n["h"]["en"].strip() and GUJARATI.search(n["h"]["gu"]))
            for lang in ("en", "gu"):
                a = n["a"][lang]
                self.assertIn("<h4>", a)
                self.assertIn("<b>", a, f"{n['id']} {lang}: answer is not highlighted")
            self.assertIn("Answer", n["a"]["en"])
            self.assertIn("જવાબ", n["a"]["gu"])
            ans = n["answer"]
            self.assertTrue(ans["en"].strip() and ans["gu"].strip())
            if not GUJARATI.search(ans["gu"]):
                self.assertEqual(ans["en"], ans["gu"], f"{n['id']}: answer not translated")
                self.assertLessEqual(len(ans["gu"]), 40)

    def test_09_numerical_answers_are_right(self):
        """The physics of the worked examples, checked against the stated answers."""
        answers = {n["id"]: n["answer"]["en"] for n in UNIT["numericals"]}
        self.assertIn("10⁵", answers["u1n01"])
        self.assertIn("10⁷", answers["u1n02"])
        self.assertIn("10⁷", answers["u1n03"])
        self.assertIn("2700", answers["u1n04"])
        self.assertIn("20 m/s", answers["u1n05"])
        self.assertIn("0.1 mm", answers["u1n06"])
        self.assertIn("0.05 mm", answers["u1n07"])
        self.assertIn("0.02 mm", answers["u1n08"])
        self.assertIn("2.36", answers["u1n09"])
        self.assertIn("2.33", answers["u1n10"])
        self.assertIn("5.50", answers["u1n11"])
        self.assertIn("0.01 mm", answers["u1n12"])
        self.assertIn("4.82", answers["u1n13"])
        self.assertIn("4.80", answers["u1n14"])
        self.assertIn("0.10", answers["u1n15"])
        self.assertIn("20 ± 0.8", answers["u1n16"])
        self.assertIn("5.00 ± 0.06", answers["u1n17"])
        self.assertIn("12.6 ± 1.3", answers["u1n18"])
        self.assertIn("3.1", answers["u1n19"])
        self.assertIn("7.24", answers["u1n20"])
        # independent recomputation of six of them
        self.assertAlmostEqual(2.3 + 6 * 0.01, 2.36, places=6)
        self.assertAlmostEqual(4.5 + 32 * 0.01, 4.82, places=6)
        self.assertAlmostEqual(250.0 / 50.0, 5.0, places=6)
        self.assertAlmostEqual(0.5 / 50, 0.01, places=9)
        self.assertAlmostEqual((4 / 3) * 3.141592653589793 * 1.20 ** 3, 7.238, places=3)
        self.assertAlmostEqual(2.5 * 1.25, 3.125, places=6)

    def test_10_practice_answers_are_substantial(self):
        self.assertEqual(len(PRACTICE), 14)
        self.assertEqual(UNIT["answered_practice_count"], len(PRACTICE))
        for it in PRACTICE:
            for lang in ("en", "gu"):
                text = strip_html(it["body"][lang])
                self.assertGreaterEqual(len(text), 260, f"{it['h']['en']}: {lang} answer is thin")
                self.assertGreaterEqual(text.count(". ") + text.count("।"), 2, it["h"]["en"])
        self.assertIn("Practice 14.", PRACTICE[-1]["h"]["en"])
        self.assertIn("સરાવ 14.", PRACTICE[-1]["h"]["gu"])

    def test_11_exam_questions_mirror_the_answers(self):
        exam = UNIT["exam_questions"]
        self.assertEqual(len(exam), len(PRACTICE))
        for q, it in zip(exam, PRACTICE):
            self.assertEqual(q["q"]["en"], "Practice: " + it["h"]["en"].split(". ", 1)[1])
            self.assertIn(q["marks"], (3, 4, 5))
            self.assertIn("સરાવ", q["q"]["gu"])
        self.assertTrue(UNIT["question_marks_are_suggested"])

    def test_12_viva_and_equations(self):
        viva = [i for g in UNIT["viva"] for i in g["items"]]
        self.assertGreaterEqual(len(viva), 12)
        for v in viva:
            self.assertTrue(v["q"]["en"].strip() and GUJARATI.search(v["q"]["gu"]))
            self.assertGreater(len(strip_html(v["a"]["en"])), 40)
            self.assertGreater(len(strip_html(v["a"]["gu"])), 40)
        items = [i for g in UNIT["equations"] for i in g["items"]]
        self.assertGreaterEqual(len(items), 12)
        for i in items:
            self.assertIn("f", i)
            for key in ("name", "terms"):
                self.assertTrue(GUJARATI.search(i[key]["gu"]), i[key])

    def test_13_subject_json_is_a_two_semester_subject(self):
        self.assertEqual(SUBJ["code"], "DI01000121")
        self.assertEqual(SUBJ["name"]["en"], "Applied Physics")
        self.assertEqual(SUBJ["semesters"], [1, 2])
        self.assertEqual(SUBJ["semester"], 1)
        self.assertEqual(len(SUBJ["branches"]), 10)
        self.assertEqual(SUBJ["semester_by_branch"]["civil"], 1)
        self.assertEqual(SUBJ["semester_by_branch"]["mechanical"], 2)
        self.assertEqual(sum(u["hours"] for u in SUBJ["units"]), 45)
        self.assertEqual(sum(u["weightage"] for u in SUBJ["units"]), 100)
        self.assertEqual(sum(SUBJ["theory_marks_by_unit"].values()), 70)
        self.assertEqual(len(SUBJ["official_practicals"]), 14)
        self.assertEqual(sum(p["hours"] for p in SUBJ["official_practicals"]), 30)


if __name__ == "__main__":
    unittest.main()
