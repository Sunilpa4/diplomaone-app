# Google sign-in — phase 1

## What this change does (and does not do)

- Optional Google sign-in, profile display and real Firebase sign-out at `#/account`.
- English/Gujarati account UI, session restoration, explicit loading states, popup/network/configuration error messages, and a retry for an unavailable SDK.
- An honest `#/purchases` placeholder: **checkout and purchase records are not connected**. It never says a visitor has bought a paper or has an empty purchase history based on a fabricated local list.
- Existing notes, solved papers, saved notes and language settings work without sign-in. Saved notes/language are still device-local, not synced to Firebase.
- No Analytics, Firestore, Firebase Storage, payment SDK, backend, new database rules or payment entitlements are initialized. No secrets are required in the browser. The unused Analytics measurement ID is intentionally not included.
- The five-branch/semester-navigation redesign and the paid-paper backend are later work. This phase does not claim to implement them.

**A successful build or mock test is not a real Google login.** Provider enablement, authorized domains, OAuth consent settings and a successful login on the deployed domain still require an owner check. They cannot be established from the supplied public config.

## Use the correct Firebase project

The owner-supplied **web** configuration is checked in at `auth/firebase-config.js`:

| Setting | Value |
| --- | --- |
| Project | `diplomaone-53b4e` |
| Auth domain | `diplomaone-53b4e.firebaseapp.com` |
| Web app | `1:784760831297:web:4d682878a2efb0b4c075c0` |

The earlier Android `google-services.json` was for **`diplomaone`**, package `com.diplomaone.app`. These are different Firebase projects. Their users and UIDs must not be assumed to match. Nothing in this change modifies the Android app or migrates its accounts. Align the projects deliberately before connecting shared purchases across web and Android.

The browser API key/app identifiers are public configuration, **not** an Admin SDK key or proof of a purchase. Do not upload a service-account JSON, private key, OAuth client secret or Razorpay secret to this repository or send one through chat. Future backend credentials belong only in the server host's secret manager.

## Owner's Firebase Console steps

