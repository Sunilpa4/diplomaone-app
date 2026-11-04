"""Build Chemical Reaction Engineering (DI05005031) Unit 5 - bilingual, with seven figures."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI05005031 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI05005031_u5_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI05005031_u5 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()
    spec = spec_for(5)
    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("5.6 Solved Numericals, Step by Step",
                              "5.6 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI05005031",
        "unit": 5,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "theory_marks": spec["theory_marks"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 5 is where the reactor is sized. One mole balance is written three ways - a batch "
            "time, a CSTR volume and a PFR integral - and the rest of the unit turns those three "
            "lines into vessels. Constant density makes the rate a function of conversion alone, so "
            "every equation can be integrated by hand. The batch, mixed flow and plug flow designs "
            "are then worked out, the CSTR rectangle and the PFR area are read off the same graph, "
            "and the unit closes on space time, space velocity and holding time, the three numbers "
            "that a plant actually quotes. Six solved numericals follow in section 5.6.",
            "Unit 5 માં reactor નું માપ નક્કી થાય છે. એક mole balance ત્રણ રીતે લખાય - batch નો સમય, "
            "CSTR નું volume અને PFR નું integral - અને બાકીનું આખું unit એ ત્રણ લીટીને પાત્રોમાં "
            "ફેરવે. Constant density rate ને ફક્ત conversion નું વિધેય બનાવે, તેથી દરેક equation હાથે "
            "integrate થાય. પછી batch, mixed flow અને plug flow ની design ગણાય, CSTR નો લંબચોરસ અને "
            "PFR નું ક્ષેત્રફળ એક જ ગ્રાફ પરથી વંચાય, અને unit space time, space velocity તથા "
            "holding time પર પૂરું થાય - જે ત્રણ આંકડા plant ખરેખર લખે છે. વિભાગ 5.6 માં છ ઉકેલેલા "
            "દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO5"],
        "practical_numbers": [12, 13, 14, 15],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits, 45 teaching hours. This unit carries 24 % weightage, 11 of the printed unit "
            "hours and 17 of the 70 theory marks, and it is the unit the practicals 12 to 15 are "
            "written against - volume, space time and space velocity for one ideal reactor. The "
            "numericals of section 5.6 are original revision problems with suggested marks, not GTU "
            "papers.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits, 45 teaching hours. આ unit નું weightage 24 %, છપાયેલા unit hours માંથી 11 અને "
            "70 theory marks માંથી 17 છે, અને practicals 12 થી 15 આ unit પર લખાયેલા છે - એક ideal "
            "reactor માટે volume, space time અને space velocity. વિભાગ 5.6 ના દાખલા revision માટેના "
            "મૂળ પ્રશ્નો છે, GTU પેપર નહીં."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI05005031_unit5_preview.html"))
    from notes_workshop import render_one
    render_one("DI05005031", 5, note="Unit 5 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Chemical Reaction Engineering Unit 5 {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


# Gujarati titles and captions for the six figures (short enough for a card header).
CAPTIONS_GU = {
    "u5_perf": "એક balance, ત્રણ design equations",
    "u5_batch": "Batch reactor ની design",
    "u5_cstr": "CSTR ની design: એક લંબચોરસ",
    "u5_pfr": "PFR ની design: ક્ષેત્રફળ",
    "u5_series": "Series માં બે CSTR",
    "u5_space": "Space time સામે holding time",
    "u5_bars": "એ જ કામ માટેના volumes",
}

CAPTIONS_GU_TAIL = {
    "u5_perf": "એ જ mole balance ત્રણ રીતે: batch માટે સમય, CSTR માટે બીજગણિતીય volume, PFR માટે "
               "નળી પર integral.",
    "u5_batch": "Batch reactor સમયમાં design થાય: concentration વક્રનો ઢોળાવ તે ક્ષણનો rate છે, "
                "તેથી ઢોળાવ જેટલો તીવ્ર તેટલું conversion ઝડપથી મળે.",
    "u5_cstr": "1/(-rA) સામે X ના ગ્રાફ પર CSTR એક લંબચોરસ છે: પહોળાઈ X, ઊંચાઈ exit નો rate, "
               "ક્ષેત્રફળ V/FA0. 80 % conversion પર એ ક્ષેત્રફળ k tau = 4 થાય.",
    "u5_pfr": "PFR એ એ જ વક્ર નીચેનું ક્ષેત્રફળ છે. 80 % conversion પર તે ln 5 = 1.61 થાય, તેથી એ જ "
              "કામ માટે નળીને ટાંકી કરતાં 2.5 ગણું ઓછું volume જોઈએ.",
    "u5_series": "Series માં બે સરખા CSTR એ દરેક k tau = 1.236 વાળા બે લંબચોરસ છે, અને સાથે મળીને "
                 "80 % સુધી પહોંચે - Unit 4 ના આંકડા પાછળની ભૂમિતિ.",
    "u5_space": "Space time feed ના volume flow થી નક્કી થાય; holding time એ છે જે પ્રવાહી ખરેખર "
                "અંદર ગાળે, અને gas માટે તે temperature તથા pressure સાથે બદલાય.",
    "u5_bars": "એ જ કામ (first order પ્રક્રિયાના 80 %, k = 0.25 h-1, v0 = 7.2 m3/h): એક CSTR "
               "115 m3, બે CSTR 71 m3, એક PFR 46 m3.",
}

if __name__ == "__main__":
    main()
