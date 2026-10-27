"""Subject metadata for DI03000031 RDBMS (Computer Sem 3) – shared by all unit builders. English only, Oracle SQL programs."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem3", "DI03000031")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)

TABS = ["notes", "programs", "diagrams", "syntax", "viva", "exam"]
INTRO = {"en": "Detailed notes as per GTU syllabus with diagrams, solved Oracle SQL queries with real output, syntax and viva."}

SUBJECT = {
    "code": "DI03000031",
    "name": {"en": "Relational Database Management System"},
    "branch": "computer", "semester": 3, "syllabus_year": "2024-25", "type": "programming",
    "languages": ["en"], "code_lang": "sql",
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 4},
    "units": [
        {"no": 1, "title": {"en": "Introduction to Database System and SQL Commands"}, "hours": 12, "weightage": 27,
         "topics": ["1.1 Data, information, data item, record, file, metadata, data dictionary",
                    "1.2 Database, DBMS, database system environment and architecture",
                    "1.3 Schema, sub-schema and instance", "1.4 SQL data types",
                    "1.5 DDL, DML and DQL commands", "1.6 DCL: users, roles, GRANT and REVOKE",
                    "1.7 TCL: transactions, ACID, COMMIT, ROLLBACK, SAVEPOINT"], "file": None},
        {"no": 2, "title": {"en": "SQL Functions and Joins"}, "hours": 11, "weightage": 24,
         "topics": ["2.1 Operators: arithmetic, comparison, logical and special", "2.2 DUAL, numeric and character functions",
                    "2.3 Date and conversion functions", "2.4 Aggregate functions, GROUP BY, HAVING, ORDER BY",
                    "2.5 Joins: inner, outer, cross and self", "2.6 Sub-queries and set operators"], "file": None},
        {"no": 3, "title": {"en": "Normalization"}, "hours": 6, "weightage": 13,
         "topics": ["3.1 Normalization: definition and importance", "3.2 Functional dependency, 1NF, 2NF and 3NF",
                    "3.3 Advantages and disadvantages of normalization"], "file": None},
        {"no": 4, "title": {"en": "Integrity Constraints and Database Objects"}, "hours": 7, "weightage": 16,
         "topics": ["4.1 Integrity constraints: NOT NULL, CHECK, UNIQUE, PRIMARY KEY, FOREIGN KEY",
                    "4.2 Views", "4.3 Synonyms", "4.4 Sequences", "4.5 Indexes"], "file": None},
        {"no": 5, "title": {"en": "PL/SQL and Triggers"}, "hours": 9, "weightage": 20,
         "topics": ["5.1 PL/SQL basics, %TYPE and %ROWTYPE", "5.2 Control structures", "5.3 Cursors",
                    "5.4 Procedures and functions", "5.5 Triggers", "5.6 Exception handling"], "file": None},
    ],
    "practicals": [
        "Create, alter, rename, truncate and drop five tables (DDL)", "Insert, update and delete at least 10 rows (DML)",
        "TCL and DCL commands: COMMIT, ROLLBACK, SAVEPOINT, GRANT, REVOKE",
        "Date functions: ADD_MONTHS, MONTHS_BETWEEN, NEXT_DAY, LAST_DAY, SYSDATE, ROUND, TRUNC",
        "Numeric and character functions", "Conversion, aggregate functions and DECODE",
        "GROUP BY, HAVING and ORDER BY", "Set operators: UNION, UNION ALL, INTERSECT, MINUS",
        "Joins: inner, outer, cross and self", "Nested (3 levels) and correlated sub-queries",
        "Integrity constraints", "Create, alter and drop views", "Synonyms, sequences and indexes",
        "PL/SQL control structures", "Implicit and explicit cursors", "Exception handling",
        "Procedures and functions", "Triggers", "Normalize a given relation up to 3NF"],
    "books": ["S. K. Singh – Database Systems: Concepts, Design and Applications (Pearson)",
              "Ivan Bayross – SQL, PL/SQL: The Programming Language of Oracle (BPB)",
              "C. J. Date – An Introduction to Database Systems (Pearson)",
              "Silberschatz, Korth, Sudarshan – Database System Concepts (McGraw Hill)",
              "ITL ESL – Introduction to Database Management Systems (Pearson)"],
}


def write_subject():
    for u in SUBJECT["units"]:
        fn = f'unit{u["no"]}.json'
        u["file"] = fn if os.path.exists(os.path.join(SUBJ_DIR, fn)) else None
    with open(os.path.join(SUBJ_DIR, "subject.json"), "w", encoding="utf-8") as f:
        json.dump(SUBJECT, f, ensure_ascii=False, indent=1)


def check_and_write(unit, diagram_titles, preview_name):
    """Sanity checks shared by all unit builders, then writes unitN.json, subject.json and the preview."""
    from preview_builder import build_preview
    unit.setdefault("tabs", TABS)
    unit.setdefault("intro_text", INTRO)
    notes = unit["notes"]
    items = [it for s in notes for it in s["items"]]
    used_d = {it.get("diagram") for it in items} - {None}
    used_p = {p for it in items for p in it.get("programs", [])}
    used_n = {n for it in items for n in it.get("examples", [])}
    pids = [p["id"] for p in unit["programs"]]
    nids = [n["id"] for n in unit.get("numericals", [])]
    assert len(pids) == len(set(pids)), "duplicate program id"
    assert len(nids) == len(set(nids)), "duplicate numerical id"
    assert used_d == set(diagram_titles), set(diagram_titles) ^ used_d
    assert used_p == set(pids), set(pids) ^ used_p
    assert used_n <= set(nids), used_n - set(nids)
    for k in diagram_titles:
        assert os.path.exists(os.path.join(DIAG_DIR, k + ".svg")), k
    for it in items:
        for v in it["body"].values():
            assert "@@" not in v, it["h"]["en"]
    for p in unit["programs"]:
        for ln in p["code"]["en"].split("\n"):
            assert len(ln) <= 43, f'{p["id"]}: line too long ({len(ln)}): {ln}'
    with open(os.path.join(SUBJ_DIR, f'unit{unit["unit"]}.json'), "w", encoding="utf-8") as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(unit, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", preview_name))
    print("topics:", len(items), "programs:", len(pids), "diagrams:", len(diagram_titles),
          "algorithms:", sum(len(g["items"]) for g in unit.get("algorithms", [])),
          "numericals:", len(nids), "viva:", sum(len(g["items"]) for g in unit["viva"]),
          "exam:", len(unit["exam_questions"]))
    print("preview:", os.path.normpath(out))
