"""DI04007011 Unit 1 extras: key-term cards, viva, exam (practical-task) questions."""

from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Page and output cards", [
        SXE("php tags", """<?php
  // code islands,
  // anywhere in the page
?>
<?= $x ?>  short echo""",
            "save as .php, not .html"),
        SXE("echo vs print", """echo "a", "b";   fastest
                 returns nothing
print "a";      returns 1
                 fits expressions""",
            "both are constructs, not functions"),
        SXE("comments", """// line comment
#  line comment
/* block
   comment */""",
            "for the reader, never the browser"),
    ]),
    G("Variable and operator cards", [
        SXE("variables + types", """$seat = 40;      int
$fare = 9.5;     float
$n = "Surat";    string
$ok = true;      bool
var_dump($x) -> type+value""",
            "value decides the type"),
        SXE("constants", """define("GST", 0.18);
const NAME = "BusBook";
no $ sign, no reassign,
global by default""",
            "set once, use forever"),
        SXE("== vs ===", """5 == "5"    true   juggled
5 === "5"   false  strict
form data arrives as
strings -> use === / cast""",
            "strict wins every time"),
        SXE("string glue", """$a . $b       concatenate
$a .= $b      append in place
"Fare: $fare" interpolates
'Fare: $fare' stays literal""",
            "dots, not pluses, join text"),
    ]),
    G("Decision and loop cards", [
        SXE("if ladder", """if ($m >= 70)      {...}
elseif ($m >= 60)  {...}
else               {...}
first TRUE branch wins""",
            "order slabs high to low"),
        SXE("switch", """switch ($day) {
  case "Mon": ...
             break;
  default:   ...
}""",
            "equality tests only; break!"),
        SXE("four loops", """for (known count)
while (pre-checked)
do-while (once minimum)
foreach (arrays)""",
            "pick by intent"),
        SXE("break / continue", """break    leave loop now
continue skip to next lap
break 2  exit two levels""",
            "innermost loop by default"),
    ]),
]

