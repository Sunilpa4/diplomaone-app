# Netlify / Firestore / Razorpay TEST backend

## Status — keep checkout OFF

The owner chose **Cloud Firestore instead of Netlify Database** after Netlify requested a paid option. The owner says Firebase billing is **already enabled** and reports creating a **Standard edition, `(default)` database in `diplomaone-53b4e`, Production mode**. The agent has not inspected that cloud database, configured its IAM/credentials/rules, uploaded papers or tested a real connection to it.

This backend uses **Netlify Functions + Firestore records + private Netlify Blobs files**, with existing Firebase Google sign-in. It no longer needs PostgreSQL, `pg`, `NETLIFY_DB_URL`, Netlify Database or a SQL migration. No old database was provisioned or contains purchases to migrate. No additional Firebase Storage/Functions service, plan upgrade, billing change or paid resource is provisioned by this code.

**This is not a finished checkout.** No Buy button, connected My purchases screen, private browser reader, provider webhook, private paper import or actual Razorpay payment has been set up. There are no seeded products/fake purchases. Existing public reading access, publishers, paper sources and the frontend-only ZIP are unchanged. Both checkout flags remain **false**.

Firebase's free Firestore allowance can reduce initial costs, but an already billed project is **not a hard spending cap**. Reads, writes, retries, storage and usage above applicable allowances can incur charges. Review the project's actual usage/billing; do not upgrade Netlify just for a database. The small order budgets below do not limit all API/database traffic or prevent denial of service. [Firestore pricing](https://firebase.google.com/docs/firestore/pricing) / [quotas](https://firebase.google.com/docs/firestore/quotas).

## Implemented boundaries

- **Test only:** fixed `/api/payments/test/` routes; `rzp_live_` keys refused. Records use **`diplomaone_test/v1/**`** in the fixed project/default database, never a live namespace. Future live selling needs a separate review/data namespace; test ownership is not a real purchase.
- **Server identity:** Google's public JWKs, RS256, exact Firebase audience/issuer/project, valid time/UID claims and Google provider. The older Android project `diplomaone` is not accepted. Verification of ID tokens does not use the database service-account private key. Disabled/revoked-account lookup is not implemented: already issued tokens may remain usable until expiry.
- **Explicit server credentials:** Firestore's privileged Node client receives only validated same-project service-account email/RSA private key and verified HTTPS endpoint. It does not discover an unrelated ADC project or accept a production emulator override. Public Firebase web config/API keys are **not** Admin credentials.
- **Invite-only:** at most 10 Firebase tester UIDs; empty/invalid lists cannot enable checkout. Protected browser requests require an invited UID; provider-signed webhooks may fulfill previously created orders without browser login.
- **Prices:** one individual subject/exam-session, not a bundle. Computer **₹19 / 1900 paise**; Mechanical/Electrical/Civil **₹29 / 2900**; Chemical **₹39 / 3900**. Canonical product metadata/branch is re-read inside the reservation transaction; browser amount/UID/branch fields are refused. Common Maths-I `DI01000021`, Applied Physics `DI01000121` and existing notes remain free. Unknown branches fail closed; catalog overlap must not guess a branch.
- **Durable transactions:** atomic request mappings, active-order pointers, unique provider-order/payment documents, grants/revocations and event-body hashes. UIDs and compound identity keys are hashed into safe document paths. All transaction reads precede writes; retried callbacks do not call Razorpay or storage. No production memory fallback.
- **Rolling order budgets:** shared transactionally updated bounded timestamp arrays permit at most **5 new orders per UID/trailing hour** and **50 total/trailing 24 hours**. No background scan, TTL service, composite-index deployment or database count query is needed. These are pilot safeguards, not a billing or DDoS guarantee.
- **Provider safety:** save reservation before provider creation; uncertain creation remains blocked for reconciliation by receipt, not blind duplicate retry. Missing private assets stop provider creation. Callback HMAC uses the stored order ID; canonical Razorpay order/payment reads must confirm the exact receipt, UID-bound local order, INR amount, fully paid order and captured/unrefunded payment. Browser success/notes alone never grant access.
- **Webhooks/refunds:** raw-byte HMAC with separate secret, event-ID/hash replay checks and atomic writes. Unrelated merchant test orders cannot create local purchases. Any confirmed test refund, including a partial one, revokes that order. Refund-before-capture cannot later re-grant it; an old refunded order cannot revoke a newer repurchase. No capture, refund, payout or live-money request is implemented. This defensive test behavior is not an agreed customer refund policy.
- **Private delivery:** Firestore stores bounded allowlisted metadata and purchase records, **not answer HTML/PDF/image bytes**. Files use the separate private **`diplomaone-private-test`** Blobs store. Every content request checks UID/ownership, allowed manifest asset, SHA256 and size. Maximum **4 MiB/file**, 300 metadata entries/paper. HTML is plain text/attachment with sandbox CSP, `nosniff` and `private, no-store`; a future reader must sanitize and authenticate image fetches. No public full-answer fallback.
- **Safe errors/deployment:** no raw SDK/provider/JWT errors, credentials, tokens or customer email in API responses/application logs. Firestore records contain UID/product/order/payment IDs, amounts/status/timestamps, not card credentials or copied Google profiles. Database failure is an error, never invented purchase history. Same-origin relative URLs, HTTPS, no permissive CORS/cookies/token-in-query. Disabled config performs no database/provider/storage operation.

### Firestore is not a browser payment database

All access to this namespace is through authenticated/verified **server routes**. Keep client reads/writes denied, including signed-in users. Do not add `allow write: if request.auth != null`, public/test-mode rules, a client `purchased=true` field or browser Admin credentials. Broad overlapping `allow` rules can override an apparent deny block; review the effective rules, not only one match statement.

Server libraries bypass Firebase client Security Rules and use **IAM**. A default-deny database does not block a properly authorized server; opening rules is not the fix for an IAM error. Conversely, client rules do not contain a leaked service-account key. [Official server client libraries](https://firebase.google.com/docs/firestore/client/libraries).

## Owner setup — secrets stay outside chat/Git/browser

### 1. Keep the existing Git-connected Netlify test deployment

Do not disconnect GitHub, move the production domain or upgrade Netlify. Root `netlify.toml` supplies the clean root/website installs, public builder, **`build/netlify-site`** publish directory, **`netlify/functions`**, and Node **22.12+** (build selects 22).

Root `package.json`/lock own runtime dependencies (`@google-cloud/firestore`, `jose`, `@netlify/blobs`; `parse5` is used by the private importer). `backend/` is not a separate npm project. The real Netlify v2 tracer must resolve packages from the repository base. Static publish output is an explicit 12-file allowlist and excludes backend, dependencies, secrets, private content and test tooling.

The manual **`DiplomaOne-Netlify.zip` is frontend-only**; drag-and-drop cannot deploy this API. It remains unchanged.

### 2. Verify the reported Firestore settings; keep rules locked

Use existing project **`diplomaone-53b4e`**, **Standard edition**, **`(default)`**, Production rules. Do not create another project/database, enable Firebase Storage/Functions, add a paid Netlify database or switch to Test mode. No collections need manual seeding: verified private import and server transactions create records later.

The code has no `firebase deploy` command or production rules file. `backend/test/firestore-deny.rules` is **emulator-only** and is never deployed to the owner's project.

### 3. Prepare a dedicated, limited server identity

On the owner's machine/console only, use Google Cloud **IAM & Admin → Service Accounts** for this same project. Prefer a dedicated account such as `diplomaone-payments-test`, with **Cloud Datastore User (`roles/datastore.user`)**, not Owner/Editor. Review database-scoped IAM conditions if other sensitive Firestore workloads share the project. That role is privileged; Security Rules do not restrict this server to a collection.

If an owner-managed service-account key is required for Netlify, create/download it **privately**, never into this repository/public Drive/chat. Transfer only its `client_email` and `private_key` values directly into the backend environment below; the public Firebase web API key cannot substitute. Do not share the JSON file, PEM, screenshots containing values, Razorpay secret, password, OTP or access token here. Secure/delete the local downloaded copy according to your credential policy; revoke/rotate the key if exposed. No key was created by the agent.

### 4. Set Netlify Functions-only private environment values

Use the selected test site's **production context** (the site's main deploy may track this feature branch), **Functions runtime scope**, not every PR/deploy preview. Keep secrets out of tracked `.env.example`, frontend/ZIP, build outputs and browser JavaScript. Preview/branch-deploy contexts cannot enable new checkout even if flags are inherited.

| Variable | Private owner action |
| --- | --- |
| `FIREBASE_PROJECT_ID` | `diplomaone-53b4e` |
| `FIRESTORE_DATABASE_ID` | `(default)` (optional; no other value accepted) |
| `FIREBASE_CLIENT_EMAIL` | Dedicated same-project service-account `client_email`, not a Google login email |
| `FIREBASE_PRIVATE_KEY` | Its PEM `private_key`, multiline or with literal `\n` escapes; never chat/Git/browser |
| `RAZORPAY_KEY_ID` | Public Test ID `rzp_test_ToAdJ9DdVMFeM2` |
| `RAZORPAY_KEY_SECRET` | Matching **Test** key secret, directly in Netlify |
| `RAZORPAY_WEBHOOK_SECRET` | Separate strong secret, at least 32 characters; later match Razorpay's Test webhook setting |
| `PAYMENTS_TESTER_UIDS` | 1–10 comma-separated Firebase Authentication **UIDs**, not tokens/emails/passwords |
| `PAYMENTS_TEST_ENABLED` | **`false`** |
| `PAYMENTS_PRIVATE_MIGRATION_CONFIRMED` | **`false`** |

No `NETLIFY_DB_URL`, ADC file, `GOOGLE_APPLICATION_CREDENTIALS`, `FIRESTORE_EMULATOR_HOST` or frontend key substitution is needed. Production refuses the emulator environment. These checks validate configuration shape, **not actual cloud permissions/connectivity**.

After redeploy, `/api/payments/test/config` must still return:

```json
{"mode":"test","enabled":false,"reason":"setup_required","currency":"INR"}
```

The owner already confirmed that response after the earlier packaging repair. It proves disabled function startup only, **not Firestore/Razorpay readiness**. Use the latest branch deployment/stable URL, not an immutable old deploy-ID URL. Agent-side requests remain behind Netlify Team protection; do not remove protection/share login just to expose setup status. A future provider webhook needs deliberately reviewed reachability.

For an independent **read-only Firestore check**, the owner may securely supply the three Firebase server values in their local environment and run from the repository root:

```sh
npm ci --include=dev --ignore-scripts --no-fund
npm run check:firestore
```

This reads at most one product record; it never writes/seeds data, calls Razorpay, changes rules or enables checkout. Successful output says `readable: true` / `checkoutChanged: false`. Failed output is sanitized. Do not paste real environment values into a command committed to Git, shell history, chat or CI.

### 5. Separately review private publishing/migration before importing

**Existing answers/images/PDFs are public on GitHub. Copying them privately or hiding a Buy button does not secure the public copies.** Before charging, review which current public files/publishers must change, preserve content privately, stop future paid uploads going to public publishers and agree preview/refund/access terms. Historical/downloaded copies cannot become never-public. No such public-content migration has been performed here.

Review exact code/session, branch/price, common subjects, language, OR choices and diagrams. Do not invent missing exam sessions, replace question cards with PDF frames or alter Drive files. The eventual browser reader must reuse the existing strict sanitizer and fetch private images through authenticated routes, without public fallbacks.

An owner can stage **one actual reviewed pilot paper** in a private folder outside public repositories, with a private manifest shaped like:

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

These paths are examples, not supplied paper files. The HTML must contain a compatible `<main>` / expandable `<details>` card reader, not an embedded PDF. List every relative image. External/public answer-image references, frames, unsupported active assets, escaping paths, duplicate/missing paths and oversized files fail import. Shape/hash checks are not educational correctness certification.

```sh
# Safe default: local validation/hashing only, no network or credentials.
npm run import:paper -- /PRIVATE/path/paper.json
# Separate owner operation after review and private environment setup:
npm run import:paper -- /PRIVATE/path/paper.json --apply
```

`--apply` additionally requires owner-private `NETLIFY_SITE_ID`, scoped `NETLIFY_AUTH_TOKEN` and the three Firebase server variables. It uploads only to **`diplomaone-private-test`**, strong-read verifies exact bytes/hashes, and **then** atomically creates Firestore product metadata. It does not alter public files or enable checkout. Duplicate imports require review; failed uploads do not activate partial products. Unused content-addressed blobs may remain for owner review, with no destructive automatic cleanup. Netlify runtime uses its own Blobs context, not the owner's personal import token.

### 6. Complete browser/provider/policy gates, then deliberately approve testers

Still pending: SDK-contained ID-token access, same-origin Bearer requests, Razorpay Test Checkout UI/CSP, My purchases, sanitized ownership-checked card/image reader, real product/publisher migration, privacy/refund/access information and provider-backed acceptance tests.

Later configure **Razorpay Test Mode** automatic capture plus signed **`payment.captured`** / **`refund.processed`** webhooks at `/api/payments/test/webhook`, after reviewing public reachability. No capture/refund/payout API is called by this code. Only after all gates are met should the owner intentionally set **both** checkout flags `true` on the selected test site's production context. Do not do that during database setup. [Razorpay integration guide](https://razorpay.com/docs/payments/payment-gateway/web-integration/standard/integration-steps/).

## API contract for upcoming browser work

All responses are test-mode, non-cacheable; protected browser calls require an invited Google UID and same-origin **Bearer ID token**. Never put tokens in DOM, URLs, logs or custom storage. POST bodies allow only the named fields.

| Route under `/api/payments/test` | Contract |
| --- | --- |
| `GET /config` | Public; disabled by default. Only an enabled catalog exposes public metadata/prices/Test Key ID, not files/secrets. |
| `POST /orders` | `{productId, requestId}` with UUID v4; server price, durable reservation/reuse. Creation-in-flight/uncertain orders fail closed. |
| `POST /verify` | `{orderId, paymentId, signature}`; stored UID/order HMAC + canonical captured payment before grant. |
| `POST /webhook` | Exact provider-signed raw body/event-ID; no Google login, no arbitrary order creation. |
| `GET /purchases` | Only that UID's actual test access records. Database failure is not an empty success. |
| `GET /content/<productId>` | Ownership-checked manifest/reader asset mapping. |
| `GET /content/<productId>/<sha256>` | Ownership/hash/size-checked bytes; authenticated images too; no public bearer URL/fallback. |

## Validation

From the repository root:

```sh
npm ci --include=dev --ignore-scripts --no-fund
npm run check
npm test
npm run check:bundle
npm audit --audit-level=moderate
```

`npm test` uses generated local test-only RSA keys, mock provider/storage and an explicitly **test-only document/transaction double**. The double checks read-before-write and retries, but is not proof of actual Firestore behavior. The browser-rules case intentionally skips without the real emulator.

**CI additionally runs the entire suite against the official Firestore emulator**, Java 21, fixed **`demo-diplomaone-payments`** on loopback only, and deny-all client rules. It tests genuine transactions, concurrency/replay/rollback, budgets, refund ordering, queries and denied anonymous/signed-in browser reads/writes. No real project, login, service-account key or billable resource is used. Emulator JAR version/size/SHA256 are pinned in `backend/test/firestore-emulator.json`; CI downloads test tooling outside Git. Locally, obtain that official JAR, set `FIRESTORE_EMULATOR_JAR` privately to its path and run `npm run test:firestore` with Java 21 installed. The runner verifies its checksum and stops its child emulator afterwards; it refuses an existing server on the test port.

`check:bundle` uses the actual pinned **Netlify v2/NFT** packager/TOML settings, extracts the deployment ZIP outside the checkout and verifies every runtime import resolves inside the ZIP. The no-secret and configured-but-disabled ESM/native Lambda v2 cases run with network transports blocked. During emulator CI the actual packaged Firestore SDK also performs real read/write/query/transaction/delete operations against the local demo emulator, catching missing dynamic SDK/proto assets. The initial direct-esbuild-only test missed the old `pg` packaging bug; it is not used as deployment evidence anymore.

The public 12-file output must still byte-match the frontend ZIP, with no backend/secrets/private files. Emulator/packager tools are not shipped in the function ZIP. See [VALIDATION.md](VALIDATION.md) for results and explicit remaining cloud/provider gates.
