"""DI04007011 Unit 4: eight original, 360-wide cookie/session/exception diagrams."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, grid, PF, GREY
from diagrams_DI03000061_u1 import code


def cookie_roundtrip():
    b = title("A Cookie Takes Two Requests")
    b += box(14, 48, 112, 28, BLUEF, BLUE, 7, 1.2)
    b += text(70, 62, "BROWSER", 10, weight="bold", color=BLUE)
    b += box(234, 48, 112, 28, GREENF, GREEN, 7, 1.2)
    b += text(290, 62, "PHP SERVER", 10, weight="bold", color=GREEN)
    b += line("M70 78 V272", "#bbb", 1.2, "4 3")
    b += line("M290 78 V272", "#bbb", 1.2, "4 3")
    b += arr([(70, 105), (290, 105)], BLUE)
    b += text(180, 92, "1. Request: no city cookie yet", 8.2, color=BLUE)
    b += arr([(290, 145), (70, 145)], GREEN)
    b += text(180, 132, "2. Response: Set-Cookie: city=Surat", 8.0, color=GREEN)
    b += box(14, 162, 112, 32, ORANGEF, ORANGE, 6, 1.1)
    b += lines(70, 173, ["browser saves", "city = Surat"], size=8.1, lh=12)
    b += arr([(70, 223), (290, 223)], BLUE)
    b += text(180, 210, "3. Next request: Cookie: city=Surat", 8.1, color=BLUE)
    b += box(224, 240, 126, 36, GREENF, GREEN, 6, 1.1)
    b += code(234, 251, ['$_COOKIE["city"]', 'is now "Surat"'], size=8.0, lh=13)
    b += note(12, 294, 336, ["setcookie() queues a RESPONSE header.",
                             "It does not change the incoming $_COOKIE.",
                             "Read the new value on the NEXT request."], size=9.1)
    return svg(360, 364, b)


def cookie_lifecycle():
    b = title("Cookie Lifecycle: Same Name and Path")
    stages = [
        ("CREATE", 'setcookie("city", "Surat", options)', "Browser saves it after the response", BLUEF, BLUE),
        ("READ", '$_COOKIE["city"] ?? "default"', "Incoming request values are client-controlled", GREENF, GREEN),
        ("UPDATE", 'setcookie("city", "Vadodara", options)', "Same name/domain/path replaces the value", ORANGEF, ORANGE),
        ("DELETE", 'expires => time() - 3600', "Expire the matching name/domain/path cookie", REDF, RED),
    ]
    for i, (label, src, desc, fill, stroke) in enumerate(stages):
        y = 44 + i * 60
        b += box(12, y, 336, 46, fill, stroke, 7, 1.2)
        b += text(22, y + 13, label, 8.1, anchor="start", color=stroke, weight="bold")
        b += text(105, y + 13, src, 7.4, anchor="start", mono=True)
        b += text(22, y + 32, desc, 8.0, anchor="start")
        if i < 3:
            b += down(180, y + 46, y + 60)
    b += note(12, 290, 336, ["Deletion is also a response: the browser stops",
                             "sending the cookie on the next request.",
                             "unset($_COOKIE[...]) alone is NOT deletion."], size=8.9)
    return svg(360, 358, b)


def cookie_flags():
    b = title("Cookie Options and Safe Defaults")
    b += grid(12, 44, [76, 260], [
        ["option", "meaning"],
        ["expires", "Timestamp; 0 = browser-session cookie"],
        ["path", '"/" makes it available across the site'],
        ["domain", "Omit for a host-only cookie"],
        ["secure", "Send only over HTTPS"],
        ["httponly", "Hide cookie from JavaScript access"],
        ["samesite", "Lax/Strict/None control cross-site sending"],
    ], rh=25, size=7.8)
    b += note(12, 236, 336, ["Production: HTTPS + Secure + HttpOnly + Lax.",
                             "SameSite=None also requires Secure.",
                             "Local HTTP demo: Secure must not be required.",
                             "Cookies are editable: validate incoming values.",
                             "Never store passwords or trust a role cookie."], size=8.8)
    return svg(360, 336, b)


def session_roundtrip():
    b = title("Session ID Travels; Session Data Stays")
    b += box(12, 48, 120, 136, BLUEF, BLUE, 8, 1.2)
    b += text(72, 66, "BROWSER", 10, weight="bold", color=BLUE)
    b += code(22, 91, ["Cookie:", "PHPSESSID=", "random-ID", "", "No cart or user", "data in this", "cookie"], size=7.8, lh=12)
    b += box(210, 48, 138, 136, GREENF, GREEN, 8, 1.2)
    b += text(279, 66, "SERVER STORE", 10, weight="bold", color=GREEN)
    b += code(220, 91, ["random-ID =>", 'user: "Ravi"', "seats: 1", "visits: 2", "", "file / database", "or other store"], size=7.8, lh=12)
    b += arr([(132, 110), (210, 110)], BLUE)
    b += text(171, 96, "ID only", 8.0, color=BLUE)
    b += arr([(210, 152), (132, 152)], GREEN)
    b += text(171, 168, "new ID*", 7.8, color=GREEN)
    b += box(12, 204, 336, 42, PF, P, 7, 1.2)
    b += code(24, 216, ["session_start();    // create OR resume",
                        '$_SESSION["seats"] = 1;'], size=8.0, lh=15)
    b += note(12, 264, 336, ["Every participating page starts/resumes first.",
                             "The same browser cookie selects the same data.",
                             "*Set-Cookie is needed for a new/rotated ID,",
                             "not necessarily on every response."], size=8.9)
    return svg(360, 348, b)


def login_flow():
    b = title("Login to Logout: The Session Gate", size=13.5)
    stages = [
        ("1  GUEST ASKS FOR DASHBOARD", "No session user -> redirect to login", BLUEF, BLUE),
        ("2  LOGIN FORM POSTS CREDENTIALS", "Check CSRF + username + password_verify()", BLUEF, BLUE),
        ("3  SUCCESS: ROTATE THE SESSION ID", "session_regenerate_id(true); save session user", GREENF, GREEN),
        ("4  DASHBOARD GUARD PASSES", "Read server-side user; escape it before HTML", GREENF, GREEN),
        ("5  LOGOUT: VALID-TOKEN POST", "Clear variables + expire cookie + destroy", REDF, RED),
        ("6  DASHBOARD GUARD FAILS AGAIN", "Direct URL access redirects back to login", ORANGEF, ORANGE),
    ]
    for i, (head, desc, fill, stroke) in enumerate(stages):
        y = 44 + i * 50
        b += box(12, y, 336, 38, fill, stroke, 7, 1.2)
        b += text(24, y + 12, head, 8.5, anchor="start", weight="bold", color=stroke)
        b += text(24, y + 27, desc, 8.0, anchor="start")
        if i < 5:
            b += down(180, y + 38, y + 50)
    b += note(12, 350, 336, ["Check authentication on EVERY protected page.",
                             "Hiding a link is not protection. Wrong password",
                             "must never create an authenticated session."], size=8.9)
    return svg(360, 420, b)


def cookie_vs_session():
    b = title("Cookies vs Sessions")
    b += grid(12, 44, [78, 129, 129], [
        ["feature", "cookie value", "session data"],
        ["stored at", "browser", "server"],
        ["request sends", "the value", "usually just an ID"],
        ["capacity", "small (~4 KB each)", "server limits apply"],
        ["lifetime", "expiry/browser policy", "server expiry policy"],
        ["control", "client can edit it", "app controls values"],
        ["risk", "tampered value", "stolen session ID"],
        ["good for", "theme / language", "login / cart / flash"],
    ], rh=25, size=7.4)
    b += note(12, 262, 336, ["Sessions often USE a cookie to carry the ID.",
                             "They are not independent alternatives at the",
                             "transport layer. Protect the ID with HTTPS,",
                             "HttpOnly and regeneration after login.",
                             "Browser-close is not a reliable logout policy."], size=8.9)
    return svg(360, 362, b)


def exception_flow():
    b = title("Exception Flow: Success and Failure")
    b += rbox(180, 58, 142, 30, "enter try", fill=BLUEF, stroke=BLUE, size=10)
    b += down(180, 73, 100)
    b += decision(180, 124, "exception thrown?", w=126, h=48, size=9)
    b += arr([(117, 124), (70, 124), (70, 186)], BLUE)
    b += text(84, 112, "no", 8.5, color=BLUE)
    b += arr([(243, 124), (290, 124), (290, 186)], ORANGE)
    b += text(277, 112, "yes", 8.5, color=ORANGE)
    b += rbox(70, 204, 112, 36, "rest of try runs", fill=BLUEF, stroke=BLUE, size=8.8)
    b += rbox(290, 204, 112, 36, "matching catch", fill=ORANGEF, stroke=ORANGE, size=8.8)
    b += text(290, 236, "remaining try is skipped", 7.6, color=ORANGE)
    b += arr([(70, 222), (70, 264), (180, 264), (180, 280)], GREEN)
    b += arr([(290, 250), (290, 264), (180, 264)], GREEN)
    b += rbox(180, 296, 148, 32, "finally: cleanup", fill=GREENF, stroke=GREEN, size=9.6)
    b += down(180, 312, 334)
    b += terminal(180, 350, "continue after handled result", w=216, h=30, size=8.9)
    b += note(12, 386, 336, ["No matching catch? finally runs, then the",
                             "exception propagates to the caller.",
                             "exit()/process termination can skip finally."], size=8.9)
    return svg(360, 456, b)


def exception_tree():
    b = title("Modern PHP: The Throwable Family")
    b += rbox(180, 56, 146, 32, "Throwable (interface)", fill=PF, stroke=P, size=9.5)
    b += arr([(180, 72), (180, 94), (84, 94), (84, 116)], BLUE)
    b += arr([(180, 94), (276, 94), (276, 116)], RED)
    b += rbox(84, 132, 140, 32, "Exception", fill=BLUEF, stroke=BLUE, size=10)
    b += rbox(276, 132, 140, 32, "Error", fill=REDF, stroke=RED, size=10)
    b += down(84, 148, 166, BLUE)
    b += down(276, 148, 166, RED)
    b += box(12, 166, 146, 104, BLUEF, BLUE, 7, 1.1)
    b += code(22, 185, ["InvalidArgumentException", "RuntimeException", "  -> your custom", "     subclasses"], size=7.3, lh=20)
    b += box(202, 166, 146, 104, REDF, RED, 7, 1.1)
    b += code(214, 190, ["TypeError", "DivisionByZeroError", "... engine errors"], size=7.4, lh=22)
    b += note(12, 290, 336, ["catch (Exception $e) does NOT catch Error.",
                             "catch (Throwable $t) can catch both families.",
                             "Ordinary warnings/notices are not automatically",
                             "exceptions. Prefer specific expected catches."], size=8.8)
    return svg(360, 376, b)


ALL = {
    "wd4_cookie_roundtrip": cookie_roundtrip,
    "wd4_cookie_lifecycle": cookie_lifecycle,
    "wd4_cookie_flags": cookie_flags,
    "wd4_session_roundtrip": session_roundtrip,
    "wd4_login_flow": login_flow,
    "wd4_cookie_vs_session": cookie_vs_session,
    "wd4_exception_flow": exception_flow,
    "wd4_exception_tree": exception_tree,
}

if __name__ == "__main__":
    from subject_DI04007011 import DIAG_DIR
    for name, build in ALL.items():
        with open(os.path.join(DIAG_DIR, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(build())
    print("written", len(ALL))
