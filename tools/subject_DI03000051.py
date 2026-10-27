"""Subject metadata for DI03000051 Computer Networks (Computer Sem 3) - shared by all unit builders.
Bilingual (EN + GU), theory subject: notes, diagrams, equations / numericals (where useful), viva, exam."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem3", "DI03000051")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)

TABS = ["notes", "programs", "diagrams", "syntax", "equations", "numericals", "viva", "exam"]
TAB_KEY = {"exam": "exam_questions"}


def _u(no, en, gu, h, w, topics):
    return {"no": no, "title": {"en": en, "gu": gu}, "hours": h, "weightage": w, "topics": topics, "file": None}


SUBJECT = {
    "code": "DI03000051",
    "name": {"en": "Computer Networks", "gu": "કમ્પ્યુટર નેટવર્ક્સ"},
    "branch": "computer", "semester": 3, "syllabus_year": "2024-25", "type": "theory",
    "languages": ["en", "gu"],
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 4},
    "units": [
        _u(1, "Basics of Computer Network", "Computer Network ની મૂળભૂત બાબતો", 8, 18,
           ["1.1 Definition and need of networks, applications", "1.2 Types of connection: point to point, multipoint",
            "1.3 LAN, MAN, WAN, Internet", "1.4 Network topology: bus, star, ring, mesh, hybrid, tree",
            "1.5 Standard organizations and protocols", "1.6 Types of servers"]),
        _u(2, "The Reference Model for Network Communication", "Network Communication માટેના Reference Models", 8, 18,
           ["2.1 OSI model and functions of each layer", "2.2 TCP/IP model and functions of each layer",
            "2.3 Comparison of OSI and TCP/IP"]),
        _u(3, "Transmission Media and Network Devices", "Transmission Media અને Network Devices", 10, 22,
           ["3.1 Guided media: twisted pair, coaxial, fiber optics", "3.2 Unguided media: propagation, spectrum, radio, microwave, infrared, satellite",
            "3.3 Network devices: repeater, hub, switch, router, access point, gateway, bridge, NIC", "3.4 Layer 2 vs Layer 3 switch"]),
        _u(4, "IP Protocol", "IP Protocol", 10, 22,
           ["4.1 IPv4: classful and classless addressing", "4.2 Subnetting, masking, reserved addresses",
            "4.3 IPv6: addressing modes, address types, special addresses", "4.4 IPv4 vs IPv6"]),
        _u(5, "Network Security Aspects", "Network Security ના પાસાં", 9, 20,
           ["5.1 Confidentiality, integrity, availability", "5.2 Threats to security", "5.3 Firewalls: packet filter, proxy firewall"]),
    ],
    "practicals": [
        "Topology with six devices: cables and ports for bus, ring, star, mesh", "Study of OSI model layers",
        "Prepare and test straight and cross UTP cable", "Study and test network devices",
        "Valid / invalid IPv4 address, class, network and host ID", "Class and network address from IPv4 address and subnet mask",
        "Subnet 216.21.5.0/24 into subnets of 30 hosts", "Identify valid and invalid IPv6 addresses",
        "Study of firewall", "Network commands: ipconfig, ping, tracert, netstat, pathping, route",
        "List adapters and configure a LAN connection"],
    "books": ["Andrew Tanenbaum – Computer Networks (Pearson)", "Behrouz A. Forouzan – Data Communication and Networking (McGraw-Hill)",
              "Bhushan Trivedi – Computer Networks (Oxford University Press)"],
}

BAD = re.compile(r"&amp;(lt|gt|amp);|&lt;b&gt;")


def write_subject():
    for u in SUBJECT["units"]:
        fn = f'unit{u["no"]}.json'
        u["file"] = fn if os.path.exists(os.path.join(SUBJ_DIR, fn)) else None
    with open(os.path.join(SUBJ_DIR, "subject.json"), "w", encoding="utf-8") as f:
        json.dump(SUBJECT, f, ensure_ascii=False, indent=1)


def _bi(d, where):
    assert isinstance(d, dict) and d.get("en") and d.get("gu"), f"missing en/gu: {where}"


def check_and_write(unit, diagram_titles, preview_name):
    from preview_builder import build_preview
    unit["tabs"] = [t for t in TABS if t in ("notes", "diagrams") or unit.get(TAB_KEY.get(t, t))]
    unit["diagrams"] = [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in diagram_titles.items()]
    items = [it for s in unit["notes"] for it in s["items"]]
    used_d = [it.get("diagram") for it in items if it.get("diagram")]
    used_n = {n for it in items for n in it.get("examples", [])}
    nids = [n["id"] for n in unit["numericals"]]
    assert len(nids) == len(set(nids)), "duplicate numerical id"
    assert set(used_d) == set(diagram_titles), set(diagram_titles) ^ set(used_d)
    assert used_n <= set(nids), used_n - set(nids)
    pids = [p["id"] for p in unit.get("programs", [])]
    assert len(pids) == len(set(pids)), "duplicate program id"
    used_p = [p for it in items for p in it.get("programs", [])]
    assert set(used_p) <= set(pids), set(used_p) - set(pids)
    assert set(pids) <= set(used_p), ("programs not linked in notes", set(pids) - set(used_p))
    for p in unit.get("programs", []):
        _bi(p["title"], p["id"]); _bi(p["code"], p["id"]); _bi(p["expl"], p["id"]); assert p["out"], p["id"]
    for g in unit.get("syntax", []):
        _bi(g["title"], "syntax group")
        for it in g["items"]:
            _bi(it["name"], it["f"]); _bi(it["terms"], it["f"])
    if "intro_text" in unit:
        _bi(unit["intro_text"], "intro_text")
    for k, v in diagram_titles.items():
        _bi(v, k)
        assert os.path.exists(os.path.join(DIAG_DIR, k + ".svg")), k
    for s in unit["notes"]:
        _bi(s["title"], "section")
        for it in s["items"]:
            _bi(it["h"], it["h"]); _bi(it["body"], it["h"]["en"])
    for n in unit["numericals"]:
        _bi(n["q"], n["id"]); _bi(n["a"], n["id"])
    for g in unit["viva"] + unit["equations"]:
        _bi(g["title"], "group")
    for x in unit["exam_questions"]:
        _bi(x["q"], x["q"])
    txt = json.dumps(unit, ensure_ascii=False)
    assert not BAD.search(txt), BAD.search(txt).group(0)
    assert "@@" not in txt
    with open(os.path.join(SUBJ_DIR, f'unit{unit["unit"]}.json'), "w", encoding="utf-8") as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(unit, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", preview_name))
    print("tabs:", unit["tabs"], "programs:", len(pids), "syntax:", sum(len(g["items"]) for g in unit.get("syntax", [])))
    print("topics:", len(items), "diagrams:", len(diagram_titles), "equations:", sum(len(g["items"]) for g in unit["equations"]),
          "numericals:", len(nids), "viva:", sum(len(g["items"]) for g in unit["viva"]), "exam:", len(unit["exam_questions"]))
    print("preview:", os.path.normpath(out))
