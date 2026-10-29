"""Unit 5 revision: 14 syntax cards, 48 viva Q&A and 18 practical/exam practice tasks."""
from php_content import SXE, VE, XE, G

SYNTAX = [
    G("Connection and Database Cards", [
        SXE("Connect and charset", '''mysqli_report(
  MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT
);
$db = new mysqli($host,$user,$pass,$name);
$db->set_charset("utf8mb4");''',
            "Credentials are private server configuration. Catch/log failures safely."),
        SXE("Query results", '''SELECT query() -> mysqli_result
DML query()    -> true on success
fetch_assoc()  -> next named row
num_rows       -> SELECT count
insert_id      -> generated ID''',
            "Strict reporting throws on SQL failures. Do not fetch rows from a successful UPDATE boolean."),
        SXE("DDL and keys", '''CREATE TABLE / ALTER TABLE / DROP TABLE
id INT PRIMARY KEY AUTO_INCREMENT
email VARCHAR(120) UNIQUE
price DECIMAL(10,2)
ENGINE=InnoDB''',
            "Structure is DDL; row CRUD changes data. IDs are not gap-free row counts."),
    ]),
    G("Prepared CRUD Cards", [
        SXE("Fetch a SELECT", '''$r = $db->query($constantSql);
while ($row = $r->fetch_assoc()) {
  echo htmlspecialchars($row["name"]);
}
$r->free();''',
            "Only use a constant/trusted query here; bind all submitted values."),
        SXE("Prepared INSERT", '''$s = $db->prepare(
  "INSERT INTO contacts(name,email) VALUES (?,?)"
);
$s->bind_param("ss", $name, $email);
$s->execute();
$id = $db->insert_id;''',
            "SQL shape and literal values travel separately. ? is not quoted."),
        SXE("Binding and reuse", '''i integer   d double
s string    b blob
bind_param("si", $name, $marks);
// Variables bind by reference.
// Change values, execute again.
// ? count = type count = variable count.''',
            "For SELECT, get_result needs mysqlnd; bind_result/fetch is an alternative."),
        SXE("Targeted writes", '''UPDATE posts SET title=? WHERE id=?
DELETE FROM posts WHERE id=?
$s->affected_rows
// 0 on UPDATE can mean unchanged OR absent.
// Validate IDs; never omit the predicate.''',
            "Mutations use POST + CSRF + authorisation; redirect after success."),
    ]),
    G("Security and Consistency Cards", [
        SXE("Placeholder boundaries", '''WHERE name=?        // yes: value
ORDER BY ?          // not a column selector
FROM ?              // not a table selector
// Allowlist identifiers / sort keywords.
// A LIKE value may still contain % wildcards.''',
            "Prepared parameters protect values, not SQL structure supplied elsewhere."),
        SXE("Different defences", '''Validate input       -> business rules
Prepared SQL         -> injection defence
htmlspecialchars     -> safe HTML output
POST + CSRF          -> request integrity
Login + permissions  -> access control''',
            "No single layer replaces the others. Stored database text can still carry XSS."),
        SXE("Transaction", '''$db->begin_transaction();
try {
  // Related InnoDB row writes.
  $db->commit();
} catch (Throwable $e) {
  $db->rollback();
  throw $e;
}''',
            "Keep all related writes or none. DDL can cause implicit commits."),
    ]),
    G("Projects and Hosting Cards", [
        SXE("MVC responsibilities", '''Controller: request, validation, redirect
Model:      prepared SQL and data access
View:       escaped HTML, no queries
index.php:  construct dependencies, dispatch''',
            "The controller passes model data to the view; no framework is required for this small MVC example."),
        SXE("AI-assisted To-Do review", '''Specify features + schema + security.
Inspect every generated query/echo/ID.
Run add/edit/toggle/filter/delete tests.
Challenge blank input, CSRF and injection.
Record corrections + observed evidence.''',
            "Generated code is a draft. Never mark an unrun test as passed or provide production secrets."),
        SXE("Inventory rules", '''SKU: unique, allowlisted shape
Qty: non-negative integer
Price: validated decimal -> DECIMAL
Sell: UPDATE ... WHERE qty >= amount
Admin: password_verify + session guard''',
            "ADMIN_HASH is required; there is no built-in admin password. Oversell must not change stock."),
        SXE("Deployment checklist", '''PHP + mysqli/mysqlnd + database + HTTPS
Import schema with admin account.
Runtime account: minimum CRUD rights.
Private DB settings + ADMIN_HASH.
Hide debug output; test backups + logout.''',
            "Static hosting cannot execute PHP. Local reference tests are not proof of external deployment."),
    ]),
]

