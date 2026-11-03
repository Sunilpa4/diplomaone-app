"""GTU Mathematics-I (DI01000021) - a COMMON subject for every diploma branch, Semester 1, w.e.f. 2024-25.

Syllabus source: tools/syllabus_DI01000021.txt (transcribed from the uploaded PDF, sha256 in subject.json).
The official five units are reproduced exactly. Unit 0 is our own foundation chapter ("Start Mathematics
From Zero"): it carries no syllabus hours or weightage and is marked official=false so nobody mistakes it
for part of the GTU syllabus.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / "content/common/sem1/DI01000021"
DIAG_DIR = SUBJ_DIR / "diagrams"
TABS = ["notes", "diagrams", "equations", "numericals", "viva", "exam"]
FOUNDATION_TABS = ["notes", "diagrams", "equations", "numericals", "viva", "exam"]


def tr(s):
    return {"en": s}


# (no, title, hours, weightage, official, topics)
UNITS = [
    (0, "Start Mathematics From Zero (Foundation)", 0, 0, False, [
        "Numbers, signs, fractions, LCM and GCD",
        "Order of operations, powers, roots and standard form",
        "Algebra: expressions, expansion and factorisation",
        "Linear equations and simultaneous equations",
        "Quadratic equations",
        "Sets, ratio, percentage and average",
        "The coordinate plane",
        "How to study mathematics: the five-step method",
    ]),
    (1, "Determinant and Function", 9, 23, True, [
        "Determinant and its value up to third order (without properties)",
        "Function and simple examples",
        "Logarithm as a function",
        "Laws of logarithm and related simple examples",
    ]),
    (2, "Trigonometry", 12, 20, True, [
        "Units of angles (degree and radian)",
        "Trigonometric functions",
        "Allied and compound angles; multiple and submultiple angles",
        "Graph of sine and cosine",
        "Periodic trigonometric function",
        "Sum and factor formulae",
        "Inverse trigonometric function",
    ]),
    (3, "Vectors", 9, 20, True, [
        "Vector, addition, subtraction, magnitude and direction",
        "Scalar and vector product and their properties",
        "Angle between two vectors",
        "Applications of scalar and vector product: work done and moment of force",
    ]),
    (4, "Coordinate Geometry", 8, 20, True, [
        "Straight line (two-point form) and slope of a straight line",
        "Slope-point form, intercept form, general form of a line",
        "Condition of parallel and perpendicular lines",
        "Equations of parallel and perpendicular lines to a given line",
        "Angle between two lines",
        "Equation of a circle with centre and radius",
        "General equation of a circle",
        "Tangent and normal to a circle",
    ]),
    (5, "Limit", 7, 17, True, [
        "Limit of a function",
        "Standard formulae of limit and related simple examples",
    ]),
]

SUBJECT = {
    "code": "DI01000021",
    "name": tr("Mathematics - I"),
    "branch": "common",
    "common_to_all_branches": True,
    "semester": 1,
    "syllabus_year": "2024-25",
    "category": "Basic Science (BSC)",
    "type": "theory",
    "languages": ["en"],
    "code_lang": None,
    "teaching": {"lecture": 3, "tutorial": 1, "practical": 0},
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 0, "practical_ese": 0,
             "total": 100, "credits": 4},
    "prerequisites": [
        "Linear equation in two variables",
        "Factorization",
        "Polynomial",
        "Quadratic equation",
        "Coordinate geometry",
        "LCM and GCD",
        "Concept of set",
    ],
    "units": [
        {"no": n, "title": tr(t), "hours": h, "weightage": w, "official": official,
         "topics": topics, "file": None}
        for n, t, h, w, official, topics in UNITS
    ],
    "course_outcomes": [
        "CO1: Interpret the function graphically, numerically and analytically.",
        "CO2: Demonstrate the ability to algebraically analyse basic functions used in trigonometry.",
        "CO3: Demonstrate the ability to crack engineering related problems based on concepts of vectors.",
        "CO4: Solve basic engineering problems under given conditions of straight lines and circle.",
        "CO5: Demonstrate the ability to analyse and illustrate the functions using the concept of limit.",
    ],
    "course_outcome_rbt": {"CO1": "Application", "CO2": "Application", "CO3": "Application",
                           "CO4": "Application", "CO5": "Application"},
    # Official specification table: marks per unit out of the 70-mark theory paper.
    "theory_marks_by_unit": {"1": 16, "2": 14, "3": 14, "4": 14, "5": 12},
    "theory_rbt_percent": {"remember": 27, "understand": 39, "apply": 34,
                           "analyze": 0, "evaluate": 0, "create": 0},
    "source_pdf_sha256": "05037c52c0d916f9292ea7c297f55f1b995db68f2c976ccc354ed93e7864bb92",
    "source_note": "Syllabus text transcribed from the uploaded GTU DI01000021 PDF (Branch: All). Unit hours, "
                   "weightages, marks split and course outcomes are copied from it. Unit 0 is a DiplomaOne "
                   "foundation chapter, not part of the official syllabus.",
    "foundation_unit": {
        "no": 0,
        "title": "Start Mathematics From Zero (Foundation)",
        "why": "The official prerequisite list assumes fractions, factorisation, quadratic equations, coordinate "
               "geometry, LCM/GCD and sets. Many first-semester students arrive without them, so this chapter "
               "rebuilds those tools with solved numericals before Unit 1 begins.",
        "official": False,
    },
    "practicals": [],
    "books": [
        "Anthony Croft - Engineering Mathematics, 3rd edition (Pearson, 2014), ISBN 978-81-317-2605-1",
        "Narayan Shanti and Mittal P.K - A Text Book of Vector Analysis (S. Chand), ISBN 978-8121922432",
        "G. B. Thomas, R. L. Finney - Calculus and Analytic Geometry, 9th edition (Addison Wesley, 1995), "
        "ISBN 978-8174906168",
        "John Bird - Understanding Engineering Mathematics (Routledge, 1st edition), ISBN 978-0415662840",
        "Erwin Kreyszig - Advanced Engineering Mathematics (Wiley, 2014), ISBN 978-0-470-45836-5",
        "Deepak Singh - Mathematics-I (Khanna Book Publishing), ISBN 978-93-91505-42-4",
        "Garima Singh - Mathematics-II (Khanna Book Publishing), ISBN 978-93-91505-52-3",
    ],
    "learning_resources": [
        "DTEGUJ YouTube channel (official GTU diploma lectures)",
        "GeoGebra - https://www.geogebra.org/",
        "PhET simulations - https://phet.colorado.edu/",
        "Khan Academy - https://www.khanacademy.org/",
        "Wolfram Mathematica - https://www.wolfram.com/mathematica/",
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
        assert not re.search(r"[\u0a80-\u0aff]", obj), f"Gujarati text in English-only unit: {obj[:60]!r}"


def spec_for(number):
    for spec in SUBJECT["units"]:
        if spec["no"] == number:
            return spec
    raise AssertionError(f"unit {number} is not registered for DI01000021")


def write_unit(unit):
    SUBJ_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(exist_ok=True)
    spec = spec_for(unit["unit"])
    assert unit["title"] == spec["title"], "unit title must match subject.json"
    if spec["official"]:
        assert (unit["hours"], unit["weightage"]) == (spec["hours"], spec["weightage"]), \
            "official unit hours/weightage must match the syllabus"
    else:
        assert (unit["hours"], unit["weightage"]) == (0, 0), "a foundation unit carries no syllabus hours"
    _check_english_only(unit)
    out = SUBJ_DIR / f"unit{unit['unit']}.json"
    out.write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    write_subject()
    return out


if __name__ == "__main__":
    write_subject()
    print("subject written:", SUBJ_DIR / "subject.json")
