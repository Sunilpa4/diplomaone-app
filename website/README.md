# DiplomaOne website

The website reads `data/catalog.json`, subject files and unit files published by the same content pipeline as the Android app. New content appears after the normal notes publisher updates the public repository; the site does not bundle a copy of the notes. Saved units and the language choice are stored only in the visitor's browser.

## Local preview

From the repository root:

```sh
python3 tools/export_app_content.py
python3 website/serve.py
```

Open the displayed server address. The preview maps `/data/` to the generated `build/data/` directory. To preview another published data snapshot, set `DATA_DIR` to its absolute path when starting the server. The actual website uses paths relative to its own root, so it works both on a GitHub Pages project path and a custom domain.

## Publishing

On a push to `main` that changes the website or app, **Publish DiplomaOne website** builds the Flutter web app at `/app/` and copies the website to the root of `Sunilpa4/diplomaone-content`. It preserves the existing `data/`, `CNAME`, and other unrelated public files. It requires the existing `CONTENT_TOKEN` repository secret. Android releases remain the responsibility of the separate Build DiplomaOne workflow. The website publisher retries non-force pushes if the notes publisher changes the public repository during a build.

The Flutter web base path is selected from the public repository's `CNAME`: `/diplomaone-content/app/` without a custom domain, `/app/` with one. After adding or removing a custom domain, rerun the website workflow so the Flutter web app is rebuilt with the correct base path. Domain DNS and GitHub Pages settings must be configured separately; do not create a CNAME until the owner has chosen the domain and confirmed the DNS setup. The website remains a hash-routed client app; no search-engine indexing of individual note pages is promised.

Rich note markup is restricted to presentational HTML. Embedded SVG diagrams are displayed as images, never injected as executable markup. Gujarati UI text falls back to English where a particular note has no Gujarati translation.

## AdSense declarations

The public publisher ID is listed in `index.html` and `ads.txt`. The website publisher adds the tracked seller records to the public `ads.txt` while preserving pre-existing records except for exact records explicitly listed in `ads-retired.txt`. It does not load advertising scripts or show ads. When the custom domain is connected, check that `https://www.diplomaone.in/ads.txt` is reachable at the domain root and that its seller records are intentional. Additional ad scripts require a separate review of security policy, consent, and the privacy notice.

## Netlify manual-deploy ZIP

Run `python3 tools/build_netlify_package.py` to produce `release/DiplomaOne-Netlify.zip` (or pass another output path). Run `python3 tools/test_netlify_package.py` to verify the archive. Extract the ZIP and drag the resulting folder, containing `index.html` at its root, into Netlify Drop. The archive contains no built-in copy of the notes: its `_redirects` rule proxies `/data/*` to the current GitHub Pages content repository, so normal content publications are visible without redeploying the website. The solved-paper reader fetches the existing public GitHub Pages papers directly, removes active markup and displays the questions and diagrams inside DiplomaOne. Original paper PDFs open on GitHub Pages. The `/papers/*` redirect remains for older direct links; it does not proxy active HTML into the site's origin. After deploying this version once, new compatible papers are discovered through the automatically updated paper index; adding a paper does not require a Netlify deployment. Keep that GitHub Pages URL available and do not point its custom domain back at the Netlify site, which would create a redirect/proxy loop. Design or code changes require another manual Netlify deployment unless a separate continuous-deployment setup is configured. The existing Flutter web app link opens its GitHub Pages location. Ads are not enabled by this package.


## Adding solved papers automatically

Publish the solution to the `main` branch of the public `Sunilpa4/diplomaone-content` repository at `papers/DIxxxxxxxx/session-year.html`, for example `papers/DI05019011/winter-2027.html`. The subject folder must use `DI` followed by eight digits; the exam filename must use lowercase letters/numbers followed by a hyphen and four-digit year (for example `summer-2026` or `winter-2027`). The HTML needs a `<main>` containing `<details>` question sections, as in the existing papers; scripts and unsupported markup are not displayed. Uploading a PDF alone does not create a solution. Provide English and Gujarati sections using the existing `.en` and `.gu` classes if both languages are available.

An optional original PDF named `winter-2027.pdf` alongside `winter-2027.html` is linked from that paper. The legacy `Question_Paper.pdf` is linked when it is the only solution in that subject or the HTML explicitly links it. The website never invents a PDF when none exists.

The **Update solved-paper index** workflow in this repository scans the public papers folder approximately every three hours, publishes only `papers/index.json`, and leaves all paper files intact. GitHub may delay scheduled runs and Pages deployment; check the workflow if a paper does not appear. The workflow uses the existing `CONTENT_TOKEN` secret, requires GitHub Actions to remain enabled, and consumes Actions minutes. A new solution then appears on the website's Solved papers page, and on its subject page if the subject is in the notes catalog, without a new website deployment. Subjects not yet in the catalog are listed by their code on Solved papers. Incorrect paths, unsupported HTML formats, failed workflows, a non-public paper or disabled Pages will prevent automatic listing; correct the published file and allow the next scan. The index is cached in the browser for up to a minute. On a temporary index failure the website shows the last known list (or the six original papers as a fallback) and a warning.
