"""DI04007011 Unit 5: Database Connectivity using MySQLi (16 h, 30%). English only."""
from php_content import make_TP
from content_DI04007011_u5_shared import STUDENTS_SCHEMA, BLOG_SCHEMA, CONTACT_SCHEMA, TODO_SCHEMA, INVENTORY_SCHEMA

SN = {
    "admin_setup": '''-- Run once using an ADMIN account in phpMyAdmin.
CREATE DATABASE busbook
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'busbook_app'@'localhost'
  IDENTIFIED BY 'change-this-lab-password';
GRANT SELECT, INSERT, UPDATE, DELETE
  ON busbook.* TO 'busbook_app'@'localhost';
-- This sample password is for a LOCAL lab only.
-- Production: unique secrets, not committed files.
''',
    "connect": r'''
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$db = new mysqli(
    "localhost", "busbook_app",
    getenv("DB_PASS"), "busbook"
);
$db->set_charset("utf8mb4");
// Check configuration and catch failures safely.
''',
    "sql_lab": '''-- Disposable schema: never use a real project's name.
CREATE DATABASE busbook_scratch CHARACTER SET utf8mb4;
USE busbook_scratch;
CREATE TABLE books (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(80) NOT NULL
);
ALTER TABLE books ADD qty INT NOT NULL DEFAULT 0;
INSERT INTO books(title,qty) VALUES ('PHP Guide',3);
SELECT id,title,qty FROM books;
UPDATE books SET qty=4 WHERE id=1;
DELETE FROM books WHERE id=1;
ALTER TABLE books DROP COLUMN qty;
DROP TABLE books;
DROP DATABASE busbook_scratch;
''',
    "student_schema": STUDENTS_SCHEMA,
    "fetch": r'''
<?php
$r = $db->query("SELECT id,name FROM students ORDER BY id");
echo $r->num_rows;
while ($row = $r->fetch_assoc()) {
    echo htmlspecialchars($row["name"]);
}
$r->free();
''',
    "prepared": r'''
<?php
$s = $db->prepare(
    "INSERT INTO students(name,email,city,marks) VALUES (?,?,?,?)"
);
$name = "Diya";
$email = "diya@example.test";
$city = "Surat";
$marks = 88;
$s->bind_param("sssi", $name, $email, $city, $marks);
$s->execute();
echo $db->insert_id;
$s->close();
''',
    "safe_lookup": r'''
<?php
$s = $db->prepare("SELECT id,name FROM contacts WHERE name=?");
$name = $_GET["name"] ?? "";
if (!is_string($name)) {
    http_response_code(400);
    exit("Invalid name.");
}
$s->bind_param("s", $name);
$s->execute();
$rows = $s->get_result()->fetch_all(MYSQLI_ASSOC);
''',
    "blog_schema": BLOG_SCHEMA,
    "contact_schema": CONTACT_SCHEMA,
    "todo_schema": TODO_SCHEMA,
    "inventory_schema": INVENTORY_SCHEMA,
    "mvc_tree": '''index.php                 front controller / wiring
db.php                    connection and charset
web.php                   CSRF, validation, HTML helpers
app/Contact.php           MODEL: prepared SQL only
app/ContactController.php CONTROLLER: request handling
views/contacts.php        VIEW: escaped HTML only
schema.sql                one-time admin import
''',
    "ai_prompt": '''Build a small PHP 8/MySQLi To-Do app.
Requirements: add, list, edit, toggle done, delete,
and filter all/pending/done. Use a todos table.
Use prepared values, strict ID validation, server-side
validation, escaped HTML, POST + CSRF for writes,
and Post/Redirect/Get. Separate connection secrets.
Provide schema.sql and a test matrix. Do not use
production credentials or claim unrun tests passed.
''',
    "inventory_hash": '''# Choose your OWN password; do not reuse the test password.
# Run PHP locally and type your chosen password + Enter.
# Copy the hash to private ADMIN_HASH configuration,
# never to a public page:
php -r 'echo password_hash(rtrim(fgets(STDIN), "\\r\\n"), PASSWORD_DEFAULT), PHP_EOL;'
# DB_HOST, DB_NAME, DB_USER, DB_PASS and ADMIN_HASH are
# server-side configuration. Plain PHP does not automatically
# read a .env file; configure the server/hosting environment.
''',
}
T = make_TP(SN)

