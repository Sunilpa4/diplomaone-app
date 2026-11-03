# DiplomaOne – project overview

| What | Where |
|---|---|
| Android APK (latest) | https://github.com/Sunilpa4/diplomaone-content/releases/latest |
| Web app | https://sunilpa4.github.io/diplomaone-content/ |
| Notes served to the app | https://sunilpa4.github.io/diplomaone-content/data/catalog.json |
| Cloud builds | https://github.com/Sunilpa4/diplomaone-app/actions |

## How notes are written
**[`docs/NOTES-GUIDE.md`](docs/NOTES-GUIDE.md)** – the full spec: unit JSON model, card design,
`<h4>` skeletons, diagram rules (360-wide SVG), numerical and derivation conventions, viva/exam
practice, build → test → publish commands, and the definition-of-done checklist.
Review loop for a new unit: `python3 tools/notes_workshop.py add <CODE> <unit>` puts only that
unit on a review shelf (`preview/workshop/index.html`, or `serve --port 8800` for a live link) -
the older committed previews stay out of the way.

Common subjects ("Branch: All") sit in `content/common/sem<N>/<CODE>/` and the exporter lists them
in that semester of every branch. A subject may also carry our own **unit 0 foundation chapter**
(e.g. Mathematics-I "Start Mathematics From Zero"): it ships with `official: false`, zero GTU
hours and marks, and the app labels it "Foundation chapter" instead of a weightage.

Read it before writing a new unit.

## Everyday workflow
* **New/changed notes** → `python3 tools/publish.py "Added <CODE> Unit N"`
  (no new APK needed – phones download the changed units on next start)
* **Backup project / app change** → `python3 tools/sync_code.py "message"`
  (a change inside `app/` triggers the cloud build: signed APKs → Releases, Play Store `.aab` → Actions artifact, web app → Pages)
* Refresh the small offline fallback inside the app (only before a new app version):
  `python3 tools/export_app_content.py --app-assets`

## Restore in a fresh session
Token lives in `.secrets/github_token` (never committed). Clones go to `/opt/repos` (outside the workspace).

## Secrets (GitHub → diplomaone-app → Settings → Secrets → Actions)
`KEYSTORE_BASE64`, `KEYSTORE_PASSWORD`, `CONTENT_TOKEN`.
**Back up `app/android/app/upload-keystore.jks` + `app/android/key.properties` offline** – losing them means you can never update the Play Store app.
