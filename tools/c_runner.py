"""Compile + run C programs with gcc and capture a real terminal transcript (input echoed like a console).
Used by the C-programming subject builders so every 'Output' shown to students is genuine."""
import hashlib, json, os, pty, select, subprocess, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "c_run_cache.json")


def _load():
    try:
        with open(CACHE, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _transcript(exe, inputs, args=(), cwd=None, timeout=5.0):
    pid, fd = pty.fork()
    if pid == 0:  # child
        if cwd:
            os.chdir(cwd)
        os.execv(exe, [exe, *args])
    out, pending, t0 = b"", list(inputs), time.time()
    while True:
        r, _, _ = select.select([fd], [], [], 0.25)
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
    os.waitpid(pid, 0)
    return out.decode("utf-8", "replace").replace("\r\n", "\n").replace("\r", "")


def run(code, inputs=(), args=(), files=None):
    """files: dict name->content created in the working dir before running (for file-handling programs)."""
    key = hashlib.sha1(json.dumps([code, list(inputs), list(args), files], sort_keys=True).encode()).hexdigest()
    cache = _load()
    if key in cache:
        return cache[key]
    with tempfile.TemporaryDirectory() as d:
        src, exe = os.path.join(d, "p.c"), os.path.join(d, "p")
        with open(src, "w", encoding="utf-8") as f:
            f.write(code)
        r = subprocess.run(["gcc", "-std=c99", "-Wall", "-Wextra", "-o", exe, src, "-lm"], capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError("COMPILE ERROR\n" + r.stderr + "\n" + code)
        warn = r.stderr.strip()
        for n, c in (files or {}).items():
            with open(os.path.join(d, n), "w", encoding="utf-8") as f:
                f.write(c)
        out = _transcript(exe, inputs, args, cwd=d).rstrip("\n")
    res = {"out": out, "warn": warn}
    cache[key] = res
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0)
    return res


if __name__ == "__main__":
    print(run('#include <stdio.h>\nint main(void){int a,b;printf("Enter two numbers: ");scanf("%d %d",&a,&b);printf("Sum = %d\\n",a+b);return 0;}', ["10 20"])["out"])
