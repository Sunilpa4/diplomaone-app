"""GTU Cloud Computing (DI04000041, Computer Sem 4, w.e.f. 2025-26) - subject metadata.

Syllabus source: tools/syllabus_DI04000041.txt (transcribed from the official GTU PDF).
English-only build, matching the recent Computer Sem 5 releases.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / "content/computer/sem4/DI04000041"
DIAG_DIR = SUBJ_DIR / "diagrams"
TABS = ["notes", "diagrams", "equations", "numericals", "viva", "exam"]


def tr(s):
    return {"en": s}


# (no, title, hours, weightage, topics)  6+10+9+10+10 = 45 h, 17+23+19+24+17 = 100 %
UNITS = [
    (1, "Introduction to Cloud Computing", 6, 17, [
        "Cloud, computing and the definition of cloud computing",
        "Central ideas behind cloud computing",
        "Characteristics of cloud computing",
        "Challenges of cloud computing",
        "Novel applications of cloud computing",
        "Security risks of cloud computing",
        "Advantages and disadvantages of cloud computing",
    ]),
    (2, "Cloud Computing Architecture and Deployment Model", 10, 23, [
        "Cloud computing architecture: front end and back end",
        "Components: client infrastructure, cloud access device, application, services, runtime cloud, storage, infrastructure, security",
        "Cloud deployment models: public, private, hybrid and community",
        "Comparative analysis of deployment models",
        "Key drivers to adopting the cloud and impact on users",
    ]),
    (3, "Cloud Service Model and Service Providers", 9, 19, [
        "SaaS, PaaS and IaaS: introduction, advantages, disadvantages and differences",
        "Service providers: AWS, Microsoft Azure, Google Cloud Platform, IBM Cloud, Oracle Cloud, Red Hat, VMware Cloud",
        "Service Level Agreement: introduction and life cycle",
    ]),
    (4, "Virtualization", 10, 24, [
        "Introduction and working of virtualization",
        "Desktop, network, storage, data, hardware and software virtualization",
        "Advantages, disadvantages, characteristics and applications of virtualization",
        "Hypervisors: type 1, type 2 and choosing the right hypervisor",
    ]),
    (5, "Security and Privacy in Cloud Computing", 10, 17, [
        "Infrastructure security at network, host and application level",
        "Data security and storage",
        "Privacy issues and key privacy concerns",
        "Data life cycle: generation, use, transfer, transformation, destruction, archival, storage",
        "Protecting privacy",
        "Cloud and big-data analytics for green hydrogen: predictive maintenance, efficiency optimisation and remote dashboards",
    ]),
]

SUBJECT = {
    "code": "DI04000041",
    "name": tr("Cloud Computing"),
    "branch": "computer",
    "semester": 4,
    "syllabus_year": "2025-26",
    "category": "Professional Elective - I",
    "type": "theory",
    "languages": ["en"],
    "code_lang": None,
    "teaching": {"lecture": 3, "tutorial": 0, "practical": 2},
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30,
             "total": 150, "credits": 4},
    "prerequisites": [
        "Basic knowledge of IT and networking",
        "Security fundamentals",
        "Programming",
        "Database",
    ],
    "units": [
        {"no": n, "title": tr(t), "hours": h, "weightage": w, "topics": topics, "file": None}
        for n, t, h, w, topics in UNITS
    ],
    "course_outcomes": [
        "CO1: Describe the principles and paradigm of cloud computing.",
        "CO2: Compare the deployment models with reference to cloud computing.",
        "CO3: Simulate the service model with reference to cloud computing.",
        "CO4: Evaluate various virtualization technologies and methods.",
        "CO5: Implement comprehensive security measures, ensuring the security and privacy of data.",
    ],
    # Official specification table: R 42 %, U 58 %, A/N/E/C 0 %.
    "theory_rbt_percent": {"remember": 42, "understand": 58, "apply": 0,
                           "analyze": 0, "evaluate": 0, "create": 0},
    "course_outcome_rbt": {
        "CO1": "Understand", "CO2": "Understand", "CO3": "Apply",
        "CO4": "Apply", "CO5": "Apply",
    },
    "practicals": [
        "Study cloud architecture and the cloud computing model.",
        "Study and implement Infrastructure as a Service; OpenStack computing components; install OpenStack on Ubuntu 18.04 with DevStack.",
        "Study and real-life application of Storage as a Service.",
        "Case study: choosing the right cloud deployment model (public, private, hybrid, community).",
        "Case study: comparative analysis of cloud service providers (AWS, Azure, Google Cloud) and their service models.",
        "Mini-project: flowchart for deploying a Hello World application on Google App Engine (steps only, no coding).",
        "Comparative chart of major cloud providers (AWS, Azure, Google Cloud, Oracle) with their unique features.",
        "Study Firebase Authentication and Cloud Datastore; flow diagram of user login and data storage.",
        "Comparative table of types of virtualization (desktop, network, storage, data, hardware, software).",
        "Case study: implementing virtualization in enterprise IT.",
        "Case study: data security and privacy in a cloud-based healthcare system.",
        "Case study: migration to the cloud from a banking perspective.",
        "Case study: a global company's hybrid cloud strategy.",
        "Case study: Netflix - personalized recommendations using cloud computing.",
        "Case study: National Renewable Energy Laboratory (NREL) Hydrogen Data Hub.",
    ],
    "books": [
        "Thomas Erl, Ricardo Puttini, Zaigham Mahmood - Cloud Computing: Concepts, Technology & Architecture (Pearson, ISBN 9780133387520)",
        "Judith Hurwitz, Robin Bloor, Marcia Kaufman, Fern Halper - Cloud Computing For Dummies (Wiley India)",
        "Kailash Jayaswal, Jagannath Kallakurchi, Donald J. Houde, Deven Shah - Cloud Computing Black Book (Dreamtech, ISBN 978-9351193944)",
        "Kris Jamsa - Cloud Computing: SaaS, PaaS, IaaS, Virtualization, Business Models, Mobile, Security and More (Jones & Bartlett Learning)",
        "Anthony T. Velte - Cloud Computing: A Practical Approach (Tata McGraw Hill, 2009)",
        "Rajkumar Buyya, Christian Vecchiola, S. Thamarai Selvi - Mastering Cloud Computing (McGraw Hill Education India)",
        "Kamal Kant Hiran et al. - Cloud Computing: Master the Concepts, Architecture and Applications (BPB, ISBN 978-9388511407)",
    ],
    "source_note": "Syllabus text transcribed from the supplied GTU DI04000041 PDF; unit hours, weightage, "
                   "marks and course outcomes are copied from it and are not invented. Reference URLs in "
                   "each unit point at the official documentation, not at mirrors.",
    "source_discrepancies": {
        "rbt_vs_co_levels": "The specification table lists 0 % for Apply (R 42 / U 58 / A 0 / N 0 / E 0 / C 0), "
                            "while the course-outcome table marks CO3-CO5 as Apply level. Both are reproduced "
                            "as printed; no percentage is adjusted.",
        "practical_hours": "The teaching scheme gives 2 practical hours per week and 150 total marks, but no "
                           "individual practical durations; none are invented.",
    },
}


def write_subject():
    SUBJ_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(exist_ok=True)
    for spec in SUBJECT["units"]:
        name = f"unit{spec['no']}.json"
        spec["file"] = name if (SUBJ_DIR / name).is_file() else None
    (SUBJ_DIR / "subject.json").write_text(
        json.dumps(SUBJECT, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def _check_english_only(obj):
    if isinstance(obj, dict):
        assert "gu" not in obj, "English-only build must not carry 'gu' keys"
        for v in obj.values():
            _check_english_only(v)
    elif isinstance(obj, list):
        for v in obj:
            _check_english_only(v)
    elif isinstance(obj, str):
        assert not re.search(r"[\u0a80-\u0aff]", obj), f"Gujarati text in English-only unit: {obj[:60]!r}"


def write_unit(unit):
    SUBJ_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(exist_ok=True)
    spec = SUBJECT["units"][unit["unit"] - 1]
    assert unit["title"] == spec["title"], "unit title must match subject.json"
    assert (unit["hours"], unit["weightage"]) == (spec["hours"], spec["weightage"]), "hours/weightage mismatch"
    _check_english_only(unit)
    out = SUBJ_DIR / f"unit{unit['unit']}.json"
    out.write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    write_subject()
    return out


if __name__ == "__main__":
    write_subject()
    print("subject written:", SUBJ_DIR / "subject.json")
