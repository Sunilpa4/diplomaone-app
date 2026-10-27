"""Builds DI03000051 Computer Networks Unit 4 (IP Protocol). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000051 import check_and_write
from content_DI03000051_u4_notes import NOTES
from content_DI03000051_u4_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "cn4_v4fmt": {"en": "IPv4 Address: 32 Bits, 4 Octets", "gu": "IPv4 Address: 32 Bits, 4 Octets"},
    "cn4_v4hdr": {"en": "IPv4 Datagram Header", "gu": "IPv4 Datagram Header"},
    "cn4_classes": {"en": "Classful Addressing: Classes A to E", "gu": "Classful Addressing: Classes A થી E"},
    "cn4_space": {"en": "Address Space of Each Class", "gu": "દરેક Class નું Address Space"},
    "cn4_netid": {"en": "Network ID and Host ID (Class B)", "gu": "Network ID અને Host ID (Class B)"},
    "cn4_mask": {"en": "Subnet Mask: Network Address (AND)", "gu": "Subnet Mask: Network Address (AND)"},
    "cn4_subnet": {"en": "Subnetting 216.21.5.0/24 (30 Hosts Each)", "gu": "Subnetting 216.21.5.0/24 (દરેકમાં 30 Hosts)"},
    "cn4_cidr": {"en": "Classless Block: 205.16.37.39/28", "gu": "Classless Block: 205.16.37.39/28"},
    "cn4_reserved": {"en": "Reserved and Special IPv4 Addresses", "gu": "Reserved અને Special IPv4 Addresses"},
    "cn4_v6fmt": {"en": "IPv6 Address: 128 Bits, 8 Groups", "gu": "IPv6 Address: 128 Bits, 8 Groups"},
    "cn4_v6hdr": {"en": "IPv6 Base Header (40 Bytes)", "gu": "IPv6 Base Header (40 Bytes)"},
    "cn4_v6modes": {"en": "IPv6 Addressing Modes", "gu": "IPv6 Addressing Modes"},
    "cn4_v6types": {"en": "IPv6 Global Unicast and Address Types", "gu": "IPv6 Global Unicast અને Address Types"},
}

UNIT = {
    "subject": "DI03000051", "unit": 4, "format": "notes",
    "title": {"en": "IP Protocol", "gu": "IP Protocol"},
    "weightage": 22, "hours": 10,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000051_u4.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000051_unit4_preview.html")
