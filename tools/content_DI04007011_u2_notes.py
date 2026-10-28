"""DI04007011 Unit 2 notes: PHP Functions, Arrays and Strings. English only."""

from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_2_1 = {
    "title": {"en": "2.1 User-Defined Functions"},
    "items": [
        T("Defining and Calling Functions", """
<ul><li>A function packages a computation: <code>function name($param, ...) { ... return $value; }</code>. Call it by name with arguments: <code>fare(265)</code>.</li>
<li><b>Parameters</b> are the inputs at the doorway; <b>arguments</b> are the actual values handed in. <code>return</code> sends exactly one value back (return an array to smuggle out several).</li>
<li>PHP functions are <b>global</b> once defined - callable from anywhere below or above in the file - and names are case-insensitive (<code>FARE()</code> works, but use the declared spelling).</li>
<li>Discipline: a function <b>computes</b>; it does not echo banners. Output is the caller's choice - this keeps functions reusable across pages.</li>
<li>Vocabulary: <i>define</i> once, <i>call</i> many times. Total of messy copy-paste &rarr; one tested function.</li></ul>
""", diagram="wd2_anatomy", programs=["wd2p1"]),
        T("Arguments: Defaults, Return Values, By Value vs By Reference", """
<ul><li><b>Default parameters</b>: <code>function fare($km, $rate = 1.2)</code> - callers may skip trailing parameters; <code>fare(265)</code> uses the default rate, <code>fare(265, 1.5)</code> overrides it. Required parameters come first, optional ones last.</li>
<li><b>By value</b> (default): PHP hands the function a <i>copy</i> - changing <code>$n</code> inside leaves the caller's variable untouched.</li>
<li><b>By reference</b>: prefix <code>&</code> - <code>function addTip(&amp;$total)</code> - and the function borrows the caller's actual variable; changes stick. Classic uses: <code>swap($a,$b)</code>, accumulating into a result array.</li>
<li>Same trick inside the signature and at call time: <code>sort($arr)</code> is built-in by-reference - that is why it changes your array without returning it.</li>
<li>Rule of thumb: default to by-value; reach for <code>&amp;</code> only when the function's job is to modify its argument.</li></ul>
""", diagram="wd2_value_ref", programs=["wd2p2"]),
        T("Variable Scope: Local, Global and Static", """
<ul><li><b>Local scope</b>: variables created inside a function live and die with the call - the outside world cannot see <code>$tip</code>, and the function cannot see your <code>$total</code>.</li>
<li><b>Global scope</b>: script-level variables. Open the window deliberately with <code>global $total;</code> inside the function, or use the super-global array <code>$GLOBALS['total']</code>.</li>
<li><b>Static locals</b>: <code>static $calls = 0;</code> survives between calls of the same function - a visit counter without globals.</li>
<li>Good style: pass inputs as parameters, return outputs - treat <code>global</code> as a last resort (hard to test, easy to tangle).</li></ul>
""", diagram="wd2_scope", programs=["wd2p3"]),
    ],
}

