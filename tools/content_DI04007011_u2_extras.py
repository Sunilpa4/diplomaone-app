"""DI04007011 Unit 2 extras: key-term cards, viva, exam (practical-task) questions."""

from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Function cards", [
        SXE("define + call", """function fare($km, $rate = 1.2) {
    return $km * $rate;
}
echo fare(265);       // 318
echo fare(265, 1.5);  // override""",
            "defaults cover skipped args"),
        SXE("value vs ref", """function f($n)   copy   safe
function f(&$n)  & = caller's box
swap($a,$b) needs &
sort($a) is built-in &""",
            "default copy; & modifies"),
        SXE("scope trio", """local   $tip dies with call
global  global $t; / $GLOBALS['t']
static  static $c remembers""",
            "pass in, return out"),
    ]),
    G("Array cards", [
        SXE("make + walk", """$c = ["Surat","Bharuch"];
$f = ["SRT"=>250];
$c[] = "AMD";        append
foreach ($f as $k=>$v) {...}""",
            "positions or named keys"),
        SXE("sort family", """sort / rsort   renumber keys
asort / arsort by VALUE keep keys
ksort / krsort by KEY""",
            "assoc arrays need asort/ksort"),
        SXE("toolbox", """count in_array array_merge
array_reverse array_push/pop
implode(",",$a) explode(",",$s)
list($a,$b) = $pair;""",
            "measure find glue flip unpack"),
    ]),
    G("String cards", [
        SXE("four quotes", """'literal $x'
"expands $x"
<<<EOT multi-line with vars EOT;
<<<'EOT' multi-line raw EOT;""",
            "heredoc = doubles, nowdoc = singles"),
        SXE("shape strings", """strlen trim ltrim rtrim
strtolower strtoupper ucwords
substr($s, 0, 3)
substr($s, -3) from the end""",
            "measure clean slice"),
        SXE("find + change", """strpos($h, $n) 0-based / false
=== false is the ONLY safe test
str_replace strrev str_repeat
strcmp strcasecmp chr ord""",
            "0 is position, not 'found nothing'"),
    ]),
]

_VIVA = [
    VE("How do you define and call a PHP function?", "function fare($km) { ... return $v; } defines it globally; call by name with arguments: fare(265)."),
    VE("Parameters vs arguments?", "Parameters are the placeholders in the definition ($km); arguments are the actual values at the call (265)."),
    VE("What does return do?", "Hands exactly one value back to the caller and ends the function; return an array when you need several results."),
    VE("What are default (optional) parameters?", "Parameters with preset values - function f($km, $rate = 1.2); callers may omit them; required params come first."),
    VE("Passing by value vs by reference?", "By value passes a copy (default - caller's variable is safe); &$n passes the original, so the function can modify it (swap, accumulate)."),
    VE("Why does sort($a) change the array without returning?", "sort is a built-in pass-by-reference function - it edits the caller's array directly."),
    VE("What is variable scope?", "Where a variable is visible: function locals die with the call; script-level globals sit outside; neither sees the other by default."),
    VE("How do you access a global inside a function?", "Declare global $total; at the top of the function, or use $GLOBALS['total'] - the super-global array."),
    VE("What is a static local variable?", "static $c = 0; inside a function keeps its value between calls - a private counter."),
    VE("Why prefer parameters over global?", "Globals tangle dependencies and are hard to test; parameters + return keep functions self-contained and reusable."),
    VE("Name six mathematical built-ins.", "round, floor, ceil, abs, max/min, pow, sqrt, intdiv, rand/random_int."),
    VE("round vs floor vs ceil?", "round() nearest (optional decimals); floor() always down; ceil() always up - money displays use round($x, 2)."),
    VE("rand() vs random_int()?", "Both pick integers in a range; random_int is cryptographically secure - use it for OTPs and anything security-related."),
    VE("What does is_numeric(\"12.5\") return?", "true - it validates numeric-looking strings before you calculate with form input."),
    VE("What does date('d M Y') produce?", "e.g. 29 Oct 2026 - date() renders a timestamp using format letters (default: right now)."),
    VE("What is a Unix timestamp?", "Seconds elapsed since 1 Jan 1970 (UTC); time() returns it - arithmetic-ready, e.g. +86400 is tomorrow."),
    VE("mktime vs strtotime?", "mktime(h,m,s,mon,day,year) builds a timestamp from parts; strtotime('next Monday') parses English text into a timestamp."),
    VE("How do you compute days between two dates?", "date_diff(date_create($a), date_create($b))->days - or subtract timestamps and divide by 86400."),
    VE("Why set date_default_timezone_set?", "So date/time functions speak local time - Asia/Kolkata for Indian projects; otherwise they use UTC."),
    VE("What are the two indexing habits of PHP arrays?", "Indexed arrays have numeric keys from 0; associative arrays map named keys to values - one ordered-map type serves both."),
    VE("How do you append to an array?", "$a[] = $v; for the next numeric slot, or $a['key'] = $v; under a named key; unset($a['key']) deletes."),
    VE("Read $students[2]['marks'][1]?", "Third element (index 2), its 'marks' sub-array, element 1 - chained brackets descend dimensions."),
    VE("Give a real use of a multidimensional array.", "A students table: each element is a record [roll, name, marks[subject=>score]] - a spreadsheet in memory."),
    VE("Two forms of foreach?", "foreach ($a as $v) for values; foreach ($a as $k => $v) when keys matter - it resets the array pointer automatically."),
    VE("What do current(), next(), end() do?", "They walk the array's internal pointer manually - foreach drives this pointer for you."),
    VE("sort vs asort - the danger?", "sort renumbers keys 0..n, destroying assoc key names; asort sorts by value keeping key-value pairs intact (ksort by key)."),
    VE("in_array vs array_key_exists?", "in_array($v,$a) searches VALUES; array_key_exists('k',$a) searches KEYS; array_search returns the matching key."),
    VE("array_push/array_pop do what?", "Add/remove at the END - stack behaviour; array_shift/unshift work the front."),
    VE("implode and explode?", "implode(',', $a) joins an array into a string; explode(',', $s) splits a string into an array - the CSV bridge."),
    VE("What does list() do?", "Unpacks array slots into named variables: list($r, $g, $b) = [255, 128, 0];"),
    VE("Difference between single and double quotes?", "Single quotes are literal ('$x' prints $x); double quotes interpolate variables (\"$x\" expands). Which escapes work? \\n \\t \\$ only in double quotes/heredoc."),
    VE("What is heredoc?", "&lt;&lt;&lt;EOT ... EOT; - a multi-line string that expands variables, like double quotes without quote juggling."),
    VE("What is nowdoc?", "&lt;&lt;&lt;'EOT' ... EOT; - heredoc's literal twin: multi-line, no interpolation; ideal for raw code/SQL text."),
    VE("Why htmlspecialchars() before echoing user text?", "It neutralises < > & \" ' into entities so user input cannot inject HTML/JS into your pages."),
    VE("strlen/substr examples?", "strlen('Surat') = 5; substr('Surat', 0, 3) = 'Sur'; substr('Surat', -3) = 'rat' (negative = from the end)."),
    VE("strpos gotcha?", "Returns 0-based position OR false; position 0 is falsy, so test === false or you misread a match at the start."),
    VE("strstr vs stristr?", "Both return the haystack from the first needle onward; stristr ignores case. strpos only returns a position."),
    VE("strcmp return values?", "Negative / zero / positive for less / equal / greater - feeds usort comparison callbacks; strcasecmp ignores case."),
    VE("chr and ord?", "chr(65) -> 'A'; ord('A') -> 65 - convert between characters and ASCII/byte codes."),
    VE("Which Unit 2 functions would power a grade sheet?", "A marks array per student, foreach totals, max/min, asort for rank order, and a function returning the grade ladder from Unit 1."),
]

