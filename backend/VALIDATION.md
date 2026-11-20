# Test-backend validation record

## Completed locally

- Clean pinned Node 22 dependency installation and syntax checks passed.
- **43 backend tests passed** (including the invite-only tester gate): generated RSA Firebase JWT verification, strict test-only configuration, fixed per-paper INR pricing/free common codes, order ownership/idempotency/concurrent reservation, pilot budgets, captured-payment verification, raw-body webhook signatures/replay, refund-before-capture handling, SQL uniqueness/transaction rollback, private asset readiness/ownership/hashes, safe errors, import path/symlink/reference/size checks, disabled actual entry and publish isolation.
- Database tests execute the additive migration and queries in **PGlite's Postgres engine**. This exercises real SQL/constraints/transactions, not a fake JSON purchase database. It does not certify distributed Netlify/Postgres network behavior or the operator's actual database role.
- The **actual Function entry** was bundled and smoke-run without secrets/network; native test route and `enabled: false` response passed. Both enabled backend logic and error cases use explicit unit doubles, not the owner's Razorpay account.
- **13 existing auth/adapter + 11 existing account/DOM tests passed**; auth SDK bundle freshness passed.
- All **8 existing offline paper/reader/listing/placement suites passed**, including the 49-paper/1,412-part refresh, Electrical answers and the Mechanical source/placement regressions.
- **2 Netlify frontend package tests + 5 existing ad-declaration Python tests passed**.
- Netlify TOML parsed and the publish/functions directory contract passed. All 12 generated public publish files match the existing manual ZIP byte-for-byte. No `backend/`, `.env`, SQL, dependencies or private source data enters that directory.
- Backend and website `npm audit --audit-level=moderate`: **0 vulnerabilities**. `git diff --check` passed.
- The existing frontend ZIP was deliberately not changed: **540,762 bytes**, SHA256 `2e4c509ad7991c0775cb8712001d6877c1d228f5568be4975947bb2ad19bea6c`.

## Not completed / no claims made

- No Netlify account, Free/legacy-plan capability, Functions deployment, real Database provisioning/migration, Blobs import or credentials were configured by the agent.
- No request was made to Razorpay with the owner's API credentials; no real or provider-backed test payment/capture/refund was made. Unit-only secrets and provider doubles are not proof that the public Key ID is active or matched to a secret.
- No live-mode path/key acceptance is implemented, and no billing, recharge, payout or Firebase database/billing change was performed.
- No paper/source/Drive item was moved, deleted, migrated, replaced, made private or newly published. Existing public copies/history remain public; no new frontend lock conceals this fact.
- The browser still has no connected Buy button/purchase-history/private-reader flow. Its existing placeholder remains truthful. Browser integration/CSP/privacy/refund/access policy and private publisher/migration review are mandatory gates before enabling the two test-checkout flags.
- No general DDoS resistance, unlimited free hosting, instantaneous token revocation, provider availability or protection of previously public/downloaded copies is promised.

Deployment/operator instructions and remaining end-to-end acceptance checks are in [README.md](README.md). Keep checkout disabled until those are met.
