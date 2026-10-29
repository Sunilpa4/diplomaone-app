"""Shared, fully shown PHP files and SQL schemas for the Unit 5 practicals."""

DB_PHP = r'''
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$host = getenv("DB_HOST") ?: "localhost";
$user = getenv("DB_USER") ?: "busbook_app";
$pass = getenv("DB_PASS");
if ($pass === false) {
    $pass = "change-this-lab-password";
}
$name = getenv("DB_NAME") ?: "busbook";
$socket = getenv("DB_SOCKET") ?: null;
try {
    $db = new mysqli($host, $user, $pass, $name, 3306, $socket);
    $db->set_charset("utf8mb4");
} catch (mysqli_sql_exception $e) {
    error_log($e->getMessage());
    http_response_code(500);
    exit("Database unavailable. Check server configuration.");
}
'''

WEB_PHP = r'''
<?php
require_once __DIR__ . "/db.php";
set_exception_handler(function (Throwable $e): void {
    error_log($e->getMessage());
    http_response_code(500);
    echo "Operation failed. Check the server log.";
});
ini_set("session.use_strict_mode", "1");
ini_set("session.use_only_cookies", "1");
$https = !empty($_SERVER["HTTPS"])
         && $_SERVER["HTTPS"] !== "off";
session_set_cookie_params([
    "path" => "/", "secure" => $https,
    "httponly" => true, "samesite" => "Lax"
]);
session_start();
$_SESSION["csrf"] ??= bin2hex(random_bytes(16));
function e(string $s): string {
    return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, "UTF-8");
}
function text(array $source, string $key): string {
    $v = $source[$key] ?? "";
    return is_string($v) ? trim($v) : "";
}
function fail(string $message, int $status = 400): void {
    http_response_code($status);
    exit(e($message));
}
function recordId($raw): int {
    $id = filter_var($raw, FILTER_VALIDATE_INT, [
        "options" => ["min_range" => 0]
    ]);
    if ($id === false) {
        fail("Invalid record ID.");
    }
    return $id;
}
function positiveId($raw): int {
    $id = recordId($raw);
    if ($id < 1) {
        fail("Invalid record ID.");
    }
    return $id;
}
function csrf_field(): string {
    return '<input type="hidden" name="csrf" value="'
           . e($_SESSION["csrf"]) . '">';
}
function check_csrf(): void {
    $token = $_POST["csrf"] ?? null;
    if (!is_string($token)
        || !hash_equals($_SESSION["csrf"], $token)) {
        fail("Invalid CSRF token.", 403);
    }
}
function redirect(string $message = ""): void {
    $_SESSION["flash"] = $message;
    header("Location: index.php", true, 303);
    exit;
}
function page(string $title): void {
    echo '<!doctype html><meta charset="utf-8">';
    echo '<title>', e($title), '</title>';
    echo '<style>body{font:16px system-ui;max-width:840px;';
    echo 'margin:24px auto;padding:12px}article{border:1px solid #ccc;';
    echo 'padding:12px;margin:12px 0}form{margin:10px 0}';
    echo 'input,textarea,button,select{font:inherit;margin:4px}';
    echo 'textarea{display:block;width:95%}</style>';
    echo '<h1>', e($title), '</h1>';
    $flash = $_SESSION["flash"] ?? "";
    unset($_SESSION["flash"]);
    if ($flash !== "") {
        echo '<p role="status">', e($flash), '</p>';
    }
}
if (!in_array($_SERVER["REQUEST_METHOD"], ["GET", "POST"], true)) {
    header("Allow: GET, POST");
    fail("Method not allowed.", 405);
}
'''

STUDENTS_SCHEMA = '''CREATE TABLE students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(80) NOT NULL,
  email VARCHAR(120) NOT NULL UNIQUE,
  city VARCHAR(40) NOT NULL,
  marks INT NOT NULL CHECK (marks BETWEEN 0 AND 100)
) ENGINE=InnoDB;
'''
STUDENTS_SEED = STUDENTS_SCHEMA + '''INSERT INTO students(name,email,city,marks) VALUES
('Ravi Patel','ravi@example.test','Surat',82),
('Asha Shah','asha@example.test','Vadodara',91),
('Mihir Desai','mihir@example.test','Surat',75);
'''

CONTACT_SCHEMA = '''CREATE TABLE contacts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(80) NOT NULL,
  email VARCHAR(120) NOT NULL
) ENGINE=InnoDB;
'''
CONTACT_SEED = CONTACT_SCHEMA + '''INSERT INTO contacts(name,email) VALUES
('Ravi','ravi@example.test'),
('Asha','asha@example.test'),
('O''Neil','oneil@example.test');
'''

STOCK_SCHEMA = '''CREATE TABLE stock (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(80) NOT NULL,
  qty INT NOT NULL CHECK (qty >= 0)
) ENGINE=InnoDB;
CREATE TABLE movements (
  id INT PRIMARY KEY AUTO_INCREMENT,
  stock_id INT NOT NULL,
  delta INT NOT NULL,
  FOREIGN KEY (stock_id) REFERENCES stock(id)
) ENGINE=InnoDB;
INSERT INTO stock(name,qty) VALUES ('USB Cable',5);
'''

BLOG_SCHEMA = '''CREATE TABLE posts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  body TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
'''
TODO_SCHEMA = '''CREATE TABLE todos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(150) NOT NULL,
  done TINYINT NOT NULL DEFAULT 0 CHECK (done IN (0,1))
) ENGINE=InnoDB;
'''
INVENTORY_SCHEMA = '''CREATE TABLE products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  sku VARCHAR(30) NOT NULL UNIQUE,
  name VARCHAR(80) NOT NULL,
  qty INT NOT NULL DEFAULT 0 CHECK (qty BETWEEN 0 AND 1000000),
  price DECIMAL(10,2) NOT NULL CHECK (price >= 0)
) ENGINE=InnoDB;
'''

CSRF_PATTERN = r'name="csrf" value="([a-f0-9]+)"'
