"""Unit 5: eleven programs, genuinely executed using PHP MySQLi + MariaDB.

Each program receives its own temporary database/user; web apps use genuine
forms, cookie jars and captured CSRF tokens. Never substitute SQLite or fake rows.
"""
import subprocess
from php_content import PP, PHP_BIN, PHP_ENV, reflow, code_block
from mysql_content import fresh_database, assert_runtime
from content_DI04007011_u5_shared import *
from content_DI04007011_u5_apps import *

SERVER_VERSION = assert_runtime()
SOURCES = {}
SCHEMAS = {}
REQUESTS = {}
EXPLANATIONS = {}
ADMIN_HASH = subprocess.run(
    [PHP_BIN, "-r", 'echo password_hash("inventory@123", PASSWORD_DEFAULT);'],
    env=PHP_ENV, text=True, capture_output=True, check=True
).stdout


def DPP(pid, title, code, expl="", fname="index.php", schema="", extra=None, steps=None, web=False):
    files = {fname: code, "db.php": DB_PHP}
    if web:
        files["web.php"] = WEB_PHP
    files.update(extra or {})
    files = {n: reflow(s.strip("\n")) + "\n" for n, s in files.items()}
    SOURCES[pid] = files
    SCHEMAS[pid] = schema
    REQUESTS[pid] = steps if steps is not None else {}
    if schema:
        expl += "<p><b>One-time schema/seed setup:</b> select the lesson database in phpMyAdmin and run this SQL before opening the PHP page.</p>" + code_block(schema)
    expl += "<p>Save each labelled PHP section as a separate file. db.php reads DB_HOST, DB_USER, DB_PASS and DB_NAME from the environment; its classroom defaults require the lab account described in the notes. DB_SOCKET is optional and used only by the isolated test harness. The output is actual HTTP/HTML source from PHP 8.4 with a real MariaDB server through MySQLi; the browser renders the forms. These temporary test databases are deleted afterwards.</p>"
    EXPLANATIONS[pid] = expl
    with fresh_database(pid, schema) as env:
        if pid == "wd5p11":
            env["ADMIN_HASH"] = ADMIN_HASH
        p = PP(pid, title, files[fname], expl, fname=fname,
               env_extra=env, request=REQUESTS[pid],
               extra={n: s for n, s in files.items() if n != fname})
    # Long filenames get their label on a separate PHP comment line. Do not
    # reflow labels as trailing comments or combine these into one PHP file.
    sections = []
    for name, source in files.items():
        sections.append("<?php\n// ===== File: " + name + " =====\n" + source[len("<?php"):].lstrip("\r\n").rstrip())
    p["code"]["en"] = "\n\n".join(sections)
    return p


