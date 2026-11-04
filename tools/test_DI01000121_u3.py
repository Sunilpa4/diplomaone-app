"""Validation for Applied Physics (DI01000121) Unit 3 "General Properties of Matter", English + Gujarati.

Run from the repo root:  python3 -m unittest tools.test_DI01000121_u3 -v
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

from subject_DI01000121 import SUBJ_DIR, DIAG_DIR  # noqa: E402
from notes_workshop import audit_svg, text_width  # noqa: E402

UNIT = json.loads((SUBJ_DIR / "unit3.json").read_text(encoding="utf-8"))
SUBJ = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
SPEC = next(u for u in SUBJ["units"] if u["no"] == 3)

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


class PhysicsUnit3(unittest.TestCase):
    def test_01_unit_matches_the_syllabus(self):
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (3, 12, 28))
        self.assertEqual((SPEC["hours"], SPEC["weightage"], SPEC["theory_marks"]), (12, 28, 19))
        self.assertEqual(UNIT["title"]["en"], "General Properties of Matter")
        self.assertEqual(UNIT["title"]["gu"], "દ્રવ્યના સામાન્ય ગુણધર્મો")
        self.assertEqual(SPEC["file"], "unit3.json")
        self.assertEqual(UNIT["course_outcomes"], ["CO3"])
        self.assertEqual(UNIT["tabs"], ["notes", "diagrams", "equations", "numericals", "viva", "exam"])
        self.assertEqual(UNIT["practical_numbers"], [4, 5, 6])

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
        self.assertFalse([n for n in prose if n["en"] == n["gu"]],
                         "a long English passage was copied into the Gujarati field")

    def test_04_every_gtu_sub_clause_is_taught(self):
        tagged = {it.get("syllabus_item") for s in UNIT["notes"][:-1] for it in s["items"]}
        required = {"3.1.1", "3.1.2", "3.1.3", "3.1.4", "3.1.5",
                    "3.2.1", "3.2.2", "3.2.3", "3.2.4", "3.2.5", "3.2.6", "3.2.7", "3.2.8",
                    "3.3.1", "3.3.2", "3.3.3", "3.3.4", "3.3.5", "3.3.6"}
        self.assertEqual(required - tagged, set(), "a GTU sub-clause has no card")
        self.assertTrue(all(t.startswith("3.") for t in tagged), tagged)
        self.assertEqual(len(SPEC["outcomes"]), 5, "3.a to 3.e")
        self.assertTrue(all(o["en"].startswith("3.") for o in SPEC["outcomes"]))

    def test_05_cards_have_the_lecture_note_shape(self):
        self.assertGreaterEqual(len(TEACHING), 20)
        for it in TEACHING:
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<h4>"), 3, f"thin card: {it['h']['en']}")
            self.assertGreater(len(strip_html(body)), 500, f"short card: {it['h']['en']}")
            self.assertIn("<h4>", it["body"]["gu"])
            assert_balanced(self, body, it["h"]["en"])
            assert_balanced(self, it["body"]["gu"], it["h"]["gu"])
            self.assertFalse([w for w in FILLER if w in body.lower()], f"filler in {it['h']['en']}")
            self.assertIn("Common mistake", body)
            self.assertIn("સામાન્ય ભૂલ", it["body"]["gu"])

    def test_06_the_required_formulas_are_present(self):
        text = " ".join(strip_html(it["body"]["en"]).lower() for it in TEACHING)
        self.assertIn("h = 2t cos θ / (ρ g r)", text, "the Ascent formula is missing")
        self.assertIn("6π η r v", text, "Stokes' law is missing")
        self.assertIn("2r²(ρ − σ)g/(9η)", text, "terminal velocity is missing")
        self.assertIn("y = (f/a)/(δl/l)", text, "Young's modulus is not defined")
        self.assertIn("re = ρ v d / η", text, "the Reynolds number is missing")
        gu = " ".join(strip_html(it["body"]["gu"]) for it in TEACHING)
        self.assertIn("h = 2t cos θ / (ρ g r)", gu.lower())

    def test_07_diagrams_are_mobile_and_clean(self):
        ids = [d["id"] for d in UNIT["diagrams"]]
        self.assertEqual(len(ids), 5)
        problems = []
        for d in UNIT["diagrams"]:
            path = DIAG_DIR / f"{d['id']}.svg"
            self.assertTrue(path.is_file(), path)
            audit_svg(path, problems)
            self.assertTrue([it for it in CARDS if it.get("diagram") == d["id"]],
                            f"{d['id']} is not linked from any card")
            self.assertTrue(GUJARATI.search(d["title"]["gu"]))
            self.assertTrue(GUJARATI.search(d["caption"]["gu"]))
        self.assertFalse(problems, problems)
        for it in CARDS:
            if "diagram" in it:
                self.assertIn(it["diagram"], ids)

    def test_08_svg_text_stays_inside_the_canvas(self):
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

    def test_09_numericals_are_fully_solved(self):
        nums = UNIT["numericals"]
        self.assertGreaterEqual(len(nums), 24)
        self.assertEqual(len({n["id"] for n in nums}), len(nums))
        for n in nums:
            self.assertTrue(GUJARATI.search(n["h"]["gu"]))
            for lang in ("en", "gu"):
                a = n["a"][lang]
                self.assertIn("<h4>", a)
                self.assertIn("<b>", a)
            self.assertIn("Answer", n["a"]["en"])
            self.assertIn("જવાબ", n["a"]["gu"])
            ans = n["answer"]
            if not GUJARATI.search(ans["gu"]):
                self.assertEqual(ans["en"], ans["gu"], f"{n['id']}: answer not translated")
                self.assertLessEqual(len(ans["gu"]), 40)

    def test_10_numerical_answers_are_right(self):
        a = {n["id"]: n["answer"]["en"] for n in UNIT["numericals"]}
        self.assertIn("5 × 10⁷", a["u3n01"])
        self.assertIn("2.5 × 10⁻⁴", a["u3n02"])
        self.assertIn("2 × 10¹¹", a["u3n03"])
        self.assertIn("0.5 mm", a["u3n04"])
        self.assertIn("2 × 10⁹", a["u3n05"])
        self.assertIn("5 × 10⁵", a["u3n06"])
        self.assertIn("1.25 × 10⁻²", a["u3n07"])
        self.assertIn("5 × 10⁻³", a["u3n08"])
        self.assertIn("7.35 cm", a["u3n09"])
        self.assertIn("2.94", a["u3n10"])
        self.assertIn("0.0735", a["u3n11"])
        self.assertIn("5 Pa", a["u3n12"])
        self.assertIn("125 N", a["u3n13"])
        self.assertIn("1.72", a["u3n14"])
        self.assertIn("0.57", a["u3n15"])
        self.assertIn("10⁵", a["u3n16"])
        self.assertIn("0.04 m/s", a["u3n17"])
        self.assertIn("500 N/m", a["u3n18"])
        self.assertIn("144 Pa", a["u3n19"])
        self.assertIn("500 N", a["u3n20"])
        self.assertIn("2.7 cm", a["u3n21"])
        self.assertIn("1000 N", a["u3n22"])
        self.assertIn("2.5 × 10⁻⁴", a["u3n23"])
        self.assertIn("2 mm", a["u3n24"])
        # independent recomputation of the physics behind ten of them
        self.assertAlmostEqual(100 / (2e-6), 5e7)
        self.assertAlmostEqual(5e7 / 2.5e-4, 2e11)
        self.assertAlmostEqual(50 * 2 / (1e-6 * 2e11), 5e-4)
        self.assertAlmostEqual(0.5 * 50 * 5e-4, 0.0125)
        self.assertAlmostEqual(2 * 0.072 / (1000 * 9.8 * 2e-4), 0.073469, places=6)
        self.assertAlmostEqual(0.144 / (1000 * 9.8 * 0.05), 2.9388e-4, places=7)
        self.assertAlmostEqual(2 * 1e-6 * 6540 * 9.8 / (9 * 0.83), 1.72e-2, places=4)
        self.assertAlmostEqual(2 * 4e-6 * 6540 * 9.8 / (9 * 0.1), 0.5697, places=4)
        self.assertAlmostEqual(2 * 0.465 * math.cos(math.radians(140)) / (13600 * 9.8 * 2e-4),
                               -0.02673, places=5)
        self.assertAlmostEqual(100e6 * 10e-6, 1000.0)

    def test_11_practice_answers_are_substantial(self):
        self.assertEqual(len(PRACTICE), 16)
        self.assertEqual(UNIT["answered_practice_count"], len(PRACTICE))
        for it in PRACTICE:
            for lang in ("en", "gu"):
                text = strip_html(it["body"][lang])
                self.assertGreaterEqual(len(text), 260, f"{it['h']['en']}: {lang} answer is thin")
                self.assertGreaterEqual(text.count(". ") + text.count("।"), 2, it["h"]["en"])
        self.assertIn("Practice 16.", PRACTICE[-1]["h"]["en"])
        self.assertIn("સરાવ 16.", PRACTICE[-1]["h"]["gu"])

    def test_12_exam_questions_mirror_the_answers(self):
        exam = UNIT["exam_questions"]
        self.assertEqual(len(exam), len(PRACTICE))
        total = 0
        for q, it in zip(exam, PRACTICE):
            self.assertEqual(q["q"]["en"], "Practice: " + it["h"]["en"].split(". ", 1)[1])
            self.assertIn(q["marks"], (3, 4, 5))
            total += q["marks"]
            self.assertIn("સરાવ", q["q"]["gu"])
        self.assertGreaterEqual(total, 56)

    def test_13_viva_and_equations(self):
        viva = [i for g in UNIT["viva"] for i in g["items"]]
        self.assertGreaterEqual(len(viva), 16)
        for v in viva:
            self.assertTrue(GUJARATI.search(v["q"]["gu"]))
            self.assertGreater(len(strip_html(v["a"]["en"])), 40)
            self.assertGreater(len(strip_html(v["a"]["gu"])), 40)
        items = [i for g in UNIT["equations"] for i in g["items"]]
        self.assertGreaterEqual(len(items), 18)
        for i in items:
            self.assertIn("f", i)
            for key in ("name", "terms"):
                self.assertTrue(GUJARATI.search(i[key]["gu"]), i[key])

    def test_14_units_and_symbols_are_consistent(self):
        text = json.dumps(UNIT, ensure_ascii=False)
        self.assertIn("Pa·s", text)
        self.assertIn("N/m²", text)
        self.assertIn("poise", text)
        self.assertNotIn("TODO", text)
        self.assertNotIn("undefined", text)


if __name__ == "__main__":
    unittest.main()
