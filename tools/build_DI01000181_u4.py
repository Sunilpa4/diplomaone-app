"""Build Engineering Materials Science (DI01000181) Unit 4 - non-metallic materials."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000181 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI01000181_u4_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI01000181_u4 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


CAPTIONS_GU = {
    "u4_tree": "Non-metallic materials નું વર્ગીકરણ",
    "u4_rubber": "Rubber નું vulcanisation",
    "u4_ceramic": "દરેક કુટુંબ કેટલી ગરમી સુધી ચાલે",
    "u4_compare": "Metal, ceramic અને polymer ની સરખામણી",
    "u4_refract": "બે સ્તરની refractory દીવાલ",
    "u4_insul": "Insulators ની dielectric strength",
    "u4_abrasive": "Mohs ladder અને abrasives",
}

CAPTIONS_GU_TAIL = {
    "u4_tree": "Polymers, ceramics, composites અને natural materials: ચાર કુટુંબ જે ડ્રોઇંગ વજન, "
               "અવાહકતા, શાંત ચાલ અને ભાવ માટે વાપરે, તાકાત માટે નહીં.",
    "u4_rubber": "Sulphur ના પુલ નરમ gum ને, જે ખેંચાઈને ખેંચાયેલું જ રહે, એવા rubber માં ફેરવે જે "
                 "પાછું આવે; એ જ 500 % elongation હવે શૂન્ય પર પાછું આવે.",
    "u4_ceramic": "સેવાનું તાપમાન bond પ્રમાણે ચાલે: polymer માં van der Waals બળ, metal માં metallic "
                  "bond, ceramic માં ionic અને covalent bond.",
    "u4_compare": "Bond, તાકાત, ductility, મર્યાદા, density અને તૂટવાની રીત - ત્રણેય કુટુંબને પૂછાતા છ "
                  "પ્રશ્નો, જેથી પસંદગી ટેવ પ્રમાણે નહીં ગુણધર્મ પ્રમાણે થાય.",
    "u4_refract": "ગરમ સપાટી પર 1200 C અને shell પર 50 C, જોડાણ પર 977 C: મોટો તાપમાન ઘટાડો "
                  "firebrick લે છે અને પાતળું અવાહક સ્તર 80 % ઉષ્મા બચાવે છે.",
    "u4_insul": "જાડાઈ dielectric strength નક્કી કરે: હવા 3 kV/mm અને PTFE 24, તેથી એક જ busbar ને "
                "સાવ જુદી દીવાલ જોઈએ.",
    "u4_abrasive": "Mohs પર quartz 7, corundum 9 અને diamond 10, અને synthetic abrasives Knoop "
                   "hardness થી તેમની વચ્ચે ગોઠવાય છે.",
}


def main():
    draw()
    spec = spec_for(4)

    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("4.6 Solved Numericals, Step by Step",
                              "4.6 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI01000181",
        "unit": 4,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "theory_marks": spec["theory_marks"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 4 of Engineering Materials Science: the materials a machine uses where strength is "
            "not the question. It classifies the non-metals by their bond, follows rubber from latex "
            "to a vulcanised compound and shows how an elastomer is chosen for a fluid, treats "
            "ceramics from the brick in a furnace wall to the silicon nitride rotor of a "
            "turbocharger, works a two-layer refractory wall and an insulator thickness, and ends "
            "with the grain, bond and grit of an abrasive and the shear of an adhesive joint. Six "
            "solved numericals follow in section 4.6.",
            "Engineering Materials Science નું Unit 4: જ્યાં તાકાત પ્રશ્ન નથી ત્યાં મશીન જે સામગ્રી "
            "વાપરે છે તે. તે non-metals ને તેમના bond પ્રમાણે વર્ગીકૃત કરે, rubber ને latex થી "
            "vulcanised compound સુધી લઈ જાય અને પ્રવાહી પ્રમાણે elastomer કેમ પસંદ થાય તે બતાવે, "
            "ceramics ને ભઠ્ઠીની ઈંટ થી turbocharger ના silicon nitride rotor સુધી લઈ જાય, બે સ્તરની "
            "refractory દીવાલ અને insulator ની જાડાઈ ગણે, અને abrasive ના grain, bond તથી grit અને "
            "adhesive જોડાણના shear પર પૂરું કરે. વિભાગ 4.6 માં છ ઉકેલેલા દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO4"],
        "practical_numbers": [6],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. This unit carries 17 % weightage, "
            "8 of the printed unit hours and 12 of the 70 theory marks, and practical 6 is the "
            "non-metallic materials report. The six numericals of section 4.6 are original revision "
            "problems with suggested marks, not GTU papers; the electricity tariff used in one of "
            "them is an assumption and is stated as one.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. આ unit નું weightage 17 %, "
            "છપાયેલા unit hours માંથી 8 અને 70 theory marks માંથી 12 છે, અને practical 6 એ "
            "non-metallic materials નો રિપોર્ટ છે. વિભાગ 4.6 ના છ દાખલા revision માટેના મૂળ પ્રશ્નો છે, "
            "GTU પેપર નહીં; તેમાંની એકમાં વીજળીનો દર ધારેલો છે અને એ સ્પષ્ટ લખેલું છે."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI01000181_unit4_preview.html"))
    from notes_workshop import render_one
    render_one("DI01000181", 4, note="Unit 4 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Engineering Materials Science Unit 4: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
