"""Publish notes to the app: export all finished content and push it to the PUBLIC repo
(served by GitHub Pages at https://sunilpa4.github.io/diplomaone-content/data/...).
The app picks up new/changed units automatically on its next start.

  python3 tools/publish.py "Added DI02000091 Unit 1"
"""
import os, shutil, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gh  # noqa: E402

README = """# DiplomaOne – content

Notes, programs, diagrams, viva and exam questions for **GTU Diploma** students,
served to the **DiplomaOne** app (Android + Web).

* Web app: https://sunilpa4.github.io/diplomaone-content/
* Android APK (testing): see **Releases** → latest
* `data/` is generated automatically – please do not edit by hand.
"""


def main():
    msg = sys.argv[1] if len(sys.argv) > 1 else "Update notes"
    repo = gh.clone(gh.CONTENT_REPO)
    data = os.path.join(repo, "data")
    if os.path.isdir(data):
        shutil.rmtree(data)
    subprocess.run([sys.executable, os.path.join(gh.ROOT, "tools", "export_app_content.py"), "--out", data],
                   check=True)
    open(os.path.join(repo, ".nojekyll"), "w").close()
    if not os.path.exists(os.path.join(repo, "README.md")):
        open(os.path.join(repo, "README.md"), "w").write(README)
    if not os.path.exists(os.path.join(repo, "index.html")):  # placeholder until CI deploys the web app
        open(os.path.join(repo, "index.html"), "w").write(
            '<!doctype html><meta charset="utf-8"><title>DiplomaOne</title>'
            '<p style="font-family:sans-serif">DiplomaOne web app is being built…</p>')
    gh.commit_push(repo, msg)


if __name__ == "__main__":
    main()
