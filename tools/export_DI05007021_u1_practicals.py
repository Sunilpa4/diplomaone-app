"""Export stored real results without networking, executing programs or a database."""
import csv,io,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'preview/DI05007021_unit1_practicals.zip'
README='''# Information Security — DI05007021 — Unit 1 (English only)

GTU 2026–27 / Semester 5 / 6 hours / 15% syllabus weight / CO1.
Practical 1 covers basic TCP/IP utilities. These six small supporting examples
illustrate trusted integrity checking, HMAC and authorized local observations.
They are not an enterprise security system or the later official cipher labs.

## Run locally
Use a private Linux learning environment with Python 3.10+ (reference 3.13.16).
No pip dependencies are required. Utility examples need iproute2 (ip and ss),
iputils ping and getent. Install through your normal OS package process if
needed; the examples never install software or change network/host settings.
Run: python3 sec1p01.py (then 02 through 06 separately).
Examples 03 and 06 briefly open their OWN loopback socket on an OS-assigned
port and close it. No browser access, persistent server or public host is used.

## Real evidence and honest limits
expected/*.txt contains actual stdout from the reference, not hand-made output.
The hash and HMAC are really computed; the HMAC key is fresh, RAM-only and never
printed. HMAC is NOT encryption, a public signature, non-repudiation or a
replay-prevention protocol. A bare hash needs a trusted reference.
The TCP example exchanges exactly one framed teaching message. Address/route/
neighbor queries inspect only loopback. ss inspects only the owned socket.
getent uses OS name-service configuration and is NOT necessarily a DNS test.

The reference sandbox denied the ping socket operation. Example 05 records
blocked_by_lab_permissions rather than inventing a successful ICMP reply.
On an appropriately permitted machine it may instead report one_local_echo_reply.
Dynamic ports and network timing are not published as fixed expected values.
These are reference results, not a guarantee of another machine's environment.

## Safety and practical journal
Use only your own system or an instructor-authorized lab. Never flood a host,
scan other people's systems, capture their traffic, publish private addresses
or credentials, or disable host protection merely to force an example to work.
No DoS/DDoS traffic is generated and no mitigation benchmark is claimed.
Windows ipconfig/tracert/netstat/arp, traceroute, nslookup, host, whois, tcpdump,
FTP and Telnet remain GUIDED examples in the notes, NOT executed reference runs.
Legacy plaintext FTP/Telnet should not carry real passwords.
Wireshark, Cisco Packet Tracer and Kali Linux are later practicals, not claimed
as run here. Use journal.csv to record your OWN observations and limitations.

Unit preview/live notes include 14 lessons, 8 diagrams, 12 reference cards,
28 viva answers and 12 answered practice questions. Suggested 3/4/7-mark sizes
are revision guidance only, not official GTU question marks or a paper pattern.
The official course scheme is theory 70+30 and practical 20+30 = 150 marks.

15 files: 6 Python examples, 6 actual output files, runtime.json, journal.csv,
and this README. No external packages, credentials or server binaries included.
'''

def export(path=OUT):
 unit=json.loads((ROOT/'content/computer/sem5/DI05007021/unit1.json').read_text())
 journal=io.StringIO();w=csv.writer(journal,lineterminator='\n')
 w.writerow(['Task','Platform','Command or example','Observed result','Interpretation','Limitation / authorization'])
 for label,cmd in [('Integrity','python3 sec1p01.py'),('HMAC','python3 sec1p02.py'),
   ('One private TCP exchange','python3 sec1p03.py'),('Loopback setup','python3 sec1p04.py'),
   ('Bounded ping','python3 sec1p05.py'),('Resolver and own socket','python3 sec1p06.py')]:
  w.writerow([label,'Linux/Python reference',cmd,'','',''])
 files={'README.md':README,'runtime.json':json.dumps(unit['runtime_evidence'],indent=2)+'\n','journal.csv':journal.getvalue()}
 for p in unit['programs']:
  files[p['id']+'.py']=p['code']['en'];files['expected/'+p['id']+'.txt']=p['out']
 assert len(files)==15
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for name,data in files.items():
   info=zipfile.ZipInfo(name,(2026,10,29,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   z.writestr(info,data.encode())
 print('Information Security practical kit:',path.stat().st_size,'bytes / 15 files');return str(path)

if __name__=='__main__':export()
