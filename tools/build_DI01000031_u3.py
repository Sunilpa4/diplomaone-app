"""Build Communication Skills in English (DI01000031) Unit 3 "Prose and Poetry".

Content JSON + five SVGs + a shelf preview page.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000031 import TABS, SUBJECT, DIAG_DIR, tr, write_unit  # noqa: E402
from content_DI01000031_u3_notes import (NOTES, EQUATIONS, VIVA, EXAM,  # noqa: E402
                                         PRACTICE_ANSWERS, SOURCES, LESSON_COUNT)
from diagrams_DI01000031_u3 import TITLES, ALL  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in ALL.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()

    assert len(PRACTICE_ANSWERS) == len(EXAM), "one model answer per practice question"
    NOTES[-1] = {
        "title": tr("4. Practice Questions with Model Answers"),
        "items": [{"h": tr(f"Practice {i}. {q['q']['en']}"), "body": PRACTICE_ANSWERS[i - 1]}
                  for i, q in enumerate(EXAM, 1)],
    }
    exam = [{"q": tr("Practice: " + e["q"]["en"]), "marks": e["marks"]} for e in EXAM]

    unit = {
        "subject": "DI01000031",
        "unit": 3,
        "format": "notes",
        "title": tr("Prose and Poetry"),
        "hours": 6,
        "weightage": 20,
        "official": True,
        "languages": ["en"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 3 of Communication Skills in English: Ruskin Bond's short story <i>The Leopard</i>, "
            "O. Henry's <i>After Twenty Years</i> and Robert Frost's poem <i>Stopping by Woods on a "
            "Snowy Evening</i>. Each text is treated in the same way - author and setting, a "
            "stanza-by-stanza or step-by-step summary, characters or voice, themes, devices and the "
            "lines worth quoting - and each closes with an answer plan. Fifteen answered questions "
            "are in section 4."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(t), "file": f"diagrams/{i}.svg"} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": [
            tr("CO3: Develop reading and listening skills in terms of fluency and comprehensibility."),
        ],
        "course_outcomes": ["CO3"],
        "practical_numbers": [],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT,
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "3 credits, 30 teaching hours; this unit carries 20 % weightage and 14 of the 70 theory "
            "marks. Practice-question marks (3/4) are suggested revision sizes, not official GTU "
            "allocations. Model answers are in Notes section 7."),
        "question_provenance": "Original answered revision questions; not official past papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR), str(ROOT / "preview/DI01000031_unit3_preview.html"))
    from notes_workshop import render_one
    shelf_file = render_one("DI01000031", 3, note="Unit 3 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Communication Skills in English Unit 3: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(s['items']) for s in st['viva'])} viva / {len(st['exam_questions'])} exam")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")


if __name__ == "__main__":
    main()
