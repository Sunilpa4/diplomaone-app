"""Subject metadata for DI03000011 Digital Electronics Fundamentals (Computer Sem 3) - shared by all unit builders.
Bilingual (EN + GU), theory subject: notes, diagrams, equations, numericals, viva, exam."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem3", "DI03000011")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)

TABS = ["notes", "diagrams", "equations", "numericals", "viva", "exam"]


def _u(no, en, gu, h, w, topics):
    return {"no": no, "title": {"en": en, "gu": gu}, "hours": h, "weightage": w, "topics": topics, "file": None}


SUBJECT = {
    "code": "DI03000011",
    "name": {"en": "Digital Electronics Fundamentals", "gu": "ડિજિટલ ઇલેક્ટ્રોનિક્સ ફંડામેન્ટલ્સ"},
    "branch": "computer", "semester": 3, "syllabus_year": "2025-26", "type": "theory",
    "languages": ["en", "gu"],
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 3},
    "units": [
        _u(1, "Number Systems and Binary Codes", "Number Systems અને Binary Codes", 6, 20,
           ["1.1 Introduction to digital systems", "1.2 Binary, octal, decimal and hexadecimal number systems",
            "1.3 Conversion between number systems", "1.4 Binary addition and subtraction using 1's and 2's complement"]),
        _u(2, "Binary Logic and Boolean Algebra", "Binary Logic અને Boolean Algebra", 7, 23,
           ["2.1 Binary logic, positive and negative logic", "2.2 Logic gates: AND, OR, NOT, EX-OR, NOR, NAND, EX-NOR",
            "2.3 Boolean postulates and laws", "2.4 De Morgan's theorems and Boolean functions"]),
        _u(3, "Simplification using Karnaugh Map", "Karnaugh Map દ્વારા Simplification", 7, 23,
           ["3.1 Need for simplification", "3.2 Two, three and four variable K-maps", "3.3 Don't-care conditions",
            "3.4 Implementation using basic gates"]),
        _u(4, "Combinational Circuits", "Combinational Circuits", 7, 23,
           ["4.1 Half adder and full adder", "4.2 Half subtractor and full subtractor", "4.3 4-to-2 encoder and 2-to-4 decoder",
            "4.4 4-to-1 multiplexer and 1-to-4 demultiplexer"]),
        _u(5, "Sequential Circuits", "Sequential Circuits", 3, 11,
           ["5.1 Combinational vs sequential circuits", "5.2 SR, JK, D and T flip-flops"]),
    ],
    "practicals": [
        "Number system conversion", "Binary addition, subtraction, 1's and 2's complement",
        "Verify truth tables of basic logic gates", "Implement Boolean expressions using logic gates",
        "Simplify Boolean functions using K-map", "Half adder and full adder", "Half subtractor and full subtractor",
        "Multiplexer and demultiplexer", "Decoder and encoder", "SR, JK, D and T flip-flops"],
    "books": ["A. Anand Kumar – Fundamentals of Digital Circuits (PHI)", "M. Morris Mano – Digital Logic and Computer Design (Pearson)",
              "R. P. Jain – Modern Digital Electronics (McGraw-Hill)"],
}

BAD = re.compile(r"&amp;(lt|gt|amp);|&lt;b&gt;")


def write_subject():
    for u in SUBJECT["units"]:
        fn = f'unit{u["no"]}.json'
        u["file"] = fn if os.path.exists(os.path.join(SUBJ_DIR, fn)) else None
    with open(os.path.join(SUBJ_DIR, "subject.json"), "w", encoding="utf-8") as f:
        json.dump(SUBJECT, f, ensure_ascii=False, indent=1)


def _bi(d, where):
    assert isinstance(d, dict) and d.get("en") and d.get("gu"), f"missing en/gu: {where}"


def check_and_write(unit, diagram_titles, preview_name):
    from preview_builder import build_preview
    unit["tabs"] = TABS
    unit["diagrams"] = [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in diagram_titles.items()]
    items = [it for s in unit["notes"] for it in s["items"]]
    used_d = [it.get("diagram") for it in items if it.get("diagram")]
    used_n = {n for it in items for n in it.get("examples", [])}
    nids = [n["id"] for n in unit["numericals"]]
    assert len(nids) == len(set(nids)), "duplicate numerical id"
    assert set(used_d) == set(diagram_titles), set(diagram_titles) ^ set(used_d)
    assert used_n <= set(nids), used_n - set(nids)
    for k, v in diagram_titles.items():
        _bi(v, k)
        assert os.path.exists(os.path.join(DIAG_DIR, k + ".svg")), k
    for s in unit["notes"]:
        _bi(s["title"], "section")
        for it in s["items"]:
            _bi(it["h"], it["h"]); _bi(it["body"], it["h"]["en"])
    for n in unit["numericals"]:
        _bi(n["q"], n["id"]); _bi(n["a"], n["id"])
    for g in unit["viva"] + unit["equations"]:
        _bi(g["title"], "group")
    for x in unit["exam_questions"]:
        _bi(x["q"], x["q"])
    txt = json.dumps(unit, ensure_ascii=False)
    assert not BAD.search(txt), BAD.search(txt).group(0)
    assert "@@" not in txt
    with open(os.path.join(SUBJ_DIR, f'unit{unit["unit"]}.json'), "w", encoding="utf-8") as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(unit, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", preview_name))
    print("topics:", len(items), "diagrams:", len(diagram_titles), "equations:", sum(len(g["items"]) for g in unit["equations"]),
          "numericals:", len(nids), "viva:", sum(len(g["items"]) for g in unit["viva"]), "exam:", len(unit["exam_questions"]))
    print("preview:", os.path.normpath(out))
