"""Build Engineering Materials Science (DI01000181) Unit 5 - surfaces, oils, paints, corrosion."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000181 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI01000181_u5_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI01000181_u5 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


CAPTIONS_GU = {
    "u5_surface": "સપાટીનું સ્તર",
    "u5_finish": "Surface finish અને તેનો ખર્ચ",
    "u5_plate": "Electroplating cell",
    "u5_thick": "કોટિંગની જાડાઈ એક જ માપદંડ પર",
    "u5_visc": "તાપમાન સામે viscosity",
    "u5_paint": "પેન્ટ તંત્રનો કાપ",
    "u5_corr": "Corrosion cell",
    "u5_types": "કાટના છ પ્રકાર",
}

CAPTIONS_GU_TAIL = {
    "u5_surface": "કોટિંગ, તેની નીચેનો સારવાર પામેલો ઝોન અને અડક્યા વગરનો bulk: ભાગ સપાટી પર નિષ્ફળ જાય "
                  "કારણ કે ત્યાં stress, ઘસારો અને પર્યાવરણ મળે છે.",
    "u5_finish": "6.3 માઇક્રોમીટર drilling થી 0.05 માઇક્રોમીટર lapping સુધી, દરેક પગલું આધી ખરબચડાઈ "
                 "ખરીદે - અને સપાટી પહેલાં સાફ ન હોય તો કંઈ જ કામ ન કરે.",
    "u5_plate": "Anode electrolyte માં ઓગળે અને કામ cathode તરીકે એ જ ધાતુ પાછી ઉગાડે, એક Faraday વખતે: "
                "300 A/m2 વીસ મિનિટ એટલે 11.7 માઇક્રોમીટર nickel.",
    "u5_thick": "3 માઇક્રોમીટરની PVD ફિલ્મ cutting edge રક્ષે, 220 માઇક્રોમીટરનું પેન્ટ પુલ રક્ષે, અને "
                "80 માઇક્રોમીટરનું hot dip zinc સખત હોવાથી નહીં, ખર્ચાઈને રક્ષે.",
    "u5_visc": "બંને તેલ 100 C પર 10 cSt: 30 C પર એક 110 cSt અને બીજું 316, અને એ જ ફરક viscosity index "
               "માપે છે.",
    "u5_paint": "Blasted પ્લેટ પર ચાર કોટ, દરેકનું પોતાનું કામ, અને કુલ 215 માઇક્રોમીટર સૂકી ફિલ્મ જે "
                "ત્યારે જ ચાલે જ્યારે દરેક કોટ નીચેના કોટ સાથે પકડાય.",
    "u5_corr": "Anode, cathode, electrolyte અને રસ્તો: જ્યાં oxygen આવે અને ધાતુ electrons આપે ત્યાં સ્ટીલ "
               "કાટ ખાય, અને 0.1 A/m2 એટલે વર્ષે 0.116 mm.",
    "u5_types": "Uniform, galvanic, pitting, crevice, stress cracking અને erosion: ફક્ત પહેલાને "
                "corrosion allowance થી ચૂકવી શકાય, તેથી બાકીના પાંચ design થી જ દૂર કરવા પડે.",
}


def main():
    draw()
    spec = spec_for(5)

    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("5.6 Solved Numericals, Step by Step",
                              "5.6 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI01000181",
        "unit": 5,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "theory_marks": spec["theory_marks"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 5 of Engineering Materials Science: the surface, and the five ways it is defended. "
            "It starts from why a part fails at the surface, then works through cleaning and "
            "mechanical finishing, electroplating and electroless plating, anodising, phosphate and "
            "chromate conversion coatings, electropolishing and photo-etching, and PVD and CVD thin "
            "films. Oils follow with viscosity, the viscosity index, additives and the designation of "
            "a drum; paints and varnishes as a system of coats over a blasted plate; and corrosion as "
            "an electrochemical cell with six shapes and one defence each. Six solved numericals "
            "follow in section 5.6.",
            "Engineering Materials Science નું Unit 5: સપાટી, અને તેનું રક્ષણ કરતી પાંચ રીતો. તે "
            "સપાટી પર ભાગ કેમ નિષ્ફળ જાય તેનાથી શરૂ થાય, પછી સફાઈ અને mechanical finishing, "
            "electroplating તથી electroless plating, anodising, phosphate તથી chromate conversion "
            "coatings, electropolishing તથી photo-etching, અને PVD તથી CVD thin films આવે. પછી તેલ: "
            "viscosity, viscosity index, additives અને ડ્રમનું designation; પેન્ટ અને varnish: "
            "blasted plate પર કોટનું તંત્ર; અને કાટ: electrochemical cell, છ આકાર અને દરેક માટે એક "
            "બચાવ. વિભાગ 5.6 માં છ ઉકેલેલા દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO5"],
        "practical_numbers": [5],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. This unit carries 17 % weightage, "
            "10 of the printed unit hours - the largest share of the course - and 12 of the 70 theory "
            "marks; practical 5, the study of heat treatment furnaces and case hardening, is the "
            "laboratory side of surface treatment. The six numericals of section 5.6 are original "
            "revision problems with suggested marks, not GTU papers; the paint price and the "
            "electricity tariff used in them are assumptions and are stated as such.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. આ unit નું weightage 17 %, "
            "છપાયેલા unit hours માંથી 10 - course માં સૌથી મોટો ભાગ - અને 70 theory marks માંથી 12 છે; "
            "practical 5, heat treatment furnace અને case hardening નો અભ્યાસ, surface treatment ની "
            "laboratory બાજુ છે. વિભાગ 5.6 ના છ દાખલા revision માટેના મૂળ પ્રશ્નો છે, GTU પેપર નહીં; "
            "તેમાં વપરાયેલો પેન્ટનો ભાવ અને વીજળીનો દર ધારેલા છે અને એ સ્પષ્ટ લખેલું છે."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI01000181_unit5_preview.html"))
    from notes_workshop import render_one
    render_one("DI01000181", 5, note="Unit 5 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Engineering Materials Science Unit 5: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
