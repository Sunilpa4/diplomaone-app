# TEST backend validation record

## Current change: protected, read-only browser connection check

The owner selected a **browser** check instead of the existing local command. The implementation adds **`https://vermillion-pothos-520a34.netlify.app/#/test-connection`** and a narrow **`POST /api/payments/test/connection`** route. It does not enable checkout or test payments.

The server requires the exact HTTPS test-site URL, same-origin JSON POST, Netlify **Production** context, verified Firebase/Google identity, an allowlisted **`PAYMENTS_TESTER_UIDS`** UID and both checkout switches OFF **before any Firestore read**. Firestore configuration is validated independently of Razorpay secrets. The lazy probe executes only the fixed products query with `limit(1)`, never inspects/returns document data and makes no writes, imports, orders, purchases, provider/storage calls or rule/account changes. Empty collections can succeed. Safe status does not prove write permission or merchant readiness.

Local validation for this revision:

- **73 backend cases: 72 passed, 1 emulator-only client-rules case skipped locally.** New cases cover real locally signed JWT verification at this endpoint, missing/uninvited/invalid identity, malformed allowlists, wrong URL host/origin/context/method, both flags/partial/invalid flags, strict bounded body/path handling, independent setup/no Razorpay dependency, no read/adapters on rejection, fixed lazy query, safe failures, busy/cooldown behavior and safe retry status. The repository test verifies the probe does not change product or payment records; CI reruns it with the genuine SDK/emulator.
- **44 offline auth/request/UI tests passed** (16 controller/adapter, 12 narrow request-helper, 16 account/router). Controller/UI suites also passed against the extracted frontend ZIP. Tests check fixed same-origin header/endpoint, no generic token exposure, no automatic probe/retry, deduplication, session/navigation/logout invalidation, timeout/late-token behavior, bounded safe response projection, hosting HTML/redirect failures, bilingual errors and no profile/token/document echo.
- **9 offline Chromium diagnostic scenarios passed** on the actual packaged app/controller and real request helper, with explicit Auth/HTTP boundary doubles and every request locally fulfilled/blocked. English/Gujarati at **1365/390/320 px**, server rejection/success copy, user gestures, same-origin POST headers, CSP/layout/focus, logout/navigation token cancellation, HTML/redirect failure and public/preview-host denial. This browser test caught a navigation timing race: the URL can change before `hashchange` dispatch. The helper now rechecks the **live route immediately before sending** and after receiving, with a dedicated regression. No real test-site/network/Google/Firestore call is made by this test.
- **33 existing offline account Chromium checks passed**, including the actual self-hosted Firebase bundle's desktop/mobile-UA network-blocked readiness/failure smoke and project-subpath resolution. Mocked sign-in is not live OAuth acceptance.
- **Actual Netlify v2/NFT Function ZIP: 2,778,341 bytes** in the local run. Extracted/isolated dependency resolution, ESM and native Lambda v2 startup passed with all network transports blocked for **no-secret**, **Firestore-only/checkout-OFF (no Razorpay secrets)** and **fully-configured/checkout-OFF** cases. Diagnostic authentication/wrong-site gates also passed in that real artifact.
- All **8 existing offline paper/reader/placement suites**, **2 frontend-package tests**, **5 ad-declaration tests**, syntax/bundle freshness and diff-whitespace checks passed. Root and website npm audits each reported **0 vulnerabilities**. No paper/source/catalog/publisher or CSP allowlist was changed.
- The rebuilt frontend-only ZIP contains exactly **12 public files**, **545,879 bytes**, SHA256 **`5318852fd2aabd628ce1588fe8510b2355f3efabc51d0f8ee44c8be28b9fa3dd`**. Public output still byte-matches it; backend, keys, dependencies, tests/tooling and private content remain excluded. The self-hosted Auth bundle is **115,793 bytes** plus its unchanged license.

