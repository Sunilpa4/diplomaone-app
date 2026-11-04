"""Build Chemical Reaction Engineering (DI05005031) Unit 4 - bilingual, with nine figures."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI05005031 import TABS, SUBJECT, DIAG_DIR, tr, write_unit, spec_for  # noqa: E402
from content_DI05005031_u4_notes import (NOTES, EQUATIONS, VIVA, PRACTICE,  # noqa: E402
                                         SOURCES, LESSON_COUNT)
from diagrams_DI05005031_u4 import TITLES, CAPTIONS, DIAGRAMS  # noqa: E402
from preview_builder import build_preview  # noqa: E402


def draw():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (DIAG_DIR / f"{key}.svg").write_text(fn(), encoding="utf-8")


def main():
    draw()
    spec = spec_for(4)
    def with_question(h, q, a, m):
        """A solved numerical opens with its own statement, so the page can be read without the paper."""
        head = {"en": f"<h4>Question ({m} marks)</h4><p>{q['en']}</p>",
                "gu": f"<h4>પ્રશ્ન ({m} marks)</h4><p>{q['gu']}</p>"}
        return {"h": h, "body": {"en": head["en"] + a["en"], "gu": head["gu"] + a["gu"]}}

    items = [with_question(h, q, a, m) for h, q, a, m in PRACTICE]
    NOTES.append({"title": tr("4.4 Solved Numericals, Step by Step",
                              "4.4 ઉકેલેલા દાખલા, પગલે પગલે"), "items": items})
    exam = [{"q": q, "marks": m} for _h, q, _a, m in PRACTICE]

    unit = {
        "subject": "DI05005031",
        "unit": 4,
        "format": "notes",
        "title": spec["title"],
        "hours": spec["hours"],
        "weightage": spec["weightage"],
        "theory_marks": spec["theory_marks"],
        "official": True,
        "languages": ["en", "gu"],
        "tabs": TABS[:],
        "intro_text": tr(
            "Unit 4 of Chemical Reaction Engineering: the reactors themselves, built and worked part "
            "by part. The three ideal mixing models come first, then the batch and semi-batch "
            "vessels, the CSTR and the plug flow tube, the fixed bed and the fluidised bed, and "
            "finally the multiphase family - slurry, bubble column, spray tower and trickle bed. "
            "Each reactor is shown with its construction, its working steps, its design equation "
            "and its own strengths and limits. Six solved numericals follow in section 4.4.",
            "Chemical Reaction Engineering નું Unit 4: reactors પોતે, ભાગે ભાગે બનાવેલા અને "
            "સમજાવેલા. પહેલા ત્રણ આદર્શ mixing models, પછી batch અને semi-batch પાત્રો, CSTR અને "
            "plug flow નળી, fixed bed અને fluidised bed, અને અંતે multiphase કુટુંબ - slurry, "
            "bubble column, spray tower અને trickle bed. દરેક reactor તેની રચના, કાર્યપદ્ધતિના પગલાં, "
            "design equation અને પોતાની તાકાત તથા મર્યાદા સાથે દર્શાવેલો છે. વિભાગ 4.4 માં છ ઉકેલેલા "
            "દાખલા છે."),
        "notes": NOTES,
        "diagrams": [{"id": i, "title": tr(TITLES[i], CAPTIONS_GU[i]), "file": f"diagrams/{i}.svg",
                      "caption": tr(CAPTIONS[i], CAPTIONS_GU_TAIL[i])} for i in TITLES],
        "equations": EQUATIONS,
        "viva": VIVA,
        "exam_questions": exam,
        "learning_outcomes": spec["outcomes"],
        "course_outcomes": ["CO4"],
        "practical_numbers": [12, 13, 14, 15],
        "content_kind": "theory",
        "lesson_count": LESSON_COUNT + len(items),
        "answered_practice_count": len(exam),
        "assessment_note": tr(
            "Official course: theory ESE 70 + PA 30 and practical PA 20 + ESE 30 = 150 marks, "
            "4 credits, 45 teaching hours. This unit carries 24 % weightage, 11 of the printed unit "
            "hours and 17 of the 70 theory marks - the largest single share of the paper, because "
            "the practical list (experiments 12 to 15) is all reactor work. The numericals of "
            "section 4.4 are original revision problems with suggested marks, not GTU papers.",
            "અધિકૃત course: theory ESE 70 + PA 30 અને practical PA 20 + ESE 30 = 150 marks, "
            "4 credits, 45 teaching hours. આ unit નું weightage 24 %, છપાયેલા unit hours માંથી 11 અને "
            "70 theory marks માંથી 17 છે - પેપરનો સૌથી મોટો હિસ્સો, કારણ કે practical યાદી "
            "(experiments 12 થી 15) આખી reactor નું કામ છે. વિભાગ 4.4 ના દાખલા revision માટેના મૂળ "
            "પ્રશ્નો છે, GTU પેપર નહીં."),
        "question_provenance": "Original solved numericals written for revision; not official past "
                               "papers",
        "question_marks_are_suggested": True,
        "sources": [{"title": n, "url": u} for n, u in SOURCES],
    }

    out = write_unit(unit)

    build_preview(unit, SUBJECT, str(DIAG_DIR),
                  str(ROOT / "preview/DI05005031_unit4_preview.html"))
    from notes_workshop import render_one
    render_one("DI05005031", 4, note="Unit 4 draft for review", register=True)

    st = json.loads(out.read_text())
    cards = sum(len(s["items"]) for s in st["notes"])
    print(f"Chemical Reaction Engineering Unit 4 {len(st['notes'])} sections / {cards} items "
          f"({LESSON_COUNT} teaching cards) / {len(st['diagrams'])} SVGs / "
          f"{sum(len(g['items']) for g in st['equations'])} formulae / "
          f"{sum(len(g['items']) for g in st['viva'])} viva / {len(st['exam_questions'])} problems")
    print("unit:   ", out.relative_to(ROOT))


# Gujarati titles and captions for the six figures (short enough for a card header).
CAPTIONS_GU = {
    "u4_models": "ત્રણ આદર્શ mixing models",
    "u4_batch": "Batch reactor, ભાગે ભાગે",
    "u4_semibatch": "Semi-batch reactor: અડધું batch",
    "u4_cstr": "CSTR: સંપૂર્ણ મિશ્ર flow reactor",
    "u4_pfr": "Tubular reactor: નળીમાં plug flow",
    "u4_fixed": "Fixed bed reactor (સ્થિર પડ)",
    "u4_fluidised": "Fluidised bed reactor (તરતો પડ)",
    "u4_slurry": "Slurry અને bubble column reactors",
    "u4_spray": "Spray tower અને trickle bed",
}

CAPTIONS_GU_TAIL = {
    "u4_models": "Batch: flow નહીં, એક જ રચના. CSTR: flow, અને outlet અંદરના જેવું જ. PFR: flow, અને "
                 "રચના નળીમાં આગળ સરકે, પાછળ મિક્સ ન થાય.",
    "u4_batch": "Jacket અને drain વાળું હલાવેલું પાત્ર: બધું શરૂઆતમાં ભરાય, અંત સુધી કંઈ નીકળે નહીં, "
                "અને આખો batch એક જ રચના જુએ.",
    "u4_semibatch": "એક reactant બીજામાં નિયંત્રિત rate પર ઉમેરાય, જેથી તેનું concentration નીચું "
                    "રહે - ઝડપી કે exothermic પ્રક્રિયા સંભાળવાનો પ્રમાણભૂત રસ્તો.",
    "u4_cstr": "Feed અંદર, product overflow થી બહાર, અને impeller એટલો ઝડપી કે outlet ની રચના અંદર "
               "દરેક જગ્યાની રચના જેવી જ હોય.",
    "u4_pfr": "પાછળ મિક્સિંગ વગરની નળી: દરેક element અંદર સરખો સમય ગાળે, અને concentration લંબાઈ પર "
              "batch ના સમય જેમ ઘટે.",
    "u4_fixed": "Catalyst pellets distributor અને support grid વચ્ચે બેસે; gas voids માંથી પસાર થાય, "
                "તેથી pressure drop અને hot spot design ની ચિંતા.",
    "u4_fluidised": "Gas distributor થી એટલી ઝડપે આવે કે particles ઊંચકાય: bed ઉકળતા પ્રવાહી જેવો "
                    "વર્તે, જે heat સરસ ઉપાડે પણ back-mixing ખરાબ કરે.",
    "u4_slurry": "Gas એ પ્રવાહીમાં bubbles કરે જેમાં catalyst તરે છે: bubble column માં હલતો ભાગ નથી, "
                 "slurry reactor માં ઘન તરતો રાખવા stirrer છે.",
    "u4_spray": "પ્રવાહી ટીપાં તરીકે કે packing પર પડ તરીકે પડે જ્યારે gas ઉપર જાય: spray tower gas ને "
                "વિશાળ contact area આપે, trickle bed catalyst ભીનો રાખે.",
}

if __name__ == "__main__":
    main()
