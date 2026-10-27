"""GitHub helpers for DiplomaOne (token from .secrets/github_token – never committed).

Repos (owner Sunilpa4):
  diplomaone-app      PRIVATE  code + tools + content sources + CI workflow
  diplomaone-content  PUBLIC   data/ (notes served to the app via GitHub Pages) + web app at root
Local clones live in /opt/repos (outside the workspace, so the 128 MB limit is not touched).
"""
import base64, json, os, subprocess, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER = "Sunilpa4"
APP_REPO = "diplomaone-app"
CONTENT_REPO = "diplomaone-content"
CLONES = "/opt/repos"
PAGES_URL = "https://sunilpa4.github.io/diplomaone-content/"


def token():
    with open(os.path.join(ROOT, ".secrets", "github_token")) as f:
        return f.read().strip()


def api(method, path, data=None, ok=(200, 201, 204)):
    req = urllib.request.Request(
        "https://api.github.com" + path, method=method,
        data=None if data is None else json.dumps(data).encode(),
        headers={"Authorization": f"Bearer {token()}", "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "diplomaone-tools"})
    try:
        with urllib.request.urlopen(req) as r:
            body = r.read()
            return r.status, (json.loads(body) if body else {})
    except urllib.error.HTTPError as e:
        body = e.read()
        try:
            body = json.loads(body)
        except Exception:
            body = body.decode(errors="replace")
        if e.code in ok:
            return e.code, body
        return e.code, body


def sh(cmd, cwd=None, check=True, quiet=False):
    r = subprocess.run(cmd, cwd=cwd, shell=True, text=True, capture_output=True)
    out = (r.stdout + r.stderr).replace(token(), "***")
    if not quiet and out.strip():
        print(out.strip())
    if check and r.returncode != 0:
        raise SystemExit(f"command failed: {cmd.replace(token(), '***')}")
    return out


def clone(repo):
    """Clone (or update) a repo into /opt/repos/<repo>; returns the path."""
    os.makedirs(CLONES, exist_ok=True)
    path = os.path.join(CLONES, repo)
    url = f"https://x-access-token:{token()}@github.com/{OWNER}/{repo}.git"
    if not os.path.isdir(os.path.join(path, ".git")):
        sh(f"git clone -q {url} {path}", quiet=True)
    else:
        sh(f"git remote set-url origin {url}", cwd=path, quiet=True)
        if sh("git ls-remote --heads origin", cwd=path, quiet=True).strip():
            sh("git pull -q --rebase origin main", cwd=path, check=False, quiet=True)
    sh('git config user.name "DiplomaOne Bot"', cwd=path, quiet=True)
    sh(f'git config user.email "{OWNER}@users.noreply.github.com"', cwd=path, quiet=True)
    sh("git checkout -q -B main", cwd=path, check=False, quiet=True)
    return path


def commit_push(path, message):
    sh("git add -A", cwd=path, quiet=True)
    if not sh("git status --porcelain", cwd=path, quiet=True).strip():
        print("nothing to commit")
        return False
    sh(f'git commit -q -m "{message}"', cwd=path, quiet=True)
    sh("git push -q -u origin main", cwd=path, quiet=True)
    print("pushed:", message)
    return True


def set_secret(repo, name, value):
    """Store an encrypted GitHub Actions secret (needs PyNaCl)."""
    from nacl import encoding, public
    _, key = api("GET", f"/repos/{OWNER}/{repo}/actions/secrets/public-key")
    box = public.SealedBox(public.PublicKey(key["key"].encode(), encoding.Base64Encoder()))
    enc = base64.b64encode(box.encrypt(value.encode())).decode()
    st, body = api("PUT", f"/repos/{OWNER}/{repo}/actions/secrets/{name}",
                   {"encrypted_value": enc, "key_id": key["key_id"]})
    print(f"secret {name}: HTTP {st}")
    return st in (201, 204)
