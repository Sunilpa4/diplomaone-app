"""Content helpers for PHP (Introduction to Web Development) – English only.

Runs every program with a real PHP 8.4 - CLI for logic demos, or the built-in
web server + curl for form/upload/session demos - so every shown output is genuine.
Note bodies use @@name@@ code snippets (make_TP from py_content).
"""
import base64, html, os, random, re, socket, subprocess, tempfile, time, urllib.parse
from py_content import make_TP, reflow, code_block          # language-neutral helpers
from c_content import SXE, VE, XE, G

PHP_ROOT = "/home/user/php_root"
if not os.path.isdir(PHP_ROOT):
    PHP_ROOT = "/tmp/phproot"
PHP_BIN = os.path.join(PHP_ROOT, "usr", "bin", "php8.4")
PHP_ENV = dict(os.environ, LD_LIBRARY_PATH=os.path.join(PHP_ROOT, "usr", "lib", "x86_64-linux-gnu"))
if os.path.isdir(os.path.join(PHP_ROOT, "conf.d")):
    PHP_ENV["PHP_INI_SCAN_DIR"] = os.path.join(PHP_ROOT, "conf.d")

TINY_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==")


def run_php(code, fname="index.php", env_extra=None, timeout=60):
    """Run a PHP program with the local PHP 8.4 CLI; return '$ php <file>' + genuine stdout/stderr."""
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, fname)
        os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(fname) else None
        with open(path, "w", encoding="utf-8") as f:
            f.write(code.strip("\n") + "\n")
        env = dict(PHP_ENV)
        if env_extra:
            env.update(env_extra)
        cp = subprocess.run([PHP_BIN, fname], cwd=d, env=env, capture_output=True, text=True, timeout=timeout)
    out = cp.stdout
    if cp.returncode != 0 and cp.stderr and cp.stderr.strip() not in out:
        out += ("\n" if out and not out.endswith("\n") else "") + cp.stderr
    return f"$ php {fname}\n" + out.rstrip("\n")


