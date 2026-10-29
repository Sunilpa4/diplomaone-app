"""Real MySQLi lesson runner: isolated databases on a private MariaDB socket.

No SQL emulation: PHP's mysqlnd/mysqli extensions connect to a real server.
The server is started separately with the process tool; it has no TCP listener.
See setup_mysql_runtime.sh for a repeatable local runtime setup.
"""
import contextlib
import os
import re
import secrets
import subprocess
from php_content import PP, PHP_BIN, PHP_ENV, reflow, run_web

SOCKET = os.environ.get("LESSON_MYSQL_SOCKET", "/tmp/di04007011_mysql/mysql.sock")


def admin_sql(sql):
    if not os.path.exists(SOCKET):
        raise RuntimeError("Start the private practice database first; see tools/setup_mysql_runtime.sh")
    cp = subprocess.run(["mariadb", "--no-defaults", "--socket=" + SOCKET,
                         "-u", "root", "--batch", "--skip-column-names"],
                        input=sql, text=True, capture_output=True, timeout=30)
    if cp.returncode:
        raise RuntimeError("Lesson database setup failed: " + cp.stderr)
    return cp.stdout.strip()


@contextlib.contextmanager
def fresh_database(label="demo", schema=""):
    """Create a new private schema/user, yield PHP environment, then remove both."""
    assert re.fullmatch(r"[a-z0-9_]+", label)
    suffix = secrets.token_hex(5)
    name = "wd5_" + label + "_" + suffix
    user = "lesson_" + suffix
    password = secrets.token_hex(20)
    admin_sql(f"CREATE DATABASE `{name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;\n"
              f"CREATE USER '{user}'@'localhost' IDENTIFIED BY '{password}';\n"
              f"GRANT ALL PRIVILEGES ON `{name}`.* TO '{user}'@'localhost';\n"
              f"GRANT ALL PRIVILEGES ON `{name}_scratch`.* TO '{user}'@'localhost';")
    try:
        if schema:
            admin_sql(f"USE `{name}`;\n" + schema)
        yield {
            "DB_HOST": "localhost", "DB_SOCKET": SOCKET,
            "DB_NAME": name, "DB_USER": user, "DB_PASS": password,
        }
    finally:
        admin_sql(f"DROP DATABASE IF EXISTS `{name}_scratch`;\n"
                  f"DROP DATABASE IF EXISTS `{name}`;\n"
                  f"DROP USER IF EXISTS '{user}'@'localhost';")


def assert_runtime():
    result = subprocess.run([PHP_BIN, "-r", 'echo extension_loaded("mysqli") ? "mysqli OK" : "MISSING";'],
                            env=PHP_ENV, text=True, capture_output=True, timeout=10)
    if result.returncode or "mysqli OK" not in result.stdout:
        raise RuntimeError("mysqli extension missing; run tools/setup_mysql_runtime.sh")
    return admin_sql("SELECT VERSION();")
