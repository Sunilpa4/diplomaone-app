"""DI04007011 Unit 3 notes: Working with Data and Forms. English only."""

from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_3_1 = {
    "title": {"en": "3.1 Creating Forms and Reading Data"},
    "items": [
        T("HTML Form Controls (Practical 11)", """
<ul><li>A form wraps controls: <code>&lt;form method=\"post\" action=\"register.php\"&gt;</code> ... inputs ... <code>&lt;input type=\"submit\"&gt;</code> <code>&lt;/form&gt;</code>. Omit <code>action</code> and the form posts back to its own page.</li>
<li>The control kit: <b>text box</b> (name, city), <b>password</b> (masked), <b>text area</b> (feedback), <b>radio</b> (one-of-many, same <code>name</code>), <b>checkbox</b> (many-of-many; use <code>name=\"hobby[]\"</code> to receive an array), <b>select/option</b> (dropdown), HTML5 types <b>date, color, email, number, file</b>, and <b>buttons</b>.</li>
<li><b>The name attribute is everything</b>: it becomes the key in <code>$_GET</code>/<code>$_POST</code>. A control without a <code>name</code> submits nothing.</li>
<li>Group radios by shared name; give every option a distinct <code>value</code> - the browser sends the value, not the label.</li></ul>
""", diagram="wd3_form_controls", programs=["wd3p1"]),
        T("Submitting Data: GET vs POST", """
<ul><li><b>GET</b> packs data into the URL query string (<code>?city=Surat&amp;seats=2</code>): visible, bookmarkable, limited (~2 KB), and retried freely on refresh. Use for <b>searches and filters</b>.</li>
<li><b>POST</b> sends data in the request body: invisible in the URL, effectively unlimited, required for uploads. Use for anything that <b>changes state</b> (register, book, pay).</li>
<li>Never put passwords or personal data in a GET URL - they land in browser history and server logs.</li>
<li>Refreshing a POST page re-submits (the classic double-booking hazard) - solved with the Post/Redirect/Get pattern in real apps.</li></ul>
""", diagram="wd3_get_post", programs=["wd3p2"]),
        T("Reading Data: The Superglobals", """
<ul><li><code>$_GET</code> and <code>$_POST</code> are associative arrays of the incoming parameters; <code>$_REQUEST</code> merges both (plus cookies - prefer the specific one).</li>
<li><code>$_FILES</code> carries upload records: <code>name, type, size, tmp_name, error</code> per file field.</li>
<li><code>$_SERVER</code> describes the request: <code>REQUEST_METHOD</code>, <code>SCRIPT_NAME</code>, <code>REMOTE_ADDR</code>, headers. <code>$_ENV</code> holds environment variables; <code>$GLOBALS</code> every script-global variable.</li>
<li>All superglobals are available in <b>every scope</b> - no <code>global</code> declaration needed inside functions.</li>
<li><code>$_SESSION</code> and <code>$_COOKIE</code> complete the family in Unit 4.</li></ul>
""", diagram="wd3_superglobals", programs=["wd3p3"]),
        T("The Self-Processing Page Pattern", """
<ul><li>One <code>.php</code> page both shows and handles a form: <code>if ($_SERVER['REQUEST_METHOD'] === 'POST') { validate + process } else { show form }</code>.</li>
<li>Advantages: errors are shown beside the same form; entered values are re-echoed (sticky form) so users fix one field, not ten.</li>
<li>Sticky values: <code>value=\"&lt;?php echo htmlspecialchars($name ?? ''); ?&gt;\"</code> - echo what the user typed, escaped.</li>
<li>Collect messages in an <code>$errors</code> array; show the list above the form when not empty.</li></ul>
""", diagram="wd3_selfprocess"),
    ],
}

SEC_3_2 = {
    "title": {"en": "3.2 Validating User Data (Practical 12)"},
    "items": [
        T("The Validation Toolkit", """
<ul><li>Presence: <code>isset($_POST['name'])</code> (exists, may be null-safe), <code>empty($v)</code> (missing or blank). Start every field with these two.</li>
<li>Shape: <code>is_numeric()</code>, <code>strlen($s) &gt;= 3</code>, <code>ctype_alpha()</code>; <code>filter_var($email, FILTER_VALIDATE_EMAIL)</code> returns the value or false; <code>filter_var($n, FILTER_VALIDATE_INT)</code> likewise for integers.</li>
<li>Clean before checking: <code>trim()</code> strips edge spaces; <code>stripslashes()</code> removes stray escapes; cast numbers with <code>(int)</code>.</li>
<li>Rules live <b>server-side only</b>: HTML <code>required</code>/<code>maxlength</code> hints are trivially bypassed - the server is the bouncer, not the browser.</li>
<li>After validating, remember output safety separately: <code>htmlspecialchars()</code> on every echo of user data.</li></ul>
""", diagram="wd3_validation", programs=["wd3p4"]),
        T("Validated Registration Form (Practicals 11-12)", """
<ul><li>Put it together: self-processing page + sticky values + <code>$errors</code> list + per-field rules.</li>
<li>Typical rules: name required, letters-minimum-3; email <code>filter_var(..., FILTER_VALIDATE_EMAIL)</code>; mobile exactly 10 digits; age numeric 15-100; route from an allowed list; terms checkbox must be set.</li>
<li>Only when <code>count($errors) === 0</code> do you accept: show the confirmation/summary, then (Units 4-5) remember the user or save to MySQL.</li>
<li>Sanity sample: our program posts <code>email=not-an-email, age=abc</code> - watch the validator catch both while echoing the rest back.</li></ul>
""", programs=["wd3p5"]),
    ],
}