SEC_5_1 = {
    "title": {"en": "5.1 Database Connectivity and MySQLi"},
    "items": [
        T("What Database Connectivity Does", """
<p>A dynamic application needs durable, structured data shared by different requests and users. PHP connects to a database server, sends SQL, reads rows/results, and renders an HTML response. A text file can store feedback, but a relational database adds keys, constraints, efficient queries and controlled concurrent updates.</p>
<ul><li><b>MySQL</b> is a database server; <b>MariaDB</b> is a MySQL-compatible server used by these real executions. <b>MySQLi</b> (MySQL Improved) is PHP's client extension/API; it is not another database server.</li>
<li><b>phpMyAdmin</b> is a PHP web administration interface for managing databases. It is neither MySQL itself nor the connection library used by your own application.</li>
<li>The request path is browser &rarr; PHP validation/application logic &rarr; MySQLi &rarr; database &rarr; result handling &rarr; HTML response. Do not connect browser JavaScript directly to the database with a privileged password.</li>
<li>Credentials, SQL and data rules belong on the server. A successful form submission must actually write to the database; a success message alone is not evidence.</li>
<li>All Unit 5 program outputs come from PHP 8.4 using mysqlnd/MySQLi and an actual MariaDB server. Each test uses a fresh private database/user; no SQLite emulation or manually invented result rows are used.</li></ul>
""", diagram="wd5_stack"),
        T("Connecting, Character Sets and the Two MySQLi Styles", """
<table><tr><th>Operation</th><th>Object-oriented</th><th>Procedural equivalent</th></tr>
<tr><td>Connect</td><td>new mysqli(...)</td><td>mysqli_connect(...)</td></tr>
<tr><td>Set charset</td><td>$db-&gt;set_charset('utf8mb4')</td><td>mysqli_set_charset($db, 'utf8mb4')</td></tr>
<tr><td>Query</td><td>$db-&gt;query($sql)</td><td>mysqli_query($db, $sql)</td></tr>
<tr><td>Fetch</td><td>$result-&gt;fetch_assoc()</td><td>mysqli_fetch_assoc($result)</td></tr>
<tr><td>Close</td><td>$db-&gt;close()</td><td>mysqli_close($db)</td></tr></table>
@@connect@@
<ul><li>Connection arguments identify host, account, password and database; optional port/socket parameters support other local/server configurations. <code>localhost</code> may use a Unix socket; <code>127.0.0.1</code> normally selects TCP.</li>
<li>Explicit <code>mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT)</code> gives consistent exception-based error handling. Modern PHP commonly enables strict reporting by default, but reference code should make its expectation clear.</li>
<li><code>set_charset('utf8mb4')</code> configures the connection for full Unicode; also create the database/tables with an appropriate charset. A browser's UTF-8 meta tag alone does not configure a database connection.</li>
<li>The complete db.php reads environment settings and handles connection failures safely. For local setup, create the database/account as admin, import each schema as admin, then run the app with the less-privileged account.</li>
<li>Classroom fallback credentials are deliberately labelled local-only. For production, choose unique secrets in private server configuration; never publish root credentials, connection dumps or a password-bearing config download.</li></ul>
@@admin_setup@@
""", diagram="wd5_connection", programs=["wd5p1"]),
    ],
}

