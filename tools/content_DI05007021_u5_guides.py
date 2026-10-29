"""Study Practicals 11/12: safe case work and Kali VM/download guidance only."""
GUIDES={
 'guides/defensive_case_study.md':'''# Practical 11 — cybersecurity fundamentals and mitigation study

These are fictional study cases, not incidents observed on real people/systems.
The scripts use in-memory databases, benign owned files, static records, owned
loopback TLS and frozen public signed metadata. They do not deliver malware,
phishing, spoofed packets, bot/C2 traffic, floods or attacks on external targets.

For each case in case_sheet.csv, identify asset, weakness/threat/action/impact,
possible CIA or personal-safety effects, a suitable prevention/detection/response
control, and what the available observation does NOT prove. Do not assume an
outage, changed MAC, matching pattern or file hash proves who attacked.

Suggested workflow:
1. Use only public/fictional data or appropriately authorized private fixtures.
2. Run a relevant supporting example and record ACTUAL output and limits.
3. Parameterize SQL values; separate query structure from data, validate allowed
   structural choices, enforce authorization and suitable least privilege.
4. Read URL/email hints without opening links or sending messages. HTTPS,
   grammar, display name or From-header parsing alone is not legitimacy proof.
5. For suspected incidents, use the institution's approved reporting procedure,
   preserve appropriate evidence safely, and involve qualified defenders. Do
   not run suspicious files or forward harmful attachments to prove a point.
6. For impersonation/harassment/stalking concerns, protect privacy, use platform
   safety/report tools and trusted support/appropriate authorities. Seek local
   emergency help if there is immediate danger; do not confront or investigate
   a suspected offender using unauthorized methods.
7. Consult current official guidance for your jurisdiction. CERT-In's official
   site is a source of Indian advisories/contact information; this handout does
   not prescribe legal filing deadlines, statute sections or a guaranteed remedy.

All recovery/hash results are narrow fixture observations, NOT malware removal,
a full incident investigation, production prevention or a resilience benchmark.
Suggested practice-question marks in the notes are revision sizes, not official
GTU allocations. Case labels are educational classifications, not legal findings.
''',
 'guides/kali_study.md':'''# Practical 12 — study Kali Linux (GUIDED VM/OS activity)

Kali Linux itself is NOT downloaded, installed or booted here. No ISO/VM image,
malware sample or offensive toolkit is shipped. The reference host is Debian 13,
not a Kali VM. Actual GPG verification in sec5p10 checks ONLY frozen signed
Kali 2026.3 metadata, NOT an absent ISO or the security of an installed OS.

Study the official role first: Kali is aimed at professional penetration testing
and security auditing, not a default general-purpose beginner desktop. Owning a
tool is not permission to assess somebody else's accounts, network or devices.

Guided optional VM procedure, NOT an executed reference run:
1. Check authorization, hardware/virtualization requirements and official Kali
   documentation. Obtain an appropriate image only through its official sources.
2. Check the CURRENT authentic signing-key fingerprint using a trusted official
   channel; do not trust an arbitrary key linked in an unexpected message.
3. Verify the detached signature on the appropriate SHA256SUMS file, then compute
   the hash of the actual downloaded ISO and compare the exact filename/digest
   locally. A signed manifest alone does not verify missing image bytes.
4. If verification fails or the version/key is no longer appropriate, STOP and
   investigate; never ignore a mismatch to continue. Do not upload hashes or
   private data to random external converters just to compare letter case.
5. Use an instructor-approved isolated VM, snapshots and appropriate host-only/
   internal networking. Do not bridge experiments to an unapproved network;
   shared folders/clipboard/integration need deliberate risk decisions. A VM is
   not a guarantee that executing malware is safe. No malware execution is part
   of this introductory study.
6. In your OWN VM, inspect OS/version, user, files and local interfaces using
   ordinary read-only commands, for example whoami, pwd, ls, cat /etc/os-release,
   ip -br address and ss -ltn. These Kali-side commands were NOT run here.
7. Follow approved updates/repository guidance, protect credentials, and study
   tool categories without targeting real systems. Record your actual OS/tool
   version, screenshot/observations and limits if your instructor requests it.

Frozen metadata exercise details:
- Official versioned manifest: https://cdimage.kali.org/kali-2026.3/SHA256SUMS
- Signature: https://cdimage.kali.org/kali-2026.3/SHA256SUMS.gpg
- Public key: https://archive.kali.org/archive-key.asc
- Documented primary pin checked 29 Oct 2026:
  827C8569F2518CC677FECA1AED65462EC8D5E4C5
- Reference entry: kali-linux-2026.3-installer-amd64.iso. Its PUBLISHED manifest
  SHA256 is db9cbed33edb45727d16911813c2434fcd1419585007884153be22a03b30ec2f.
- This is a frozen historical teaching record, NOT a perpetual latest-release,
  key-validity or image-security claim. No bytes of that ISO were downloaded.

sec5p10 uses a temporary mode0700 GPG home, disables automatic retrieval, checks
VALIDSIG under the pinned primary fingerprint and removes the keyring. It does
not import into a user/system keyring or assert ownertrust automatically. A
public signing key is provided; no secret/private signing material is included.
'''}
CASES=[
 ('C01','An application exposes an unpatched component. Distinguish weakness, threat, attempted action and impact.'),
 ('C02','An unexpected message asks for a login one-time passcode. Plan verification/reporting without replying or opening its links.'),
 ('C03','A fictional gateway IP/MAC mapping changes. Could legitimate replacement/failover also explain it?'),
 ('C04','A service becomes unavailable. Explain why an outage alone is not proof of DoS or its source.'),
 ('C05','A benign fixture file no longer matches a trusted digest. What is known, and what is not established?'),
 ('C06','A six-event token-bucket model refuses two admissions. Why is this not a network DDoS benchmark?'),
 ('C07','An SQL-like input is bound as a value. Explain injection prevention versus access authorization.'),
 ('C08','A person reports persistent threatening online contact. Plan privacy-preserving support and appropriate official reporting.'),
 ('C09','A learner has security tools. Explain why tool availability is not authorization to use them on other systems.'),
 ('C10','A pinned-key signature verifies a checksum manifest but the ISO is absent. What has NOT been verified?')]
