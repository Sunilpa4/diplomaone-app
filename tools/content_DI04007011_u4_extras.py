"""DI04007011 Unit 4: 10 syntax cards, 40 viva Q&A, 14 exam/practical tasks."""
from php_content import SXE, VE, XE, G

SYNTAX = [
    G("Cookie Cards", [
        SXE("Create and read", '''setcookie("city", "Surat", [
  "expires" => time() + 3600,
  "path" => "/"
]);
$_COOKIE["city"] ?? "default"''',
            "Set before output; read the new value on the next request."),
        SXE("Update and expire", '''Same name + domain + path:
setcookie(name, newValue, opts)
Delete with a past expiry:
"expires" => time() - 3600
unset($_COOKIE[...]) is local only''',
            "A different path can create a second cookie instead of replacing the first."),
        SXE("Security options", '''"secure"   => true   // HTTPS
"httponly" => true   // no JS read
"samesite" => "Lax"
"path"     => "/"
Validate all incoming values.''',
            "Production HTTPS: protect transport and minimise scope. Local HTTP demos do not require Secure."),
    ]),
    G("Session Cards", [
        SXE("Start, set and read", '''session_start(); // every page
$_SESSION["user"] = "Ravi";
$_SESSION["cart"] = ["seat" => 2];
$user = $_SESSION["user"] ?? "Guest";''',
            "Browser carries the ID; server stores the session values."),
        SXE("Clear one vs all", '''unset($_SESSION["theme"]);
// Remove just one variable.
session_unset();
// Clear all values; still active.
// Or: $_SESSION = [];''',
            "Removing values is not the same as destroying the session or expiring its cookie."),
        SXE("Full logout sequence", '''session_start();
$_SESSION = [];
// Expire session_name() cookie
// using session_get_cookie_params().
session_destroy();
// Redirect, then exit.''',
            "Three jobs: clear current values, remove browser cookie, destroy server data. See the complete program."),
        SXE("Login and page guard", '''// After successful verification:
session_regenerate_id(true);
$_SESSION["user"] = $userId;
// On every protected page:
if (!isset($_SESSION["user"])) {
  header("Location: login.php");
  exit;
}''',
            "Start before output. Use password_verify, CSRF tokens and HTTPS in the complete app."),
    ]),
    G("Exception Cards", [
        SXE("try / throw / catch / finally", '''try {
  throw new Exception("Failure");
} catch (Exception $e) {
  echo $e->getMessage();
} finally {
  // Release resources.
}''',
            "A throw skips the rest of try. Escape messages if rendering untrusted text as HTML."),
        SXE("Custom class and order", '''class SoldOut extends RuntimeException {}
// Catch specific classes first:
catch (SoldOut $e) { ... }
catch (Exception $e) { ... }
// Rethrow with: throw $e;''',
            "Only the first matching catch executes; broad parents belong last."),
        SXE("Throwable families", '''Throwable
  Exception -> RuntimeException
  Error     -> TypeError
            -> DivisionByZeroError
catch (Throwable $t) { ... }''',
            "Exception does not catch Error. Ordinary warnings/notices are not automatically exceptions."),
    ]),
]

