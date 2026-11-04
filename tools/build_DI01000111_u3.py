"""Build Engineering Graphics (DI01000111) Unit 3 - Points and Lines, English only."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000111 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI01000111_u3_notes import (NOTES, EQUATIONS, VIVA, EXAM,  # noqa: E402
                                         PRACTICE_ANSWERS, SOURCES, LESSON_COUNT)
from diagrams_DI01000111_u3 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()
    spec = spec_for(3)
    assert len(PRACTICE_ANSWERS) == len(EXAM), "one model answer per solved problem"

    items = [{"h": tr(f"Problem {i}. {e['q']['en']}"), "body": PRACTICE_ANSWERS[i - 1]}
             for i, e in enumerate(EXAM, 1)]
    NOTES.append({"title": tr("4. Solved Drawing Problems, Step by Step"), "items": items})
    exam = [{"q": tr(e["q"]["en"]), "marks": e["marks"]} for e in EXAM]

    unit = {
        "subject": "DI01000111",
        "unit": 3,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "official": True,
        "languages": ["en"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 3 of Engineering Graphics: how a three-dimensional object becomes two views on "
            "paper. The two reference planes and the four quadrants are built first, then points are "
            "projected with their heights and depths, then lines are carried through every position - "
            "parallel to a plane, perpendicular to it, inclined to one plane and inclined to both - "
            "with the true length, the true inclinations and the traces drawn out of the projections. "
            "Every topic is a numbered construction on the sheet, and seven fully solved drawing "
            "problems follow in section 4."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(t), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i])} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO3"],
        "practical_numbers": [3],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT,
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "3 credits, 30 teaching hours (2 lecture + 2 practical). This unit carries 20 % "
            "weightage, 5 of the 30 hours and 14 of the 70 theory marks (the PDF prints weightage "
            "only, so the marks are split by weightage). The solved drawing problems in section 4 "
            "are revision constructions with suggested marks, not official GTU papers, and the "
            "syllabus allows any valid method in the exam, so the notes show one clear method for "
            "each curve and name the alternatives."),
        "question_provenance": "Original solved drawing problems written for revision; not official "
                               "past papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR), str(ROOT / "preview/DI01000111_unit3_preview.html"))
    from notes_workshop import render_one
    shelf_file = render_one("DI01000111", 3, note="Unit 3 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Engineering Graphics Unit 3: {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")


if __name__ == "__main__":
    main()
