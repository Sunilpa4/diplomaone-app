"""Builds DI03000051 Computer Networks Unit 5 (Network Security Aspects). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000051 import check_and_write
from content_DI03000051_u5_notes import NOTES
from content_DI03000051_u5_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "cn5_attacks": {"en": "Security Attacks on a Message", "gu": "Message પર Security Attacks"},
    "cn5_cia": {"en": "CIA Triad of Security", "gu": "Security નો CIA Triad"},
    "cn5_encrypt": {"en": "Confidentiality: Encryption", "gu": "Confidentiality: Encryption"},
    "cn5_hash": {"en": "Integrity: Hash Check", "gu": "Integrity: Hash Check"},
    "cn5_dos": {"en": "Availability Attack: DDoS", "gu": "Availability Attack: DDoS"},
    "cn5_pyramid": {"en": "Threat Sophistication Levels", "gu": "Threat Sophistication Levels"},
    "cn5_virus_worm": {"en": "Virus vs Worm", "gu": "Virus vs Worm"},
    "cn5_firewall": {"en": "Firewall: Working", "gu": "Firewall: કાર્યપદ્ધતિ"},
    "cn5_dmz": {"en": "Firewall Design: DMZ", "gu": "Firewall Design: DMZ"},
    "cn5_fw_osi": {"en": "Firewall Types and OSI Layers", "gu": "Firewall Types અને OSI Layers"},
    "cn5_pfilter": {"en": "Packet Filter Firewall", "gu": "Packet Filter Firewall"},
    "cn5_proxy": {"en": "Proxy Firewall (Application Gateway)", "gu": "Proxy Firewall (Application Gateway)"},
}

UNIT = {
    "subject": "DI03000051", "unit": 5, "format": "notes",
    "title": {"en": "Network Security Aspects", "gu": "Network Security Aspects"},
    "weightage": 20, "hours": 9,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000051_u5.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000051_unit5_preview.html")
