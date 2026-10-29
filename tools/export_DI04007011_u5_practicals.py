"""Export runnable Unit 5 practical files from the exact built/shown code, without a DB dependency."""
import json
import os
import re
import zipfile
from pathlib import Path, PurePosixPath
from content_DI04007011_u5_shared import (STUDENTS_SCHEMA, STUDENTS_SEED, CONTACT_SCHEMA,
    CONTACT_SEED, STOCK_SCHEMA, BLOG_SCHEMA, TODO_SCHEMA, INVENTORY_SCHEMA)

ROOT = Path(__file__).resolve().parent.parent
UNIT = ROOT / "content/computer/sem4/DI04007011/unit5.json"
OUTPUT = ROOT / "preview/DI04007011_unit5_practicals.zip"
FOLDERS = ["01-connection", "02-schema-lab", "03-select", "04-insert", "05-update-delete",
           "06-injection-lab-LOCAL-ONLY", "07-transactions", "08-blog", "09-mvc-contacts",
           "10-todo", "11-inventory"]
SCHEMAS = {3: STUDENTS_SEED, 4: STUDENTS_SCHEMA, 5: STUDENTS_SEED, 6: CONTACT_SEED,
           7: STOCK_SCHEMA, 8: BLOG_SCHEMA, 9: CONTACT_SCHEMA, 10: TODO_SCHEMA, 11: INVENTORY_SCHEMA}