_VIVA = [
    VE("Why do web applications need cookies or sessions?", "HTTP is stateless: separate requests do not automatically remember earlier choices or authentication. Cookies/sessions provide continuity."),
    VE("What is a cookie?", "A small name/value record stored by the browser for a site and sent with requests that match its scope and policy."),
    VE("Which two HTTP headers implement the cookie round trip?", "The server sends Set-Cookie in a response; the browser later sends Cookie in a request."),
    VE("Why is a newly set cookie missing from $_COOKIE in the same request?", "setcookie queues an outgoing response header; $_COOKIE contains the values from the incoming request. Read the new cookie on the next request."),
    VE("How do you read a cookie without an undefined-key warning?", "Use $_COOKIE['name'] ?? 'default', or check isset($_COOKIE['name']) before reading it."),
    VE("How do you update a cookie?", "Call setcookie again with a new value and the same name, domain and path. A different path can create another cookie."),
    VE("How do you delete a cookie?", "Expire it in the past using the same name, domain and path. The browser stops returning it on later requests."),
    VE("Why is unset($_COOKIE['x']) not browser-side deletion?", "It only removes the element from the PHP array for this request; it sends no Set-Cookie deletion header."),
    VE("Why must setcookie run before HTML or echo?", "It changes HTTP headers, which must be sent before the response body. Leading whitespace or a BOM can also cause headers-already-sent problems."),
    VE("Persistent cookie vs browser-session cookie?", "A persistent cookie has a future expiry timestamp; expiry 0/omitted creates a browser-session cookie. Browser policy and session restore affect actual retention."),
    VE("Secure, HttpOnly and SameSite - what does each do?", "Secure restricts sending to HTTPS; HttpOnly blocks JavaScript reading the cookie; SameSite controls cross-site sending. They protect different aspects and do not replace all other security checks."),
    VE("Can an application trust a cookie saying role=admin?", "No. Cookie values are client-controlled. Authenticate and authorise using validated server-side data; never store raw passwords in cookies."),

    VE("What is a PHP session?", "Server-side per-visitor storage normally selected by an opaque ID carried in a browser cookie."),
    VE("What does PHPSESSID contain?", "Normally a random session identifier, not the user's name, password or cart data. The ID maps to a server-side session record."),
    VE("What does session_start do on a second page?", "It resumes the existing session if a valid incoming ID is available, otherwise creates one. Call it before output on every participating page."),
    VE("Can $_SESSION hold an array?", "Yes. Session values can include arrays, strings, numbers and other serialisable application data; they are not limited to cookie-style string values."),
    VE("Do two browsers normally share one session?", "No. Separate cookie jars normally carry different session IDs and select separate server-side records."),
    VE("unset($_SESSION['x']) vs session_unset()?", "unset removes one named key. session_unset clears all variables in the active session, but does not destroy its identity or delete its cookie."),
    VE("Does session_destroy automatically empty $_SESSION and delete its cookie?", "No. It destroys server-side session data. Clear the current array and explicitly expire the matching cookie as separate steps."),
    VE("List the steps of full logout.", "Start/resume the session; clear $_SESSION; expire the session cookie using its original parameters; call session_destroy; redirect and exit."),
    VE("What does session_regenerate_id(true) do?", "Creates a new session ID while preserving current values, and deletes the old session data. Use after successful authentication to reduce fixation risk."),
    VE("Session fixation vs session hijacking?", "Fixation makes a victim use an attacker-known ID before authentication. Hijacking steals an already valid ID. ID regeneration, strict mode, HTTPS and cookie protections address different parts of these risks."),
    VE("Why enable session.use_strict_mode and cookie-only IDs?", "Strict mode rejects uninitialised supplied IDs; cookie-only IDs avoid leaking session identifiers through URLs. They are useful defaults, not a complete security solution."),
    VE("How is a PHP page protected after login?", "Start/resume the session and test a server-set authentication key before any private output. If missing, redirect to login and exit; hiding a link is not access control."),
    VE("Is closing the browser a reliable logout mechanism?", "No. Session restore may preserve cookies, and server records may remain. Enforce idle/absolute expiry explicitly and implement full logout."),
    VE("What if a browser rejects the session cookie?", "In a cookie-only configuration it cannot normally retain the same session across independent requests. Do not work around this by exposing IDs in URLs."),
    VE("What is a CSRF token and where is it checked?", "A random value stored in the session and included in a form; the server compares it on POST, for example with hash_equals. It helps reject forged state-changing requests."),

    VE("Name the four main exception-handling keywords.", "try surrounds risky work, throw signals failure with an object, catch handles a matching type, and finally performs cleanup."),
    VE("What happens to statements after a throw inside try?", "They are skipped. PHP searches for a compatible catch; cleanup in finally normally runs before control continues or the exception propagates."),
    VE("Why must specific catches precede parent classes?", "Only the first matching catch runs. A broad Exception catch placed first would absorb its subclasses and prevent more specific handling."),
    VE("How do you obtain an exception's message and location?", "getMessage() returns its description; getCode(), getFile() and getLine() provide diagnostics. Keep internal locations out of public error pages."),
    VE("Why use finally instead of cleanup at the end of try?", "An exception can skip the remaining try statements. finally provides a shared cleanup path for success and failure, including a normal return."),
    VE("Does finally run under absolutely every circumstance?", "No. It normally runs for return and propagated exceptions, but exit/die or process termination can prevent it. Avoid return inside finally because it can override a pending result or exception."),
    VE("How do you define a custom exception?", "Extend Exception or a suitable subclass, for example class SeatsUnavailable extends RuntimeException {}. Throw an instance and catch that specific class."),
    VE("What is rethrowing?", "A catch can use throw $e to pass the failure to an outer handler after local logging or other handling."),
    VE("Will catch(Exception) automatically handle fopen warnings?", "No. Many functions emit warnings and return false rather than throw. Check the return value and deliberately throw if your application requires exception flow."),
    VE("Exception vs Error in PHP 7+?", "They are distinct families. Application exceptions usually extend Exception; engine failures such as TypeError and DivisionByZeroError extend Error. Exception does not catch Error."),
    VE("What does catch(Throwable $t) catch?", "Both Exception and Error objects, since both implement Throwable. It does not automatically catch ordinary warnings or notices."),
    VE("What happens if no matching catch exists?", "The exception propagates to callers, with finally cleanup during normal unwinding. If still unhandled at the top level, the request terminates."),
    VE("Should a production site display a complete stack trace?", "No. Log useful diagnostics securely and show a safe user-facing message. Do not silently ignore failures or reveal internal paths, credentials or traces."),
]
assert len(_VIVA) == 40, len(_VIVA)
VIVA = [
    G("Cookies and Browser State", _VIVA[:12]),
    G("Sessions, Login and Logout", _VIVA[12:27]),
    G("Exception Handling", _VIVA[27:]),
]

