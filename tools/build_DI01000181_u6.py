"""Build Engineering Materials Science (DI01000181) Unit 6 - green and advanced materials."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000181 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI01000181_u6_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI01000181_u6 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


CAPTIONS_GU = {
    "u6_cycle": "સામગ્રીનું જીવનચક્ર",
    "u6_energy": "Embodied energy અને recycling",
    "u6_ev": "ઇલેક્ટ્રિક કારમાં સામગ્રી",
    "u6_batt": "લિથિયમ-ion cell ના સ્તર",
    "u6_solar": "સૂર્યપ્રકાશથી kWh સુધી",
    "u6_light": "Lightweighting માટે specific strength",
}

CAPTIONS_GU_TAIL = {
    "u6_cycle": "કાચો માલ, ઉત્પાદન, વપરાશ અને જીવનનો અંત, જેમાં recycling ચક્ર બંધ કરે અને landfill તેને "
                "ખુલ્લું રાખે - cradle to grave અને cradle to cradle વચ્ચેનો ફરક.",
    "u6_energy": "એક કિલોગ્રામ aluminium 170 MJ પ્રાથમિક ઊર્જા ઉપાડે અને એક કિલોગ્રામ concrete એક; એ "
                 "aluminium recycle કરવાથી 95 % ઊર્જા બચે, તેથી ભંગાર કાચો માલ છે.",
    "u6_ev": "1500 કિલોની ઇલેક્ટ્રિક કાર 675 કિલો સ્ટીલ, 300 કિલો aluminium અને 225 કિલો battery છે, અને "
             "battery એ ભાગ છે જે સામગ્રીની યાદીમાં પહેલાં નહોતો.",
    "u6_batt": "Current collector, cathode, separator અને electrolyte, anode, current collector: 150 "
               "માઇક્રોમીટર જાડાઈમાં પાંચ સામગ્રી, અને એક cell 3.7 V અને 185 Wh.",
    "u6_solar": "1000 W/m2 આવે, cell માંથી 200 W/m2 વીજળી તરીકે નીકળે, અને 2 m2 પેનલ ચાર peak sun hour પર "
                "inverter પછી દિવસના 1.28 kWh આપે.",
    "u6_light": "સ્ટીલ 57 સામે CFRP 938 kN m પ્રતિ kg: ચાલતો ભાગ specific strength નક્કી કરે, અને પેનલ "
                "સામાન્ય રીતે stiffness નક્કી કરે.",
}


def main():
    draw()
    spec = spec_for(6)

    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("6.6 Solved Numericals, Step by Step",
                              "6.6 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI01000181",
        "unit": 6,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "theory_marks": spec["theory_marks"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 6 closes the syllabus with the question the first five units leave open: which "
            "material should a part be made of, once energy and life are counted as well as strength. "
            "It defines a green material on four counts and sets out the account - embodied energy, "
            "carbon, energy payback - then applies it to the automotive sector, where a 1500 kg electric "
            "car is 675 kg of steel and 225 kg of battery, and to renewable energy, where a solar module "
            "is mostly glass and a wind blade is 60 tonnes of composite. Natural fibre, recycled metal "
            "and biolubricants follow on the shop floor, and advanced materials - AHSS, aluminium, NdFeB "
            "magnets, Al-SiC - close the unit with the trade between mass, money and carbon. Six solved "
            "numericals follow in section 6.6.",
            "Unit 6 પહેલા પાંચ unit જે પ્રશ્ન ખુલ્લો રાખે તેનાથી અભ્યાસક્રમ પૂરો કરે: ઊર્જા અને આયુષ્ય પણ "
            "ગણતરીમાં લેતાં ભાગ કઈ સામગ્રીનો બનવો જોઈએ. તે green સામગ્રીને ચાર ગણતરીએ વ્યાખ્યાયિત કરે અને "
            "હિસાબ મૂકે - embodied energy, કાર્બન, energy payback - પછી તેને ઓટોમોબાઇલ ક્ષેત્રે લગાવે, જ્યાં "
            "1500 કિલોની ઇલેક્ટ્રિક કાર 675 કિલો સ્ટીલ અને 225 કિલો battery છે, અને નવીનીકરણીય ઊર્જામાં, જ્યાં "
            "સોલાર module મોટે ભાગે કાચ છે અને પવન blade 60 ટન composite છે. કારખાના ફ્લોર પર કુદરતી રેસા, "
            "recycled ધાતુ અને biolubricant આવે, અને advanced materials - AHSS, aluminium, NdFeB magnet, "
            "Al-SiC - દળ, પૈસા અને કાર્બન વચ્ચેના સોદા સાથે unit પૂરો કરે. વિભાગ 6.6 માં છ ઉકેલેલા દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO6"],
        "practical_numbers": [7],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. This last unit carries 15 % "
            "weightage, 6 of the printed unit hours and 10 of the 70 theory marks; practical 7, the "
            "report on green materials, is assessed there. The embodied energy, carbon and recycling "
            "figures are typical published values, not measurements of a particular plant, and the "
            "grid emission factor 0.71 kg CO2 per kWh is the Indian figure used throughout. The six "
            "numericals of section 6.6 are original revision problems with suggested marks, not GTU "
            "papers; the scrap price in problem 6 is an assumption and is stated as one.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. આ છેલ્લા unit નું weightage 15 %, "
            "છપાયેલા unit hours માંથી 6 અને 70 theory marks માંથી 10 છે; practical 7, green materials નો "
            "રિપોર્ટ, ત્યાં મપાય છે. embodied energy, કાર્બન અને recycling ના આંકડા પ્રકાશિત લાક્ષણિક મૂલ્યો "
            "છે, કોઈ એક કારખાનાના માપ નહીં, અને grid emission factor 0.71 kg CO2 પ્રતિ kWh એ સ્થળે વપરાયેલો "
            "ભારતીય આંકડો છે. વિભાગ 6.6 ના છ દાખલા revision માટેના મૂળ પ્રશ્નો છે, GTU પેપર નહીં; દાખલા 6 "
            "માંનો ભંગારનો ભાવ ધારેલો છે અને એ સ્પષ્ટ લખેલું છે."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI01000181_unit6_preview.html"))
    from notes_workshop import render_one
    render_one("DI01000181", 6, note="Unit 5 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Engineering Materials Science Unit 6: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
