"""GTU Engineering Graphics (DI01000111) - Semester 1, w.e.f. 2024-25.

The PDF lists fifteen branches (Power Electronics through Textile Processing Technology), all of them
taught by this single drawing course, so subject.json records the list in "branches" and the exporter
lists the subject in semester 1 of each of those branches that the app carries.

Content policy for this subject (user decision): **English only** - no Gujarati nodes at all - and
every drawing topic is taught as a numbered construction, "step 1, step 2, ... check", so a student
learns how the drawing is built rather than only what it looks like.

Syllabus source: tools/syllabus_DI01000111.txt (transcribed from the uploaded PDF, sha256 kept in
subject.json). Units, hours, weightages, the marks split, the course outcomes, the books, the
practical list, the project and the activities are copied from it exactly.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / "content/common/sem1/DI01000111"
DIAG_DIR = SUBJ_DIR / "diagrams"
TABS = ["notes", "diagrams", "equations", "viva", "exam"]

CODE = "DI01000111"
TITLE = "Engineering Graphics"


def tr(s):
    return {"en": s}


# (no, title, hours, weightage, theory_marks, course_outcome, topics, outcome)
UNITS = [
    (1, "Introduction to Engineering Graphics", 4, 10, 7, "CO1", [
        "Introduction to drawing instruments and accessories",
        "Types of lines as per BIS-SP 46",
        "Dimensioning as per BIS-SP 46",
        "Plane scale: representative fraction and construction",
        "Draw polygons with various methods (any one method may be used in the exam)",
    ],
     "Apply the conventions and methods of engineering drawing: instruments, line types, "
     "dimensioning, scales and regular polygons."),
    (2, "Engineering Curves", 5, 20, 14, "CO2", [
        "Applications of engineering curves",
        "Construction of conical curves: ellipse, parabola and hyperbola",
        "Drawing of cycloidal curves",
        "Involutes",
        "Spirals",
        "Construction of tangents and normals to the curves",
    ],
     "Construct engineering curves - conics, cycloids, involutes and spirals - as per the given "
     "dimensions."),
    (3, "Projections of Points and Lines", 5, 20, 14, "CO3", [
        "Introduction to the principal planes of projection",
        "Projections of points in all four quadrants",
        "Projections of a line parallel to one or both reference planes",
        "Projections of a line inclined to HP and VP",
        "True length, true inclination and the apparent angles",
        "Traces of a line",
    ],
     "Draw the projections of points, lines and planes under different conditions and find true "
     "length and true inclination."),
    (4, "Projections of Planes", 4, 10, 7, "CO3", [
        "Projection of a plane surface in its simplest position",
        "Inclination of a square plane with the reference planes",
        "Inclination of a hexagonal plane with the reference planes",
        "Inclination of a circular plane with the reference planes",
        "Edge view and the change of position method",
    ],
     "Project a square, hexagonal or circular plane inclined to the reference planes and read its "
     "true shape."),
    (5, "Orthographic Projections", 6, 20, 14, "CO4", [
        "Projections from the pictorial view of an object",
        "Draw front, top and side views of simple objects",
        "First angle and third angle methods of arrangement",
        "Missing line problems",
        "Free hand sketches of square, triangle, circle, semi-circle, hexagon and pentagon",
    ],
     "Read a pictorial (isometric) view and produce the front, top and side views of a simple "
     "object by first-angle projection."),
    (6, "Isometric View", 6, 20, 14, "CO5", [
        "Isometric axes, isometric lines and non-isometric lines",
        "Isometric view of simple objects",
        "Isometric scale and the 0.816 factor",
        "Free hand sketches of a prism, a pyramid, a cylinder and a cone",
        "Box method and offset method of construction",
    ],
     "Draw the isometric view of a simple object from its orthographic views, using the isometric "
     "scale."),
]

BRANCH_KEYS = ["power", "robotics", "civil", "environmental", "mining", "chemical", "metallurgy",
               "plastic", "mechanical", "automobile", "mechatronics", "textile_proc"]

SUBJECT = {
    "code": CODE,
    "name": tr(TITLE),
    "branch": "common",
    "branches": BRANCH_KEYS,
    # The branches above teach it in semester 1 only; naming the semesters lets the publisher check
    # the registration against BRANCH_SEMS instead of demanding all 27 branches.
    "semesters": [1],
    "common_to_all_branches": False,
    "semester": 1,
    "syllabus_year": "2024-25",
    "category": "Engineering Science (ESC-01)",
    "type": "theory",
    "languages": ["en"],
    "code_lang": None,
    "teaching": {"lecture": 2, "tutorial": 0, "practical": 2},
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30,
             "total": 150, "credits": 3},
    "prerequisites": tr("Zeal to learn the subject, as printed in the syllabus; school geometry "
                        "(angles, triangles, circles and regular polygons) and a working hand with "
                        "a pencil and a drawing instrument box"),
    "units": [
        {"no": no, "title": tr(t), "hours": hours, "weightage": weightage,
         "theory_marks": marks, "official": True, "course_outcome": co,
         "topics": [tr(x) for x in topics], "outcomes": [tr(outcome)]}
        for (no, t, hours, weightage, marks, co, topics, outcome) in UNITS
    ],
    "course_outcomes": [
        tr("CO1: Apply the conventions and methods of engineering drawing. (Application)"),
        tr("CO2: Construct engineering curves as per given dimensions. (Remember)"),
        tr("CO3: Draw the projection of points, lines and planes under different conditions. "
           "(Analyze)"),
        tr("CO4: Draw orthographic projection from isometric views of simple objects. "
           "(Application)"),
        tr("CO5: Draw isometric views from orthographic projection of simple objects. "
           "(Application)"),
    ],
    "course_outcome_rbt": {"CO1": "Apply", "CO2": "Remember", "CO3": "Analyze", "CO4": "Apply",
                           "CO5": "Apply"},
    "theory_marks_by_unit": {"1": 7, "2": 14, "3": 14, "4": 7, "5": 14, "6": 14},
    "theory_marks_note": tr(
        "The PDF prints only the weightage column, so the 70 theory marks are split by weightage: "
        "7 / 14 / 14 / 7 / 14 / 14 = 70. The practical half (PA 20 + ESE 30) is assessed on the "
        "seven drawing practicals and the A2 sheets."),
    "theory_rbt_percent": {"remember": 10, "understand": 20, "apply": 40, "analyze": 30,
                           "evaluate": 0, "create": 0},
    "theory_rbt_marks": {"remember": 7, "understand": 14, "apply": 28, "analyze": 21,
                         "evaluate": 0, "create": 0},
    "total_hours": 30,
    "source_pdf_sha256": "c88b56fd4567b334c37c0b9314a04d7bfe79e9331c97444dd1136025a25c170a",
    "source_note": tr(
        "Syllabus text transcribed from the uploaded GTU DI01000111 PDF (Engineering Graphics, "
        "semester 1, w.e.f. 2024-25). Unit hours, weightages, the marks split, the course outcomes, "
        "the reference books, the practical list, the laboratory resources, the project and the "
        "activities are copied from it. The PDF names fifteen branches; the app carries twelve of "
        "them and the subject is listed in semester 1 of those twelve."),
    "official_practicals": [
        tr("Use of drawing instruments (types of lines, dimensioning, scale as per BIS, angles, "
           "polygons)"),
        tr("Drawing of conical curves (ellipse, parabola, hyperbola)"),
        tr("Drawing of spiral, involute and cycloidal curves"),
        tr("Projections of points and line"),
        tr("Projections of plane"),
        tr("Draw orthographic projections of the given isometric view"),
        tr("Draw isometric view of the given orthographic projection"),
    ],
    "practicals": [],
    "suggested_projects": [
        tr("Prepare a chart that shows real applications of the topics of this subject: a road "
           "curve for a parabola, a gear tooth for an involute, a thread for a helix, a machine "
           "part for orthographic views."),
    ],
    "activities": [
        tr("Draw a free hand sketch of any object around you, then draw both its isometric view and "
           "its orthographic views."),
        tr("All the problems must be drawn in the sketch book first and then on an A2 drawing "
           "sheet; both sides may be used if needed."),
    ],
    "books": [
        "P. S. Gill - A Text Book of Engineering Drawing, S. K. Kataria & Sons, Delhi",
        "N. D. Bhatt - Elementary Engineering Drawing, Charotar Publishing House, Anand",
    ],
    "learning_resources": [
        "Mechanical Engineering Subjects GTU - https://www.youtube.com/c/MechanicalEnggSubjectsGTU/playlists",
        "Engineering Drawing playlist - https://youtube.com/playlist?list=PL5Rqb_WO7qVy2-6FluBrQcJhrXvyOxe",
        "Drawing paper, scale, 0.5 mm H and 2H lead pencil, protractor and set squares",
    ],
}


def write_subject():
    SUBJ_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(exist_ok=True)
    for spec in SUBJECT["units"]:
        name = f"unit{spec['no']}.json"
        spec["file"] = name if (SUBJ_DIR / name).is_file() else None
    (SUBJ_DIR / "subject.json").write_text(
        json.dumps(SUBJECT, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def _check_english_only(obj):
    if isinstance(obj, dict):
        assert "gu" not in obj, "English-only build must not carry 'gu' keys"
        for v in obj.values():
            _check_english_only(v)
    elif isinstance(obj, list):
        for v in obj:
            _check_english_only(v)
    elif isinstance(obj, str):
        assert not re.search(r"[\u0a80-\u0aff]", obj), \
            f"Gujarati text in an English-only unit: {obj[:60]!r}"


def spec_for(number):
    for spec in SUBJECT["units"]:
        if spec["no"] == number:
            return spec
    raise AssertionError(f"unit {number} is not registered for {CODE}")


def write_unit(unit):
    SUBJ_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(exist_ok=True)
    spec = spec_for(unit["unit"])
    assert unit["title"] == spec["title"], "unit title must match subject.json"
    assert (unit["hours"], unit["weightage"]) == (spec["hours"], spec["weightage"]), \
        "unit hours/weightage must match the syllabus"
    _check_english_only(unit)
    out = SUBJ_DIR / f"unit{unit['unit']}.json"
    out.write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    write_subject()
    return out


if __name__ == "__main__":
    write_subject()
    print("subject written:", SUBJ_DIR / "subject.json")