EXAM_QS = [
    XE("Write a PHP program that creates, reads and updates a city cookie. Demonstrate the first and next request, and explain the Set-Cookie/Cookie header exchange. (Practical 17)", 4),
    XE("Why is a newly set cookie not immediately present in $_COOKIE? Explain why setcookie must precede output.", 3),
    XE("Develop a theme-preference form that remembers light/dark for 30 days. Validate the value, use suitable cookie options, and implement Post/Redirect/Get. (Practical 17)", 6),
    XE("Write the code to destroy a cookie. Explain matching name/domain/path and why unset($_COOKIE['x']) is insufficient.", 3),
    XE("Compare cookies and PHP sessions in terms of storage, request transport, capacity, lifetime, trust and suitable uses.", 4),
    XE("Write a two-page PHP application that sets session variables on one page and reads them on another. Show what happens in a separate browser. (Practical 16)", 4),
    XE("Differentiate unset($_SESSION['x']), session_unset and session_destroy. Give the complete logout sequence.", 4),
    XE("Develop a multi-page login application: password verification, session ID regeneration, a guarded dashboard and POST logout. Prove direct dashboard access fails both before login and after logout. (Practical 16)", 6),
    XE("Explain session fixation, session hijacking, strict mode, HTTPS cookie flags and CSRF tokens in the context of a login system.", 4),
    XE("Explain try, throw, catch and finally, including control flow on success, on a matching catch and when no handler exists.", 4),
    XE("Write a fare-per-passenger program that throws for zero/negative count, catches the exception and prints cleanup in finally. Test success and failure. (Practical 18)", 6),
    XE("Create a custom SeatsUnavailable exception for a booking function. Distinguish invalid input from insufficient availability and demonstrate specific-before-general catches. (Practical 18)", 6),
    XE("Write a file-reading program with finally cleanup. Demonstrate success, failure after open and failure before open; explain warnings/false versus thrown exceptions.", 6),
    XE("Differentiate Exception, Error and Throwable in modern PHP, using TypeError and DivisionByZeroError examples. Why is catch(Exception) not a universal handler?", 4),
]