def _free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def run_web(code, fname="index.php", request=None, extra=None, upload=None, assets=None, timeout=60, env_extra=None):
    """Serve PHP and issue genuine HTTP requests using curl.

    request may be one dict (backwards-compatible) or a list of steps. Each step
    accepts method, path, query, data, headers, show_headers, follow_redirects and
    label. A sequence shares a curl cookie jar, just like one browser. Set
    cookies=False on a step to simulate a different, fresh browser.
    capture={name: regex} extracts a value from the response for later steps;
    {{name}} in later data/query/header values substitutes that captured value.
    upload=(field, filename) uploads the bundled tiny PNG. The PHP session store
    and cookie jar are isolated per run and deleted afterwards.
    """
    steps = request if isinstance(request, list) else [request or {}]
    assert steps, "run_web needs at least one request"
    captured = {}
    env = dict(PHP_ENV)
    if env_extra:
        env.update(env_extra)

    def expand(value):
        if isinstance(value, dict):
            return {k: expand(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [expand(v) for v in value]
        if isinstance(value, str):
            for k, v in captured.items():
                value = value.replace("{{" + k + "}}", v)
        return value

    with tempfile.TemporaryDirectory() as d:
        docroot = os.path.join(d, "www")
        sessions = os.path.join(d, "sessions")
        os.makedirs(docroot)
        os.makedirs(sessions)
        cookie_jar = os.path.join(d, "cookies.txt")
        for name, src in {fname: code, **(extra or {})}.items():
            p = os.path.join(docroot, name)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(src.strip("\n") + "\n")
        for rel, blob in (assets or {}).items():
            p = os.path.join(docroot, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "wb") as f:
                f.write(blob)
        port = _free_port()
        with open(os.path.join(d, "server.log"), "w+") as log:
            srv = subprocess.Popen(
                [PHP_BIN, "-d", "session.save_path=" + sessions,
                 "-S", f"127.0.0.1:{port}", "-t", docroot],
                stdout=log, stderr=subprocess.STDOUT,
                env=env, text=True, cwd=docroot)
            transcripts = []
            try:
                for _ in range(60):
                    try:
                        with socket.create_connection(("127.0.0.1", port), timeout=0.5):
                            break
                    except OSError:
                        if srv.poll() is not None:
                            log.seek(0)
                            raise RuntimeError("PHP server exited: " + log.read())
                        time.sleep(0.05)
                else:
                    raise RuntimeError("PHP server did not start")
                for step in steps:
                    method = step.get("method", "GET").upper()
                    data = expand(step.get("data"))
                    path = step.get("path", fname).lstrip("/")
                    url_show = f"http://localhost/{path}"
                    url = f"http://127.0.0.1:{port}/{path}"
                    query = expand(step.get("query"))
                    if query:
                        q = urllib.parse.urlencode(query, doseq=True)
                        url += "?" + q
                        url_show += "?" + q
                    cmd = ["curl", "-sS", "--max-time", str(timeout)]
                    flags = []
                    if step.get("show_headers"):
                        cmd += ["-i"]
                        flags += ["-i"]
                    if step.get("follow_redirects"):
                        cmd += ["-L"]
                        flags += ["-L"]
                    if isinstance(request, list) and step.get("cookies", True):
                        cmd += ["-b", cookie_jar, "-c", cookie_jar]
                        flags += ["-b cookies.txt -c cookies.txt"]
                    for k, v in expand(step.get("headers", {})).items():
                        cmd += ["-H", f"{k}: {v}"]
                        flags += ["-H " + repr(f"{k}: {v}")]
                    if method == "UPLOAD":
                        up_field, up_name = upload
                        up_path = os.path.join(d, up_name)
                        with open(up_path, "wb") as f:
                            f.write(TINY_PNG)
                        cmd += ["-F", f"{up_field}=@{up_path}"]
                        flags += [f"-F {up_field}=@{up_name}"]
                        for k, v in (data or {}).items():
                            cmd += ["-F", f"{k}={v}"]
                            flags += ["-F " + repr(f"{k}={v}")]
                    elif method == "POST":
                        body = urllib.parse.urlencode(data or {}, doseq=True)
                        cmd += ["-d", body]
                        flags += ["-d " + repr(body)]
                    elif method != "GET":
                        cmd += ["-X", method]
                        flags += ["-X " + method]
                    cmd += [url]
                    shown = "$ curl " + " ".join(flags + [repr(url_show)])
                    if step.get("label"):
                        shown = "# " + step["label"] + "\n" + shown
                    cp = subprocess.run(cmd, capture_output=True, text=True,
                                        timeout=timeout + 10)
                    if cp.returncode:
                        raise RuntimeError(shown + "\n" + cp.stderr)
                    for key, pattern in step.get("capture", {}).items():
                        match = re.search(pattern, cp.stdout)
                        if not match:
                            raise AssertionError("capture failed: " + key + "\n" + cp.stdout)
                        captured[key] = match.group(1)
                    transcripts.append(shown + "\n" + cp.stdout.rstrip("\n"))
            finally:
                srv.terminate()
                try:
                    srv.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    srv.kill()
                    srv.wait(timeout=5)
    return "\n\n".join(transcripts)


def PP(id_, title, code, expl="", fname="index.php", env_extra=None, run=True,
       request=None, extra=None, upload=None, assets=None, show_extra=False):
    """A solved PHP program. CLI by default; request=dict serves one HTTP request,
    request=list serves a sequence with a shared cookie jar. extra provides other
    PHP files; show_extra displays clearly labelled, separate file sections.
    upload=(field, filename) sends the bundled test PNG."""
    code = code.strip("\n") + "\n"
    assert "<?php" in code, id_ + ": must contain an opening <?php tag"
    out = ""
    if run:
        if request is not None:
            out = run_web(code, fname, request, extra, upload, assets, env_extra=env_extra)
        else:
            out = run_php(code, fname, env_extra)
    shown = code
    if extra and show_extra:
        # Each labelled section is saved as a SEPARATE file. Do not prepend a
        # second <?php tag or use lstrip("<?php\n"), which removes characters.
        def labelled(name, source):
            return source.replace("<?php", "<?php // ===== File: " + name + " =====", 1).strip("\n")
        shown = "\n\n".join(labelled(n, src) for n, src in [(fname, code), *extra.items()])
    return {"id": id_, "title": {"en": title}, "code": {"en": reflow(shown).rstrip("\n")},
            "out": out, "expl": {"en": expl}}


__all__ = ["make_TP", "PP", "run_php", "run_web", "TINY_PNG", "SXE", "VE", "XE", "G", "reflow", "code_block"]
