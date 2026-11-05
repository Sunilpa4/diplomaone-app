"""Build Engineering Materials Science (DI01000181) Unit 3 - metals and their alloys."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000181 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI01000181_u3_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI01000181_u3 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


CAPTIONS_GU = {
    "u3_tree": "Metals નું વર્ગીકરણ",
    "u3_carbon": "Carbon સામે તાકાત અને ductility",
    "u3_ci": "ચાર cast irons",
    "u3_cu": "Copper અને તેના alloys",
    "u3_desig": "Workshop માં ઓર્ડર થતાં સ્ટીલ",
    "u3_al": "Aluminium: આઠ series",
    "u3_compare": "Metals સામે non-metals",
}

CAPTIONS_GU_TAIL = {
    "u3_tree": "Ferrous એટલે iron પર આધારિત: 2.14 % carbon સુધી steel અને તેની ઉપર cast iron, જે "
               "carbon content તથી graphite ના આકાર પ્રમાણે વહેંચાય. Non-ferrous એટલે બાકીનું બધું, એક "
               "base metal અને તેમાં ઉમેરેલું.",
    "u3_carbon": "Carbon 0.1 % થી 1.2 % કરો તો tensile strength લગભગ બમણી થાય અને elongation 30 % થી "
                 "5 % થાય; સૌથી સારું સંયોજન વચ્ચે મળે છે.",
    "u3_ci": "ચારેય cast irons માં 2 % થી વધુ carbon હોય છે; બદલાય છે carbon જે આકાર લે છે - flakes, "
             "cementite, temper carbon કે nodules - અને એ આકાર તાકાત નક્કી કરે છે.",
    "u3_cu": "Zinc copper ની તાકાત વધારે અને તે જ વખતે વાહકતા નષ્ટ કરે, તેથી electrical કામમાં copper "
             "અને bearing ના કામમાં bronze વપરાય.",
    "u3_desig": "સ્ટીલ તેના designation થી ઓર્ડર થાય, અને વચ્ચેનો આંકડો ટકાના સોમાં ભાગમાં carbon છે.",
    "u3_al": "Series નો આંકડો કહે છે કે મુખ્ય alloying ઉમેરો કયો છે; series 7 ના zinc alloys 570 MPa સુધી "
             "પહોંચે, જે સરખા વજનના plain carbon steel કરતાં બમણાથી વધુ છે.",
    "u3_compare": "Metals અને non-metals એક જ ગુણધર્મથી અલગ પડે - outer electrons મુક્ત છે કે નહીં - અને "
                  "કોષ્ટકનો બાકીનો દરેક ફરક એમાંથી આવે છે.",
}


def main():
    draw()
    spec = spec_for(3)

    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("3.6 Solved Numericals, Step by Step",
                              "3.6 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI01000181",
        "unit": 3,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "theory_marks": spec["theory_marks"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 3 of Engineering Materials Science: the two branches of engineering metals, the "
            "carbon content that separates steel from cast iron, what each family of steel is ordered "
            "for, the four cast irons whose graphite shape decides their strength, and the copper and "
            "aluminium alloys that carry the current, save the weight and resist the sea. Every "
            "composition and strength quoted here is a handbook value, the designations are the ones "
            "used on an Indian drawing, and six solved numericals follow in section 3.6.",
            "Engineering Materials Science નું Unit 3: ઇજનેરી ધાતુઓની બે શાખા, steel અને cast iron ને "
            "વહેંચતું carbon content, સ્ટીલનું દરેક કુટુંબ શેના માટે ઓર્ડર થાય, જેનો graphite આકાર "
            "તાકાત નક્કી કરે તે ચાર cast irons, અને current વહન કરતા, વજન બચાવતા તથી દરિયા સામે ટકતા "
            "copper તથી aluminium alloys. અહીંનું દરેક composition અને strength handbook નું મૂલ્ય છે, "
            "designations ભારતીય drawing પર વપરાતા છે, અને વિભાગ 3.6 માં છ ઉકેલેલા દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO3"],
        "practical_numbers": [1, 3],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. This unit carries 17 % weightage, "
            "8 of the printed unit hours and 12 of the 70 theory marks. The six numericals of section "
            "3.6 are original revision problems with suggested marks, not GTU papers; the metal "
            "prices in one of them are assumptions, stated as such.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits (3 lecture + 2 practical), 45 teaching hours. આ unit નું weightage 17 %, "
            "છપાયેલા unit hours માંથી 8 અને 70 theory marks માંથી 12 છે. વિભાગ 3.6 ના છ દાખલા revision "
            "માટેના મૂળ પ્રશ્નો છે, GTU પેપર નહીં; તેમાંના એકમાં ધાતુના ભાવ ધારેલા છે અને એ સ્પષ્ટ લખેલું છે."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI01000181_unit3_preview.html"))
    from notes_workshop import render_one
    render_one("DI01000181", 3, note="Unit 3 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Engineering Materials Science Unit 3: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
