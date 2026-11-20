# Netlify / Razorpay TEST backend foundation

## Status — do not mistake code/tests for an enabled checkout

The owner supplied public Test Key ID **`rzp_test_ToAdJ9DdVMFeM2`** and chose **free-tier-first / no Firebase billing**. The owner reports Netlify's **Free** plan.

This change prepares a **server-side test backend**. It does **not** enable a Buy button, wire the browser's My purchases screen, provision a database, upload private papers, configure secrets/webhooks, connect a Netlify account, deploy anything or take payments. There are **no seeded products or fake purchases**. The existing website's reading access and manual frontend ZIP are unchanged.

**Next browser integration is a separate gate:** obtain Firebase ID tokens inside the SDK layer and send them only as same-origin Bearer headers; never expose them in DOM/URLs/logs/custom storage. Build the Razorpay test Checkout UI and an ownership-checked reader which reuses the existing strict paper sanitizer, rewrites private image references to authenticated fetches, and has no public full-answer fallback. Update the site's payment/privacy/refund/access information before inviting testers. Do not enable the two checkout flags before this review.

### Free-tier boundary

Recommended deployment: existing Firebase Google sign-in + **Netlify Functions**, **Netlify Database (Postgres)** and **Netlify Blobs**. No Firestore, Firebase Storage, Firebase Functions, Firebase billing or new provider account is added.

Netlify's current credit-based Free plan includes server functions/storage/database features with **300 credits/month, a hard limit and no automatic recharge**. At exhaustion, projects can pause; this is not unlimited or guaranteed always-on hosting. Usage, database compute, bandwidth and deploys consume the allowance. A separate test site isolates deployment/data from your current frontend, but sites on the same team still share its plan allowance. [1](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/) [5](https://docs.netlify.com/manage/accounts-and-billing/billing/resume-paused-projects/)

