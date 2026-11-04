"""DI05005031 Unit 5 notes, assembled from parts A, B and C."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from content_DI05005031_u5_a import NOTES_A  # noqa: E402
from content_DI05005031_u5_b import NOTES_B  # noqa: E402
from content_DI05005031_u5_c import (NOTES_C, EQUATIONS, VIVA, PRACTICE, EXAM,  # noqa: E402
                                     PRACTICE_ANSWERS, SOURCES)

NOTES = NOTES_A + NOTES_B + NOTES_C
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)

__all__ = ["NOTES", "LESSON_COUNT", "EQUATIONS", "VIVA", "PRACTICE", "EXAM",
           "PRACTICE_ANSWERS", "SOURCES"]
