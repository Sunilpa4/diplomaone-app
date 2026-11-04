"""Build Environmental Sustainability (DI02000051) Unit 4 - bilingual en + gu."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI02000051 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI02000051_u4_notes import (NOTES, EQUATIONS, NUMERICALS, VIVA, EXAM,  # noqa: E402
                                         PRACTICE_ANSWERS, SOURCES, LESSON_COUNT)
from diagrams_DI02000051_u4 import (TITLES, TITLES_GU, CAPTIONS, CAPTIONS_GU,  # noqa: E402
                                    DIAGRAMS)
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()
    spec = spec_for(4)
    assert len(PRACTICE_ANSWERS) == len(EXAM), "one model answer per practice question"

    NOTES.append({
        "title": tr("5. Practice Questions with Model Answers", "5. સરાવ પ્રશ્નો અને આદર્શ જવાબો"),
        "items": [{"h": tr(f"Practice {i}. {q['q']['en']}", f"સરાવ {i}. {q['q']['gu']}"),
                   "body": PRACTICE_ANSWERS[i - 1]}
                  for i, q in enumerate(EXAM, 1)],
    })
    exam = [{"q": tr("Practice: " + e["q"]["en"], "સરાવ: " + e["q"]["gu"]), "marks": e["marks"]}
            for e in EXAM]

    unit = {
        "subject": "DI02000051",
        "unit": 4,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 4 of Environmental Sustainability: the five parts of the climate system and the "
            "greenhouse effect; the gases, their global warming potential and their sources; the "
            "evidence - temperature records and proxies, melting ice, rising seas, shifting rain and "
            "extreme events, with the attribution method; the impacts on species, the ocean, dry land, "
            "health and the economy; and the mitigation ladder from efficiency and electrification "
            "through carbon capture and land sinks to net zero. Nine lecture cards, six diagrams, ten "
            "fully solved numericals and twelve answered practice questions.",
            "પર્યાવરણીય ટકાઉપણાનું યુનિટ 4: જળવાયુ પ્રણાલીના પાંચ ભાગ અને હરિતગૃહ પ્રભાવ; વાયુ, તેમની વૈશ્વિક "
            "ગરમી સંભાવના અને સ્રોત; પુરાવા - તાપમાન રેકોર્ડ અને પરોક્ષ પુરાવા, પીગળતો બરફ, વધતો દરિયો, બદલાતો "
            "વરસાદ અને આત્યંતિક ઘટનાઓ, કારણ નિર્ધારણની રીત સાથે; જાતિઓ, મહાસાગર, સૂકી જમીન, આરોગ્ય અને "
            "અર્થતંત્ર પર અસરો; અને કાર્યક્ષમતા તથા વીજીકરણથી કાર્બન પકડ અને જમીન શોષક થઈને નેટ ઝીરો સુધીનું "
            "શમન સોપાન. નવ પાઠ-કાર્ડ, છ આકૃતિઓ, દસ પૂરા ઉકેલાયેલા દાખલા અને બાર ઉત્તરસહિત સરાવ પ્રશ્નો."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(t, TITLES_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU[i])} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "numericals": NUMERICALS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO4"],
        "practical_numbers": [],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT,
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 = 100 marks, 2 credits, 30 teaching hours, no "
            "practical. This unit carries 20 % weightage, 6 of the 30 hours and 14 of the 70 theory "
            "marks (the PDF prints weightage only, so the marks are split by weightage). Practice "
            "marks 3/4/5 are suggested revision sizes, not GTU allocations. Model answers are in "
            "Notes section 5.",
            "અધિકૃત કોર્સ: થિયરી ESE 70 + PA 30 = 100 માર્ક્સ, 2 ક્રેડિટ, 30 શિક્ષણ કલાક, પ્રેક્ટિકલ નથી. "
            "આ યુનિટનું વેઇટેજ 20 %, 30માંથી 6 કલાક અને 70 થિયરી માર્ક્સમાંથી 14 માર્ક્સ (PDFમાં ફક્ત વેઇટેજ "
            "છે, તેથી માર્ક્સ વેઇટેજ પ્રમાણે વહેંચ્યા છે). સરાવના 3/4/5 માર્ક્સ સૂચિત પુનરાવર્તન માપ છે, GTU "
            "ફાળવણી નહીં. આદર્શ જવાબો નોંધ વિભાગ 5માં છે."),
        "question_provenance": "Original answered revision questions; not official past papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": s["en"], "url": ("https://syllabus.gtu.ac.in/" if "GTU" in s["en"]
                                               else "https://www.envis.nic.in/")}
                    for s in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI02000051_unit2_preview.html"))
    from notes_workshop import render_one
    shelf_file = render_one("DI02000051", 4, note="Unit 4 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Environmental Sustainability Unit 4: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{len(st['numericals'])} numericals / {sum(len(s['items']) for s in st['viva'])} viva / "
          f"{len(st['exam_questions'])} exam")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")


if __name__ == "__main__":
    main()
