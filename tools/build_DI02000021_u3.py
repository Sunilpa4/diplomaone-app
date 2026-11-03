"""Build Engineering Mathematics (DI02000021) Unit 3 "Integration and its Applications"."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI02000021 import TABS, SUBJECT, DIAG_DIR, tr, write_unit  # noqa: E402
from content_DI02000021_u3_notes import (NOTES, NUMERICALS, EQUATIONS, VIVA, EXAM,  # noqa: E402
                                         PRACTICE_ANSWERS, SOURCES, LESSON_COUNT)
from diagrams_DI02000021_u3 import TITLES, ALL  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in ALL.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()

    assert len(PRACTICE_ANSWERS) == len(EXAM), "one model answer per practice question"
    NOTES[-1] = {
        "title": tr("8. Practice Questions with Model Answers"),
        "items": [{"h": tr(f"Practice {i}. {q['q']['en']}"), "body": PRACTICE_ANSWERS[i - 1]}
                  for i, q in enumerate(EXAM, 1)],
    }
    exam = [{"q": tr("Practice: " + e["q"]["en"]), "marks": e["marks"]} for e in EXAM]

    unit = {
        "subject": "DI02000021",
        "unit": 3,
        "format": "notes",
        "title": tr("Integration and its Applications"),
        "hours": 10,
        "weightage": 20,
        "official": True,
        "languages": ["en"],
        "tabs": TABS[:],
        "intro_text": tr("Unit 3 of Engineering Mathematics: integration as the reverse of differentiation, "
                         "the standard integrals and working rules, substitution, integration by parts, the "
                         "definite integral with its properties, and the two applications - the area under "
                         "a curve and the volume of revolution. Twenty-five fully solved numericals, each "
                         "linked to a card."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(t), "file": f"diagrams/{i}.svg"} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "numericals": NUMERICALS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": [
            tr("CO3: Demonstrate the ability to solve engineering related problems based on applications "
               "of integration."),
        ],
        "course_outcomes": ["CO3"],
        "practical_numbers": [],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT,
        "answered_practice_count": len(exam),
        "assessment_note": tr("Official course: theory ESE 70 + PA 30 = 100 marks, 4 credits, 45 teaching "
                              "hours; this unit carries 20 % weightage and about 14 of the 70 theory marks. "
                              "Practice-question marks (3/4) are suggested revision sizes, not official GTU "
                              "allocations or a guaranteed paper pattern. Model answers are in Notes "
                              "section 8."),
        "question_provenance": "Original answered revision questions; not official past papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR), str(ROOT / "preview/DI02000021_unit3_preview.html"))
    from notes_workshop import render_one
    shelf_file = render_one("DI02000021", 3, note="Unit 3 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Engineering Mathematics Unit 3: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / {len(st['numericals'])} numericals "
          f"/ {sum(len(s['items']) for s in st['viva'])} viva / {len(st['exam_questions'])} exam")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")


if __name__ == "__main__":
    main()
