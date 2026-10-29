"""DI04007011 Unit 4: genuine multi-request cookie/session demos and PHP exceptions.

Every web transcript uses a real curl cookie jar. Files and requests are exposed
for repeatable behavioral tests; a multi-file code card must be split at its file labels.
"""
from php_content import PP, reflow

SOURCES = {}
DEMO_REQUESTS = {}


def P(pid, title, code, expl="", fname="index.php", request=None, extra=None):
    # Run precisely the reflowed sources that the learner sees.
    code = reflow(code.strip("\n")) + "\n"
    extra = {n: reflow(s.strip("\n")) + "\n" for n, s in (extra or {}).items()}
    SOURCES[pid] = {fname: code, **extra}
    DEMO_REQUESTS[pid] = request
    return PP(pid, title, code, expl, fname=fname, request=request,
              extra=extra, show_extra=bool(extra))


LOGIN_CONFIG = r'''
<?php
// config.php: include BEFORE any HTML or echo.
ini_set("session.use_strict_mode", "1");
ini_set("session.use_only_cookies", "1");
$https = !empty($_SERVER["HTTPS"])
         && $_SERVER["HTTPS"] !== "off";
session_set_cookie_params([
    "lifetime" => 0, "path" => "/",
    "secure" => $https, "httponly" => true,
    "samesite" => "Lax"
]);
session_start();
$_SESSION["csrf"] ??= bin2hex(random_bytes(16));

function e(string $s): string {
    return htmlspecialchars(
        $s, ENT_QUOTES | ENT_SUBSTITUTE, "UTF-8"
    );
}
function valid_csrf(): bool {
    $token = $_POST["csrf"] ?? null;
    return is_string($token)
        && hash_equals($_SESSION["csrf"], $token);
}
'''

LOGIN = r'''
<?php
require __DIR__ . "/config.php";
$error = "";
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (!valid_csrf()) {
        http_response_code(403);
        exit("Invalid CSRF token.");
    }
    $user = $_POST["username"] ?? "";
    $pass = $_POST["password"] ?? "";
    // Lab account only: ravi / demo@123.
    // Unit 5 replaces this with a database hash.
    $hash = password_hash("demo@123", PASSWORD_DEFAULT);
    if (is_string($user) && is_string($pass)
        && $user === "ravi"
        && password_verify($pass, $hash)) {
        session_regenerate_id(true);
        $_SESSION["user"] = "Ravi Patel";
        $_SESSION["csrf"] = bin2hex(random_bytes(16));
        header("Location: dashboard.php", true, 303);
        exit;
    }
    $error = "Invalid username or password.";
}
?>
<h2>BusBook Login</h2>
<p><?= e($error) ?></p>
<form method="post">
  <input type="hidden" name="csrf" value="<?= e($_SESSION['csrf']) ?>">
  Username: <input name="username" required><br>
  Password: <input type="password" name="password" required><br>
  <button>Log in</button>
</form>
'''

DASHBOARD = r'''
<?php
require __DIR__ . "/config.php";
if (!isset($_SESSION["user"])) {
    header("Location: login.php", true, 303);
    exit;
}
?>
<h2>Protected Dashboard</h2>
<p>Welcome, <?= e($_SESSION["user"]) ?>!</p>
<form method="post" action="logout.php">
  <input type="hidden" name="csrf" value="<?= e($_SESSION['csrf']) ?>">
  <button>Log out</button>
</form>
'''

LOGOUT = r'''
<?php
require __DIR__ . "/config.php";
if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    header("Allow: POST");
    http_response_code(405);
    exit("Use the logout button.");
}
if (!valid_csrf()) {
    http_response_code(403);
    exit("Invalid CSRF token.");
}
$_SESSION = [];
$p = session_get_cookie_params();
setcookie(session_name(), "", [
    "expires" => time() - 3600,
    "path" => $p["path"], "domain" => $p["domain"],
    "secure" => $p["secure"],
    "httponly" => $p["httponly"],
    "samesite" => $p["samesite"] ?? "Lax"
]);
session_destroy();
header("Location: login.php", true, 303);
exit;
'''

CSRF_PATTERN = r'name="csrf" value="([a-f0-9]+)"'

