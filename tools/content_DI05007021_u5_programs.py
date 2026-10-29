"""Ten bounded defensive illustrations; no malware/attack delivery or Kali boot."""
import subprocess,sys,tempfile,textwrap,shutil
from pathlib import Path
from subject_DI05007021 import ROOT,tr
HELPERS={'defence.py':ROOT/'tools/infosec_u5_defence.py',
 'manifest_verify.py':ROOT/'tools/infosec_u5_manifest.py',
 'localnet.py':ROOT/'tools/infosec_u4_localnet.py','pki_lab.py':ROOT/'tools/infosec_u3_lab.py'}
FIXTURES=ROOT/'tools/fixtures_DI05007021_u5'

def example(n,title,code,expl):
 return {'id':f'sec5p{n:02d}','title':tr(title),'code':tr(textwrap.dedent(code).strip()+'\n'),'expl':tr(expl)}

EXAMPLES=[
 example(1,'Actual SQLite parameter binding: input stays data, not SQL syntax',r'''
 import sqlite3
 from contextlib import closing

 with closing(sqlite3.connect(":memory:")) as db:
     db.execute("CREATE TABLE courses(code TEXT, title TEXT)")
     db.executemany("INSERT INTO courses VALUES (?, ?)",
                    [("C01", "Networks"), ("C02", "Security")])
     query = "SELECT title FROM courses WHERE code = ?"
     normal = db.execute(query, ("C01",)).fetchall()
     fixed_demo_input = "' OR 1=1 --"
     literal = db.execute(query, (fixed_demo_input,)).fetchall()
     count = db.execute("SELECT COUNT(*) FROM courses").fetchone()[0]
     print("normal_rows:", len(normal))
     print("bound_demo_input_rows:", len(literal))
     print("fixture_rows_unchanged:", count == 2)
 ''','A real in-memory SQLite database executes only fixed/parameterized query structures. The fixed classroom input is bound as a literal value and returns no match, rather than altering SQL syntax. No vulnerable concatenated query, real account, public service or external database is attacked. Binding data values does not supply application authorization or parameterize table/column identifiers.'),
 example(2,'Actual SQLite authorizer: deny a fixture write operation',r'''
 import sqlite3
 from contextlib import closing

 with closing(sqlite3.connect(":memory:")) as db:
     db.execute("CREATE TABLE courses(code TEXT)")
     db.executemany("INSERT INTO courses VALUES (?)", [("C01",), ("C02",)])
     def authorize(action, arg1, arg2, database, source):
         allowed = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ}
         return (sqlite3.SQLITE_OK if action in allowed
                 else sqlite3.SQLITE_DENY)
     db.set_authorizer(authorize)
     rows = db.execute("SELECT code FROM courses").fetchall()
     print("read_rows:", len(rows))
     denied = False
     try:
         db.execute("DELETE FROM courses")
     except sqlite3.DatabaseError as error:
         denied = (getattr(error, "sqlite_errorcode", None)
                   == sqlite3.SQLITE_AUTH
                   or "not authorized" in str(error).lower())
     print("delete_denied:", denied)
     rows = db.execute("SELECT code FROM courses").fetchall()
     print("remaining_rows:", len(rows))
 ''','The actual SQLite connection authorizer allows reads and denies a DELETE, leaving both fictional rows intact. This illustrates a limited per-connection restriction, not a full database-account/OS least-privilege or row-authorization system. It runs only in memory; no user data or deployed database privilege is changed.'),
 example(3,'Offline URL hints: parse hostname, not display-prefix appearance',r'''
 from defence import url_signals

 intended = url_signals("https://college.example.test/portal")
 suffix = url_signals("https://college.example.test.attacker.test/portal")
 userinfo = url_signals(
     "https://college.example.test@notice.attacker.test/portal")
 plain = url_signals("http://college.example.test/portal")
 print("intended_exact_host:", intended["exact_expected_host"])
 print("suffix_exact_host:", suffix["exact_expected_host"])
 print("userinfo_exact_host:", userinfo["exact_expected_host"])
 print("userinfo_present:", userinfo["userinfo_present"])
 print("plain_http_https_signal:", plain["https_scheme"])
 print("any_legitimacy_proven:", any(x["authenticity_proven"]
       for x in [intended, suffix, userinfo, plain]))
 ''','Actually parses fixed reserved .test strings locally, without opening any URL. A familiar prefix or userinfo text is not the actual hostname. HTTPS/host matching alone do not prove a site honest, an email authentic or a link safe. This is not a URL-reputation service, comprehensive adversarial URL validator or phishing classifier.'),
 example(4,'ARP-change comparison on fictional dictionaries, not network spoofing',r'''
 from defence import arp_changes

 trusted = {"192.0.2.1": "02:00:00:00:00:01",
            "192.0.2.53": "02:00:00:00:00:53"}
 observed = dict(trusted)
 print("unchanged_entries:", arp_changes(trusted, observed))
 observed["192.0.2.1"] = "02:00:00:00:00:99"
 print("changed_entries:", arp_changes(trusted, observed))
 print("attack_confirmed:", False)
 print("ARP_packets_sent_or_cache_modified:", False)
 ''','Compares two invented IP/MAC mappings. A legitimate replacement/failover can also change a mapping, so a difference is a signal to investigate, not proof of ARP poisoning. No live ARP cache is read/changed and no forged ARP/IP packet, MITM path or external target is created.'),
 example(5,'DoS mitigation concept: six synthetic token-bucket decisions',r'''
 from defence import TokenBucket

 model = TokenBucket(capacity=2, refill=1)
 times = [0, 0, 0, 1, 1, 2]
 allowed = [model.allow(t) for t in times]
 print("synthetic_clock_decisions:", allowed)
 print("allowed:", sum(allowed))
 print("limited:", len(allowed) - sum(allowed))
 print("network_requests_or_flood_sent:", False)
 ''','Actually evaluates a tiny admission model on six fixed logical timestamps. No requests, load test, flood or service exhaustion occurs. A local rate limiter alone cannot guarantee DDoS resilience or protect saturated upstream capacity; the example is not a benchmark or deployed mitigation system.'),
 example(6,'Parse a training email without delivering it or trusting its display name',r'''
 from email import policy
 from email.parser import BytesParser

 raw = (b'From: "Campus Desk" <notice@notice.attacker.test>\r\n'
        b'Reply-To: training@reply.attacker.test\r\n'
        b'To: learner@college.example.test\r\n'
        b'Subject: Offline training fixture\r\n\r\n'
        b'Training data only. No links, requests or attachments.\r\n')
 message = BytesParser(policy=policy.default).parsebytes(raw)
 sender = message["From"].addresses[0]
 print("display_name:", sender.display_name)
 print("parsed_sender_domain:", sender.domain)
 print("matches_expected_domain:", sender.domain == "college.example.test")
 print("header_parsing_authenticates_sender:", False)
 print("email_sent_or_links_opened:", False)
 ''','A real RFC-style parser reads only neutral in-memory training headers. The displayed Campus Desk name is not the sender domain, and even a matching From header can be forged. No SMTP message, lure, credential form or attachment is sent. SPF/DKIM/DMARC or institutional verification is not performed or claimed.'),
 example(7,'Handle a benign file as data: trusted digest versus changed content',r'''
 import hashlib
 import tempfile
 from pathlib import Path

 with tempfile.TemporaryDirectory(prefix="owned-u5-file-") as folder:
     path = Path(folder) / "course-note.txt"
     path.write_bytes(b"Benign course note version 1\n")
     trusted = hashlib.sha256(path.read_bytes()).hexdigest()
     print("original_digest_matches:",
           hashlib.sha256(path.read_bytes()).hexdigest() == trusted)
     path.write_bytes(b"Benign course note version 2\n")
     print("changed_digest_matches:",
           hashlib.sha256(path.read_bytes()).hexdigest() == trusted)
     print("malware_scanner_or_payload_executed:", False)
 print("fixture_removed:", not Path(folder).exists())
 ''','Only a harmless owned text file is written/hashed; it is never executed. A mismatch detects this change relative to a trusted reference, not maliciousness, malware family, authenticity of an untrusted digest or complete host safety. No real malware sample, executable, EICAR string or antivirus product is introduced.'),
 example(8,'Actual owned TLS check: valid server versus wrong hostname',r'''
 import ssl
 import threading
 from unittest.mock import patch
 import localnet

 before = set(threading.enumerate())
 valid = localnet.private_tls_relay()
 rejected = False
 try:
     with patch.object(localnet, "HOST", "wrong.diploma.test"):
         localnet.private_tls_relay()
 except ssl.SSLCertVerificationError:
     rejected = True
 print("valid_TLS_version:", valid["tls_version"])
 print("valid_echo:", valid["echo_matches"])
 print("wrong_hostname_rejected:", rejected)
 print("network_workers_closed:", set(threading.enumerate()) == before)
 print("MITM_or_foreign_network_attack_performed:", False)
 ''','A real private TLS1.3 relay validates its owned server certificate and rejects a wrong hostname without disabling checks. Only fresh owned loopback fixtures are used; sockets/workers/keys close. This is not an actual MITM attack/detector, public TLS audit, client-certificate authentication, system VPN or guarantee against compromised endpoints or a malicious correctly named site.'),
 example(9,'Actual recovery of one benign owned file from a trusted copy',r'''
 import hashlib
 import tempfile
 from pathlib import Path
 import shutil

 with tempfile.TemporaryDirectory(prefix="owned-u5-recovery-") as folder:
     current = Path(folder) / "course.txt"
     backup = Path(folder) / "copy.txt"
     current.write_bytes(b"Known benign course content\n")
     trusted = hashlib.sha256(current.read_bytes()).digest()
     shutil.copyfile(current, backup)
     current.write_bytes(b"Changed teaching fixture\n")
     print("current_changed:",
           hashlib.sha256(current.read_bytes()).digest() != trusted)
     shutil.copyfile(backup, current)
     print("restored_digest_matches:",
           hashlib.sha256(current.read_bytes()).digest() == trusted)
     print("ransomware_or_offline_backup_system_tested:", False)
 print("fixture_removed:", not Path(folder).exists())
 ''','Really copies/restores an owned harmless file and checks the recovered content. This same-folder copy is NOT an offline/immutable backup architecture, ransomware experiment or proof that a compromised host is clean. Real recovery needs appropriate separate protection, access control, consistency and tested procedures.'),
 example(10,'Actual Kali signed-metadata verification — not ISO verification or boot',r'''
 from pathlib import Path
 from manifest_verify import verify_manifest

 result = verify_manifest(Path(__file__).resolve().parent / "kali_metadata")
 for name in ["signature_valid", "primary_fingerprint", "release",
              "installer_filename", "published_installer_sha256",
              "ISO_downloaded_or_verified", "Kali_booted",
              "isolated_keyring_removed"]:
     print(name + ":", result[name])
 ''','Real GPG verifies the bundled official Kali2026.3 SHA256SUMS detached signature under the primary fingerprint checked against Kali documentation. It uses an isolated temporary keyring, no keyserver/automatic retrieval and no change to user/system keyrings. Only signed METADATA is verified: no ISO/VM image is downloaded, hashed, installed or booted. A frozen historical entry is not a current-release or permanent key-validity guarantee.')]

def run_program(example):
 with tempfile.TemporaryDirectory(prefix='infosec-u5-example-') as td:
  folder=Path(td)
  for name,source in HELPERS.items():(folder/name).write_text(source.read_text())
  shutil.copytree(FIXTURES,folder/'kali_metadata')
  script=folder/(example['id']+'.py');script.write_text(example['code']['en'])
  r=subprocess.run([sys.executable,'-E',str(script)],cwd=folder,text=True,capture_output=True,timeout=60)
  assert r.returncode==0,(example['id'],r.stderr)
  assert not r.stderr,(example['id'],r.stderr)
 return dict(example,out=r.stdout)

def execute_all():return [run_program(p) for p in EXAMPLES]
