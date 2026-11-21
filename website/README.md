# DiplomaOne website

The website reads the published `data/catalog.json`, subject files and free notes from the existing content pipeline. Saved units and language preferences remain device-local, not synced by signing in. Ads are not enabled.

## Simplified website navigation

The homepage has subject/code search, two clear notes/papers shortcuts, My purchases, five branch cards and links to the two common free papers. Repeated promotional sections, decorative hero imagery and the download banner are removed from the page. Optional web/Android app links remain under a collapsed **More resources** footer, not primary study navigation. English/Gujarati, keyboard focus, Escape-to-close mobile navigation and reduced-motion behavior are retained.

The **website presentation** is limited to **Computer, Civil, Chemical, Electrical and Mechanical**, **Semesters 1–5**. The complete catalog, other branches, Semester 6 and original files are not edited/deleted. Branch/semester pages, paper filters/counts, subject search and saved-list display use that same scope. A subject shared with a current placement stays visible; unregistered papers remain discoverable without guessing their branch or semester. A sixth **unit** of a visible subject is not a sixth semester and remains readable.

Deferred-only saved entries are hidden with a notice, never removed from device storage. Direct deferred note routes show a clear selection notice instead of fetching their content. **This is not a payment authorization rule:** an existing owner can still reopen a purchased historical/unlisted paper through My purchases or its direct paper route. The backend, price table, private delivery and all four OFF launch gates are unchanged. The separate optional Flutter/Android app is not redesigned by this website change.

`test_navigation.js` exercises the actual SPA against a frozen full synthetic catalog, including shared/unknown/legacy papers, persisted hidden saves and an owned historical paper. `test_navigation_browser.js` uses the built Netlify frontend at 1440/1024/390/320 px in both languages, plus keyboard/reduced-motion checks. All requests are fulfilled locally or blocked; screenshots contain test data, not real purchases.

## Individual-paper purchases (implemented; sales NOT launched)

The flow is **select a paper/price → Google sign-in → server order → Razorpay Checkout → verified full capture → only that account’s selected paper**. Prices per subject/exam-session paper: Computer **₹19**, Mechanical/Electrical/Civil **₹29**, Chemical **₹39**. **All notes, Maths-I `DI01000021` and Applied Physics `DI01000121` remain free.** No whole-subject bundle/subscription is implied.