SEC_2_2 = {
    "title": {"en": "2.2 Built-in Functions: Math and Date-Time"},
    "items": [
        T("Mathematical Built-ins", """
<ul><li>Rounding family: <code>round($x, 2)</code>, <code>floor()</code>, <code>ceil()</code> - money displays always round.</li>
<li>Magnitudes: <code>abs()</code>, <code>max(...)</code>, <code>min(...)</code>, <code>pow($b, $e)</code>, <code>sqrt()</code>; integer division <code>intdiv(17, 5)</code> &rarr; 3.</li>
<li>Randomness: <code>rand(1, 6)</code> or <code>random_int(1, 6)</code> for cryptographic-quality picks (OTPs, dice).</li>
<li>Type shapers: <code>(int)$s</code>, <code>(float)$s</code> casts; checkers <code>is_numeric()</code> (true for "12.5") - Unit 3 uses these on every form field.</li>
<li>All and more live at php.net - knowing they exist beats memorising signatures.</li></ul>
""", programs=["wd2p4"]),
        T("Date and Time Functions", """
<ul><li><code>date(\"format\")</code> renders the current moment: <code>d M Y</code> &rarr; 29 Oct 2026; <code>date(\"H:i\")</code> &rarr; 24h time. Format letters: d D m M y Y H h i s a l.</li>
<li><code>time()</code> returns the Unix timestamp (seconds since 1970) - arithmetic-ready (<code>time() + 86400</code> = tomorrow).</li>
<li><code>mktime(h, m, s, month, day, year)</code> builds a timestamp; wrap in <code>date()</code> to read it.</li>
<li><code>strtotime(\"next Monday\")</code> parses English into a timestamp - surprisingly capable for booking deadlines.</li>
<li>Intervals and differences: <code>date_create()</code>/<code>date_diff()</code> or <code>DateTime::diff</code> give exact day gaps ("booked 12 days before travel").</li>
<li>Set the zone once for India: <code>date_default_timezone_set(\"Asia/Kolkata\")</code>.</li></ul>
""", programs=["wd2p5"]),
    ],
}

SEC_2_3 = {
    "title": {"en": "2.3 Arrays: Indexed, Associative, Multidimensional"},
    "items": [
        T("Indexed and Associative Arrays (Practical 7)", """
<ul><li>One <b>ordered map</b> type serves both habits. <b>Indexed</b>: numeric keys auto-assigned from 0 - <code>$cities = [\"Surat\", \"Vadodara\"];</code>, read with <code>$cities[0]</code>.</li>
<li><b>Associative</b>: named keys - <code>$fare = [\"SRT\" =&gt; 250, \"AMD\" =&gt; 160];</code>, read with <code>$fare['SRT']</code>. Keys are strings or ints; quotes only around strings.</li>
<li>Create empty <code>$a = [];</code> and append with <code>$a[] = $v;</code> (indexed) or <code>$a['key'] = $v;</code> (associative). Add, overwrite, delete with <code>unset($a['key'])</code>.</li>
<li>Arrays are PHP's workhorse: form data (<code>$_POST</code>), database rows and config are all associative arrays.</li></ul>
""", diagram="wd2_array_types", programs=["wd2p6"]),
        T("Multidimensional Arrays (Practical 7)", """
<ul><li>Arrays inside arrays: a list of students, each <code>[&quot;roll&quot; =&gt; 7, &quot;name&quot; =&gt; &quot;Asha&quot;, &quot;marks&quot; =&gt; [78, 81, 69]]</code> - three dimensions deep.</li>
<li>Address precisely: <code>$students[2]['marks'][1]</code> reads row 2, sub-array, position 1.</li>
<li>Nested <code>foreach</code> walks the table naturally - an outer lap per record, an inner lap per field.</li>
<li>Mental image: rows of a spreadsheet stored in PHP memory; Unit 5 swaps this for real MySQL tables with the same shape.</li></ul>
""", programs=["wd2p7"]),
        T("Traversing and Processing Array Data (Practical 8)", """
<ul><li><code>foreach ($a as $v)</code> streams values; <code>foreach ($a as $k =&gt; $v)</code> streams keys too - the idiomatic PHP loop.</li>
<li>Common processing patterns: <b>sum/count &rarr; average</b>; <b>max/min via comparisons</b>; <b>filter into a new array</b> (only bookings above Rs 200); <b>map</b> (format every row as an HTML <code>&lt;li&gt;</code>).</li>
<li>The manual gearbox exists too: <code>current()</code>, <code>next()</code>, <code>prev()</code>, <code>end()</code>, <code>reset()</code> move an internal pointer - foreach resets and drives it for you.</li>
<li>Keep loops readable: give the value variable a real name (<code>$booking</code>, not <code>$x</code>).</li></ul>
""", diagram="wd2_foreach_map", programs=["wd2p8"]),
        T("Array Library Functions (Practical 9)", """
<ul><li>Measure: <code>count($a)</code>; search: <code>in_array($v, $a)</code>, <code>array_search($v, $a)</code> (returns key), <code>array_key_exists()</code>.</li>
<li>Order: <code>sort()</code>/<code>rsort()</code> renumber keys (0..n) - fine for lists, <b>fatal for assoc keys</b>; use <code>asort()</code>, <code>arsort()</code> (by value) or <code>ksort()</code>/<code>krsort()</code> (by key) to keep pairs glued.</li>
<li>Combine and reshape: <code>array_merge()</code>, <code>array_reverse()</code>, <code>array_slice()</code>, <code>array_unique()</code>.</li>
<li>Stack ends: <code>array_push()</code>/<code>array_pop()</code> (end), <code>array_shift()</code>/<code>array_unshift()</code> (front).</li>
<li>Bridges: <code>implode(', ', $a)</code> (array &rarr; string), <code>explode(',', $s)</code> (string &rarr; array), <code>list($x, $y) = $pair</code> unpacks; <code>each()</code> is long-deprecated - use foreach.</li></ul>
""", diagram="wd2_array_funcs", programs=["wd2p9"]),
    ],
}

