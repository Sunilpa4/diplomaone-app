"""Builds Unit 5 (IC 555 Timer) JSON + preview. Real-notes format."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_DI01000151_u1 import SUBJECT, SUBJ_DIR, DIAG_DIR, ROOT, write_subject
from preview_builder import build_preview
from content_DI01000151_u5_notes_a import NOTES_A
from content_DI01000151_u5_notes_b import NOTES_B
from content_DI01000151_u5_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

NOTES = NOTES_A + NOTES_B

DIAGRAM_TITLES = {
    "u5_pin_diagram": {"en": "Pin Diagram of IC 555", "gu": "IC 555 નો Pin Diagram"},
    "u5_block_diagram": {"en": "Functional Block Diagram of IC 555", "gu": "IC 555 નો Functional Block Diagram"},
    "u5_mono_circuit": {"en": "555 as Monostable Multivibrator", "gu": "Monostable Multivibrator તરીકે 555"},
    "u5_mono_wave": {"en": "Monostable Waveforms", "gu": "Monostable Waveforms"},
    "u5_astable_circuit": {"en": "555 as Astable Multivibrator", "gu": "Astable Multivibrator તરીકે 555"},
    "u5_astable_wave": {"en": "Astable Waveforms", "gu": "Astable Waveforms"},
    "u5_led_flasher": {"en": "555 as LED Flasher (Pulse Generator)", "gu": "LED Flasher (Pulse Generator) તરીકે 555"},
    "u5_freq_counter": {"en": "Frequency Counter using 555", "gu": "555 વાપરીને Frequency Counter"},
}

UNIT = {
    "subject": "DI01000151", "unit": 5, "format": "notes",
    "title": {"en": "IC 555 Timer", "gu": "IC 555 Timer"},
    "weightage": 15, "hours": 4,
    "notes": NOTES,
    "numericals": NUMERICALS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    # sanity: every referenced diagram / example exists, every diagram used, every example referenced
    used_d = {it.get("diagram") for s in NOTES for it in s["items"]} - {None}
    used_e = {e for s in NOTES for it in s["items"] for e in it.get("examples", [])}
    assert used_d == set(DIAGRAM_TITLES), set(DIAGRAM_TITLES) ^ used_d
    assert used_e == {n["id"] for n in NUMERICALS}, used_e
    for k in DIAGRAM_TITLES:
        assert os.path.exists(os.path.join(DIAG_DIR, k + ".svg")), k
    ids = {n["id"] for n in NUMERICALS}
    for s in NOTES:
        for it in s["items"]:
            assert it.get("diagram") in (None, *DIAGRAM_TITLES), it.get("diagram")
            for e in it.get("examples", []):
                assert e in ids, e
    with open(os.path.join(SUBJ_DIR, "unit5.json"), "w", encoding="utf-8") as f:
        json.dump(UNIT, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(UNIT, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", "DI01000151_unit5_preview.html"))
    print("topics:", sum(len(s["items"]) for s in NOTES), "numericals:", len(NUMERICALS),
          "formulas:", sum(len(g["items"]) for g in EQUATIONS), "viva:", sum(len(g["items"]) for g in VIVA),
          "exam:", len(EXAM_QS))
    print("preview:", out)