**UPI / QR is the selected payment experience.** Checkout prioritises the standard UPI method, hides typed-UPI-ID Collect and cash on delivery, and retains other enabled online methods as fallback. Razorpay—not this site—provides the mobile UPI app/Intent or desktop order-linked QR for the server-created order/amount. Options depend on device/provider/merchant enablement; mobile QR may require account activation. English/Gujarati guidance warns that the UPI PIN belongs only in the UPI app. There is no static personal QR, `upi://` transfer link, PIN/VPA form, transaction-number/screenshot approval or new payment-proof endpoint. These presentation settings never replace the existing fully captured payment verification. Real UPI availability/QR handoff still needs controlled owner acceptance; see the [live-launch guide](../backend/LIVE-LAUNCH.md#selected-payment-experience--automatic-upi--qr).

Paid solutions are locked before any public HTML/image/PDF request. After authorization, the private reader preserves the existing expandable question-answer cards, English/Gujarati or explicit English-only content, diagrams, OR labels, fractions, image enlargement and optional PDF downloads. PDFs never replace the cards. Unknown/legacy/PDF-only paid papers cannot bypass the lock with an old public URL.

`#/purchases` requests actual server-owned UID-scoped records, persists across navigation/reload via Firestore and never invents a local purchase or empty success on error. Opening another paper or changing account does not transfer ownership. Signing in or a browser success callback is not payment authorization. Existing private owners can read while new checkout is paused.

**Charging stays OFF.** Public source cleanup/private import, merchant activation/capture/webhook setup, approved support/refund/access terms and controlled real delivery acceptance remain external launch gates. `#/purchase-info` intentionally says sales are not open rather than inventing legal terms/contact details. See **[backend/LIVE-LAUNCH.md](../backend/LIVE-LAUNCH.md)** for the exact migration/launch procedure and boundaries. No cloud import, real payment, account setting, rules deployment, billing change or extra paid service was performed by the agent.

### Authentication and token boundaries

`auth.js` lazily loads the self-hosted Firebase app/auth bundle on Account/Purchases or an approved-origin paid-paper screen. Ordinary notes/free papers do not initialize Auth. The existing web project is **`diplomaone-53b4e`**, using Google and tab-session persistence, never a long-term app-managed token store. Browsers can restore tab sessions; sign out on shared devices. The older Android Firebase project is separate.

`auth/payment-client.js` is bundled **inside** the Auth adapter, not publicly exported as a generic request/token API. Narrow methods target only fixed relative `/api/payments/live/*` paths on `www.diplomaone.in` or the protected setup site. ID tokens go only in a transient Authorization header, never the URL, DOM, logs or app-managed storage. The helper validates live-mode responses, bounded manifests/assets, exact selected paper/order and server-owned prices. Tokens are not sent to Razorpay. Checkout loads its exact provider script only after a user click and enabled live configuration.

Navigation/account changes/logout cancel requests, reject late results, clear private HTML and revoke image/PDF object URLs. Hash/origin are rechecked even before `hashchange` dispatch. Read timeouts do not undo server reads, and cancellation does not undo an accepted payment. If debited but not unlocked, the UI says **do not pay again; refresh My purchases using the same Google account**. Provider-signed capture webhooks can fulfill without a browser callback.

CSP permits the scoped Google auth helper and exact Razorpay Checkout script/API frames, with blob images and no executable paper HTML/PDF frames. No wildcard hosts, inline/eval script allowance, Firestore/Storage/Analytics SDK or browser Admin credentials are added. Public Firebase web config is not an Admin key or a purchase entitlement. Authorized readers can still copy received content; this is not DRM.

See **[AUTH-SETUP.md](AUTH-SETUP.md)** for retained Google provider/domain/session details. Its phase-1 results are historical; **[backend/VALIDATION.md](../backend/VALIDATION.md)** records current validation and owner acceptance limits.

### Protected read-only setup diagnostic (retained, not a prerequisite walkthrough)

`https://vermillion-pothos-520a34.netlify.app/#/test-connection` remains manual/tester-only. It uses the fixed `/api/payments/test/connection` endpoint, Google/test-UID authorization, exact origin/Production context and checkout flags OFF. One `limit(1)` Firestore metadata query returns safe status only, with no writes, provider call or automatic retry. It needs no Razorpay secret. A 30-second per-instance cooldown is not a billing cap; a success is not payment acceptance. Keep test-site Team protection and client rules unchanged.

## Foreground paper discovery — no polling

The existing GitHub tree request discovers free readers and non-sensitive `papers/<code>/<session>.json` private-paper metadata. On approved live hosts, one foreground `/api/payments/live/config` metadata request also discovers new activated private imports, independently of GitHub availability. No scheduled three-hour scan or background polling is added. Refresh/open a new tab after publishing/importing; normal API/Pages caches and visitor-IP rate limits still apply.

Papers remain grouped under their actual catalog subject/branch/semester. Original DI/seven-digit legacy codes and sessions are preserved. Explicit reviewed cross-lists (for example `4351902` → related `DI05019011`) do not relabel exams or claim equal syllabuses. Unknown subjects remain listed by code without guessed catalog placement or price. Displayed prices are informative; the server re-reads canonical branch/price inside the order transaction.

**Do not publish new paid answers in this public repository or the public content repository.** Use the private importer/migration workflow. The public solved-paper publisher now copies only the two free subjects and tiny private listing metadata. Current old public answers/source archives still require verified private backup/import and explicit cleanup; UI locks cannot revoke history/downloaded copies. See the live-launch guide and `npm run audit:public-papers`.

Free paper HTML uses a `<main>` with expandable `<details>` and the established presentational sanitizer. Optional matching original/solution PDFs remain downloads. The legacy `Question_Paper.pdf` is linked only when explicitly matched; no exam or translation is invented.

## Local checks and preview

From the repository root:

```sh
npm ci --include=dev --ignore-scripts --no-fund
npm ci --prefix website --include=dev --ignore-scripts --no-fund
npm run build:auth --prefix website       # after changing bundled client sources
npm run check:auth --prefix website
npm run test:auth --prefix website       # Auth, navigation, Checkout and SPA tests
python3 tools/build_netlify_package.py DiplomaOne-Netlify.zip
python3 tools/build_netlify_site.py
NODE_PATH="$PWD/website/node_modules" python3 tools/test_netlify_package.py
npm test                                # after rebuilding the ZIP; includes exact artifact equality
npm run check:bundle                     # actual isolated Netlify Function ZIP
python3 tools/export_app_content.py
python3 website/serve.py
```

The preview maps `/data/` to `build/data/`; `DATA_DIR` can select another local public note export. A local/Arena/branch preview intentionally cannot send live payment tokens or start checkout; it links to the approved `www` origin. Offline HTTP/SDK/Checkout doubles and the official DEMO emulator never charge money or establish owner-cloud acceptance.

## Deployment and the manual ZIP

Use root **`netlify.toml`** for the Git-connected API + frontend deployment. It builds exactly **12 allowlisted public frontend files** and packages Functions separately. Credentials, private imports, source papers, test tooling and dependencies are never copied into static output or substituted from environment variables.

**`DiplomaOne-Netlify.zip` is frontend-only.** Drag/drop cannot install the payment API. Its `/data/*` rewrite serves current public notes; only legacy paths under the two free subject codes redirect to public paper files. Other `/papers/*` paths return a 404 frontend instead of disclosing old answers. GitHub Pages/static-only deployments cannot host the private payment API; paid screens link to the approved domain.

The existing GitHub website workflow still builds `/app/` and stages only frontend/app files in `Sunilpa4/diplomaone-content`, preserving `data/`, `CNAME` and unrelated files. Both notes publishers stay in place and stage only `data/`. No Drive file is moved/deleted. Do not change domain/DNS or upgrade plans to work around missing private setup. Google/provider console authorization and reachable webhooks require owner-controlled setup, never shared passwords/keys.

Code/design changes require a frontend redeploy; free note publications and activated private imports do not require scheduled site rebuilds. The site remains hash-routed; searchable per-note URLs/sitemap work is deferred.

## AdSense declarations

`index.html` and `ads.txt` retain **ca-pub-6133298835140242** / the matching seller record. The publisher preserves existing seller records except explicitly retired exact records. No ad script or display-ad unit is invented. Any later advertising changes require separate consent/privacy/CSP review.
