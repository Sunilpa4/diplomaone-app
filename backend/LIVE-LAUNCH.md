# Individual-paper live checkout — implemented, NOT launched

The requested flow is **selected paper + agreed price → Google sign-in → server order → Razorpay Checkout → verified full capture → only that UID’s selected paper**. It is no longer a request to finish a separate test-setup walkthrough. Automated offline/CI checks remain required.

## What the code now does

- Prices in INR/paise, derived on the server: Computer **₹19 / 1900**; Mechanical, Electrical and Civil **₹29 / 2900**; Chemical **₹39 / 3900**. No bundle/subscription is created. **All notes, Maths-I `DI01000021` and Applied Physics `DI01000121` stay free.**
- Paid HTML/cards, scoped images and optional PDFs never use the public paper fetch/cache/redirect fallback. The existing sanitizer, expandable Q&A, English/Gujarati/English-only notices, original exam identities, OR labels, fractions, diagrams and image enlargement remain the reader.
- Google ID tokens stay inside the self-hosted Auth adapter. Narrow methods call only fixed relative live endpoints, transiently using `Authorization: Bearer …`. No generic token getter, arbitrary authenticated fetch, client Firestore purchase write, app-managed token/answer storage or browser authorization flag exists.
- My purchases loads actual UID-scoped records, including after reload. Errors are not presented as an empty purchase history. A browser callback is not sufficient: the signature uses the **stored** order ID and the server fetches the canonical order/payment to confirm exact receipt, INR amount, full capture and no refund. A separately signed webhook can fulfill if the customer closes the browser.
- Private bytes are served only after a fresh ownership/asset check, bounded by size/SHA-256, with `private, no-store`, `nosniff` and non-executable HTML. Images/PDFs are authenticated fetches converted to temporary object URLs, revoked on navigation/account change/logout. Authorized readers can still copy or screenshot received content; this is access control, not DRM.
- Same-order duplicate callbacks/webhooks are idempotent. Other accounts/papers/test orders cannot claim live ownership. Uncertain provider-order creation blocks a blind retry and needs receipt-based owner reconciliation. Any provider-confirmed refund disables automated access for that order; this is **not** a published refund-eligibility policy. No capture/refund/payout API is implemented: configure automatic full capture privately in Razorpay.
- Pausing new checkout or removing gateway keys does not remove existing live purchases/private access when the database/private files remain available. Delisting a product blocks new sales but preserves its existing owners’ delivery.

## Selected payment experience — automatic UPI / QR

The owner chose **automatic, gateway-verified UPI/QR**, not a personal UPI ID/static QR with manual approval. The live helper prioritises the standard `upi` method with `config.display.sequence=['upi']`, keeps other enabled **online** payment methods available, hides UPI `collect` and hides cash on delivery. It does not create custom UPI blocks (which could reintroduce hidden instruments), accept customer-entered VPAs/PINs/transaction IDs/screenshots, generate a `upi://` link or expose a QR payment-proof endpoint.

Razorpay manages the payment screen for the **server-created order and exact price**. Its documented Standard Checkout flow uses a UPI app/Intent on supported mobile devices and QR on desktop; mobile QR is account/on-demand dependent. Options depend on merchant enablement, browser/device and provider settings. The bilingual site explains this and warns that the UPI PIN belongs only in the UPI app, never on DiplomaOne. No actual provider QR/app handoff has been accepted by the agent's offline doubles.

The display configuration is **not an authorization rule**. A UPI app return, QR scan, success message, screenshot or typed transaction ID cannot grant ownership. The existing stored-order signature/canonical fully captured payment check and independently signed webhook remain the only fulfillment path. An enabled online fallback method is subject to exactly the same verification. Switching to UPI/QR does not remove the need for Live API keys, private migration, server credentials, approved policies or a reachable webhook; it does not enable charging or promise any fee rate.

