"""DI04007011 Unit 1 notes: Introduction to PHP. English only."""

from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_1_1 = {
    "title": {"en": "1.1 PHP and the Web Environment"},
    "items": [
        T("What is PHP: History and Advantages", """
<ul><li><b>PHP</b> originally stood for <i>Personal Home Page tools</i> - created by <b>Rasmus Lerdorf in 1994-95</b> to track visitors to his online resume. Today the name is a recursive acronym: <b>PHP: Hypertext Preprocessor</b>.</li>
<li>It is a <b>server-side scripting language</b> embedded inside HTML: the server executes the PHP code and ships plain HTML to the browser.</li>
<li><b>Advantages</b>: free and open-source; runs on Windows/Linux/macOS; the classic partner of MySQL; easy to learn (C-like syntax, no compilation step); a gigantic ecosystem - <b>WordPress, Wikipedia, Facebook (historically)</b> - and massive documentation at php.net.</li>
<li>Interpreted per-request: edit the file, refresh the browser - no build, no deploy ceremony. This is why tutorials (and hostels full of student projects) start with PHP.</li>
<li>Current lineage: PHP 4 (Zend engine) &rarr; PHP 5 (OOP) &rarr; PHP 7 (2x speed, scalar types) &rarr; PHP 8.x (JIT, modern syntax). Our examples run on PHP 8.</li></ul>
"""),
        T("The Client-Server Request Cycle", """
<ul><li><b>Client</b>: the browser - sends an HTTP request for a page, renders the returned HTML. <b>Server</b>: Apache with the PHP engine - executes scripts and answers with generated HTML.</li>
<li>The browser <b>never sees PHP source</b>; it receives only the echo'ed output. Server-side means logic, passwords and database credentials stay on the server.</li>
<li>One cycle: URL typed &rarr; request travels &rarr; PHP engine runs the script &rarr; flat HTML returns &rarr; browser renders. Every page view repeats it.</li>
<li>Dynamic means <i>generated per request</i>: the same seat-status page shows 37 seats now, 2 seats an hour later - one script, infinite HTML pages.</li></ul>
""", diagram="wd1_client_server"),
        T("The 3-Tier Architecture of a Web Application", """
<ul><li><i>Presentation tier</i> (browser, HTML/CSS) &rarr; <i>Application tier</i> (Apache + PHP, business logic) &rarr; <i>Data tier</i> (MySQL tables, files).</li>
<li>On a developer laptop all three tiers live together (XAMPP); in production they may be three different machines - the tiers communicate over HTTP and SQL.</li>
<li>Layer pay-off: change the database without touching the pages; reskin the pages without touching the logic. Each tier minds its own business.</li>
<li>PHP sits in the application tier: it receives browser data through forms (Unit 3), remembers users via sessions (Unit 4) and talks to MySQL (Unit 5).</li></ul>
""", diagram="wd1_3tier"),
    ],
}

SEC_1_2 = {
    "title": {"en": "1.2 Setting Up: XAMPP and the First Page"},
    "items": [
        T("Installing XAMPP and Running Your First Page (Practicals 1-2)", """
<ul><li><b>XAMPP</b> = X (any OS) + <b>A</b>pache + <b>M</b>ariaDB/MySQL + <b>P</b>HP + <b>P</b>erl - one installer packs the whole 3-tier lab. Cousins: WAMP (Windows), LAMP (Linux), MAMP (macOS).</li>
<li>Install flow: download from apachefriends.org &rarr; install &rarr; open the XAMPP control panel &rarr; <b>Start Apache</b> (and MySQL later, Unit 5). Apache must show green before any page works.</li>
<li>Web root: the folder <code>C:\\xampp\\htdocs</code> (Windows) or <code>/opt/lampp/htdocs</code> (Linux). Save <code>hello.php</code> there and browse <code>http://localhost/hello.php</code>.</li>
<li>Troubleshooting reflexes: <b>404</b> = the file is not under htdocs (or wrong name); <b>source code visible</b> = saved as .html instead of .php, or Apache off; <b>blank page</b> = PHP error - check the Apache error log.</li>
<li>The CLI (<code>php file.php</code>) is a second, server-free way to run PHP - every program in this unit is verified with the PHP 8 CLI, exactly as shown.</li></ul>
""", diagram="wd1_xampp", programs=["wd1p1"]),
    ],
}

