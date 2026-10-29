"""DI04007011 Unit 3 extras: key-term cards, viva, exam (practical-task) questions."""

from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Form cards", [
        SXE("form skeleton", """<form method="post">
  <input name="city">
  <select name="route">...
  <button>Go</button>
</form>
no name => no data""",
            "name = server-side key"),
        SXE("when which", """GET    reads (search, filter)
       url ?a=1&b=2, ~2KB
POST   changes (register, pay)
       body, unlimited, files""",
            "never passwords in a URL"),
        SXE("checkbox array", """<input type="checkbox"
  name="hobby[]" value="art">
arrives as array:
$_POST["hobby"] = ["art", ...]""",
            "[] suffix collects many"),
    ]),
    G("Validation cards", [
        SXE("field rules", "isset($v)      exists?\nempty($v)      blank?\nis_numeric($v) number?\nstrlen($v) >= 3 long enough?\nin_array strict   listed?",
            "presence first, rules next"),
        SXE("filter_var", """filter_var($e,
  FILTER_VALIDATE_EMAIL)
-> value or false
FILTER_VALIDATE_INT same""",
            "false = reject, value = accept"),
        SXE("escape rule", """htmlspecialchars($userText)
before ANY echo of user data
< becomes &lt;   & becomes &amp;""",
            "validate in, escape out"),
    ]),
    G("File and mail cards", [
        SXE("file modes", """"r" read (must exist)
"w" write, TRUNCATES
"a" append (creates)
"w+" truncates, then reads""",
            "fopen work fclose"),
        SXE("one-liners", """file_get_contents($f)
file_put_contents($f,$t,
  FILE_APPEND)
file($f) -> array of lines
fputcsv / fgetcsv""",
            "skip the trio for quick jobs"),
        SXE("upload bits", """$_FILES['f'] has
name type size tmp_name error
error === 0 ? then
move_uploaded_file(tmp, dest)""",
            "tmp file dies with request"),
        SXE("mail()", """mail($to, $subj, $body, $hdrs);
plain  = bare body
html   = Content-Type: text/html
attach = MIME multipart""",
            "localhost needs SMTP config"),
    ]),
]