PROGRAMS = [
    DPP("wd5p1", "Connect to a database with MySQLi and utf8mb4", r'''
<?php
require __DIR__ . "/db.php";
header("Content-Type: text/plain; charset=UTF-8");
echo "Connection established.\n";
echo "Server: ", $db->server_info, "\n";
echo "Character set: ", $db->character_set_name(), "\n";
$r = $db->query("SELECT 2 + 3 AS answer");
echo "Query answer: ", $r->fetch_assoc()["answer"], "\n";
$r->free();
$db->close();
echo "Connection closed.\n";
''',
        """<p>db.php enables strict MySQLi reporting, connects, selects the database and sets <code>utf8mb4</code>. The main page executes a constant SELECT, fetches one associative row, frees the result and closes the connection. Errors are logged server-side; the browser receives a generic configuration message rather than credentials or a stack trace. The server version in the genuine output identifies MariaDB (MySQL-compatible); MySQLi is PHP's client API, not the server's name.</p>""",
        fname="connect.php"),

    DPP("wd5p2", "Database and table lifecycle: phpMyAdmin SQL lab (Practical 19)", r'''
<?php
require __DIR__ . "/db.php";
header("Content-Type: text/plain; charset=UTF-8");
// Disposable database, never a real application's database.
$scratch = $name . "_scratch";
if (!preg_match('/^[A-Za-z0-9_]+$/', $scratch)) {
    exit("Invalid database identifier.");
}
$db->query("CREATE DATABASE `$scratch` CHARACTER SET utf8mb4");
echo "Created scratch database.\n";
$db->query("CREATE TABLE `$scratch`.books ("
    . "id INT PRIMARY KEY, title VARCHAR(80) NOT NULL)");
echo "Created books table.\n";
$db->query("ALTER TABLE `$scratch`.books ADD qty INT NOT NULL DEFAULT 0");
$r = $db->query("SHOW COLUMNS FROM `$scratch`.books");
echo "After ADD: ", implode(", ", array_column($r->fetch_all(MYSQLI_ASSOC), "Field")), "\n";
$db->query("ALTER TABLE `$scratch`.books DROP COLUMN qty");
$r = $db->query("SHOW COLUMNS FROM `$scratch`.books");
echo "After DROP COLUMN: ", implode(", ", array_column($r->fetch_all(MYSQLI_ASSOC), "Field")), "\n";
$db->query("DROP TABLE `$scratch`.books");
echo "Dropped books table.\n";
$db->query("DROP DATABASE `$scratch`");
$s = $db->prepare("SELECT COUNT(*) AS n FROM information_schema.SCHEMATA WHERE SCHEMA_NAME=?");
$s->bind_param("s", $scratch);
$s->execute();
echo "Scratch databases remaining: ", $s->get_result()->fetch_assoc()["n"], "\n";
''',
        """<p>This executes the same CREATE/ALTER/DROP SQL used in phpMyAdmin's SQL tab. It verifies column lists before/after alteration and queries metadata after deletion. It does <b>not</b> claim to automate or screenshot phpMyAdmin's GUI. CREATE/DROP DATABASE requires suitable administrative privileges; the test account is granted rights only to its disposable lesson schemas. Identifiers cannot be bound with <code>?</code>: this generated database name is validated before quoting.</p>""",
        fname="schema_lab.php"),

    DPP("wd5p3", "Procedural MySQLi: SELECT, num_rows and fetch_assoc", r'''
<?php
require __DIR__ . "/db.php";
header("Content-Type: text/plain; charset=UTF-8");
// Constant query: no untrusted value is concatenated.
$sql = "SELECT id,name,marks FROM students WHERE city='Surat' ORDER BY id";
$result = mysqli_query($db, $sql);
echo "Rows: ", mysqli_num_rows($result), "\n";
while ($row = mysqli_fetch_assoc($result)) {
    echo $row["id"], " | ", $row["name"], " | ", $row["marks"], "\n";
}
mysqli_free_result($result);
mysqli_close($db);
''',
        """<p>The procedural functions operate on the same mysqli connection object used by the object-oriented API. SELECT returns a result set; <code>mysqli_num_rows</code> counts it and <code>mysqli_fetch_assoc</code> advances one row at a time. Never echo an unescaped database value into HTML; this demonstration deliberately sends <code>text/plain</code>. In a template use htmlspecialchars, because stored data can also contain unsafe markup.</p>""",
        fname="read_students.php", schema=STUDENTS_SEED),

    DPP("wd5p4", "Prepared INSERT, bind_param and insert_id", r'''
<?php
require __DIR__ . "/db.php";
header("Content-Type: text/plain; charset=UTF-8");
$s = $db->prepare("INSERT INTO students(name,email,city,marks) VALUES (?,?,?,?)");
$studentName = "Diya Shah";
$email = "diya@example.test";
$city = "Surat";
$marks = 88;
$s->bind_param("sssi", $studentName, $email, $city, $marks);
$s->execute();
echo "Inserted ID: ", $db->insert_id, "; rows: ", $s->affected_rows, "\n";
// Same prepared statement, new variable values.
$studentName = "O'Neil";
$email = "oneil@example.test";
$marks = 79;
$s->execute();
echo "Inserted ID: ", $db->insert_id, "; rows: ", $s->affected_rows, "\n";
try {
    $s->execute();
} catch (mysqli_sql_exception $e) {
    if ($e->getCode() !== 1062) {
        throw $e;
    }
    echo "Duplicate email rejected (1062).\n";
}
$s->close();
$r = $db->query("SELECT id,name,marks FROM students ORDER BY id");
foreach ($r->fetch_all(MYSQLI_ASSOC) as $row) {
    echo $row["id"], " | ", $row["name"], " | ", $row["marks"], "\n";
}
''',
        """<p>The four placeholders have four bound variables and a four-letter type string: <code>sssi</code> = string, string, string, integer. Bound variables are references: changing their values then calling execute reuses the prepared statement. Apostrophes in O'Neil stay data. The UNIQUE email constraint rejects the intentional duplicate; only error 1062 is handled as that known case. Other database errors are not silently swallowed.</p>""",
        fname="insert_students.php", schema=STUDENTS_SCHEMA),

    DPP("wd5p5", "Prepared UPDATE/DELETE with WHERE and affected_rows", r'''
<?php
require __DIR__ . "/db.php";
header("Content-Type: text/plain; charset=UTF-8");
$s = $db->prepare("UPDATE students SET marks=? WHERE id=?");
$marks = 95;
$id = 1;
$s->bind_param("ii", $marks, $id);
$s->execute();
echo "Updated matching row: ", $s->affected_rows, "\n";
$id = 999;
$s->execute();
echo "Updated missing ID: ", $s->affected_rows, "\n";
$s->close();
$s = $db->prepare("DELETE FROM students WHERE id=?");
$id = 2;
$s->bind_param("i", $id);
$s->execute();
echo "Deleted rows: ", $s->affected_rows, "\n";
$s->close();
$r = $db->query("SELECT id,name,marks FROM students ORDER BY id");
foreach ($r->fetch_all(MYSQLI_ASSOC) as $row) {
    echo $row["id"], " | ", $row["name"], " | ", $row["marks"], "\n";
}
''',
        """<p>The WHERE clause targets one primary key. Omit it and UPDATE/DELETE can affect the whole table. affected_rows reports the last write, not a SELECT count; for UPDATE a zero can mean missing ID <b>or an unchanged value</b> with the default client flags. The full apps check existence separately when that distinction matters. HTTP deletion belongs in a validated, CSRF-protected POST, not an edit-style GET link.</p>""",
        fname="update_delete.php", schema=STUDENTS_SEED),

    DPP("wd5p6", "SQL-injection regression: unsafe lab query vs prepared lookup", r'''
<?php
require __DIR__ . "/db.php";
header("Content-Type: text/plain; charset=UTF-8");
$probe = "missing' OR '1'='1";
// ISOLATED READ-ONLY LAB ANTI-EXAMPLE. Never use in an app.
$unsafe = "SELECT id FROM contacts WHERE name='$probe'";
echo "Unsafe concatenation rows: ", $db->query($unsafe)->num_rows, "\n";
$s = $db->prepare("SELECT id FROM contacts WHERE name=?");
$s->bind_param("s", $probe);
$s->execute();
echo "Prepared probe rows: ", $s->get_result()->num_rows, "\n";
$probe = "O'Neil";
$s->execute();
echo "Prepared apostrophe-name rows: ", $s->get_result()->num_rows, "\n";
$s->close();
''',
        """<p>A deliberately unsafe, read-only query is run <b>only against this isolated test database</b> to make the failure visible: the injected OR condition returns every row. The parameterised lookup treats the same string as one literal name and returns zero; a legitimate apostrophe-containing name returns one. None of the web apps use this unsafe concatenation. Prepared statements protect value positions, not arbitrary column names or SQL fragments; allowlist those separately.</p>""",
        fname="injection_lab.php", schema=CONTACT_SEED),

    DPP("wd5p7", "Transaction: atomic stock change with commit and rollback", r'''
<?php
require __DIR__ . "/db.php";
header("Content-Type: text/plain; charset=UTF-8");
function sell(mysqli $db, int $wanted): void {
    if ($wanted <= 0) {
        throw new InvalidArgumentException("Quantity must be positive.");
    }
    $db->begin_transaction();
    try {
        $id = 1;
        $s = $db->prepare("UPDATE stock SET qty=qty-? WHERE id=? AND qty>=?");
        $s->bind_param("iii", $wanted, $id, $wanted);
        $s->execute();
        if ($s->affected_rows !== 1) {
            throw new RuntimeException("Insufficient stock.");
        }
        $s->close();
        $delta = -$wanted;
        $s = $db->prepare("INSERT INTO movements(stock_id,delta) VALUES (?,?)");
        $s->bind_param("ii", $id, $delta);
        $s->execute();
        $s->close();
        $db->commit();
        echo "Committed sale of $wanted.\n";
    } catch (RuntimeException $e) {
        $db->rollback();
        echo "Rolled back: ", $e->getMessage(), "\n";
    } catch (Throwable $e) {
        $db->rollback();
        throw $e;
    }
}
sell($db, 2);
sell($db, 9);
echo "Final qty: ", $db->query("SELECT qty FROM stock WHERE id=1")->fetch_assoc()["qty"], "\n";
echo "Movement rows: ", $db->query("SELECT COUNT(*) AS n FROM movements")->fetch_assoc()["n"], "\n";
''',
        """<p>InnoDB groups the stock decrement and audit insert into one unit. A conditional UPDATE prevents selling more than the available quantity; commit keeps both writes, rollback prevents a partial operation. The first sale (2 of 5) succeeds; the second (9 of 3) fails, leaving quantity 3 and one movement. The function rejects non-positive quantities before beginning; real request handlers must also validate submitted integer shape/range. DDL such as CREATE/ALTER often causes implicit commits and is not part of this transaction.</p>""",
        fname="stock_transaction.php", schema=STOCK_SCHEMA),

    DPP("wd5p8", "Complete Blog CRUD with forms and prepared SQL (Practical 20)", BLOG,
        """<p>End-to-end create, list/search, edit and delete. Server-side rules validate title/body; every value-bearing SQL statement is prepared; output is escaped (including stored text), mutations require POST + CSRF, and successful writes redirect with 303. Invalid or missing IDs are rejected instead of becoming broad updates/deletes. This is a local single-editor lab: add the Unit 4 authentication/authorisation guard before exposing it publicly.</p>""",
        schema=BLOG_SCHEMA, web=True, steps=[
            {"label": "1. Open the empty blog form", "capture": {"csrf": CSRF_PATTERN}},
            {"label": "2. Create a post and follow Post/Redirect/Get", "method": "POST", "data": {"action": "save", "id": "0", "title": "BusBook Begins", "body": "Our first Surat route is live.", "csrf": "{{csrf}}"}, "follow_redirects": True, "capture": {"id": r'<article data-id="(\d+)"', "csrf": CSRF_PATTERN}},
            {"label": "3. Load the edit form", "query": {"edit": "{{id}}"}},
            {"label": "4. Update that primary key", "method": "POST", "data": {"action": "save", "id": "{{id}}", "title": "Weekend Route Update", "body": "Extra buses on Saturday.", "csrf": "{{csrf}}"}, "follow_redirects": True},
            {"label": "5. Search uses a bound LIKE value", "query": {"q": "Weekend"}},
            {"label": "6. Delete with POST; listing becomes empty", "method": "POST", "data": {"action": "delete", "id": "{{id}}", "csrf": "{{csrf}}"}, "follow_redirects": True},
        ]),

    DPP("wd5p9", "OOP MVC Contacts: add/search/update/delete safely (Practical 21)", CONTACT_INDEX,
        """<p>A genuine small MVC app: index.php dispatches; ContactController handles HTTP/validation/redirects; Contact owns all database operations; views/contacts.php renders escaped data. Dependencies are supplied through constructors. Search, insert, update and delete all bind values. The transcript searches for O'Neil successfully and an injection-shaped value returns zero rows. Like the blog, this local admin lab needs a login/authorisation guard before public deployment.</p>""",
        schema=CONTACT_SCHEMA, web=True,
        extra={"app/Contact.php": CONTACT_MODEL, "app/ContactController.php": CONTACT_CONTROLLER, "views/contacts.php": CONTACT_VIEW},
        steps=[
            {"label": "1. Open the empty MVC contact form", "capture": {"csrf": CSRF_PATTERN}},
            {"label": "2. Add an apostrophe-containing name", "method": "POST", "data": {"action": "save", "id": "0", "name": "O'Neil", "email": "oneil@example.test", "csrf": "{{csrf}}"}, "follow_redirects": True, "capture": {"id": r'<article data-id="(\d+)"'}},
            {"label": "3. Search for that exact name fragment", "query": {"q": "O'Neil"}},
            {"label": "4. Injection-shaped search remains literal data", "query": {"q": "' OR '1'='1"}},
            {"label": "5. Edit the contact", "method": "POST", "data": {"action": "save", "id": "{{id}}", "name": "O'Neil Shah", "email": "oneil.shah@example.test", "csrf": "{{csrf}}"}, "follow_redirects": True},
            {"label": "6. Delete one contact with a primary-key predicate", "method": "POST", "data": {"action": "delete", "id": "{{id}}", "csrf": "{{csrf}}"}, "follow_redirects": True},
        ]),

    DPP("wd5p10", "AI-assisted To-Do reference: add/edit/toggle/filter/delete (Practical 22)", TODO,
        """<p>Complete PHP/MySQLi To-Do application generated for this lesson and executed against the real database. It is a reference for the AI-assisted practical, not a claim that a separate external AI service was used. Students should record their prompt, review and explain the returned code, make corrections, and run the test matrix in the notes. The filter maps an allowlisted key to trusted SQL, while record values are bound. Blank titles, forged CSRF, invalid IDs and arbitrary filter clauses are rejected. This is a local single-user lab; add access control before hosting it publicly.</p>""",
        schema=TODO_SCHEMA, web=True, steps=[
            {"label": "1. Open the empty task form", "capture": {"csrf": CSRF_PATTERN}},
            {"label": "2. Add a study task", "method": "POST", "data": {"action": "save", "id": "0", "title": "Revise MySQLi", "csrf": "{{csrf}}"}, "follow_redirects": True, "capture": {"id": r'<article data-id="(\d+)"'}},
            {"label": "3. Mark it done", "method": "POST", "data": {"action": "toggle", "id": "{{id}}", "csrf": "{{csrf}}"}, "follow_redirects": True},
            {"label": "4. Read only done tasks", "query": {"filter": "done"}},
            {"label": "5. Edit the task title", "method": "POST", "data": {"action": "save", "id": "{{id}}", "title": "Practise prepared statements", "csrf": "{{csrf}}"}, "follow_redirects": True},
            {"label": "6. Delete the completed task", "method": "POST", "data": {"action": "delete", "id": "{{id}}", "csrf": "{{csrf}}"}, "follow_redirects": True},
        ]),

    DPP("wd5p11", "Authenticated Inventory CRUD and stock checks (Practical 23)", INVENTORY,
        """<p>Inventory Manager supports product CRUD, unique SKU, integer quantities, DECIMAL prices, low-stock alerts, atomic sell/restock and authenticated access. auth.php requires an <code>ADMIN_HASH</code> environment value generated with password_hash; it has no built-in default password. The test supplies a temporary lab hash and uses <code>admin / inventory@123</code> only for this local demonstration. Set your own unique password/hash before running or hosting it.</p><p>All mutations require a CSRF-protected POST; after login the session ID/token rotate, and logout clears both server state and cookie. Selling 99 when only 2 remain returns 409 and leaves stock unchanged. Prices are bound as validated decimal strings, not binary floating-point arithmetic. The local HTTP test is real, but this application has <b>not</b> been deployed to an external host; the notes provide the separate HTTPS/credentials/import/backup/smoke-test hosting checklist.</p>""",
        schema=INVENTORY_SCHEMA, web=True, extra={"auth.php": INVENTORY_AUTH}, steps=[
            {"label": "1. Anonymous request receives login, not inventory", "capture": {"csrf": CSRF_PATTERN}},
            {"label": "2. Authenticate; redirected form has a new CSRF token", "method": "POST", "data": {"action": "login", "username": "admin", "password": "inventory@123", "csrf": "{{csrf}}"}, "follow_redirects": True, "capture": {"csrf": CSRF_PATTERN}},
            {"label": "3. Add a product", "method": "POST", "data": {"action": "save", "id": "0", "sku": "USB001", "name": "USB Cable", "qty": "5", "price": "149.50", "csrf": "{{csrf}}"}, "follow_redirects": True, "capture": {"id": r'<article data-id="(\d+)"'}},
            {"label": "4. Update quantity and price", "method": "POST", "data": {"action": "save", "id": "{{id}}", "sku": "USB001", "name": "USB Cable", "qty": "8", "price": "159.50", "csrf": "{{csrf}}"}, "follow_redirects": True},
            {"label": "5. Sell six; quantity 2 triggers low-stock alert", "method": "POST", "data": {"action": "sell", "id": "{{id}}", "amount": "6", "csrf": "{{csrf}}"}, "follow_redirects": True},
            {"label": "6. Oversell is rejected without changing stock", "method": "POST", "data": {"action": "sell", "id": "{{id}}", "amount": "99", "csrf": "{{csrf}}"}, "show_headers": True},
            {"label": "7. Restock three; quantity becomes 5", "method": "POST", "data": {"action": "restock", "id": "{{id}}", "amount": "3", "csrf": "{{csrf}}"}, "follow_redirects": True},
            {"label": "8. Delete the product", "method": "POST", "data": {"action": "delete", "id": "{{id}}", "csrf": "{{csrf}}"}, "follow_redirects": True},
            {"label": "9. Logout restores the login gate", "method": "POST", "data": {"action": "logout", "csrf": "{{csrf}}"}, "follow_redirects": True},
        ]),
]