SEC_1_3 = {
    "title": {"en": "1.3 Embedding, echo/print, and the Type System"},
    "items": [
        T("Embedding PHP in HTML; echo, print and Comments", """
<ul><li>PHP code lives inside <code>&lt;?php ... ?&gt;</code> tags, which may appear <b>any number of times, anywhere</b> in an .html skeleton saved as a .php file. The engine replaces each island with the output it generates.</li>
<li><code>echo</code> writes output - accepts several comma-separated values, no parentheses needed, returns nothing (slightly faster). <code>print</code> outputs one value and returns 1, so it can sit inside an expression (rarely used).</li>
<li><b>Comments</b>: <code>// line</code>, <code># line</code> and <code>/* block */</code>. Comments never reach the browser - they are for the next reader of the source.</li>
<li>Every PHP statement ends with a semicolon; missing <code>;</code> is the classic first-parse-error. Short open tag <code>&lt;?= $x ?&gt;</code> is a shortcut for <code>&lt;?php echo $x ?&gt;</code>.</li></ul>
""", diagram="wd1_embed", programs=["wd1p2"]),
        T("Variables, Constants and Data Types", """
<ul><li>Variables start with <b>$</b> and a letter/underscore: <code>$seatCount = 40;</code>. No type declaration - the value decides the type, and it can change (<b>loose/dynamic typing</b>).</li>
<li>PHP is <b>case-sensitive for variables</b> (<code>$Seat</code> &ne; <code>$seat</code>) but case-insensitive for keywords and function names.</li>
<li>Scalars: <b>int, float, string, bool</b>; compound: <b>array, object</b>; plus <b>NULL</b> and <b>resource</b>. Inspect any variable with <code>var_dump($x)</code> (type + value) or query with <code>gettype($x)</code>.</li>
<li><b>Constants</b>: <code>define(\"GST\", 0.18)</code> or <code>const GST = 0.18;</code> - no $ sign, global by default, immutable.</li>
<li>Strings in <b>double quotes interpolate variables</b> (<code>\"Fare: Rs $fare\"</code>); single quotes print them literally. Concatenation uses the <b>dot</b> operator: <code>\"Hello \" . $name</code>.</li></ul>
""", diagram="wd1_datatypes", programs=["wd1p3", "wd1p4"]),
        T("Operators and Expressions", """
<ul><li>Families: <b>arithmetic</b> (+ - * / % **), <b>assignment</b> (= += .=), <b>comparison</b> (== === != &lt;&gt; &lt; &gt; &lt;=&gt;), <b>logical</b> (&amp;&amp; || ! and or), <b>string</b> (. .=), <b>increment</b> (++$i $i--).</li>
<li><b>Loose vs strict comparison</b>: <code>==</code> juggles types (<code>5 == \"5\"</code> is true); <code>===</code> also demands the same type (<code>5 === \"5\"</code> is false). Form data arrives as strings - always compare with <code>===</code>/casts.</li>
<li>Spaceship <code>&lt;=&gt;</code> returns -1, 0 or 1 (less, equal, greater) - built for sort callbacks.</li>
<li>Precedence: ** then * / %, then + -, comparisons last before &amp;&amp;, ||. When in doubt, parenthesise - clarity beats cleverness.</li>
<li>The dot family matters daily: building HTML strings means <code>$msg .= \"&lt;li&gt;$item&lt;/li&gt;\"</code> style accumulation.</li></ul>
""", diagram="wd1_operators"),
    ],
}

SEC_1_4 = {
    "title": {"en": "1.4 Conditional Structures"},
    "items": [
        T("if, if-else and else-if Chains", """
<ul><li><code>if (cond) { ... }</code> runs the block only when the condition is truthy. Add <code>else { ... }</code> for the alternative, or chain <code>elseif</code> for tested ladders (grade calculators, fare slabs).</li>
<li>Once one branch matches, the rest are skipped - order the ladder carefully (test the highest slab first).</li>
<li>Truthy/falsy shorthand: <code>0, \"\", \"0\", NULL, false, []</code> count as false; almost everything else is true. <code>if ($seats)</code> reads as "if any seats remain".</li>
<li>The <b>ternary</b> <code>$label = ($marks &gt;= 40) ? \"Pass\" : \"Fail\";</code> compresses a two-way choice into one expression - ideal inside echo statements.</li>
<li>Always brace even one-liners in team code: braced blocks survive the next edit.</li></ul>
""", diagram="wd1_ifelif", programs=["wd1p5"]),
        T("switch-case: One Expression, Many Routes", """
<ul><li><code>switch ($day) { case \"Mon\": ...; break; ... default: ... }</code> compares one expression against many constant values - cleaner than a long elseif ladder when the test is equality.</li>
<li><b>break</b> ends each case; forget it and execution <i>falls through</i> into the next case (occasionally intentional, usually a bug).</li>
<li><code>default</code> handles everything unmatched - put it last, like the safety net of an else.</li>
<li>Use switch for menus, day names, status codes; use if-elseif for ranges (<code>$marks &gt;= 70</code>) and compound conditions.</li></ul>
""", programs=["wd1p6"]),
    ],
}

SEC_1_5 = {
    "title": {"en": "1.5 Looping Structures"},
    "items": [
        T("for, while, do-while and foreach", """
<ul><li><b>for</b> <code>(init; test; step)</code> - the counted loop: multiplication tables, seat numbers 1..40.</li>
<li><b>while</b> - pre-checked condition loop: runs zero or more times; classic for reading database rows (<code>while ($row = ...)</code>) once Unit 5 begins.</li>
<li><b>do-while</b> - body first, test after: guaranteed <b>one execution</b>, natural for menu/retry patterns ("show menu, ask again while the choice is invalid").</li>
<li><b>foreach</b> <code>($arr as $v)</code> or <code>($arr as $k =&gt; $v)</code> - PHP's signature loop for arrays; Unit 2 fills it with real data. No off-by-one, no counter boilerplate.</li>
<li>Pick by intent: known count &rarr; for; unknown count &rarr; while; at-least-once &rarr; do-while; collections &rarr; foreach.</li></ul>
""", diagram="wd1_loops", programs=["wd1p7"]),
        T("break and continue: Steering the Loop", """
<ul><li><code>break</code> leaves the loop immediately - e.g. stop searching once the seat is found.</li>
<li><code>continue</code> skips the rest of this lap and jumps to the next iteration - e.g. skip printing taken seats, or skip multiples of 3.</li>
<li>Both act on the <b>innermost</b> enclosing loop by default; <code>break 2;</code> escapes two levels (rare, use sparingly).</li>
<li>Wisdom: a well-shaped condition usually beats a forest of flags and breaks; keep loop bodies small enough to read at a glance.</li></ul>
""", programs=["wd1p8"]),
    ],
}

NOTES = [SEC_1_1, SEC_1_2, SEC_1_3, SEC_1_4, SEC_1_5]