_VIVA = [
    VE("What two attributes does every form control need to submit data?", "name (the key PHP sees) and value (what is sent); without name, the control submits nothing."),
    VE("Radio vs checkbox?", "Radios share one name and submit ONE value (gender); checkboxes are independent - use name=\"x[]\" to collect many into an array."),
    VE("Difference between text input and textarea?", "Text input is single-line (name, city); textarea is multi-line with rows/cols (feedback)."),
    VE("Name three HTML5 input types and their benefit.", "date / color / email / number - the browser shows a native picker and basic client-side checking."),
    VE("What does the submit button actually do?", "Fires an HTTP request to the form's action URL carrying every named control; no action attribute means post back to the same page."),
    VE("GET vs POST - two key differences?", "GET puts data in the URL (visible, bookmarkable, ~2KB limit); POST puts it in the request body (hidden, unlimited, required for uploads)."),
    VE("When should a form use GET?", "For read-only actions: search, filter, paginate - anything you could safely bookmark."),
    VE("Why must passwords never travel by GET?", "URLs live in browser history and server logs - anyone with access reads the password."),
    VE("What is $_POST?", "The associative superglobal array of parameters sent in the request body of a POST."),
    VE("$_REQUEST holds what exactly?", "GET + POST (+ cookies) merged - convenient but vague; prefer the specific $_GET/$_POST."),
    VE("Which superglobal tells you the request method?", "$_SERVER['REQUEST_METHOD'] - 'GET' or 'POST'."),
    VE("What does $_FILES contain per upload?", "name, type, size, tmp_name, error - the facts PHP gathered about the uploaded file."),
    VE("Why are superglobals 'super'?", "They are visible in every scope - usable inside functions without global declarations."),
    VE("Explain the self-processing page pattern.", "One file: if REQUEST_METHOD==='POST' validate/process, else render the form; actionless form posts to itself."),
    VE("What is a sticky form?", "A form re-rendered with the user's previous values echoed back into each field (escaped) - fix one error, keep the rest."),
    VE("Why validate on the server even with HTML required?", "Client-side rules are hints that anyone can bypass; the server is the only trustworthy checkpoint."),
    VE("isset() vs empty()?", "isset checks the key exists (and isn't null); empty catches missing, '', 0, '0', null, false, [] - beware '0' counts as empty."),
    VE("What does filter_var do with an email?", "FILTER_VALIDATE_EMAIL returns the email if valid, false otherwise - one call replaces regexes."),
    VE("Validation vs escaping - same thing?", "No: validation guards INPUT (rules on arrival), escaping (htmlspecialchars) guards OUTPUT (safe echo). Both, always."),
    VE("What does stripslashes() do?", "Removes escape backslashes from text - mostly a legacy-magic-quotes cleanup, kept for completeness."),
    VE("fopen modes r, w, a?", "r: read (file must exist); w: write after truncating; a: append, creating the file if missing."),
    VE("One-call alternatives to fopen/fwrite/fclose?", "file_put_contents($f, $text, FILE_APPEND) to write, file_get_contents($f) to read, file($f) for an array of lines."),
    VE("What does fputcsv do?", "Writes one array as a proper CSV line - quotes and escapes commas/newlines correctly."),
    VE("How do you list a directory's contents?", "scandir($dir) (skip '.' and '..') or glob('uploads/*.png') for pattern-filtered lists."),
    VE("mkdir gotcha?", "Check is_dir() first and remember rmdir only removes EMPTY directories."),
    VE("What does pathinfo() give you?", "dirname, basename, filename and extension of a path - extension extraction without string surgery."),
    VE("Which enctype does an upload form need?", "multipart/form-data with method post - without it $_FILES stays empty."),
    VE("Why must uploaded files be moved?", "The upload waits in a temporary location (tmp_name) that PHP deletes when the request ends - move_uploaded_file() saves it permanently."),
    VE("What checks before accepting an upload?", "error === UPLOAD_ERR_OK, size limit, extension whitelist, getimagesize() to confirm image type, basename() the name."),
    VE("What is basename()'s security role?", "It strips directory paths from the submitted name (../../ tricks), so uploads cannot escape the target folder."),
    VE("How does a page force a download?", "Send Content-Type: application/octet-stream plus Content-Disposition: attachment; filename=\"x\" headers, then the bytes (readfile)."),
    VE("mime_content_type or getimagesize - which for images?", "getimagesize - it returns pixel dimensions too and proves the file really is an image."),
    VE("mail() signature?", "mail($to, $subject, $message, $headers) - headers carry From, Reply-To and the MIME Content-Type."),
    VE("Plain vs HTML email?", "Plain is the bare body; HTML adds the header Content-Type: text/html; charset=UTF-8 so clients render tags."),
    VE("How are attachments sent?", "MIME multipart: boundary, message part, then the file base64-encoded - in practice use PHPMailer."),
    VE("Why does mail() often return false on XAMPP locally?", "No SMTP server is configured for localhost - set sendmail.ini/SMTP settings (or Gmail SMTP) before it can send."),
]

VIVA = [
    G("Forms and Controls", _VIVA[0:8]),
    G("Superglobals and Patterns", _VIVA[8:15]),
    G("Validation and Files", _VIVA[15:26]),
    G("Uploads, Downloads, Email", _VIVA[26:36]),
]

assert len(_VIVA) == 36, len(_VIVA)

EXAM_QS = [
    XE("Design a bus-passenger registration form using text, email, date, radio, checkbox array, dropdown and textarea controls. (Practical 11)", 6),
    XE("Differentiate GET and POST with examples; when must a form use POST?", 4),
    XE("Write a PHP page that demonstrates $_GET, $_POST and $_REQUEST on a single form.", 4),
    XE("Explain the self-processing form pattern with REQUEST_METHOD and sticky values; why is it preferred?", 4),
    XE("Validate a registration form: name 3+ letters, valid email via filter_var, numeric age 15-100, route from an allowed list, terms accepted. Show the $errors pattern. (Practical 12)", 6),
    XE("Why is server-side validation mandatory even when HTML provides required and type=email?", 3),
    XE("Write a program demonstrating mkdir, scandir, glob, pathinfo, filesize, unlink and cleanup.", 6),
    XE("Write the feedback practical: POST form, validate non-empty, append a timestamped line to feedback.txt, then display all stored feedback. (Practical 13)", 6),
    XE("Compare fopen modes r, w, a, w+ and the file_get_contents/file_put_contents shortcuts.", 4),
    XE("Write the image-upload practical: enctype, $_FILES checks (error, size, extension), basename, move_uploaded_file, thumbnail display. (Practical 14)", 6),
    XE("Explain the three headers that turn a PHP response into a file download.", 3),
    XE("Write the newsletter practical: validate email, store the subscriber, compose plain and HTML bodies, show headers, attempt mail(). Why does mail() fail on localhost? (Practical 15)", 6),
    XE("Explain validation vs escaping as two separate duties, with htmlspecialchars example.", 3),
    XE("List every index of $_FILES['photo'] and explain the role of tmp_name.", 4),
]