SEC_5_2 = {
    "title": {"en": "5.2 phpMyAdmin and Database Structure (Practical 19)"},
    "items": [
        T("phpMyAdmin: Create, Inspect, Run SQL, Export and Delete", """
<ol><li>Start the local web/PHP and database services in XAMPP/WAMP/LAMP. Open <code>http://localhost/phpmyadmin</code> where that stack provides it; authenticate with the appropriate local admin account.</li>
<li>Use <b>New / Databases</b> to create a disposable schema with utf8mb4. Select the database in the navigation tree before creating its tables.</li>
<li><b>Structure</b> shows columns, types, indexes and constraints. <b>Browse</b> shows stored rows. <b>SQL</b> executes entered SQL and displays result/error feedback; menu details vary by version.</li>
<li><b>Import</b> loads a schema/data SQL file; <b>Export</b> creates a backup. Export before destructive work, and verify you can restore it.</li>
<li>DROP only the intended scratch database/table. Confirm its name before accepting a destructive action. The SQL lab below intentionally deletes its own disposable schema.</li></ol>
@@sql_lab@@
<ul><li>The matching PHP program executes these kinds of SQL statements and checks metadata after ALTER/DROP; it does not pretend that the phpMyAdmin GUI itself was automated.</li>
<li>CREATE/DROP DATABASE and schema alteration require suitable privileges. An ordinary runtime account with only SELECT/INSERT/UPDATE/DELETE should not administer schemas.</li>
<li>To run the PHP scratch lab with the default account, an admin may grant <code>CREATE, ALTER, DROP, SELECT ON busbook_scratch.*</code> to that local lab account; remove administrative privileges when no longer needed.</li>
<li>Never expose an unprotected phpMyAdmin/root account on the public internet. Use the host's controlled admin access, strong credentials and suitable access restrictions.</li></ul>
""", diagram="wd5_phpmyadmin", programs=["wd5p2"]),
        T("Designing Tables: Types, Keys, Constraints and DDL", """
@@student_schema@@
<ul><li><b>INT</b> stores whole numbers; <b>VARCHAR(n)</b> stores bounded text; <b>TEXT</b> stores longer post bodies; <b>DECIMAL(10,2)</b> stores exact fixed-point prices; <b>TIMESTAMP</b> can record creation time. Do not use binary FLOAT for exact money calculations.</li>
<li>A <b>PRIMARY KEY</b> uniquely identifies each row and cannot be null. <b>AUTO_INCREMENT</b> generates a new numeric ID; IDs are identifiers, not guaranteed gap-free row counts.</li>
<li><b>NOT NULL</b>, <b>UNIQUE</b> and <b>CHECK</b> enforce server-side rules. Test the target server version's support; these lesson constraints are actually executed on the test server.</li>
<li>A <b>FOREIGN KEY</b> links related rows, e.g. movements.stock_id to stock.id. Decide deletion/update behaviour deliberately rather than silently orphaning dependent rows.</li>
<li><b>CREATE TABLE</b> defines structure; <b>ALTER TABLE</b> adds/changes/removes columns or keys; <b>DROP TABLE</b> removes structure and rows. <b>DELETE FROM ... WHERE ...</b> removes selected data, not the table.</li>
<li>Constraints complement validation: validate for clear user feedback, then let database rules protect consistency when requests race or another client writes data.</li></ul>
""", diagram="wd5_table_design"),
    ],
}

