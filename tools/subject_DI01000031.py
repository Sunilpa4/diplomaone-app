"""GTU Communication Skills in English (DI01000031) - Semester 1, w.e.f. 2024-25.

Branch: All (the PDF prints "Branch: All"), so subject.json marks the subject common to every
diploma branch and the exporter lists it in semester 1 of all of them.

Syllabus source: tools/syllabus_DI01000031.txt (transcribed from the uploaded PDF, sha256 kept in
subject.json). Unit hours, the 14/28/14/14 marks split, the theory totals and the course outcomes
are copied from the PDF exactly.

Content policy for this subject (author's decision): the prose and poetry unit carries full
summaries and question-answer sets, while grammar and the communication/writing units stay
example-driven - rules are one line each, followed by model sentences.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / "content/common/sem1/DI01000031"
DIAG_DIR = SUBJ_DIR / "diagrams"
TABS = ["notes", "diagrams", "viva", "exam"]

CODE = "DI01000031"
TITLE = "Communication Skills in English"


def tr(s):
    return {"en": s}


# (no, title, hours, weightage, official, topics, course_outcome)
UNITS = [
    (1, "Theory of Communication", 6, 20, True, [
        "Concept of effective communication and communication skills",
        "Basic communication models (S+E+C+D+R+N+F)",
        "Level of communication: upward and downward",
        "Types of communication: verbal, non-verbal and visual",
        "Types of communication: interpersonal, intrapersonal, extra personal and mass",
        "Barriers of effective communication",
    ], "CO1"),
    (2, "Grammar", 10, 40, True, [
        "Parts of speech: noun, verb, pronoun, adjective, adverb, preposition, conjunction, "
        "interjection",
        "Tenses: present simple, continuous, perfect and perfect continuous",
        "Tenses: past simple, continuous and perfect; future simple",
        "Modal auxiliaries: can, could, may, might, must, shall, will, should, would, ought to, need",
        "Subject-verb agreement",
        "Basic sentence patterns of English: SV, SVO, SVA, SVC",
    ], "CO2"),
    (3, "Prose and Poetry", 6, 20, True, [
        "Prose: The Leopard - Ruskin Bond",
        "Short story: After Twenty Years - O. Henry",
        "Poetry: Stopping by Woods on a Snowy Evening - Robert Frost",
    ], "CO3"),
    (4, "Techniques of Writing", 8, 20, True, [
        "Email writing: format and types (inquiry, reply to inquiry, order, complaint)",
        "Paragraph writing of about 150 words",
        "Paragraph topics: festivals, nature and environment, famous personalities, favourite "
        "sports, friends and family members",
    ], "CO4"),
]

SUBJECT = {
    "code": CODE,
    "name": tr(TITLE),
    "branch": "common",
    "common_to_all_branches": True,
    "semester": 1,
    "syllabus_year": "2024-25",
    "category": "Humanities, Social Science and Management (HSMC-1)",
    "type": "theory",
    "languages": ["en"],
    "code_lang": None,
    "teaching": {"lecture": 2, "tutorial": 0, "practical": 2},
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30,
             "total": 150, "credits": 3},
    "prerequisites": ["Basic knowledge of English"],
    "units": [
        {"no": n, "title": tr(t), "hours": h, "weightage": w, "official": official,
         "topics": topics, "course_outcome": co, "file": None}
        for n, t, h, w, official, topics, co in UNITS
    ],
    "course_outcomes": [
        "CO1: Use strategies to minimize barriers of effective communication.",
        "CO2: Construct grammatically correct sentences.",
        "CO3: Develop reading and listening skills in terms of fluency and comprehensibility.",
        "CO4: Compose different types of written communication.",
        "CO5: Communicate orally in a given situation with a purpose.",
    ],
    "course_outcome_rbt": {"CO1": "Application", "CO2": "Application", "CO3": "Application",
                           "CO4": "Application", "CO5": "Application"},
    # Official specification table: marks per unit out of the 70-mark theory paper.
    "theory_marks_by_unit": {"1": 14, "2": 28, "3": 14, "4": 14},
    "theory_rbt_percent": {"remember": 24, "understand": 41, "apply": 34,
                           "analyze": 0, "evaluate": 0, "create": 0},
    "theory_rbt_marks": {"remember": 17, "understand": 29, "apply": 24,
                         "analyze": 0, "evaluate": 0, "create": 0},
    "total_hours": 30,
    "source_pdf_sha256": "378d668600cb73ec90abbc823afa1663f1afef60a2832de6b3e111dfbf84511e",
    "source_note": "Syllabus text transcribed from the uploaded GTU DI01000031 PDF "
                   "(Communication Skills in English, Semester 1, HSMC-1). Unit hours, weightages, "
                   "the 70 + 30 + 20 + 30 marks split and the course outcomes are copied from it.",
    "official_practicals": [
        {"no": 1, "outcome": "Listening to recorded lectures, poems, interviews and speeches",
         "co": "CO1, CO3", "hours": 4, "compulsory": True},
        {"no": 2, "outcome": "Use antonyms and synonyms effectively in oral and written forms",
         "co": "CO3, CO4", "hours": 4, "compulsory": True},
        {"no": 3, "outcome": "Use grammatically correct sentences", "co": "CO2, CO5", "hours": 2,
         "compulsory": False},
        {"no": 4, "outcome": "Communicate ideas effectively and fluently in oral and written "
                             "communication", "co": "CO1, CO2, CO3, CO5", "hours": 2,
         "compulsory": True},
        {"no": 5, "outcome": "Articulate vowels, consonants and diphthongs correctly",
         "co": "CO1, CO5", "hours": 2, "compulsory": True},
        {"no": 6, "outcome": "Speak with appropriate intonation, voice modulation, pitch, speed and "
                             "volume", "co": "CO1, CO5", "hours": 2, "compulsory": False},
        {"no": 7, "outcome": "Participate in conversations (group discussion, meetings)",
         "co": "CO1, CO3, CO5", "hours": 4, "compulsory": True},
        {"no": 8, "outcome": "Deliver a presentation effectively in the class",
         "co": "CO1, CO3, CO5", "hours": 4, "compulsory": True},
        {"no": 9, "outcome": "Communicate effectively through verbal and non-verbal means",
         "co": "CO1, CO3, CO5", "hours": 4, "compulsory": True},
        {"no": 10, "outcome": "Practice online exercises for listening and reading comprehension",
         "co": "CO3, CO5", "hours": 2, "compulsory": True},
    ],
    "practicals": [],
    "books": [
        "W. S. Allen - Living English Structures (Pearson Education India, 1992), "
        "ISBN 9788131728499",
        "N. K. Aggrawal - Essentials of English Grammar and Composition (Goyal Brothers "
        "Prakashan, 2015), ISBN 8183896162",
        "M. Gnanamurali - English Grammar at a Glance (S. Chand & Co., 2010), "
        "ISBN 9788121929042",
        "E. Suresh Kumar and others - Effective English (Pearson, 2010), ISBN 9788131731000",
        "S. Chandrashekhar and others - English Communication for Polytechnics (Orient BlackSwan, "
        "2013), ISBN 8125037462",
        "English Fluency Step 1 and 2 (Macmillan, 2010), ISBN 9781405003650 / 9781405003667",
        "Active English Dictionary (Longman, 1991), ISBN 8131707865",
        "Daniel Jones - The Pronunciation of English (Cambridge University Press, 4th edition, "
        "1956), ISBN 0521093694",
        "James Hartman et al. - English Pronouncing Dictionary (Cambridge University Press, 17th "
        "edition, 2006), ISBN 0521680867",
        "Kulbhushan Kumar - Effective Communication Skills (Khanna Publishing House, New Delhi, "
        "revised edition 2018), ISBN 9789382609940",
        "J. D. O'Connor - Better English Pronunciation (Cambridge University Press, 1982), "
        "ISBN 0521231523",
        "Lindley Murray - An English Grammar: Comprehending Principles and Rules (Franklin "
        "Classics, 2018), ISBN 0342097008",
        "Margaret M. Maison - Examine your English (Orient Longman, New Delhi, 1964), "
        "ISBN 812500176X",
        "J. Sethi et al. - A Practice Course in English Pronunciation (Prentice Hall, New Delhi, "
        "2004), ISBN 9788120325944",
        "William Sanborn Pfeiffer and T. V. S. Padmaja - Technical Communication: A Practical "
        "Approach (Pearson, Delhi, 2007), ISBN 9788131700884",
    ],
    "learning_resources": [
        "British Council LearnEnglish - https://learnenglish.britishcouncil.org",
        "Free English Study - http://www.free-english-study.com/",
        "English Online - http://www.english-online.org.uk/",
        "TalkEnglish - http://www.talkenglish.com/",
        "Learn English - http://www.learnenglish.de/",
        "Cambridge Linguaskill - https://www.cambridgeenglish.org/exams-and-tests/linguaskill/",
        "Cambridge Dictionary - https://dictionary.cambridge.org/dictionary/english/",
        "Oxford Learner's Dictionaries - https://www.oxfordlearnersdictionaries.com/",
        "Language lab software, headphones and LCD projector in the classroom",
    ],
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
        assert not re.search(r"[\u0a80-\u0aff]", obj), \
            f"Gujarati text in an English-only unit: {obj[:60]!r}"


def spec_for(number):
    for spec in SUBJECT["units"]:
        if spec["no"] == number:
            return spec
    raise AssertionError(f"unit {number} is not registered for {CODE}")


def write_unit(unit):
    SUBJ_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(exist_ok=True)
    spec = spec_for(unit["unit"])
    assert unit["title"] == spec["title"], "unit title must match subject.json"
    assert (unit["hours"], unit["weightage"]) == (spec["hours"], spec["weightage"]), \
        "unit hours/weightage must match the syllabus"
    _check_english_only(unit)
    out = SUBJ_DIR / f"unit{unit['unit']}.json"
    out.write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    write_subject()
    return out


if __name__ == "__main__":
    write_subject()
    print("subject written:", SUBJ_DIR / "subject.json")
