"""DI04007011 Unit 4: Cookies, Sessions and Exception Handling (10 h, 15%). English only."""
from php_content import make_TP

SN = {
    "cookie_basic": r'''
<?php
// Before HTML, echo or other output:
setcookie("city", "Surat", [
    "expires" => time() + 3600,
    "path" => "/",
    "httponly" => true,
    "samesite" => "Lax"
]);
// New value arrives on the NEXT request:
$city = $_COOKIE["city"] ?? "not selected";
echo htmlspecialchars($city);
''',
    "cookie_delete": r'''
<?php
// Use the SAME name, path and domain as creation.
setcookie("city", "", [
    "expires" => time() - 3600,
    "path" => "/",
    "httponly" => true,
    "samesite" => "Lax"
]);
// Browser stops sending it on the next request.
''',
    "session_basic": r'''
<?php
session_start();  // before output, on EACH page
$_SESSION["user"] = "Ravi";
$_SESSION["seats"] = 2;
// On another page, after session_start():
echo htmlspecialchars($_SESSION["user"] ?? "Guest");
''',
    "session_end": r'''
<?php
session_start();
unset($_SESSION["theme"]); // one key only
// Full logout is a DIFFERENT operation:
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
''',
    "page_guard": r'''
<?php
session_start();
if (!isset($_SESSION["user"])) {
    header("Location: login.php", true, 303);
    exit; // never render the protected body
}
// Only authenticated requests reach this line.
''',
    "exceptions": r'''
<?php
try {
    if ($count <= 0) {
        throw new InvalidArgumentException(
            "Count must be positive."
        );
    }
    echo $total / $count;
} catch (InvalidArgumentException $e) {
    echo htmlspecialchars($e->getMessage());
} finally {
    // Close resources here; avoid return/exit.
}
''',
    "custom_exception": r'''
<?php
class SeatsUnavailable extends RuntimeException {}
try {
    throw new SeatsUnavailable("Route is full.");
} catch (SeatsUnavailable $e) {
    echo "Choose another departure.";
} catch (Exception $e) {
    // Broad parent comes LAST, not first.
    error_log($e->getMessage());
    echo "Booking could not be completed.";
}
''',
}
T = make_TP(SN)

