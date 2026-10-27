"""Builds Unit 3 (Diodes and Rectifiers) JSON + preview. Real-notes format."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_DI01000151_u1 import SUBJECT, SUBJ_DIR, DIAG_DIR, ROOT, write_subject
from preview_builder import build_preview
from content_DI01000151_u3_notes_a import NOTES_A
from content_DI01000151_u3_notes_b import NOTES_B
from content_DI01000151_u3_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

NOTES = NOTES_A + NOTES_B

DIAGRAM_TITLES = {
    "u3_pn_junction": {"en": "P-N Junction and Depletion Layer", "gu": "P-N Junction અને Depletion Layer"},
    "u3_diode_symbol": {"en": "P-N Junction Diode Symbol", "gu": "P-N Junction Diode નો Symbol"},
    "u3_forward_bias": {"en": "Forward Biased P-N Junction", "gu": "Forward Biased P-N Junction"},
    "u3_reverse_bias": {"en": "Reverse Biased P-N Junction", "gu": "Reverse Biased P-N Junction"},
    "u3_vi_circuit": {"en": "Circuit for Diode V-I Characteristics", "gu": "Diode V-I Characteristics માટેનો Circuit"},
    "u3_vi_char": {"en": "V-I Characteristics of P-N Diode", "gu": "P-N Diode ની V-I Characteristics"},
    "u3_zener_char": {"en": "Zener Diode V-I Characteristics", "gu": "Zener Diode ની V-I Characteristics"},
    "u3_zener_regulator": {"en": "Zener Diode as Voltage Regulator", "gu": "Voltage Regulator તરીકે Zener Diode"},
    "u3_varactor": {"en": "Varactor Diode – Symbol and C-V Curve", "gu": "Varactor Diode – Symbol અને C-V Curve"},
    "u3_photodiode": {"en": "Photodiode – Symbol and Characteristics", "gu": "Photodiode – Symbol અને Characteristics"},
    "u3_led": {"en": "Light Emitting Diode (LED)", "gu": "Light Emitting Diode (LED)"},
    "u3_multicolour_led": {"en": "Multicolour LEDs (Bi-colour and RGB)", "gu": "Multicolour LEDs (Bi-colour અને RGB)"},
    "u3_hwr": {"en": "Half-Wave Rectifier with Waveforms", "gu": "Waveforms સાથે Half-Wave Rectifier"},
    "u3_fwr_ct": {"en": "Centre-Tap Full-Wave Rectifier with Waveforms", "gu": "Waveforms સાથે Centre-Tap Full-Wave Rectifier"},
    "u3_bridge": {"en": "Full-Wave Bridge Rectifier with Waveforms", "gu": "Waveforms સાથે Full-Wave Bridge Rectifier"},
}

UNIT = {
    "subject": "DI01000151", "unit": 3, "format": "notes",
    "title": {"en": "Diodes and Rectifiers", "gu": "Diodes અને Rectifiers"},
    "weightage": 30, "hours": 8,
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
    with open(os.path.join(SUBJ_DIR, "unit3.json"), "w", encoding="utf-8") as f:
        json.dump(UNIT, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(UNIT, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", "DI01000151_unit3_preview.html"))
    print("topics:", sum(len(s["items"]) for s in NOTES), "numericals:", len(NUMERICALS),
          "formulas:", sum(len(g["items"]) for g in EQUATIONS), "viva:", sum(len(g["items"]) for g in VIVA),
          "exam:", len(EXAM_QS))
    print("preview:", out)