SEC_5_3 = {
    "title": {"en": "5.3 Queries, Prepared Statements and CRUD"},
    "items": [
        T("Executing SELECT and Processing Result Sets", """
@@fetch@@
<ul><li><code>query()</code> with a successful SELECT returns a <code>mysqli_result</code>. A successful INSERT/UPDATE/DELETE through query returns true rather than a row set. With strict reporting, failures throw mysqli_sql_exception.</li>
<li><code>num_rows</code> counts rows in a buffered result. <code>fetch_assoc()</code> returns the next row keyed by column names; null marks exhaustion. <code>fetch_all(MYSQLI_ASSOC)</code> reads all remaining rows as an array.</li>
<li>Use explicit columns and stable <code>ORDER BY</code> when order matters. Do not assume rows arrive in insertion order just because a small test happened to do so.</li>
<li><code>free()</code> releases the result; close statements/connections when their work is finished. PHP also cleans up request-bound resources, but explicit lifecycle knowledge matters for long-running work.</li>
<li>The procedural program selects two Surat students from a genuine seeded table. Hard-coded constant SQL is safe from value interpolation; any submitted search/filter value should instead be bound.</li>
<li>Values stored in a database are not automatically safe HTML. Escape output even if the original source was a trusted-looking form.</li></ul>
""", programs=["wd5p3"]),
        T("prepare, bind_param, execute and Fetching Prepared Results", """
@@prepared@@
<ol><li><b>Prepare</b> the SQL template with unquoted <code>?</code> placeholders in value positions.</li>
<li><b>Bind</b> variables in placeholder order. Type letters are <code>i</code> integer, <code>d</code> double, <code>s</code> string and <code>b</code> blob. Count and order must match.</li>
<li><b>Execute</b> using the current bound variable values. bind_param binds by reference; use variables, not temporary literal expressions.</li>
<li><b>Inspect:</b> INSERT can supply <code>$db-&gt;insert_id</code>; writes expose <code>$stmt-&gt;affected_rows</code>; SELECT can use <code>get_result()</code> then fetch rows.</li>
<li><b>Reuse/close:</b> assign new variable values and execute again if appropriate; close the statement after its work.</li></ol>
<ul><li><code>get_result()</code> requires mysqlnd support. Where unavailable, use <code>bind_result($id, $name)</code> followed by <code>fetch()</code> instead. The supplied runtime includes mysqlnd.</li>
<li>The INSERT program actually stores Diya and O'Neil, then demonstrates the UNIQUE email constraint rejecting a duplicate. The successful row count remains two; a rejected insert may still consume an auto-increment value.</li>
<li>For exact money, validate a decimal string and store it in DECIMAL; the inventory program binds that decimal string as <code>s</code>, avoiding application-side binary floating-point arithmetic.</li></ul>
""", diagram="wd5_prepared", programs=["wd5p4"]),
        T("CRUD: Create, Read, Update and Delete Safely", """
<table><tr><th>CRUD</th><th>SQL pattern</th><th>Typical form behaviour</th></tr>
<tr><td>Create</td><td>INSERT INTO posts(title,body) VALUES (?,?)</td><td>Validated POST, obtain new ID, redirect</td></tr>
<tr><td>Read</td><td>SELECT ... WHERE id=?</td><td>GET listing/detail/search; fetch results</td></tr>
<tr><td>Update</td><td>UPDATE posts SET title=? WHERE id=?</td><td>Load edit form by GET; save by POST</td></tr>
<tr><td>Delete</td><td>DELETE FROM posts WHERE id=?</td><td>Explicit CSRF-protected POST; never a deleting GET link</td></tr></table>
<ul><li>Validate record IDs as positive integers and check existence where needed. Casting arbitrary input to int is not a substitute for meaningful validation.</li>
<li><b>WHERE is critical:</b> without it, UPDATE/DELETE may alter every row. A prepared statement without the intended WHERE is still logically dangerous.</li>
<li><code>affected_rows</code> is evidence of the last write, not a SELECT count. With default client flags, UPDATE can return zero both for a missing row and for an unchanged value. Check existence separately if the UI must distinguish those cases.</li>
<li>On successful writes, use <b>Post/Redirect/Get</b>: send a 303 Location response and exit. The fresh GET lists committed state and reduces refresh resubmission.</li>
<li>POST/CSRF prevents some forged or unintended requests; it does not grant permission to edit someone else's data. Add ownership/role checks for a real multi-user application.</li></ul>
""", diagram="wd5_crud", programs=["wd5p5"]),
        T("Preventing SQL Injection: Values Are Not SQL Syntax", """
<p>SQL injection occurs when untrusted input is concatenated into SQL and changes the query's structure. A value like <code>missing' OR '1'='1</code> can turn a supposed exact lookup into an always-true predicate.</p>
@@safe_lookup@@
<ul><li><b>Prepared statements</b> keep SQL structure separate from parameter data. The server treats an apostrophe or OR expression in a bound value as data, not as newly supplied SQL syntax.</li>
<li>Do not quote the placeholder itself: use <code>WHERE name=?</code>, not a quoted question mark. Do not concatenate a submitted value elsewhere in the same query and assume the prepared part protects it.</li>
<li><code>?</code> cannot stand for a table name, column name, ASC/DESC keyword or arbitrary SQL clause. Map submitted options through a small allowlist of trusted identifiers/fragments.</li>
<li><code>htmlspecialchars</code> protects HTML output, not SQL. <code>addslashes</code> is not the preferred SQL defence. Even proper SQL escaping requires correct connection encoding and is more error-prone than parameterising values.</li>
<li>A bound LIKE value can still contain legitimate LIKE wildcards such as %. That affects search semantics, not SQL structure; escape wildcards separately if the requirement is literal substring matching.</li>
<li>The isolated read-only anti-example returns all three seed contacts; the prepared probe returns zero, and a genuine O'Neil lookup returns one. The unsafe query is labelled a lab anti-example and is absent from all four web apps.</li></ul>
""", diagram="wd5_injection", programs=["wd5p6"]),
    ],
}

