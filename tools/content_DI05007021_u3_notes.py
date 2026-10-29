"""English-only public-key/RSA/PKI syllabus coverage with scoped real evidence."""
from subject_DI05007021 import tr
from content_DI05007021_u1_notes import ul,table,topic
SOURCES=[
 ('GTU DI05007021 syllabus, 2026–27','https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI05007021.pdf'),
 ('RFC 8017: RSA primitives, OAEP and PSS','https://www.rfc-editor.org/rfc/rfc8017.html'),
 ('RFC 5280: X.509 certificates, trust paths and CRLs','https://www.rfc-editor.org/rfc/rfc5280.html'),
 ('NIST FIPS 186-5: Digital Signature Standard','https://csrc.nist.gov/pubs/fips/186-5/final'),
 ('RFC 8446: TLS 1.3, including no RSA key transport','https://www.rfc-editor.org/rfc/rfc8446.html'),
 ('OpenSSL 3.5 pkeyutl: asymmetric operations','https://docs.openssl.org/3.5/man1/openssl-pkeyutl/'),
 ('OpenSSL 3.5 dgst: signatures and verification','https://docs.openssl.org/3.5/man1/openssl-dgst/'),
 ('OpenSSL 3.5 req: CSR signatures','https://docs.openssl.org/3.5/man1/openssl-req/'),
 ('OpenSSL 3.5 verify: certificate verification','https://docs.openssl.org/3.5/man1/openssl-verify/'),
 ('OpenSSL 3.5 verification options: trust/purpose/time','https://docs.openssl.org/3.5/man1/openssl-verification-options/'),
 ('OpenSSL 3.5 ca: local issuance and CRLs','https://docs.openssl.org/3.5/man1/openssl-ca/')]
