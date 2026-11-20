# Test-backend validation record

## Deployment crash regression: missing `pg`

The owner's first Netlify test deployment reached the function but crashed at ESM startup with **`ERR_MODULE_NOT_FOUND: Cannot find package 'pg'`**. The agent reproduced that exact error using Netlify's real `@netlify/zip-it-and-ship-it@16.6.0` packager on the original dependency layout. The resulting v2/NFT archive had five files and unresolved bare runtime imports; sibling `backend/node_modules` packages were not traced into it. The earlier standalone esbuild smoke was insufficient and did **not** establish correct deploy packaging.

Correction: the server's pinned npm manifest/lock now live at the **repository/Netlify base**; `npm ci` installs runtime packages where the function tracer can include them. Netlify build/CI/import commands and docs use the root installation. Root JS remains **CommonJS** so existing `tools/*.js` behavior is not changed; server source/entry stays explicit `.mjs`. No purchase logic, secrets, service provisioning or checkout flags changed.

`npm run check:bundle` now uses the **actual Netlify packager and TOML settings**, which select **NFT** for this native v2 function. The corrected ZIP includes `pg`, `jose`, `@netlify/blobs` and their traced runtime dependencies. It is extracted into an isolated temporary directory **outside the checkout** and executed with a stripped environment / no `NODE_PATH`. Dependency resolution is asserted to stay inside that artifact. Both the app's ESM default export and Netlify's generated Lambda v2 bootstrap/entry return disabled-config HTTP 200 in **two cases**: no secrets, and unit-fixture configuration with checkout still disabled. The latter also exercises creation of the real PG client/pool without making a database/provider call. Native route metadata is checked. The old dependency layout failed this kind of artifact import; the new one passes. Dev-only packaging glob/minimatch dependencies use tested, pinned patched overrides.

**A new owner-side Netlify deployment is still needed to confirm the hosted fix.** The agent cannot certify the protected site's new build from local artifacts/CI, and old deploy-ID URLs remain immutable.

## Completed locally for the packaging correction

- Clean pinned Node 22 root dependency install and syntax checks passed, without any old `backend/node_modules` fallback.
- **44 backend tests passed**, including the new root-dependency/lockfile/Netlify-base regression plus all existing Firebase JWT, fixed INR pricing/free-common-code, UID/order ownership/idempotency/concurrency, pilot budget, capture/HMAC/webhook/replay/refund, SQL rollback/constraints, private hash/size/reference/path and tester-allowlist cases.
- Database tests execute the additive migration and queries in **PGlite's Postgres engine**. This exercises real SQL/constraints/transactions, not a fake JSON purchase database. It does not certify distributed Netlify/Postgres network behavior or the operator's actual database role.
- Actual isolated **Netlify Function ZIP and native Lambda v2 entry** passed both no-secret and configured-disabled smoke cases, with mock AWS response streaming only. No provider-backed payment test is claimed.
- **13 existing auth/adapter + 11 existing account/DOM tests passed**; auth SDK bundle freshness passed.
- All **8 existing offline paper/reader/listing/placement suites passed**, including the 49-paper/1,412-part refresh, Electrical answers and Mechanical source/placement regressions.
- **2 Netlify frontend package tests + 5 existing ad-declaration Python tests passed**.
- Netlify TOML/publish isolation passed. All 12 generated public frontend files match the existing manual ZIP byte-for-byte. No backend, npm manifests/lockfiles, `.env`, SQL, dependencies or private source enters that static output.
- Root and website `npm audit --audit-level=moderate`: **0 vulnerabilities**. `git diff --check` passed.
- The frontend ZIP was deliberately not changed: **540,762 bytes**, SHA256 `2e4c509ad7991c0775cb8712001d6877c1d228f5568be4975947bb2ad19bea6c`.

## Not completed / no claims made

- The **owner** created the initial test site and supplied its startup error. No Netlify account/plan setting, Functions redeployment, actual database provisioning/migration, Blobs import or private credentials were configured by the agent.
- The public agent-side fetch reached **Netlify Team protection**, not the app/API, so hosted readiness cannot be inferred. Do not share Netlify credentials or disable protection simply to expose setup errors.
- No request was made to Razorpay with the owner's API credentials; no real or provider-backed test payment/capture/refund was made. Unit-only secrets/provider doubles are not proof that the supplied public Key ID is active or matched to a secret.
- No live-mode key/path acceptance is implemented. No billing, recharge, payout or Firebase database/billing change was performed.
- No paper/source/Drive item was moved, deleted, migrated, replaced, made private or newly published. Existing public copies/history remain public; no frontend lock conceals this fact.
- The browser still has no connected Buy button/purchase-history/private-reader flow. Its existing placeholder remains truthful. Browser integration/CSP/privacy/refund/access policy and private publisher/migration review are mandatory gates before enabling the two test-checkout flags.
- No general DDoS resistance, unlimited free hosting, instantaneous token revocation, provider availability or protection of previously public/downloaded copies is promised.

Owner recovery steps and remaining end-to-end acceptance gates are in [README.md](README.md). Keep checkout disabled until those are met.