SEC_4_1 = {
    "title": {"en": "4.1 Working with Cookies (Practical 17)"},
    "items": [
        T("Stateless HTTP and the Cookie Round Trip", """
<p><b>HTTP is stateless:</b> one request does not automatically remember what happened on the previous page. Cookies and sessions add continuity for preferences, shopping carts and login.</p>
<ul><li>A <b>cookie</b> is a small name/value record stored by the browser for a site. PHP sends a <code>Set-Cookie</code> response header; the browser later sends the applicable value in a <code>Cookie</code> request header.</li>
<li><code>setcookie()</code> queues that response header. <code>$_COOKIE</code> describes the <b>incoming</b> request, so it is not automatically updated by the call. Read the new value after a reload or redirect.</li>
<li>Cookie values are strings; PHP can encode/decode them for HTTP transport. They are <b>not encrypted</b> by setcookie, and the user can inspect, edit, block or delete them.</li>
<li>Run cookie programs through <code>http://localhost/...</code> under XAMPP or <code>php -S localhost:8000</code>, not by opening the PHP file directly. The CLI alone has no browser to store and return a cookie.</li>
<li>Our verified transcripts use <code>curl -b cookies.txt -c cookies.txt</code>: read incoming cookies from a jar and save response cookies back to that same jar.</li></ul>
""", diagram="wd4_cookie_roundtrip", programs=["wd4p1"]),
        T("Creating, Reading, Updating and Destroying Cookies", """
<p>The options-array form is <code>setcookie($name, $value, $options)</code>. The older positional form supplies expiry, path, domain, secure and httponly separately; the options array is clearer and also supports SameSite.</p>
@@cookie_basic@@
<ul><li><b>Create:</b> give the cookie a name, string value, expiry and scope. <code>time() + 3600</code> is an absolute timestamp one hour from now, not a duration by itself.</li>
<li><b>Read:</b> use <code>$_COOKIE['city'] ?? 'default'</code> or an <code>isset</code> check. Missing cookies are normal, not a reason for an undefined-key warning.</li>
<li><b>Update:</b> set the same <b>name/domain/path</b> again with a new value and expiry. A different path may create a second cookie rather than replace the first.</li>
<li><b>Delete:</b> set that same cookie with an expiry in the past. <code>unset($_COOKIE['city'])</code> only removes an entry from this script's array; it sends no deletion instruction to the browser.</li>
<li><b>Before output:</b> setcookie, header and session-start operations must precede HTML, echo and accidental whitespace/BOM output. A true return from setcookie means the header was queued, not that the browser accepted it.</li></ul>
@@cookie_delete@@
""", diagram="wd4_cookie_lifecycle", programs=["wd4p3"]),
        T("Cookie Lifetime, Scope and Safe Preferences", """
<table><tr><th>Option</th><th>Purpose and practical rule</th></tr>
<tr><td>expires</td><td>Future timestamp = persistent cookie, subject to browser policy; 0/omitted = browser-session cookie. Browser session restore may preserve session cookies.</td></tr>
<tr><td>path</td><td>URL paths that receive the cookie. Use / for a whole-site preference. A path is routing scope, not a security boundary.</td></tr>
<tr><td>domain</td><td>Omit for host-only scope. Set a wider domain only if subdomain sharing is actually needed.</td></tr>
<tr><td>secure</td><td>Send over HTTPS only. Enable for production HTTPS; these local plain-HTTP examples do not require Secure.</td></tr>
<tr><td>httponly</td><td>Stops JavaScript from reading the cookie through document.cookie; it does not eliminate every XSS attack.</td></tr>
<tr><td>samesite</td><td>Lax/Strict/None controls cross-site sending. None requires Secure. SameSite is useful defence-in-depth, not a replacement for CSRF tokens.</td></tr></table>
<ul><li>Good cookie data: <b>language, theme, last selected city</b>. Bad data: passwords, trusted roles, bank balances or an unprotected login flag.</li>
<li>Browsers impose small per-cookie limits (roughly 4 KB, including overhead) and other count/size policies. Do not use cookies as a large database.</li>
<li>Validate every received value against an allowlist. A theme form should accept only <code>light</code>/<code>dark</code>, even if the normal HTML dropdown offers only those choices.</li>
<li><b>Post/Redirect/Get:</b> process POST, set the cookie, send a 303 Location header, exit; the redirected GET can read the newly returned cookie.</li></ul>
""", diagram="wd4_cookie_flags", programs=["wd4p2"]),
    ],
}

