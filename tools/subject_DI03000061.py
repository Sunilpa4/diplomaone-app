"""Subject metadata for DI03000061 Responsive Web Page Design (Computer Sem 3) – shared by all unit builders. English only, HTML/Bootstrap/jQuery programs with live preview."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem3", "DI03000061")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)

TABS = ["notes", "programs", "diagrams", "syntax", "viva", "exam"]
INTRO = {"en": "Detailed notes as per GTU syllabus with diagrams, solved Bootstrap and jQuery programs (tap Run to see the page live), class reference and viva."}
MAXW = 56

SUBJECT = {
    "code": "DI03000061",
    "name": {"en": "Responsive Web Page Design"},
    "branch": "computer", "semester": 3, "syllabus_year": "2024-25", "type": "practical",
    "languages": ["en"], "code_lang": "html",
    "exam": {"theory_ese": 0, "theory_pa": 0, "practical_pa": 20, "practical_ese": 30, "total": 50, "credits": 3},
    "units": [
        {"no": 1, "title": {"en": "Introduction to jQuery and Bootstrap Framework"}, "hours": 10, "weightage": 17,
         "topics": ["1.1 jQuery: introduction, importance, syntax, selectors and events",
                    "1.2 Bootstrap: why Bootstrap, history, advantages, responsive web page, removing responsiveness, major features"], "file": None},
        {"no": 2, "title": {"en": "Bootstrap Grid"}, "hours": 12, "weightage": 20,
         "topics": ["2.1 Grid system, containers, offset, reordering and nesting columns",
                    "2.2 Responsive images, typography and tables",
                    "2.3 Form layout and buttons", "2.4 Image shapes, carets, show/hide text"], "file": None},
        {"no": 3, "title": {"en": "Bootstrap Components"}, "hours": 14, "weightage": 23,
         "topics": ["3.1 Icons, dropdowns, cards, button groups and toolbar, input groups",
                    "3.2 Navs (pills, tabs), navbar, breadcrumb, pagination, badges",
                    "3.3 Jumbotron/page header, thumbnails, alerts, progress bars, media objects, list group, panels"], "file": None},
        {"no": 4, "title": {"en": "Bootstrap Plug-ins"}, "hours": 14, "weightage": 23,
         "topics": ["4.1 Plug-ins: transition, modal, scrollspy, tab, dropdown",
                    "4.2 Tooltip, popover, alert, button, collapse, carousel, affix (sticky)"], "file": None},
        {"no": 5, "title": {"en": "Advance Bootstrap Utilities and Customization"}, "hours": 10, "weightage": 17,
         "topics": ["5.1 Utilities: spacing, sizing, display, position, flex, border, background, opacity, overflow, shadow",
                    "5.2 Customization: variables, Sass, components and themes"], "file": None},
    ],
    "practicals": [
        "Install Bootstrap and study the files and tags needed for a responsive page",
        "Department and college name at the centre of a page, with and without Bootstrap",
        "Student information using container and container-fluid",
        "Offset, reordering and nesting columns", "Class time table using the grid system",
        "Co-curricular activities with responsive images and tables", "Blog page using typography",
        "Student registration form with form layout and buttons", "Dropdown menus and icons",
        "Odd/even semester menus with button groups and toolbar", "Job application form with input groups",
        "Unit summary of a course using nav tabs / pills", "Fixed-top navbar and fixed-bottom footer",
        "Education website with breadcrumb, pagination, badges, page header and thumbnails",
        "Progress bars: labels, colours, striped, animated, dynamic with JavaScript",
        "Family members using media objects", "Service providers with panels (cards), list group and alerts",
        "Page transitions with the transition plug-in", "Save / delete confirmation with modal dialogs",
        "News page with scrollspy, tooltip, collapse and popover", "Photo gallery with carousel (7 photos)",
        "Header and footer with utility classes", "Customizing Bootstrap with Sass",
        "Customized components and themes", "Responsive website of 5-7 pages on a chosen domain"],
    "books": ["Jake Spurlock – Bootstrap (O'Reilly)", "Jacob Lett – Bootstrap Reference Guide",
              "Ajdin Imsirovic – Bootstrap 4 Cookbook (Packt)", "Benjamin Jakobus – Mastering Bootstrap 4 (Packt)",
              "Silvio Moreto – Bootstrap 4 By Example (Packt)", "Thomas Powell – HTML & CSS: The Complete Reference (TMH)"],
}

def write_subject():
    for u in SUBJECT["units"]:
        fn = f'unit{u["no"]}.json'
        u["file"] = fn if os.path.exists(os.path.join(SUBJ_DIR, fn)) else None
    with open(os.path.join(SUBJ_DIR, "subject.json"), "w", encoding="utf-8") as f:
        json.dump(SUBJECT, f, ensure_ascii=False, indent=1)


def check_and_write(unit, diagram_titles, preview_name):
    """Sanity checks shared by all unit builders, then writes unitN.json, subject.json and the preview."""
    from preview_builder import build_preview
    unit.setdefault("tabs", TABS)
    unit.setdefault("intro_text", INTRO)
    notes = unit["notes"]
    items = [it for s in notes for it in s["items"]]
    used_d = {it.get("diagram") for it in items} - {None}
    used_p = {p for it in items for p in it.get("programs", [])}
    used_n = {n for it in items for n in it.get("examples", [])}
    pids = [p["id"] for p in unit["programs"]]
    nids = [n["id"] for n in unit.get("numericals", [])]
    assert len(pids) == len(set(pids)), "duplicate program id"
    assert len(nids) == len(set(nids)), "duplicate numerical id"
    assert used_d == set(diagram_titles), set(diagram_titles) ^ used_d
    assert used_p == set(pids), set(pids) ^ used_p
    assert used_n <= set(nids), used_n - set(nids)
    for k in diagram_titles:
        assert os.path.exists(os.path.join(DIAG_DIR, k + ".svg")), k
    for it in items:
        for v in it["body"].values():
            assert "@@" not in v, it["h"]["en"]
    for p in unit["programs"]:
        assert p.get("run") == "html" and p.get("out"), p["id"]
        for ln in p["code"]["en"].split("\n"):
            assert len(ln) <= MAXW or "://" in ln, f'{p["id"]}: line too long ({len(ln)}): {ln}'
    unit["programs"] = [{k: v for k, v in p.items() if not k.startswith("_")} for p in unit["programs"]]
    with open(os.path.join(SUBJ_DIR, f'unit{unit["unit"]}.json'), "w", encoding="utf-8") as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(unit, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", preview_name))
    print("topics:", len(items), "programs:", len(pids), "diagrams:", len(diagram_titles),
          "algorithms:", sum(len(g["items"]) for g in unit.get("algorithms", [])),
          "numericals:", len(nids), "viva:", sum(len(g["items"]) for g in unit["viva"]),
          "exam:", len(unit["exam_questions"]))
    print("preview:", os.path.normpath(out))
