"""Subject metadata for DI04007011 Introduction to Web Development (Computer Sem 4).
English-only practical subject: PHP notes, runnable programs, diagrams, syntax-cards, viva, exam."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem4", "DI04007011")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")
os.makedirs(DIAG_DIR, exist_ok=True)


def _u(no, en, h, w, topics):
    return {"no": no, "title": {"en": en}, "hours": h, "weightage": w, "topics": topics, "file": None}


SUBJECT = {
    "code": "DI04007011",
    "name": {"en": "Introduction to Web Development"},
    "branch": "computer", "semester": 4, "syllabus_year": "2025-26", "type": "programming",
    "languages": ["en"], "code_lang": "php",
    "exam": {"theory_ese": 0, "theory_pa": 0, "practical_pa": 20, "practical_ese": 30, "total": 50, "credits": 4},
    "units": [
        _u(1, "Introduction to PHP", 12, 20,
           ["1.1 Introduction to PHP: history and advantages; client-server environment and 3-tier architecture",
            "1.2 Installation and configuration of XAMPP/WAMP/LAMP server",
            "1.3 Embedding PHP in web pages: file structure and syntax; echo and print; comments",
            "1.4 Data types, variables, constants and expressions; operators",
            "1.5 Conditional structures: if, if-else, else-if, switch-case",
            "1.6 Looping structures: for, while, do-while, foreach; break and continue"]),
        _u(2, "PHP Functions, Arrays and Strings", 12, 20,
           ["2.1 User-defined functions: defining, calling, arguments, default values, by value and by reference, return",
            "2.2 Variable scope: local, global, the global keyword and $GLOBALS",
            "2.3 Built-in mathematical and date-time functions",
            "2.4 Arrays: indexed, associative and multidimensional; creating, manipulating, traversing",
            "2.5 Array library functions: count, in_array, sort, array_merge, array_reverse and more",
            "2.6 Strings: quoting styles, heredoc/nowdoc; search, replace, format; string library functions"]),
        _u(3, "Working with Data and Forms", 10, 15,
           ["3.1 HTML form controls: text box, text area, radio, checkbox, list, dropdown, upload, color, date",
            "3.2 Submitting data with GET and POST; reading $_GET, $_POST, $_REQUEST, $_FILES, $_SERVER",
            "3.3 Server-side validation: isset, empty, is_numeric, strlen, htmlspecialchars, filter_var",
            "3.4 Working with directories; reading and writing text files",
            "3.5 Uploading and downloading files; sending plain text and HTML email with attachments"]),
        _u(4, "Cookies, Sessions and Exception Handling", 10, 15,
           ["4.1 Cookies: creating, setting, accessing and destroying",
            "4.2 Sessions: creating, setting and accessing session variables, destroying a session",
            "4.3 Exception handling with try, throw, catch and finally"]),
        _u(5, "Database Connectivity using MySQLi", 16, 30,
           ["5.1 Introduction to database connectivity and MySQLi",
            "5.2 Managing databases with phpMyAdmin",
            "5.3 Connecting to a database and executing MySQLi queries",
            "5.4 Creating, altering and deleting tables; CRUD operations",
            "5.5 Preventing SQL injection with prepared statements",
            "5.6 Developing a simple MVC application with MySQLi and OOP"]),
    ],
    "practicals": [
        "Install and configure a local web server using XAMPP/WAMP/LAMP",
        "Create a web page using PHP that displays a welcome message",
        "Develop simple PHP web applications using variables, constants and operators",
        "Develop PHP web applications using control structures",
        "Develop PHP web applications using looping structures",
        "Develop PHP web applications using user-defined functions",
        "Develop PHP web applications demonstrating indexed, associative and multidimensional arrays",
        "Develop PHP web applications to process data stored in arrays",
        "Develop PHP web applications to demonstrate array functions",
        "Develop PHP web applications to demonstrate string functions",
        "Develop a PHP web application to display a user registration form and show submitted data",
        "Update the registration-form application to validate user data",
        "Develop a PHP web application to collect user feedback and store it in a text file",
        "Develop a PHP web application to upload an image file and display its thumbnail",
        "Develop a newsletter-subscription application and send a confirmation email (plain and HTML)",
        "Develop a PHP web application demonstrating sessions (protected page after login)",
        "Develop a PHP web application demonstrating cookies",
        "Develop a PHP web application demonstrating exception handling",
        "Perform database operations using phpMyAdmin (create/delete databases and tables, run SQL queries)",
        "Develop a Blog web application with create, read, update and delete (CRUD) operations",
        "Develop an MVC Contact Management application with CRUD and SQL-injection prevention",
        "Develop a To-Do List application with the help of AI code-generation tools",
        "Develop an Inventory Management application and host it on a web server",
    ],
    "books": ["Steven Holzner – PHP: The Complete Reference",
              "Lynn Beighley and Michael Morrison – Head First PHP and MySQL",
              "Robin Nixon – Learning PHP, MySQL and JavaScript with jQuery, CSS and HTML5",
              "Laura Thomson and Luke Welling – PHP and MySQL Web Development",
              "David Sklar and Adam Trachtenberg – PHP Cookbook"],
}


def write_subject():
    for u in SUBJECT["units"]:
        fn = f'unit{u["no"]}.json'
        u["file"] = fn if os.path.exists(os.path.join(SUBJ_DIR, fn)) else None
    with open(os.path.join(SUBJ_DIR, "subject.json"), "w", encoding="utf-8") as f:
        json.dump(SUBJECT, f, ensure_ascii=False, indent=1)


def en_only(o):
    """Recursively drop Gujarati ('gu') entries - this subject is English only."""
    if isinstance(o, dict):
        return {k: en_only(v) for k, v in o.items() if k != "gu"}
    if isinstance(o, list):
        return [en_only(v) for v in o]
    return o


def check_and_write(unit, diagram_titles, preview_name):
    """Sanity checks shared by all unit builders, then writes unitN.json, subject.json and the preview."""
    from preview_builder import build_preview
    unit = en_only(unit)
    for u in SUBJECT["units"]:
        u["title"] = en_only(u["title"])
    notes = unit["notes"]
    used_d = {it.get("diagram") for s in notes for it in s["items"]} - {None}
    used_p = {p for s in notes for it in s["items"] for p in it.get("programs", [])}
    pids = [p["id"] for p in unit["programs"]]
    assert len(pids) == len(set(pids)), "duplicate program id"
    assert used_d == set(diagram_titles), set(diagram_titles) ^ used_d
    assert used_p == set(pids), set(pids) ^ used_p
    for k in diagram_titles:
        assert os.path.exists(os.path.join(DIAG_DIR, k + ".svg")), k
    for s in notes:  # every @@snippet@@ must be expanded
        for it in s["items"]:
            for v in it["body"].values():
                assert "@@" not in v, it["h"]["en"]
    with open(os.path.join(SUBJ_DIR, f'unit{unit["unit"]}.json'), "w", encoding="utf-8") as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    write_subject()
    out = build_preview(unit, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", preview_name))
    print("topics:", sum(len(s["items"]) for s in notes), "programs:", len(unit["programs"]),
          "diagrams:", len(diagram_titles), "syntax:", sum(len(g["items"]) for g in unit["syntax"]),
          "viva:", sum(len(g["items"]) for g in unit["viva"]), "exam:", len(unit["exam_questions"]))
    print("preview:", os.path.normpath(out))
