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


def run_web(code, fname="index.php", request=None, extra=None, upload=None, assets=None, timeout=60):
    """Serve `code` (+ extra php files) with php -S and fire a real curl request.

    request: {"method": "GET"|"POST"|"UPLOAD", "data": dict, "headers": dict} (path = fname).
    upload:  (field_name, filename) - uploads the bundled tiny PNG.
    assets:  {relative_path: bytes} extra files written into the docroot.
    Returns a displayable transcript: '$ curl ...' + genuine response body (+ response stderr).
    """
    request = request or {}
    method = request.get("method", "GET")
    data = request.get("data")
    headers = request.get("headers", {})
    with tempfile.TemporaryDirectory() as d:
        for name, src in {fname: code, **(extra or {})}.items():
            p = os.path.join(d, name)
            os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(name) else None
            with open(p, "w", encoding="utf-8") as f:
                f.write(src.strip("\n") + "\n")
        for rel, blob in (assets or {}).items():
            p = os.path.join(d, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(rel) else None
            with open(p, "wb") as f:
                f.write(blob)
        port = _free_port()
        srv = subprocess.Popen([PHP_BIN, "-S", f"127.0.0.1:{port}", "-t", d],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=PHP_ENV,
                               text=True, cwd=d)
        try:
            for _ in range(60):     # wait until the dev server answers
                try:
                    with socket.create_connection(("127.0.0.1", port), timeout=0.5):
                        break
                except OSError:
                    time.sleep(0.05)
            url_show = f"http://localhost/{fname}"
            url = f"http://127.0.0.1:{port}/{fname}"
            q = request.get("query")
            if q:
                url += "?" + urllib.parse.urlencode(q, doseq=True)
                url_show += "?" + urllib.parse.urlencode(q, doseq=True)
            cmd = ["curl", "-s", "--max-time", str(timeout)]
            shown = f"$ curl "
            if request.get("show_headers"):
                cmd += ["-i"]
                shown = "$ curl -i "
            for k, v in headers.items():
                cmd += ["-H", f"{k}: {v}"]
            if method == "GET":
                shown += f"'{url_show}'"
                cmd += [url]
            elif method == "UPLOAD":
                up_field, up_name = upload
                up_path = os.path.join(d, up_name)
                with open(up_path, "wb") as f:
                    f.write(TINY_PNG)
                cmd += ["-F", f"{up_field}=@{up_path}"]
                if data:
                    for k, v in data.items():
                        cmd += ["-F", f"{k}={v}"]
                    shown_parts = " ".join(f"-F {k}={v} " for k, v in data.items())
                else:
                    shown_parts = ""
                shown += f"{shown_parts}-F {up_field}=@{up_name} '{url_show}'"
                cmd += [url]
            else:   # POST (urlencoded)
                body = urllib.parse.urlencode(data or {})
                cmd += ["-d", body, url]
                shown += f"-d '{body}' '{url_show}'"
            cp = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
        finally:
            srv.kill()
            try:
                srv.wait(timeout=5)
            except Exception:
                pass
    out = cp.stdout
    err = cp.stderr.strip()
    return (shown + "\n" + out.rstrip("\n")) + (("\n" + err) if err and cp.returncode else "")


def PP(id_, title, code, expl="", fname="index.php", env_extra=None, run=True,
       request=None, extra=None, upload=None, assets=None, show_extra=False):
    """A solved PHP program. CLI run by default; pass request= for a real served request.
    extra: additional php files (includes) written beside the main file; upload: (field, filename)."""
    code = code.strip("\n") + "\n"
    assert "<?php" in code, id_ + ": must contain an opening <?php tag"
    out = ""
    if run:
        if request is not None:
            out = run_web(code, fname, request, extra, upload, assets)
        else:
            out = run_php(code, fname, env_extra)
    shown = code
    if extra and show_extra:
        parts = [f"<?php // ===== File: {n} =====\n" + c.strip("\n") + "\n?>" for n, c in extra.items()]
        shown = "\n".join(parts) + f"\n<?php // ===== File: {fname} =====\n" + code.lstrip("<?php\n")
    return {"id": id_, "title": {"en": title}, "code": {"en": reflow(shown).rstrip("\n")},
            "out": out, "expl": {"en": expl}}


__all__ = ["make_TP", "PP", "run_php", "run_web", "TINY_PNG", "SXE", "VE", "XE", "G", "reflow", "code_block"]