Netlify Database is available on **credit-based** plans only. The exact account has not been inspected; a legacy plan called Free may differ. If the dashboard requires a paid upgrade/card or has no included Database, **stop—do not upgrade or enable recharge**. Choose another free-tier backend after review instead. None of these account changes was performed by the agent. [3](https://docs.netlify.com/build/data-and-storage/netlify-database/)

## Implemented security boundaries

- All routes are under **`/api/payments/test/`**. **Live `rzp_live_` keys are refused.** There is no environment toggle to turn these tables/endpoints into live checkout. A future live integration needs a separate review and data namespace; test purchases never establish real purchase ownership.
- JWT verification uses Google's public signing keys, **RS256**, exact audience/issuer/project `diplomaone-53b4e`, expiry/issued/authentication times, UID bounds and Google sign-in provider. The earlier Android project `diplomaone` is deliberately not accepted. No Firebase Admin/service-account private key is needed. Revocation/disabled-account lookup is not implemented: a signed ID token can remain usable until its expiry; immediate server-side logout/revocation is **not** claimed.
- The pilot is **invite-only**: configure at most 10 Firebase test-account UIDs in `PAYMENTS_TESTER_UIDS`; other Google users cannot create orders or read private test purchases/files. The list is never returned by the public config endpoint. An empty/invalid list cannot enable checkout. Provider-signed webhooks can still fulfill previously created orders independently of this browser allowlist.
- An order takes **only `productId` + a random UUID-v4 `requestId`**. UID comes from the verified token. INR/paise price comes from the imported, owner-reviewed server product branch, not caller `amount`, notes, email or branch.
- Fixed prices **per individual subject/exam-session**, not bundles: Computer **1900 paise (₹19)**; Mechanical/Electrical/Civil **2900 (₹29)**; Chemical **3900 (₹39)**. Unknown branches fail closed. Maths-I `DI01000021` and Applied Physics `DI01000121` cannot become paid products, including at SQL constraint level. Notes stay outside this system and remain free. Review any future/common/legacy codes explicitly; catalog overlap/code prefixes must not guess a branch or price.
- Postgres transactions, row/advisory locks, unique payment/receipt/request constraints and durable idempotency prevent duplicate grants and parallel active orders per user/paper. The pilot permits at most **5 new orders/user/hour and 50 total/day**. These reduce accidental API use; they are **not** a general DDoS shield or a guarantee the hosting allowance cannot be exhausted.
- A reservation is saved before calling the provider. Network/uncertain creation failures are kept for operator reconciliation by receipt; a retry does not blindly create another order. While an order is still being created, retry the same request later; do not invent another amount or grant access. Existing created orders can be fulfilled even after new checkout is disabled.
- Before creating a new provider order, strong-read private asset metadata must still match the approved import. Full byte SHA256/size is checked again at delivery. Missing private storage does not fall back to public answers or create an order for a known unavailable paper.
- Callback HMAC uses the **locally stored order ID**, then fetches the canonical order/payment from Razorpay. Only the exact stored INR amount, same order/payment/receipt, a fully **paid order + captured, unrefunded payment** grants ownership. Client-side success, authorized-only/failed payments, arbitrary payment notes and another user's order do not.
- Webhooks verify HMAC over **exact raw bytes** before parsing, use a **different webhook secret**, deduplicate event IDs/body hashes, fetch canonical provider state and grant atomically. Subscribe to **`payment.captured` and `refund.processed`**. Valid unrelated merchant test orders are ignored, not turned into local purchases.
- Any canonically confirmed test refund (including a partial refund) revokes test access. Refund-before-capture delivery cannot later re-grant a revoked payment. No capture, refund, payout or live-money API is called. This defensive test behavior is **not** an agreed customer refund policy; choose that before real selling.
- Purchases and every file request are UID/ownership checked. HTML is returned as **plain text / attachment**, with `nosniff`, sandbox CSP and `private, no-store`; an eventual browser reader must sanitize it, not execute/inject raw HTML. Assets are content-addressed, allowlisted by manifest and buffered at **at most 4 MiB each**; larger files/unsupported active assets are refused, not silently truncated. Additional streaming support needs a separate test/review.
- No secret, raw provider/JWT/database error, Authorization header, customer email or connection string is logged/rendered. SQL stores UID + product/order/payment IDs, amount/status/timestamps—not card credentials or a copied Google profile. API errors are safe codes. Backend outages return an error, never an invented empty purchase history.
- Same-origin relative API, no permissive CORS, browser token-in-query, cookies or browser calls to localhost. Database TLS verification is required. There is no production in-memory purchase fallback.

## Owner setup — keep checkout OFF

### 1. Prepare a separate Free test site in Netlify

Use a **Git-connected** site pointed at this repository/current feature branch. Root `netlify.toml` supplies:

- Build: clean pinned installs at the **repository root** and in `website/`, auth-bundle freshness check, `python3 tools/build_netlify_site.py`.
- **Root `package.json` / `package-lock.json` own all server runtime dependencies** (`pg`, `jose`, `@netlify/blobs`). `backend/` is a source/test directory, not a separate npm project. Netlify's native v2 function tracer must find the packages from its root base; a sibling `backend/node_modules` install alone can produce a ZIP with unresolved imports.
- Publish directory: **`build/netlify-site`** only.
- Functions: **`netlify/functions`**, Node **22.12+** (build selects Node 22).
- SQL migrations: **`netlify/database/migrations`** (native migration convention).

The publish builder uses the exact existing frontend packaging rules and never puts `backend/`, `.env`, dependencies, private imports, SQL or paper data in the static publish folder. The old manual `DiplomaOne-Netlify.zip` is **not** a backend deployment artifact: dragging it into Netlify cannot deploy this API/database. It is intentionally not modified by this backend-only phase.

Do not move your current production domain or disconnect GitHub. Add only the exact new test-site hostname to Firebase Authentication's authorized domains if Google login is tested there. If Netlify's UI labels/settings differ, review before clicking a paid option.

### 2. Provision the included test database deliberately

In the selected Free test site's Database section, create/attach **Netlify Database only if included in the current Free plan**. If using the current Netlify CLI, the owner can use its `db` setup commands on their own logged-in machine; follow [the official CLI guide](https://docs.netlify.com/build/data-and-storage/netlify-database/cli/). Never paste a CLI access token or database connection string in chat.

Netlify supplies **`NETLIFY_DB_URL`** to Functions. The additive migration creates **`diplomaone_test`** only, seeds nothing, revokes PUBLIC schema/table privileges and does not touch notes or any live tables. Verify that the runtime connection uses the intended application/owner role; do not resolve a permissions error by granting anonymous/PUBLIC access. Netlify applies native migrations in the deploy lifecycle once the database is configured. [Migrations](https://docs.netlify.com/build/data-and-storage/netlify-database/migrations/) / [Postgres driver connection](https://docs.netlify.com/build/data-and-storage/netlify-database/tooling/).

### 3. Set private environment variables in Netlify

Use Netlify's environment-variable settings with **Functions runtime scope** and the selected test site's **production deploy context**, not every untrusted PR/preview. Keep secret values private. **Do not upload `.env` to the website or edit the tracked example with real secrets.** A preview context cannot enable new checkout via these flags.

| Variable | Value/action |
| --- | --- |
| `RAZORPAY_KEY_ID` | `rzp_test_ToAdJ9DdVMFeM2` (public test identifier) |
| `RAZORPAY_KEY_SECRET` | Paste its matching Test Key Secret directly into Netlify; not chat/Git/browser. |
| `RAZORPAY_WEBHOOK_SECRET` | Choose/store a separate strong secret (at least 32 characters) privately in Netlify and the Razorpay Test webhook settings. |
| `FIREBASE_PROJECT_ID` | `diplomaone-53b4e` |
| `PAYMENTS_TESTER_UIDS` | At most 10 comma-separated permitted test-account UIDs, copied from Firebase Authentication → Users. These are **UIDs, not tokens, emails or passwords**. No public wildcard. |
| `PAYMENTS_TEST_ENABLED` | **`false`** |
| `PAYMENTS_PRIVATE_MIGRATION_CONFIRMED` | **`false`** |
| `NETLIFY_DB_URL` | Supplied privately by Netlify Database; do not publish/copy into frontend. |

Do not enable Firebase billing. No real key/secret is needed. No bank details, passwords, OTPs or KYC documents should be sent through chat. A public Key ID alone **does not** establish working API access.

After a Git-connected deploy, visiting the test site's **`/api/payments/test/config`** should return JSON with **`mode: "test", enabled: false`**. This is the expected safe setup state, not a checkout test or proof the credentials/database are valid. A missing Function/404 means the static ZIP was deployed or the functions build is not configured; do not work around it by exposing keys in JavaScript.

### Recovery for `Cannot find package 'pg'`

The first user-deployed test build exposed a real packaging defect: packages installed only under `backend/` were not included by Netlify's native v2 tracer, even though the earlier standalone esbuild smoke passed. Root dependency manifests and a new actual-ZIP regression replace that layout/test. It is **not** a missing Razorpay secret or a reason to upgrade a plan.

For the existing Git-connected **test** project:

1. Keep branch **`arena/7e6ec7f8-diplomaone-app`**, the repository root as the base directory, publish **`build/netlify-site`**, and functions **`netlify/functions`**. Use the updated root `netlify.toml`; remove a stale dashboard build-command override only if it still runs `npm ci --prefix backend`.
2. Wait for the new commit's auto-deploy. If it does not start, use **Deploys → Trigger deploy → Clear cache and deploy site** (wording may be **Retry without cache**) and ensure the selected build is the **latest branch commit**, not a retry of the old commit/artifact.
3. Test the **stable site URL** `https://vermillion-pothos-520a34.netlify.app/api/payments/test/config`. The old long deploy-ID-prefixed URL is immutable and will still refer to the broken build. Keep both checkout flags false and all secret values unchanged.
4. If Netlify Team protection displays a login, check the route from the owner's signed-in browser. Do not share Netlify credentials or disable protection just to expose a setup error. A future Razorpay webhook will need a deliberately reviewed publicly reachable endpoint, not this login barrier.

A freshly built **disabled** config should return HTTP 200 with `mode: "test"` / `enabled: false`. That verifies function startup only. Public/live payment readiness still requires the separate gates below.

### 4. Review the private-content migration, then import one real pilot paper

**Do not turn on payment collection just because files were copied.** Existing answers/images/PDFs are public on GitHub. Public/history/downloaded copies cannot be retrospectively made never-public. Before a paid launch:

- decide which full answers/images/solution PDFs must leave the **current public serving/publishing paths**, preserving source content privately;
- stop all existing automatic publishers from republishing the paid full files; future private uploads must not enter a public source repo/workflow;
- keep common subjects/notes free, agree on preview size and continued access/refund terms;
- review exact code/session, original PDF links, canonical branch/price and language/OR/diagram fidelity. A shared subject must not accidentally become two differently priced versions of the same paper.

No files have been moved, deleted, made private or republished by this phase. The current automatic public discovery remains unchanged until the separate migration/browser integration is approved.

For test setup, the **owner** can stage one actual reviewed paper and its diagrams in a private folder **outside public Git repositories**. The importer makes an exact byte copy; it does not generate educational answers, change Drive files, invent a missing session or delete public files. Use a private manifest with this shape (the paths below are examples, not supplied paper files):

```json
{
  "version": 1,
  "id": "DI03000161--summer-2026",
  "title": "Manufacturing Engineering-I",
  "branch": "mechanical",
  "reader": "reader.html",
  "files": ["reader.html", "reader.assets/diagram.png"]
}
```

`reader.html` must be an actual compatible `<main>` / expandable `<details>` card reader, not an embedded PDF. List **every referenced relative image** in `files`; external/public answer-image references, frames, unsupported SVG files, escaping paths/symlinks, duplicate paths, missing diagrams and files over 4 MiB fail import. Inline SVG content is preserved as source text and still needs the existing browser sanitizer at display time. Shape/hash/reference checks do not certify educational correctness.

From the **repository root** (the importer source is still in `backend/`):

```sh
npm ci --ignore-scripts --no-fund
# Safe default: validates/hashes only; no network or credential required.
npm run import:paper -- /PRIVATE/path/paper.json
```

Applying is a separate owner operation, **not performed by the agent**. On the owner's machine, privately configure `NETLIFY_SITE_ID`, an appropriately scoped `NETLIFY_AUTH_TOKEN`, and the selected test database's `NETLIFY_DB_URL`. Do not send any credential here. Then add `--apply`:

```sh
npm run import:paper -- /PRIVATE/path/paper.json --apply
```

The tool writes only to **`diplomaone-private-test`** Blobs, verifies strong-read bytes/hashes, and only then activates SQL metadata. Failed uploads do not activate a partial product. Replacing an existing imported product is refused for explicit review; unused content-addressed blobs may remain after a failure and can be reviewed by the owner. No automatic destructive rollback/cleanup is run. Runtime Functions use Netlify's own blob access context; the owner's personal import token is not needed in the frontend or Function environment.

### 5. Connect the test browser flow and webhook before enabling orders

Still pending: browser Checkout integration and CSP review, updated privacy/refund/access policy, ownership-checked image/card rendering, product mapping/migration review, and provider end-to-end tests. The UI currently still says purchases are not connected; no frontend-only `purchased=true` flag is introduced.

Once those are reviewed, add a webhook in **Razorpay Test Mode** pointing to your test site's **`/api/payments/test/webhook`**, with the separately stored webhook secret. Select **`payment.captured`** and **`refund.processed`**. Configure **automatic capture in Test Mode**; this code does not perform capture/refund/payout requests. Follow the provider's [standard integration guide](https://razorpay.com/docs/payments/payment-gateway/web-integration/standard/integration-steps/) and [webhook guidance](https://razorpay.com/docs/webhooks/).

Only after the launch gates are met should the owner deliberately set **both** `PAYMENTS_PRIVATE_MIGRATION_CONFIRMED=true` and `PAYMENTS_TEST_ENABLED=true` on that test site's production context and redeploy. Do not enable them now on the public website. Even then, a live key is rejected and no actual customer payment can be taken by this implementation.

## API contract for the upcoming browser integration

All responses are `mode: "test"` and `no-store`. Protected browser routes require an **invited test UID** and **`Authorization: Bearer <valid Firebase ID token>`**. Token placeholders below are documentation, not credentials to request/share. POSTs other than webhooks must also be same-origin JSON requests; no user/price fields are accepted.

| Endpoint | Contract |
| --- | --- |
| `GET /api/payments/test/config` | Public, off by default. When configured/allowed, returns public product metadata/key ID, not private file keys/answers or secrets. Readiness here is not a real gateway test. |
| `POST /api/payments/test/orders` | `{productId, requestId}`; requestId is a UUID v4. Returns the server-created test order/key ID/INR amount. Same active paper/order is reused; a creation in flight returns `order_being_created`; an uncertain creation requires operator reconciliation by receipt. |
| `POST /api/payments/test/verify` | `{orderId, paymentId, signature}` from Checkout. Server checks order owner, HMAC and canonical captured/unrefunded payment before granting. |
| `POST /api/payments/test/webhook` | Provider's raw signed body + signature/event-ID headers. No user Google login on this route; HMAC and stored canonical order are mandatory. |
| `GET /api/payments/test/purchases` | Only that UID's actual test purchase/access records. DB/setup failure is an error, not `[]`. |
| `GET /api/payments/test/content/<productId>` | Purchaser-only reader asset ID + mapping of allowed asset paths/hashes; not a public signed-URL bearer token. |
| `GET /api/payments/test/content/<productId>/<sha256>` | Purchaser-only, hash-verified bytes, no arbitrary blob path/URL, no public fallback. Authenticated fetch required (including future image fetches). |

Do not pass a Firebase/Google token in a URL, dump it to logs/DOM or return it from a general-purpose public profile API. Do not assume closing the popup/sign-out invalidates an already issued server token instantly. Access checks always use the database, not a browser storage flag.

## Validation and remaining acceptance gates

Run these from the **repository root**, not `backend/`:

```sh
npm ci --include=dev --ignore-scripts --no-fund
npm run check
npm test
npm run check:bundle
npm audit --audit-level=moderate
```

Tests use **local PGlite (real Postgres engine/transactions/constraints), generated RSA-signed JWTs, mock Razorpay/private storage and fake unit-only secrets**. `check:bundle` uses pinned **`@netlify/zip-it-and-ship-it`** with the real `netlify.toml` settings. For v2 functions Netlify selects **NFT** even when `node_bundler = "esbuild"` is set. The test checks the actual ZIP contains every runtime package, extracts it **outside the checkout**, and runs its ESM module **and Netlify-generated Lambda v2 entry/bootstrap** with no repository dependency fallback. Both the no-secret and configured-but-disabled cases must return safe disabled JSON; the latter uses fake credentials only and never connects to a database/provider. This replaces the inadequate standalone esbuild-only smoke.

The root's dev-only Netlify packager uses explicitly pinned patched `glob`/`minimatch` overrides to avoid known audit advisories; the actual packaging/ZIP tests exercise that tooling. These tools and PGlite are not shipped in the Function ZIP. Deployment tests also verify the public frontend output excludes all backend/secret/private/source material. Tests are not a provider certification, a real charge, a real database/blob deploy or proof of account-plan availability.

Before marking test checkout complete, verify on the actual selected Netlify test site:

- included Free database/functions/blob availability, Node/runtime routes, migrations and safe disabled configuration;
- owner-only secret settings (production context/Functions scope), no secrets in downloaded frontend assets;
- private import/delivery hashes and no current-public full-answer fallback;
- real Google login/session with correct Firebase project and same-origin authenticated API;
- actual Razorpay **test** capture, failure/cancel/authorized-only behavior, callback and webhook replay/reordering, wrong UID/amount/paper, refund revocation and reload purchases;
- no test ownership in any future live namespace; no paid upgrades, recharge, real card payment, capture/refund API calls or Firebase billing;
- completed browser integration/security/privacy/policy review and deliberate approval before any future live deployment.