SEC_5_4 = {
    "title": {"en": "5.4 Error Handling, Consistency and Application Security"},
    "items": [
        T("Database Exceptions, Transactions, Commit and Rollback", """
<ul><li>Use strict MySQLi reporting and catch <code>mysqli_sql_exception</code> where a known condition needs a specific response. For example, duplicate key error 1062 can become a clear validation message; unrelated failures should still be logged/handled rather than silently ignored.</li>
<li>A transaction groups related writes: <code>begin_transaction()</code> &rarr; operations &rarr; <code>commit()</code> on complete success; <code>rollback()</code> on failure. Use transactional tables such as <b>InnoDB</b>.</li>
<li>Stock change + movement log is a useful example: either decrement the quantity and record the movement, or keep neither change. A failure between independent autocommitted writes otherwise leaves inconsistent data.</li>
<li>A conditional statement such as <code>UPDATE stock SET qty=qty-? WHERE id=? AND qty&gt;=?</code> checks availability in the write itself. A separate read-then-update without adequate locking can race with another request.</li>
<li>The program commits a sale of 2 from 5, rejects a later sale of 9, and verifies the remaining quantity (3) and movement rows (1). Validate positive quantities before processing any stock request.</li>
<li>CREATE/ALTER/DROP can cause <b>implicit commits</b>; do not assume DDL will roll back like normal InnoDB row changes. Transactions also do not magically undo external email or other non-database side effects.</li>
<li>Keep detailed errors in restricted server logs, not in public HTML. Free result resources and close statements when finished; roll back any pending transaction before propagating an unexpected failure.</li></ul>
""", diagram="wd5_transaction", programs=["wd5p7"]),
        T("Validation, Escaping, CSRF and Authorisation Are Separate Jobs", """
<table><tr><th>Boundary</th><th>Required control</th></tr>
<tr><td>Input shape/business rules</td><td>Validate IDs, lengths, email, non-negative integer stock, permitted actions and decimal prices.</td></tr>
<tr><td>SQL execution</td><td>Bind values; allowlist structural options; use a least-privileged database account.</td></tr>
<tr><td>HTML output</td><td>Escape database/form values with htmlspecialchars, including attributes and textarea content.</td></tr>
<tr><td>State-changing HTTP request</td><td>POST + a server-checked session CSRF token + Post/Redirect/Get after success.</td></tr>
<tr><td>Access to private data</td><td>Authenticate and authorise every applicable request; a CSRF token is not a login.</td></tr>
<tr><td>Deployment/configuration</td><td>HTTPS, secure session cookies, private secrets, safe public errors, updates and backups.</td></tr></table>
<ul><li>A row read back from the database can contain a stored XSS payload. For a post body use <code>nl2br(htmlspecialchars($body))</code>, not raw HTML rendering.</li>
<li>Hidden fields and dropdowns are editable by a client. Check every posted ID/action and re-check permissions on the server.</li>
<li>All project writes use CSRF-protected POSTs. Blog, Contacts and To-Do are intentionally local, single-user/admin labs; add the Unit 4 access guard and record-level permissions before public or multi-user use.</li>
<li>Inventory includes its own login gate and has no default admin password: ADMIN_HASH must be configured. Its successful login rotates the session ID/token; full logout revokes access.</li></ul>
"""),
    ],
}

