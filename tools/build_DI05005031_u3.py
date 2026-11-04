"""Build Chemical Reaction Engineering (DI05005031) Unit 3 - bilingual, with six figures."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI05005031 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI05005031_u3_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI05005031_u3 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()
    spec = spec_for(3)
    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("3.5 Solved Numericals, Step by Step",
                              "3.5 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI05005031",
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
            "Unit 3 of Chemical Reaction Engineering: how a batch experiment is turned into a rate "
            "equation. The three methods - differential, integral and half-life - are derived and "
            "compared on one set of data; the constant-volume relations, the expansion factor and "
            "the batch design equation t = CA0 integral dX/(-rA) follow; pressure readings are "
            "converted into concentrations; and the integrated laws of zero, first, second, third "
            "and nth order are derived once and tabulated with their half-lives and units. Six "
            "solved numericals follow in section 3.5.",
            "Chemical Reaction Engineering નું Unit 3: batch experiment ને rate equation માં કેવી "
            "રીતે ફેરવવો. ત્રણ રીતો - differential, integral અને half-life - derive કરીને એક જ data "
            "પર સરખાવેલી છે; ત્યારબાદ અચળ volume ના સંબંધો, expansion factor અને batch design "
            "equation t = CA0 integral dX/(-rA); pressure વાંચનને concentrations માં ફેરવવું; અને "
            "zero, first, second, third તથા nth order ના integrated laws એક વાર derive કરીને "
            "half-life અને એકમ સાથે કોષ્ટકમાં. વિભાગ 3.5 માં છ ઉકેલેલા દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO3"],
        "practical_numbers": [3, 4, 6, 7, 8, 12],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits, 45 teaching hours. This unit carries 20 % weightage, 9 of the printed unit "
            "hours and 14 of the 70 theory marks - the second largest theory share, because every "
            "kinetics practical of the laboratory depends on it. The numericals of section 3.5 are "
            "original revision problems with suggested marks, not GTU papers.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits, 45 teaching hours. આ unit નું weightage 20 %, છપાયેલા unit hours માંથી 9 અને "
            "70 theory marks માંથી 14 છે - બીજો સૌથી મોટો theory હિસ્સો, કારણ કે laboratory નો દરેક "
            "kinetics practical તેના પર આધારિત છે. વિભાગ 3.5 ના દાખલા revision માટેના મૂળ પ્રશ્નો "
            "છે, GTU પેપર નહીં."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI05005031_unit3_preview.html"))
    from notes_workshop import render_one
    render_one("DI05005031", 3, note="Unit 3 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Chemical Reaction Engineering Unit 3 {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


# Gujarati titles and captions for the six figures (short enough for a card header).
CAPTIONS_GU = {
    "u3_paths": "એક કોષ્ટકમાંથી rate equation સુધીની ત્રણ રીતો",
    "u3_diff": "Differential method: ઢાળ, પછી log-log રેખા",
    "u3_integral_test": "Integral method: કયો પ્લોટ સીધો છે",
    "u3_halflife": "Half-life અને શરૂઆતના concentration",
    "u3_pressure": "Pressure વાંચનને concentration માં ફેરવવું",
    "u3_orders": "દરેક order ના integrated laws",
}

CAPTIONS_GU_TAIL = {
    "u3_paths": "એક જ CA અને t કોષ્ટક ત્રણ રીતે વંચાય; differential method power law ફિટ કરે, "
                "integral method ધારણા ચકાસે, half-life method half-life કેવી રીતે બદલાય તેમાંથી "
                "order વાંચે.",
    "u3_diff": "CA-t વક્રના સ્પર્શક દરેક concentration પર એક rate આપે; ln(-rA) અને ln CA માંથી "
               "પસાર થતી સીધી રેખાનો ઢાળ order અને intercept ln k આપે.",
    "u3_integral_test": "order ધારો, integrate કરો, અને concentration નું અનુરૂપ વિધેય દોરો: ફક્ત "
                        "સાચો order સીધી રેખા આપે, અને તેનો ઢાળ k છે.",
    "u3_halflife": "log-log કાગળ પર half-life ઢાળ 1 - n વાળી સીધી રેખા છે: સપાટ એટલે first order, "
                   "ચઢતી એટલે zero order, ઊતરતી એટલે second order.",
    "u3_pressure": "અચળ volume વાળી gas પ્રક્રિયામાં gauge total pressure વાંચે; stoichiometry તેને "
                   "A ના partial pressure માં અને gas law તેને concentration માં ફેરવે.",
    "u3_orders": "દરેક order માટે સીધી રેખા આપતું ચલ જુદું છે - CA, ln CA, 1/CA - અને half-life એ જ "
                 "માહિતી એક આંકડામાં આપે છે.",
}

if __name__ == "__main__":
    main()
