"""Export stored Unit 3 results; no RSA generation, OpenSSL or network required."""
import csv,io,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'preview/DI05007021_unit3_practicals.zip'
README='''# DI05007021 — Unit 3 — Public-Key Cryptography (English only)

GTU Semester 5 / 2026–27 / 10 hours / 25% / CO3.
Official Practical 6: implement RSA asymmetric-key encryption. Examples 01–03
show public small-number RSA arithmetic and its limits;04–10 are supporting
real RSA-OAEP, RSA-PSS, CSR and local certificate-validation illustrations.
They are not invented extra official practical numbers.

## Run
Python 3.10+; reference Python 3.13.16 and OpenSSL 3.5.7 on Debian 13 x86_64.
No pip packages are required. Install OpenSSL 3 through your normal trusted OS
process if missing. PKI/permission examples are reference-tested on Linux;
Windows users can use an appropriate authorized WSL/Linux lab. Native Windows
GUI, browser trust settings and public CA workflows are not claimed as tested.
Keep rsa_math.py and pki_lab.py beside the 10 scripts at the extracted ZIP ROOT.
Run: python3 sec3p01.py (then other examples separately). No PYTHONPATH setup.

01 textbook RSA;02 square-and-multiply;03 raw-RSA weaknesses on fixed toy data;
04 real RSA-OAEP/SHA-256;05 RSA-PSS/SHA-256;06 CSR signature/tamper;
07 local root/intermediate/leaf chain;08 negative validation matrix;
09 real local leaf CRL before/after revocation;10 certificate tamper/cleanup.

## Teaching arithmetic is not production RSA
p61,q53,n3233,e17,d2753 are all PUBLIC classroom values. The private exponent
label in 01 is explicitly public demo data, not a real private key. Use integer
representatives0 through n−1. The trial-prime helper is bounded, not a real
key-generation engine, secure encoding or constant-time implementation.
Raw RSA is deterministic and algebraic; never deploy textbook pow encryption.
Real byte-message demo uses OAEP with SHA-256 and MGF1-SHA-256. RSA 2048 gives
256-byte ciphertext and a 190-byte OAEP message limit under this profile.
Digital signatures use RSA-PSS/SHA-256 with digest-length salt, not private-key
encryption. None of these examples is a complete authenticated messaging/TLS
protocol, post-quantum design, security-for-ever promise or FIPS certification.

## Private fixture, no identity/trust claim
Real RSA keys are fresh 2048-bit keys generated only inside a temporary owned
mode 0700 directory. Private PEM files are 0600 and deleted on context exit,
including tested failure paths. They are NEVER printed or shipped. Unencrypted
short-lived lab keys are not advice for persistent production storage.
All identities are fictional/reserved .test names. CSR verification proves a
key-related signature, not real RA identity/control vetting. The local CA is a
disposable fixture, not a public or production CA. No OS/browser trust store is
changed, no real domain enrolled, no external network or TLS server accessed.

Certificate verification explicitly supplies the owned lab root and issuer,
checks strict X.509 profile, dates, hostname and server purpose. Wrong hostname,
purpose, missing intermediate, expiry, unrelated root and signature modification
are actually rejected. Expiry uses an evaluation timestamp, not an OS clock
change. Do not bypass validation errors to make a connection work.
The actual CRL experiment checks the LEAF only against a supplied local CRL.
It is NOT full-chain revocation, live CRL download or OCSP. Ordinary path
verification without a status check still accepts the revoked leaf: path OK
alone is not a non-revocation assertion. Follow required status policy in real
clients. No general PKIX conformance or browser-validation claim is made.

## Output and study
expected/*.txt records actual reference stdout. Random keys, signatures,
ciphertexts, temporary paths and certificate timestamps are not exposed as fixed
sample values: real facts and verification outcomes are reported instead.
New runs create new keys/certificates; version-dependent error wording/codes or
OS restrictions may differ. Report restrictions, do not weaken host protection.
The RSA arithmetic CSV records the actual fixed worked square-and-multiply
trace. journal.csv has blank cells for your own observations.

Main notes contain 16 lessons, 10 diagrams, 14 cards, 36 viva and 16 answered
practice questions. Suggested 3/4/7-mark sizes are original revision guidance,
NOT official GTU questions, assigned marks or a promised paper pattern.
Course assessment stays 70+30 theory and 20+30 practical=150.

26 files: 10 scripts, 10 actual output files,rsa_math.py,pki_lab.py,runtime.json,
rsa_trace.csv,journal.csv and this README. No private PEMs, binaries or packages.
'''

def csv_text(rows):
 f=io.StringIO();csv.writer(f,lineterminator='\n').writerows(rows);return f.getvalue()

def export(path=OUT):
 unit=json.loads((ROOT/'content/computer/sem5/DI05007021/unit3.json').read_text())
 files={'README.md':README,'rsa_math.py':(ROOT/'tools/infosec_u3_math.py').read_text(),
  'pki_lab.py':(ROOT/'tools/infosec_u3_lab.py').read_text(),
  'runtime.json':json.dumps(unit['runtime_evidence'],indent=2)+'\n'}
 files['rsa_trace.csv']=csv_text([['LSB_first_bit','Successive_power_mod3233','Accumulator_mod3233']]+[
  [r['bit'],r['power'],r['accumulator']] for r in unit['worked_data']['modexp_trace']])
 files['journal.csv']=csv_text([['Example','Public input / intended profile','Observed output','Interpretation','Limitation']]+[
  [p['id'],'','','',''] for p in unit['programs']])
 for p in unit['programs']:
  files[p['id']+'.py']=p['code']['en'];files['expected/'+p['id']+'.txt']=p['out']
 assert len(files)==26
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for name,data in files.items():
   info=zipfile.ZipInfo(name,(2026,10,29,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   z.writestr(info,data.encode())
 print('Unit 3 practical kit:',path.stat().st_size,'bytes / 26 files');return str(path)

if __name__=='__main__':export()
