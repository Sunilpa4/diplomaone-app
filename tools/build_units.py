# -*- coding: utf-8 -*-
"""Build DI04000081 units 2-5 (whichever content/diagram modules exist) + refresh subject.json."""
import copy, importlib, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from build_DI04000081_u1 import SUBJECT as BASE_SUBJECT, SOURCES

def tr(en, gu): return {"en": en, "gu": gu}
CODE = "DI04000081"
SUBJ_DIR = ROOT / "content/common/sem4/DI04000081"

def main():
    built = [1]
    for n in (2, 3, 4, 5):
        try:
            cm = importlib.import_module(f"content_DI04000081_u{n}")
            dm = importlib.import_module(f"diagrams_u{n}")
        except ModuleNotFoundError:
            continue
        info = BASE_SUBJECT["units"][n - 1]
        diagrams = dm.DIAGRAMS
        (SUBJ_DIR / "diagrams").mkdir(parents=True, exist_ok=True)
        for (did, _t, svg) in diagrams:
            (SUBJ_DIR / "diagrams" / f"{did}.svg").write_text(svg, encoding="utf-8")
        unit = {
         "subject": CODE, "unit": n, "format": "notes",
         "title": info["title"], "hours": info["hours"], "weightage": info["weightage"], "languages": ["en", "gu"],
         "tabs": ["notes", "diagrams", "exam"], "tab_labels": {},
         "intro_text": {"en": cm.INTRO_EN, "gu": cm.INTRO_GU},
         "notes": cm.NOTES,
         "diagrams": [{"id": i, "title": tr(t, t), "file": f"diagrams/{i}.svg"} for (i, t, _s) in diagrams],
         "numericals": [], "syntax": [], "viva": [],
         "exam_questions": [{"q": tr(en, gu), "marks": m} for (en, gu, m) in cm.EXAM_PRACTICE],
         "practicals": [], "practical_numbers": [],
         "learning_outcomes": [BASE_SUBJECT["course_outcomes"][i] for i in cm.CO_INDEX],
         "content_kind": "theory_with_guided_activities",
         "assessment_note": tr(f"Official scheme (GTU DI04000081): Theory ESE 70 + PA 30, total 100 marks, 3 credits, no practical examination. Unit {n} carries {info['hours']} hours and {info['weightage']} % weightage in the official syllabus. All exam questions in this unit are original practice questions; their marks are suggested, not from an official paper.",
                               f"સત્તાવાર scheme (GTU DI04000081): Theory ESE 70 + PA 30, કુલ 100 marks, 3 credits, કોઈ practical examination નથી. Unit {n} ને સત્તાવાર syllabus માં {info['hours']} hours તથા {info['weightage']} % weightage છે. આ unit ના બધા exam questions original practice questions છે; તેમના marks suggested છે, સત્તાવાર paper માંથી નથી."),
         "question_provenance": "Original revision questions; not official past papers",
         "question_marks_are_suggested": True,
         "lesson_count": sum(len(s["items"]) for s in cm.NOTES),
         "answered_practice_count": 0,
         "sources": SOURCES,
        }
        (SUBJ_DIR / f"unit{n}.json").write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        built.append(n)
        print(f"unit{n}: cards={unit['lesson_count']} diagrams={len(diagrams)} exam={len(unit['exam_questions'])} ({(SUBJ_DIR / f'unit{n}.json').stat().st_size/1024:.1f} KB)")
    subject = copy.deepcopy(BASE_SUBJECT)
    subject["available_units"] = built
    for u in subject["units"]:
        u["file"] = f"unit{u['no']}.json" if u["no"] in built else None
    (SUBJ_DIR / "subject.json").write_text(json.dumps(subject, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("subject.json available_units:", built)

if __name__ == "__main__":
    main()