VIVA = [
    G("Functions and Scope", _VIVA[0:10]),
    G("Math and Date Built-ins", _VIVA[10:19]),
    G("Arrays", _VIVA[19:30]),
    G("Strings", _VIVA[30:40]),
]

assert len(_VIVA) == 40, len(_VIVA)

EXAM_QS = [
    XE("Explain user-defined functions in PHP: definition, calling, parameters vs arguments, return value - with an example. (Practical 6)", 6),
    XE("Explain default parameters. Write fare($km, $rate = 1.2) and show calls that use and override the default.", 4),
    XE("Distinguish pass-by-value from pass-by-reference. Write swap(&$a, &$b) and prove the difference with output. (Practical 6)", 6),
    XE("Explain local, global and static scope with one small program demonstrating all three.", 6),
    XE("Write a program demonstrating six mathematical built-ins (round, floor, ceil, max, pow, random_int).", 4),
    XE("Write a program that prints today's date in two formats, a travel date built with mktime, and the days remaining until the trip.", 6),
    XE("Create an indexed array of cities and an associative array of code-to-fare pairs; append, update, delete and display both. (Practical 7)", 6),
    XE("Build a multidimensional student table (roll, name, marks per subject) and print each student's total with nested foreach. (Practical 7)", 6),
    XE("Process a bookings array: total, average, maximum, minimum, and a filtered list of premium bookings (>= 300). (Practical 8)", 6),
    XE("Demonstrate count, in_array, asort, ksort, array_merge, array_reverse, array_push/pop and implode on one array. Explain why sort() endangers associative arrays. (Practical 9)", 6),
    XE("Compare single quotes, double quotes, heredoc and nowdoc with a receipt-printing example. (Practical 10)", 4),
    XE("Write a program demonstrating strlen, trim, strtoupper, ucwords, substr, strpos (with the === false rule), str_replace, strrev, strcmp, chr and ord. (Practical 10)", 6),
    XE("A page must display user comments - explain the quoting and escaping choices (double quotes + htmlspecialchars) and show one safe echo.", 4),
    XE("Write a function gstSlab($amount) returning the GST-inclusive fare, used by three different routes - emphasise why functions beat copy-paste.", 4),
]
