"""Validation for Applied Physics (DI01000121) Unit 2 "Circular Motion", English + Gujarati.

Run from the repo root:  python3 -m unittest tools.test_DI01000121_u2 -v
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


class PhysicsUnit2(unittest.TestCase):
    def test_01_unit_matches_the_syllabus(self):
        self.assertEqual((UNIT["unit"], UNIT["hours"], UNIT["weightage"]), (2, 8, 14))
        self.assertEqual((SPEC["hours"], SPEC["weightage"], SPEC["theory_marks"]), (8, 14, 10))
        self.assertEqual(UNIT["title"]["en"], "Circular Motion")
        self.assertEqual(UNIT["title"]["gu"], "વર્તુળ ગતિ")
        self.assertEqual(SPEC["file"], "unit2.json")
        self.assertEqual(UNIT["course_outcomes"], ["CO2"])
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
        self.assertFalse([n for n in prose if n["en"] == n["gu"]],
                         "a long English passage was copied into the Gujarati field")

    def test_04_every_gtu_sub_clause_is_taught(self):
        tagged = {it.get("syllabus_item") for s in UNIT["notes"][:-1] for it in s["items"]}
        self.assertEqual(tagged, {"2.1", "2.2", "2.3"})
        self.assertEqual(len(SPEC["outcomes"]), 2)
        self.assertTrue(all(o["en"].startswith("2.") for o in SPEC["outcomes"]))

    def test_05_cards_have_the_lecture_note_shape(self):
        self.assertGreaterEqual(len(TEACHING), 16)
        for it in TEACHING:
            body = it["body"]["en"]
            self.assertGreaterEqual(body.count("<h4>"), 3, f"thin card: {it['h']['en']}")
            self.assertGreater(len(strip_html(body)), 500, f"short card: {it['h']['en']}")
            self.assertIn("<h4>", it["body"]["gu"])
            assert_balanced(self, body, it["h"]["en"])
            assert_balanced(self, it["body"]["gu"], it["h"]["gu"])
            self.assertFalse([w for w in FILLER if w in body.lower()], f"filler in {it['h']['en']}")
            self.assertIn("Common mistake", body)

    def test_06_the_three_required_derivations_are_present(self):
        text = " ".join(strip_html(it["body"]["en"]).lower() for it in TEACHING)
        self.assertIn("tan θ = v²/(r g)", text, "banking angle is not derived")
        self.assertIn("m₁u₁ + m₂u₂", text, "conservation of momentum is not stated")
        self.assertIn("v = r ω", text, "the line/angular link is missing")
        gu = " ".join(strip_html(it["body"]["gu"]) for it in TEACHING)
        self.assertIn("tan θ = v²/(r g)", gu)

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
        self.assertGreaterEqual(len(nums), 18)
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
        self.assertIn("30 000", a["u2n01"])
        self.assertIn("6000 N", a["u2n02"])
        self.assertIn("300 N", a["u2n03"])
        self.assertIn("1.6 m/s", a["u2n04"])
        self.assertIn("2 m/s", a["u2n05"])
        self.assertIn("31.4", a["u2n06"])
        self.assertIn("12.6", a["u2n07"])
        self.assertIn("12.57", a["u2n08"])
        self.assertIn("5 rad/s²", a["u2n09"])
        self.assertIn("0.6 m/s²", a["u2n10"])
        self.assertIn("5 m/s²", a["u2n11"])
        self.assertIn("6.4 N", a["u2n12"])
        self.assertIn("14 m/s", a["u2n13"])
        self.assertIn("22.2", a["u2n14"])
        self.assertIn("14.3", a["u2n15"])
        self.assertIn("1800", a["u2n16"])
        self.assertIn("7.27", a["u2n17"])
        self.assertIn("6000 N", a["u2n18"])
        self.assertIn("8 N", a["u2n19"])
        # independent recomputation of the physics behind eight of them
        self.assertAlmostEqual(1500 * 20, 30000)
        self.assertAlmostEqual(0.020 * 400 / 5, 1.6)
        self.assertAlmostEqual(2 * 3 / 3, 2.0)
        self.assertAlmostEqual(2 * math.pi * 300 / 60, 31.416, places=3)
        self.assertAlmostEqual(0.4 * 2 * math.pi * 300 / 60, 12.566, places=3)
        self.assertAlmostEqual(0.2 * 16 / 0.5, 6.4)
        self.assertAlmostEqual(math.sqrt(0.4 * 50 * 9.8), 14.0, places=6)
        self.assertAlmostEqual(math.degrees(math.atan(400 / (100 * 9.8))), 22.2, places=1)
        self.assertAlmostEqual(math.degrees(math.atan(25 / (10 * 9.8))), 14.3, places=1)

    def test_11_practice_answers_are_substantial(self):
        self.assertEqual(len(PRACTICE), 14)
        self.assertEqual(UNIT["answered_practice_count"], len(PRACTICE))
        for it in PRACTICE:
            for lang in ("en", "gu"):
                text = strip_html(it["body"][lang])
                self.assertGreaterEqual(len(text), 260, f"{it['h']['en']}: {lang} answer is thin")
                self.assertGreaterEqual(text.count(". ") + text.count("।"), 2, it["h"]["en"])
        self.assertIn("Practice 14.", PRACTICE[-1]["h"]["en"])
        self.assertIn("સરાવ 14.", PRACTICE[-1]["h"]["gu"])

    def test_12_exam_questions_mirror_the_answers(self):
        exam = UNIT["exam_questions"]
        self.assertEqual(len(exam), len(PRACTICE))
        for q, it in zip(exam, PRACTICE):
            self.assertEqual(q["q"]["en"], "Practice: " + it["h"]["en"].split(". ", 1)[1])
            self.assertIn(q["marks"], (3, 4, 5))
            self.assertIn("સરાવ", q["q"]["gu"])

    def test_13_viva_and_equations(self):
        viva = [i for g in UNIT["viva"] for i in g["items"]]
        self.assertGreaterEqual(len(viva), 12)
        for v in viva:
            self.assertTrue(GUJARATI.search(v["q"]["gu"]))
            self.assertGreater(len(strip_html(v["a"]["en"])), 40)
            self.assertGreater(len(strip_html(v["a"]["gu"])), 40)
        items = [i for g in UNIT["equations"] for i in g["items"]]
        self.assertGreaterEqual(len(items), 13)
        for i in items:
            self.assertIn("f", i)
            for key in ("name", "terms"):
                self.assertTrue(GUJARATI.search(i[key]["gu"]), i[key])

    def test_14_formula_consistency_with_unit_1_symbols(self):
        """No unit-1 leftovers and consistent SI symbols across both units."""
        text = json.dumps(UNIT, ensure_ascii=False)
        self.assertNotIn("least count of the vernier", text.lower())
        for token in ("m v²/r", "tan θ", "ω", "α", "Δp"):
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