_VIVA = [
    VE("What does MySQLi stand for?", "MySQL Improved: PHP's extension/API for connecting to a MySQL-compatible database and executing queries, including prepared statements."),
    VE("MySQL vs phpMyAdmin?", "MySQL is a database server. phpMyAdmin is a web administration interface for it or a compatible server; your own PHP application uses a client API such as MySQLi."),
    VE("Which database actually generated this unit's outputs?", "A real MariaDB server through PHP 8.4 mysqlnd/MySQLi. MariaDB is MySQL-compatible; these outputs are not SQLite emulation or hand-written rows."),
    VE("Why use a database instead of a feedback text file?", "Structured queries, keys, constraints, shared persistent storage and transactional/concurrent changes become easier to manage reliably."),
    VE("Name the usual MySQLi connection arguments.", "Host, username, password and database, with optional port and Unix socket. Keep credentials in private server configuration."),
    VE("Why can localhost and 127.0.0.1 behave differently?", "localhost may select a local Unix socket, whereas 127.0.0.1 normally uses TCP. Match the server listener and connection configuration."),
    VE("Why call set_charset('utf8mb4')?", "It configures full-Unicode encoding on the database connection. A UTF-8 HTML meta tag does not configure the connection or table charset."),
    VE("Object-oriented vs procedural MySQLi?", "They expose the same underlying API in different syntax: $db->query($sql) versus mysqli_query($db,$sql), for example."),
    VE("phpMyAdmin Structure vs Browse vs SQL?", "Structure shows columns/indexes/constraints; Browse shows records; SQL runs entered statements and presents their results or errors."),
    VE("CREATE TABLE, ALTER TABLE and DROP TABLE do what?", "Create defines structure, alter changes it, and drop removes the table including its data. These are DDL operations."),
    VE("DELETE FROM vs DROP TABLE?", "DELETE removes selected rows while keeping table structure; DROP removes the structure and its rows. Be certain of the target and back up first."),
    VE("Primary key, UNIQUE and AUTO_INCREMENT?", "A primary key uniquely identifies a non-null row; UNIQUE rejects duplicate values under its rules; AUTO_INCREMENT generates numeric identifiers, not gap-free row numbers."),

    VE("What does query() return for SELECT versus a successful UPDATE?", "SELECT returns mysqli_result; an UPDATE through query returns true on success. With strict reporting, failures throw rather than being ordinary successful results."),
    VE("What does fetch_assoc do at the end of a result?", "It returns the next associative row each time and null when no rows remain. The keys correspond to selected column names or aliases."),
    VE("num_rows vs affected_rows?", "num_rows counts buffered result rows from a SELECT; affected_rows reports the last write's affected-row count, subject to operation/client flags."),
    VE("What is insert_id?", "The generated auto-increment ID from the last applicable insert on that connection. It is not the number of records in the table."),
    VE("The normal prepared-statement sequence?", "prepare the SQL template; bind variables; execute; fetch SELECT results or inspect write evidence; close when finished."),
    VE("What are the bind_param type letters?", "i integer, d double, s string and b blob. The type-string length/order and variables must match the placeholders."),
    VE("What does binding by reference mean?", "The statement uses the current values of its bound variables at execute time. Change those variables and execute again to reuse it; bind variables rather than temporary expressions."),
    VE("Why must the question-mark placeholder not be quoted?", "The unquoted question mark marks a parameter position. Quoting it makes it a literal SQL string rather than that parameter placeholder."),
    VE("What if get_result is unavailable?", "get_result requires mysqlnd. Bind output variables with bind_result and loop fetch instead, or deploy with mysqlnd support."),
    VE("Why is WHERE critical in UPDATE and DELETE?", "Without the intended predicate the statement can affect all rows. Parameterisation does not repair a missing or logically wrong WHERE clause."),
    VE("Does UPDATE affected_rows=0 always mean no matching ID?", "No. With default client flags it can also mean the matching row already had those values. Check existence separately if the UI needs that distinction."),
    VE("Should the production runtime account have CREATE/DROP privileges?", "Normally not for a CRUD application. Import/migrate schemas with an appropriate admin account, then grant only the runtime privileges actually required."),

    VE("What is SQL injection?", "Untrusted input is incorporated into SQL syntax and changes the query structure, potentially disclosing or changing unintended data."),
    VE("How does a prepared parameter prevent value-based injection?", "It keeps the SQL template separate from the bound value, so quotes or OR clauses in that value remain literal data rather than new SQL syntax."),
    VE("Can a parameter stand for a table or column name?", "No. Use a controlled mapping/allowlist of trusted identifiers, sort directions or clauses. Bind ordinary values separately."),
    VE("Does htmlspecialchars prevent SQL injection?", "No. It escapes HTML output. Prepared SQL values prevent SQL injection; they do not automatically escape the value when rendering HTML."),
    VE("Does a bound LIKE value make percent signs literal?", "No. Percent/underscore can still have LIKE wildcard semantics inside the value. That is search behaviour, not SQL injection; escape wildcards separately if literal matching is required."),
    VE("Is a CSRF token the same as authentication?", "No. It helps verify request origin/integrity for a session; login and authorisation decide who may access or change the data."),
    VE("Why use POST and a redirect for mutations?", "GET should not delete or otherwise mutate records. A validated CSRF-protected POST performs the change, then 303/GET displays stored state and reduces refresh resubmission."),
    VE("What do commit and rollback do?", "commit keeps a completed transaction's related changes; rollback undoes its uncommitted transactional row changes after failure."),
    VE("Why use InnoDB, and can DDL be rolled back like row writes?", "InnoDB supports these transactions. CREATE/ALTER/DROP can trigger implicit commits, so do not assume DDL participates like ordinary transactional row updates."),
    VE("Why check availability inside the stock UPDATE?", "A conditional UPDATE with qty >= amount checks and changes stock atomically. A separate read-then-write can race unless adequate concurrency control is used."),
    VE("Why use DECIMAL for prices?", "It stores exact fixed-point decimal amounts; binary floating-point can introduce rounding surprises. The reference validates and binds price strings into DECIMAL."),
    VE("How should duplicate key error 1062 and unexpected errors be handled?", "Recognise the known duplicate case and show a clear validation message; log unexpected details securely and return a safe generic failure instead of exposing raw database messages."),

    VE("What is MVC?", "Model-View-Controller: a separation of data access, presentation and request/application coordination. A small PHP MVC app does not require a framework."),
    VE("What belongs in the Contact model?", "Prepared database operations such as search/find/save/delete. It should not read $_POST or emit HTML."),
    VE("What belongs in the controller?", "Read and validate HTTP input, check CSRF/permissions, call the appropriate model method, choose a redirect or pass data to a view."),
    VE("What belongs in the view?", "Forms and escaped HTML output. It should not open database connections or execute SQL."),
    VE("Why pass a model/connection through a constructor?", "Dependencies become explicit and replaceable, rather than hidden global state inside every method; the front controller wires them together."),
    VE("Name the four Blog CRUD actions in Practical 20.", "Create a validated post, list/read/search stored posts, load and save an edit, and delete one primary key using a CSRF-protected POST."),
    VE("What evidence should an AI-assisted To-Do practical record?", "The requirement prompt, generated draft, your review/corrections, and actually observed add/edit/toggle/filter/delete and negative-test results. Never claim unrun tests passed."),
    VE("Why is the To-Do filter allowlisted?", "The all/pending/done key selects a fixed trusted SQL fragment. Arbitrary submitted SQL clauses are not concatenated into the query."),
    VE("Which Inventory values must be validated?", "SKU shape/uniqueness, name length, non-negative integer quantity, decimal price precision, positive stock-change amount and explicit record ID, alongside session/CSRF checks."),
    VE("Why does Inventory require ADMIN_HASH?", "There is no built-in default admin password. The operator configures a hash of a unique chosen password; login checks it with password_verify and starts authenticated access."),
    VE("Can this PHP inventory run on static hosting such as GitHub Pages?", "No. It needs a PHP-capable server with MySQLi/mysqlnd and a compatible database. Publishing study-material JSON/HTML is different from hosting that database application."),
    VE("What proves a successful remote deployment?", "Remote guest/login/CRUD/validation/oversell/logout smoke tests over HTTPS, correctly configured private credentials, safe errors and a tested backup/restore process; local execution alone is not proof."),
]
assert len(_VIVA) == 48, len(_VIVA)
VIVA = [
    G("Database Foundations and Administration", _VIVA[:12]),
    G("MySQLi, Results and Prepared CRUD", _VIVA[12:24]),
    G("Injection, Security and Transactions", _VIVA[24:36]),
    G("MVC, Projects, AI Review and Hosting", _VIVA[36:]),
]

