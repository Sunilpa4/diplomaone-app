"""Build Engineering Materials Science (DI01000181) Unit 2 - solidification and phase diagrams."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000181 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI01000181_u2_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI01000181_u2 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


CAPTIONS_GU = {
    "u2_coolcurve": "શુદ્ધ ધાતુ અને alloy ની cooling curve",
    "u2_ingot": "Casting ingot નું grain structure",
    "u2_solution": "Substitutional અને interstitial solid solution",
    "u2_cuni": "Copper-nickel: isomorphous system નો diagram",
    "u2_pbsn": "Lead-tin: eutectic system નો diagram",
    "u2_fec": "Iron-iron carbide diagram ના મુખ્ય બિંદુઓ",
    "u2_micro": "Eutectoid આસપાસનાં microstructures",
    "u2_hallpetch": "Grain size yield strength નક્કી કરે છે",
}

CAPTIONS_GU_TAIL = {
    "u2_coolcurve": "શુદ્ધ ધાતુ એક જ temperature પર થીજે અને latent heat નીકળે ત્યાં સુધી રેખા સપાટ "
                    "રહે; alloy liquidus અને solidus વચ્ચેની range માં થીજે તેથી રેખા ફક્ત ઢાળ બદલે.",
    "u2_ingot": "Mould ની દીવાલ પહેલી ઠંડી થાય તેથી ત્યાં નાના grains બને, ગરમીના પ્રવાહ સાથે અંદર "
                "તરફ લાંબા columnar grains વધે, અને ગરમ વચ્ચે છેલ્લે જાડા equiaxed grains થીજે.",
    "u2_solution": "Substitutional solution માં સરખા માપનો atom બીજાની જગ્યાએ બેસે (Cu-Ni); "
                   "interstitial solution માં નાનો atom ખાલી જગ્યામાં બેસે (iron માં carbon) - તેથી જ "
                   "carbon iron માં 2.14 % સુધી જ બેસે.",
    "u2_cuni": "Copper અને nickel દરેક પ્રમાણમાં એકબીજામાં ઓગળે, તેથી diagram માં eutectic નથી: એક "
               "liquidus નીચે એક solidus, અને tie line બંને phase આપે.",
    "u2_pbsn": "Lead અને tin એકબીજામાં થોડા જ ઓગળે, તેથી બંને liquidus શાખા eutectic પર મળે - 183 C "
               "અને 61.9 % tin - જ્યાં alloy એક જ temperature પર થીજે.",
    "u2_fec": "Austenite માં carbon 2.14 % સુધી ઓગળે; 0.8 % અને 727 C પર એ austenite pearlite બને, અને "
              "સ્ટીલની દરેક heat treatment એ જ eutectoid ફરતે ફરે છે.",
    "u2_micro": "0.8 % થી નીચે pearlite ferrite ના ખેતરમાં દેખાય, બરાબર 0.8 % પર આખું micrograph "
                "pearlite હોય, અને 0.8 % થી ઉપર cementite grain boundary પર ભંગુર જાળી બનાવે.",
    "u2_hallpetch": "Yield strength grain size ના વ્યસ્ત વર્ગમૂળ સાથે વધે: grain size અડધું કરો તો એ જ "
                    "સ્ટીલની તાકાત લગભગ 40 % વધે.",
}


def main():
    draw()
    spec = spec_for(2)

    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("2.7 Solved Numericals, Step by Step",
                              "2.7 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI01000181",
        "unit": 2,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "theory_marks": spec["theory_marks"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 2 of Engineering Materials Science: what a phase is and how the phase rule counts "
            "them, what a cooling curve tells a foundry, how a casting freezes from the mould wall "
            "inwards and why that leaves three zones of grains, how a solid solution differs from a "
            "compound, and how to read the three diagrams that the rest of the subject stands on - "
            "copper-nickel, lead-tin and iron-carbon. The lever rule is worked on every one of them, "
            "the eutectoid of steel is computed for three carbon contents, and six solved numericals "
            "follow in section 2.7.",
            "Engineering Materials Science નું Unit 2: phase એટલે શું અને phase rule તેને કેવી રીતે "
            "ગણે, cooling curve ફાઉન્ડ્રીને શું કહે, casting mould ની દીવાલથી અંદર તરફ કેવી રીતે થીજે અને "
            "તેથી grains ના ત્રણ zone કેમ રહે, solid solution અને compound માં ફરક શું, અને આખો વિષય "
            "જેના પર ઊભો છે તે ત્રણ diagram - copper-nickel, lead-tin અને iron-carbon - કેવી રીતે વાંચવા. "
            "Lever rule ત્રણેય પર ગણાયેલો છે, સ્ટીલના eutectoid ની ગણતરી ત્રણ carbon content માટે કરેલી "
            "છે, અને પછી વિભાગ 2.7 માં છ ઉકેલેલા દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO2"],
        "practical_numbers": [2],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. This unit carries 20 % weightage, "
            "7 of the printed unit hours and 14 of the 70 theory marks - the largest of the six. The "
            "six numericals of section 2.7 are original revision problems with suggested marks, not "
            "GTU papers.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. આ unit નું weightage 20 %, "
            "છપાયેલા unit hours માંથી 7 અને 70 theory marks માંથી 14 છે - છમાંથી સૌથી મોટું. વિભાગ 2.7 ના "
            "છ દાખલા revision માટેના મૂળ પ્રશ્નો છે, GTU પેપર નહીં."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI01000181_unit2_preview.html"))
    from notes_workshop import render_one
    render_one("DI01000181", 2, note="Unit 2 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Engineering Materials Science Unit 2: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
