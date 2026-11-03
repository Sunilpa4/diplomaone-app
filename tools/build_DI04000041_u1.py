"""Build Cloud Computing (DI04000041) Unit 1: content JSON + diagrams + review previews."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI04000041 import TABS, SUBJECT, DIAG_DIR, tr, write_unit  # noqa: E402
from content_DI04000041_u1_notes import (NOTES, NUMERICALS, EQUATIONS, VIVA, EXAM,  # noqa: E402
                                         ANSWERED, SOURCES, LESSON_COUNT)
from diagrams_DI04000041_u1 import TITLES, main as draw  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def main():
    draw()

    unit = {
        "subject": "DI04000041",
        "unit": 1,
        "format": "notes",
        "title": tr("Introduction to Cloud Computing"),
        "hours": 6,
        "weightage": 17,
        "languages": ["en"],
        "tabs": TABS[:],
        "intro_text": tr("Unit 1 of Cloud Computing: what cloud computing is (and is not), the six central "
                         "ideas, the five essential characteristics, the challenges that come with them, novel "
                         "applications including green-hydrogen analytics, the security risks under shared "
                         "responsibility, and a cost/availability comparison. Eight worked numericals with "
                         "recomputed answers; practice questions are original and their marks are suggested, "
                         "not official GTU allocations."),
        "notes": NOTES + [ANSWERED],
        "diagrams": [{"id": i, "title": tr(t), "file": f"diagrams/{i}.svg"} for i, t in TITLES.items()],
        "equations": EQUATIONS,
        "numericals": NUMERICALS,
        "viva": VIVA,
        "exam_questions": EXAM,
        "learning_outcomes": [tr("CO1: Describe the principles and paradigm of cloud computing.")],
        "practical_numbers": [1],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT,
        "answered_practice_count": len(EXAM),
        "assessment_note": tr("Official course: theory ESE 70 + PA 30, practical PA 20 + ESE 30 = 150 marks, "
                              "4 credits. Practice-question marks (3/4/7) are suggested revision sizes, not "
                              "official GTU allocations or a guaranteed paper pattern. Model answers are in "
                              "Notes section 8."),
        "question_provenance": "Original answered revision questions; not official past papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    # repo-convention preview (kept with the other unit previews)
    build_preview(unit, SUBJECT, str(DIAG_DIR), str(ROOT / "preview/DI04000041_unit1_preview.html"))
    # review shelf: only units authored in this session appear here
    from notes_workshop import render_one
    shelf_file = render_one("DI04000041", 1, note="Unit 1 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Cloud Computing Unit 1: {len(st['notes'])} sections / {cards} cards / {len(st['diagrams'])} SVGs / "
          f"{len(st['numericals'])} numericals / {sum(len(s['items']) for s in st['viva'])} viva / "
          f"{len(st['exam_questions'])} exam")
    print("unit:   ", out.relative_to(ROOT))
    print("preview:", Path(shelf_file).relative_to(ROOT), "(shelf)")
    print("        preview/DI04000041_unit1_preview.html")


if __name__ == "__main__":
    main()