NOTES=[
 {'title':tr('1. Public-Key Principles and Applications'),'items':[
  topic('1.1 Public and private keys: different roles, related mathematics',
   '<p>A <b>public-key / asymmetric cryptosystem</b> uses a mathematically related key pair. The public key may be distributed; the corresponding private key must remain protected. Knowing a public key should not make deriving the private key computationally feasible under the scheme’s assumptions.</p>'+ul(
    '<b>Encryption:</b> protect information for a recipient using the recipient’s authentic public encryption key; the corresponding private key performs the intended decryption.',
    '<b>Signature:</b> a signer uses a private signing key; others verify with the authentic public verification key. This is a different operation and security goal from encryption.',
    'Not every public-key algorithm supports every operation. Encryption, signatures and key agreement have distinct schemes and requirements.',
    'A publicly available key is not automatically an authentic key. An attacker’s key with someone else’s name does not become trustworthy just because the mathematics works.') , 'sec3_keys'),
  topic('1.2 Applications and the hybrid approach',
   table(['Application','Public-key role','Important limit'],[
    ('Confidential exchange','Use an appropriate encryption/key-establishment scheme.','Authenticate the recipient key; encryption alone does not identify the sender.'),
    ('Digital signatures','Check integrity and origin evidence under a trusted verification key.','Protect the signing key and establish what identity it represents.'),
    ('PKI / certificates','Bind a public key to an identity/attributes under an issuer’s policy.','Trust anchors and validation rules must be established independently.'),
    ('Hybrid systems','Use public-key methods to establish/authenticate key material and symmetric authenticated encryption for bulk data.','Do not directly RSA-encrypt a large file or invent a complete protocol from classroom formulas.')])+
   '<p>Hybrid is a design idea, not a claim that every protocol transports a key with RSA. <b>TLS 1.3 does not use RSA key transport</b>; RSA signatures can still be relevant to authentication. No live TLS handshake or bulk-encryption protocol is implemented in this unit.</p>','sec3_hybrid'),
  topic('1.3 Symmetric versus asymmetric protection',
   table(['Aspect','Symmetric','Asymmetric'],[
    ('Key relationship','Shared secret material.','Public/private pair with different roles.'),
    ('Distribution challenge','Arrange protected shared-secret distribution.','Distribute authentic public keys while protecting private keys.'),
    ('Typical use','Efficient authenticated bulk encryption with an appropriate scheme.','Key establishment, signatures and other small-data public-key operations.'),
    ('Identity issue','Shared-secret holders may generate the same MAC.','A signature can be publicly checked, but only under a properly trusted identity/key binding.')])+
   '<p>Key lengths from different algorithm families are not comparable bit-for-bit: “RSA 2048 bits” does not mean 2048 bits of security. Neither family automatically solves endpoint compromise, authorization, replay or availability. Follow current requirements and vetted protocols in real systems; this course does not promise future or post-quantum security.</p>')]},
 {'title':tr('2. RSA Algorithm, Computation and Security'),'items':[
  topic('2.1 RSA key generation in the two-prime classroom model',
   '<ol><li>Choose distinct suitable primes p and q. Real generation needs secure, vetted procedures; the published small primes here are only teaching data.</li><li>Compute <code>n=p×q</code> and <code>phi(n)=(p−1)(q−1)</code>.</li><li>Select e with <code>1&lt;e&lt;phi(n)</code> and <code>gcd(e,phi(n))=1</code>.</li><li>Compute the modular inverse <code>d=e^-1 mod phi(n)</code>.</li><li>Public key: (n,e). The private material includes d and ordinarily the factors/CRT information; keep real private material secret.</li></ol>'+
   '<p><b>Worked key:</b> p=61, q=53, n=3233, phi=60×52=3120. Choose e=17; d=2753 because 17×2753=46801=1+15×3120.</p><p>e need not be prime merely to satisfy this classroom arithmetic condition; coprimality is the requirement. Real key-generation policies impose additional rules. RFC 8017 states the inverse relation modulo lambda(n); choosing an inverse modulo phi(n) here is sufficient because lambda(n) divides phi(n). This example’s lambda(n)=780.</p>','sec3_keygen'),
  topic('2.2 RSA encryption/decryption and representative bounds',
   '<p>For a valid numeric representative <code>0≤m&lt;n</code>, textbook RSA uses <code>c=m^e mod n</code> and <code>m=c^d mod n</code>. The ciphertext representative also lies from 0 through n−1.</p>'+table(['Step','Actual classroom result'],[
    ('Key material','n=3233, e=17, public demo d=2753'),
    ('Encrypt m=65','65^17 mod 3233 = 2790'),
    ('Decrypt c=2790','2790^2753 mod 3233 = 65')])+
   '<p>Here 65 is a numeric representative, not the A=0 letter convention from Unit 2. Real byte messages need a defined encoding/padding scheme; arbitrary text cannot simply be treated as one unlimited integer. The helper rejects negative or out-of-range representatives. Correct two-prime RSA works for all representatives in range, not only those coprime to n; the general justification uses the Chinese remainder structure.</p>','sec3_rsa',programs=['sec3p01']),
  topic('2.3 Computational aspect: modular exponentiation',
   '<p>Do not first construct a huge full power and only then reduce it. <b>Square-and-multiply</b> repeatedly squares/reduces and multiplies selected powers according to the exponent bits.</p>'+table(['Power','Value modulo 3233'],[
    ('65^1','65'),('65^2','992'),('65^4','1232'),('65^8','1547'),('65^16','789')])+
   '<p>17=16+1, so <code>65^17 mod 3233 = 789×65 mod 3233 = 2790</code>. The program processes five exponent-bit positions. The number of such modular operations grows with the exponent’s bit length; this is not a speed benchmark and does not make our Python helper constant-time.</p>'+ul(
    'Large real operands still require efficient arithmetic and protected implementations.',
    'CRT can speed private operations using factor-related values, but the private factors/CRT parameters must be protected; this unit does not implement a hardened CRT engine.',
    'Side channels, randomness, padding, key handling and protocol behaviour matter beyond the modular-power formula.') ,programs=['sec3p02']),
  topic('2.4 RSA security: assumptions, raw-RSA weaknesses and key handling',
   '<p>Factoring the public modulus into its secret prime factors enables recovery of private information. This does not mean every possible RSA attack is proven equivalent to factoring. Small parameters, weak generation, implementation flaws and unsafe protocols can fail for other reasons.</p>'+ul(
    '<b>Raw RSA is deterministic:</b> the same representative and public key give the same ciphertext.',
    '<b>Raw RSA has algebraic structure:</b> multiplying two ciphertexts modulo n corresponds to multiplying their plaintext representatives modulo n. The fixed tiny example demonstrates this; it is not a live-system attack.',
    'Anyone with the public encryption key can encrypt; a ciphertext is not proof of sender identity.',
    'Protect real private keys with appropriate storage/access controls, vetted generation and lifecycle procedures. Do not reuse toy parameters, log private factors or copy a lab CA into an operating-system trust store.',
    'RSA is not post-quantum protection. Required algorithms and sizes depend on policy, lifetime and the current threat model; the 2048-bit lab setting is not a guarantee for every real use.') ,programs=['sec3p03']),
  topic('2.5 Real encryption profile: RSA-OAEP with SHA-256',
   '<p>The supporting lab uses actual OpenSSL RSA-OAEP with SHA-256 and MGF1-SHA-256, a fresh 2048-bit key and an empty default OAEP label. It does not use raw pow-based RSA for those byte messages.</p><p>OAEP’s message limit is <code>mLen≤k−2×hLen−2</code>, where k is the modulus byte length and hLen the hash output byte length. Here k=256 and hLen=32, giving <b>190 bytes</b>, not 190 characters in every encoding.</p>'+ul(
    'The actual example yields 256-byte ciphertexts, recovers the message and observes different randomized ciphertexts for two encryptions of the same message.',
    'A 191-byte message is actually rejected, and a modified ciphertext fails decryption. Failures are not exposed through a public decryption service or claimed as an oracle-resistant protocol.',
    'OAEP alone does not authenticate a sender or establish public-key ownership. Use a complete appropriate authenticated protocol for real applications.',
    'Private keys and random ciphertext bytes are not included in expected outputs or the practical kit.') ,programs=['sec3p04'])]},
 {'title':tr('3. Digital Signatures'),'items':[
  topic('3.1 Signing and verification are not private-key encryption',
   '<p>A <b>digital signature</b> is generated with a private signing key and checked against the exact message using the corresponding authentic public verification key. Suitable schemes use defined hashing/encoding steps; do not describe a modern signature as simply “encrypting the message with the private key.”</p>'+ul(
    'The actual file-message example uses <b>RSA-PSS with SHA-256</b> and digest-length salt.',
    'Original data verifies; modified data and a different public key do not. The RSA 2048 signature here is 256 bytes, not a separate encrypted copy of the document.',
    'The signed message is not thereby confidential. Its contents can still be visible to anyone who receives it.',
    'A document signature profile and the signature format on an X.509 certificate are not necessarily identical; our certificate-issuing commands use their explicit OpenSSL certificate profile.') ,'sec3_signature',programs=['sec3p05']),
  topic('3.2 Integrity, origin evidence and non-repudiation assumptions',
   '<p>Signatures can support detection of alteration and evidence of origin under the right trust assumptions. Non-repudiation also depends on identity binding, private-key control, evidence handling, time context and the applicable process.</p>'+ul(
    'A valid signature is not proof that a statement is true, that a particular human operated the device, or that a specific legal outcome follows.',
    'A compromised or wrongly attributed private key can defeat the intended interpretation of a signature.',
    'A valid old signed message can be replayed; applications need appropriate freshness/context checks.',
    '<b>Contrast with HMAC:</b> both shared-secret holders can create tags, so HMAC is not public proof against the other holder. A public signature has a different verification model, not an automatic identity guarantee.') )]},
 {'title':tr('4. PKI, Certificates and Enrollment'),'items':[
  topic('4.1 What a digital certificate contains—and does not contain',
   '<p>A <b>digital certificate</b> is a signed data structure associating a public key with a subject and attributes under an issuer’s policy. X.509 is a widely used certificate format; PKI includes the policies, entities, keys, issuance and status processes around it.</p>'+table(['Field / extension','Purpose'],[
    ('Subject and relevant identity names','Identify the subject/claimed identity; TLS host matching normally uses the appropriate SAN names.'),
    ('Subject public key information','The public algorithm/key, not the subject’s private key.'),
    ('Issuer and serial number','Identify the issuer and an issuer-scoped certificate identifier.'),
    ('Validity: notBefore / notAfter','The certificate’s time interval; a trustworthy evaluation clock is needed.'),
    ('Basic constraints, key usage and extended key usage','State CA status and permitted/intended uses under validation rules.'),
    ('Issuer signature','Allows verification that the signed certificate data matches the issuer’s signing operation under the issuer key/trust assumptions.')])+
   '<p>A certificate is not an encrypted container for a private key and not a guarantee that a website is harmless. Inspecting its printed name or signature field is not full validation. PEM and DER are encodings, not proof of authenticity.</p>','sec3_certificate'),
  topic('4.2 CA, RA, trust anchors and intermediate issuers',
   '<p>A <b>certificate authority (CA)</b> issues/signs certificates under its policy and manages relevant status information. A <b>registration authority (RA)</b> handles delegated registration/identity checks and approves or forwards requests. The roles may be integrated; they are not necessarily separate companies.</p>'+ul(
    'A root trust anchor is accepted through a trusted configuration/policy, not merely because its certificate is self-signed.',
    'An intermediate CA can issue within constraints granted by its issuer. An ordinary end-entity certificate is not automatically entitled to issue more certificates.',
    'The relying party needs an authentic trust anchor and a valid certification path. Matching an issuer name alone does not verify the issuer signature or its authority.',
    'The local example explicitly supplies an owned lab root and intermediate to OpenSSL. No browser/OS root store is modified, and the fictitious .test names are not publicly enrolled.') ,'sec3_chain'),
  topic('4.3 Steps for obtaining a certificate',
   '<ol><li>Choose the intended use, identity names and applicable CA/organizational policy.</li><li>Generate and protect the key pair using an appropriate trusted implementation; normally retain the private key locally.</li><li>Create a signed CSR carrying the public key and requested subject/attributes.</li><li>The RA/CA performs the required identity/control/authorization checks; verifying the CSR signature alone is insufficient.</li><li>The CA applies its issuance policy and signs an appropriate certificate.</li><li>Check the issued certificate, install it and the required intermediate chain for the application, while protecting the private key.</li><li>Plan renewal, revocation/status handling and key replacement when required.</li></ol>'+
   '<p><b>Actual CSR example:</b> a generated request’s signature validates; a signature-byte modification fails. This demonstrates proof related to key possession, not a real identity investigation, domain-control validation or approval by a public CA. Our local issuing helper is a disposable teaching fixture, not a production enrollment service.</p>','sec3_enrollment',programs=['sec3p06'])]},
 {'title':tr('5. Verification and Safe Practical 6'),'items':[
  topic('5.1 Verify authenticity and integrity using an explicit profile',
   '<p>Validation is a set of checks under an intended use, not just a successful signature calculation:</p><ol><li>Start from an independently trusted anchor and build the required chain.</li><li>Verify issuer signatures and CA/constraint rules, including relevant critical extensions.</li><li>Check the validity interval at a trustworthy evaluation time.</li><li>Match the intended identity—for this lab, SAN hostname portal.diploma.test.</li><li>Check key usage/extended key usage and the application purpose.</li><li>Apply the required current revocation/status policy using appropriate trusted status information.</li><li>In an actual protocol, also perform its proof-of-possession, handshake and application checks; an offline certificate check does not substitute for them.</li></ol>'+
   '<p>The executed profile explicitly supplies the lab root/intermediate, disables default CA path/store lookup, uses strict X.509 checks and checks server purpose/hostname. It actually rejects a wrong hostname, wrong purpose, missing intermediate, an expired evaluation time and an unrelated trust root. Another example detects an altered certificate signature. No insecure “ignore errors” or time-bypass fix is taught.</p>','sec3_validation',programs=['sec3p07','sec3p08','sec3p10']),
  topic('5.2 Revocation is distinct from expiry and ordinary path validity',
   '<p>A certificate may be revoked before its expiry, for example after suspected private-key compromise or a policy/identity change. A CA-signed <b>CRL</b> lists relevant revoked serials; its issuer/signature and freshness also matter. OCSP is another status mechanism, not performed in this lab.</p>'+table(['Actual observation','Meaning'],[
    ('Before revocation, supplied leaf CRL check succeeds.','The leaf is acceptable under that particular current local status/profile.'),
    ('After local revocation and a new CRL, error 23 rejects the leaf.','The explicit leaf status check detected revocation.'),
    ('Ordinary path checking without CRL still succeeds.','A valid path alone is not a revocation-status assertion.')])+
   '<p><b>Scope limit:</b> the demonstration checks the leaf only against a locally supplied CRL. It does not check full-chain revocation, perform live CRL/OCSP download, install trust roots, or contact a public CA. Real clients apply their own required status policy; do not silently disable validation when status or chain construction fails.</p>','sec3_revocation',programs=['sec3p09']),
  topic('5.3 Practical 6 journal, secure boundaries and assessment',
   '<p><b>Official Practical 6:</b> implement RSA asymmetric-key encryption in an allowed language. The pure-Python arithmetic example supplies the small-number key calculation, encryption and decryption. The remaining examples are clearly supporting RSA/PKI study, not invented additional official practical numbers.</p>'+ul(
    'Record p,q,n,phi,e,d,m,c and the recovered representative only for <b>public small-number teaching data</b>; never publish real private keys or factors.',
    'The kit includes rsa_math.py and pki_lab.py beside all ten scripts. Python’s standard library plus OpenSSL 3 CLI are required; no pip package is needed. Reference execution is on Linux, not a claimed Windows GUI/browser certificate workflow.',
    'Real demo RSA keys are fresh 2048-bit keys in mode 0600 files under a mode 0700 temporary directory, deleted at context exit. Their unencrypted temporary PEM form is a bounded lab convenience, not a recommendation for persistent production key storage.',
    'No real identities, public CA enrollment, external network service, TLS handshake, OS trust installation or FIPS certification is claimed. All shown .test identities and documents are fictional.',
    'The official course scheme remains 70+30 theory and 20+30 practical=150. Unit 3 is 10 hours/25% syllabus weight, not a guaranteed question allocation. The sixteen answered revision questions have suggested 3/4/7-mark sizes only; they are not official GTU papers or predictions.')+
   '<p><b>References:</b> '+', '.join('<a href="'+u+'">'+n+'</a>' for n,u in SOURCES)+'. Explanations and classroom questions are original; standards are cited for scheme/validation concepts, not as certification of this code.</p>')]}]

