"""Subject metadata for DI04000021 Object Oriented Programming - Java - shared by all unit builders."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem4", "DI04000021")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)

SUBJECT = {
    "code": "DI04000021",
    "name": {"en": "Object Oriented Programming - Java"},
    "branch": "computer", "semester": 4, "syllabus_year": "2025-26", "type": "programming",
    "languages": ["en"], "code_lang": "java",
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 4},
    "units": [
        {"no": 1, "title": {"en": "Introduction to Java Programming"}, "hours": 10, "weightage": 20,
         "topics": ["1.1 Introduction to Java, features and applications",
                    "1.2 JDK, JRE, JVM, byte code, program structure, Hello World",
                    "1.3 Data types, variables, scope, conversion, casting, operators",
                    "1.4 Control flow: if-else, switch, loops, break, continue",
                    "1.5 Arrays: 1D arrays, introduction to 2D arrays"], "file": None},
        {"no": 2, "title": {"en": "Object-Oriented Programming Concepts"}, "hours": 10, "weightage": 25,
         "topics": ["2.1 Principles of OOP: abstraction, encapsulation, inheritance, polymorphism",
                    "2.2 Classes, objects, fields and methods",
                    "2.3 Constructors: default, parameterized, overloading",
                    "2.4 Keywords: this and static",
                    "2.5 Access modifiers: public, private, protected, default",
                    "2.6 Methods: definition, calling, overloading",
                    "2.7 String class and common string methods",
                    "2.8 Wrapper classes, autoboxing and unboxing",
                    "2.9 User input: Scanner class, command line arguments",
                    "2.10 Garbage collection and finalize()"], "file": None},
        {"no": 3, "title": {"en": "Inheritance, Interfaces and Abstraction"}, "hours": 10, "weightage": 25,
         "topics": ["3.1 Inheritance: concept, need, types, super, overriding, dynamic method dispatch, final",
                    "3.2 Abstract classes and abstract methods",
                    "3.3 Interfaces: declaration, implementation, multiple inheritance, default and static methods",
                    "3.4 Packages: defining, importing, built-in packages"], "file": None},
        {"no": 4, "title": {"en": "Exception Handling and Collections Framework"}, "hours": 8, "weightage": 20,
         "topics": ["4.1 Errors and exceptions, exception hierarchy",
                    "4.2 try, catch, finally, throw, throws, multiple catch, built-in exceptions",
                    "4.3 Collections framework: ArrayList, HashSet, for-each loop"], "file": None},
        {"no": 5, "title": {"en": "Modern Java Features"}, "hours": 7, "weightage": 10,
         "topics": ["5.1 Overview of Java version updates from Java 7 onwards",
                    "5.2 Lambda expressions and Stream API",
                    "5.3 Introduction to AI with Java"], "file": None},
    ],
    "practicals": [
        "Hello World, arithmetic operations and type casting",
        "Control structures: maximum of three numbers, sum of digits",
        "Arrays: sum and average, addition of two matrices",
        "Student class with fields and methods; object creation",
        "Constructors, this and static keywords",
        "Method overloading",
        "String operations with built-in methods",
        "Scanner input; autoboxing and unboxing",
        "Single and multilevel inheritance (Person > Employee > Manager)",
        "Abstract class Shape, interface Drawable, Circle/Rectangle classes",
        "final keyword", "User-defined package: create, import and use",
        "Exception handling: divide by zero, null pointer, try-catch-finally",
        "Collections: ArrayList and HashSet operations with for-each",
        "Lambda expressions and Stream API: filter even numbers, uppercase strings"],
    
    "books": ["Cay S. Horstmann and Gary Cornell – Core Java Volume I: Fundamentals",
              "Herbert Schildt – Java: The Complete Reference",
              "Kathy Sierra and Bert Bates – Head First Java",
              "E. Balagurusamy – Programming in Java",
              "P. Radha Krishna – Java Programming"],
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