README = """# DI04007011 Unit 5 — runnable reference practicals

These files match the code displayed in the Unit 5 lesson. All reference programs
were actually executed using PHP 8.4 mysqlnd/MySQLi and a real MariaDB server.
MySQL-compatible SQL is used. The inventory service has NOT been deployed to an
external host; remote deployment remains a separate practical step.

## Requirements

- A supported PHP 8 release with mysqli + mysqlnd and session support.
- MySQL/MariaDB with InnoDB and the CHECK-constraint support used by the schemas.
- A PHP web server (XAMPP/WAMP/LAMP or PHP's local development server).
- phpMyAdmin or another appropriate administrative SQL client for setup/import.

## Every numbered folder is an INDEPENDENT example

Use a fresh disposable database for each example. Do not import different
students.sql/schema.sql seeds into an already populated students table and assume
IDs/counts will match. Never reset or DROP a real project's database.

1. As an administrator, create a database, for example busbook_blog, with utf8mb4.
2. Create a local account with your own password, for example busbook_app.
3. Import that folder's schema.sql as administrator (if provided).
4. Grant the runtime account SELECT, INSERT, UPDATE, DELETE on that database.
5. Configure DB_HOST, DB_NAME, DB_USER and DB_PASS in the PHP server environment.
   db.php has classroom defaults only; override them with your private settings.
   Plain PHP does NOT automatically load a .env file.
6. Start only the folder you are testing and open its entry point via HTTP.

Example administrative SQL (replace the password, do not commit a real one):

    CREATE DATABASE busbook_blog CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    CREATE USER 'busbook_app'@'localhost' IDENTIFIED BY 'YOUR-OWN-LOCAL-PASSWORD';
    GRANT SELECT, INSERT, UPDATE, DELETE ON busbook_blog.* TO 'busbook_app'@'localhost';

Example Bash local launch without putting the actual DB password in shell history:

    export DB_HOST=localhost DB_NAME=busbook_blog DB_USER=busbook_app
    read -rs -p 'Database password: ' DB_PASS; echo
    export DB_PASS
    php -S localhost:8000 -t 08-blog

Then visit http://localhost:8000/index.php. Adapt the folder and DB_NAME for each
example. On XAMPP/other hosts, use their private Apache/PHP configuration or
hosting environment controls instead. DB_SOCKET is optional and normally unset;
it was only used for the isolated Unix-socket execution harness.

## Entry points

01: connect.php             connection, charset, actual SELECT
02: schema_lab.php          disposable CREATE/ALTER/DROP lab
03: read_students.php       procedural SELECT/fetch
04: insert_students.php     prepared insert/reuse/duplicate handling
05: update_delete.php       targeted prepared writes
06: injection_lab.php       isolated READ-ONLY anti-example; LOCAL ONLY
07: stock_transaction.php   commit/rollback and stock/log consistency
08: index.php               Blog CRUD (Practical 20)
09: index.php               MVC/OOP Contacts (Practical 21)
10: index.php               AI-assisted To-Do reference (Practical 22)
11: index.php               authenticated Inventory (Practical 23)

## Additional rights for example 02 only

It creates `${DB_NAME}_scratch`, not a real production database. An administrator
must grant the lab account suitable CREATE/ALTER/DROP/SELECT privileges on that
scratch schema. For DB_NAME=busbook_schema, the grant target is
`busbook_schema_scratch`.*. Do not give the production CRUD account global DDL
privileges. The lesson also contains equivalent SQL to run in phpMyAdmin directly.

## Inventory administrator configuration

Inventory intentionally has NO built-in default admin password. It requires an
ADMIN_HASH environment value. Generate a hash locally: run the command, then type your chosen password and Enter:

    php -r 'echo password_hash(rtrim(fgets(STDIN), "\\r\\n"), PASSWORD_DEFAULT), PHP_EOL;'

Set the returned hash as ADMIN_HASH in private server configuration, then sign in
with username `admin` and your chosen password. The reference transcript uses a
disposable local-only test password; do not reuse it for hosting. On Unix shells,
quote a pasted hash so its dollar signs are not expanded. Treat the hash as private
configuration. Log in, create/edit/sell/restock/delete, test oversell rejection,
then log out and verify anonymous access no longer shows records.

## Safety and test evidence

- Blog, Contacts and To-Do are LOCAL single-user/admin labs. Add the Unit 4 login
  and authorisation/ownership checks before public or multi-user deployment.
- All four apps use prepared values, escaped HTML, validated IDs, POST + CSRF and
  redirects after successful writes. Inventory also includes an authentication gate.
- Do NOT deploy the connection/DDL/injection diagnostic scripts as public endpoints.
- PHP's development server is for local testing, not a production host.
- `observed-output.txt` contains the lesson's genuine HTTP responses. Random ports,
  session IDs and CSRF tokens vary and are no longer live. The displayed localhost
  command address is normalised for the lesson; use your chosen local server port.
- Those reference observations are not your own journal evidence: run the examples
  yourself and record expected versus observed results, including negative cases.
- For Practical 22, keep your requirement prompt, review/corrections and actual tests.
- For hosting, use the Unit 5 HTTPS, secrets, least-privilege, backup/restore and
  remote smoke-test checklist. Static hosting cannot execute this PHP/MySQLi app.
"""


def main():
    unit = json.loads(UNIT.read_text())
    assert len(FOLDERS) == len(unit["programs"]) == 11
    prefix = "DI04007011_Unit5_Practicals/"
    count = 0
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(prefix + "README.md", README)
        count += 1
        for no, (folder, program) in enumerate(zip(FOLDERS, unit["programs"]), 1):
            chunks = re.split(r"(?m)^<\?php\n// ===== File: (.+) =====\n", program["code"]["en"])
            assert chunks[0] == "", program["id"]
            for i in range(1, len(chunks), 2):
                name = chunks[i]
                assert not PurePosixPath(name).is_absolute() and ".." not in PurePosixPath(name).parts
                source = "<?php\n" + chunks[i + 1].rstrip() + "\n"
                z.writestr(prefix + folder + "/" + name, source)
                count += 1
            if no in SCHEMAS:
                z.writestr(prefix + folder + "/schema.sql", SCHEMAS[no])
                count += 1
            z.writestr(prefix + folder + "/observed-output.txt", program["out"] + "\n")
            count += 1
    print("practical bundle:", OUTPUT, "|", count, "files |", OUTPUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
