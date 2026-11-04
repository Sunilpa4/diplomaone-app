"""DI05005031 Chemical Reaction Engineering - Unit 1 notes, assembled from parts A, B and C.

The unit is written in three files so that no single file becomes unmanageable:
    content_DI05005031_u1_a.py  sections 1.1 - 1.3  (scope, classification, direction and heat)
    content_DI05005031_u1_b.py  sections 1.4 - 1.5  (molecularity and order, enzymes)
    content_DI05005031_u1_c.py  sections 1.6 - 1.7, formulas, viva, solved numericals
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from content_DI05005031_u1_a import NOTES_A  # noqa: E402
from content_DI05005031_u1_b import NOTES_B  # noqa: E402
from content_DI05005031_u1_c import (NOTES_C, EQUATIONS, VIVA, PRACTICE, EXAM,  # noqa: E402
                                     PRACTICE_ANSWERS, SOURCES)

NOTES = NOTES_A + NOTES_B + NOTES_C
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)

__all__ = ["NOTES", "LESSON_COUNT", "EQUATIONS", "VIVA", "PRACTICE", "EXAM",
           "PRACTICE_ANSWERS", "SOURCES"]
