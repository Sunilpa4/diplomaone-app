"""Builds DI03000051 Computer Networks Unit 1 (Basics of Computer Network). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000051 import check_and_write
from content_DI03000051_u1_notes import NOTES
from content_DI03000051_u1_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "cn1_basic": {"en": "Components of Data Communication", "gu": "Data Communication ના ઘટકો"},
    "cn1_conn": {"en": "Point to Point and Multipoint", "gu": "Point to Point અને Multipoint"},
    "cn1_lan": {"en": "Local Area Network (LAN)", "gu": "Local Area Network (LAN)"},
    "cn1_man": {"en": "Metropolitan Area Network (MAN)", "gu": "Metropolitan Area Network (MAN)"},
    "cn1_wan": {"en": "Wide Area Network (WAN)", "gu": "Wide Area Network (WAN)"},
    "cn1_internet": {"en": "The Internet: Network of Networks", "gu": "Internet: Networks નું Network"},
    "cn1_bus": {"en": "Bus Topology", "gu": "Bus Topology"},
    "cn1_star": {"en": "Star Topology", "gu": "Star Topology"},
    "cn1_ring": {"en": "Ring Topology", "gu": "Ring Topology"},
    "cn1_mesh": {"en": "Mesh Topology (6 devices)", "gu": "Mesh Topology (6 devices)"},
    "cn1_tree": {"en": "Tree Topology", "gu": "Tree Topology"},
    "cn1_hybrid": {"en": "Hybrid Topology", "gu": "Hybrid Topology"},
    "cn1_client_server": {"en": "Client-Server Network and Servers", "gu": "Client-Server Network અને Servers"},
    "cn1_proxy": {"en": "Proxy Server", "gu": "Proxy Server"},
}

UNIT = {
    "subject": "DI03000051", "unit": 1, "format": "notes",
    "title": {"en": "Basics of Computer Network", "gu": "Computer Network ની મૂળભૂત બાબતો"},
    "weightage": 18, "hours": 8,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000051_u1.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000051_unit1_preview.html")
