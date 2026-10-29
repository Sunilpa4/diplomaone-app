"""Offline deterministic final-unit kit: read frozen evidence only."""
import csv,io,json,zipfile
from pathlib import Path
from content_DI05007021_u5_guides import GUIDES,CASES
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'preview/DI05007021_unit5_practicals.zip'
HELPERS={'defence.py':'infosec_u5_defence.py','manifest_verify.py':'infosec_u5_manifest.py',
         'localnet.py':'infosec_u4_localnet.py','pki_lab.py':'infosec_u3_lab.py'}
README='''# DI05007021 — Unit 5 — Introduction to Cyber Security (English only)

Semester 5 / 2026–27 / 8 hours / 15% / CO5. Official Practicals 11/12 study
cybersecurity fundamentals/mitigation and Kali Linux. The ten scripts are safe
supporting illustrations, not invented extra official practical numbers.

## Run
Python 3.10+ with sqlite3 in its standard-library build; reference 3.13.16.
Keep defence.py,manifest_verify.py,localnet.py,pki_lab.py beside the 10 root
scripts and preserve the kali_metadata/ subfolder. No pip or PYTHONPATH setup.
Run: python3 sec5p01.py (then other scripts separately).
TLS example 08 requires OpenSSL 3 CLI and Python TLS1.3 support; metadata 10 needs
GPG. Reference Debian 13 x86_64 / OpenSSL 3.5.7 / GnuPG2.4.7. Native Kali/Windows
GUI/VM workflows are not claimed as executed; use an appropriate authorized
local learning environment and trusted OS package processes for prerequisites.

01 actual parameter binding in SQLite memory;02 actual connection-authorizer
write rejection;03 offline URL hints;04 fictional ARP dictionary comparison;
05 six-event token-bucket model;06 neutral in-memory email parsing;07 benign
owned file digest;08 real owned loopback TLS and wrong-name rejection;
09 actual benign single-file copy/restore;10 actual pinned-key signed metadata.

## Strictly bounded study
No malware, EICAR string, bot/C2, backdoor, persistence, credential harvesting,
phishing delivery, spoofed packet/cache change, network flood, public target or
real user data is created/accessed. No links are opened or emails sent.
SQL-like test input is bound as data; no vulnerable concatenated query or
account-bypass attack is executed. The authorizer is a limited per-connection
fixture, not a complete OS/database-role or row-authorization design.
ARP/rate examples are logical models, not attacks/detection proof or a DDoS
benchmark. URL/header hints do not establish legitimacy, reputation or sender
authentication. Hash changes do not identify malware/attackers. Recovery of one
same-folder copy is not offline/immutable backup architecture or incident cure.

Only08 opens sockets: owned 127.0.0.1, OS-assigned ports, bounded message and
explicit certificate/hostname checking. Wrong hostname is really rejected;
validation is never bypassed. It is not an actual MITM, public TLS audit, mutual
TLS or full VPN. All workers, listeners, temporary files and fresh private keys
close/are removed, including tested failure paths. No private PEMs are shipped.

## Kali: metadata-only reality, guided OS study
Kali Linux itself is NOT downloaded, installed or booted. No ISO/VM or offensive
toolkit is included. Reference host is Debian, not relabelled Kali output.
The bundled public official Kali 2026.3 files are SHA256SUMS, its detached
signature, public archive key and a dated provenance record. GPG actually checks
VALIDSIG under the primary fingerprint independently compared with official
Kali documentation: 827C8569F2518CC677FECA1AED65462EC8D5E4C5.
It uses a temporary 0700 keyring with no keyserver/automatic retrieval and does
not modify user/system keyrings or assert ownertrust automatically.
Only signed METADATA is verified. The published installer hash was checked
against the official download-page entry; no actual ISO bytes were obtained or
hashed. Students must still check current authentic keys/version/status and hash
their actual downloaded image before any guided isolated-VM activity.
The historical frozen record is not a perpetual latest-release/key-validity or
image-security guarantee. No private signing key is supplied.

## Journal/cases
Guides provide fictional defensive case study and optional safe Kali VM/OS
steps; those Kali-side steps were not run here. case_sheet.csv and journal.csv
are blank learner-work templates, not real incident records. Use appropriate
institutional/verified official reporting channels and preserve relevant evidence
safely. Do not investigate/confront/trace people without authorization or publish
private details. Legal classification depends on facts/jurisdiction; no statutory
reporting deadline, law-section result or guaranteed remedy is promised.

Notes contain 16 topics, 8 diagrams, 12 cards, 32 viva answers and 16 original
answered revision questions. Suggested 3/4/7-mark sizes are NOT official GTU
questions/allocations/paper predictions. Course scheme stays 70+30 theory and
20+30 practical=150. All five Information Security units are now prepared.

34 files: 10 scripts, 10 actual outputs, 4 helpers, 4 small public metadata files,
README,runtime.json,case_sheet.csv,journal.csv and 2 guided-only Markdown files.
No executable binaries, real malware/captured traffic, private keys or ISO/VM.
'''

def csv_text(rows):
 f=io.StringIO();csv.writer(f,lineterminator='\n').writerows(rows);return f.getvalue()

def export(path=OUT):
 unit=json.loads((ROOT/'content/computer/sem5/DI05007021/unit5.json').read_text())
 files={'README.md':README,'runtime.json':json.dumps(unit['runtime_evidence'],indent=2)+'\n'}
 files.update({name:(ROOT/'tools'/source).read_text() for name,source in HELPERS.items()})
 for p in sorted((ROOT/'tools/fixtures_DI05007021_u5').iterdir()):
  if p.is_file():files['kali_metadata/'+p.name]=p.read_bytes()
 files.update(GUIDES)
 files['case_sheet.csv']=csv_text([['Case','Fictional study scenario','Your classification','Your defensive response','What is not proven']]+[[n,s,'','',''] for n,s in CASES])
 files['journal.csv']=csv_text([['Example','Input/tool/version','Observed output','Interpretation','Limitation']]+[[p['id'],'','','',''] for p in unit['programs']])
 for p in unit['programs']:
  files[p['id']+'.py']=p['code']['en'];files['expected/'+p['id']+'.txt']=p['out']
 assert len(files)==34
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for name,data in files.items():
   info=zipfile.ZipInfo(name,(2026,10,29,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   z.writestr(info,data if isinstance(data,bytes) else data.encode())
 print('Unit 5 practical kit:',path.stat().st_size,'bytes / 34 files');return str(path)

if __name__=='__main__':export()
