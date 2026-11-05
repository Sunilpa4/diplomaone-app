"""DI01000181 Unit 1 notes, assembled from parts A, B, C and D."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from content_DI01000181_u1_a import NOTES_A  # noqa: E402
from content_DI01000181_u1_b import NOTES_B  # noqa: E402
from content_DI01000181_u1_c import NOTES_C  # noqa: E402
from content_DI01000181_u1_d import (NOTES_D, EQUATIONS, VIVA, PRACTICE, EXAM,  # noqa: E402
                                     PRACTICE_ANSWERS, SOURCES)

NOTES = NOTES_A + NOTES_B + NOTES_C + NOTES_D
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)

__all__ = ["NOTES", "LESSON_COUNT", "EQUATIONS", "VIVA", "PRACTICE", "EXAM",
           "PRACTICE_ANSWERS", "SOURCES"]
