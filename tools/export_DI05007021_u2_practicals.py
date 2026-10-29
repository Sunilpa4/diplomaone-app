"""Deterministic offline export from stored Unit 2 evidence (no execution needed)."""
import csv,io,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'preview/DI05007021_unit2_practicals.zip'
README='''# DI05007021 — Unit 2 — Conventional and Symmetric Cryptography

English only / GTU Semester 5 / 2026–27 / 12 hours / 25% syllabus weight.
Official Practicals 2–5: Caesar encryption/decryption, Hill encryption,
Playfair encryption and rail-fence encryption. Other examples are supporting
classroom illustrations, not additional invented official practical numbers.

## Run
Python 3.10+; reference Python 3.13.16. No pip packages or server are needed.
Keep ciphers.py beside the 12 examples at the extracted ZIP ROOT.
Run: python3 sec2p01.py (then the other scripts separately).
No PYTHONPATH setup is required. The helper source contains the actual cipher
implementations and historical DES tables/round logic; inspect it while studying.

01 Caesar; 02 fixed-sample Caesar candidate search; 03 monoalphabetic mapping;
04 Vigenere; 05 Playfair; 06 Hill 2x2; 07 Hill 3x3/padding; 08 rail fence;
09 letter-pad arithmetic; 10 binary pad/key-reuse relation; 11 historical DES;
12 steganography in synthetic raw RGB bytes.

## Conventions — do not hide data loss
A=0 through Z=25; classical text is ASCII letters uppercased with whitespace
removed. Other characters are REJECTED, not silently discarded. Decryption
returns normalized/prepared text, not original formatting or punctuation.
Playfair merges J into I. Insert X for repeats/odd endings, using Q for a
repeated/final X. Decryption never blindly strips legitimate X/Q letters.
Hill uses COLUMN vectors and invertible 2x2 or 3x3 matrices modulo26; preserve
explicit X padding rather than guessing the original length. Rail-fence decoding
handles uneven rows directly without padding. One rail is the identity case.

## Security boundaries
These classical algorithms and single DES are NOT suitable for real secrets.
They do not provide authenticated encryption or a production key service.
All visible keys and messages are PUBLIC teaching data. Never put real keys,
credentials or user data into a shared journal. No live target is accessed.
The fixed XMCKL pad demonstrates arithmetic only, NOT perfect secrecy.
A genuine OTP needs independent uniform random secret pad material at least as
long as the message and used once. Python secrets uses an OS-backed CSPRNG;
our fresh-key example does not prove ideal information-theoretic randomness.
Its actual random key/cipher bytes are never printed or stored. The separate
fixed public reuse example checks C1 XOR C2 = P1 XOR P2, not automatic full
recovery of arbitrary secrets. OTP confidentiality alone does not authenticate.
The LSB example uses only a synthetic pixel-byte array, not a PNG/JPEG decoder,
real photo, network covert channel or guarantee of undetectability.

## Actual results and DES status
expected/*.txt stores actual stdout from all 12 examples. des_trace.csv stores
the real public-vector initial state and all 16 DES rounds. The cipher is really
computed, not replaced by a hard-coded expected output. Reference DES results
were independently compared with OpenSSL for 66 blocks in both directions.
OpenSSL is a maintainer-side cross-check; students do NOT need it to run scripts.
Its legacy provider was enabled only for individual comparison processes, never
by changing system crypto configuration. This is NOT FIPS validation.
NIST withdrew FIPS 46-3 on 19 May 2005. Historical structure is taught because it
is in the syllabus, not as a deployment recommendation. Real applications need
appropriate current authenticated encryption using vetted libraries/protocols.

## Revision and journal
journal.csv has blank observations for your own runs. Record preparation,
calculation, actual output, recovery target and limitations. Main preview/live
notes include 18 lessons, 10 diagrams, 14 reference cards, 36 viva and 16 answered
practice questions. Suggested 3/4/7-mark practice sizes are NOT official GTU
questions or a guaranteed exam pattern. Course scheme: 70+30 theory, 20+30
practical=150 marks; 25% weight is not a guaranteed question allocation.

29 files: 12 scripts, 12 actual outputs, ciphers.py,runtime.json,des_trace.csv,
journal.csv and this README. No dependencies, credentials or binaries shipped.
'''

def csv_text(rows):
 buffer=io.StringIO();writer=csv.writer(buffer,lineterminator='\n');writer.writerows(rows)
 return buffer.getvalue()

def export(path=OUT):
 unit=json.loads((ROOT/'content/computer/sem5/DI05007021/unit2.json').read_text())
 files={'README.md':README,'ciphers.py':(ROOT/'tools/infosec_u2_ciphers.py').read_text(),
  'runtime.json':json.dumps(unit['runtime_evidence'],indent=2)+'\n'}
 files['des_trace.csv']=csv_text([['Round','Left32_hex','Right32_hex','Subkey48_hex']]+[
  [r['round'],r['left'],r['right'],r['subkey']] for r in unit['worked_data']['des_rounds']])
 files['journal.csv']=csv_text([['Example','Public teaching input / preparation','Actual output','Recovery target','Limitation']]+[
  [p['id'],'','','',''] for p in unit['programs']])
 for p in unit['programs']:
  files[p['id']+'.py']=p['code']['en'];files['expected/'+p['id']+'.txt']=p['out']
 assert len(files)==29
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for name,data in files.items():
   info=zipfile.ZipInfo(name,(2026,10,29,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   z.writestr(info,data.encode())
 print('Unit 2 practical kit:',path.stat().st_size,'bytes / 29 files');return str(path)

if __name__=='__main__':export()
