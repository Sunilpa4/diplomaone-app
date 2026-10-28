"""DI04007011 Unit 2 - solved PHP programs. Every output below is genuine (PHP 8.4 CLI)."""

from php_content import PP

PROGRAMS = [
    PP("wd2p1", "User-defined function: defaults and return (Practical 6)", r'''
<?php
// One tested function replaces copy-paste fare maths
function fare($km, $rate = 1.2, $minFare = 50) {
    $total = $km * $rate;
    return max($total, $minFare);   // never below the minimum fare
}

function receipt($city, $km, $rate = 1.2) {
    $f = fare($km, $rate);
    return "$city: {$km} km, Rs $f";
}

echo receipt("Bharuch", 60), "\n";      // uses default rate
echo receipt("Ahmedabad", 265), "\n";
echo receipt("Gandhinagar", 265, 1.5), "\n";  // override rate
echo receipt("Navsari", 30), "\n";      // min fare kicks in
?>
''',
       """<p><code>fare()</code> has one required parameter (<code>$km</code>) and two with <b>defaults</b> - skip them and the defaults apply. <code>return</code> hands one value back; <code>receipt()</code> shows function-calling-function composition. Note <code>{$km}</code> braced interpolation inside the double-quoted string.</p>"""),

    PP("wd2p2", "Passing by value vs by reference (swap demo)", r'''
<?php
function trySwap($a, $b) {          // BY VALUE: gets copies
    $t = $a; $a = $b; $b = $t;
}
function swap(&$a, &$b) {           // BY REFERENCE: gets originals
    $t = $a; $a = $b; $b = $t;
}

$x = "Surat"; $y = "Mumbai";
trySwap($x, $y);
echo "after trySwap: $x / $y\n";    // unchanged!

swap($x, $y);
echo "after swap&  : $x / $y\n";    // swapped for real

// practical use: accumulate INTO a caller's array
function addBooking(&$list, $seat) {
    $list[] = $seat;                // appends to caller's array
}
$bookings = ["12A"];
addBooking($bookings, "14C");
addBooking($bookings, "3B");
echo "bookings: ", implode(", ", $bookings), "\n";
?>
''',
       """<p><code>trySwap</code> shuffles photocopies - the caller's variables survive untouched. With <code>&amp;$a, &amp;$b</code> the function borrows the originals and the swap is real. The <code>addBooking</code> pattern (array passed by reference) is how helper functions grow a caller's data.</p>"""),

    PP("wd2p3", "Scope: local, global and static", r'''
<?php
$total = 100;                       // GLOBAL scope variable

function addTip($tip) {
    global $total;                  // open the window
    $total += $tip;
    $localNote = "added $tip";      // LOCAL: dies with the call
    echo "  inside: $localNote\n";
}

function visitCounter() {
    static $visits = 0;             // STATIC: survives between calls
    $visits++;
    return $visits;
}

addTip(15);
addTip(10);
echo "global total now: $total\n";

echo "via \$GLOBALS: ", $GLOBALS["total"], "\n";

echo "visits: ", visitCounter(), ", ", visitCounter(), ", ", visitCounter(), "\n";
// echo $localNote;  // would be empty - local scope!
?>
''',
       """<p>Three scopes in one program: <code>$localNote</code> vanishes when <code>addTip</code> ends; <code>global $total</code> (or <code>$GLOBALS['total']</code>) lets a function modify a script-level variable; <code>static $visits</code> is a local that <i>remembers</i> across calls - perfect for counters.</p>"""),

    PP("wd2p4", "Mathematical built-in functions", r'''
<?php
$bill = 102.789;
echo "round : ", round($bill), " / ", round($bill, 2), "\n";
echo "floor : ", floor($bill), "  ceil: ", ceil($bill), "\n";
echo "abs   : ", abs(-42), "\n";
echo "max   : ", max(250, 160, 320), "  min: ", min(250, 160, 320), "\n";
echo "pow   : ", pow(2, 10), "  sqrt: ", sqrt(144), "\n";
echo "intdiv: ", intdiv(17, 5), "  mod: ", 17 % 5, "\n";

echo "dice  : ", rand(1, 6), "  otp : ", random_int(1000, 9999), "\n";

// is_numeric checks form strings before calculating
$raw = "12.5";                      // as it would arrive from a form
echo "is_numeric('12.5'): ", var_export(is_numeric($raw), true), "\n";
if (is_numeric($raw)) {
    echo "per km for 40 km: Rs ", (float)$raw * 40, "\n";
}
?>
''',
       """<p>PHP's math library covers rounding (<code>round/floor/ceil</code>), magnitudes (<code>abs/max/min/pow/sqrt</code>), integer division (<code>intdiv</code>) and randomness (<code>rand</code>, <code>random_int</code> for OTPs). <code>is_numeric</code> validates string input <i>before</i> you trust it in arithmetic - the Unit 3 habit.</p>"""),

    PP("wd2p5", "Date and time functions", r'''
<?php
date_default_timezone_set("Asia/Kolkata");

echo "Today       : ", date("d M Y"), "\n";
echo "Full banner : ", date("l, jS F Y"), "\n";
echo "Time        : ", date("h:i A"), "\n";
echo "Timestamp   : ", time(), " seconds since 1970\n";

$travel = mktime(6, 30, 0, 11, 15, 2026);   // bus departs 15 Nov 06:30
echo "Travel day  : ", date("d M Y h:i A", $travel), "\n";

$days = (int)(($travel - time()) / 86400);
echo "Days to trip: $days\n";

echo "Next Monday : ", date("d M", strtotime("next Monday")), "\n";
echo "Deadline    : ", date("d M Y", strtotime("+7 days")), "\n";

// date_diff for exact gaps
$booked = date_create("2026-10-01");
$trip   = date_create("2026-10-29");
$gap    = date_diff($booked, $trip);
echo "Booked ", $gap->days, " days before travel\n";
?>
''',
       """<p><code>date()</code> renders any timestamp with format letters; <code>time()</code> is seconds-since-1970 (so <code>+86400</code> = tomorrow); <code>mktime()</code> builds timestamps, <code>strtotime()</code> parses English ("next Monday"), and <code>date_diff()</code> measures exact gaps between two dates - the booking-window calculation every ticket site needs.</p>"""),

    PP("wd2p6", "Indexed and associative arrays (Practical 7)", r'''
<?php
// INDEXED array: positions 0, 1, 2 ...
$cities = ["Surat", "Bharuch", "Vadodara"];
$cities[] = "Ahmedabad";            // append
echo "First stop: $cities[0]\n";
echo "Stops: ", count($cities), "\n";
foreach ($cities as $c) echo "  -> $c\n";

// ASSOCIATIVE array: named keys
$fare = ["SRT" => 250, "BRC" => 120, "AMD" => 160];
$fare["GANDHI"] = 300;              // add by key
$fare["SRT"] = 260;                 // overwrite
echo "Fare to AMD: Rs ", $fare["AMD"], "\n";
foreach ($fare as $code => $amt) {
    echo "  $code : Rs $amt\n";
}
unset($fare["BRC"]);                // delete a pair
echo "after unset: ", implode(", ", array_keys($fare)), "\n";
?>
''',
       """<p>Indexed arrays order items by position (auto keys from 0, append with <code>$a[]</code>); associative arrays pair <i>named</i> keys with values (<code>$fare['SRT']</code>). Add/overwrite by assigning a key, delete with <code>unset</code>, walk either with <code>foreach</code> - with <code>$k =&gt; $v</code> when keys matter.</p>"""),

    PP("wd2p7", "Multidimensional array: students table (Practical 7)", r'''
<?php
$students = [
    ["roll" => 7,  "name" => "Asha",  "marks" => ["SE" => 78, "Java" => 81, "IWD" => 69]],
    ["roll" => 12, "name" => "Bhuvi", "marks" => ["SE" => 91, "Java" => 66, "IWD" => 72]],
    ["roll" => 19, "name" => "Chirag","marks" => ["SE" => 55, "Java" => 74, "IWD" => 88]],
];

echo "Row 2 name      : ", $students[1]["name"], "\n";
echo "Row 3 IWD marks : ", $students[2]["marks"]["IWD"], "\n\n";

// nested foreach: whole table, with totals
foreach ($students as $s) {
    $sum = 0;
    foreach ($s["marks"] as $sub => $m) $sum += $m;
    printf("%-8s (roll %2d): total %d / 270\n", $s["name"], $s["roll"], $sum);
}
?>
''',
       """<p>Arrays inside arrays model a spreadsheet: each student is an associative record, <code>marks</code> is itself an associative array. Address with chained brackets (<code>$students[2]['marks']['IWD']</code>) and walk with nested <code>foreach</code> - outer lap per student, inner lap per subject. <code>printf</code> keeps columns neat.</p>"""),

    PP("wd2p8", "Processing array data: stats and filtering (Practical 8)", r'''
<?php
$bookings = [250, 160, 320, 480, 120, 260, 310];

$total = 0; $max = $bookings[0]; $min = $bookings[0];
foreach ($bookings as $amt) {
    $total += $amt;
    if ($amt > $max) $max = $amt;
    if ($amt < $min) $min = $amt;
}
$avg = $total / count($bookings);

echo "Bookings  : ", implode(", ", $bookings), "\n";
printf("Total Rs %d | avg Rs %.2f | max %d | min %d\n", $total, $avg, $max, $min);

// filter: premium bookings only (>= 300)
$premium = [];
foreach ($bookings as $amt) {
    if ($amt >= 300) $premium[] = $amt;
}
echo "Premium (>=300): ", implode(", ", $premium), "\n";

// map: format every amount as an HTML list item
foreach ($bookings as $amt) {
    $rows[] = "<li>Rs $amt</li>";
}
echo "as HTML:\n", implode("\n", $rows), "\n";
?>
''',
       """<p>The four array-processing archetypes in one file: <b>accumulate</b> (total/average), <b>extremes</b> (max/min via comparisons), <b>filter</b> (premium bookings into a new array) and <b>map</b> (each amount into an HTML <code>&lt;li&gt;</code>). <code>implode</code> flattens arrays back to displayable strings.</p>"""),

    PP("wd2p9", "Array function carnival (Practical 9)", r'''
<?php
$shopping = ["milk" => 62, "bread" => 45, "eggs" => 78, "tea" => 140];

echo "count     : ", count($shopping), "\n";
echo "in_array  : ", var_export(in_array(78, $shopping), true), "\n";
echo "key exists: ", var_export(array_key_exists("bread", $shopping), true), "\n";

// sort WITHOUT breaking name <-> price pairs
$cheap = $shopping;
asort($cheap);
echo "cheapest first -> ", implode(", ", array_map(fn($k,$v)=>"$k:$v", array_keys($cheap), $cheap)), "\n";

$list = ["Surat", "Vadodara", "Ahmedabad"];
sort($list);                        // renumbers keys 0..n - fine here
echo "sorted list : ", implode(", ", $list), "\n";

$merged = array_merge(["jam" => 95], $shopping);
echo "merged keys : ", implode(", ", array_keys($merged)), "\n";
echo "reversed    : ", implode(", ", array_reverse($list)), "\n";

array_push($list, "Gandhinagar");
echo "pushed/popped: ", array_pop($list), " popped; now ", count($list), "\n";

// list() unpacks slots; explode/implode bridge strings
list($a, $b, $c) = ["red", "green", "blue"];
echo "list() : $a | $b | $c\n";
echo "explode: ", count(explode(",", "12A,14C,3B")), " seat codes\n";
?>
''',
       """<p>Highlights: <code>asort</code> sorts by value <i>keeping keys glued</i> (<code>sort</code> renumbers and destroys names); <code>array_merge</code> glues arrays; <code>array_push/pop</code> treat the end like a stack; <code>list()</code> unpacks a small array into variables; <code>explode/implode</code> convert CSV text to arrays and back.</p>"""),

    PP("wd2p10", "Quoting styles: single, double, heredoc, nowdoc (Practical 10)", r'''
<?php
$city = "Surat";
$fare = 260;

echo 'single : Fare to $city is $fare', "\n";     // literal
echo "double : Fare to $city is Rs $fare\n";      // variables expand

// heredoc - multi-line block WITH interpolation (like double quotes)
echo <<<EOT
--- RECEIPT ---
Route : $city Express
Fare  : Rs {$fare}.00
Thanks for riding with us!
EOT;
echo "\n";

// nowdoc - multi-line AND literal (like single quotes)
echo <<<'EOT'
Sample code: echo "Fare: $fare";   // printed as-is
Useful for showing code or raw SQL text.
EOT;

echo "\nescapes: tab\\t works in double quotes only ->\t<- here\n";
echo "html escape: ", htmlspecialchars("<b>bold</b>"), "\n";
?>
''',
       """<p>Four ways to hold text: <i>single</i> quotes print everything literally; <i>double</i> quotes expand <code>$vars</code>; <b>heredoc</b> is a multi-line double-quoted block (markers at line starts); <b>nowdoc</b> (<code>&lt;&lt;&lt;'EOT'</code>) is its literal twin. Escapes like <code>\\t</code>/<code>\\n</code> work only in double-quoted/heredoc text, and <code>htmlspecialchars()</code> neutralises tags before echoing user content.</p>"""),

    PP("wd2p11", "String functions: search, replace, compare (Practical 10)", r'''
<?php
$name = "  Surat Express  ";
echo "strlen : ", strlen($name), "\n";                 // includes spaces!
echo "trim   : '", trim($name), "'\n";
echo "case   : ", strtoupper(trim($name)), " -> ", ucwords(strtolower(trim($name))), "\n";

$s = "Surat to Ahmedabad";
echo "substr : ", substr($s, 0, 5), " / ", substr($s, -9), "\n";

$pos = strpos($s, "to");
echo "strpos : ", var_export($pos, true), "\n";        // 6
echo "miss   : ", var_export(strpos($s, "zzz"),
    true), "  (== false would misfire on position 0)\n";
if (strpos($s, "Surat") === false) { echo "not found\n"; } else { echo "Surat found\n"; }
echo "stristr: ", stristr($s, "TO"), "\n";             // case-insensitive, rest-of-string

echo "replace: ", str_replace("to", "-", $s), "\n";
echo "strrev : ", strrev("madam"), "\n";
echo "repeat : ", str_repeat("-", 20), "\n";

echo "strcmp : ", strcmp("apple", "apply"), "  strcasecmp: ", strcasecmp("PHP", "php"), "\n";
echo "chr/ord: ", chr(65), " / ", ord("A"), "\n";
?>
''',
       """<p>The string toolkit: measure (<code>strlen</code>), clean (<code>trim</code>, case fixers), slice (<code>substr</code>, negative length reads from the end), locate (<code>strpos</code> 0-based or <b>false</b>; <code>stristr</code> case-insensitive), mutate (<code>str_replace</code>, <code>strrev</code>, <code>str_repeat</code>), compare (<code>strcmp/strcasecmp</code>) and hop between characters and codes (<code>chr/ord</code>). Golden rule: test <code>strpos(...) === false</code> - never <code>== false</code>.</p>"""),
]
