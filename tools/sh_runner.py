"""Runs shell scripts and command demos for OS Unit 5 and returns realistic terminal transcripts.

- run_script(code, inputs, args, files): runs `bash script.sh args` in a temp dir; whatever the script reads from the
  keyboard (stdin) is echoed into the output like a terminal would show it.
- demo(cmds, files): runs a list of commands one after another in the same directory (cd persists) and returns
  "$ cmd\\noutput" blocks.
Temp paths are shown as /home/student; the sandbox user is shown as student; file times are fixed.
"""
import os, re, shutil, subprocess, tempfile

PRELUDE = r'''
__ORIG0=$(readlink /proc/$BASHPID/fd/0)
read() {
  if [ "$(readlink /proc/$BASHPID/fd/0)" != "$__ORIG0" ]; then builtin read "$@"; return; fi
  local __l
  IFS= builtin read -r __l || return 1
  printf '%s\n' "$__l"
  builtin read "$@" <<< "$__l"
}
'''
HOME_SHOWN = "/home/student"
STAMP = "202610271030"


def _setup(files):
    tmp = tempfile.mkdtemp(prefix="sh_")
    for name, content in (files or {}).items():
        p = os.path.join(tmp, name)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as f:
            f.write(content)
        subprocess.run(["touch", "-t", STAMP, p])
    return tmp


def _clean(out, tmp):
    out = out.replace(os.path.realpath(tmp), HOME_SHOWN).replace(tmp, HOME_SHOWN)
    user = os.environ.get("USER") or subprocess.run(["id", "-un"], capture_output=True, text=True).stdout.strip()
    out = re.sub(rf"\b{re.escape(user)} {re.escape(user)}\b", "student student", out)
    return out


def run_script(code, inputs=(), args=(), files=None, name="script.sh"):
    tmp = _setup(files)
    with open(os.path.join(tmp, name), "w") as f:
        f.write(code)
    with open(os.path.join(tmp, ".prelude"), "w") as f:
        f.write(PRELUDE)
    cmd = ["bash", "--noprofile", "--norc", "-c", f'source .prelude; source {name} "$@"', name] + list(args)
    env = {"PATH": "/usr/bin:/bin", "HOME": tmp, "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TERM": "dumb"}
    r = subprocess.run(cmd, cwd=tmp, input="".join(s + "\n" for s in inputs), capture_output=True, text=True, timeout=10, env=env)
    out = r.stdout + (r.stderr if r.stderr else "")
    files_after = {}
    for n in os.listdir(tmp):
        p = os.path.join(tmp, n)
        if os.path.isfile(p) and not n.startswith(".") and n != name:
            files_after[n] = open(p).read()
    shutil.rmtree(tmp)
    head = f"$ bash {name}" + ("".join(" " + a for a in args))
    return head + "\n" + _clean(out, tmp).rstrip("\n"), files_after


def demo(cmds, files=None, show_prompt=True):
    tmp = _setup(files)
    cwd = tmp
    env = {"PATH": "/usr/bin:/bin", "HOME": tmp, "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TERM": "dumb", "COLUMNS": "40"}
    parts = []
    for c in cmds:
        rc = c
        if (c == "ls" or c.startswith("ls ")) and "|" not in c and " -l" not in c:
            rc = "ls -C" + c[2:]          # a terminal shows ls in columns
        r = subprocess.run(["bash", "--noprofile", "--norc", "-c", f"{rc}\necho __PWD__; pwd"], cwd=cwd, capture_output=True, text=True,
                           timeout=10, env=env)
        out, _, pw = r.stdout.rpartition("__PWD__\n")
        if not _:
            out, pw = r.stdout, cwd
        cwd = pw.strip() or cwd
        for root, ds, fs in os.walk(tmp):
            for x in ds + fs:
                subprocess.run(["touch", "-h", "-t", STAMP, os.path.join(root, x)])
        out = out + r.stderr
        parts.append(("$ " + c if show_prompt else c) + ("\n" + out.rstrip("\n") if out.strip() else ""))
    shutil.rmtree(tmp)
    return _clean("\n".join(parts), tmp)


if __name__ == "__main__":
    print(run_script('echo -n "Enter name: "\nread n\necho "Hello $n"\nwhile read l; do echo "[$l]"; done < f.txt\n', ["Ravi"],
                     files={"f.txt": "a\nb\n"})[0])
    print(demo(["pwd", "mkdir os", "cd os", "pwd", "echo hi > a.txt", "ls -l", "cd ..", "ls"]))
