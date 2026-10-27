"""Back up the whole project (code, tools, content sources) to the PRIVATE repo diplomaone-app.
A push that changes app/ also triggers the cloud build (APK + Play Store bundle + web app).

  python3 tools/sync_code.py "Message"

Files are copied (not deleted) – removing old subjects from the workspace to save space does
NOT delete them from GitHub. Restore everything in a new session with:
  python3 -c "import sys; sys.path.insert(0,'tools'); import gh; print(gh.clone(gh.APP_REPO))"
"""
import fnmatch, os, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gh  # noqa: E402

EXCLUDES = [".secrets", "build", ".dart_tool", ".gradle", ".kotlin", "__pycache__", "*.pyc", "*.jks",
            "*.keystore", "key.properties", "local.properties", ".flutter-plugins-dependencies",
            ".idea", "*.iml", "preview/*.png", "release"]


def skip(rel):
    parts = rel.split(os.sep)
    for e in EXCLUDES:
        if "/" in e:
            if fnmatch.fnmatch(rel.replace(os.sep, "/"), e):
                return True
        elif any(fnmatch.fnmatch(p, e) for p in parts):
            return True
    return False


def main():
    msg = sys.argv[1] if len(sys.argv) > 1 else "Sync project"
    repo = gh.clone(gh.APP_REPO)
    n = 0
    for d, dirs, files in os.walk(gh.ROOT):
        rel_d = os.path.relpath(d, gh.ROOT)
        dirs[:] = [x for x in dirs if not skip(os.path.normpath(os.path.join(rel_d, x)))]
        for f in files:
            rel = os.path.normpath(os.path.join(rel_d, f))
            if skip(rel):
                continue
            src, dst = os.path.join(gh.ROOT, rel), os.path.join(repo, rel)
            if os.path.exists(dst) and os.path.getsize(dst) == os.path.getsize(src) \
                    and open(dst, "rb").read() == open(src, "rb").read():
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            n += 1
    print("files copied/updated:", n)
    gh.commit_push(repo, msg)


if __name__ == "__main__":
    main()