SEC_4_2 = {
    "title": {"en": "4.2 Working with Sessions (Practical 16)"},
    "items": [
        T("Creating a Session and Sharing Data Between Pages", """
<p>A <b>PHP session</b> stores per-visitor data on the server and normally uses a browser cookie, typically <code>PHPSESSID</code>, to carry an opaque session ID. The ID is a lookup key, not the session's user/cart data.</p>
@@session_basic@@
<ul><li><code>session_start()</code> creates a session or resumes an existing one using the incoming ID; call it <b>before output on every participating page</b>. Calling it on a second page does not necessarily start a new visitor.</li>
<li>Set variables with <code>$_SESSION['key'] = $value</code>. Unlike cookie values, session data can contain arrays, numbers and other serialisable application values.</li>
<li>After starting the session, another page reads the same keys. Use <code>??</code> defaults or <code>isset</code> for first visits and logged-out users.</li>
<li>PHP's default handler stores data in server-side files; deployments may use a database or another session store. The browser receives only the identifier unless your application explicitly sends more.</li>
<li>Two browsers with different IDs normally have different sessions. A new incognito window is useful for testing isolation.</li>
<li>With a cookie-only configuration, a client that refuses the session cookie cannot retain the same session across separate requests. Do not put session IDs into URLs as a workaround.</li></ul>
""", diagram="wd4_session_roundtrip", programs=["wd4p4"]),
        T("Removing Session Variables and Destroying a Session", """
<table><tr><th>Operation</th><th>What it actually does</th></tr>
<tr><td>unset($_SESSION['theme'])</td><td>Removes only that key; user/cart and the session remain.</td></tr>
<tr><td>session_unset() or $_SESSION = []</td><td>Clears all variables in the active session, not the browser cookie or the session identity.</td></tr>
<tr><td>session_destroy()</td><td>Destroys the server-side session data. It does not itself clear the current $_SESSION array or remove the browser's session cookie.</td></tr></table>
<p><b>Complete logout:</b> start/resume the session, clear the in-memory data, expire its cookie with matching scope, destroy the server-side record, then redirect and exit.</p>
@@session_end@@
<ul><li>Do not confuse <code>session_regenerate_id(true)</code> with logout: it rotates the identifier while preserving current session values and invalidates the old session record.</li>
<li>Do not rely on closing the browser for authentication expiry. Cookies can be restored, and old server-side data may survive until garbage collection.</li>
<li>Real applications enforce idle/absolute expiry explicitly using timestamps stored in the session. If expired, perform the same full logout and require authentication again.</li>
<li>The verified program separately demonstrates one-key removal, clearing all values while the session stays active, and complete destruction followed by a new empty visit.</li></ul>
""", programs=["wd4p5"]),
        T("Protected Login, Session Fixation Defence and Logout", """
<p><b>Practical 16</b> requires more than storing a name: an unauthenticated visitor must not be able to open a protected page, even by typing its URL directly.</p>
<ol><li><b>Common config:</b> enable strict mode and cookie-only IDs, set cookie parameters, then call session_start before any output.</li>
<li><b>Login:</b> accept a POST, verify its CSRF token, validate credentials using a password hash and <code>password_verify</code>. Never trust a hidden field or a cookie saying <code>logged_in=1</code>.</li>
<li><b>Success:</b> call <code>session_regenerate_id(true)</code> to reduce session-fixation risk, store a user ID/name in <code>$_SESSION</code>, then redirect to the dashboard.</li>
<li><b>Guard:</b> check the server-side authentication key on <em>every</em> protected request, before producing any private content. Redirect and <code>exit</code> if it is missing.</li>
<li><b>Logout:</b> use a POST with a valid CSRF token; clear variables, expire the session cookie, destroy the session, redirect to login and exit.</li></ol>
@@page_guard@@
<ul><li><b>CSRF token:</b> a random server-generated value stored in the session and echoed into the form. Compare it with <code>hash_equals</code> on submission. It helps reject a forged request from another site.</li>
<li><b>Session fixation</b> means making a victim authenticate under an attacker-known ID. Strict mode rejects uninitialised IDs, and regeneration changes the ID after login.</li>
<li><b>Session hijacking</b> means stealing a valid ID. HTTPS, Secure/HttpOnly cookies, suitable SameSite policy and prompt logout help; sessions are not automatically secure just because data lives on the server.</li>
<li><b>Run the program:</b> save its four labelled sections as <code>login.php</code>, <code>config.php</code>, <code>dashboard.php</code> and <code>logout.php</code>. Open login.php through the server; lab credentials are <code>ravi / demo@123</code>. Database-backed credentials arrive in Unit 5.</li></ul>
""", diagram="wd4_login_flow", programs=["wd4p6"]),
        T("Cookies vs Sessions: Choosing the Right Storage", """
<table><tr><th>Aspect</th><th>Cookie value</th><th>PHP session data</th></tr>
<tr><td>Stored at</td><td>Browser</td><td>Server-side session store</td></tr>
<tr><td>Sent with request</td><td>Applicable cookie's value</td><td>Normally an opaque ID in a cookie</td></tr>
<tr><td>Typical capacity</td><td>Small per-cookie browser limit</td><td>Governed by server storage/configuration</td></tr>
<tr><td>Lifetime</td><td>Expiry and browser policy</td><td>Application expiry, storage lifetime and garbage collection</td></tr>
<tr><td>Trust</td><td>Client may edit the value</td><td>Server controls stored values, but the ID can still be stolen</td></tr>
<tr><td>Best use</td><td>Theme/language preference</td><td>Authenticated user, cart, temporary workflow data</td></tr></table>
<ul><li>They are related mechanisms, not mutually exclusive alternatives: PHP sessions <b>usually use a cookie</b> for the session identifier.</li>
<li>A persistent preference cookie can survive longer than an authenticated session without keeping the visitor logged in.</li>
<li>A secure persistent remember-me login needs carefully designed expiring, revocable tokens; it is not a plaintext username/password cookie.</li>
<li>Both fail if the application exposes private data in HTML without checking access. Server-side storage is one part of security, not the whole design.</li></ul>
""", diagram="wd4_cookie_vs_session"),
    ],
}