SEC_5_5 = {
    "title": {"en": "5.5 Complete Database Applications (Practicals 20-23)"},
    "items": [
        T("Blog Application: Complete Create, Read, Update and Delete (Practical 20)", """
@@blog_schema@@
<ul><li><b>Create:</b> a POST supplies title/body; validate title 1-100 and body 1-5000 bytes in this reference, execute a prepared INSERT, then redirect.</li>
<li><b>Read:</b> list posts in stable ID order and search titles with a bound LIKE value. All displayed titles/bodies are escaped; newline formatting is applied only after escaping.</li>
<li><b>Update:</b> a GET edit ID loads the existing row into a sticky form; POST validates both input and row existence before a prepared UPDATE.</li>
<li><b>Delete:</b> the per-post form sends a positive ID, action and CSRF token by POST. Delete one matching primary key, then redirect to the updated list.</li>
<li><b>Files:</b> index.php, db.php, web.php, plus the one-time schema SQL. The full code card shows each PHP file; save sections separately.</li>
<li><b>Verify:</b> create BusBook Begins, edit it to Weekend Route Update, search Weekend, then delete it. The genuine transcript ends with <code>Posts: 0</code>.</li>
<li>Lengths in these compact references use strlen (byte length); use mb_strlen plus a consistent validation policy when character-count rules for multilingual text are required.</li></ul>
""", programs=["wd5p8"]),
        T("MVC + OOP Contact Management (Practical 21)", """
<p><b>MVC</b> separates responsibilities so changes to HTML do not force changes to SQL. It is an organisation pattern, not a framework you must install.</p>
@@mvc_tree@@
@@contact_schema@@
<ul><li><b>Model (Contact):</b> owns prepared database operations: search, find, save and delete. It knows table structure but does not read $_POST or emit HTML.</li>
<li><b>Controller (ContactController):</b> reads the request, validates name/email/ID, checks CSRF, chooses the model operation, redirects after writes, and passes data to the view.</li>
<li><b>View:</b> renders forms and contact rows using escaped values. It does not open connections or run SQL.</li>
<li><b>Front controller:</b> index.php creates the dependencies and calls handle. Constructors receive a connection/model, illustrating a simple OOP design without hidden global dependencies inside the classes.</li>
<li>All four requirements are implemented: <b>add, search, update, delete</b>. Name and email search values and every write ID/value are bound parameters.</li>
<li>Test O'Neil as legitimate data and an injection-shaped search as literal input. Correct handling is one matching contact for the real name and no broad data disclosure for the probe.</li></ul>
""", diagram="wd5_mvc", programs=["wd5p9"]),
        T("AI-Assisted To-Do Development and Review (Practical 22)", """
<p>The practical asks for a PHP To-Do application with the help of an AI code-generation tool. The reference here is generated for this lesson, reviewed and really executed; it does not claim that a separate external AI service was used.</p>
@@todo_schema@@
<p><b>Example requirement prompt:</b></p>
@@ai_prompt@@
<ol><li><b>Specify:</b> list features, table fields, PHP/MySQLi requirement, safety rules and acceptance tests before requesting code. Do not provide real production credentials.</li>
<li><b>Inspect:</b> explain each query and request branch. Replace concatenated values, deleting GET links, raw HTML echoes and unchecked IDs; ensure server-side validation exists.</li>
<li><b>Run:</b> import a fresh schema, configure the connection, open through a PHP server, then test create/edit/toggle/filter/delete against actual stored rows.</li>
<li><b>Challenge:</b> submit a blank title, forged token, missing ID and unrecognised filter. The reference rejects them and keeps valid state.</li>
<li><b>Document:</b> retain the prompt, original response, your corrections, screenshots and the observed test results. Be able to explain the code rather than merely copying generated output.</li></ol>
<ul><li>The implementation uses a boolean-like done field constrained to 0/1. Toggle updates one ID; all/pending/done filters map to fixed allowlisted SQL fragments.</li>
<li>Human review and real execution are necessary even when generated code looks plausible. Never record a test as passed without actually running it.</li></ul>
""", programs=["wd5p10"]),
        T("Inventory Management: CRUD, Login and Stock Integrity (Practical 23)", """
@@inventory_schema@@
<ul><li><b>Products:</b> unique SKU, name, integer quantity and DECIMAL price. Create/update validate every field; list/edit/delete target explicit IDs.</li>
<li><b>Stock operations:</b> sell/restock use positive integers and conditional UPDATEs. Overselling returns 409 without decreasing quantity; restocking also enforces the maximum quantity. Quantity at or below 3 shows a low-stock alert.</li>
<li><b>Authentication:</b> auth.php refuses operation unless ADMIN_HASH is configured. Login uses password_verify; successful authentication rotates the session ID/token. Anonymous requests see login, not product records.</li>
<li><b>Writes:</b> CSRF-protected POSTs and prepared values; duplicate SKU becomes a user-facing validation error instead of a raw database message.</li>
<li><b>Money:</b> validated decimal strings are bound as strings into DECIMAL. This avoids relying on binary floating-point calculations for the displayed price.</li>
<li><b>Local proof:</b> add USB Cable at qty 5, update to 8, sell 6 (qty 2), reject an oversell, restock 3 (qty 5), delete and log out. Test credentials in the transcript are only disposable lab credentials.</li>
<li><b>Hosting is a separate step:</b> the reference has been locally executed, not externally deployed as a live inventory service. Follow the next section to carry out the hosting part on your own PHP-capable account.</li></ul>
@@inventory_hash@@
""", programs=["wd5p11"]),
    ],
}

