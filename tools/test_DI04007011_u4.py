"""Local Unit 4 content/behavior checks. Requires the PHP runtime in php_content.
Run: python3 tools/test_DI04007011_u4.py
These use real PHP requests, including stale-cookie replay and CSRF rejection.
"""
import json
import os
import re
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

from php_content import PHP_BIN, PHP_ENV, run_web
from subject_DI04007011 import SUBJ_DIR, DIAG_DIR
from content_DI04007011_u4_programs import PROGRAMS, SOURCES, CSRF_PATTERN

BY_ID = {p["id"]: p for p in PROGRAMS}


def serve(pid, steps):
    files = SOURCES[pid]
    main = next(iter(files))
    return run_web(files[main], fname=main, request=steps,
                   extra={n: src for n, src in files.items() if n != main})


class FragmentParser(HTMLParser):
    allowed = {"p", "b", "strong", "i", "em", "code", "pre", "ul", "ol", "li",
               "br", "table", "tr", "th", "td", "span", "div", "h2", "h3", "h4",
               "a", "sup", "sub"}

    def handle_starttag(self, tag, attrs):
        if tag not in self.allowed:
            raise AssertionError("Unexpected raw HTML tag in educational prose: " + tag)


class Unit4Tests(unittest.TestCase):
    def test_content_structure_and_safe_html(self):
        with open(os.path.join(SUBJ_DIR, "unit4.json")) as f:
            unit = json.load(f)
        self.assertEqual((unit["unit"], unit["hours"], unit["weightage"]), (4, 10, 15))
        self.assertEqual(sum(len(g["items"]) for g in unit["notes"]), 11)
        self.assertEqual(len(unit["programs"]), 10)
        self.assertEqual(len(unit["diagrams"]), 8)
        self.assertEqual(sum(len(g["items"]) for g in unit["syntax"]), 10)
        self.assertEqual(sum(len(g["items"]) for g in unit["viva"]), 40)
        self.assertEqual(len(unit["exam_questions"]), 14)
        used_d = {i["diagram"] for g in unit["notes"] for i in g["items"] if "diagram" in i}
        used_p = {p for g in unit["notes"] for i in g["items"] for p in i.get("programs", [])}
        self.assertEqual(used_d, {d["id"] for d in unit["diagrams"]})
        self.assertEqual(used_p, set(BY_ID))
        for d in unit["diagrams"]:
            ET.parse(os.path.join(DIAG_DIR, d["id"] + ".svg"))
        def check(o):
            if isinstance(o, dict):
                self.assertNotIn("gu", o)
                for value in o.values():
                    check(value)
            elif isinstance(o, list):
                for value in o:
                    check(value)
        check(unit)
        fragments = [i["body"]["en"] for g in unit["notes"] for i in g["items"]]
        fragments += [p["expl"]["en"] for p in unit["programs"]]
        fragments += [i["a"]["en"] for g in unit["viva"] for i in g["items"]]
        for text in fragments:
            self.assertNotIn("@@", text)
            FragmentParser().feed(text)

    def test_all_shown_program_files_lint_and_have_real_outputs(self):
        for program in PROGRAMS:
            with self.subTest(program=program["id"]):
                self.assertTrue(program["out"].strip())
                for bad in ["Fatal error:", "Parse error:", "Warning:", "Deprecated:"]:
                    self.assertNotIn(bad, program["out"])
                # Lint the displayed code, not merely a hidden source version.
                shown = program["code"]["en"]
                if len(SOURCES[program["id"]]) > 1:
                    chunks = re.split(r"(?m)^<\?php // ===== File: (.+) =====\n", shown)
                    self.assertFalse(chunks[0])
                    files = {chunks[i]: "<?php\n" + chunks[i + 1].rstrip() + "\n"
                             for i in range(1, len(chunks), 2)}
                else:
                    files = {next(iter(SOURCES[program["id"]])): shown + "\n"}
                self.assertEqual(set(files), set(SOURCES[program["id"]]))
                for name, source in files.items():
                    self.assertEqual(source.strip(), SOURCES[program["id"]][name].strip())
                    with tempfile.TemporaryDirectory() as d:
                        path = os.path.join(d, name)
                        with open(path, "w") as f:
                            f.write(source)
                        result = subprocess.run([PHP_BIN, "-l", path], env=PHP_ENV,
                                                capture_output=True, text=True)
                        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_cookie_roundtrip_update_and_deletion(self):
        out = BY_ID["wd4p1"]["out"]
        self.assertIn("Set-Cookie: city=Surat;", out)
        self.assertIn("Incoming city: (missing)\nQueued for NEXT request: Surat", out)
        self.assertIn("Incoming city: Surat\nQueued for NEXT request: Vadodara", out)
        self.assertTrue(out.endswith("Incoming city: Vadodara"))
        out = BY_ID["wd4p3"]["out"]
        self.assertIn("Max-Age=0; path=/", out)
        self.assertIn("Action: clear\nIncoming demo: BusBook", out)
        self.assertTrue(out.endswith("Incoming demo: (missing)"))

    def test_theme_persistence_isolation_and_validation(self):
        out = BY_ID["wd4p2"]["out"]
        self.assertEqual(out.count("<h2>BusBook: dark theme</h2>"), 2)
        self.assertEqual(out.count("<h2>BusBook: light theme</h2>"), 2)
        tampered = serve("wd4p2", [{"headers": {"Cookie": "theme=%3Cscript%3E"}}])
        self.assertIn("<h2>BusBook: light theme</h2>", tampered)
        self.assertNotIn("<script>", tampered)
        invalid = serve("wd4p2", [{"method": "POST", "data": {"theme[]": "dark"}, "show_headers": True}])
        self.assertIn("HTTP/1.1 400", invalid)
        self.assertIn("Invalid theme.", invalid)

    def test_session_shared_pages_and_full_logout(self):
        out = BY_ID["wd4p4"]["out"]
        self.assertIn("Cart reads visits: 2\nCart reads seats: 1", out)
        self.assertTrue(out.endswith("Cart reads visits: 0\nCart reads seats: 0"))
        out = BY_ID["wd4p5"]["out"]
        self.assertIn("Action: remove-theme\nUser: Ravi\nTheme: (none)", out)
        self.assertIn("Action: clear-values\nUser: (none)\nTheme: (none)\nActive session: yes", out)
        self.assertIn("Action: destroy\nUser: (none)\nTheme: (none)\nActive session: no", out)
        self.assertTrue(out.endswith("Action: read\nUser: (none)\nTheme: (none)\nActive session: yes"))

    def test_login_main_demo_guest_success_logout_guest(self):
        out = BY_ID["wd4p6"]["out"]
        self.assertEqual(out.count("Location: login.php"), 3)
        self.assertIn("Invalid username or password.", out)
        self.assertIn("Location: dashboard.php", out)
        self.assertEqual(out.count("<p>Welcome, Ravi Patel!</p>"), 1)
        ids = re.findall(r"(?m)^Set-Cookie: PHPSESSID=([^;\n]+)", out)
        self.assertEqual(len(ids), 4)
        self.assertNotEqual(ids[0], ids[1])
        self.assertEqual(ids[2], "deleted")
        self.assertNotEqual(ids[3], ids[1])

    def test_csrf_rejection_id_rotation_and_stale_cookie_replay(self):
        out = serve("wd4p6", [
            {"show_headers": True, "capture": {"csrf": CSRF_PATTERN,
                "old_id": r"Set-Cookie: PHPSESSID=([^;\n]+)"}},
            {"method": "POST", "show_headers": True, "data": {"username": "ravi", "password": "demo@123"}},
            {"method": "POST", "data": {"username": "ravi", "password": "wrong", "csrf": "{{csrf}}"}},
            {"path": "dashboard.php", "show_headers": True},
            {"method": "POST", "show_headers": True,
                "data": {"username": "ravi", "password": "demo@123", "csrf": "{{csrf}}"},
                "capture": {"auth_id": r"Set-Cookie: PHPSESSID=([^;\n]+)"}},
            {"path": "dashboard.php", "capture": {"csrf": CSRF_PATTERN}},
            {"label": "REPLAY_OLD_ID", "path": "dashboard.php", "cookies": False,
                "headers": {"Cookie": "PHPSESSID={{old_id}}"}, "show_headers": True},
            {"path": "logout.php", "method": "POST", "show_headers": True, "data": {"csrf": "bad-token"}},
            {"path": "dashboard.php", "capture": {"csrf": CSRF_PATTERN}},
            {"path": "logout.php", "show_headers": True},
            {"path": "logout.php", "method": "POST", "data": {"csrf": "{{csrf}}"}, "show_headers": True},
            {"label": "REPLAY_DESTROYED_ID", "path": "dashboard.php", "cookies": False,
                "headers": {"Cookie": "PHPSESSID={{auth_id}}"}, "show_headers": True},
        ])
        self.assertEqual(out.count("HTTP/1.1 403"), 2)
        self.assertIn("HTTP/1.1 405", out)
        self.assertIn("Allow: POST", out)
        self.assertEqual(out.count("<p>Welcome, Ravi Patel!</p>"), 2)
        for label in ["REPLAY_OLD_ID", "REPLAY_DESTROYED_ID"]:
            segment = out.split("# " + label, 1)[1].split("\n\n$ curl", 1)[0]
            self.assertIn("Location: login.php", segment)
            self.assertNotIn("<p>Welcome,", segment)

    def test_exception_branches_and_resource_cleanup(self):
        out = BY_ID["wd4p7"]["out"]
        self.assertIn("Fare each: Rs 300", out)
        self.assertIn("Rejected: Passenger count must be positive.", out)
        self.assertEqual(out.count("this line runs only on success"), 1)
        self.assertEqual(out.count("finally: request finished"), 2)
        out = BY_ID["wd4p8"]["out"]
        for expected in ["Reserved 2 seats.", "Input: Request at least one seat.",
                         "Availability: Only 3 seats remain; wanted 5."]:
            self.assertIn(expected, out)
        self.assertEqual(out.count("Booking attempt finished."), 3)
        out = BY_ID["wd4p9"]["out"]
        self.assertEqual(out.count("finally: file closed"), 2)
        self.assertEqual(out.count("finally: no open handle"), 1)
        out = BY_ID["wd4p10"]["out"]
        for expected in ["Exception branch: RuntimeException", "Error branch: DivisionByZeroError",
                         "Error branch: TypeError", "Throwable also catches TypeError"]:
            self.assertIn(expected, out)

    def test_web_runner_unit3_backwards_compatibility(self):
        from content_DI04007011_u3_programs import PROGRAMS as OLD_PROGRAMS
        self.assertEqual(len(OLD_PROGRAMS), 11)
        self.assertIn("extras = <b>meal, insurance</b>", OLD_PROGRAMS[0]["out"])
        self.assertIn("(70 bytes, 1x1 px)", OLD_PROGRAMS[8]["out"])
        self.assertIn('Content-Disposition: attachment; filename="report.txt"', OLD_PROGRAMS[9]["out"])
        self.assertIn("subscriber recorded in subscribers.txt", OLD_PROGRAMS[10]["out"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
