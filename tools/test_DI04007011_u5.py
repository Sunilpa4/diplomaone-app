"""Real PHP/MySQLi Unit 5 regression suite; no SQL emulator.
Run after starting the private socket server and building Unit 5:
    python3 tools/test_DI04007011_u5.py
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
from mysql_content import fresh_database, admin_sql, assert_runtime
from subject_DI04007011 import SUBJ_DIR, DIAG_DIR
from content_DI04007011_u5_programs import PROGRAMS, SOURCES, SCHEMAS, ADMIN_HASH
from content_DI04007011_u5_shared import CSRF_PATTERN, CONTACT_SEED, STOCK_SCHEMA

BY_ID = {p["id"]: p for p in PROGRAMS}


def call(pid, steps, schema=None, observe="SELECT 1;", env_override=None):
    files = SOURCES[pid]
    main = next(iter(files))
    with fresh_database("test_" + pid, SCHEMAS[pid] if schema is None else schema) as env:
        if pid == "wd5p11":
            env["ADMIN_HASH"] = ADMIN_HASH
        env.update(env_override or {})
        out = run_web(files[main], fname=main, request=steps,
                      extra={n: s for n, s in files.items() if n != main}, env_extra=env)
        observed = admin_sql("USE `" + env["DB_NAME"] + "`;\n" + observe)
    return out, observed


def form():
    return {"capture": {"csrf": CSRF_PATTERN}}


def post(data, **opts):
    return {"method": "POST", "data": {**data, "csrf": "{{csrf}}"}, **opts}


def login_steps():
    return [form(), post({"action": "login", "username": "admin", "password": "inventory@123"},
                         follow_redirects=True, capture={"csrf": CSRF_PATTERN})]


class SafeFragment(HTMLParser):
    allowed = {"p", "b", "strong", "i", "em", "code", "pre", "ul", "ol", "li", "br",
               "table", "tr", "th", "td", "span", "div", "h2", "h3", "h4", "a", "sup", "sub"}

    def handle_starttag(self, tag, attrs):
        if tag not in self.allowed:
            raise AssertionError("Unexpected unescaped tag in educational prose: " + tag)


class Unit5Tests(unittest.TestCase):
    def test_01_real_runtime_and_complete_course_structure(self):
        self.assertIn("MariaDB", assert_runtime())
        with open(os.path.join(SUBJ_DIR, "unit5.json")) as f:
            u = json.load(f)
        self.assertEqual((u["unit"], u["hours"], u["weightage"]), (5, 16, 30))
        self.assertEqual(sum(len(g["items"]) for g in u["notes"]), 16)
        self.assertEqual(len(u["programs"]), 11)
        self.assertEqual(len(u["diagrams"]), 10)
        self.assertEqual(sum(len(g["items"]) for g in u["syntax"]), 14)
        self.assertEqual(sum(len(g["items"]) for g in u["viva"]), 48)
        self.assertEqual(len(u["exam_questions"]), 18)
        used_d = {i["diagram"] for g in u["notes"] for i in g["items"] if "diagram" in i}
        used_p = {p for g in u["notes"] for i in g["items"] for p in i.get("programs", [])}
        self.assertEqual(used_d, {d["id"] for d in u["diagrams"]})
        self.assertEqual(used_p, set(BY_ID))
        for d in u["diagrams"]:
            ET.parse(os.path.join(DIAG_DIR, d["id"] + ".svg"))
        with open(os.path.join(SUBJ_DIR, "subject.json")) as f:
            s = json.load(f)
        self.assertEqual(len(s["units"]), 5)
        self.assertEqual(sum(u["hours"] for u in s["units"]), 60)
        self.assertEqual(sum(u["weightage"] for u in s["units"]), 100)
        for unit in s["units"]:
            self.assertEqual(unit["file"], "unit" + str(unit["no"]) + ".json")
            self.assertTrue(os.path.isfile(os.path.join(SUBJ_DIR, unit["file"])))
        def check(o):
            if isinstance(o, dict):
                self.assertNotIn("gu", o)
                for v in o.values():
                    check(v)
            elif isinstance(o, list):
                for v in o:
                    check(v)
        check(u)
        fragments = [i["body"]["en"] for g in u["notes"] for i in g["items"]]
        fragments += [p["expl"]["en"] for p in u["programs"]]
        fragments += [i["a"]["en"] for g in u["viva"] for i in g["items"]]
        for text in fragments:
            self.assertNotIn("@@", text)
            SafeFragment().feed(text)

    def test_02_displayed_files_lint_and_match_executed_sources(self):
        def normal(s):
            return re.sub(r"^<\?php\s*", "<?php\n", s.strip())
        for p in PROGRAMS:
            with self.subTest(program=p["id"]):
                chunks = re.split(r"(?m)^<\?php\n// ===== File: (.+) =====\n", p["code"]["en"])
                self.assertFalse(chunks[0])
                files = {chunks[i]: "<?php\n" + chunks[i + 1].rstrip() + "\n"
                         for i in range(1, len(chunks), 2)}
                self.assertEqual(set(files), set(SOURCES[p["id"]]))
                for name, source in files.items():
                    self.assertEqual(normal(source), normal(SOURCES[p["id"]][name]))
                    with tempfile.TemporaryDirectory() as d:
                        path = os.path.join(d, "source.php")
                        with open(path, "w") as f:
                            f.write(source)
                        cp = subprocess.run([PHP_BIN, "-l", path], env=PHP_ENV,
                                            text=True, capture_output=True)
                        self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
                self.assertTrue(p["out"].strip())
                for bad in ["Fatal error:", "Parse error:", "Warning:", "Deprecated:",
                            "Database unavailable.", "Operation failed. Check the server log."]:
                    self.assertNotIn(bad, p["out"])

    def test_03_connection_charset_and_unicode_round_trip(self):
        out = BY_ID["wd5p1"]["out"]
        for text in ["Connection established.", "Character set: utf8mb4", "Query answer: 5", "Connection closed."]:
            self.assertIn(text, out)
        name = "Diya 🌼"
        out, stored = call("wd5p9", [form(), post({"action": "save", "id": "0", "name": name,
            "email": "diya@example.test"}, follow_redirects=True)],
            observe="SELECT HEX(name) FROM contacts;")
        self.assertIn(name, out)
        self.assertEqual(stored, name.encode().hex().upper())

    def test_04_scratch_ddl_and_result_apis(self):
        out = BY_ID["wd5p2"]["out"]
        self.assertIn("After ADD: id, title, qty", out)
        self.assertIn("After DROP COLUMN: id, title", out)
        self.assertTrue(out.endswith("Scratch databases remaining: 0"))
        out = BY_ID["wd5p3"]["out"]
        self.assertIn("Rows: 2", out)
        self.assertIn("1 | Ravi Patel | 82", out)
        self.assertIn("3 | Mihir Desai | 75", out)
        self.assertNotIn("Asha", out)

    def test_05_prepared_crud_and_duplicate_constraint(self):
        out = BY_ID["wd5p4"]["out"]
        for text in ["Inserted ID: 1; rows: 1", "Inserted ID: 2; rows: 1",
                     "Duplicate email rejected (1062).", "2 | O'Neil | 79"]:
            self.assertIn(text, out)
        out = BY_ID["wd5p5"]["out"]
        self.assertIn("Updated matching row: 1", out)
        self.assertIn("Updated missing ID: 0", out)
        self.assertIn("Deleted rows: 1", out)
        self.assertIn("1 | Ravi Patel | 95", out)
        self.assertNotIn("Asha", out)

    def test_06_injection_regression_and_legitimate_apostrophe(self):
        out = BY_ID["wd5p6"]["out"]
        self.assertIn("Unsafe concatenation rows: 3", out)
        self.assertIn("Prepared probe rows: 0", out)
        self.assertIn("Prepared apostrophe-name rows: 1", out)
        out, stored = call("wd5p9", [
            {"query": {"q": "' OR '1'='1"}},
            {"query": {"q": "O'Neil"}},
        ], schema=CONTACT_SEED, observe="SELECT COUNT(*) FROM contacts;")
        self.assertIn("<p>Contacts: 0</p>", out)
        self.assertIn("<p>Contacts: 1</p>", out)
        self.assertIn("O&#039;Neil", out)
        self.assertEqual(stored, "3")

    def test_07_commit_rollback_and_failure_after_first_write(self):
        out = BY_ID["wd5p7"]["out"]
        self.assertIn("Committed sale of 2.", out)
        self.assertIn("Rolled back: Insufficient stock.", out)
        self.assertIn("Final qty: 3\nMovement rows: 1", out)
        # Deliberately make the second write fail AFTER stock was decremented.
        schema = STOCK_SCHEMA.replace("delta INT NOT NULL,", "delta INT NOT NULL CHECK (delta > 0),")
        out, stored = call("wd5p7", {}, schema=schema,
            observe="SELECT qty,(SELECT COUNT(*) FROM movements) FROM stock WHERE id=1;")
        self.assertIn("Final qty: 5\nMovement rows: 0", out)
        self.assertNotIn("Committed sale", out)
        self.assertEqual(stored, "5\t0")

    def test_08_blog_complete_crud_and_unchanged_update(self):
        out = BY_ID["wd5p8"]["out"]
        for text in ["Post created.", "Post updated.", "Post deleted.", "Weekend Route Update", "<p>Posts: 0</p>"]:
            self.assertIn(text, out)
        out, stored = call("wd5p8", [form(),
            post({"action": "save", "id": "0", "title": "Same", "body": "Same body"},
                 follow_redirects=True, capture={"id": r'<article data-id="(\d+)"'}),
            post({"action": "save", "id": "{{id}}", "title": "Same", "body": "Same body"}, follow_redirects=True),
        ], observe="SELECT title,body,COUNT(*) FROM posts GROUP BY title,body;")
        self.assertIn("Post updated.", out)
        self.assertNotIn("Post not found.", out)
        self.assertEqual(stored, "Same\tSame body\t1")

    def test_09_stored_xss_is_escaped_not_rendered(self):
        payload = '<script>alert(1)</script>'
        out, stored = call("wd5p8", [form(), post({"action": "save", "id": "0", "title": payload,
            "body": '<img src=x onerror=alert(1)>\nO\'Neil & friends'}, follow_redirects=True)],
            observe="SELECT COUNT(*) FROM posts;")
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", out)
        self.assertIn("&lt;img src=x onerror=alert(1)&gt;", out)
        self.assertNotIn("<script>", out)
        self.assertNotIn("<img src=x", out)
        self.assertEqual(stored, "1")

    def test_10_blog_bad_input_ids_get_delete_and_csrf_do_not_mutate(self):
        schema = SCHEMAS["wd5p8"] + "INSERT INTO posts(title,body) VALUES ('Keep','Original');"
        out, stored = call("wd5p8", [form(),
            post({"action": "save", "id": "0", "title": "", "body": "x"}, show_headers=True),
            {"query": {"action": "delete", "id": "1"}},
            {"query": {"edit": "1 OR 1=1"}, "show_headers": True},
            post({"action": "save", "id": "999", "title": "Wrong", "body": "x"}, show_headers=True),
            {"method": "POST", "data": {"action": "delete", "id": "1", "csrf": "forged"}, "show_headers": True},
        ], schema=schema, observe="SELECT title,body FROM posts;")
        for status in ["422", "400", "404", "403"]:
            self.assertIn("HTTP/1.1 " + status, out)
        self.assertEqual(stored, "Keep\tOriginal")

    def test_11_mvc_layers_and_validation(self):
        out = BY_ID["wd5p9"]["out"]
        for text in ["Contact added.", "Contact updated.", "Contact deleted.", "<p>Contacts: 0</p>"]:
            self.assertIn(text, out)
        self.assertNotIn("$_POST", SOURCES["wd5p9"]["app/Contact.php"])
        self.assertNotIn("$db->", SOURCES["wd5p9"]["views/contacts.php"])
        out, stored = call("wd5p9", [form(),
            post({"action": "save", "id": "0", "name": "Ravi", "email": "not-an-email"}, show_headers=True),
            {"query": {"edit": "999"}, "show_headers": True},
        ], observe="SELECT COUNT(*) FROM contacts;")
        self.assertIn("HTTP/1.1 422", out)
        self.assertIn("HTTP/1.1 404", out)
        self.assertEqual(stored, "0")

    def test_12_todo_persistence_toggle_filter_edit_delete(self):
        out = BY_ID["wd5p10"]["out"]
        for text in ["Task added.", "Status changed.", "<b>Done</b>", "Task updated.", "Task deleted."]:
            self.assertIn(text, out)
        out, stored = call("wd5p10", [form(),
            post({"action": "save", "id": "0", "title": "Task A"}, follow_redirects=True),
            post({"action": "save", "id": "0", "title": "Task B"}, follow_redirects=True),
            post({"action": "toggle", "id": "1"}, follow_redirects=True),
            {"label": "PENDING_ONLY", "query": {"filter": "pending"}},
            {"label": "DONE_ONLY", "query": {"filter": "done"}},
            post({"action": "save", "id": "1", "title": "Task A revised"}, follow_redirects=True),
            post({"action": "delete", "id": "2"}, follow_redirects=True),
            {"query": {"filter": "all; DROP TABLE todos"}, "show_headers": True},
        ], observe="SELECT title,done FROM todos;")
        pending = out.split("# PENDING_ONLY", 1)[1].split("# DONE_ONLY", 1)[0]
        done = out.split("# DONE_ONLY", 1)[1].split("\n\n$ curl", 1)[0]
        self.assertIn("Task B", pending)
        self.assertNotIn("Task A", pending)
        self.assertIn("Task A", done)
        self.assertNotIn("Task B", done)
        self.assertIn("HTTP/1.1 400", out)
        self.assertEqual(stored, "Task A revised\t1")

    def test_13_all_project_csrf_and_unsupported_methods(self):
        for pid in ["wd5p8", "wd5p9", "wd5p10", "wd5p11"]:
            with self.subTest(program=pid):
                out, _ = call(pid, [
                    {"method": "POST", "data": {"action": "delete", "id": "1", "csrf": "forged"}, "show_headers": True},
                    {"method": "PUT", "show_headers": True},
                ])
                self.assertIn("HTTP/1.1 403", out)
                self.assertIn("HTTP/1.1 405", out)
                self.assertIn("Allow: GET, POST", out)

    def test_14_inventory_requires_configuration_and_authentication(self):
        out, stored = call("wd5p11", [{}], env_override={"ADMIN_HASH": ""},
            observe="SELECT COUNT(*) FROM products;")
        self.assertIn("Configure ADMIN_HASH", out)
        self.assertEqual(stored, "0")
        out, stored = call("wd5p11", [form(),
            post({"action": "login", "username": "admin", "password": "wrong"}, show_headers=True),
            post({"action": "save", "id": "0", "sku": "X", "name": "Hidden", "qty": "1", "price": "1.00"}, show_headers=True),
        ], observe="SELECT COUNT(*) FROM products;")
        self.assertIn("HTTP/1.1 401", out)
        self.assertNotIn("<h1>Inventory Manager</h1>", out)
        self.assertEqual(stored, "0")

    def test_15_inventory_validation_decimals_and_atomic_stock(self):
        base = {"action": "save", "id": "0", "sku": "USB001", "name": "USB Cable", "qty": "5", "price": "0.10"}
        steps = login_steps() + [post(base, follow_redirects=True)]
        for changes in [{}, {"sku": "BAD1", "qty": "-1"}, {"sku": "BAD2", "qty": "1.5"},
                        {"sku": "BAD3", "price": "0.101"}]:
            steps.append(post({**base, **changes}, show_headers=True))
        steps += [
            post({"action": "sell", "id": "1", "amount": "6"}, show_headers=True),
            post({"action": "sell", "id": "1", "amount": "1"}, follow_redirects=True),
            post({"action": "restock", "id": "1", "amount": "2"}, follow_redirects=True),
            post({"action": "sell", "id": "1", "amount": "0"}, show_headers=True),
            post({"action": "restock", "id": "1", "amount": "1000000"}, show_headers=True),
            {"query": {"edit": "1"}},
        ]
        out, stored = call("wd5p11", steps, observe="SELECT qty,price,(SELECT COUNT(*) FROM products) FROM products WHERE id=1;")
        self.assertIn("SKU already exists.", out)
        self.assertGreaterEqual(out.count("HTTP/1.1 422"), 5)
        self.assertEqual(out.count("HTTP/1.1 409"), 2)
        self.assertIn("Qty: 6 | Price: Rs 0.10", out)
        self.assertEqual(stored, "6\t0.10\t1")

    def test_16_inventory_logout_rotation_and_stale_id_replay(self):
        out, _ = call("wd5p11", [
            {"show_headers": True, "capture": {"csrf": CSRF_PATTERN,
                "guest_id": r"Set-Cookie: PHPSESSID=([^;\n]+)"}},
            post({"action": "login", "username": "admin", "password": "inventory@123"},
                 show_headers=True, capture={"auth_id": r"Set-Cookie: PHPSESSID=([^;\n]+)"}),
            {"capture": {"csrf": CSRF_PATTERN}},
            {"label": "OLD_GUEST_ID", "cookies": False, "headers": {"Cookie": "PHPSESSID={{guest_id}}"}},
            post({"action": "logout"}, show_headers=True),
            {"label": "OLD_AUTH_ID", "cookies": False, "headers": {"Cookie": "PHPSESSID={{auth_id}}"}},
        ])
        self.assertIn("<h1>Inventory Manager</h1>", out)
        for label in ["OLD_GUEST_ID", "OLD_AUTH_ID"]:
            segment = out.split("# " + label, 1)[1].split("\n\n$ curl", 1)[0]
            self.assertIn("Inventory Login", segment)
            self.assertNotIn("<h1>Inventory Manager</h1>", segment)
        self.assertIn("Max-Age=0", out)
        ids = re.findall(r"(?m)^Set-Cookie: PHPSESSID=([^;\n]+)", out)
        self.assertNotEqual(ids[0], ids[1])

    def test_17_inventory_main_crud_oversell_and_logout_evidence(self):
        out = BY_ID["wd5p11"]["out"]
        for text in ["Product added.", "Product updated.", "Qty: 2 | Price: Rs 159.50",
                     "Low stock", "HTTP/1.1 409", "Stock change rejected; quantity unchanged.",
                     "Qty: 5 | Price: Rs 159.50", "Product deleted.", "<p>Products: 0</p>"]:
            self.assertIn(text, out)
        self.assertIn("Inventory Login", out.rsplit("# 9.", 1)[1])

    def test_18_disposable_database_and_user_cleanup(self):
        self.assertEqual(admin_sql("SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE 'wd5\\_%';"), "0")
        self.assertEqual(admin_sql("SELECT COUNT(*) FROM mysql.user WHERE User LIKE 'lesson\\_%';"), "0")

    def test_19_practical_bundle_matches_displayed_sources(self):
        import zipfile
        from export_DI04007011_u5_practicals import OUTPUT, FOLDERS
        with zipfile.ZipFile(OUTPUT) as z:
            self.assertIsNone(z.testzip())
            names = z.namelist()
            self.assertEqual(len(names), 51)
            self.assertEqual(sum(n.endswith(".php") for n in names), 30)
            self.assertEqual(sum(n.endswith("/schema.sql") for n in names), 9)
            self.assertTrue(all(".." not in n.split("/") for n in names))
            for folder, p in zip(FOLDERS, PROGRAMS):
                for name, source in SOURCES[p["id"]].items():
                    path = "DI04007011_Unit5_Practicals/" + folder + "/" + name
                    actual = z.read(path).decode()
                    norm = lambda s: re.sub(r"^<\?php\s*", "<?php\n", s.strip())
                    self.assertEqual(norm(actual), norm(source))

    def test_20_documented_hash_command_preserves_password_spaces(self):
        import shlex
        from content_DI04007011_u5_notes import SN
        command = next(ln for ln in SN["inventory_hash"].splitlines() if ln.startswith("php -r "))
        args = shlex.split(command)
        args[0] = PHP_BIN
        password = " intentional spaces "
        cp = subprocess.run(args, input=password + "\n", env=PHP_ENV,
                            text=True, capture_output=True, check=True)
        code = 'echo password_verify(getenv("VERIFY_PASS"),getenv("VERIFY_HASH")) ? "OK" : "FAIL";'
        verified = subprocess.run([PHP_BIN, "-r", code],
            env={**PHP_ENV, "VERIFY_PASS": password, "VERIFY_HASH": cp.stdout.strip()},
            text=True, capture_output=True, check=True)
        self.assertEqual(verified.stdout, "OK")


if __name__ == "__main__":
    unittest.main(verbosity=2)