**Genuine-engine gate remains mandatory:** Java is unavailable locally. The payment workflow reruns all **73** backend cases with the official pinned demo emulator, including the new probe and denied browser rules, and the isolated packaged-SDK operations. Use the latest payment check on [PR #37](https://github.com/Sunilpa4/diplomaone-app/pull/37) for this revision's CI result; the historical 57-case runs below do not validate new code.

**Owner/cloud acceptance still pending:** replacement credentials/deployment are owner-reported, not inspected by the agent. The latest real `/config` JSON and a real read result have not been independently observed; the site remains Team-protected. Deletion of an earlier exposed key, replacement identity/IAM and Production-only secret contexts are owner-private checks. The owner must privately allowlist their Firebase UID, redeploy the latest reviewed branch and click once; only the safe displayed status should be shared. No key, token or login sharing is needed. Keep protection, rules and both flags unchanged/OFF. A 30-second per-instance cooldown and 15-second browser deadline are not a distributed billing cap or cancellation of an already accepted read.

## Earlier foundation: Firestore instead of paid Netlify Database

The owner rejected Netlify Database after a payment prompt, chose Firebase, explicitly confirmed billing is already enabled, and reports creating the Standard/default/Production Firestore database in **`diplomaone-53b4e`**. Cloud existence/settings are owner-reported, not independently verified by the agent.

The runtime, configuration and owner importer now use **`@google-cloud/firestore@9.4.1`**, not `pg`/PostgreSQL/`NETLIFY_DB_URL`. The unused, never-deployed SQL migration and PGlite dependency are removed; there is no real old purchase database/data migration. Fixed TEST-only Firestore namespace: **`diplomaone_test/v1/**`**. File bytes remain in the separately private Netlify Blobs store. No cloud write, account configuration, key creation, rules deployment, additional paid service or private paper upload was performed.

### Completed locally

- Node 22 syntax checks, pinned root install, root audit **0 vulnerabilities**.
- **57 backend cases: 56 passed, 1 intentionally skipped** without an emulator. Tests cover exact-project Firebase JWTs; server-only credentials and TLS; fixed INR pricing/free subjects; tester scoping; request/order/payment binding; transactional uniqueness/idempotency; uncertain-provider fail-closed behavior; budget exhaustion/expiry/concurrency; captured-only grants; raw HMAC/event conflicts; refunds/replay/racing delivery/repurchase; UID-safe document paths; bounded metadata; private source/hash/size/reference/import checks; safe disabled deployment and sanitized failed connection probe.
- Local repository tests use an explicit **test-only Firestore document/transaction double**, with atomic commits, version conflicts/retries and read-before-write checking. They are not claimed to be a real Firestore engine. The browser Security Rules test intentionally skips here; Java/emulator tooling is absent from this sandbox.
- Actual Netlify native **v2/NFT Function ZIP**: approximately **2.78 MB compressed** with the Firestore SDK, JWK/Blobs/runtime dependencies. Extracted outside the checkout; all required dependency imports resolve inside the artifact. App ESM and generated Lambda v2 bootstrap return the exact expected disabled JSON for both no-secret and configured-but-disabled cases. Fetch/Node network transports are blocked in this disabled smoke; no cloud call is hidden by it.
- The public build still contains exactly the same **12 frontend files**, byte-for-byte matching the existing frontend-only ZIP. No backend, credentials, npm dependencies, emulator/test tooling or private files enter static publish output.
- Existing regressions re-run for this change: **24 auth/account tests**, auth-bundle freshness, **8 offline paper/reader/listing/source-placement suites**, **2 frontend-package tests** and **5 ad-declaration tests** passed. Website audit: **0 vulnerabilities**. Workflow YAML/shell syntax and `git diff --check` passed.

### Required CI emulator gate (not replaced by the double)

The payment workflow installs Java 21 and downloads the official **Firestore emulator 1.22.0**, verifying the pinned **136,707,194-byte** JAR and SHA256 **`9b6498b7f62714d67f48f59b3818883cd682dbcd46b9f59511de81c97bb5166c`** before executing it. The source/checksum come from Firebase Tools **v15.37.0**'s official emulator manifest.

`npm run test:firestore` starts a fresh loopback-only emulator with **`demo-diplomaone-payments`**, no real cloud project/login/key, and emulator-only deny-all rules. It runs **all 57 cases against the real SDK/emulator**, including the previously skipped anonymous/signed-in client-rule checks, then exercises actual read/write/query/transaction/delete operations from the **isolated deployed ZIP's SDK**. Files sharing the same demo namespace run sequentially; individual cases explicitly exercise concurrency. The runner refuses an existing server, strips owner credentials, pins the demo ID, and stops its child emulator. Diagnostics are retained only as short-lived CI artifacts.

**Passed on `ffcfcf4`:** [payment run 44690340020](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44690340020/job/136134349439), **1m03s**, including all **57 real-emulator cases**, the SDK connection probe and the isolated packaged-SDK operations. Local-double results are not used as a substitute.

The first real-emulator attempt (`db0fc94`, run 44688769415) caught a defect the double could not: REST-fallback cleanup repeatedly failed with SDK `UNAVAILABLE`/code 14. A separate local transport probe also showed that fallback trying ADC without credentials. The implementation and emulator clients now use the SDK's **native gRPC transport**, with the Google universe explicitly pinned to avoid ambient metadata discovery; the fresh genuine-emulator/ZIP run passed. The emulator runner now fails fast on connection problems and emits diagnostic annotations instead of silently spending minutes retrying every setup hook. No owner cloud setting was changed to make tests pass.

Use the latest payment check on [draft PR #37](https://github.com/Sunilpa4/diplomaone-app/pull/37) for subsequent revisions. Emulator success still does not certify real-project IAM, network latency, contention, billing settings or provider behavior.

## Earlier deployment crash regression: resolved startup only

The owner's first deployment failed with **`ERR_MODULE_NOT_FOUND: Cannot find package 'pg'`**. The agent reproduced it with the real Netlify packager: the old five-file archive had unresolved runtime imports because packages were installed only in sibling `backend/node_modules`. The earlier standalone esbuild test missed the defect.

Commit **`afecd4f`** moved manifest/install ownership to the repository/Netlify base, retained CommonJS for existing tools and added actual ZIP/isolation/native Lambda checks. The old implementation's **44 backend tests**, **24 auth/account tests**, **8 offline reader suites**, **2 frontend-package + 5 ad tests** passed; root/website audits were clear. PR payment/content/publish checks passed (publisher required a same-commit failed-job retry; the original sub-check failure was not diagnosed). The owner subsequently confirmed this response from the new preview:

```json
{"mode":"test","enabled":false,"reason":"setup_required","currency":"INR"}
```

That confirms the packaging/startup repair, **not payment/database readiness**. `pg` is now removed as part of the Firestore replacement, but the root-tracing/isolated ZIP regression remains mandatory for the new SDK. Old immutable deploy URLs still refer to old artifacts. Agent-side requests remain behind Netlify Team protection.

## Not completed / no claims made

- No real Firestore connectivity/IAM/read/write acceptance, server secret configuration, Netlify account inspection/change or Blobs import by the agent. Production rules/SA permissions must be reviewed privately by the owner; server IAM bypasses client Security Rules.
- No request using the owner's Razorpay API secret; no actual provider-backed test payment, charge, capture, refund, payout or live-key acceptance. Local doubles and the supplied public Test Key ID do not establish a working merchant integration.
- No change to billing, recharge, plans, Firebase Storage/Functions or paid infrastructure. Existing Firebase billing is not a free-unlimited/cost-cap claim or permission to provision more services.
- No paper/source/Drive item moved, deleted, replaced, made private or newly published. Existing public answers/history/downloads remain public; UI locking/copying privately cannot revoke those copies. Existing automatic publishers are unchanged.
- No connected browser Buy/My purchases/private-reader flow or agreed customer refund/access/preview policy. These and publisher/private-content migration review are mandatory before enabling either checkout flag.
- No general DDoS protection, instantaneous ID-token revocation, unlimited free hosting, real-project availability or live-payment readiness is promised.

The previous foundation's frontend ZIP was **540,762 bytes**, SHA256 **`2e4c509ad7991c0775cb8712001d6877c1d228f5568be4975947bb2ad19bea6c`**; the current rebuilt diagnostic UI artifact is recorded above. See [README.md](README.md) for safe owner setup and separate acceptance gates. Keep checkout OFF.
