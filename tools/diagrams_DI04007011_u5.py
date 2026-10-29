"""DI04007011 Unit 5: 10 original 360-wide MySQLi, CRUD, MVC and deployment diagrams."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, grid, PF, GREY
from diagrams_DI03000061_u1 import code


def stack():
    b = title("From Browser Form to Stored Rows")
    for y, head, desc, fill, st in [
        (46, "BROWSER / PRESENTATION", "HTML forms, links, rendered responses", BLUEF, BLUE),
        (118, "PHP + MySQLi / APPLICATION", "validate -> prepare -> bind -> execute", PF, P),
        (190, "MySQL-COMPATIBLE SERVER / DATA", "tables, keys, constraints, transactions", GREENF, GREEN),
    ]:
        b += box(12, y, 336, 48, fill, st, 8, 1.3)
        b += text(180, y + 15, head, 9.3, weight="bold", color=st)
        b += text(180, y + 34, desc, 8.5)
    b += arr([(170, 94), (170, 118)], BLUE)
    b += arr([(190, 118), (190, 94)], GREEN)
    b += arr([(170, 166), (170, 190)], P)
    b += arr([(190, 190), (190, 166)], GREEN)
    b += note(12, 258, 336, ["MySQLi is PHP's client API, not a database.",
                             "phpMyAdmin is a web administration UI.",
                             "The lesson runs real MySQLi against MariaDB,",
                             "a MySQL-compatible server, not a SQL emulator."], size=8.8)
    return svg(360, 342, b)


def phpmyadmin():
    b = title("phpMyAdmin: Practical 19 Workflow")
    steps = [
        ("1  START SERVICES", "Local Apache/PHP + MySQL/MariaDB", BLUEF, BLUE),
        ("2  OPEN ADMIN UI", "localhost/phpmyadmin; sign in appropriately", BLUEF, BLUE),
        ("3  CREATE / SELECT DATABASE", "Choose utf8mb4; select it before SQL", GREENF, GREEN),
        ("4  SQL TAB", "CREATE / ALTER / INSERT / SELECT / UPDATE", PF, P),
        ("5  INSPECT RESULTS", "Structure = columns; Browse = stored rows", GREENF, GREEN),
        ("6  EXPORT BEFORE DESTRUCTIVE WORK", "Back up first; DROP only the scratch schema", ORANGEF, ORANGE),
    ]
    for i, (head, desc, fill, st) in enumerate(steps):
        y = 44 + i * 50
        b += box(12, y, 336, 38, fill, st, 7, 1.2)
        b += text(24, y + 12, head, 8.4, anchor="start", color=st, weight="bold")
        b += text(24, y + 27, desc, 8.0, anchor="start")
        if i < 5:
            b += down(180, y + 38, y + 50)
    b += note(12, 350, 336, ["SQL executes on the database server; the GUI",
                             "helps manage it. Screens differ by version.",
                             "Never expose a root/blank-password admin UI."], size=8.9)
    return svg(360, 420, b)


def table_design():
    b = title("Table Design: Types, Keys and Rules")
    b += grid(12, 44, [80, 108, 148], [
        ["column", "type", "rule / purpose"],
        ["id", "INT", "PRIMARY KEY, AUTO_INCREMENT"],
        ["name", "VARCHAR(80)", "NOT NULL"],
        ["email", "VARCHAR(120)", "UNIQUE"],
        ["marks", "INT", "CHECK 0..100"],
        ["price*", "DECIMAL(10,2)", "exact money, not FLOAT"],
    ], rh=25, size=7.5)
    b += rbox(78, 238, 126, 32, "stock.id (PK)", fill=BLUEF, stroke=BLUE, size=8.5)
    b += rbox(276, 238, 146, 32, "movements.stock_id (FK)", fill=GREENF, stroke=GREEN, size=7.8)
    b += arr([(141, 238), (203, 238)], P)
    b += text(172, 221, "1 : many", 8.3, color=P)
    b += note(12, 278, 336, ["*Price belongs to products; shown as a type example.",
                             "A key identifies or links rows. Constraints are",
                             "server-side rules, not substitutes for form checks.",
                             "CREATE/ALTER/DROP change structure (DDL).",
                             "INSERT/UPDATE/DELETE change data (DML)."], size=8.5)
    return svg(360, 378, b)


def connection():
    b = title("A MySQLi Connection's Working Life")
    steps = [
        ("1  REPORT STRICT ERRORS", "mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT)", ORANGEF, ORANGE),
        ("2  CONNECT + SELECT DATABASE", "new mysqli(host, user, password, database)", BLUEF, BLUE),
        ("3  SET THE CONNECTION CHARSET", 'set_charset("utf8mb4")', BLUEF, BLUE),
        ("4  EXECUTE SQL", "constant query OR prepared values", PF, P),
        ("5  READ RESULT / CHECK WRITE", "fetch_assoc / num_rows / affected_rows", GREENF, GREEN),
        ("6  RELEASE RESOURCES", "free result -> close statement / connection", GREENF, GREEN),
    ]
    for i, (head, src, fill, st) in enumerate(steps):
        y = 44 + i * 48
        b += box(12, y, 336, 36, fill, st, 7, 1.1)
        b += text(24, y + 11, head, 8.3, anchor="start", weight="bold", color=st)
        b += text(24, y + 26, src, 7.7, anchor="start", mono=True)
        if i < 5:
            b += down(180, y + 36, y + 48)
    b += note(12, 346, 336, ["Any database operation can fail. Catch known",
                             "mysqli_sql_exception cases, log details safely,",
                             "and show generic failures to public visitors.",
                             "Do not publish connection passwords in a repo."], size=8.8)
    return svg(360, 430, b)


def crud():
    b = title("CRUD: HTTP Action, SQL and Evidence")
    b += grid(12, 44, [54, 44, 142, 96], [
        ["action", "HTTP", "SQL", "evidence"],
        ["Create", "POST", "INSERT ... VALUES (?,?)", "insert_id"],
        ["Read", "GET", "SELECT ... WHERE id=?", "result rows"],
        ["Update", "POST", "UPDATE ... WHERE id=?", "affected_rows"],
        ["Delete", "POST", "DELETE ... WHERE id=?", "affected_rows"],
    ], rh=29, size=7.2)
    labels = [("FORM", BLUEF, BLUE), ("CHECK", ORANGEF, ORANGE),
              ("PREPARE", PF, P), ("303 -> GET", GREENF, GREEN)]
    for i, (label, fill, st) in enumerate(labels):
        x = 12 + i * 88
        b += box(x, 218, 72, 40, fill, st, 6, 1.1)
        b += text(x + 36, 238, label, 7.9, weight="bold", color=st)
        if i < 3:
            b += arr([(x + 72, 238), (x + 88, 238)], GREY)
    b += note(12, 278, 336, ["Validate values + ID, check CSRF and authorisation.",
                             "No WHERE in UPDATE/DELETE can change every row.",
                             "A GET link must not delete records.",
                             "UPDATE affected_rows=0 can also mean unchanged."], size=8.7)
    return svg(360, 362, b)


def prepared():
    b = title("Prepared Statements Keep Values Separate", size=13.3)
    b += box(12, 44, 336, 44, BLUEF, BLUE, 7, 1.2)
    b += code(24, 57, ['INSERT INTO students(name,marks)', 'VALUES (?, ?)   // placeholders are NOT quoted'], size=7.8, lh=15)
    b += box(12, 104, 336, 42, GREENF, GREEN, 7, 1.2)
    b += code(24, 117, ['$name = "O\'Neil";   $marks = 88;', 'bind_param("si", $name, $marks);'], size=7.9, lh=15)
    b += down(180, 88, 104, P)
    b += down(180, 146, 164, P)
    b += rbox(180, 180, 210, 32, "prepare -> bind -> execute", fill=PF, stroke=P, size=9.3)
    b += down(180, 196, 218, P)
    b += box(12, 218, 336, 44, ORANGEF, ORANGE, 7, 1.2)
    b += lines(180, 231, ["SELECT: get_result -> fetch rows",
                          "WRITE: affected_rows / insert_id"], size=8.6, lh=17)
    b += note(12, 282, 336, ["Types: i integer, d double, s string, b blob.",
                             "Variables bind by reference; change values and",
                             "execute again. Count/type order must match ?.",
                             "? is for values, not table/column names."], size=8.8)
    return svg(360, 366, b)


def injection():
    b = title("SQL Injection: Code vs Literal Data")
    b += box(12, 44, 336, 100, REDF, RED, 8, 1.2)
    b += text(24, 60, "UNSAFE CONCATENATION - isolated anti-example", 8.5, anchor="start", color=RED, weight="bold")
    b += code(24, 84, ["input: missing' OR '1'='1", "WHERE name='$input'", "SQL syntax changes -> all 3 seed rows"], size=8.0, lh=18)
    b += box(12, 162, 336, 100, GREENF, GREEN, 8, 1.2)
    b += text(24, 178, "PREPARED SQL + SEPARATE VALUE", 9.0, anchor="start", color=GREEN, weight="bold")
    b += code(24, 202, ["WHERE name=?", "bind the entire input as ONE value", "No exact name match -> 0 rows"], size=8.0, lh=18)
    b += note(12, 282, 336, ["A real name like O'Neil works without SQL surgery.",
                             "Do not try to fix injection with HTML escaping.",
                             "Prepared values + allowlisted identifiers +",
                             "least-privilege accounts are complementary."], size=8.8)
    return svg(360, 366, b)


def transaction():
    b = title("Transaction: All Writes or No Writes")
    b += rbox(180, 58, 180, 30, "begin_transaction()", fill=BLUEF, stroke=BLUE, size=9.7)
    b += down(180, 73, 98)
    b += rbox(180, 120, 258, 44, "decrement stock if enough\n+ insert movement record", fill=PF, stroke=P, size=9)
    b += down(180, 142, 166)
    b += decision(180, 190, "all checks/writes OK?", w=154, h=48, size=8.7)
    b += arr([(103, 190), (80, 190), (80, 252)], GREEN)
    b += arr([(257, 190), (280, 190), (280, 252)], RED)
    b += text(76, 177, "yes", 8.4, color=GREEN)
    b += text(283, 177, "no / throw", 8.0, color=RED)
    b += rbox(80, 270, 138, 36, "commit: keep both", fill=GREENF, stroke=GREEN, size=8.7)
    b += rbox(280, 270, 138, 36, "rollback: undo both", fill=REDF, stroke=RED, size=8.7)
    b += note(12, 314, 336, ["InnoDB is required for these transactional writes.",
                             "5 - 2 succeeds; selling 9 of the remaining 3 fails.",
                             "Final qty = 3, successful movements = 1.",
                             "CREATE/ALTER/DROP can cause implicit commits."], size=8.7)
    return svg(360, 398, b)


def mvc():
    b = title("MVC Contacts: Each Layer Has One Job")
    b += rbox(180, 54, 148, 30, "Browser / HTTP", fill=BLUEF, stroke=BLUE, size=9.7)
    b += down(180, 69, 98, BLUE)
    b += rbox(180, 120, 172, 44, "Controller\nvalidate + choose action", fill=PF, stroke=P, size=9.1)
    b += arr([(266, 120), (280, 120), (280, 188)], P)
    b += text(306, 157, "call", 8, color=P)
    b += rbox(280, 210, 130, 44, "Model\nprepared SQL", fill=GREENF, stroke=GREEN, size=9.1)
    b += arr([(215, 210), (205, 210), (205, 142)], GREEN)
    b += text(220, 174, "rows", 7.8, color=GREEN)
    b += arr([(94, 120), (70, 120), (70, 188)], P)
    b += text(44, 157, "render", 8, color=P)
    b += rbox(70, 210, 120, 44, "View\nescaped HTML", fill=ORANGEF, stroke=ORANGE, size=9)
    b += down(70, 232, 295, ORANGE)
    b += rbox(70, 310, 120, 30, "HTML response", fill=BLUEF, stroke=BLUE, size=8.8)
    b += arr([(290, 232), (290, 295)], GREEN)
    b += arr([(270, 295), (270, 232)], GREEN)
    b += rbox(280, 310, 130, 30, "Database", fill=GREENF, stroke=GREEN, size=9.3)
    b += note(12, 350, 336, ["Controller passes model results to the view.",
                             "No SQL in the view; no HTML in the model.",
                             "Constructors receive their dependencies."], size=9.0)
    return svg(360, 420, b)


def deploy():
    b = title("Inventory Hosting: A Separate Checklist")
    steps = [
        ("1  LOCAL PROOF", "CRUD, login/logout, CSRF, oversell and bad-input tests"),
        ("2  BACKUP + EXPORT", "Export schema/data; keep a restorable local copy"),
        ("3  HOST CAPABILITY", "Supported PHP + MySQLi/mysqlnd + MySQL-compatible DB"),
        ("4  SECRETS + PRIVILEGES", "Unique DB account, ADMIN_HASH, no secrets in public files"),
        ("5  DEPLOY + IMPORT", "Upload PHP files; import SQL into the selected database"),
        ("6  HTTPS + SAFE ERRORS", "Secure session cookie; log details, hide debug output"),
        ("7  REMOTE SMOKE TEST", "Guest blocked; CRUD/stock work; logout revokes access"),
        ("8  OPERATE SAFELY", "Backups, updates, least privilege and access monitoring"),
    ]
    for i, (head, desc) in enumerate(steps):
        y = 44 + i * 47
        fill, st = (BLUEF, BLUE) if i < 4 else (GREENF, GREEN)
        b += box(12, y, 336, 35, fill, st, 7, 1.1)
        b += text(24, y + 10, head, 8.3, anchor="start", weight="bold", color=st)
        b += text(24, y + 25, desc, 7.2, anchor="start")
        if i < 7:
            b += down(180, y + 35, y + 47)
    b += note(12, 434, 336, ["The reference is locally execution-tested. This",
                             "checklist is not a claim of external deployment."], size=8.9)
    return svg(360, 490, b)


ALL = {
    "wd5_stack": stack, "wd5_phpmyadmin": phpmyadmin,
    "wd5_table_design": table_design, "wd5_connection": connection,
    "wd5_crud": crud, "wd5_prepared": prepared,
    "wd5_injection": injection, "wd5_transaction": transaction,
    "wd5_mvc": mvc, "wd5_deploy": deploy,
}

if __name__ == "__main__":
    from subject_DI04007011 import DIAG_DIR
    for name, build in ALL.items():
        with open(os.path.join(DIAG_DIR, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(build())
    print("written", len(ALL))
