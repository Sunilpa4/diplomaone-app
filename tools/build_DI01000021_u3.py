"""Build Mathematics-I (DI01000021) Unit 3 "Vectors": content JSON + diagrams + previews."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000021 import TABS, SUBJECT, DIAG_DIR, tr, write_unit  # noqa: E402
from content_DI01000021_u3_notes import (NOTES, NUMERICALS, EQUATIONS, VIVA, EXAM,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI01000021_u3 import TITLES, ALL  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in ALL.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()

    unit = {
        "subject": "DI01000021",
        "unit": 3,
        "format": "notes",
        "title": tr("Vectors"),
        "hours": 9,
        "weightage": 20,
        "official": True,
        "languages": ["en"],
        "tabs": TABS[:],
        "intro_text": tr("Unit 3 of Mathematics-I: what a vector is and how it differs from a scalar; "
                         "magnitude, unit vector and direction cosines; addition by the triangle and "
                         "parallelogram laws, subtraction and position vectors, and the i j k component form; "
                         "the scalar product with its properties, the angle between two vectors and "
                         "projections; the vector product with its determinant form, properties and the area of "
                         "a parallelogram and a triangle; and the two applications the syllabus names - work "
                         "done (F · d) and moment of force (r × F). Twenty-six fully solved numericals."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(t), "file": f"diagrams/{i}.svg"} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "numericals": NUMERICALS,
        "viva": VIVA,
        "exam_questions": EXAM,
        "learning_outcomes": [
            tr("CO3: Demonstrate the ability to crack engineering related problems based on concepts of vectors."),
        ],
        "course_outcomes": ["CO3"],
        "practical_numbers": [],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT,
        "answered_practice_count": len(EXAM),
        "assessment_note": tr("Official course: theory ESE 70 + PA 30 = 100 marks, 4 credits; this unit carries "
                              "20 % weightage and about 14 of the 70 theory marks. Practice-question marks "
                              "(3/4) are suggested revision sizes, not official GTU allocations or a guaranteed "
                              "paper pattern. Model answers are in Notes section 7."),
        "question_provenance": "Original answered revision questions; not official past papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR), str(ROOT / "preview/DI01000021_unit3_preview.html"))
    from notes_workshop import render_one
    shelf_file = render_one("DI01000021", 3, note="Unit 3 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Mathematics-I Unit 3: {len(st['notes'])} sections / {cards} cards / {len(st['diagrams'])} SVGs / "
          f"{len(st['numericals'])} numericals / {sum(len(s['items']) for s in st['viva'])} viva / "
          f"{len(st['exam_questions'])} exam")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")


if __name__ == "__main__":
    main()
