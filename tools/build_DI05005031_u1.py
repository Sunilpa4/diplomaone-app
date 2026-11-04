"""Build Chemical Reaction Engineering (DI05005031) Unit 1 - bilingual, with six figures."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI05005031 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI05005031_u1_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI05005031_u1 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()
    spec = spec_for(1)
    items = [{"h": h, "body": a} for h, _q, a, _m in PRACTICE]
    NOTES.append({"title": tr("1.8 Solved Numericals, Step by Step",
                              "1.8 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI05005031",
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
            "Unit 1 of Chemical Reaction Engineering: what the subject is for, the six ways a "
            "reaction is classified, enzymes and the Michaelis-Menten derivation, the rate of "
            "reaction on four different bases, and the variables that change a rate. Every result is "
            "derived line by line - the Michaelis-Menten law from the steady-state balance, the "
            "adiabatic temperature rise from the energy balance, the unit of k from the unit balance "
            "- and six solved numericals follow in section 1.8.",
            "Chemical Reaction Engineering નું Unit 1: subject શેના માટે છે, પ્રક્રિયાના "
            "વર્ગીકરણની છ રીતો, enzymes અને Michaelis-Menten derivation, ચાર જુદા આધાર પર reaction "
            "rate, અને rate બદલતા ચલો. દરેક પરિણામ લીટી-બાય-લીટી derive કરેલું છે - Michaelis-"
            "Menten law steady-state balance પરથી, adiabatic temperature rise energy balance "
            "પરથી, k નું એકમ unit balance પરથી - અને પછી વિભાગ 1.8 માં છ ઉકેલેલા દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO1"],
        "practical_numbers": [1, 2, 10, 11],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. This unit carries 15 % "
            "weightage, 7 of the printed unit hours and 10 of the 70 theory marks. The six "
            "numericals of section 1.8 are original revision problems with suggested marks, not GTU "
            "papers.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. આ unit નું weightage 15 %, "
            "છપાયેલા unit hours માંથી 7 અને 70 theory marks માંથી 10 છે. વિભાગ 1.8 ના છ દાખલા "
            "revision માટેના મૂળ પ્રશ્નો છે, GTU પેપર નહીં."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI05005031_unit1_preview.html"))
    from notes_workshop import render_one
    render_one("DI05005031", 1, note="Unit 1 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Chemical Reaction Engineering Unit 1: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


# Gujarati titles and captions for the six figures (short enough for a card header).
CAPTIONS_GU = {
    "u1_map": "Reaction engineering છ બાજુથી ઉધાર લે છે",
    "u1_tree": "પ્રક્રિયાના છ પ્રકારનું વર્ગીકરણ",
    "u1_energy": "Energy profile: exothermic અને endothermic",
    "u1_basis": "Rate લખવાના ચાર આધાર",
    "u1_variables": "પ્રક્રિયાનો rate શું બદલે છે",
    "u1_mm": "Enzyme kinetics: Michaelis-Menten વક્ર",
}

CAPTIONS_GU_TAIL = {
    "u1_map": "Reactor નું size kinetics થી નક્કી થાય, પણ તેને feed, stir, heat અને ખર્ચ પણ "
              "જોઈએ - તેથી design છ વિષયોને એકસાથે લે છે.",
    "u1_tree": "એક જ પ્રક્રિયાને phases, catalyst, દિશા, molecularity, heat અને order થી વર્ણવી "
               "શકાય; પરીક્ષા આ છમાંથી કોઈ પણ પૂછી શકે.",
    "u1_energy": "શિખર એ activation energy છે અને બે સપાટી વચ્ચેનું અંતર heat of reaction; catalyst "
                 "શિખર નીચું કરે છે, અંતર નહીં.",
    "u1_basis": "એ જ moles પ્રતિ second ને volume, catalyst mass, area કે solid mass વડે ભાગવાથી "
                "rate constant નું એકમ બદલાય છે.",
    "u1_variables": "Concentration અને temperature ડિઝાઇનર સીધા બદલી શકે તેવા બે ચલ છે; બાકીના "
                    "reactor બનાવતી વખતે નક્કી થાય છે.",
    "u1_mm": "Enzyme saturate થાય: ઓછા substrate પર rate first order, વધુ પર zero order અને Vmax પર "
             "અટકે છે.",
}

if __name__ == "__main__":
    main()