SEC_5_6 = {
    "title": {"en": "5.6 Hosting and Practical Verification"},
    "items": [
        T("Hosting the Inventory Application: Deployment Checklist", """
<ol><li><b>Choose an appropriate host:</b> supported PHP with mysqli/mysqlnd, a MySQL-compatible database and HTTPS. Static-file hosting, including GitHub Pages, cannot execute PHP or run this database application.</li>
<li><b>Back up:</b> export schema/data with phpMyAdmin or an appropriate dump tool; retain a restorable local copy. Practise import before changing the deployed database.</li>
<li><b>Create database/account:</b> import schema using an administrative account, then give the runtime application only the SELECT/INSERT/UPDATE/DELETE privileges it needs on that database.</li>
<li><b>Configure secrets privately:</b> set DB_HOST, DB_NAME, DB_USER, DB_PASS and a unique ADMIN_HASH using the hosting/server's environment mechanism. PHP does not automatically load .env. Never place real passwords in a public repository, downloadable SQL backup or source-view endpoint.</li>
<li><b>Upload files:</b> transfer the required PHP files and confirm paths/case sensitivity. Keep admin-only imports/backups and private configuration outside the public document root where possible.</li>
<li><b>Enforce HTTPS:</b> make sure the server correctly recognises HTTPS and sends Secure/HttpOnly/SameSite session cookies. Behind a TLS proxy, configure this according to the trusted deployment rather than trusting an arbitrary client-supplied header.</li>
<li><b>Safe error policy:</b> disable public debug/stack-trace output, log details to restricted server logs and test the friendly failure path with a temporary bad configuration.</li>
<li><b>Remote smoke test:</b> guest blocked, login succeeds with your own password, CRUD persists after reload, duplicate/negative values fail, oversell does not alter stock, CSRF fails safely and logout revokes direct access.</li>
<li><b>Maintain:</b> keep PHP/server dependencies updated, rotate credentials when needed, monitor access/errors and regularly test backup restoration.</li></ol>
<p>The lesson's publication makes the <b>study material</b> available in the app. It is not a claim that the inventory PHP/database project itself has been hosted on an external service.</p>
""", diagram="wd5_deploy"),
        T("Acceptance Test Matrix for Practicals 19-23", """
<table><tr><th>Test</th><th>Expected evidence</th></tr>
<tr><td>Connect + UTF-8</td><td>Actual query returns 5; utf8mb4 and a Unicode round trip work.</td></tr>
<tr><td>DDL scratch lab</td><td>Columns change after ALTER; deleted scratch schema is absent from metadata.</td></tr>
<tr><td>Prepared CRUD</td><td>New ID, real changed rows, intended deletion and remaining records verified.</td></tr>
<tr><td>Apostrophe/injection</td><td>O'Neil works; injection-shaped bound input does not broaden results.</td></tr>
<tr><td>Blog</td><td>Create/edit/search/delete, escaped stored HTML, blank/missing-ID/CSRF rejection.</td></tr>
<tr><td>MVC Contacts</td><td>Add/search/update/delete with controller/model/view separation and literal search data.</td></tr>
<tr><td>To-Do</td><td>Persist title, edit, toggle, filter done/pending, delete; invalid filter is rejected.</td></tr>
<tr><td>Inventory gate</td><td>Anonymous and wrong-password requests cannot read/alter stock; logout removes access.</td></tr>
<tr><td>Inventory rules</td><td>Negative/fractional stock, excess decimals, duplicate SKU and oversell are rejected.</td></tr>
<tr><td>Transaction failure</td><td>No partial stock/log update; committed count and final quantity match.</td></tr>
<tr><td>Request safety</td><td>GET cannot delete; forged CSRF and malformed IDs do not mutate rows.</td></tr>
<tr><td>Hosted environment</td><td>Own remote smoke-test evidence, HTTPS configuration and restorable backup, not merely a local success message.</td></tr></table>
<ul><li>Use a fresh disposable database for repeatable tests. A listing screenshot alone may hide a failed write; query the stored state or reload independently.</li>
<li>Record expected and observed results separately. The unit's local database tests and app-render checks are distinct from a student's future hosting verification.</li>
<li>Practicals 19-23 together cover administration, CRUD, MVC/OOP, SQL-injection prevention, AI-assisted review and deployment discipline.</li></ul>
"""),
    ],
}

NOTES = [SEC_5_1, SEC_5_2, SEC_5_3, SEC_5_4, SEC_5_5, SEC_5_6]
