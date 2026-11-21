# Payment-flow validation record

## Current revision — individual-paper LIVE flow (2026-10-30)

The owner chose the real individual-paper flow rather than another separate test-setup walkthrough. The implementation connects **selected paper/price → Google → same-origin server order → UPI-first Razorpay Checkout → server-verified full capture → only that UID/paper**, My purchases and private card/image/PDF delivery. Test routes/keys/records remain separate.

**Implemented is not launched. All four live switches stay OFF.** Actual public-source migration/private import, merchant activation/reachable webhook, approved customer support/refund/access terms and controlled real delivery acceptance are still required. See **[LIVE-LAUNCH.md](LIVE-LAUNCH.md)**. No automated result below certifies the owner's project or a real payment.

### Executed locally on this change

| Gate | Observed result |
| --- | --- |
| Node syntax / all server, importer, migration and test modules | Passed |
| Backend API/domain/repository/security/import/migration tests | **88 cases: 87 passed, 1 emulator-only browser-rules case skipped locally** |
| Frontend controller/request/account/purchase UI | **67 passed:** 16 Auth, 12 diagnostic helper, 14 payment helper, 16 account/router, 9 integrated purchase UI |
| Actual packaged SPA in offline Chromium | **9 live-flow scenarios passed:** English/Gujarati at 1365/390/320 px, plus checkout OFF, pending capture and navigation-before-callback |
| Retained offline Chromium regressions | **9 diagnostic scenarios + 33 account checks passed**, including actual bundled Firebase SDK readiness/network-failure smoke and project-subpath loading |
| Existing offline reader/listing/source suites | **10 passed** across Mechanical/Electrical/Computer/common/refreshed papers; cards, text, supplied languages, diagrams, OR, fractions, grouping and exam/PDF identities preserved |
| Frontend ZIP/package tests | **2 passed**, including extracted controller/reader/content tests and exact committed ZIP equality |
| Public publisher and source tests | **22 publisher cases passed**; PDF batch, common-subject, card-file and both Mechanical source-identity cases passed |
| Unchanged source-PDF pixel audit | **3,129 excerpts match pixel for pixel** with pinned PyMuPDF/Pillow; no source bytes changed |
| Ad declarations | **5 passed**; no ad script or invented unit added |
| Auth bundle freshness / root and website audits | Passed; **0 vulnerabilities** in each production manifest's audit |
| Workflow YAML/changed shell syntax / diff whitespace | Passed |

The purchase UI tests run the actual SPA, controller and narrow payment helper with only Auth/HTTP/Checkout boundaries doubled. They check agreed prices, sign-in, selected-paper capture and cards, failed/pending fulfillment, authenticated images/PDFs, purchases/reload/account denial, cancellation/revocation, no public fallback, free subjects and discovery during a GitHub outage. Neither sign-in nor a simulated browser callback is a real entitlement.

The payment helper tests reject unapproved origins/routes, extra/malformed/test-mode responses, cross-paper success, stale tokens/callbacks, redirects/HTML hosting gates, oversized/invalid manifests, missing images and concurrent duplicate buys. No generic ID-token getter, arbitrary authenticated fetch, browser Firestore write, app-managed token/answer storage or payment token sent to Razorpay exists.

The actual offline Chromium payment test uses the **built 12-file frontend** and real Auth/payment adapter bundled with an explicit Firebase boundary replacement. **Every network request is fulfilled locally or blocked**; it makes no Google/provider/cloud request or charge. It checks direct user gestures, Authorization/Origin boundaries, real object-URL images/PDF download, expandable cards/image dialog, purchases after reload, other-paper denial, expected warnings, CSP and horizontal layout in both languages. Screenshots are ignored test artifacts, not real customer purchases. The rupee glyph is explicitly covered by the existing self-hosted font.

**Automatic UPI/QR follow-up:** the owner selected the verified gateway flow. New assertions check the exact standard UPI-first `config.display` sequence, hidden Collect/COD, retained default online methods, no custom block that bypasses Collect hiding, fresh per-Checkout options and the unchanged server-owned order ID/amount/key. English/Gujarati SPA/browser checks cover method/PIN guidance, desktop-vs-mobile/merchant availability caveats, no app-managed static QR/UPI URL/PIN/VPA form and rejection of a typed transaction/QR-success callback without valid signed verification. The nine packaged Chromium scenarios and all 33 account/nine diagnostic checks were rerun; the 390px English locked-paper screenshot was visually reviewed. These tests do **not** execute Razorpay itself, prove merchant UPI/QR availability, display an actual provider QR or complete an app handoff/payment.