1. Open [Authentication in diplomaone-53b4e](https://console.firebase.google.com/project/diplomaone-53b4e/authentication/providers). Double-check the project name/ID before changing anything.
2. Choose **Get started** if Authentication has not been set up. Under **Sign-in method**, enable **Google**, select the project support email, and save.
3. Under **Authentication → Settings → Authorized domains**, add the exact production hosts that will serve this code:
   - `diplomaone.in`
   - `www.diplomaone.in`
   - `sunilpa4.github.io` (if using the GitHub Pages copy)
4. If testing on Netlify's default hostname, add the exact `.netlify.app` hostname shown for that site. If testing an Arena preview, add only that preview's exact hostname temporarily. Do not authorize a whole shared hosting parent domain. The hostname has **no** `https://`, path, `#/account` or port.
5. Keep Firebase's generated auth handler on `diplomaone-53b4e.firebaseapp.com`. This implementation does not require a custom auth-domain proxy. Check the Google consent screen's application name/support information and any test-user restrictions in the same project if Google asks for them.
6. If the public browser API key has Google Cloud API/referrer restrictions, verify they permit this web app's deployed hosts and Firebase Authentication's Identity Toolkit/Secure Token APIs. Do not solve a restriction error by placing a private key in the website or making database rules public.

These console steps have **not** been executed or verified by the agent. There is no Firebase console integration in this session.

## Deploy the complete website

Both deployment paths must ship **all** of:

- `index.html`, `app.js`, `styles.css`, `auth.js`;
- `assets/firebase-auth.js` and `assets/firebase-auth.js.LEGAL.txt`;
- the existing illustration, favicon, font/license and ad declarations.

The GitHub website publisher checks the generated auth bundle against the pinned sources and explicitly copies/stages those files. The manual `DiplomaOne-Netlify.zip` also includes them; do not deploy just `app.js`. Source files, tests, npm dependencies and private credentials are not included in that ZIP. Code changes still require a frontend redeploy; ordinary note/paper updates keep using the existing content pipeline.

Build/check with Node 20+ (CI uses Node 22):

```sh
npm ci --prefix website --ignore-scripts --no-fund
npm run build:auth --prefix website       # after config/client/dependency changes
npm run check:auth --prefix website      # byte-for-byte freshness check
npm run test:auth --prefix website
python3 tools/build_netlify_package.py DiplomaOne-Netlify.zip
NODE_PATH="$PWD/website/node_modules" python3 tools/test_netlify_package.py
```

`@firebase/app` and `@firebase/auth` are the only Firebase runtime packages. Versions and transitive packages are pinned by `package-lock.json`, with one shared app instance. The bundled SDK is self-hosted ESM, not fetched from a Firebase CDN. GAPI and the Firebase auth helper are still external parts of Google's popup flow; bundling the SDK does not make sign-in work offline.

## Session and security choices

- The small `auth.js` controller loads the SDK only on opening Account/Purchases. It does not contact Firebase just because someone reads a note. On a reload, the header uses a neutral **My account** until the optional SDK restores/knows the session; the site does not falsely infer a signed-out state from an unloaded SDK.
- `initializeAuth` explicitly uses **browser-session persistence**, not a long-term remembered login. The SDK, not application code, manages its session tokens. Browsers can restore/duplicate tab sessions, so shared-device users should explicitly sign out rather than rely on closing a tab. Sign-out does not erase the account's Firebase Authentication record or log the user out of other Google services.
- Only UID/name/email/email-verification metadata reaches the controller; only escaped name/email/status appears in the UI. No user photo/tracking URL is loaded. OAuth credentials and raw errors are not logged, copied to custom storage, rendered in HTML or placed in URLs. There is no app-managed `purchased=true` flag.
- The Google provider asks for its standard sign-in identity, selects an account explicitly, and requests **no Drive scopes**. Sign-in is called directly in the click path after the SDK is ready; an initial import/retry never opens a popup automatically. There is no silent redirect fallback.
- A readiness deadline, observer cleanup and generation guards stop a timed-out import/session result from replacing a newer state. Duplicate click operations are ignored. A failed Firebase sign-out leaves the signed-in UI intact and reports the error instead of faking success.
- The CSP allows scripts from this site and `apis.google.com`, auth connections only to the configured Firebase/Identity Toolkit/Secure Token hosts in addition to the existing content endpoints, and a helper frame only under `https://diplomaone-53b4e.firebaseapp.com/__/auth/`. No PDF frame, wildcard, inline script or `unsafe-eval` was added. `object-src 'none'` remains.
- Privacy and account screens do not depend on loading the note catalog. A content outage or a late catalog failure must not block sign-out or overwrite the account screen.

### Paid-content boundary

**Login is not a paywall.** Existing solution HTML, images and PDFs are still publicly served from GitHub. Before charging, private answer storage, server-side Firebase ID-token verification, server-owned paper prices/orders, verified Razorpay payments/webhooks and ownership-checked downloads are required. Public/downloaded copies cannot be retrospectively made never-public.

The agreed later prices are **per individual subject/exam-session solution**, not a bundle: Computer ₹19; Mechanical/Electrical/Civil ₹29; Chemical ₹39. Common subjects remain free; existing notes remain free. No payment collection or UI-only locking is included here.

## Checks and live acceptance checklist

Automated, offline:

- `test_auth.js`: lazy/deduplicated initialization, projected profile only, direct click invocation, safe errors, observer-based identity, failed sign-out, import/session deadlines, stale callbacks, retry and the actual adapter's Firebase API boundary.
- `test_account.js`: real controller plus DOM/router, both languages, profile XSS, loading/errors/retry, no invented purchases, local preferences, catalog failure and navigation races, and exact CSP/script ordering. It also runs against the extracted Netlify package.
- `test_account_browser.js`: optional Chromium checks of the shipped controller/app/CSP at **320, 390, 768, 1024 and 1365 px**, English/Gujarati, with an offline SDK double for success/failure UI. Separate smoke checks load the **real bundle** with external networking blocked (desktop/mobile user agent) and verify graceful GAPI-loading failure. A GitHub Pages-style subpath checks relative ESM resolution. Screenshots stay under ignored `build/account-browser/`. See the commands at the top of that script; `CHROMIUM_EXECUTABLE_PATH` can select a locally installed browser. These are **not** live Google OAuth tests or Safari-device certification.
- The existing question-card, Mechanical/Electrical placement/listing, saved-note link and Netlify package regressions remain applicable. The live `test_published_papers.js` needs outbound access to GitHub Pages; a sandbox without that access cannot certify public CORS/deployment.

Still required after deploying and completing Console setup:

- [ ] Open the deployed `/#/account` in a **normal top-level browser tab**, not a restricted in-app/preview iframe. Check the actual deployed host is authorized.
- [ ] Click **Sign in with Google**, choose a real test account, and verify name/email. Confirm the new user is recorded in **diplomaone-53b4e → Authentication → Users** (do not share tokens).
- [ ] Reload the same tab and open Account: confirm restoration. Navigate to notes and confirm reading still works without any payment claim.
- [ ] Sign out: confirm name/email disappear, Saved notes/language remain device-local, and other Google services are unaffected.
- [ ] Test popup cancellation/blocked popup, offline failure, and an actual mobile browser. If using several hosts, test each host separately; same-project sessions are not automatically shared across origins.
- [ ] Confirm no checkout is enabled and My purchases still explains that purchase records are not connected.

Do not mark these live steps complete based on mocks, a generated ZIP, CI success or the presence of a public API key.

### Local validation recorded for this change

- Clean pinned `npm ci`, generated-bundle freshness check, **13 auth/adapter tests and 11 account/DOM tests passed**. The same 24 tests also passed against the controller/UI extracted from the manual Netlify ZIP.
- **33 offline Chromium account checks passed**: 30 layout/state cases across five widths and two languages, two actual-SDK/network-blocked smoke cases, and one project-subpath case. Mock success is never substituted for live OAuth.
- All eight existing offline website/reader/placement suites passed, including the 49-paper/1,412-part refresh, all 336 supplied Electrical answers and the Mechanical 224 unique/228 source-occurrence refresh.
- **60 real-browser question-card/language/viewport checks and two Mechanical listing/filter checks passed** with the new index/CSP/controller. No note/paper content was changed by this phase.
- Both Netlify package tests (including ZIP freshness/contents) and five existing ad-declaration Python tests passed. The rebuilt ZIP has 12 deploy files and is 540,762 bytes.
- `npm audit --prefix website --audit-level=moderate` reported **0 vulnerabilities**. `git diff --check` and JavaScript syntax checks passed.
- The existing live `test_published_papers.js` did **not** complete locally: Node's request failed with `UNABLE_TO_VERIFY_LEAF_SIGNATURE` at the public API, and this sandbox does not allow outbound GitHub Pages access. TLS verification was not disabled. This is not evidence of a public-site outage, nor a live deployment/CORS validation. The publishing workflow retains that integration check for its normal GitHub runner.
- No live Google OAuth completion, provider/domain/consent change, Firebase database change, payment, Android rebuild or production deployment was performed as part of local validation.