SEC_2_4 = {
    "title": {"en": "2.4 Strings"},
    "items": [
        T("Quoting Styles: Single, Double, Heredoc, Nowdoc", """
<ul><li><b>Single quotes</b>: literal text - <code>'$fare'</code> prints a dollar sign, not a value. <b>Double quotes</b>: interpolate variables - <code>\"Fare: $fare\"</code> expands in place.</li>
<li><b>Heredoc</b>: <code>echo &lt;&lt;&lt;EOT ... EOT;</code> - multi-line block that behaves like double quotes; perfect for HTML receipts with variables.</li>
<li><b>Nowdoc</b>: <code>&lt;&lt;&lt;'EOT'</code> (quoted marker) - multi-line AND literal; perfect for raw SQL or code samples.</li>
<li>Escapes inside double quotes: <code>\\n</code> newline, <code>\\t</code> tab, <code>\\$</code> literal dollar, <code>\\\\</code> backslash.</li>
<li>Before echoing user data into HTML, escape with <code>htmlspecialchars()</code> - the first rule of safe output (Unit 3 drills it).</li></ul>
""", diagram="wd2_quotes", programs=["wd2p10"]),
        T("String Library Functions: Search, Replace, Compare (Practical 10)", """
<ul><li>Shape: <code>strlen()</code>, <code>strtolower()</code>/<code>strtoupper()</code>, <code>ucfirst()</code>/<code>ucwords()</code>, <code>trim()</code>/<code>ltrim()</code>/<code>rtrim()</code>, <code>substr($s, 0, 3)</code>.</li>
<li>Find: <code>strpos($hay, $needle)</code> (0-based position or <b>false</b>), <code>strrpos()</code> (last), <code>stristr()</code>/<code>strstr()</code> (rest of string from match), case-insensitive twins carry the <code>i</code>.</li>
<li>Change: <code>str_replace($find, $with, $s)</code>, <code>substr_replace()</code>, <code>strrev()</code>, <code>str_repeat()</code>, <code>wordwrap()</code>.</li>
<li>Compare: <code>strcmp()</code>/<code>strcasecmp()</code> return negative/zero/positive - feed <code>usort()</code> callbacks.</li>
<li>Characters: <code>chr(65)</code> &rarr; "A", <code>ord('A')</code> &rarr; 65 for code-point tricks.</li>
<li><b>Trap</b>: when a needle is NOT found, strpos returns <code>false</code> - but position <code>0</code> is also falsy, so always test with <code>=== false</code>.</li></ul>
""", diagram="wd2_string_funcs", programs=["wd2p11"]),
    ],
}

NOTES = [SEC_2_1, SEC_2_2, SEC_2_3, SEC_2_4]