PRACTICE=[
 ('Explain public/private key roles for encryption and signatures.',4,
  '<p>Encryption for a recipient uses the recipient’s authentic public encryption key; corresponding private material performs decryption. Signing uses a private signing key and verification uses the authentic public verification key. These are distinct schemes/goals, not interchangeable directions of one secure “encryption” operation. Public keys need authentic identity binding; private keys need protection. Not every public-key algorithm supports every operation.</p>'),
 ('Describe three applications of public-key cryptography and the hybrid approach.',4,
  '<p>Examples are appropriate key establishment/encryption, digital signatures and PKI identity-to-key binding. A hybrid design uses public-key methods to establish/authenticate material and appropriate symmetric authenticated encryption for bulk data. Do not RSA-encrypt an unrestricted file directly. TLS 1.3 is not an RSA key-transport protocol, even though RSA signatures can be relevant to authentication. A conceptual hybrid diagram is not a tested complete protocol.</p>'),
 ('Compare symmetric and asymmetric methods without claiming automatic identity protection.',4,
  '<p>Symmetric systems use shared secret material and are typically appropriate for efficient authenticated bulk processing under the right scheme. Asymmetric systems use public/private pairs for operations such as signatures and key establishment. Symmetric distribution must protect shared secrets; asymmetric distribution must authenticate public keys and protect private keys. Neither solves compromised endpoints, authorization or replay automatically, and key-size numbers from different families are not directly equivalent security strengths.</p>'),
 ('Generate the textbook RSA key for p61, q53 and e17.',7,
  '<p>n=61×53=3233; phi=(61−1)(53−1)=60×52=3120. gcd(17,3120)=1. The inverse d=2753 because 17×2753=46801=1+15×3120, so ed≡1 modulo phi. Public data is(n,e)=(3233,17); d and normally factors/CRT data form private material in a real system. Here all values are published toy data and grossly too small for protection. lambda=lcm(60,52)=780; the phi-based inverse is also a valid lambda-based inverse relation.</p>'),
 ('Encrypt representative65 and decrypt2790 using the worked RSA key.',4,
  '<p>For 0≤m&lt;3233, c=m^17 mod 3233. With m=65, c=2790. Decrypt m=2790^2753 mod 3233=65. Both message and ciphertext are numeric representatives within range; this is not a general text encoding or secure padding scheme. Reject representatives outside0 through 3232. Correct two-prime RSA works for all representatives in range, not only values coprime to n. Real protection requires appropriate standardized schemes and protected implementations.</p>'),
 ('Use modular exponentiation to explain65^17 mod 3233.',7,
  '<p>Repeated squaring yields 65^1=65,65^2=992,65^4=1232,65^8=1547 and65^16=789 modulo 3233. Since 17=16+1, multiply 789×65 and reduce modulo 3233 to obtain 2790. The square-and-multiply program processes five exponent bits and reduces intermediate products. The operation count relates to exponent bit length; it does not construct the whole integer power first. This teaching code is not constant-time or a performance benchmark.</p>'),
 ('Explain why raw RSA is not secure encryption and why key size alone is insufficient.',7,
  '<p>Raw RSA is deterministic and has a multiplicative algebraic relation, so the modular-power formula alone is not an appropriate message-encryption scheme. Factoring n is enough to recover private information, but not every RSA failure is proven equivalent to factoring; weak randomness, padding, side channels, key storage and protocol errors also matter. Anyone with the public encryption key can encrypt, so ciphertext is not sender authentication. Use vetted current schemes/protocols; toy parameters and a lab2048-bit setting are not universal or future-security guarantees.</p>'),
 ('Derive the 2048-bit RSA-OAEP/SHA-256 message limit and interpret the lab.',4,
  '<p>RFC8017 gives mLen≤k−2hLen−2. Here k=2048/8=256 bytes and SHA-256 hLen=32, so the limit is 256−64−2=190 bytes. The actual lab yields 256-byte ciphertexts, recovers the message, sees differing randomized ciphertexts, rejects 191 bytes and rejects a modified ciphertext. Bytes are not necessarily characters. OAEP is not sender authentication or a full secure messaging protocol, and no public decryption endpoint is exposed.</p>'),
 ('Explain digital-signature generation/verification and the RSA-PSS example.',7,
  '<p>A signing scheme uses a private signing key; verification checks the exact message with the corresponding authentic public key using the specified hashing/encoding rules. The actual example uses RSA-PSS/SHA-256 with digest-length salt and a fresh 2048-bit key. Original data verifies; changed data and a wrong key fail. A signature is not “private-key encryption” and does not hide message contents. Trust, private-key control, identity binding and context are necessary before interpreting the result.</p>'),
 ('State what a valid digital signature does not prove.',3,
  '<p>It does not automatically prove that a statement is true, that a particular human operated a device, that a legal outcome follows, or that an old signed message is fresh. A compromised/misattributed signing key weakens origin evidence. Applications need identity/key trust and appropriate freshness/context handling. Shared-secret HMAC has a different model because either holder can create a tag and it is not public proof against the other holder.</p>'),
 ('Explain important X.509 certificate fields and why the private key is absent.',4,
  '<p>Fields include subject/relevant identity names, subject public-key information, issuer, issuer-scoped serial number, validity interval, applicable basic constraints and key-usage/EKU extensions, and the issuer signature. The public key is distributed; the private key must remain separately protected. The certificate is not an encrypted private-key container or a guarantee that a website is harmless. Parsing fields alone is not chain/identity/purpose/status validation.</p>'),
 ('Differentiate CA, RA and trust anchor with an intermediate chain.',4,
  '<p>The CA issues/signs certificates and manages relevant status under its policy. An RA handles delegated registration/identity checks; the roles can be combined. A trust anchor is accepted through trusted configuration, not merely self-signature. A constrained intermediate signed by a trusted root may issue an end-entity certificate according to its authority. Chain validation checks signatures and constraints, not just matching issuer names. Our lab root is explicitly supplied only to the lab verifier, not installed in an OS/browser.</p>'),
 ('Describe the steps to obtain a certificate and the limit of a valid CSR signature.',7,
  '<p>Select intended identity/use/policy; generate/protect the key; create a signed CSR with public key and requested attributes; complete required RA/CA identity/control/authorization checks; obtain the policy-conforming CA-signed certificate; check/install the certificate and intermediate chain while protecting the private key; plan renewal and revocation. A valid CSR signature relates to possession of its key, not proof that the requester owns the claimed identity. The actual tampered-CSR rejection does not replace real RA vetting or public CA approval.</p>'),
 ('Give a checklist for certificate authenticity/integrity validation.',7,
  '<p>Use an independently trusted anchor, build the chain, verify issuer signatures and CA/critical-extension constraints, evaluate validity at a trustworthy time, match intended identity such as the appropriate SAN hostname, check usage/EKU and application purpose, and apply the required current status/revocation policy. Actual protocols need their own handshake/possession/application checks too. A printed name or one good signature is insufficient. Do not accept arbitrary downloaded roots or bypass failed checks.</p>'),
 ('Interpret the five negative certificate tests and the modified-signature test.',4,
  '<p>The correct explicit lab profile succeeds. A wrong hostname fails with error 62, wrong purpose with 26, missing intermediate or unrelated root with 20, and expiry at the explicit evaluation time with 10. Modifying a certificate signature produces error 7 under the correct chain. These are actual OpenSSL observations, not merely arbitrary command failures. They are reference codes for this tested version/profile; an offline profile does not claim a live TLS/browser handshake or complete PKIX conformance testing.</p>'),
 ('Explain why an ordinary valid chain is not evidence of non-revocation.',4,
  '<p>A certificate can be revoked before expiry. The local lab issues a CRL, verifies before revocation, revokes the leaf, generates a new CRL and observes error 23 under an explicit leaf CRL check. Plain path verification without that check still succeeds, so path validity is not a status assertion. Verify trusted status data/signatures and required freshness under policy. This demonstration checks only the leaf against a supplied local CRL; full-chain revocation, OCSP and live CRL fetching are not performed.</p>')]
