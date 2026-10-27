"""Run Python programs with python3 and capture a real terminal transcript (input echoed like a console).
Used by the Python (Scripting Language) subject builders so every 'Output' shown to students is genuine."""
import hashlib, json, os, pty, select, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "py_run_cache.json")
PY = sys.executable


def _load():
    try:
        with open(CACHE, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _transcript(src, inputs, args=(), cwd=None, timeout=20.0):
    pid, fd = pty.fork()
    if pid == 0:  # child
        os.chdir(cwd)
        env = dict(os.environ, PYTHONUNBUFFERED="1", PYTHONIOENCODING="utf-8", MPLBACKEND="Agg", PYTHONHASHSEED="0")
        os.execve(PY, [PY, "-u", src, *args], env)
    out, pending, t0 = b"", list(inputs), time.time()
    while True:
        r, _, _ = select.select([fd], [], [], 0.3)
        if r:
            try:
                chunk = os.read(fd, 4096)
            except OSError:
                break
            if not chunk:
                break
            out += chunk
        elif pending:
            os.write(fd, (pending.pop(0) + "\n").encode())
        if time.time() - t0 > timeout:
            os.kill(pid, 9)
            out += b"\n[timeout]"
            break
    _, status = os.waitpid(pid, 0)
    txt = out.decode("utf-8", "replace").replace("\r\n", "\n").replace("\r", "")
    return txt, status


def run(code, inputs=(), args=(), files=None, expect_error=False, script="prog.py", extra=None):
    """files: dict name->content created in the working dir before running.
    extra: dict name->content of extra .py modules/packages (paths may contain '/').
    Returns {'out', 'files'} where 'files' holds the text of any new .txt/.csv files written by the program."""
    key = hashlib.sha1(json.dumps([code, list(inputs), list(args), files, extra, script], sort_keys=True).encode()).hexdigest()
    cache = _load()
    if key in cache:
        return cache[key]
    with tempfile.TemporaryDirectory() as d:
        for n, c in {**(files or {}), **(extra or {})}.items():
            p = os.path.join(d, n)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(c)
        src = os.path.join(d, script)
        with open(src, "w", encoding="utf-8") as f:
            f.write(code)
        before = set(os.listdir(d))
        out, status = _transcript(src, inputs, args, cwd=d)
        out = out.rstrip("\n")
        if ("Traceback (most recent call last)" in out or status != 0) and not expect_error:
            raise RuntimeError("RUNTIME ERROR\n" + out + "\n----\n" + code)
        new = {}
        for n in sorted(set(os.listdir(d)) - before):
            if n.endswith((".txt", ".csv")):
                with open(os.path.join(d, n), encoding="utf-8") as f:
                    new[n] = f.read()
    res = {"out": out, "files": new}
    cache[key] = res
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0)
    return res


if __name__ == "__main__":
    print(run('name = input("Enter name: ")\nprint("Hello", name)', ["Ravi"])["out"])
