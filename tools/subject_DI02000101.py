"""Subject metadata for DI02000101 Scripting Language (Python) – shared by all unit builders."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem2", "DI02000101")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)

SUBJECT = {
    "code": "DI02000101",
    "name": {"en": "Scripting Language (Python)"},
    "branch": "computer", "semester": 2, "syllabus_year": "2024-25", "type": "programming",
    "languages": ["en"], "code_lang": "python",
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 4},
    "units": [
        {"no": 1, "title": {"en": "Introduction and Syntax of Python Programming"}, "hours": 7, "weightage": 15,
         "topics": ["1.1 Introduction, history, features and applications", "1.2 Installing Python and structure of a program",
                    "1.3 Keywords, identifiers, variables, literals and constants", "1.4 Input-output functions and type casting",
                    "1.5 Data types: number, string, list, tuple, set, dictionary"], "file": None},
        {"no": 2, "title": {"en": "Operators and Control Flow Structures"}, "hours": 8, "weightage": 18,
         "topics": ["2.1 Operators and precedence", "2.2 Indentation, if, if-else, if-elif-else",
                    "2.3 while, for, range()", "2.4 break, continue, pass, return, nested loops"], "file": None},
        {"no": 3, "title": {"en": "Data Structures in Python"}, "hours": 8, "weightage": 18,
         "topics": ["3.1 Lists", "3.2 Tuples", "3.3 Sets", "3.4 Dictionaries"], "file": None},
        {"no": 4, "title": {"en": "Python Functions and File Handling"}, "hours": 12, "weightage": 27,
         "topics": ["4.1 Built-in conversion, math and string functions", "4.2 File handling functions",
                    "4.3 User-defined functions, recursion, scope"], "file": None},
        {"no": 5, "title": {"en": "Python Modules and Packages"}, "hours": 10, "weightage": 22,
         "topics": ["5.1 Modules and built-in math modules", "5.2 Packages", "5.3 Matplotlib", "5.4 NumPy"], "file": None},
    ],
    "practicals": [
        "Install and configure Python; run basic commands",
        "Read name, contact number, email and birth date and print them",
        "Create, access, update and delete operations on list, tuple, set and dictionary",
        "Conditional statements: if, if-else, if-elif-else",
        "Operators: arithmetic, logical, comparison, assignment, bitwise, membership, identity",
        "Looping: while, for and nested loops", "User-defined functions",
        "Math and string built-in functions", "Built-in and user-defined modules",
        "Built-in and user-defined packages", "String processing functions", "Basic file functions"],
    "books": ["R. Nageswara Rao – Core Python Programming", "John Zelle – Python Programming: An Introduction to Computer Science",
              "Charles Dierbach – Introduction to Computer Science Using Python", "Paul Barry – Head First Python",
              "Mark Lutz – Learning Python"],
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
    used_d |= {p.get("plot") for p in unit["programs"]} - {None}   # Matplotlib output plots
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
