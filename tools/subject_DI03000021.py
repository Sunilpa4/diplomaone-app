"""Subject metadata for DI03000021 Data Structures (Computer Sem 3) – shared by all unit builders. English only, C programs."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem3", "DI03000021")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)

TABS = ["notes", "programs", "diagrams", "algorithms", "numericals", "viva", "exam"]

SUBJECT = {
    "code": "DI03000021",
    "name": {"en": "Data Structures"},
    "branch": "computer", "semester": 3, "syllabus_year": "2024-25", "type": "programming",
    "languages": ["en"], "code_lang": "c",
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 4},
    "units": [
        {"no": 1, "title": {"en": "Basic Concepts of Data Structures"}, "hours": 6, "weightage": 14,
         "topics": ["1.1 Data, data structure and its types", "1.2 Algorithms and their characteristics",
                    "1.3 Time and space complexity, asymptotic notations", "1.4 Arrays: representation, row and column major",
                    "1.5 Array operations: insert, update, delete, traverse, search"], "file": None},
        {"no": 2, "title": {"en": "Stack and Queues"}, "hours": 8, "weightage": 18,
         "topics": ["2.1 Stack: array representation, PUSH and POP", "2.2 Applications of stack, infix, prefix and postfix",
                    "2.3 Recursion: factorial, GCD, Fibonacci", "2.4 Queue: array representation, insert and delete",
                    "2.5 Circular queue and applications of queue"], "file": None},
        {"no": 3, "title": {"en": "Linked List"}, "hours": 11, "weightage": 24,
         "topics": ["3.1 Pointer, structure, structure using pointer, dynamic memory allocation",
                    "3.2 Linked list representation and types", "3.3 Insertion in singly linked list",
                    "3.4 Deletion, searching and counting nodes", "3.5 Applications of linked list"], "file": None},
        {"no": 4, "title": {"en": "Trees and Graph"}, "hours": 9, "weightage": 20,
         "topics": ["4.1 Tree terminology and binary trees", "4.2 Converting a general tree to a binary tree",
                    "4.3 Tree traversal: inorder, preorder, postorder", "4.4 Binary search tree: insert, delete, search",
                    "4.5 Graph terminology and types"], "file": None},
        {"no": 5, "title": {"en": "Sorting and Searching"}, "hours": 11, "weightage": 24,
         "topics": ["5.1 Bubble, selection and insertion sort", "5.2 Quick, merge and radix sort",
                    "5.3 Linear and binary search", "5.4 Hashing: hash table and hash functions"], "file": None},
    ],
    "practicals": [
        "Find the maximum of 10 numbers using an array and find the time complexity",
        "Implement PUSH and POP algorithms of a stack", "Implement recursive functions (factorial)",
        "Implement insert and delete algorithms of a queue", "Simple structure programs using pointers",
        "Insert a node in a singly linked list", "Delete a node from a singly linked list",
        "Count the number of nodes in a singly linked list", "Search a node in a singly linked list",
        "Construct a binary search tree", "Bubble sort", "Selection sort", "Insertion sort", "Binary search"],
    "books": ["Tremblay & Sorenson – An Introduction to Data Structures with Applications (TMH)",
              "Tanenbaum – Data Structures using C & C++ (PHI)", "Reema Thareja – Data and File Structures using C (Oxford)",
              "G. S. Baluja – Data Structures Through C (Dhanpat Rai)", "D. Samanta – Classic Data Structures (PHI)"],
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
    unit.setdefault("intro", "intro_ds")
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
            assert len(ln) <= 46, f'{p["id"]}: line too long ({len(ln)}): {ln}'
    with open(os.path.join(SUBJ_DIR, f'unit{unit["unit"]}.json'), "w", encoding="utf-8") as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(unit, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", preview_name))
    print("topics:", len(items), "programs:", len(pids), "diagrams:", len(diagram_titles),
          "algorithms:", sum(len(g["items"]) for g in unit.get("algorithms", [])),
          "numericals:", len(nids), "viva:", sum(len(g["items"]) for g in unit["viva"]),
          "exam:", len(unit["exam_questions"]))
    print("preview:", os.path.normpath(out))
