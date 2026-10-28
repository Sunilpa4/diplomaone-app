"""Subject metadata for DI04000011 Software Engineering (Computer Sem 4).
English-only theory subject: notes, diagrams, syntax-cards, viva, exam."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem4", "DI04000011")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)

TABS = ["notes", "diagrams", "syntax", "viva", "exam"]


def _u(no, en, h, w, topics):
    return {"no": no, "title": {"en": en}, "hours": h, "weightage": w, "topics": topics, "file": None}


SUBJECT = {
    "code": "DI04000011",
    "name": {"en": "Software Engineering"},
    "branch": "computer", "semester": 4, "syllabus_year": "2025-26", "type": "theory",
    "languages": ["en"],
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 4},
    "units": [
        _u(1, "Software Process Models", 11, 26,
           ["1.1 Defining software and application domains (system, application, embedded, web, AI, green-hydrogen software)",
            "1.2 Software engineering layers, generic process model, framework and umbrella activities",
            "1.3 Traditional models: waterfall, incremental, prototype, spiral, V-model",
            "1.4 Agile approach: principles, Scrum, Extreme Programming"]),
        _u(2, "Software Requirement Analysis and Design", 15, 28,
           ["2.1 Requirement gathering and analysis; functional vs non-functional requirements",
            "2.2 Software Requirement Specification (SRS) and its characteristics",
            "2.3 Good software design; analysis vs design; cohesion and coupling",
            "2.4 Function-oriented design: DFD - context level and level 1",
            "2.5 Object-oriented modelling with UML: use case, class, component, sequence, activity diagrams"]),
        _u(3, "Software Project Estimation and Scheduling", 11, 26,
           ["3.1 Responsibilities of a software project manager",
            "3.2 Size metrics: Lines of Code and Function Points",
            "3.3 Project estimation with the COCOMO model",
            "3.4 Project scheduling: Gantt chart, flow chart, sprint burndown chart",
            "3.5 Risk management: identification, assessment, mitigation, monitoring"]),
        _u(4, "Software Coding and Testing", 8, 20,
           ["4.1 Coding standards and guidelines; code walkthrough and inspection",
            "4.2 Software documentation: internal and external",
            "4.3 Testing fundamentals; black-box and white-box testing",
            "4.4 Alpha and beta testing; unit and integration testing; test case template"]),
    ],
    "practicals": [
        "Describe software development models with appropriate diagrams",
        "Write a problem statement defining the project title with bounded scope",
        "Select a relevant process model and define activities/tasks for the project",
        "Gather application-specific requirements",
        "Prepare a broad SRS for the selected project",
        "Develop DFDs and E-R diagram for the project",
        "Prepare use cases and draw the use-case diagram",
        "Develop a class diagram for the project",
        "Develop a component diagram for the project",
        "Develop a sequence diagram for the project",
        "Develop an activity diagram for the project",
        "Evaluate project size using the Function Point metric",
        "Estimate project cost using COCOMO / COCOMO II",
        "Track progress with flow charts, Gantt charts (or sprint burndown for agile)",
        "Prepare test cases for the selected project"],
    "books": ["Roger S. Pressman – Software Engineering: A Practitioner's Approach",
              "Rajib Mall – Fundamentals of Software Engineering",
              "Blaha and Rumbaugh – Object Oriented Modeling and Design with UML"],
}


def write_subject():
    for u in SUBJECT["units"]:
        fn = f'unit{u["no"]}.json'
        u["file"] = fn if os.path.exists(os.path.join(SUBJ_DIR, fn)) else None
    with open(os.path.join(SUBJ_DIR, "subject.json"), "w", encoding="utf-8") as f:
        json.dump(SUBJECT, f, ensure_ascii=False, indent=1)


def check_and_write(unit, diagram_titles, preview_name):
    """Sanity checks shared by all SE unit builders, then writes unitN.json, subject.json and the preview."""
    from preview_builder import build_preview
    unit["tabs"] = [t for t in TABS if t != "syntax" or "syntax" in unit]
    unit["diagrams"] = [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in diagram_titles.items()]
    notes = unit["notes"]
    used_d = {it.get("diagram") for s in notes for it in s["items"]} - {None}
    assert used_d == set(diagram_titles), set(diagram_titles) ^ used_d
    for k in diagram_titles:
        assert os.path.exists(os.path.join(DIAG_DIR, k + ".svg")), k
    for s in notes:
        for it in s["items"]:
            assert "@@" not in it["body"]["en"], it["h"]["en"]
    with open(os.path.join(SUBJ_DIR, f'unit{unit["unit"]}.json'), "w", encoding="utf-8") as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(unit, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", preview_name))
    print("topics:", sum(len(s["items"]) for s in notes),
          "diagrams:", len(diagram_titles),
          "syntax:", sum(len(g["items"]) for g in unit.get("syntax", [])),
          "viva:", sum(len(g["items"]) for g in unit["viva"]),
          "exam:", len(unit["exam_questions"]))
    print("preview:", os.path.normpath(out))
