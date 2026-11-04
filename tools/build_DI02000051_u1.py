"""Build Environmental Sustainability (DI02000051) Unit 1 - bilingual en + gu."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI02000051 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI02000051_u1_notes import (NOTES, EQUATIONS, NUMERICALS, VIVA, EXAM,  # noqa: E402
                                         PRACTICE_ANSWERS, SOURCES, LESSON_COUNT)
from diagrams_DI02000051_u1 import (TITLES, TITLES_GU, CAPTIONS, CAPTIONS_GU,  # noqa: E402
                                    DIAGRAMS)
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()
    spec = spec_for(1)
    assert len(PRACTICE_ANSWERS) == len(EXAM), "one model answer per practice question"

    NOTES[-1] = {
        "title": tr("5. Practice Questions with Model Answers", "5. સરાવ પ્રશ્નો અને આદર્શ જવાબો"),
        "items": [{"h": tr(f"Practice {i}. {q['q']['en']}", f"સરાવ {i}. {q['q']['gu']}"),
                   "body": PRACTICE_ANSWERS[i - 1]}
                  for i, q in enumerate(EXAM, 1)],
    }
    exam = [{"q": tr("Practice: " + e["q"]["en"], "સરાવ: " + e["q"]["gu"]), "marks": e["marks"]}
            for e in EXAM]

    unit = {
        "subject": "DI02000051",
        "unit": 1,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 1 of Environmental Sustainability: what sustainability means and the three pillars "
            "it stands on; the structure of an ecosystem, its producers, consumers and decomposers; "
            "energy flow with the ten per cent law and the ecosystem services we get for free; the "
            "carbon, nitrogen, sulphur and phosphorus cycles; and biodiversity - its three levels, "
            "its value, the five threats it faces and the conservation strategies that answer them. "
            "Nine lecture cards, five diagrams, ten fully solved numericals and twelve answered "
            "practice questions.",
            "પર્યાવરણીય ટકાઉપણાનું યુનિટ 1: ટકાઉપણું એટલે શું અને તેના ત્રણ સ્તંભ; પારિતંત્રની રચના, "
            "તેના ઉત્પાદક, ઉપભોક્તા અને વિઘટક; દસ ટકાના નિયમ સાથે ઊર્જા પ્રવાહ અને મફત મળતી પારિતંત્ર "
            "સેવાઓ; કાર્બન, નાઇટ્રોજન, સલ્ફર અને ફોસ્ફરસ ચક્ર; અને જૈવવિવિધતા - તેનાં ત્રણ સ્તર, તેનું "
            "મૂલ્ય, તેના પાંચ ભય અને તેમનો જવાબ આપતી સંરક્ષણ વ્યૂહરચનાઓ. નવ પાઠ-કાર્ડ, પાંચ આકૃતિઓ, "
            "દસ પૂરા ઉકેલાયેલા દાખલા અને બાર ઉત્તરસહિત સરાવ પ્રશ્નો."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(t, TITLES_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU[i])} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "numericals": NUMERICALS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO1"],
        "practical_numbers": [],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT,
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA/CA 30 = 100 marks, 2 credits, 30 teaching hours, "
            "no practical and no laboratory requirement (NIL in the PDF). This unit carries 10 % "
            "weightage, 4 of the 30 hours and 7 of the 70 theory marks (the PDF prints weightage "
            "only, so marks are split by weightage). Practice marks 3/4/5 are suggested revision "
            "sizes, not GTU allocations. Model answers are in Notes section 5.",
            "અધિકૃત કોર્સ: થિયરી ESE 70 + PA/CA 30 = 100 માર્ક્સ, 2 ક્રેડિટ, 30 શિક્ષણ કલાક, કોઈ "
            "પ્રેક્ટિકલ કે લેબોરેટરી જરૂરિયાત નથી (PDFમાં NIL). આ યુનિટનું વેઇટેજ 10 %, 30માંથી 4 કલાક "
            "અને 70 થિયરી માર્ક્સમાંથી 7 માર્ક્સ (PDFમાં ફક્ત વેઇટેજ છે, તેથી માર્ક્સ વેઇટેજ પ્રમાણે "
            "વહેંચ્યા છે). સરાવના 3/4/5 માર્ક્સ સૂચિત પુનરાવર્તન માપ છે, GTU ફાળવણી નહીં. આદર્શ જવાબો "
            "નોંધ વિભાગ 5માં છે."),
        "question_provenance": "Original answered revision questions; not official past papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": s["en"], "url": ("https://syllabus.gtu.ac.in/" if "GTU" in s["en"]
                                               else "https://www.envis.nic.in/")}
                    for s in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI02000051_unit1_preview.html"))
    from notes_workshop import render_one
    shelf_file = render_one("DI02000051", 1, note="Unit 1 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Environmental Sustainability Unit 1: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{len(st['numericals'])} numericals / {sum(len(s['items']) for s in st['viva'])} viva / "
          f"{len(st['exam_questions'])} exam")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")


if __name__ == "__main__":
    main()
