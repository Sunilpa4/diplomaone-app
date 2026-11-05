"""Build Engineering Materials Science (DI01000181) Unit 1 - bilingual, with eight figures."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000181 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI01000181_u1_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI01000181_u1 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


CAPTIONS_GU = {
    "u1_class": "ઇજનેરી સામગ્રીનું વર્ગીકરણ",
    "u1_select": "વજન દીઠ તાકાત પરથી પસંદગી",
    "u1_bonds": "બંધનના પાંચ પ્રકાર",
    "u1_bondenergy": "બંધનની તાકાત ગલનબિંદુ નક્કી કરે",
    "u1_cells": "BCC, FCC અને HCP unit cells",
    "u1_packing": "ચાર રચનાનું packing fraction",
    "u1_stress": "Tensile test અને તેના ગુણધર્મો",
    "u1_thermal": "Thermal અને electrical ગુણધર્મો",
}

CAPTIONS_GU_TAIL = {
    "u1_class": "ચાર કુટુંબ લગભગ દરેક machine part આવરે છે - ધાતુ, ceramics, polymers અને "
                "composites; semiconductors અને smart materials તેમાંના બે નવા ઉમેરા છે.",
    "u1_select": "Tensile strength સામે density દોરો તો વજન દીઠ તાકાતની રેખાઓ દેખાય: titanium અને "
                 "carbon fibre steel કરતાં ઘણી તીવ્ર રેખા પર બેસે છે.",
    "u1_bonds": "બંધનમાં ફરક ફક્ત એટલો છે કે electrons ક્યાં જાય - transferred, shared, એક atom દાન "
                "કરે, hydrogen bridge થી shared, કે ધાતુમાં pool થઈ જાય.",
    "u1_bondenergy": "બંધન જેટલું મજબૂત તેટલી તેને તોડવા વધુ ગરમી જોઈએ અને ગલનબિંદુ ઊંચું: hydrogen "
                     "bond માટે 20 kJ/mol સામે rock salt માટે 787.",
    "u1_cells": "BCC માં cell દીઠ બે atoms અને 68 % packing, FCC માં ચાર અને HCP માં છ atoms સાથે "
                "74 % - તેથી જ close-packed ધાતુઓ વધુ ductile હોય છે.",
    "u1_packing": "Simple cubic 48 % જગ્યા વેડફે, BCC 32 % અને close-packed રચના ફક્ત 26 %; packing "
                  "fraction જ density નક્કી કરે છે.",
    "u1_stress": "Tensile test ઢોળાવ પરથી modulus, બે શિખર પરથી yield અને ultimate strength, અને "
                 "specimen કેટલું ખેંચાયું તેના પરથી ductility આપે છે.",
    "u1_thermal": "ધાતુઓ એ જ મુક્ત electrons થી ગરમી અને current બંને વહન કરે: copper steel કરતાં "
                  "આઠ ગણું અને rubber કરતાં બે હજાર ગણું સારું વહન કરે.",
}


def main():
    draw()
    spec = spec_for(1)

    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("1.5 Solved Numericals, Step by Step",
                              "1.5 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI01000181",
        "unit": 1,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "theory_marks": spec["theory_marks"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 1 of Engineering Materials Science: the four families of material, the five kinds "
            "of bond and the properties each one explains, the crystal and its unit cell with the "
            "BCC, FCC and HCP numbers, the density that follows from a cell edge, and the properties "
            "a designer actually asks for - strength, ductility, hardness, conductivity and expansion. "
            "Every number in this unit is computed from a formula that is printed beside it: the "
            "packing fractions, the densities of iron and copper, the specific strengths and the "
            "technical values of the tensile test. Six solved numericals follow in section 1.5.",
            "Engineering Materials Science નું Unit 1: સામગ્રીનાં ચાર કુટુંબ, બંધનના પાંચ પ્રકાર અને "
            "દરેક જે ગુણધર્મ સમજાવે, crystal અને તેનો unit cell BCC, FCC તથા HCP ના આંકડા સાથે, cell "
            "edge પરથી નીકળતી density, અને designer ખરેખર માંગે તે ગુણધર્મો - તાકાત, ductility, "
            "hardness, વાહકતા અને પ્રસરણ. આ unit નો દરેક આંકડો તેની બાજુમાં છપાયેલા સૂત્ર પરથી ગણાયેલો "
            "છે: packing fractions, iron અને copper ની density, specific strengths અને tensile test ના "
            "મૂલ્યો. વિભાગ 1.5 માં છ ઉકેલેલા દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO1"],
        "practical_numbers": [1, 2, 3],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. This unit carries 14 % weightage, "
            "6 of the printed unit hours and 10 of the 70 theory marks. The six numericals of section "
            "1.5 are original revision problems with suggested marks, not GTU papers.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. આ unit નું weightage 14 %, "
            "છપાયેલા unit hours માંથી 6 અને 70 theory marks માંથી 10 છે. વિભાગ 1.5 ના છ દાખલા "
            "revision માટેના મૂળ પ્રશ્નો છે, GTU પેપર નહીં."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI01000181_unit1_preview.html"))
    from notes_workshop import render_one
    render_one("DI01000181", 1, note="Unit 1 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Engineering Materials Science Unit 1: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
