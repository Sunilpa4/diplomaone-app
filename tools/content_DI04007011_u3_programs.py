"""DI04007011 Unit 3 - solved PHP programs. Form/upload demos run on a real php -S server via curl."""

from php_content import PP

PROGRAMS = [
    PP("wd3p1", "Registration form with every control (Practical 11)", r'''
<?php
// register.php - self-processing registration form (Practical 11)
if ($_SERVER["REQUEST_METHOD"] === "POST" || !empty($_GET)) {
    echo "<h2>Registration received</h2>";
    echo "Method used : <b>", $_SERVER["REQUEST_METHOD"], "</b><br>";
    foreach ($_REQUEST as $field => $value) {
        $value = is_array($value) ? implode(", ", $value) : htmlspecialchars($value);
        echo htmlspecialchars($field), " = <b>$value</b><br>";
    }
    exit;
}
?>
<!DOCTYPE html><html><head><title>BusBook Registration</title></head><body>
<h2>Passenger Registration</h2>
<form method="get">
  Name:    <input type="text" name="name"><br>
  Email:   <input type="email" name="email"><br>
  Journey: <input type="date" name="jdate"><br>
  Seat colour: <input type="color" name="tint"><br>
  Gender:  <input type="radio" name="gender" value="F">F
           <input type="radio" name="gender" value="M">M<br>
  City:    <select name="city">
             <option>Surat</option><option>Vadodara</option><option>Ahmedabad</option>
           </select><br>
  Extras:  <input type="checkbox" name="extras[]" value="meal">Meal
           <input type="checkbox" name="extras[]" value="insurance">Insurance<br>
  Message: <textarea name="msg" rows="2" cols="24"></textarea><br>
  <input type="submit" value="Register">
</form>
</body></html>
''',
       """<p>Every control carries a <code>name</code> - that name becomes the array key server-side. Radios share one name (one value wins); checkboxes with <code>extras[]</code> arrive as an <b>array</b>. The handler loops <code>$_REQUEST</code> generically, escaping each value - it prints whatever the form sent. We demo with a GET submit so the URL itself shows the data.</p>""",
       request={"method": "GET", "query": {"name": "Ravi Patel", "email": "ravi@gmail.com", "jdate": "2026-11-15", "tint": "#2266aa", "gender": "M", "city": "Surat", "extras[]": ["meal", "insurance"], "msg": "Window seat please"}}),

    PP("wd3p2", "GET vs POST side by side on one page", r'''
<?php
// one page, two forms - compare how the same data travels
echo "<h3>Gate report</h3>";
echo "REQUEST_METHOD: <b>", $_SERVER["REQUEST_METHOD"], "</b><br>";
echo "\$_GET   : ", json_encode($_GET), "<br>";
echo "\$_POST  : ", json_encode($_POST), "<br>";
echo "\$_REQUEST: ", json_encode($_REQUEST), "<br>";
?>
<form method="get">
  Search route: <input name="q" placeholder="GET - stays in URL">
  <button>Search</button>
</form>
<form method="post">
  Register PIN: <input type="password" name="pin" placeholder="POST - hidden body">
  <button>Register</button>
</form>
''',
       """<p>Same key names, different lanes: a GET submit fills <code>$_GET</code> (and the browser address bar); a POST fills <code>$_POST</code>; <code>$_REQUEST</code> merges them. Try both forms and compare the URL bar. <code>json_encode</code> gives a compact honest dump of each super-global.</p>""",
       request={"method": "POST", "data": {"pin": "4407"}}),

    PP("wd3p3", "Superglobals tour: $_SERVER, $_ENV, $GLOBALS", r'''
<?php
$appName = "BusBook";          // lives in $GLOBALS

echo "=== \$_SERVER ===\n";
echo "method     : ", $_SERVER["REQUEST_METHOD"], "\n";
echo "script     : ", $_SERVER["SCRIPT_NAME"], "\n";
echo "server     : ", $_SERVER["SERVER_NAME"], ":", $_SERVER["SERVER_PORT"], "\n";
echo "user-agent : ", $_SERVER["HTTP_USER_AGENT"] ?? "(none)", "\n";
echo "query str  : ", $_SERVER["QUERY_STRING"] ?: "(empty)", "\n\n";

echo "=== \$_ENV (sample) ===\n";
echo "PATH set?  ", isset($_ENV["PATH"]) ? "yes" : "no", "\n\n";

echo "=== \$GLOBALS ===\n";
echo "appName via \$GLOBALS: ", $GLOBALS["appName"], "\n";
echo "some keys: ", implode(", ", array_slice(array_keys($GLOBALS), 0, 6)), " ...\n";

echo "\n=== \$_GET from the URL ===\n";
print_r($_GET);
?>
''',
       """<p>Superglobals are pre-filled associative arrays visible in every scope. <code>$_SERVER</code> reveals the request line, script path and client agent; <code>$_ENV</code> the environment; <code>$GLOBALS</code> every global variable by name. The curl query lands in <code>$_GET</code> exactly as typed.</p>""",
       request={"method": "GET", "query": {"src": "web", "debug": "1"}}),

    PP("wd3p4", "Validation functions laboratory (Practical 12)", r'''
<?php
// isolate each validator and watch it judge real values
$cases = [
    ["isset",     isset($_POST["ghost"]) ? "true" : "false (ghost never submitted)"],
    ["empty('')", var_export(empty(""), true)],
    ["empty('0')", var_export(empty("0"), true) . "  <- surprise! '0' is empty"],
    ["is_numeric('12.5')", var_export(is_numeric("12.5"), true)],
    ["is_numeric('12a')",  var_export(is_numeric("12a"), true)],
    ["strlen('Surat') >= 3", var_export(strlen("Surat") >= 3, true)],
    ["strlen('ab') >= 3",    var_export(strlen("ab") >= 3, true)],
    ["filter email ok",      var_export(filter_var("a@b.com", FILTER_VALIDATE_EMAIL), true)],
    ["filter email bad",     var_export(filter_var("a@b", FILTER_VALIDATE_EMAIL), true)],
    ["filter int '42'",      var_export(filter_var("42", FILTER_VALIDATE_INT), true)],
    ["filter int '4.2'",     var_export(filter_var("4.2", FILTER_VALIDATE_INT), true)],
    ["trim('  x  ')",        "'" . trim("  x  ") . "'"],
    ["stripslashes",         stripslashes("surat\\'s")],
    ["htmlspecialchars",     htmlspecialchars("<script>alert(1)</script>")],
];
foreach ($cases as [$fn, $verdict]) {
    printf("%-24s -> %s\n", $fn, $verdict);
}
?>
''',
       """<p>Each validator answers one narrow question. Traps worth remembering: <code>empty(\"0\")</code> is true (string zero counts as empty); <code>filter_var</code> returns <b>false</b> on failure and the <i>value</i> on success; <code>htmlspecialchars</code> converts dangerous characters into entities for safe echoing. Compose these into per-field rules.</p>"""),

    PP("wd3p5", "Validated, sticky self-processing form (Practicals 11-12)", r'''
<?php
$errors = [];
$name = trim($_POST["name"] ?? "");
$email = trim($_POST["email"] ?? "");
$age = trim($_POST["age"] ?? "");
$route = $_POST["route"] ?? "";
$allowedRoutes = ["Surat-Bharuch", "Surat-Vadodara", "Surat-Ahmedabad"];

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (strlen($name) < 3)                                  $errors[] = "Name needs 3+ letters";
    if (!filter_var($email, FILTER_VALIDATE_EMAIL))         $errors[] = "Email looks wrong";
    if (!is_numeric($age) || $age < 15 || $age > 100)       $errors[] = "Age must be 15-100";
    if (!in_array($route, $allowedRoutes, true))            $errors[] = "Pick a listed route";
    if (empty($_POST["terms"]))                             $errors[] = "Accept the terms";

    if (!$errors) {
        echo "<h3>Welcome aboard, ", htmlspecialchars($name), "!</h3>";
        echo "Seat on <b>$route</b> reserved for age $age.<br>";
        echo "Confirmation sent to ", htmlspecialchars($email), "<br>";
        exit;
    }
}
?>
<?php if ($errors): ?>
<b>Fix these:</b><ul>
<?php foreach ($errors as $e) echo "<li>$e</li>"; ?>
</ul>
<?php endif; ?>
<form method="post">
  Name: <input name="name" value="<?= htmlspecialchars($name) ?>"><br>
  Email: <input name="email" value="<?= htmlspecialchars($email) ?>"><br>
  Age: <input name="age" value="<?= htmlspecialchars($age) ?>"><br>
  Route: <select name="route">
    <?php foreach ($allowedRoutes as $r): ?>
      <option <?= $r === $route ? "selected" : "" ?>><?= $r ?></option>
    <?php endforeach; ?>
  </select><br>
  <input type="checkbox" name="terms" value="yes"> I accept the terms<br>
  <button>Register</button>
</form>
''',
       """<p>The complete pattern: gather + trim input, apply per-field rules into <code>$errors</code>, re-render the same form with the list on top and <b>sticky values</b> echoed back (escaped). Only a clean <code>$errors</code> reaches the welcome message. The demo posts a bad email and non-numeric age - both get caught while good fields survive.</p>""",
       request={"method": "POST", "data": {"name": "Ravi", "email": "not-an-email", "age": "abc", "route": "Surat-Ahmedabad", "terms": "yes"}}),

    PP("wd3p6", "Working with directories", r'''
<?php
$base = __DIR__ . "/arena";

echo "mkdir arena          : ", var_export(@mkdir($base), true), "\n";
echo "mkdir arena/logs     : ", var_export(mkdir("$base/logs"), true), "\n";
echo "is_dir(arena)        : ", var_export(is_dir($base), true), "\n";

file_put_contents("$base/a.txt", "alpha");
file_put_contents("$base/b.log", "beta");
file_put_contents("$base/logs/run.log", "run 1");

echo "scandir              : ", implode(", ", scandir($base)), "\n";
echo "glob *.txt           : ", implode(", ", array_map("basename", glob("$base/*.txt"))), "\n";

$info = pathinfo("$base/b.log");
echo "pathinfo b.log       : ", $info["extension"], " ext / ", $info["filename"], " name\n";
echo "filesize a.txt       : ", filesize("$base/a.txt"), " bytes\n";
echo "last modified        : ", date("H:i:s", filemtime("$base/a.txt")), "\n";

unlink("$base/a.txt"); unlink("$base/b.log"); unlink("$base/logs/run.log");
rmdir("$base/logs"); rmdir($base);
echo "cleanup              : ", is_dir($base) ? "still there" : "all gone", "\n";
?>
''',
       """<p>Directory toolkit: <code>mkdir/rmdir</code>, <code>is_dir/file_exists</code> probes, <code>scandir</code> (skip <code>.</code>/<code>..</code>), <code>glob</code> pattern filters, <code>pathinfo</code> to split extensions, <code>filesize/filemtime</code> for facts, <code>unlink</code> for files. Create-before-use and clean-up-after are the two habits.</p>"""),

    PP("wd3p7", "Feedback form saving to a text file (Practical 13)", r'''
<?php
$file = __DIR__ . "/feedback.txt";
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = trim($_POST["name"] ?? "");
    $msg  = trim($_POST["msg"] ?? "");
    if ($name !== "" && $msg !== "") {
        $line = date("Y-m-d H:i") . "," . $name . "," . str_replace(["\n", ","], " ", $msg) . "\n";
        file_put_contents($file, $line, FILE_APPEND);
        echo "<b>Thanks $name - feedback saved.</b><br>";
    }
}
if (file_exists($file)) {
    echo "<h4>All feedback so far:</h4><pre>";
    echo htmlspecialchars(file_get_contents($file));
    echo "</pre>";
}
?>
<form method="post">
  Name: <input name="name"><br>
  Feedback: <textarea name="msg"></textarea><br>
  <button>Send feedback</button>
</form>
''',
       """<p>Full Practical-13 cycle: POST the feedback, validate non-empty, flatten newlines/commas (CSV-friendly), append one stamped line with <code>file_put_contents(..., FILE_APPEND)</code>, then <b>read the file back</b> and show every previous entry (escaped). Refresh-submit adds another line - the file is the database until Unit 5.</p>""",
       request={"method": "POST", "data": {"name": "Asha", "msg": "Loved the window seats!"}}),

    PP("wd3p8", "File modes cookbook: r / w / a / w+", r'''
<?php
$f = __DIR__ . "/log.txt";

// "w" - fresh write (truncates anything old)
$h = fopen($f, "w"); fwrite($h, "day 1: server up\n"); fclose($h);

// "a" - append keeps history
$h = fopen($f, "a"); fwrite($h, "day 2: added route BRC\n"); fclose($h);

// "r" - read line by line
echo "== read with fgets ==\n";
$h = fopen($f, "r");
while (!feof($h)) {
    $line = fgets($h);
    if ($line === false) break;
    echo "  " . rtrim($line) . "\n";
}
fclose($h);

// shortcuts
file_put_contents($f, "day 3: backup done\n", FILE_APPEND);
echo "== read whole at once ==\n";
echo file_get_contents($f);

// "w+" truncates then allows reading too
$h = fopen($f, "w+");
fwrite($h, "fresh start\n");
rewind($h);
echo "== w+ after truncate ==\n  " . rtrim(fgets($h)) . "\n";
fclose($h);
?>
''',
       """<p>Same file, four moods: <code>w</code> rewrites from scratch (old content gone), <code>a</code> appends to the end, <code>r</code> reads with <code>fgets + feof</code>, and <code>w+</code> truncates <i>then</i> lets you read back (<code>rewind</code> returns the pointer home). The <code>file_get_contents</code>/<code>file_put_contents</code> pair handles most cases in one call.</p>"""),

    PP("wd3p9", "Image upload with checks (Practical 14)", r'''
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_FILES["avatar"])) {
    $f = $_FILES["avatar"];

    if ($f["error"] !== UPLOAD_ERR_OK) {
        echo "Upload failed (error code {$f['error']}).<br>";
    } elseif ($f["size"] > 500000) {
        echo "File too large (max 500 KB).<br>";
    } elseif (!in_array(strtolower(pathinfo($f["name"], PATHINFO_EXTENSION)), ["png", "jpg", "jpeg", "gif"])) {
        echo "Only png/jpg/gif images allowed.<br>";
    } else {
        $saveDir = __DIR__ . "/uploads";
        if (!is_dir($saveDir)) mkdir($saveDir);
        $safe = basename($f["name"]);                    // strip path tricks
        $dest = "$saveDir/$safe";
        if (move_uploaded_file($f["tmp_name"], $dest)) {
            $d = getimagesize($dest);
            echo "Uploaded <b>$safe</b> ({$f['size']} bytes, {$d[0]}x{$d[1]} px).<br>";
            echo "<img src='uploads/$safe' width='64' alt='avatar thumbnail'>";
            echo " <- thumbnail via <i>img width</i>";
        }
    }
    exit;
}
?>
<form method="post" enctype="multipart/form-data">
  Avatar: <input type="file" name="avatar"><br>
  <button>Upload</button>
</form>
''',
       """<p>The gate in order: <b>error code OK</b> &rarr; size limit &rarr; extension whitelist &rarr; <code>getimagesize</code> confirms image-ness &rarr; <code>basename()</code> sanitises the name &rarr; <code>move_uploaded_file()</code> relocates the temp file before it vanishes. The thumbnail trick needs no image library: store once, render small with <code>&lt;img width=\"64\"&gt;</code>. Our 1x1 png demo passes every gate.</p>""",
       request={"method": "UPLOAD"}, upload=("avatar", "ravi-avatar.png")),

    PP("wd3p10", "Download a file with header()", r'''
<?php
// download.php?file=report.txt - forces a save-as dialog
$known = ["report.txt" => "Surat Express daily report\nBookings: 34\nRevenue: Rs 8,900\n"];
$name = $_GET["file"] ?? "";
if (!isset($known[$name])) {
    echo "Unknown file requested.";
    exit;
}
header("Content-Type: application/octet-stream");
header("Content-Disposition: attachment; filename=\"$name\"");
header("Content-Length: " . strlen($known[$name]));
echo $known[$name];
?>
''',
       """<p>Three headers change a page into a download: <code>Content-Type: application/octet-stream</code>, <code>Content-Disposition: attachment; filename=...</code>, and <code>Content-Length</code>. The browser pops a save dialog instead of rendering. <code>curl -i</code> shows the genuine response headers - look for Content-Disposition below. Real sites stream with <code>readfile()</code> after these headers.</p>""",
       request={"method": "GET", "query": {"file": "report.txt"}, "show_headers": True}),

    PP("wd3p11", "Newsletter subscription with plain + HTML email (Practical 15)", r'''
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = trim($_POST["email"] ?? "");
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email address.<br>";
    } else {
        file_put_contents(__DIR__ . "/subscribers.txt", $email . "\n", FILE_APPEND);

        $to = $email;
        $subject = "Welcome to BusBook Updates";

        // ---- plain text version (always send one) ----
        $plain = "Hi!\n\nThanks for subscribing to BusBook route alerts.\n"
               . "Unsubscribe anytime: http://localhost/unsub.php?e=" . urlencode($email);

        // ---- HTML version (needs the MIME header) ----
        $html = "<html><body style='font-family:sans-serif'>"
              . "<h2 style='color:#1565C0'>Welcome aboard!</h2>"
              . "<p>Thanks for subscribing to <b>BusBook</b> route alerts.</p>"
              . "<ul><li>Weekly fare drops</li><li>New route news</li></ul>"
              . "</body></html>";

        $headers = "From: BusBook <admin@busbook.in>\r\n"
                 . "Reply-To: support@busbook.in\r\n"
                 . "Content-Type: text/html; charset=UTF-8\r\n";

        echo "== would send PLAIN ==\n$plain\n\n";
        echo "== would send HTML ==\n$html\n\n";
        echo "headers:\n$headers\n";
        $ok = @mail($to, $subject, $html, $headers);   // no SMTP on localhost
        echo "mail() returned: ", $ok ? "true (sent)" : "false (no SMTP configured - expected on localhost)", "\n";
        echo "subscriber recorded in subscribers.txt\n";
    }
    exit;
}
?>
<form method="post">
  Email: <input name="email" type="email"><br>
  <button>Subscribe</button>
</form>
''',
       """<p>Practical 15 end-to-end: validate the email, persist the subscriber, then compose <b>both</b> a plain-text and an HTML body (the <code>Content-Type: text/html</code> header switches the client into rendering mode; <code>From</code>/<code>Reply-To</code> ride in <code>$headers</code>). <code>mail()</code> returns false on an unconfigured localhost - we show the exact messages and the honest status instead of pretending.</p>""",
       request={"method": "POST", "data": {"email": "ravi.patel@gmail.com"}}),
]
