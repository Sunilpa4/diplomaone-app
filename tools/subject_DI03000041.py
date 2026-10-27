"""Subject metadata for DI03000041 Fundamentals of Operating System (Computer Sem 3) - shared by all unit builders.
Bilingual (EN + GU), theory subject: notes, diagrams, numericals (where useful), viva, exam."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem3", "DI03000041")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)

TABS = ["notes", "diagrams", "equations", "numericals", "viva", "exam"]


def _u(no, en, gu, h, w, topics):
    return {"no": no, "title": {"en": en, "gu": gu}, "hours": h, "weightage": w, "topics": topics, "file": None}


SUBJECT = {
    "code": "DI03000041",
    "name": {"en": "Fundamentals of Operating System", "gu": "ફંડામેન્ટલ્સ ઓફ ઓપરેટિંગ સિસ્ટમ"},
    "branch": "computer", "semester": 3, "syllabus_year": "2025-26", "type": "theory",
    "languages": ["en", "gu"],
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 4},
    "units": [
        _u(1, "Introduction of Operating System", "Operating System નો પરિચય", 6, 13,
           ["1.1 Goals and services of OS", "1.2 Types of operating systems", "1.3 OS structure: layered, monolithic, microkernel",
            "1.4 Case study: Linux, Windows, macOS"]),
        _u(2, "Concepts of Process", "Process ના Concepts", 14, 31,
           ["2.1 Process, threads, process states, PCB", "2.2 Scheduling criteria and algorithms (FCFS, SJF, RR, Priority)",
            "2.3 Schedulers, queues, context switch", "2.4 Process synchronization", "2.5 Deadlock"]),
        _u(3, "Memory Management", "Memory Management", 10, 23,
           ["3.1 Logical and physical address, swapping", "3.2 Contiguous allocation, fragmentation, first/best/worst fit",
            "3.3 Paging and segmentation", "3.4 Page replacement: FIFO, LRU"]),
        _u(4, "File System", "File System", 6, 13,
           ["4.1 Files: attributes, operations, types, paths, protection", "4.2 Directory structures",
            "4.3 Disk space allocation methods", "4.4 Disk structure and scheduling: SCAN, C-SCAN"]),
        _u(5, "Unix/Linux Operating System", "Unix/Linux Operating System", 9, 20,
           ["5.1 Linux introduction and architecture", "5.2 Shell and basic commands", "5.3 Editors: vi, vim, gedit, gcc",
            "5.4 Basic shell scripts"]),
    ],
    "practicals": [
        "Compare Windows, Linux and Mac OS (latest versions)", "Process scheduling: FCFS, SJF and Round Robin with Gantt chart",
        "First fit, best fit and worst fit allocation", "Page replacement using FIFO and LRU", "Disk scheduling using SCAN and C-SCAN",
        "Basic Unix commands", "Advanced Unix commands", "File editing with vi, vim, gedit and gcc",
        "Shell script: read from command line and print Hello", "Shell script: display a file and append one file to another",
        "Shell script: convert a lower-case string to upper case", "Shell script: add two numbers"],
    "books": ["Silberschatz, Galvin, Gagne – Operating System Concepts (Wiley)", "Sumitabha Das – Unix Concepts and Applications (McGraw-Hill)",
              "Andrew Tanenbaum, Herbert Bos – Modern Operating Systems (Pearson)", "Milan Milenkovic – Operating Systems (McGraw-Hill)"],
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
    unit["tabs"] = [t for t in TABS if not (t == "equations" and not unit["equations"]) and not (t == "numericals" and not unit["numericals"])]
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