SEC_3_3 = {
    "title": {"en": "3.3 Directories and Text Files"},
    "items": [
        T("Working with Directories", """
<ul><li>Create and remove: <code>mkdir(\"uploads\")</code>, <code>rmdir(\"uploads\")</code> (only when empty); probe with <code>is_dir()</code>/<code>file_exists()</code>.</li>
<li>List contents: <code>scandir($dir)</code> returns everything (includes <code>.</code> and <code>..</code> - skip them); <code>glob(\"uploads/*.png\")</code> filters by pattern.</li>
<li>Inspect files: <code>is_file()</code>, <code>filesize()</code>, <code>filemtime()</code> (last modified), <code>basename()</code>/<code>pathinfo()</code> split names and extensions.</li>
<li>Housekeeping mantra: check <code>is_dir()</code> before <code>mkdir()</code>, and never trust a filename from a browser - rebuild it yourself.</li></ul>
""", programs=["wd3p6"]),
        T("Reading and Writing Text Files (Practical 13)", """
<ul><li>Explicit trio: <code>$h = fopen(\"feedback.txt\", \"a\")</code> &rarr; <code>fwrite($h, $line)</code> / <code>fgets($h)</code> &rarr; <code>fclose($h)</code>. Modes: <code>r</code> read, <code>w</code> write-and-truncate, <code>a</code> append, <code>+</code> variants add the other direction.</li>
<li>Shortcuts: <code>file_get_contents()</code> reads whole; <code>file_put_contents($f, $t, FILE_APPEND)</code> appends in one call; <code>file()</code> returns an array of lines; <code>fputcsv()</code> writes CSV rows safely.</li>
<li>The feedback practical carries the full cycle: POST form &rarr; validate &rarr; append one CSV line &rarr; display all stored feedback.</li>
<li>Always check <code>fopen</code>'s return (<code>false</code> = permission/path problem) before writing.</li></ul>
""", diagram="wd3_files", programs=["wd3p7", "wd3p8"]),
    ],
}

SEC_3_4 = {
    "title": {"en": "3.4 Uploads, Downloads and Email"},
    "items": [
        T("Uploading and Downloading Files (Practical 14)", """
<ul><li>The form needs <code>method=\"post\"</code> and <code>enctype=\"multipart/form-data\"</code>; without the enctype, no file travels.</li>
<li>Server side: <code>$_FILES['avatar']</code> holds <code>name, type, size, tmp_name, error</code>. If <code>error === UPLOAD_ERR_OK</code>, the file waits in a temp folder - <code>move_uploaded_file($tmp, \"uploads/\".$safe)</code> or it vanishes.</li>
<li>Verify: check the extension whitelist and size limit, confirm with <code>getimagesize()</code> that an image really is one, and <code>basename()</code> the name to strip path tricks.</li>
<li>Thumbnail cheat without GD: store once, display with a fixed <code>&lt;img width=\"64\"&gt;</code> - the browser scales it.</li>
<li>Download: reply with headers - <code>Content-Type: application/octet-stream</code> and <code>Content-Disposition: attachment; filename=\"...\"</code> - then <code>readfile()</code> the contents.</li></ul>
""", diagram="wd3_upload", programs=["wd3p9", "wd3p10"]),
        T("Sending Email: Plain, HTML and Attachments (Practical 15)", """
<ul><li><code>mail($to, $subject, $message, $headers)</code> - headers carry <code>From</code>, <code>Cc</code>, <code>Reply-To</code>, and the MIME content type.</li>
<li>Plain text: default body - just send. <b>HTML email</b>: add <code>Content-Type: text/html; charset=UTF-8</code> and compose the body with tags.</li>
<li><b>Attachments</b> need MIME multipart: a boundary string, the message part, then the file base64-encoded - real projects use PHPMailer instead of hand-rolled MIME.</li>
<li>On XAMPP localhost, <code>mail()</code> returns false until an SMTP account is configured (sendmail.ini / Mercury) - so our program composes and displays the exact messages first, then reports the send attempt honestly.</li>
<li>Newsletter flow: validate email &rarr; store subscriber &rarr; send confirmation (plain + HTML versions).</li></ul>
""", diagram="wd3_email", programs=["wd3p11"]),
    ],
}

NOTES = [SEC_3_1, SEC_3_2, SEC_3_3, SEC_3_4]
