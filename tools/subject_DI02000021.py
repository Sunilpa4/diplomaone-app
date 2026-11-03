"""GTU Engineering Mathematics (DI02000021) - Semester 2, w.e.f. 2024-25.

Official branches: Electrical Engineering, Renewable Energy, Automation and Robotics,
Instrumentation & Control Engineering, Power Electronics Engineering.

Syllabus source: tools/syllabus_DI02000021.txt (transcribed from the uploaded PDF,
sha256 kept in subject.json). The five units, their hours, weightages, marks split
and course outcomes are copied from the PDF exactly.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / "content/common/sem2/DI02000021"
DIAG_DIR = SUBJ_DIR / "diagrams"
TABS = ["notes", "diagrams", "equations", "numericals", "viva", "exam"]

CODE = "DI02000021"
TITLE = "Engineering Mathematics"


def tr(s):
    return {"en": s}


# (no, title, hours, weightage, official, topics, course_outcome)
UNITS = [
    (1, "Matrices", 10, 23, True, [
        "Concept of matrix",
        "Types of matrices",
        "Addition, subtraction and multiplication by a scalar of matrices",
        "Product of two matrices",
        "Adjoint and inverse of a matrix of order 2×2 and 3×3",
        "Solution of simultaneous linear equations of two variables",
    ], "CO1"),
    (2, "Differentiation and its Applications", 11, 23, True, [
        "Concept and definition of differentiation",
        "Working rules: sum, product, division",
        "Chain rule",
        "Derivative of implicit functions",
        "Derivative of parametric functions",
        "Logarithmic differentiation",
        "Successive differentiation up to second order",
        "Applications: velocity, acceleration, maxima and minima of given simple functions",
    ], "CO2"),
    (3, "Integration and its Applications", 10, 20, True, [
        "Concept and definition of integration",
        "Working rules and integral of standard functions",
        "Method of substitution",
        "Integration by parts",
        "Definite integral and its properties",
        "Applications: area and volume (simple problems)",
    ], "CO3"),
    (4, "Differential Equations", 7, 17, True, [
        "Concept and definition, order and degree of differential equation",
        "Solution of DE of first degree and first order by variable separable method",
        "Solution of linear differential equation",
    ], "CO4"),
    (5, "Complex Numbers", 7, 17, True, [
        "Concept of complex number",
        "Algebra of complex numbers",
        "Conjugate, modulus and inverse of complex numbers",
        "Argument and polar form of a complex number",
        "De Moivre's theorem and related simple examples",
        "Square root of a complex number and cube root of unity",
    ], "CO5"),
]

SUBJECT = {
    "code": CODE,
    "name": tr(TITLE),
    "branch": "common",
    "branches": ["electrical", "renewable", "robotics", "ic", "power"],
    "common_to_all_branches": False,
    "semester": 2,
    "syllabus_year": "2024-25",
    "category": "Basic Science (BSC)",
    "type": "theory",
    "languages": ["en"],
    "code_lang": None,
    "teaching": {"lecture": 3, "tutorial": 1, "practical": 0},
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 0, "practical_ese": 0,
             "total": 100, "credits": 4},
    "prerequisites": [
        "Function",
        "Logarithm",
        "Determinant",
        "Trigonometry",
        "Limit",
        "Factorization",
        "Polynomial",
        "Quadratic equation",
        "Coordinate geometry",
        "LCM and GCD",
        "Concept of set",
    ],
    "units": [
        {"no": n, "title": tr(t), "hours": h, "weightage": w, "official": official,
         "topics": topics, "course_outcome": co, "file": None}
        for n, t, h, w, official, topics, co in UNITS
    ],
    "course_outcomes": [
        "CO1: Demonstrate the ability to crack engineering related problems based on matrices.",
        "CO2: Demonstrate the ability to solve engineering related problems based on applications "
        "of differentiation.",
        "CO3: Demonstrate the ability to solve engineering related problems based on applications "
        "of integration.",
        "CO4: Develop the ability to apply differential equations to significant applied problems.",
        "CO5: Represent complex numbers algebraically and geometrically for solving engineering "
        "related problems.",
    ],
    "course_outcome_rbt": {"CO1": "Application", "CO2": "Application", "CO3": "Application",
                           "CO4": "Application", "CO5": "Application"},
    # Official specification table: marks per unit out of the 70-mark theory paper.
    "theory_marks_by_unit": {"1": 16, "2": 16, "3": 14, "4": 12, "5": 12},
    "theory_rbt_percent": {"remember": 23, "understand": 34, "apply": 43,
                           "analyze": 0, "evaluate": 0, "create": 0},
    "theory_rbt_marks": {"remember": 16, "understand": 24, "apply": 30,
                         "analyze": 0, "evaluate": 0, "create": 0},
    "total_hours": 45,
    "source_pdf_sha256": "59bcab9b6dbf69b5585c51e859029ea892151b26ab9c702ad23ac54be04abc17",
    "source_note": "Syllabus text transcribed from the uploaded GTU DI02000021 PDF "
                   "(Engineering Mathematics, Semester 2, BSC). Unit hours, weightages, the marks "
                   "split and the course outcomes are copied from it.",
    "practicals": [],
    "books": [
        "B. S. Grewal - Elementary Engineering Mathematics (Khanna Publishers, 15th edition), "
        "ISBN 978-81-7409-257-1",
        "Anthony Croft - Engineering Mathematics, 3rd edition (Pearson, 2014), ISBN 978-81-317-2605-1",
        "Bittinger, Ellenbogen, Surgent - Calculus and Its Applications, 10th edition "
        "(Addison-Wesley), ISBN 978-0-321-69433-1",
        "G. B. Thomas, R. L. Finney - Calculus and Analytic Geometry, 9th edition (1995), "
        "ISBN 978-8174906168",
        "John Bird - Understanding Engineering Mathematics (Routledge, 1st edition), "
        "ISBN 978-0415662840",
        "Erwin Kreyszig - Advanced Engineering Mathematics (Wiley, 2014), ISBN 978-0-470-45836-5",
        "Deepak Singh - Mathematics-I (Khanna Book Publishing), ISBN 978-93-91505-42-4",
        "Garima Singh - Mathematics-II (Khanna Book Publishing), ISBN 978-93-91505-52-3",
    ],
    "learning_resources": [
        "DTEGUJ YouTube channel (official GTU diploma lectures)",
        "GeoGebra - https://www.geogebra.org/",
        "PhET simulations - https://phet.colorado.edu/",
        "Khan Academy - https://www.khanacademy.org/",
        "SciLab - https://www.scilab.org/",
        "DPlot - https://www.dplot.com/",
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
