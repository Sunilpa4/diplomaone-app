"""Builds Unit 2 (Fundamentals of Semiconductors) JSON + preview. Real-notes format."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_DI01000151_u1 import SUBJECT, SUBJ_DIR, DIAG_DIR, ROOT, write_subject
from preview_builder import build_preview
from content_DI01000151_u2_notes import NOTES
from content_DI01000151_u2_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "u2_bohr_silicon": {"en": "Bohr Model of Silicon Atom", "gu": "Silicon Atom નો Bohr Model"},
    "u2_valence_atoms": {"en": "Trivalent, Tetravalent and Pentavalent Atoms", "gu": "Trivalent, Tetravalent અને Pentavalent Atoms"},
    "u2_energy_bands": {"en": "Energy Bands: Insulator, Semiconductor, Conductor", "gu": "Energy Bands: Insulator, Semiconductor, Conductor"},
    "u2_covalent_si": {"en": "Covalent Bonds in Silicon Crystal", "gu": "Silicon Crystal માં Covalent Bonds"},
    "u2_intrinsic": {"en": "Intrinsic Semiconductor – Electron-Hole Pair", "gu": "Intrinsic Semiconductor – Electron-Hole Pair"},
    "u2_ntype": {"en": "N-type Semiconductor", "gu": "N-type Semiconductor"},
    "u2_ptype": {"en": "P-type Semiconductor", "gu": "P-type Semiconductor"},
}

UNIT = {
    "subject": "DI01000151", "unit": 2, "format": "notes",
    "title": {"en": "Fundamentals of Semiconductors", "gu": "Semiconductors ના મૂળભૂત સિદ્ધાંતો"},
    "weightage": 15, "hours": 6,
    "notes": NOTES,
    "numericals": NUMERICALS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    # sanity: every referenced diagram / example exists
    ids = {n["id"] for n in NUMERICALS}
    for s in NOTES:
        for it in s["items"]:
            assert it.get("diagram") in (None, *DIAGRAM_TITLES), it.get("diagram")
            for e in it.get("examples", []):
                assert e in ids, e
    with open(os.path.join(SUBJ_DIR, "unit2.json"), "w", encoding="utf-8") as f:
        json.dump(UNIT, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(UNIT, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", "DI01000151_unit2_preview.html"))
    print("topics:", sum(len(s["items"]) for s in NOTES), "numericals:", len(NUMERICALS),
          "formulas:", sum(len(g["items"]) for g in EQUATIONS), "viva:", sum(len(g["items"]) for g in VIVA),
          "exam:", len(EXAM_QS))
    print("preview:", out)
