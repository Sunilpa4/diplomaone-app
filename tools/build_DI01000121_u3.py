"""Build Applied Physics (DI01000121) Unit 3 "General Properties of Matter" - bilingual en + gu."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000121 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI01000121_u3_notes import (NOTES, EQUATIONS, NUMERICALS, VIVA, EXAM,  # noqa: E402
                                         PRACTICE_ANSWERS, SOURCES, LESSON_COUNT)
from diagrams_DI01000121_u3 import (TITLES, TITLES_GU, CAPTIONS, CAPTIONS_GU,  # noqa: E402
                                    DIAGRAMS)
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()
    spec = spec_for(3)
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
        "subject": "DI01000121",
        "unit": 3,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 3 of Applied Physics: elasticity with stress, strain, Hooke's law, the three "
            "moduli and the stress-strain curve; surface tension from the molecular theory through "
            "cohesion and adhesion, the angle of contact, capillarity and its engineering uses; and "
            "viscosity with Newton's law, streamline and turbulent flow, the Reynolds number and "
            "Stokes' law. Twenty-one lecture cards, five diagrams, twenty-four fully solved "
            "numericals and sixteen answered practice questions.",
            "એપ્લાઇડ ફિઝિક્સનું યુનિટ 3: સ્થિતિસ્થાપકતા સાથે પ્રતિબળ, વિકૃતિ, હૂકનો નિયમ, ત્રણ ગુણાંક "
            "અને પ્રતિબળ-વિકૃતિ વક્ર; આણ્વીય સિદ્ધાંતથી પૃષ્ઠતાણ, સંસક્તિ-આસક્તિ, સંપર્ક કોણ, કેશનળી "
            "ચઢાણ અને તેના ઇજનેરી ઉપયોગો; અને શ્યાનતા સાથે ન્યૂટનનો નિયમ, સ્તરીય તથા વમળીય પ્રવાહ, "
            "રેનોલ્ડ્સ આંક અને સ્ટોક્સનો નિયમ. એકવીસ પાઠ-કાર્ડ, પાંચ આકૃતિઓ, ચોવીસ પૂરા ઉકેલાયેલા "
            "દાખલા અને સોળ ઉત્તરસહિત સરાવ પ્રશ્નો."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(t, TITLES_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU[i])} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "numericals": NUMERICALS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO3"],
        "practical_numbers": [4, 5, 6],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT,
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits, 45 teaching hours; this unit carries 28 % weightage, 12 of the 45 hours and "
            "19 of the 70 theory marks (the PDF prints weightage only, so the marks are split by "
            "weightage). Practice marks 3/4/5 are suggested revision sizes, not GTU allocations. "
            "Model answers are in Notes section 5.",
            "અધિકૃત કોર્સ: થિયરી ESE 70 + PA 30 અને પ્રેક્ટિકલ PA 20 + ESE 30 = 150 માર્ક્સ, 4 ક્રેડિટ, "
            "45 શિક્ષણ કલાક; આ યુનિટનું વેઇટેજ 28 %, 45માંથી 12 કલાક અને 70 થિયરી માર્ક્સમાંથી 19 માર્ક્સ "
            "(PDFમાં ફક્ત વેઇટેજ છે, તેથી માર્ક્સ વેઇટેજ પ્રમાણે વહેંચ્યા છે). સરાવના 3/4/5 માર્ક્સ સૂચિત "
            "પુનરાવર્તન માપ છે, GTU ફાળવણી નહીં. આદર્શ જવાબો નોંધ વિભાગ 5માં છે."),
        "question_provenance": "Original answered revision questions; not official past papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": s["en"], "url": (s["en"].split("(")[-1].rstrip(")")
                                              if "http" in s["en"] else "https://syllabus.gtu.ac.in/")}
                    for s in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI01000121_unit3_preview.html"))
    from notes_workshop import render_one
    shelf_file = render_one("DI01000121", 3, note="Unit 3 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Applied Physics Unit 3: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{len(st['numericals'])} numericals / {sum(len(s['items']) for s in st['viva'])} viva / "
          f"{len(st['exam_questions'])} exam")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")


if __name__ == "__main__":
    main()