The refreshed local run also re-executed all 88 backend cases (87 pass/one official-emulator-only skip), the actual NFT archive/four disabled configurations, migration dry run, Auth freshness and both package tests. Evidence is under ignored `build/upi-*-validation*.log`. One preliminary local deployment assertion compared the new source with the not-yet-rebuilt tracked ZIP; rebuilding the ZIP before the dependent backend run resolved it without changing assertions or backend authorization.

The local repository harness is an explicit **test-only document/transaction double**, not a production memory fallback or real Firestore engine. It checks atomic commits, conflicts/retries and read-before-write. The genuine emulator gate below remains mandatory for both fixed test/live namespaces and denied client reads/writes.

### Actual deployment artifact checks

`npm run check:bundle` used the pinned **Netlify v2/NFT** packager and root TOML, not a standalone esbuild approximation. Observed compressed Function archive: **2,779,108 bytes**. It was extracted outside this checkout; Firestore/JWK/Blobs dependencies resolved inside that ZIP. All fetch and Node transports were blocked.

Four isolated ESM + **native Lambda v2 bootstrap** cases passed for both live/test routes:

1. No secrets (no accidental database/provider access).
2. Firestore-only / checkout OFF, with no Razorpay secret.
3. Test-configured / checkout OFF.
4. Separately live-configured / checkout OFF.

These checks verify real artifact startup, disabled config/authentication/origin gates and existing-owner initialization without gateway keys. They do **not** prove owner credentials, real IAM/connectivity, storage availability, live Checkout provider/CSP behavior or reachable webhooks.

The rebuilt **frontend-only** `DiplomaOne-Netlify.zip` contains exactly **12 public files**, **559,352 bytes**, SHA256:

```text
684ad333547676d29e073b8d31cf5e25e277e0d87cebef75b11b96c8322202cf
```

Static output byte-matches the ZIP and excludes backend files, source papers, private imports, dependencies, tests/tooling and secrets. Auth bundle: **125,516 bytes**; license: **23,256 bytes**. Only Maths-I/Applied Physics legacy paper paths redirect publicly. Other `/papers/*` paths return a 404 frontend. **Drag/drop does not deploy Functions**; the real API requires the reviewed Git-connected root build.

### Offline migration checks and known launch blocker

`npm run prepare:live-papers` validated the actual retained sources **without writing/exporting/importing them or making network calls**:

- **76 priced papers / 3,380 files / 169,975,648 bytes**, including optional PDFs.
- Explicit **54-code** branch mapping; the two common/free subject codes are excluded.
- Shared importer card/image/path/size validation; no invented sessions, translated answers or PDF-only reader substitution.

Six migration/audit groups pass, including byte-preserving synthetic exports, exact file hashes, 0700/0600 output, overwrite rejection, optional PDF exclusion, unknown branch/missing image/PDF-only/symlink rejection, build-only output confinement, mistyped audit roots and safe public metadata/free-vs-paid distinctions. Synthetic test exports are deleted; **no actual private export or cloud import was performed**.

`npm run audit:public-papers -- . --report=build/final-public-migration-audit.json` returned the expected **exit 2**, **ready=false, 3,418 files requiring migration**. This is a launch blocker, not an audit crash. The new public publisher prevents future paid HTML/PDF/image copies, but it does not silently remove existing ones. Only this app checkout was scanned; public-content checkouts, Git history, releases, caches and downloaded copies are not certified private. No source/Drive cleanup or history rewrite was performed.

### Required CI: official Firestore emulator + extracted packaged SDK

Local Java/emulator tooling is unavailable, so the local skipped client-rules case is **not** treated as passed. The payment workflow must run all **88** cases with Java 21 and the official pinned **Firestore emulator 1.22.0**, **136,707,194 bytes**, SHA256:

```text
9b6498b7f62714d67f48f59b3818883cd682dbcd46b9f59511de81c97bb5166c
```

`npm run test:firestore` verifies the JAR, refuses an already-open test port, strips owner credentials and uses only **127.0.0.1:8085 / demo-diplomaone-payments** with emulator-only deny-all rules. Test files are sequential; cases explicitly exercise concurrency. It then uses the **actual isolated Function ZIP's Firestore SDK** for real read/write/query/transaction/delete operations against that DEMO engine and stops its child emulator. No cloud project/login/key, rule deployment or billable provisioning is involved.

