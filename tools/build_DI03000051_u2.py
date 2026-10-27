"""Builds DI03000051 Computer Networks Unit 2 (The Reference Model for Network Communication). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000051 import check_and_write
from content_DI03000051_u2_notes import NOTES
from content_DI03000051_u2_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "cn2_osi": {"en": "OSI Reference Model: 7 Layers", "gu": "OSI Reference Model: 7 Layers"},
    "cn2_peer": {"en": "Peer-to-Peer Communication in OSI", "gu": "OSI માં Peer-to-Peer Communication"},
    "cn2_encap": {"en": "Encapsulation and Decapsulation", "gu": "Encapsulation અને Decapsulation"},
    "cn2_modes": {"en": "Transmission Modes", "gu": "Transmission Modes"},
    "cn2_frame": {"en": "Data Link Layer: Frame Format", "gu": "Data Link Layer: Frame Format"},
    "cn2_hop": {"en": "Network Layer vs Data Link Layer", "gu": "Network Layer vs Data Link Layer"},
    "cn2_ports": {"en": "Transport Layer: Process to Process", "gu": "Transport Layer: Process to Process"},
    "cn2_session": {"en": "Session Layer: Synchronisation Points", "gu": "Session Layer: Synchronisation Points"},
    "cn2_present": {"en": "Presentation Layer Functions", "gu": "Presentation Layer નાં કાર્યો"},
    "cn2_tcpip": {"en": "TCP/IP Model and Protocol Suite", "gu": "TCP/IP Model અને Protocol Suite"},
    "cn2_map": {"en": "OSI vs TCP/IP: Layer Mapping", "gu": "OSI vs TCP/IP: Layer Mapping"},
    "cn2_addr": {"en": "Addresses Used in TCP/IP", "gu": "TCP/IP માં વપરાતા Addresses"},
}

UNIT = {
    "subject": "DI03000051", "unit": 2, "format": "notes",
    "title": {"en": "The Reference Model for Network Communication", "gu": "Network Communication માટેના Reference Models"},
    "weightage": 18, "hours": 8,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000051_u2.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000051_unit2_preview.html")
