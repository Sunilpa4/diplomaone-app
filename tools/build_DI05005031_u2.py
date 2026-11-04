"""Build Chemical Reaction Engineering (DI05005031) Unit 2 - bilingual, with five figures."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI05005031 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI05005031_u2_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI05005031_u2 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()
    spec = spec_for(2)
    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("2.6 Solved Numericals, Step by Step",
                              "2.6 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI05005031",
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
            "Unit 2 of Chemical Reaction Engineering: the rate law split into its temperature term "
            "k(T) and its concentration term f(C), what the rate constant really is, elementary and "
            "non-elementary reactions (with the H2 + Br2 chain derived from its steady state), the "
            "Arrhenius law derived from the van't Hoff relation and from collision theory, and the "
            "activation energy - what it is, how a catalyst lowers it, and how it is measured from "
            "rate constants at several temperatures. Six solved numericals follow in section 2.6.",
            "Chemical Reaction Engineering નું Unit 2: rate law ના બે ભાગ - temperature વાળો k(T) "
            "અને concentration વાળો f(C), rate constant ખરેખર શું છે, elementary અને non-elementary "
            "પ્રક્રિયાઓ (H2 + Br2 ની chain તેના steady state પરથી derive કરેલી), van't Hoff સંબંધ "
            "અને collision theory પરથી Arrhenius law, અને activation energy - તે શું છે, catalyst "
            "તેને કેવી રીતે ઘટાડે છે, અને ઘણા temperatures પરના rate constants પરથી તે કેવી રીતે "
            "માપાય છે. વિભાગ 2.6 માં છ ઉકેલેલા દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO2"],
        "practical_numbers": [1, 2, 5, 9, 10, 11],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits, 45 teaching hours. This unit carries 17 % weightage, 8 of the printed unit "
            "hours and 12 of the 70 theory marks. The numericals of section 2.6 are original revision "
            "problems with suggested marks, not GTU papers.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits, 45 teaching hours. આ unit નું weightage 17 %, છપાયેલા unit hours માંથી 8 અને "
            "70 theory marks માંથી 12 છે. વિભાગ 2.6 ના દાખલા revision માટેના મૂળ પ્રશ્નો છે, GTU "
            "પેપર નહીં."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI05005031_unit2_preview.html"))
    from notes_workshop import render_one
    render_one("DI05005031", 2, note="Unit 2 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Chemical Reaction Engineering Unit 2: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


# Gujarati titles and captions for the six figures (short enough for a card header).
CAPTIONS_GU = {
    "u2_terms": "Rate law એ બે ભાગનો ગુણાકાર છે",
    "u2_arrhenius": "Arrhenius law: k(T) તરીકે અને સીધી રેખા તરીકે",
    "u2_ea": "ln k અને 1/T પરથી activation energy",
    "u2_barrier": "અવરોધ, catalyst સાથે અને વગર",
    "u2_chain": "Chain પ્રક્રિયાનો order અપૂર્ણાંક કેમ થાય",
}

CAPTIONS_GU_TAIL = {
    "u2_terms": "Concentration ભાગ chemistry છે અને temperature ભાગ exponential; rate law એક વાર "
                "માપીને k(T) દ્વારા કોઈ પણ temperature પર વપરાય છે.",
    "u2_arrhenius": "k, T સાથે exponential વધે છે, પણ ln k, 1/T સાથે સીધી રેખા બને છે - તેથી "
                    "laboratory માં ઢાળ પરથી Ea મળે છે.",
    "u2_ea": "ત્રણ temperature ના ત્રણ rate constants રેખા નક્કી કરે; ઢાળ -Ea/R હોવાથી Ea સીધી "
             "J/mol માં વંચાય.",
    "u2_barrier": "Catalyst નીચા શિખર વાળો બીજો માર્ગ ખોલે; reactant અને product ની સપાટી, એટલે "
                  "dH અને K_eq, અડક્યા વિના રહે.",
    "u2_chain": "Bromine atoms પ્રક્રિયા શરૂ કરે અને ચલાવે; termination propagation સાથે સ્પર્ધા "
                "કરતું હોવાથી Br2 માં order 1.5 મળે, molecularity 2 નહીં.",
}

if __name__ == "__main__":
    main()