**Passed for implementation commit `9a901fb46c13d3e78075753387d72f5737bdd985`:** [payment run 44721602034 / job 136238463106](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44721602034/job/136238463106), **1m36s**. The GitHub job API independently reports SUCCESS for the required **real Firestore transactions/denied client rules/packaged SDK DEMO-emulator step**, the offline packaged Chromium purchase step and the actual-source migration dry run. The runner executes the complete 88-case suite on the real SDK/DEMO engine; the locally skipped browser-rules case is included. No raw provider or owner-cloud acceptance is inferred from that result.

The same implementation revision's [website validation 44721602013](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44721602013), [free-only solved-paper publisher/source validation 44721601935](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44721601935), [content validation 44721602157](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44721602157) and both Netlify deploy-preview checks also passed. These were PR checks, not publication, source cleanup or a Production payment launch. That historical revision predates the UPI-first follow-up; consult the latest checks on [draft PR #37](https://github.com/Sunilpa4/diplomaone-app/pull/37) for subsequent revisions rather than treating an older run as validation of new code.

### Follow-up frontend check diagnostics

The validation-record-only **`aa5b008`** run [44722137491 / job 136240289431](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44722137491/job/136240289431) failed its combined frontend step before Java/emulator setup. Backend/package checks, the other three workflows and both previews passed. The API supplied only exit 1; external raw-log retrieval returned EOF, so the specific failed assertion was **not observed** and no production/emulator cause is claimed. Twenty standalone local purchase-UI repeats passed.

The follow-up makes the unit/Chromium steps distinct, removes CPU-dependent fixed-count `setImmediate` waits from the jsdom purchase UI in favor of bounded timer/deadline synchronization, and adds safe fixture-only failure annotations to the purchase UI/browser tests. Those diagnostic changes do not alter production payment code, authorizations, assertions or retries. The subsequent **`aa4981d52a9e71d3389d29564a101d1076dd0e6f`** revision passed [payment run 44723253153 / job 136244104602](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44723253153/job/136244104602), [website run 44723253161](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44723253161), [source/publisher run 44723253172](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44723253172) and [content run 44723253175](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44723253175), plus both Netlify previews, independently verified with the PR checks API. That confirms the post-diagnostics revision, not the exact cause of the older failure or real provider acceptance. The current UPI-first follow-up is a further frontend change and has its own local results above/PR checks; historical green runs are never substituted for its current checks.

## Historical evidence (not current live acceptance)

- Diagnostic revision **d0d185c**: [payment run 44706097903 / job 136185965007](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44706097903/job/136185965007) reported SUCCESS, including the official-emulator/packaged-SDK step verified via the GitHub job API. Its 73-case/44-frontend diagnostic baseline is superseded locally above. The protected manual connection page remains available, but the owner's actual cloud read result was never independently observed.
- Native-gRPC foundation **ffcfcf4**: [payment run 44690340020 / job 136134349439](https://github.com/Sunilpa4/diplomaone-app/actions/runs/44690340020/job/136134349439) passed all 57 then-current real-emulator cases and packaged SDK operations. The earlier REST fallback had failed on the genuine engine (`UNAVAILABLE`, code 14); native gRPC plus an explicit Google universe fixed it. The double was never used as proof that failure was fixed.
- Startup repair **afecd4f**: reproduced the owner's `Cannot find package 'pg'` using the real Netlify packager. Root manifest ownership, NFT and isolated Lambda checks fixed deployment startup. `pg` was later removed for Firestore. The owner confirmed disabled test JSON from a new preview; that response proved startup only, not database/payment readiness.

## Not completed / no claims made

- No agent-operated real Firestore read/write acceptance, private Blobs import, credential/IAM/rules/key change, Netlify environment/account inspection or billing/plan change. Owner-reported database/replacement credentials are not independent verification. Prior exposed-key revocation and Production-only isolation remain owner-private checks.
- No real Google OAuth, independently verified merchant live/KYC/key/UPI/QR acceptance, provider charge/capture/refund/payout, webhook delivery/replay or actual customer delivery acceptance. The owner reports Live/KYC activated and selected Netlify project `sunilpa4` for `diplomaone.in`/`www.diplomaone.in`; Production Live secrets saving/mapping has not been inspected. Offline Checkout doubles and the DEMO emulator cannot prove these.
- No current/public-history solution migration or Drive move/edit/delete. Existing public materials cannot become never-public by hiding links, copying privately or deleting current files.
- No invented support contact, refund eligibility, access duration, legal/tax/invoice promise, ad unit, extra paid service or unlimited free/cost-cap claim. The order budgets do not cap all database reads, bandwidth or invocations.
- No immediate JWT revocation, DRM, screenshot/copy prevention, general DDoS protection or production availability guarantee.

Keep new checkout OFF while these prerequisites remain unresolved. Existing owners' private delivery is deliberately independent of the new-order launch switch.