EXAM=[{'q':tr('Practice: '+q),'marks':m} for q,m,a in PRACTICE]
ANSWERED={'title':tr('6. Answered Exam-Style Practice — Suggested Marks Only'),'role':'practice',
 'items':[topic(f'Practice {i}. {q}',a) for i,(q,m,a) in enumerate(PRACTICE,1)]}
CARDS=[
 ('Public-key roles','Encrypt: recipient public -> private decrypt\nSign: signer private -> public verify','Different schemes/goals; public-key authenticity still matters.'),
 ('RSA toy key','n=p*q; phi=(p-1)*(q-1)\ngcd(e,phi)=1; d=e^-1 mod phi','Distinct suitable primes. Real generation and key policy are not implemented by small-number trial division.'),
 ('Worked classroom key','p61, q53 -> n3233, phi3120\ne17 -> public demo d2753','All values are public teaching data, not secure key material.'),
 ('Representative bounds','0 <= m < n; 0 <= c < n\nc=pow(m,e,n); m=pow(c,d,n)','Raw arithmetic is not a standardized padded message-encryption scheme.'),
 ('Fast exponentiation','65,992,1232,1547,789 mod 3233\n17=16+1 -> 789*65 mod 3233=2790','Reduce repeatedly; the teaching helper is not constant-time production code.'),
 ('OAEP size bound','mLen <= k - 2*hLen - 2\nRSA 2048/SHA256 -> 256-64-2=190 bytes','Explicit SHA-256 and MGF1-SHA-256. Bytes are not always characters.'),
 ('PSS signature','RSA-PSS + SHA-256\nDigest-length salt in this lab','A signature is not private-key encryption, confidentiality or an automatic legal/human-identity guarantee.'),
 ('Certificate fields','Identity + public key + issuer/serial\nValidity + constraints/usage + issuer signature','No subject private key is part of the certificate.'),
 ('CA versus RA','CA: policy-based issuance/status\nRA: delegated registration/identity checks','The roles may be integrated. CSR signature checking alone is not identity vetting.'),
 ('Enrollment sequence','Key -> signed CSR -> identity/policy checks\n-> CA issuance -> installation/lifecycle','Keep private material protected; no public enrollment occurs in this lab.'),
 ('Validation profile','Trust/path -> signatures/constraints\n-> dates -> identity -> purpose -> status','Do not bypass errors. Offline certificate checks do not prove a live TLS handshake.'),
 ('Actual negative reference codes','Hostname62; purpose26; issuer20\nExpiry10; signature7; revoked23','Observed OpenSSL 3.5.7 outcomes for these specific fixtures, not universal output wording.'),
 ('Revocation scope','Leaf CRL check != all-chain status\nPlain valid path != not revoked','Only an explicitly supplied local leaf CRL is checked here; no OCSP/download.'),
 ('Temporary lab boundary','Fresh RSA 2048; .test names only\nPrivate files 0600; directory 0700; cleanup','No trust-store installation, public CA, real identity vetting, production CA or FIPS certification.')]
