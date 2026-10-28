"""DI04007011 Unit 1 - solved PHP programs. Every output below is genuine (PHP 8.4 CLI)."""

from php_content import PP

PROGRAMS = [
    PP("wd1p1", "Welcome page: echo, print and comments (Practical 2)", r'''
<?php
// My first PHP page - Practical 2
#  hash comments also work
/* block comments
   span several lines */

echo "Welcome to Web Development!\n";
echo "Diploma", " Sem 4", " - Computer\n";   // echo takes many values
print "Powered by PHP\n";                     // print: one value only

$name = "Ravi";          // double quotes interpolate variables
echo "Hello, $name\n";   // Hello, Ravi
echo 'Hello, $name' . "\n";  // single quotes stay literal
?>
''',
       """<p><code>echo</code> accepts comma-separated values; <code>print</code> takes one and returns 1. Double-quoted strings <b>interpolate</b> (expand) <code>$variables</code>; single-quoted strings print them literally. Comments after <code>//</code>, <code>#</code> or inside <code>/* */</code> never reach the output.</p>"""),

    PP("wd1p2", "Embedding PHP islands inside HTML", r'''
<?php
$seatsTotal = 40;
$seatsBooked = 3;
?>
<!DOCTYPE html>
<html>
<head><title>Bus Booking</title></head>
<body>
<h1>Bus Booking - Surat to Ahmedabad</h1>
<p>Date: <?php echo date("d M Y"); ?></p>
<?php
    $seats = $seatsTotal - $seatsBooked;
    echo "<p><b>Seats left: $seats</b></p>";
?>
<p>Have a safe journey!</p>
</body>
</html>
''',
       """<p>The <code>&lt;?php ?&gt;</code> islands can appear anywhere in the page. The engine executes each island and replaces it with its output, so the browser receives one flat HTML document. Run this with the CLI and you see the same HTML the browser would (tags are echoed text here).</p>"""),

    PP("wd1p3", "Variables, constants and operators (Practical 3)", r'''
<?php
// Fare calculator - variables, constants, operators
define("GST_RATE", 0.18);        // constant: no $ sign
const APP_NAME = "BusBook";

$baseFare = 250;                 // int
$distance = 265;                 // int (kms)
$perKm = 1.2;                    // float

$fare = $baseFare + $distance * $perKm;   // * and + : int+float -> float
$tax = $fare * GST_RATE;
$total = $fare + $tax;

echo APP_NAME, " receipt\n";
echo "Base fare : Rs ", $fare, "\n";
echo "GST 18%   : Rs ", round($tax, 2), "\n";
echo "Total     : Rs ", round($total, 2), "\n";

$seats = 40;
$seats -= 3;                     // compound assignment
$seats++;                        // increment
echo "Seats left now: $seats\n";
?>
''',
       """<p>Operators behave as in C/Java: <code>*</code> binds tighter than <code>+</code>; mixed int/float arithmetic promotes to float. Constants need no <code>$</code> and cannot be redefined. Compound assignment (<code>-=</code>) and <code>++</code> update a variable in place.</p>"""),

    PP("wd1p4", "Types, var_dump and == vs === (Practical 3)", r'''
<?php
$age = 18;              // int
$price = 19.99;         // float
$name = "Surat";        // string
$isActive = true;       // bool
$pending = null;        // NULL

var_dump($age, $price, $name, $isActive, $pending);

$fromForm = "18";       // form data always arrives as string
var_dump($age == $fromForm);    // loose: true (type juggled)
var_dump($age === $fromForm);   // strict: false (types differ)
var_dump($age === (int)$fromForm); // after casting: true

echo "2 + 3 = ", 2 + 3, " but 2 . 3 = ", 2 . 3, "\n";
?>
''',
       """<p><code>var_dump()</code> prints type and value - the PHP debugger's first tool. <b>Loose vs strict</b>: <code>==</code> converts types before comparing (dangerous with form input), <code>===</code> requires identical type AND value. Note the two operators: <code>+</code> adds numbers, <code>.</code> glues strings.</p>"""),

    PP("wd1p5", "Grade ladder with if - elseif - else (Practical 4)", r'''
<?php
$marks = 54;

if ($marks >= 70) {
    $grade = "Distinction";
} elseif ($marks >= 60) {
    $grade = "First Class";
} elseif ($marks >= 50) {
    $grade = "Second Class";
} elseif ($marks >= 40) {
    $grade = "Pass";
} else {
    $grade = "Fail";
}

echo "Marks: $marks  ->  $grade\n";

// ternary: compact two-way choice
$result = ($marks >= 40) ? "PASS" : "FAIL";
echo "Result: $result\n";

// truthiness shorthand
$seatsLeft = 0;
if ($seatsLeft) {
    echo "Seats available\n";
} else {
    echo "Housefull!\n";   // 0 counts as false
}
?>
''',
       """<p>The ladder tests from the top; the first true branch wins and the rest are skipped - so test the highest slabs first (swap 50 and 40 and watch the bug). The ternary folds a two-way choice into one expression. <code>0</code>, <code>\"\"</code>, <code>null</code>, <code>false</code> are falsy - <code>if ($seatsLeft)</code> reads naturally.</p>"""),

    PP("wd1p6", "Day planner with switch-case (Practical 4)", r'''
<?php
$day = "Wed";

switch ($day) {
    case "Mon":
    case "Wed":
    case "Fri":
        echo "$day: Theory lectures\n";
        break;
    case "Tue":
    case "Thu":
        echo "$day: Lab sessions\n";
        break;
    case "Sat":
        echo "$day: Project work\n";
        break;
    default:
        echo "$day: Holiday / unknown day\n";
}

$route = "SURAT";
switch ($route) {
    case "SURAT":
        echo "Boarding point: Adajan\n";
        // break forgotten on purpose is a bug - never do this
        break;
    case "BHARUCH":
        echo "Boarding point: Zadeshwar\n";
        break;
    default:
        echo "Route not served\n";
}
?>
''',
       """<p><code>switch</code> tests one expression against constants - ideal for menus, days and status codes. Stacked cases (<code>Mon/Wed/Fri</code>) share one block. Every case needs a <code>break</code>: without it execution falls through into the next case. <code>default</code> is the safety net for unmatched values.</p>"""),

    PP("wd1p7", "Four loops doing real work (Practical 5)", r'''
<?php
// for: counted repetition - table of 7
echo "Table of 7:\n";
for ($i = 1; $i <= 5; $i++) {
    echo "7 x $i = " . (7 * $i) . "\n";
}

// while: keep halving until we reach 1
$n = 40;
echo "Halving $n:";
while ($n > 1) {
    $n = $n / 2;
    echo " -> $n";
}
echo "\n";

// do-while: body runs at least once
$attempt = 5;
do {
    echo "Attempt $attempt: seat locked, verifying...\n";
    $attempt--;
} while ($attempt > 3);

// foreach: PHP's array loop (arrays come properly in Unit 2)
$cities = ["Surat", "Bharuch", "Vadodara", "Ahmedabad"];
foreach ($cities as $stop) {
    echo "Stop: $stop\n";
}
?>
''',
       """<p>Choose the loop by intent: <b>for</b> when the count is known, <b>while</b> when the end depends on data (it may run zero times), <b>do-while</b> when the body must run at least once, and <b>foreach</b> whenever an array is in hand - no counter, no off-by-one.</p>"""),

    PP("wd1p8", "break and continue: fine steering inside loops", r'''
<?php
// continue: print seats 1..10 but skip booked ones 3 and 7
$booked = [3, 7];
echo "Free seats:";
for ($seat = 1; $seat <= 10; $seat++) {
    if (in_array($seat, $booked)) {
        continue;                       // skip this lap
    }
    echo " $seat";
}
echo "\n";

// break: search route list, stop at first match
$routes = ["Surat-Baroda", "Surat-Ahmedabad", "Navsari-Surat"];
foreach ($routes as $r) {
    if (str_contains($r, "Navsari")) {
        echo "Found: $r\n";
        break;                          // no need to scan the rest
    }
}

// break 2: exit nested loops
for ($bus = 1; $bus <= 3; $bus++) {
    for ($seat = 1; $seat <= 5; $seat++) {
        if ($bus == 2 && $seat == 3) {
            echo "Stopping at bus $bus seat $seat\n";
            break 2;                    // leave BOTH loops
        }
        echo "bus $bus seat $seat\n";
    }
}
echo "Done.\n";
?>
''',
       """<p><code>continue</code> skips to the next iteration (free-seat printing); <code>break</code> abandons the loop entirely (stop once found); <code>break 2</code> escapes two nesting levels. Use them as precision tools - if every loop needs three breaks, the condition itself is probably wrong.</p>"""),
]