PROGRAMS = [
    P("wd4p1", "Create, read and update a cookie (Practical 17)", r'''
<?php
$incoming = $_COOKIE["city"] ?? "(missing)";
$queued = null;
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $city = $_POST["city"] ?? "";
    if (!in_array($city, ["Surat", "Vadodara"], true)) {
        http_response_code(400);
        exit("Choose a listed city.");
    }
    setcookie("city", $city, [
        "expires" => time() + 3600, "path" => "/",
        "httponly" => true, "samesite" => "Lax"
    ]);
    $queued = $city;
}
header("Content-Type: text/plain; charset=UTF-8");
echo "Incoming city: $incoming\n";
if ($queued !== null) {
    echo "Queued for NEXT request: $queued\n";
}
''',
      """<p>A response's <code>Set-Cookie</code> header asks the browser to save a value; only a <b>later request</b> returns it in <code>$_COOKIE</code>. Updating uses the same name and path. Four genuine requests show missing &rarr; Surat &rarr; incoming Surat while queuing Vadodara &rarr; Vadodara. The shared <code>-b/-c cookies.txt</code> file is curl's browser memory. On production HTTPS also set <code>secure =&gt; true</code>; these local HTTP demos omit it.</p>""",
      fname="city.php", request=[
          {"label": "1. First response queues a cookie; incoming array is still empty", "method": "POST", "data": {"city": "Surat"}, "show_headers": True},
          {"label": "2. Browser returns the saved cookie"},
          {"label": "3. Updating does not rewrite this request's cookie array", "method": "POST", "data": {"city": "Vadodara"}},
          {"label": "4. The updated value arrives on the next request"},
      ]),

    P("wd4p2", "Remember a theme preference with a cookie (Practical 17)", r'''
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $choice = $_POST["theme"] ?? "";
    if (!in_array($choice, ["light", "dark"], true)) {
        http_response_code(400);
        exit("Invalid theme.");
    }
    setcookie("theme", $choice, [
        "expires" => time() + 30 * 86400,
        "path" => "/", "httponly" => true,
        "samesite" => "Lax"
    ]);
    header("Location: theme.php", true, 303);
    exit;
}
$theme = $_COOKIE["theme"] ?? "light";
if (!in_array($theme, ["light", "dark"], true)) {
    $theme = "light";
}
$bg = $theme === "dark" ? "#172033" : "#ffffff";
$fg = $theme === "dark" ? "#ffffff" : "#172033";
?>
<body style="background:<?= $bg ?>;color:<?= $fg ?>">
<h2>BusBook: <?= $theme ?> theme</h2>
<form method="post">
  <select name="theme">
    <option value="light">Light</option>
    <option value="dark">Dark</option>
  </select>
  <button>Remember for 30 days</button>
</form>
</body>
''',
      """<p>A working preference form, not an authentication cookie. POST validates an allowlisted theme, sets a persistent cookie, then redirects (303) to a fresh GET. The GET sees the new cookie without manually changing <code>$_COOKIE</code>. Re-check incoming cookie values too: the client can edit them. Another browser with no jar still sees the default light theme.</p>""",
      fname="theme.php", request=[
          {"label": "1. New visitor: default light theme"},
          {"label": "2. Save dark; follow the redirect to render the next GET", "method": "POST", "data": {"theme": "dark"}, "follow_redirects": True},
          {"label": "3. Return visit in the same browser: still dark"},
          {"label": "4. Separate browser without cookies: light", "cookies": False},
      ]),

    P("wd4p3", "Delete a cookie using the matching path", r'''
<?php
$old = $_COOKIE["demo"] ?? "(missing)";
$action = $_POST["action"] ?? "read";
$options = [
    "path" => "/", "httponly" => true,
    "samesite" => "Lax"
];
if ($action === "set") {
    setcookie("demo", "BusBook", [
        "expires" => time() + 3600, ...$options
    ]);
} elseif ($action === "clear") {
    setcookie("demo", "", [
        "expires" => time() - 3600, ...$options
    ]);
}
header("Content-Type: text/plain; charset=UTF-8");
echo "Action: $action\n";
echo "Incoming demo: $old\n";
if ($action === "clear") {
    echo "Deletion queued; the next request proves it.\n";
}
''',
      """<p>Cookie identity includes <b>name, domain and path</b>. Expire that same cookie in the past; <code>unset($_COOKIE['demo'])</code> alone would only change a PHP array for one request. The clear response still prints the incoming old value, then the next GET prints missing. Its genuine header shows an expired cookie with <code>Max-Age=0</code>.</p>""",
      fname="clear_cookie.php", request=[
          {"label": "1. Store the cookie", "method": "POST", "data": {"action": "set"}},
          {"label": "2. Confirm it returned"},
          {"label": "3. Expire the same name/path cookie", "method": "POST", "data": {"action": "clear"}, "show_headers": True},
          {"label": "4. Browser no longer sends it"},
      ]),

    P("wd4p4", "Session data across two pages (Practical 16)", r'''
<?php
session_start();
$_SESSION["visits"] = ($_SESSION["visits"] ?? 0) + 1;
$_SESSION["seats"] ??= 0;
if ($_SERVER["REQUEST_METHOD"] === "POST"
    && ($_POST["add"] ?? "") === "seat") {
    $_SESSION["seats"]++;
}
header("Content-Type: text/plain; charset=UTF-8");
echo "Booking-page visits: ", $_SESSION["visits"], "\n";
echo "Reserved seats: ", $_SESSION["seats"], "\n";
echo "Open cart.php to read the same session.\n";
''',
      """<p>Save each labelled section as its own file. Every participating page calls <code>session_start()</code> before output. PHP sends a random session ID cookie, while <code>visits</code> and <code>seats</code> stay server-side. The cart page resumes the same record using that ID; a fresh browser has no seat reservation. This is a state demonstration, not an actual payment or inventory system.</p>""",
      fname="booking.php", extra={"cart.php": r'''
<?php
session_start();
header("Content-Type: text/plain; charset=UTF-8");
echo "Cart reads visits: ", $_SESSION["visits"] ?? 0, "\n";
echo "Cart reads seats: ", $_SESSION["seats"] ?? 0, "\n";
'''}, request=[
          {"label": "1. First booking-page visit"},
          {"label": "2. Add a seat using the same session", "method": "POST", "data": {"add": "seat"}},
          {"label": "3. Another PHP page reads the saved values", "path": "cart.php"},
          {"label": "4. A different browser has its own empty cart", "path": "cart.php", "cookies": False},
      ]),

    P("wd4p5", "unset, session_unset and full session destruction", r'''
<?php
session_start();
$action = $_POST["action"] ?? "read";
if ($action === "set") {
    $_SESSION["user"] = "Ravi";
    $_SESSION["theme"] = "dark";
} elseif ($action === "remove-theme") {
    unset($_SESSION["theme"]);
} elseif ($action === "clear-values") {
    session_unset();
} elseif ($action === "destroy") {
    $_SESSION = [];
    if (ini_get("session.use_cookies")) {
        $p = session_get_cookie_params();
        setcookie(session_name(), "", [
            "expires" => time() - 3600,
            "path" => $p["path"],
            "domain" => $p["domain"],
            "secure" => $p["secure"],
            "httponly" => $p["httponly"],
            "samesite" => $p["samesite"] ?? "Lax"
        ]);
    }
    session_destroy();
}
header("Content-Type: text/plain; charset=UTF-8");
echo "Action: $action\n";
echo "User: ", $_SESSION["user"] ?? "(none)", "\n";
echo "Theme: ", $_SESSION["theme"] ?? "(none)", "\n";
echo "Active session: ",
     session_status() === PHP_SESSION_ACTIVE ? "yes" : "no",
     "\n";
''',
      """<p>Three different operations: <code>unset</code> removes one key; <code>session_unset()</code> clears all variables but leaves the session active; full logout clears <code>$_SESSION</code>, expires the session cookie using its original parameters, and calls <code>session_destroy()</code> to remove server-side data. The final request starts a <b>new empty session</b>, not the old user's record.</p>""",
      fname="session_tools.php", request=[
          {"label": "1. Seed two session variables", "method": "POST", "data": {"action": "set"}},
          {"label": "2. Remove only the theme; keep the user", "method": "POST", "data": {"action": "remove-theme"}},
          {"label": "3. Clear all values, but the session remains active", "method": "POST", "data": {"action": "clear-values"}},
          {"label": "4. Seed again before full logout", "method": "POST", "data": {"action": "set"}},
          {"label": "5. Clear values, expire cookie and destroy server data", "method": "POST", "data": {"action": "destroy"}, "show_headers": True},
          {"label": "6. Next visit begins with an empty session"},
      ]),

    P("wd4p6", "Multi-page protected login and logout (Practical 16)", LOGIN,
      """<p><b>Save four separate files:</b> login.php, config.php, dashboard.php and logout.php in one folder. Demo credentials: <code>ravi / demo@123</code>. The sample hash is generated from that lab password; real applications store a previously generated hash in the database, never hard-code real credentials.</p><p>The config starts a strict, cookie-only session before HTML. Login checks a CSRF token and <code>password_verify()</code>, regenerates the session ID on success, stores the user's name, then redirects. Dashboard checks authentication on <b>every</b> request; logout only accepts a valid-token POST, clears server state and expires the cookie. Secure is enabled automatically on direct HTTPS; configure it explicitly for your deployment if HTTPS terminates at a proxy.</p><p>The transcript proves guest denied &rarr; wrong password denied &rarr; correct password accepted &rarr; dashboard visible &rarr; logout &rarr; dashboard denied again. CSRF tokens are extracted from the actual forms for subsequent curl submissions. Random IDs and tokens change each run.</p>""",
      fname="login.php", extra={"config.php": LOGIN_CONFIG, "dashboard.php": DASHBOARD, "logout.php": LOGOUT},
      request=[
          {"label": "1. Guest requests the protected page: redirect to login", "path": "dashboard.php", "show_headers": True},
          {"label": "2. Open the form and read its CSRF token", "capture": {"csrf": CSRF_PATTERN}},
          {"label": "3. Wrong password: no authenticated session", "method": "POST", "data": {"username": "ravi", "password": "wrong", "csrf": "{{csrf}}"}, "capture": {"csrf": CSRF_PATTERN}},
          {"label": "4. Correct password: rotate ID and redirect", "method": "POST", "data": {"username": "ravi", "password": "demo@123", "csrf": "{{csrf}}"}, "show_headers": True},
          {"label": "5. Same browser can now open the dashboard", "path": "dashboard.php", "capture": {"csrf": CSRF_PATTERN}},
          {"label": "6. Log out with the dashboard's fresh CSRF token", "path": "logout.php", "method": "POST", "data": {"csrf": "{{csrf}}"}, "show_headers": True},
          {"label": "7. Direct dashboard access is denied again", "path": "dashboard.php", "show_headers": True},
      ]),

    P("wd4p7", "try, throw, catch and finally: fare division (Practical 18)", r'''
<?php
function farePerPassenger(float $total, int $count): float {
    if ($count <= 0) {
        throw new InvalidArgumentException(
            "Passenger count must be positive."
        );
    }
    return $total / $count;
}
foreach ([3, 0] as $count) {
    echo "Passengers: $count\n";
    try {
        echo "  checking...\n";
        $fare = farePerPassenger(900, $count);
        echo "  Fare each: Rs $fare\n";
        echo "  this line runs only on success\n";
    } catch (InvalidArgumentException $e) {
        echo "  Rejected: ", $e->getMessage(), "\n";
    } finally {
        echo "  finally: request finished\n";
    }
    echo "  continues after try/catch\n\n";
}
''',
      """<p>Normal case: all try statements run, catch is skipped, finally runs. Zero-passenger case: the function <code>throw</code>s before dividing; the remaining try statements are skipped, the matching catch handles the exception, and finally still runs. The outer loop then continues. This deliberately throws an <code>InvalidArgumentException</code>; an unguarded PHP division by zero instead raises a <code>DivisionByZeroError</code>.</p>"""),

    P("wd4p8", "Custom exception and specific-first catches (Practical 18)", r'''
<?php
class SeatsUnavailable extends RuntimeException {}

function reserveSeats(int $wanted, int $available): string {
    if ($wanted <= 0) {
        throw new InvalidArgumentException(
            "Request at least one seat."
        );
    }
    if ($wanted > $available) {
        throw new SeatsUnavailable(
            "Only $available seats remain; wanted $wanted."
        );
    }
    return "Reserved $wanted seats.";
}
foreach ([2, 0, 5] as $wanted) {
    echo "Want $wanted:\n";
    try {
        $result = reserveSeats($wanted, 3);
        echo "  $result\n";
    } catch (SeatsUnavailable $e) {
        echo "  Availability: ", $e->getMessage(), "\n";
    } catch (InvalidArgumentException $e) {
        echo "  Input: ", $e->getMessage(), "\n";
    } catch (Exception $e) {
        echo "  Unexpected: ", $e->getMessage(), "\n";
    } finally {
        echo "  Booking attempt finished.\n\n";
    }
}
''',
      """<p>A domain-specific class (<code>SeatsUnavailable extends RuntimeException</code>) lets the caller distinguish sold-out routes from bad input. Catch specific types <b>before</b> a parent such as Exception: only the first matching catch executes. A broad parent placed first would swallow the custom case. In production, log internal failures and show a safe generic message rather than exposing paths or stack traces.</p>"""),

    P("wd4p9", "finally closes a file on success and failure", r'''
<?php
function readManifest(string $path, bool $reject): void {
    $h = null;
    try {
        if (!is_readable($path)) {
            throw new RuntimeException("Manifest unavailable.");
        }
        $h = fopen($path, "r");
        if ($h === false) {
            throw new RuntimeException("Cannot open manifest.");
        }
        echo "  File opened.\n";
        if ($reject) {
            throw new RuntimeException("Manifest failed validation.");
        }
        echo "  Passenger: ", trim(fgets($h)), "\n";
    } catch (RuntimeException $e) {
        echo "  Handled: ", $e->getMessage(), "\n";
    } finally {
        if (is_resource($h)) {
            fclose($h);
            echo "  finally: file closed\n";
        } else {
            echo "  finally: no open handle\n";
        }
    }
}
$file = __DIR__ . "/manifest.txt";
file_put_contents($file, "Ravi Patel\n");
echo "1. Success\n";
readManifest($file, false);
echo "2. Failure AFTER open\n";
readManifest($file, true);
echo "3. Failure BEFORE open\n";
readManifest(__DIR__ . "/missing.txt", false);
unlink($file);
''',
      """<p>One cleanup path for three genuine cases: normal read, exception after opening, and missing file before opening. Initialise the handle, test <code>is_resource()</code>, and close in <code>finally</code>. Many file functions warn/return false rather than throwing; test the return and throw deliberately when your application needs exception flow. <code>finally</code> normally runs even with return or a propagated exception, but not after <code>exit()</code> or process termination.</p>"""),

    P("wd4p10", "Exception vs Error: catching Throwable in modern PHP", r'''
<?php
declare(strict_types=1);

function doubleSeats(int $n): int {
    return $n * 2;
}
$jobs = [
    "App exception" => function () {
        throw new RuntimeException("Payment service unavailable.");
    },
    "Division error" => function () {
        return 10 / 0;
    },
    "Type error" => function () {
        return doubleSeats("two");
    },
];
foreach ($jobs as $label => $job) {
    echo "$label:\n";
    try {
        $job();
    } catch (Exception $e) {
        echo "  Exception branch: ", get_class($e), "\n";
    } catch (Error $e) {
        echo "  Error branch: ", get_class($e), "\n";
    } finally {
        echo "  cleaned up\n";
    }
}
echo "Broad handler:\n";
try {
    doubleSeats("two");
} catch (Throwable $t) {
    echo "  Throwable also catches ", get_class($t), "\n";
}
''',
      """<p>PHP 7+ has two throwable families: application <code>Exception</code> and engine <code>Error</code> (including TypeError and DivisionByZeroError). Both implement <code>Throwable</code>. <code>catch (Exception $e)</code> does not catch an Error; <code>catch (Throwable $t)</code> can handle either. Ordinary warnings/notices are <b>not automatically exceptions</b>. Handle expected failures close to the cause; a broad Throwable handler is a last safety boundary, not a reason to ignore programming bugs.</p>"""),
]