EXAM_QS = [
    XE("Explain the browser-PHP-MySQLi-database request path. Distinguish MySQL/MariaDB, MySQLi and phpMyAdmin.", 4),
    XE("Perform the phpMyAdmin practical: create/select a scratch database, create and alter a table, run CRUD SQL, export a backup, then safely drop the scratch table/database. Record observed evidence. (Practical 19)", 6),
    XE("Compare CREATE, ALTER, DROP and DELETE; explain suitable data types, primary/foreign keys, UNIQUE, NOT NULL and CHECK.", 4),
    XE("Write a MySQLi connection with explicit error reporting and utf8mb4. Explain private credentials, local socket/TCP differences and safe error handling.", 4),
    XE("Write a SELECT program using num_rows, fetch_assoc and free. Show its procedural equivalents and explain result types.", 4),
    XE("Write and reuse a prepared INSERT with bind_param, insert_id and duplicate-email handling. Explain placeholder order, type letters and binding by reference.", 6),
    XE("Write prepared UPDATE and DELETE statements for a supplied primary key. Explain missing WHERE hazards and the ambiguity of UPDATE affected_rows=0.", 6),
    XE("Demonstrate SQL injection using an isolated read-only lookup, then correct it with a prepared parameter. Test an apostrophe-containing name and an injection-shaped value.", 6),
    XE("Explain why parameters cannot replace table/column names, how to allowlist sorting/filter options, and why SQL parameterisation is different from HTML escaping.", 4),
    XE("Implement an InnoDB stock decrement plus movement log in one transaction. Commit success, roll back insufficient stock/failure, and verify quantity and movement count.", 6),
    XE("Give a layered security checklist covering validation, prepared SQL, escaped stored text, POST/CSRF, authentication/authorisation and least-privilege credentials.", 4),
    XE("Develop the complete Blog application with create/list/search/edit/delete, sticky validation errors, prepared values, safe HTML and Post/Redirect/Get. (Practical 20)", 6),
    XE("Draw MVC request/data flow and explain the responsibilities of the front controller, model, controller and view in a PHP/OOP application.", 4),
    XE("Develop MVC Contacts with add/search/update/delete. Use constructor-supplied dependencies, prepared SQL, CSRF checks and escaped views. Prove injection-shaped search remains data. (Practical 21)", 6),
    XE("Use an AI code-generation workflow to build/review a PHP/MySQLi To-Do app. Record the prompt, corrections and actual add/edit/toggle/filter/delete plus negative-test evidence. (Practical 22)", 6),
    XE("Develop authenticated Inventory CRUD with unique SKU, integer quantity, DECIMAL price, atomic stock checks, low-stock alerts and full logout. (Practical 23)", 6),
    XE("Carry out the Inventory hosting checklist on a PHP-capable account: import, private settings, unique admin hash, HTTPS, safe errors, remote smoke tests and backup/restore. Distinguish local proof from deployment proof. (Practical 23)", 6),
    XE("Design an acceptance-test matrix for CRUD, malformed/missing IDs, XSS/injection probes, forged CSRF, duplicate/negative stock, oversell, transaction rollback and logged-out access.", 4),
]
