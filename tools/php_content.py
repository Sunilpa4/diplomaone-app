"""Content helpers for PHP (Introduction to Web Development) – English only.

Runs each program with a locally extracted PHP 8.4 CLI (see PHP_BIN below), so every
shown output is genuine. Note bodies use @@name@@ code snippets (make_TP from py_content).
"""
import html, os, re, subprocess, tempfile
from py_content import make_TP, reflow, code_block          # language-neutral helpers
from c_content import SXE, VE, XE, G

PHP_ROOT = "/tmp/phproot"
PHP_BIN = os.path.join(PHP_ROOT, "usr", "bin", "php8.4")
PHP_ENV = dict(os.environ, LD_LIBRARY_PATH=os.path.join(PHP_ROOT, "usr", "lib", "x86_64-linux-gnu"))

if not os.path.exists(PHP_BIN):
    import urllib.request, subprocess as _sp
    raise SystemExit("PHP binary not extracted - see workspace notes (apt download php8.4-cli + deps into " + PHP_ROOT + ")")


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


def PP(id_, title, code, expl="", fname="index.php", env_extra=None, run=True):
    """A solved PHP program with genuine CLI output.
    run=False for web-request demos whose output is produced later (forms unit)."""
    code = code.strip("\n") + "\n"
    assert "<?php" in code, id_ + ": must contain an opening <?php tag"
    out = run_php(code, fname, env_extra) if run else ""
    return {"id": id_, "title": {"en": title}, "code": {"en": reflow(code).rstrip("\n")},
            "out": out, "expl": {"en": expl}}


__all__ = ["make_TP", "PP", "run_php", "SXE", "VE", "XE", "G", "reflow", "code_block"]
