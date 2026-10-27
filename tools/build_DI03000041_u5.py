"""Builds DI03000041 Fundamentals of Operating System Unit 5 (Unix/Linux Operating System). Bilingual EN + GU.
Has programs (shell scripts with real bash output) and a syntax tab; no equations / numericals."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000041 import check_and_write
from content_DI03000041_u5_notes import NOTES
from content_DI03000041_u5_programs import PROGRAMS
from content_DI03000041_u5_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "os5_arch": {"en": "Architecture of Unix / Linux", "gu": "Unix / Linux નું Architecture"},
    "os5_kernel": {"en": "Linux System Structure", "gu": "Linux System Structure"},
    "os5_fs_tree": {"en": "Linux Directory Hierarchy", "gu": "Linux Directory Hierarchy"},
    "os5_shell": {"en": "How the Shell Executes a Command", "gu": "Shell command કેવી રીતે ચલાવે છે"},
    "os5_ls_l": {"en": "Fields of ls -l Output", "gu": "ls -l Output ના Fields"},
    "os5_vi_modes": {"en": "Modes of the vi / vim Editor", "gu": "vi / vim Editor ના Modes"},
    "os5_gcc": {"en": "Compiling a C Program with gcc", "gu": "gcc વડે C Program Compile કરવો"},
    "os5_if": {"en": "if ... else ... fi", "gu": "if ... else ... fi"},
    "os5_case": {"en": "case ... esac (menu)", "gu": "case ... esac (menu)"},
    "os5_while": {"en": "while Loop", "gu": "while Loop"},
    "os5_for": {"en": "for Loop", "gu": "for Loop"},
}

UNIT = {
    "subject": "DI03000041", "unit": 5, "format": "notes",
    "title": {"en": "Unix/Linux Operating System", "gu": "Unix/Linux Operating System"},
    "weightage": 20, "hours": 9,
    "intro": "intro_d",
    "intro_text": {
        "en": "Detailed notes as per GTU syllabus with diagrams, real command outputs, solved shell scripts, syntax and viva.",
        "gu": "GTU syllabus મુજબ આકૃતિઓ, commands ના ખરા output, ઉકેલેલી shell scripts, syntax અને viva સાથે વિગતવાર નોટ્સ.",
    },
    "notes": NOTES,
    "programs": PROGRAMS, "syntax": SYNTAX,
    "numericals": [], "equations": [], "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000041_u5.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000041_unit5_preview.html")