_VIVA = [
    VE("What does PHP stand for?", "PHP: Hypertext Preprocessor - a recursive acronym; earlier it meant Personal Home Page tools."),
    VE("Who created PHP and when?", "Rasmus Lerdorf, around 1994-95, to track visitors to his online resume."),
    VE("Is PHP server-side or client-side?", "Server-side - the PHP engine on the server executes it; the browser receives only the generated HTML."),
    VE("List four advantages of PHP.", "Free and open-source; cross-platform (Windows/Linux/macOS); easy C-like syntax with no compilation; huge ecosystem (WordPress, phpMyAdmin) and native MySQL support."),
    VE("What is the client-server environment?", "The browser (client) sends HTTP requests; the web server (Apache) processes them - running PHP for dynamic pages - and returns HTML responses."),
    VE("Explain the 3-tier architecture of a web application.", "Presentation tier (browser, HTML/CSS), application tier (Apache + PHP logic), data tier (MySQL/files). Requests flow down, responses bubble back."),
    VE("Where do the three tiers live during development?", "All on one machine - XAMPP installs Apache, PHP and MySQL together on the developer's laptop."),
    VE("What does XAMPP stand for?", "X = cross-platform (any OS), Apache, MariaDB/MySQL, PHP, Perl."),
    VE("Which folder holds PHP files under XAMPP?", "htdocs (e.g. C:\\xampp\\htdocs); browse them at http://localhost/filename.php."),
    VE("A page shows 404 - likely cause?", "The file is not under htdocs, the name/URL is mistyped, or Apache is not running."),
    VE("How do you embed PHP in an HTML page?", "Wrap code in <?php ... ?> islands anywhere in the page, and save the file with a .php extension."),
    VE("Difference between echo and print?", "echo takes multiple comma-separated values and returns nothing; print takes one value and returns 1, so it can sit in expressions. echo is marginally faster."),
    VE("Which comment styles does PHP support?", "// and # for single lines; /* ... */ for blocks."),
    VE("What rules govern PHP variable names?", "Start with $ then a letter or underscore; case-sensitive; no type declaration needed (loose typing)."),
    VE("List PHP's scalar and compound types.", "Scalar: int, float, string, bool. Compound: array, object. Special: NULL and resource."),
    VE("How do you inspect a variable's type and value?", "var_dump($x) shows both; gettype($x) returns the type name."),
    VE("How do you define a constant?", "define(\"GST\", 0.18) or const GST = 0.18; - no $ sign, global, immutable."),
    VE("Double-quoted vs single-quoted strings?", "Double quotes interpolate variables (\"Hi $name\" expands); single quotes treat them literally."),
    VE("Which operator joins two strings?", "The dot: \"Hello \" . $name. .= appends in place."),
    VE("Difference between == and ===?", "== compares after type juggling (\"18\" == 18 is true); === also requires the same type. Prefer === with form data."),
    VE("What does the spaceship operator <=> return?", "-1, 0 or 1 for less, equal, greater - made for custom sort comparisons."),
    VE("Structure of an if-elseif-else ladder?", "Conditions tested top-down; the first true branch executes and the rest are skipped; else catches the remainder."),
    VE("Which values are falsy in PHP?", "false, 0, 0.0, \"\" (empty string), \"0\", null, [] (empty array)."),
    VE("When is the ternary operator useful?", "Compact two-way choices inside echo or assignments: ($m >= 40) ? \"Pass\" : \"Fail\"."),
    VE("When would you pick switch over if-elseif?", "When one expression is compared for equality against many constants - day names, menu choices, status codes."),
    VE("What happens if break is omitted in a case?", "Execution falls through into the next case - almost never intended; always end cases with break."),
    VE("Difference between while and do-while?", "while checks first (may run zero times); do-while runs the body once before checking (minimum one execution)."),
    VE("Which loop is best for arrays?", "foreach - it iterates elements directly: foreach ($arr as $v) or as $k => $v; no counter needed."),
    VE("for vs foreach?", "for needs init/test/step and suits counted ranges; foreach streams array elements with no index bookkeeping."),
    VE("What do break and continue do?", "break exits the loop immediately; continue skips the rest of the current iteration and starts the next."),
    VE("What does break 2 do?", "Exits two levels of nested loops at once."),
    VE("Why is PHP called 'loosely typed'?", "Variables take the type of the value assigned and can change type on reassignment - PHP juggles types automatically in expressions."),
    VE("How do you run a PHP file without a browser?", "With the CLI: php filename.php - useful for logic testing before wiring up forms."),
    VE("What PHP version family do we target?", "PHP 8.x - JIT compiler, modern syntax; all lab programs in these notes were run on PHP 8."),
    VE("What is the URL of a page saved as htdocs/hello.php?", "http://localhost/hello.php - localhost is your own machine, port 80 by default."),
    VE("A .php file shows its source code in the browser - why?", "It was saved as .html (server never invokes PHP), or Apache/PHP handler is off."),
    VE("What is variable interpolation?", "Embedding $variables inside double-quoted strings so their values are substituted - \"Seats: $seats\"."),
    VE("Give three everyday PHP programs from Unit 1.", "Welcome page with echo/print; grade ladder with if-elseif; seat-listing loop with continue for booked seats."),
]

VIVA = [
    G("PHP and the Web", _VIVA[0:8]),
    G("Setup, Syntax and Types", _VIVA[8:19]),
    G("Operators and Decisions", _VIVA[19:26]),
    G("Loops and Practice", _VIVA[26:38]),
]

assert len(_VIVA) == 38, len(_VIVA)

EXAM_QS = [
    XE("Explain the client-server environment and the 3-tier architecture of a web application with a diagram.", 4),
    XE("Write the history of PHP and any four advantages. Why is it called server-side?", 4),
    XE("Describe the steps to install XAMPP and run hello.php on localhost. (Practical 1-2)", 4),
    XE("Explain embedding of PHP within HTML with a page that contains two <?php islands.", 4),
    XE("Write a PHP program for a fare calculator using a constant GST rate, variables and arithmetic operators. (Practical 3)", 6),
    XE("Distinguish == and === with var_dump output, explaining why strict comparison matters for form data.", 4),
    XE("Write a PHP program that prints the grade (Distinction/First/Second/Pass/Fail) for given marks using if-elseif-else. (Practical 4)", 6),
    XE("Rewrite a weekday schedule program using switch-case; explain fall-through and the role of break. (Practical 4)", 4),
    XE("Write one PHP program demonstrating for, while, do-while and foreach, stating when each loop is preferred. (Practical 5)", 6),
    XE("Write a PHP program to print free seats 1-10 skipping booked seats 3 and 7 (continue), then stop a route search at the first 'Navsari' match (break).", 6),
    XE("Explain PHP data types with a var_dump table; distinguish variables and constants.", 4),
    XE("List the operator families of PHP with two examples each, and explain the spaceship operator.", 4),
]
