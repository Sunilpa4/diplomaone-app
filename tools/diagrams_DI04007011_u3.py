"""DI04007011 Web Development - Unit 3 diagrams: forms, files, email."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def form_controls():
    b = title("Form Controls Catalog")
    b += grid(12, 44, [104, 116, 116], [
        ["control", "tag", "use"],
        ["text box", '<input type="text">', "name, city"],
        ["password", '<input type="password">', "masked typing"],
        ["text area", "<textarea>", "long feedback"],
        ["radio", 'type="radio" same name', "one of many"],
        ["checkbox", 'type="checkbox"', "many of many"],
        ["dropdown", "<select><option>", "city pick"],
        ["date / color", 'type="date" / "color"', "pickers"],
        ["file", 'type="file"', "uploads (3.4)"],
        ["submit", 'type="submit"', "fires the request"],
    ], rh=19, size=7.6)
    b += note(12, 248, 336, ["Every control needs a name= attribute - the",
                             "name becomes the key in $_GET / $_POST.",
                             "No name, no data on the server."], size=9.2)
    return svg(360, 304, b)


def get_post():
    b = title("GET vs POST")
    b += box(12, 46, 158, 120, BLUEF, BLUE, 8, 1.2)
    b += text(91, 63, "GET", 10, weight="bold", color=BLUE)
    b += code(24, 80, ["data in the URL",
                       "?city=Surat&seats=2",
                       "bookmarkable",
                       "limited (~2KB)",
                       "for SEARCHES"], size=7.6, lh=13)
    b += box(192, 46, 158, 120, GREENF, GREEN, 8, 1.2)
    b += text(271, 63, "POST", 10, weight="bold", color=GREEN)
    b += code(204, 80, ["data in the BODY",
                        "invisible in URL",
                        "no size limit",
                        "files need POST",
                        "for CHANGES"], size=7.6, lh=13)
    b += note(12, 180, 336, ["Rule of thumb: GET reads the world",
                             "(search, filter); POST changes it",
                             "(register, book, upload). Never put",
                             "passwords in a GET URL."], size=9.2)
    return svg(360, 262, b)


def superglobals():
    b = title("The Superglobals Map")
    rows = [
        ["$_GET", "URL query string data", GREENF, GREEN],
        ["$_POST", "form body data", GREENF, GREEN],
        ["$_REQUEST", "GET + POST (+cookie)", BLUEF, BLUE],
        ["$_FILES", "uploaded file records", ORANGEF, ORANGE],
        ["$_SERVER", "method, paths, headers", BLUEF, BLUE],
        ["$_ENV", "environment variables", PF, P],
        ["$GLOBALS", "every global variable", PF, P],
    ]
    y = 46
    for name, desc, f, st in rows:
        b += box(12, y, 104, 24, f, st, 6, 1.1)
        b += text(64, y + 16, name, 8.4, weight="bold", color=st, mono=True)
        b += text(126, y + 16, desc, 8.2, anchor="start")
        y += 30
    b += note(12, y + 6, 336, ["Available in every scope - no global",
                               "keyword needed. $_SESSION / $_COOKIE",
                               "join the family in Unit 4."], size=9.2)
    return svg(360, y + 66, b)


def selfprocess():
    b = title("The Self-Processing Page Pattern")
    b += terminal(180, 44, "request arrives", w=118, h=26)
    b += down(180, 57, 72)
    b += decision(180, 102, "method POST?", w=110, h=44)
    b += rbox(56, 158, 100, 30, "show the form", fill=BLUEF, stroke=BLUE, size=8.6)
    b += line("M125 102 L66 143", INK, 1.4) + arrowhead(66, 143, -125, 6, INK)
    b += text(84, 120, "no / GET", 7.4, color=BLUE)
    b += rbox(300, 158, 104, 30, "validate + process", fill=GREENF, stroke=GREEN, size=8.4)
    b += line("M235 102 L290 143", INK, 1.4) + arrowhead(290, 143, -55, 6, INK)
    b += text(270, 120, "yes", 7.4, color=GREEN)
    b += down(300, 173, 200)
    b += rbox(300, 216, 104, 28, "errors? show with data", fill=ORANGEF, stroke=ORANGE, size=8.0)
    b += down(56, 173, 240)
    b += line("M56 240 L180 240", INK, 1.4)
    b += down(300, 230, 240)
    b += line("M300 240 L180 240", INK, 1.4)
    b += terminal(180, 258, "one page.php does both", w=150, h=26)
    b += down(180, 240, 245)
    b += note(12, 282, 336, ["if ($_SERVER['REQUEST_METHOD'] === 'POST')",
                             "handle + validate; else render the form.",
                             "Actionless: form posts back to itself."], size=9.0)
    return svg(360, 336, b)


def validation():
    b = title("Validation Pipeline")
    steps = [("1 RAW", "untrusted|as typed", REDF, RED),
             ("2 CLEAN", "trim+|stripslashes", ORANGEF, ORANGE),
             ("3 CHECK", "empty / numeric|/ strlen / filter", BLUEF, BLUE),
             ("4 ESCAPE", "htmlspecial-|chars() on echo", GREENF, GREEN)]
    x = 10
    for h, s, f, st in steps:
        b += box(x, 54, 78, 66, f, st, 7, 1.2)
        b += text(x + 39, 72, h, 8.4, weight="bold", color=st)
        b += lines(x + 39, 90, s.split("|"), size=7.0, lh=12)
        x += 88
    b += rarrow(88, 98, 86, color=GREY); b += rarrow(176, 186, 86, color=GREY); b += rarrow(264, 274, 86, color=GREY)
    line4 = steps[3][1]
    b += note(12, 140, 336, ["Never trust the browser: every field gets",
                             "isset() + empty() first, then type rules.",
                             "SERVER checks even when HTML has required/",
                             "maxlength - those are only hints."], size=9.0)
    b += box(12, 210, 336, 34, PF, P, 7, 1.2)
    b += text(180, 224, "remember: validation guards input, escaping guards output", 8.2, weight="bold", color=P)
    b += text(180, 238, "two different jobs at two different ends", 7.8)
    return svg(360, 258, b)


def files_io():
    b = title("Reading and Writing Text Files")
    b += grid(12, 44, [60, 138, 138], [
        ["mode", "works", "watch out"],
        ['"r"', "read only", "file must exist"],
        ['"w"', "write, TRUNCATES", "old content lost"],
        ['"a"', "append at end", "creates if missing"],
        ['"w+"', "read + write", "truncates first!"],
    ], rh=19, size=7.8)
    b += code(16, 140, ["$h = fopen(\"feedback.txt\", \"a\");",
                        "fwrite($h, $line . \"\\n\");",
                        "fclose($h);   // always close"], size=7.8, lh=14)
    b += box(12, 196, 336, 30, GREENF, GREEN, 7, 1.2)
    b += text(180, 210, "shortcuts:  file_put_contents(file, text, FILE_APPEND)", 8.2, weight="bold", color=GREEN)
    b += text(180, 223, "file_get_contents(file)  - one-call read", 8.0)
    b += note(12, 240, 336, ["fopen/fwrite/fclose = the explicit trio;",
                             "file_* = the one-liners. Check fopen",
                             "returned false before writing."], size=9.0)
    return svg(360, 296, b)


def upload():
    b = title("File Upload Flow")
    b += box(12, 52, 104, 62, BLUEF, BLUE, 7, 1.2)
    b += text(64, 70, "1 form", 8.6, weight="bold", color=BLUE)
    b += code(22, 86, ['enctype=',
                       '"multipart/"',
                       'form-data'], size=7.4, lh=12)
    b += box(128, 52, 104, 62, ORANGEF, ORANGE, 7, 1.2)
    b += text(180, 70, "2 tmp file", 8.6, weight="bold", color=ORANGE)
    b += code(138, 86, ['$_FILES[...]',
                        "['tmp_name']",
                        "php_tmp/xyz"], size=7.4, lh=12)
    b += box(244, 52, 104, 62, GREENF, GREEN, 7, 1.2)
    b += text(296, 70, "3 moved", 8.6, weight="bold", color=GREEN)
    b += code(254, 86, ["move_uploaded",
                        "_file(...)",
                        "uploads/"], size=7.4, lh=12)
    b += rarrow(116, 128, 83, color=GREY); b += rarrow(232, 244, 83, color=GREY)
    b += note(12, 132, 336, ["$_FILES['f']: name, type, size, tmp_name,",
                             "error. Check error === UPLOAD_ERR_OK,",
                             "extension whitelist + size limit, THEN",
                             "basename() the name and move it.",
                             "tmp vanishes after the request - move",
                             "or lose it."], size=8.8)
    b += box(12, 234, 336, 30, PF, P, 7, 1.2)
    b += text(180, 248, "thumbnail: save once, show with <img width>", 8.2, weight="bold", color=P)
    b += text(180, 261, "getimagesize() confirms it really is an image", 7.8)
    return svg(360, 278, b)


def email():
    b = title("mail(): Anatomy of Sending")
    src = ["mail($to, $subject, $body, $headers);",
           "",
           "$to      = \"user@gmail.com\";",
           "$subject = \"Welcome to BusBook\";",
           "$body    = plain text  or  HTML;",
           "$headers = \"From: admin@busbook.in\\r\\n\" .",
           "           \"Content-Type: text/html\";"]
    b += code(14, 58, src, size=7.8, lh=14)
    b += grid(12, 168, [106, 108, 122], [
        ["plain text", "HTML email", "attachment"],
        ["bare body", "add header:", "MIME multipart"],
        ["default type", "text/html", "base64 chunks"],
    ], rh=18, size=7.6)
    b += note(12, 232, 336, ["XAMPP on localhost: mail() needs an SMTP",
                             "setup (or it returns false). Compose and",
                             "verify the message first; wire SMTP later."], size=9.0)
    return svg(360, 286, b)


ALL = {"wd3_form_controls": form_controls, "wd3_get_post": get_post, "wd3_superglobals": superglobals,
       "wd3_selfprocess": selfprocess, "wd3_validation": validation, "wd3_files": files_io,
       "wd3_upload": upload, "wd3_email": email}

if __name__ == "__main__":
    import subject_DI04007011 as S
    for k, fn in ALL.items():
        with open(os.path.join(S.DIAG_DIR, k + ".svg"), "w", encoding="utf-8") as f:
            f.write(fn())
    print("written", len(ALL))
