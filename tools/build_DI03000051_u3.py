"""Builds DI03000051 Computer Networks Unit 3 (Transmission Media and Network Devices). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000051 import check_and_write
from content_DI03000051_u3_notes import NOTES
from content_DI03000051_u3_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "cn3_class": {"en": "Classification of Transmission Media", "gu": "Transmission Media નું વર્ગીકરણ"},
    "cn3_tp": {"en": "Twisted Pair Cable: UTP and STP", "gu": "Twisted Pair Cable: UTP અને STP"},
    "cn3_rj45": {"en": "RJ-45 Colour Codes (Practical 3)", "gu": "RJ-45 Colour Codes (Practical 3)"},
    "cn3_coax": {"en": "Coaxial Cable", "gu": "Coaxial Cable"},
    "cn3_fiber": {"en": "Fiber Optic Cable: Structure", "gu": "Fiber Optic Cable: રચના"},
    "cn3_fiber_modes": {"en": "Fiber Optic Propagation Modes", "gu": "Fiber Optic Propagation Modes"},
    "cn3_prop": {"en": "Propagation Methods", "gu": "Propagation Methods"},
    "cn3_spectrum": {"en": "Electromagnetic Spectrum", "gu": "Electromagnetic Spectrum"},
    "cn3_microwave": {"en": "Terrestrial Microwave Transmission", "gu": "Terrestrial Microwave Transmission"},
    "cn3_satellite": {"en": "Satellite Transmission", "gu": "Satellite Transmission"},
    "cn3_repeater": {"en": "Repeater: Regenerates the Signal", "gu": "Repeater: Signal ફરી બનાવે"},
    "cn3_hub_switch": {"en": "Hub (broadcast) vs Switch (unicast)", "gu": "Hub (broadcast) vs Switch (unicast)"},
    "cn3_bridge": {"en": "Bridge: Connects Two LAN Segments", "gu": "Bridge: બે LAN Segments જોડે"},
    "cn3_router": {"en": "Router: Connects Different Networks", "gu": "Router: જુદા Networks જોડે"},
    "cn3_ap": {"en": "Wireless Access Point (Wi-Fi)", "gu": "Wireless Access Point (Wi-Fi)"},
    "cn3_nic": {"en": "Network Interface Card (NIC)", "gu": "Network Interface Card (NIC)"},
    "cn3_dev_osi": {"en": "Network Devices and OSI Layers", "gu": "Network Devices અને OSI Layers"},
}

UNIT = {
    "subject": "DI03000051", "unit": 3, "format": "notes",
    "title": {"en": "Transmission Media and Network Devices", "gu": "Transmission Media અને Network Devices"},
    "weightage": 22, "hours": 10,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000051_u3.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000051_unit3_preview.html")