SEC_4_3 = {
    "title": {"en": "4.3 Exception Handling (Practical 18)"},
    "items": [
        T("try, throw, catch and finally: The Control Flow", """
<p>An <b>exception</b> is an object reporting a failure that interrupts normal execution. Instead of checking a return code at every nested call, code can throw an exception and let a suitable caller handle it.</p>
@@exceptions@@
<ul><li><b>try:</b> surround operations that may throw. A try requires at least a catch or a finally.</li>
<li><b>throw:</b> throw an exception object such as <code>new InvalidArgumentException('bad count')</code>. It immediately skips remaining statements in the try and searches outward for a matching catch.</li>
<li><b>catch:</b> receives the exception in a variable, e.g. <code>$e</code>. <code>$e-&gt;getMessage()</code> gives its description; <code>getCode()</code>, <code>getFile()</code> and <code>getLine()</code> help diagnostics.</li>
<li><b>finally:</b> runs cleanup after the normal try or the catch, including when a return or propagated exception leaves the block. Abrupt termination such as exit/die or killing the process can prevent it.</li>
<li>If handled without rethrow/return, execution continues after the structure. If there is no matching handler, the exception propagates to the caller; unhandled at the top level it terminates the request.</li>
<li>The fare program tests <b>both</b> a normal division and an invalid zero-passenger request, making the skipped line and the shared finally visible.</li></ul>
""", diagram="wd4_exception_flow", programs=["wd4p7"]),
        T("Custom Exceptions and Catch Order", """
<p>PHP provides <code>Exception</code>, <code>InvalidArgumentException</code>, <code>RuntimeException</code> and other standard classes. Extend a suitable class when callers need to recognise a particular domain failure.</p>
@@custom_exception@@
<ul><li>The booking program distinguishes invalid input (zero seats) from a legitimate request that cannot be fulfilled (too few seats available).</li>
<li>Only the <b>first compatible catch</b> runs. Put specific subclasses before broad parents such as Exception; otherwise the broad catch absorbs the specific case.</li>
<li>Different catches can take different actions: ask for corrected input, offer another departure, or log an unexpected failure.</li>
<li><code>throw $e;</code> in a catch rethrows to an outer handler, useful when local code cannot recover.</li>
<li>Do not silently catch and ignore failures. Log diagnostic details securely and show a safe user-facing message; internal file paths and stack traces should not be exposed on a production site.</li></ul>
""", programs=["wd4p8"]),
        T("Resource Cleanup with finally", """
<ul><li>Opening a file, acquiring a lock or beginning another resource-dependent operation creates a cleanup obligation. Putting cleanup only at the end of try misses the exception path.</li>
<li>Initialise the handle before try, open/work inside try, and in finally close it only if <code>is_resource($h)</code>. This also handles failures before the open.</li>
<li>A successful return does not normally skip finally; a return <em>inside</em> finally can override the intended return or pending exception. Keep finally dedicated to cleanup.</li>
<li>Many PHP file functions produce a warning and return <code>false</code>, not an exception. Check the documented return value and explicitly throw if you want exception-based application flow.</li>
<li>The manifest program runs three cases against real files: success, failure after opening, and an unavailable file before opening. Its output confirms two closures and one no-handle cleanup.</li>
<li>A catch without finally is allowed, and try/finally without catch is also allowed when cleanup is needed but recovery belongs to the caller.</li></ul>
""", programs=["wd4p9"]),
        T("Exception, Error and Throwable in Modern PHP", """
<p>In PHP 7+, throwable failures have two major families, both implementing the <code>Throwable</code> interface:</p>
<table><tr><th>Family</th><th>Examples</th><th>Catching it</th></tr>
<tr><td>Exception</td><td>RuntimeException, InvalidArgumentException and your subclasses</td><td>catch (Exception $e), or a more specific exception type</td></tr>
<tr><td>Error</td><td>TypeError, DivisionByZeroError and related engine errors</td><td>catch (Error $e), or a more specific error type</td></tr>
<tr><td>Both</td><td>Any object implementing Throwable</td><td>catch (Throwable $t)</td></tr></table>
<ul><li><b>Exception does not include Error.</b> A raw <code>10 / 0</code> raises DivisionByZeroError; the earlier fare validator instead deliberately throws an InvalidArgumentException before division.</li>
<li>Ordinary warnings/notices are <b>not automatically throwable</b>. A broad catch is not a universal replacement for checking function returns or validating input.</li>
<li>The strict-types program generates a real application exception, division error and type error, then proves the broad Throwable catch can also catch a TypeError.</li>
<li>Prefer specific, expected handlers close to the operation; use a broad boundary handler to log unexpected failures and return a safe error response, not to conceal programming bugs.</li></ul>
""", diagram="wd4_exception_tree", programs=["wd4p10"]),
    ],
}

NOTES = [SEC_4_1, SEC_4_2, SEC_4_3]
