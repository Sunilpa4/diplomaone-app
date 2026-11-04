# -*- coding: utf-8 -*-
"""Generic builder: python3 build_unit_generic.py <unit_no> <module_name>"""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
SUBJ_DIR = ROOT / "content/chemical/sem4/DI04005071"
CODE = "DI04005071"

def build(unit_no, mod_name):
    m = __import__(mod_name)
    subj = json.loads((SUBJ_DIR / "subject.json").read_text(encoding="utf-8"))
    spec = next(u for u in subj["units"] if u["no"] == unit_no)
    notes = m.NOTES + [m.ANSWERED]
    unit = {
        "subject": CODE, "unit": unit_no, "format": "notes",
        "title": spec["title"], "hours": spec["hours"], "weightage": spec["weightage"],
        "languages": ["en", "gu"],
        "tabs": ["notes", "diagrams", "numericals", "syntax", "viva", "exam"],
        "tab_labels": {"numericals": {"en": "Solved numericals", "gu": "ઉકેલેલા દાખલા"},
                       "syntax": {"en": "Formulae and conversions", "gu": "સૂત્રો તથા conversions"}},
        "intro_text": {"en": m.INTRO_EN, "gu": m.INTRO_GU},
        "notes": notes,
        "diagrams": [{"id": d[0], "title": {"en": d[1], "gu": d[1]}, "file": f"diagrams/{d[0]}.svg"} for d in m.DIAGRAMS],
        "numericals": m.NUMERICALS, "syntax": m.SYNTAX, "viva": m.VIVA,
        "exam_questions": m.EXAM,
        "practicals": getattr(m, "PRACTICALS", []),
        "learning_outcomes": [subj["course_outcomes"][i] for i in m.CO_INDEX],
        "practical_numbers": getattr(m, "PRACTICAL_NUMBERS", []),
        "content_kind": "theory_with_guided_practical_support",
        "assessment_note": {"en": f"Official scheme (GTU DI04005071): Theory ESE 70 + PA 30, Practical PA 20 + ESE 30, total 150 marks, 4 credits. Unit {unit_no} carries {spec['hours']} hours and {spec['weightage']} % weightage in the official syllabus. All exam questions in this unit are original practice questions; their marks are suggested, not from an official paper.",
                            "gu": f"સત્તાવાર scheme (GTU DI04005071): Theory ESE 70 + PA 30, Practical PA 20 + ESE 30, કુલ 150 marks, 4 credits. Unit {unit_no} ને સત્તાવાર syllabus માં {spec['hours']} hours તથા {spec['weightage']} % weightage છે. આ unit ના બધા exam questions original practice questions છે; તેમના marks suggested છે, સત્તાવાર paper માંથી નથી."},
        "question_provenance": "Original answered revision questions; not official past papers",
        "question_marks_are_suggested": True,
        "lesson_count": sum(len(s["items"]) for s in m.NOTES),
        "answered_practice_count": len(m.ANSWERED["items"]),
        "sources": m.SOURCES,
    }
    (SUBJ_DIR / "diagrams").mkdir(parents=True, exist_ok=True)
    try:
        from diagrams_real import REAL
    except Exception:
        REAL = {}
    for (did, _title, svg_text) in m.DIAGRAMS:
        (SUBJ_DIR / "diagrams" / f"{did}.svg").write_text(REAL.get(did, svg_text), encoding="utf-8")
    out = SUBJ_DIR / f"unit{unit_no}.json"
    out.write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Unit {unit_no}: {out.name} {out.stat().st_size/1024:.1f} KB | cards={unit['lesson_count']} diagrams={len(m.DIAGRAMS)} numericals={len(m.NUMERICALS)} viva={sum(len(g['items']) for g in m.VIVA)} exam={len(m.EXAM)}")

if __name__ == "__main__":
    build(int(sys.argv[1]), sys.argv[2])
