# DI05007021 — source, scope and execution record

Checked: **29 October 2026**. User selected **English only** after reviewing the syllabus. This release prepares **Unit 1 only**; Units 2–5 remain unprepared. The user mentioned two main Semester 5 subjects, but only this subject's syllabus was supplied: no second subject or syllabus is invented.

## Authoritative curriculum

- Uploaded `/home/user/uploads/DI05007021.pdf`: 5 pages, SHA256 **ae1602e5b6a1ee6b8e523a832e4908141ea4a79c8fb89208d987f17f6e3b05aa**. The official GTU download at https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI05007021.pdf was independently retrieved and is **byte-identical**. Local text transcription: `tools/syllabus_DI05007021.txt`.
- Computer Engineering, Semester 5, effective **2026–27**, PCC-13. Information Security, 4 credits, L3/T0/PR2. Theory ESE 70 + PA 30; practical PA 20 + ESE 30 = **150**.
- Five units: security fundamentals 6h/15%; conventional/symmetric cryptography 12h/25%; public-key cryptography 10h/25%; network security 9h/20%; cybersecurity 8h/15%. Total 45h/100%.
- CO1: describe information-security fundamentals. Practical 1: basic TCP/IP utilities. Remaining eleven practicals cover the named ciphers, Wireshark, VLAN/DMZ/firewall simulation, cybersecurity study and Kali Linux; none is relabelled as completed in this release.
- Theory RBT distribution: Remember 25%, Understand 50%, Apply 25%; other levels 0%. Practice questions are original, with clearly **suggested** 3/4/7-mark revision sizes, not official paper questions, official allocations, predictions or a guaranteed paper pattern. Their model answers are in Notes section 6.

## Technical references and interpretation

- NIST CSRC confidentiality/integrity/availability and passive-attack definitions support the CIA distinctions. Definitions are paraphrased; fictional college examples do not imply a real deployment.
- **ITU-T X.800 (1991)**, especially §§5.2–5.4, supplies the five service categories, eight specific and five pervasive mechanisms. The actual official PDF was read, not only its landing page. Names are retained; explanations are original. The historical classification is not a recommendation to deploy old ciphers.
- CISA's **archived 2021** DoS article supports the basic DoS/DDoS distinction and defensive context. It is identified as archived, not current policy. No attack instructions, attack traffic, resource exhaustion or performance benchmark are included.
- Official Python hashlib/hmac documentation supports the small executable illustrations. Runtime is the actually observed Python **3.13.16**, not the version currently behind the generic `/3/` documentation link.
- All nine source URLs are recorded in unit1.json and linked from Notes. GTU, all NIST term pages, ITU landing/PDF, CISA article, hashlib and hmac links were fetched successfully.
- Authentication is distinguished from authorization/enforcement; HMAC is not encryption, a public signature, replay protection or public non-repudiation. A bare hash needs a trustworthy reference. Signatures do not automatically prove a human action, a statement's truth or a legal outcome. Availability and local reachability are not security guarantees.

## Actual execution and limits

- **6 executed examples**: real SHA-256 comparison; real HMAC-SHA256 verification with fresh RAM-only key; one framed private TCP echo; read-only loopback address/route/neighbour queries; bounded localhost ping attempt; actual localhost name-service resolution and an owned socket-table query.
- Reference: Python 3.13.16, Debian GNU/Linux 13 (trixie), x86_64; ip/ss iproute2 **6.15.0**, ping iputils **20240905**. Existing utilities were used; no database/runtime installation or host-security change was required.
- **Ping was actually denied socket permission**. Stored output says `blocked_by_lab_permissions`; no ICMP success is invented. A permitted student machine may instead observe one echo reply. Denied ping plus working local TCP is not evidence of DoS.
- Private IPv4 loopback only, TCP port 0/OS-assigned ports, one fixed teaching message, bounded timeouts, exact-length receive, closed sockets and joined worker. No public service, traffic capture, foreign hosts/processes, permanent server, user credentials or production system is involved.
- Windows ipconfig/tracert/netstat/arp and unexecuted traceroute/DNS/WHOIS/tcpdump/FTP/Telnet examples are labelled **guided**, not executed. getent localhost is OS name-service resolution, not necessarily a DNS query; route lookup is not traceroute. Legacy plaintext FTP/Telnet must not carry real credentials.
- Six programs and six actual stdout files, non-secret runtime metadata, README and blank CSV journal form a deterministic **15-file ZIP**. No pip dependency, binary or credential is shipped. Archive export needs only stored JSON, not networking, executing examples or a database.

## Validation and release gates

- **26 validation groups passed**: syllabus/scheme and only-U1 availability; English/no stars; all topic/mechanism counts; original answered questions; all six fresh program outputs; genuine SHA/HMAC tamper/wrong-key checks; TCP framing, incomplete-message and closure checks; real read-only CLI, ping-denial and owned-socket observations; honest guided-tool scope; safe HTML and linked IDs; eight self-contained SVG font bounds/rasterization; six preview views; all six extracted-ZIP reruns; offline ZIP export; deterministic rebuild; complete prior-content/public-export preservation and credential/binary checks.
- Both eight-diagram contact sheets were visually reviewed. All text is present, legible and within bounds; the authentication-flow label has a white backing to avoid the connecting arrow crossing its text. Rasterization explicitly uses app-normalized DejaVu fonts.
- `tools/baseline_before_DI05007021.json` protects **all 766 prior content files** byte-for-byte. Every prior exported subject/unit is also compared with the last published public repository. Catalog changes only add the new subject, Computer Semester 5 listing and new hashes; existing subject/branch entries retain their data. English-only catalog names may omit the optional Gujarati value without changing older names.
- Old MongoDB/Cassandra/Neo4j/Redis suites are **not claimed as rerun**: their temporary installations were deliberately cleaned earlier. New checks require no old database. The final native Flutter CI must render all **65 units**, including the prior 64, at the exact new source commit before publishing.
- Publication must preserve the existing web-app root, all old subjects/units and NoSQL availability [1,2,3,4,5]. Fresh LIVE catalog/subject/unit bytes, all eight normalized embedded SVGs, hashes and new subject availability **[1]** are required after publication. Do not use an older green CI run as approval.

## Rebuild / validate / export

- `python3 tools/build_DI05007021_u1.py` — execute safe examples and rebuild Unit 1, SVGs, preview and kit.
- `python3 tools/test_DI05007021_u1.py` — run 26 validation groups (prior public-repo clone expected at `/opt/repos/diplomaone-content`).
- `python3 tools/export_DI05007021_u1_practicals.py` — regenerate the kit offline from stored results.

Downloads: `preview/DI05007021_unit1_preview.html` and `preview/DI05007021_unit1_practicals.zip`. Diagnostic PNGs/build/bytecode are regenerable and should be removed after review to retain the user's workspace cleanup. Raw source SVGs, notes, code, HTML preview and ZIP must remain.
