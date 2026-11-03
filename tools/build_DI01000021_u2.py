"""Build Mathematics-I (DI01000021) Unit 2 "Trigonometry": content JSON + diagrams + previews."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000021 import TABS, SUBJECT, DIAG_DIR, tr, write_unit  # noqa: E402
from content_DI01000021_u2_notes import (NOTES, NUMERICALS, EQUATIONS, VIVA, EXAM,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI01000021_u2 import TITLES, ALL  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in ALL.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()

    unit = {
        "subject": "DI01000021",
        "unit": 2,
        "format": "notes",
        "title": tr("Trigonometry"),
        "hours": 12,
        "weightage": 20,
        "official": True,
        "languages": ["en"],
        "tabs": TABS[:],
        "intro_text": tr("Unit 2 of Mathematics-I: angles in degrees and radians with arc length, sector "
                         "area and angular speed; the six trigonometric functions and the ASTC signs; allied "
                         "angles; compound angles sin(A ± B), cos(A ± B) and tan(A ± B); multiple and "
                         "submultiple (double, half and triple) angles; the graphs of sine and cosine with "
                         "amplitude, period and phase; the sum and factor formulae in both directions; and "
                         "inverse trigonometric functions with their principal ranges. Twenty-six fully solved "
                         "numericals, every one linked to a card."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(t), "file": f"diagrams/{i}.svg"} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "numericals": NUMERICALS,
        "viva": VIVA,
        "exam_questions": EXAM,
        "learning_outcomes": [
            tr("CO2: Demonstrate the ability to algebraically analyse basic functions used in trigonometry."),
        ],
        "course_outcomes": ["CO2"],
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

    build_preview(unit, SUBJECT, str(DIAG_DIR), str(ROOT / "preview/DI01000021_unit2_preview.html"))
    from notes_workshop import render_one
    shelf_file = render_one("DI01000021", 2, note="Unit 2 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Mathematics-I Unit 2: {len(st['notes'])} sections / {cards} cards / {len(st['diagrams'])} SVGs / "
          f"{len(st['numericals'])} numericals / {sum(len(s['items']) for s in st['viva'])} viva / "
          f"{len(st['exam_questions'])} exam")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")


if __name__ == "__main__":
    main()
