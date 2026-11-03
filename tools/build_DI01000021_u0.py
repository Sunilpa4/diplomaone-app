"""Build Mathematics-I (DI01000021) Unit 0 "Start Mathematics From Zero": content JSON + diagrams + previews."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000021 import TABS, SUBJECT, DIAG_DIR, tr, write_unit  # noqa: E402
from content_DI01000021_u0_notes import (NOTES, NUMERICALS, EQUATIONS, VIVA, EXAM,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI01000021_u0 import TITLES, ALL  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in ALL.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()

    unit = {
        "subject": "DI01000021",
        "unit": 0,
        "format": "notes",
        "title": tr("Start Mathematics From Zero (Foundation)"),
        "hours": 0,
        "weightage": 0,
        "official": False,
        "foundation": True,
        "languages": ["en"],
        "tabs": TABS[:],
        "intro_text": tr("Our own foundation chapter, written for students who reach diploma Mathematics-I "
                         "without the school-level tools the GTU syllabus assumes. It rebuilds numbers and "
                         "signs, fractions, LCM and GCD, BODMAS, indices and surds, standard form, algebraic "
                         "expansion and factorisation, linear and simultaneous equations, quadratic equations, "
                         "sets, ratio, percentage, averages and the coordinate plane - then adds a five-step "
                         "study method and an exam plan. Twenty-two fully solved numericals, and every definition "
                         "written in the same style as the official units. This chapter carries no GTU hours or "
                         "marks."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(t), "file": f"diagrams/{i}.svg"} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "numericals": NUMERICALS,
        "viva": VIVA,
        "exam_questions": EXAM,
        "learning_outcomes": [
            tr("Use fractions, powers, roots and standard form without a calculator."),
            tr("Expand and factorise algebraic expressions, and check the result by expanding back."),
            tr("Solve linear, simultaneous and quadratic equations, including word problems."),
            tr("Work with sets, ratio, percentage and averages in engineering contexts."),
            tr("Read the coordinate plane and compute distance, midpoint and slope."),
        ],
        "course_outcomes": [],
        "practical_numbers": [],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT,
        "answered_practice_count": len(EXAM),
        "assessment_note": tr("This is a DiplomaOne foundation chapter, not a GTU syllabus unit: it carries no "
                              "official hours, weightage or marks. Practice marks are suggested revision sizes. "
                              "Model answers are in Notes section 9."),
        "question_provenance": "Original answered revision questions; not official past papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR), str(ROOT / "preview/DI01000021_unit0_preview.html"))
    from notes_workshop import render_one
    shelf_file = render_one("DI01000021", 0, note="Unit 0 (foundation) draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Mathematics-I Unit 0: {len(st['notes'])} sections / {cards} cards / {len(st['diagrams'])} SVGs / "
          f"{len(st['numericals'])} numericals / {sum(len(s['items']) for s in st['viva'])} viva / "
          f"{len(st['exam_questions'])} exam")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")
    print("        preview/DI01000021_unit0_preview.html")


if __name__ == "__main__":
    main()