SYNTAX=[{'title':tr('RSA and PKI Quick Reference'),'items':[{'name':tr(n),'f':f,'terms':tr(t)} for n,f,t in CARDS]}]
QA=[
 ('What is a public-key cryptosystem?','A system using mathematically related public/private keys for specified asymmetric operations.'),
 ('Is a public key automatically authentic?','No. Its identity binding must be established through an appropriate trusted process.'),
 ('Whose public key encrypts for a recipient?','The recipient’s authentic public encryption key; the corresponding private key decrypts under the scheme.'),
 ('Does any public-key algorithm support encryption and signatures?','No. Algorithms and schemes have different supported operations and requirements.'),
 ('Why use hybrid designs?','Public-key methods establish/authenticate material, while appropriate symmetric authenticated encryption handles bulk data efficiently.'),
 ('Does TLS 1.3 use RSA key transport?','No. RSA signatures may be relevant to authentication, but TLS 1.3 does not use RSA key transport.'),
 ('What are n and phi in two-prime RSA?','n=p×q and phi=(p−1)(q−1) for distinct primes.'),
 ('What condition must classroom e satisfy?','1&lt;e&lt;phi and gcd(e,phi)=1; primality of e alone is not the condition.'),
 ('What is d in the phi-based classroom model?','The modular inverse e^-1 modulo phi.'),
 ('What is the worked key’s n,phi,e,d?','3233,3120,17,2753, all published small-number teaching data.'),
 ('What does RSA do to m65 in that model?','It gives ciphertext 2790 and decrypts back to 65.'),
 ('What representative values are allowed?','Integers from 0 through n−1; out-of-range values are rejected.'),
 ('Must m be coprime to n for correct two-prime RSA?','No. Correctness extends to all representatives in range using the two-prime/CRT structure.'),
 ('Why use square-and-multiply?','To compute modular powers with intermediate reduction using exponent bits, rather than constructing a huge full power.'),
 ('Is the teaching pow helper constant-time?','No. It is transparent bounded arithmetic, not protected production RSA.'),
 ('Why is raw RSA deterministic?','The same representative and public key produce the same modular-power result, without randomized scheme encoding.'),
 ('Does factoring n suffice to recover private information?','Yes, but that does not prove all possible RSA failures equivalent to factoring.'),
 ('Does a 2048-bit RSA key imply 2048-bit security?','No. Algorithm key length is not the same as security strength across algorithm families.'),
 ('What OAEP hashes are used in the actual lab?','SHA-256 for OAEP and MGF1-SHA-256.'),
 ('What is its OAEP message-byte limit?','190 bytes with a 256-byte modulus and 32-byte digest:256−64−2.'),
 ('Does OAEP identify the sender?','No. Anyone with the public encryption key can encrypt; an authenticated protocol is still required.'),
 ('What signature scheme actually runs?','RSA-PSS/SHA-256 with digest-length salt and fresh 2048-bit keys.'),
 ('Is signing private-key encryption?','No. A signature scheme has defined hashing/encoding/verification rules and a different goal.'),
 ('Can a signed statement still be false?','Yes. A valid signature does not establish truth, a specific human action, freshness or a legal outcome automatically.'),
 ('Why is HMAC not public non-repudiation?','Each shared-secret holder can create valid tags, unlike a publicly verified signature under its assumptions.'),
 ('What does a certificate bind?','A public key to a subject/attributes under an issuer’s signature and issuance policy.'),
 ('Does a certificate contain its subject’s private key?','No. The private material must be separately protected.'),
 ('What is a CA?','An authority performing policy-based certificate issuance/signing and relevant status management.'),
 ('What is an RA?','A delegated registration/identity-checking role; it can be integrated with a CA.'),
 ('Does a valid CSR signature prove the claimed identity?','No. It relates to possession of the signing key, not the truth/authorization of the requested identity.'),
 ('Why is a self-signed root not automatically trusted?','Trust comes from an independently trusted configuration/policy, not self-signature alone.'),
 ('Which hostname is used in the lab certificate?','The reserved fictional SAN portal.diploma.test; no public domain is enrolled.'),
 ('What else matters besides an issuer signature?','Trust path, constraints, time, intended identity, usage/purpose and the required status policy.'),
 ('How do expiry and revocation differ?','Expiry ends the stated validity interval; revocation can invalidate a certificate earlier.'),
 ('Does ordinary path validity prove non-revocation?','No. The actual revoked leaf still passes the profile without its explicit CRL check.'),
 ('What important activities are not performed?','Public enrollment, real RA identity vetting, OS/browser trust installation, live TLS, full-chain revocation, OCSP and FIPS certification.')]
VIVA=[{'title':tr('Unit 3 Viva and Short Revision'),'items':[{'q':tr(q),'a':tr(a)} for q,a in QA]}]
