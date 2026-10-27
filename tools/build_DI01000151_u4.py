"""Builds Unit 4 (Bipolar Junction Transistor) JSON + preview. Real-notes format."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_DI01000151_u1 import SUBJECT, SUBJ_DIR, DIAG_DIR, ROOT, write_subject
from preview_builder import build_preview
from content_DI01000151_u4_notes_a import NOTES_A
from content_DI01000151_u4_notes_b import NOTES_B
from content_DI01000151_u4_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

NOTES = NOTES_A + NOTES_B

DIAGRAM_TITLES = {
    "u4_structure": {"en": "Construction of NPN and PNP Transistors", "gu": "NPN અને PNP Transistors ની રચના"},
    "u4_symbols": {"en": "Transistor Symbols and Current Directions", "gu": "Transistor Symbols અને Current ની દિશા"},
    "u4_npn_working": {"en": "Working of NPN Transistor", "gu": "NPN Transistor નું કાર્ય"},
    "u4_pnp_working": {"en": "Working of PNP Transistor", "gu": "PNP Transistor નું કાર્ય"},
    "u4_cb": {"en": "Common Base (CB) Configuration", "gu": "Common Base (CB) Configuration"},
    "u4_cb_char": {"en": "CB Input and Output Characteristics", "gu": "CB Input અને Output Characteristics"},
    "u4_ce": {"en": "Common Emitter (CE) Configuration", "gu": "Common Emitter (CE) Configuration"},
    "u4_ce_test": {"en": "Circuit for CE Characteristics", "gu": "CE Characteristics માટેનો Circuit"},
    "u4_ce_input": {"en": "CE Input Characteristics", "gu": "CE Input Characteristics"},
    "u4_ce_output": {"en": "CE Output Characteristics and Regions", "gu": "CE Output Characteristics અને Regions"},
    "u4_cc": {"en": "Common Collector (CC) Configuration", "gu": "Common Collector (CC) Configuration"},
    "u4_load_line": {"en": "DC Load Line and Operating Regions", "gu": "DC Load Line અને Operating Regions"},
    "u4_switch": {"en": "Transistor as a Switch", "gu": "Switch તરીકે Transistor"},
}

UNIT = {
    "subject": "DI01000151", "unit": 4, "format": "notes",
    "title": {"en": "Bipolar Junction Transistor", "gu": "Bipolar Junction Transistor (BJT)"},
    "weightage": 20, "hours": 6,
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
    with open(os.path.join(SUBJ_DIR, "unit4.json"), "w", encoding="utf-8") as f:
        json.dump(UNIT, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(UNIT, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", "DI01000151_unit4_preview.html"))
    print("topics:", sum(len(s["items"]) for s in NOTES), "numericals:", len(NUMERICALS),
          "formulas:", sum(len(g["items"]) for g in EQUATIONS), "viva:", sum(len(g["items"]) for g in VIVA),
          "exam:", len(EXAM_QS))
    print("preview:", out)