Provider references: [Standard Checkout UPI Intent/QR migration](https://razorpay.com/docs/announcements/upi-collect-migration/standard-integration) and [display sequence, preferences and hide behavior](https://razorpay.com/docs/payments/payment-gateway/web-integration/standard/configure-payment-methods/understand-configuration/).

## Isolation and deployment

| | Test | Live |
| --- | --- | --- |
| API | `/api/payments/test/*` | `/api/payments/live/*` |
| Gateway ID | `RAZORPAY_KEY_ID` (`rzp_test_…`) | `RAZORPAY_LIVE_KEY_ID` (`rzp_live_…`) |
| Gateway secret | `RAZORPAY_KEY_SECRET` | `RAZORPAY_LIVE_KEY_SECRET` |
| Webhook secret | `RAZORPAY_WEBHOOK_SECRET` | `RAZORPAY_LIVE_WEBHOOK_SECRET` |
| Firestore root | `diplomaone_test/v1` | `diplomaone_live/v1` |
| Private Blobs store | `diplomaone-private-test` | `diplomaone-private-live` |
| Receipt prefix | `dt_` | `dl_` |

Live never falls back to test keys or test ownership. Every live route, including its webhook, requires Netlify **Production context** and one exact HTTPS origin: `https://www.diplomaone.in` or the existing protected setup site `https://vermillion-pothos-520a34.netlify.app`. Public/branch/deploy-preview/GitHub Pages hosts cannot use live delivery. The apex domain should continue redirecting to `www`; do not move the domain to the setup project.

The function’s native path is now `/api/payments/*`. Both modes are independently cached/validated. Use the Git-connected root `netlify.toml` build (Node 22, root dependencies, `build/netlify-site`, `netlify/functions`). The **12-file frontend ZIP cannot deploy Functions**. Its public output excludes backend files, dependencies, private sources/imports and all secrets. Legacy `/papers/*` redirects expose only the two free codes; every other legacy paper path returns a 404 frontend, not a public-answer redirect.

Keep existing Firebase project `diplomaone-53b4e`, Standard/default Firestore, denied browser access and reviewed least-privilege server IAM. No additional service, plan upgrade or paid provisioning is required/authorized here. Existing Firebase billing is **not a spending cap**. The pilot’s 5 new orders/UID/hour and 50 total/day do not cap all reads, storage, Function invocations, retries or denial-of-service traffic.

## Hard launch switches — leave ALL false now

```dotenv
PAYMENTS_LIVE_ENABLED=false
PAYMENTS_LIVE_PRIVATE_MIGRATION_CONFIRMED=false
PAYMENTS_LIVE_MERCHANT_CONFIRMED=false
PAYMENTS_LIVE_POLICIES_CONFIRMED=false
```

Absent/invalid flags, non-Production context, wrong key mode or missing private credentials cannot enable checkout. Test switches remain separate and false. Live `/config` while OFF performs no product/database/provider/storage query. Authenticated existing owners may still load their purchases/content. Turning flags on is an **owner assertion of completed external work**, not something these switches verify automatically; do not use them to bypass the missing work below.

The owner identified **`sunilpa4`** as the existing Production Netlify project for **`diplomaone.in` / `www.diplomaone.in`**; this mapping has not been independently inspected. Put real live secrets directly into that project’s private **Production-only** environment, never chat, Git, Drive, static assets or screenshots. Do not use all-context values or preview/branch overrides. Use Functions-only scope when available without upgrading; on Free, all scopes also expose these values to trusted Production builds. The allowlisted builder does not substitute/export environment values, but that is not build-time secret isolation. The older exposed Admin key must be revoked privately; replacing a Netlify value does not revoke it.

## Public-to-private migration is still a real blocker

The current app checkout still retains previously public paper/source bytes. **They have NOT been made private by this change.** The public content repository, historical commits, release archives, CDN caches, forks and downloaded copies need separate review. Removing current public files cannot turn these historical materials into never-public content. No Git history rewrite, Drive mutation or destructive cleanup is done automatically.

The normal solved-paper publisher now copies **only the two free subjects plus tiny `{version, private, id}` listing JSON**. It can never copy new paid HTML/PDF/images, even if an HTML replacement manifest is supplied. The two notes publishers remain in place and stage only `data/`; the website publisher stages frontend/app files, not paper sources. Existing public paid copies are deliberately not silently deleted before a verified private backup/import.

### Offline preparation (no credentials/network/cloud writes)

`backend/paper-products.json` maps the currently supplied **54 priced subject codes** to their actual subject directory/explicit reviewed legacy relation, not a code-prefix/Drive-folder guess. New/ambiguous subjects require review. Source filenames determine the real sessions; no sessions or translations are invented.

```sh
npm ci --include=dev --ignore-scripts --no-fund
npm run prepare:live-papers
# Default is a validating, NO-WRITE dry run. Current sources: 76 paid papers,
# 3,380 assets, 169,975,648 bytes; the four free exam sets are excluded.
npm run prepare:live-papers -- --write --out=build/private-live-import
```

The write option creates owner-private/ignored output (0700 directories/0600 files) only below `build/`, refusing an existing output. Each `<productId>/paper.json` is self-contained and validated by the same strict importer. `migration.json` pins every exported byte/hash and explicitly says **privateImportApplied=false**. `public-metadata/papers/` is the only subdirectory suitable for a public content checkout; it contains no answers. Protect/back up the private export outside Git. `--without-pdfs` explicitly omits optional PDFs if needed; it never drops question cards/diagrams. No private export is attached or committed.

### Owner-only import (a real cloud write; NOT executed by the agent)

Use the private environment on the owner’s trusted machine, targeting **the same Netlify site that will serve live purchases**. Blobs are site-scoped; importing into the protected setup site does not import into the site serving `www`. Required server Firestore credentials are the existing project’s paired `FIREBASE_CLIENT_EMAIL`/complete `FIREBASE_PRIVATE_KEY`, plus private `NETLIFY_SITE_ID`/`NETLIFY_AUTH_TOKEN` for owner-operated Blobs upload. Never send these here.

```sh
# Dry run first; default importer mode is still TEST, so live must be explicit.
npm run import:paper -- build/private-live-import/DI03000161--summer-2026/paper.json --mode=live
# ONLY in an owner-private environment, after approving this billable import:
PAYMENTS_LIVE_IMPORT_CONFIRMED=true npm run import:paper -- build/private-live-import/DI03000161--summer-2026/paper.json --mode=live --apply
```

Upload plus strong-read/hash verification of **all** files finishes before the product is activated in `diplomaone_live/v1/products`. Test records are never copied. Existing product IDs refuse replacement; do not delete purchase/product records or relabel a different exam to force an update. Import each reviewed paper you actually intend to sell (the owner says two or three real sessions/subject is sufficient), keeping launch switches OFF. No runtime bootstrap seeds content or purchases.

After verifying private bytes/products and keeping an owner-private backup, remove **current paid sources** from both the public app repository (`papers-upload/papers` **and** `papers-upload/originals`) and the public content repository (`papers/<paid-code>/…` HTML/images/PDFs). Preserve free papers/notes, original exam codes and listing metadata; check alternative previews/archives/releases/other publishing paths. This cleanup needs an explicit reviewed source migration, not a blanket deletion or moving files around Drive. Do not claim public Git history has been secured.

Audit local checkouts without changing them:

```sh
npm run audit:public-papers -- . /PRIVATE/public-content-checkout --report=build/private-public-audit.json
# exit 2 = public files remain, exit 1 = audit failed, exit 0 = known current
# paper/source surfaces clean. Reports are owner-private; no deletion/network.
```

The audit scans known current paper/source directories; it cannot certify all history, releases, caches, semantic content hidden in other files or third-party copies. **This app checkout currently fails it (3,418 files require migration).** Keep the migration switch false. A clean frontend ZIP or hiding links is not evidence that the sources are private.

## Merchant, policy and controlled delivery acceptance — owner decisions pending

The owner **reports that Razorpay Live/KYC is activated**. This is not independent provider acceptance; saved Production Live keys, automatic capture, merchant UPI/QR enablement and a reachable verified webhook remain unconfirmed. Merchant support/refund/access decisions have not been supplied. None of these can be inferred from the test key or a successful build.

Before opening sales:

1. Confirm privately that Razorpay live payments/settlement and automatic full capture are enabled. Configure a distinct live webhook secret and `payment.captured` / `refund.processed` events at **`https://www.diplomaone.in/api/payments/live/webhook`** on the actual API deployment. The public production endpoint must be reachable by Razorpay and authenticate its raw HMAC; it must not require Firebase login. Keep the protected setup site’s Netlify Team protection intact—provider webhooks cannot pass that interactive hosting gate.
2. Publish owner-approved merchant/contact/support details, refund/cancellation rules, access duration/delivery terms and privacy information at `#/purchase-info` (currently an honest **sales not open** notice, not fabricated legal terms). Review any tax/invoice/consumer requirements privately. Do not mark policies confirmed while the placeholder is present.
3. Confirm the new server identity/IAM, exposed-key revocation, private source cleanup, private assets and Production-only credentials. Keep preview/branch secrets absent. Do not weaken Firestore browser rules or move/change the public domain for a shortcut.
4. After the preceding migration/merchant/policy prerequisites, set **`PAYMENTS_LIVE_PILOT_UIDS`** privately to the owner’s approved Google Firebase UID (up to 10 pilot UIDs), then explicitly activate the four live flags and redeploy for a **restricted soft launch**. A malformed nonempty pilot list fails closed. Only those UIDs can create new orders; purchases/late webhooks for existing owners are never cut off by this list. The list is not returned publicly. Complete one real selected-paper purchase and verify actual capture, webhook delivery/replay, reload/My purchases, the correct Google UID and a second account/paper denial. Verify mobile UPI Intent opens a supported installed payment app and desktop Checkout QR is tied to that order/amount; cancellation/expiry must not unlock. A completed UPI payment must unlock only after server verification, including signed-webhook recovery if the tab is closed. Confirm merchant UPI/QR availability; do not advertise mobile QR unless enabled. Never use an uninformed customer as the first delivery check. No real charge/refund/capture was initiated by the agent.
5. Only after controlled acceptance, open sales by removing the optional pilot restriction and redeploying the chosen Production project with the four reviewed live flags. Pause new sales with `PAYMENTS_LIVE_ENABLED=false` if needed, retaining credentials/private delivery for existing customers and late webhook fulfillment.

No owner/cloud/provider acceptance is claimed by the offline tests, official DEMO emulator, build previews or packaging checks. See [VALIDATION.md](VALIDATION.md) for executed results and limits.
