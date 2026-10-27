"""Subject metadata for DI01000131 Computer Programming Fundamentals (shared by all unit builders)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem1", "DI01000131")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")

SUBJECT = {
    "code": "DI01000131",
    "name": {"en": "Computer Programming Fundamentals", "gu": "કમ્પ્યુટર પ્રોગ્રામિંગ ફન્ડામેન્ટલ્સ"},
    "branch": "computer", "semester": 1, "syllabus_year": "2024-25", "type": "programming", "languages": ["en"],
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 4},
    "units": [
        {"no": 1, "title": {"en": "Flowchart, Algorithm, Basics of C, Operators", "gu": "Flowchart, Algorithm, C ના મૂળભૂત ખ્યાલો, Operators"},
         "hours": 8, "weightage": 20,
         "topics": ["1.1 Flowchart", "1.2 Algorithm", "1.3 Overview of C", "1.4 Constants, Variables and Data Types",
                    "1.5 Managing Input and Output Operations", "1.6 Operators and Expressions"], "file": None},
        {"no": 2, "title": {"en": "Decision Making, Branching and Looping", "gu": "Decision Making, Branching અને Looping"},
         "hours": 10, "weightage": 22,
         "topics": ["2.1 Decision making with if, if-else, nested if, else-if ladder", "2.2 switch and goto",
                    "2.3 Looping: while, do-while, for", "2.4 break and continue"], "file": None},
        {"no": 3, "title": {"en": "Arrays and Pointers", "gu": "Arrays અને Pointers"}, "hours": 8, "weightage": 20,
         "topics": ["3.1 One-dimensional arrays", "3.2 Two-dimensional arrays", "3.3 Introduction to pointers",
                    "3.4 void and null pointers"], "file": None},
        {"no": 4, "title": {"en": "User-defined Functions", "gu": "User-defined Functions"}, "hours": 10, "weightage": 24,
         "topics": ["4.1 Need and elements of functions", "4.2 Category of functions", "4.3 Passing arrays to functions",
                    "4.4 Recursion", "4.5 Scope, visibility and lifetime of variables"], "file": None},
        {"no": 5, "title": {"en": "Strings and Files", "gu": "Strings અને Files"}, "hours": 9, "weightage": 14,
         "topics": ["5.1 Declaring, initializing, reading and writing strings", "5.2 String-handling functions",
                    "5.3 Command line arguments", "5.4 Text files: open, close, read, write"], "file": None},
    ],
    "practicals": [
        "Practice using Scratch / Snap programming", "Flowchart and algorithm for problem statements",
        "Programs using constants, variables, data types and operators", "Formatted and unformatted I/O",
        "Decision making: if, if-else, nested if, else-if ladder, switch, goto", "Loops: for, while, do-while",
        "break and continue", "One- and two-dimensional arrays", "Pointers", "User-defined functions", "Recursion",
        "String functions", "File operations", "Command line arguments"],
    "books": ["E. Balagurusamy – Programming in ANSI C", "Ashok N. Kamthane – Programming with ANSI and Turbo C",
              "Yashavant Kanetkar – Let Us C", "Reema Thareja – Introduction to C Programming"],
}


def write_subject():
    for u in SUBJECT["units"]:
        fn = f'unit{u["no"]}.json'
        u["file"] = fn if os.path.exists(os.path.join(SUBJ_DIR, fn)) else None
    with open(os.path.join(SUBJ_DIR, "subject.json"), "w", encoding="utf-8") as f:
        json.dump(SUBJECT, f, ensure_ascii=False, indent=1)


def en_only(o):
    """Recursively drop Gujarati ('gu') entries – this subject is English only."""
    if isinstance(o, dict):
        return {k: en_only(v) for k, v in o.items() if k != "gu"}
    if isinstance(o, list):
        return [en_only(v) for v in o]
    return o


def check_and_write(unit, diagram_titles, preview_name):
    """Sanity checks shared by all unit builders, then writes unitN.json, subject.json and the preview."""
    from preview_builder import build_preview
    if SUBJECT.get("languages") == ["en"]:
        unit = en_only(unit)
        for u in SUBJECT["units"]:
            u["title"] = en_only(u["title"])
    notes = unit["notes"]
    used_d = {it.get("diagram") for s in notes for it in s["items"]} - {None}
    used_p = {p for s in notes for it in s["items"] for p in it.get("programs", [])}
    pids = [p["id"] for p in unit["programs"]]
    assert len(pids) == len(set(pids)), "duplicate program id"
    assert used_d == set(diagram_titles), set(diagram_titles) ^ used_d
    assert used_p == set(pids), set(pids) ^ used_p
    for k in diagram_titles:
        assert os.path.exists(os.path.join(DIAG_DIR, k + ".svg")), k
    for s in notes:  # every @@snippet@@ must be expanded
        for it in s["items"]:
            for v in it["body"].values():
                assert "@@" not in v, it["h"]["en"]
    with open(os.path.join(SUBJ_DIR, f'unit{unit["unit"]}.json'), "w", encoding="utf-8") as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(unit, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", preview_name))
    print("topics:", sum(len(s["items"]) for s in notes), "programs:", len(unit["programs"]),
          "diagrams:", len(diagram_titles), "syntax:", sum(len(g["items"]) for g in unit["syntax"]),
          "viva:", sum(len(g["items"]) for g in unit["viva"]), "exam:", len(unit["exam_questions"]))
    print("preview:", os.path.normpath(out))
