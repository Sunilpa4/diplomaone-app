"""Offline deterministic Unit 4 kit; exports frozen evidence, no tools/network needed."""
import csv,io,json,zipfile
from pathlib import Path
from content_DI05007021_u4_guides import GUIDES
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'preview/DI05007021_unit4_practicals.zip'
HELPERS={'models.py':'infosec_u4_models.py','packets.py':'infosec_u4_packets.py',
 'localnet.py':'infosec_u4_localnet.py','pki_lab.py':'infosec_u3_lab.py'}
README='''# DI05007021 — Unit 4 — Network Security (English only)

GTU Semester 5 / 2026–27 / 9 hours / 20% / CO4. Practicals 7–10 are covered with
HONESTLY DIFFERENT evidence classes. This kit does not invent simulator output.

## What actually runs
01–04: declared Python logical DMZ/rule/state/VLAN models, NOT kernel/router/
switch enforcement or Packet Tracer.05–06 and12: actual TShark offline analysis
of a 1373-byte,16-frame SYNTHETIC PCAP.07: actual owned loopback HTTP allow-list
with200/403 outcomes.08: actual private TLS1.3 byte relay with a checked owned
certificate.09: actual owned temporary-file hash changes.10–11: invented
NIDS-style pattern/label fixtures, NOT Snort/Suricata or a deployed IDS.

## Run and requirements
Python 3.10+; reference 3.13.16. Keep models.py,packets.py,localnet.py,pki_lab.py
beside all 12 scripts at the ZIP ROOT; no PYTHONPATH setup or pip dependency.
Run: python3 sec4p01.py (then the others separately).
Analysis scripts need tshark on PATH; TLS example needs OpenSSL 3 CLI and a
Python SSL build supporting TLS1.3. Reference TShark 4.4.19 / OpenSSL 3.5.7 on
Debian 13 x86_64. Use a trusted OS package process if tools are missing.
No tool binary/package is included. Linux is the tested permission/network
reference; native Windows GUI commands are not claimed as executed.

## Synthetic PCAP, real dissection
synthetic.pcap is CONSTRUCTED by the supplied packet helper, NOT live capture,
not Packet Tracer output, and not a recording of the separate TLS example.
It has fake local MACs, RFC5737 documentation IPs, reserved .test DNS names,
ARP2,DNS2,TCP10 and two tagged UDP frames (VLAN10/20). Protocol-column labels
show HTTP2 as part of those TCP frames; filters may overlap. IPv4/TCP/UDP
checksums are actually computed and explicitly validated. In tested 4.4.19,
checksum.status1=Good,0=Bad,2=Unverified. Fixed timestamps are teaching data,
not a throughput/latency or production IDS benchmark.

Examples use tshark -n -r, never live -i/-f capture. Network name resolution is
disabled. No foreign traffic is observed. Correct checksums are not identity
proof or policy enforcement. BPF 'tcp port 80' differs from display expression
 'tcp.port == 80'; the BPF form is really rejected when used as a -Y expression.
packet_manifest.csv contains actual dissector fields from the supplied file.

## Networking and cryptographic scope
Only07/08 open real sockets: owned 127.0.0.1, OS-assigned ports, bounded teaching
messages, explicit timeouts and closed/joined workers. No public server, scan,
OS firewall/VLAN/route/namespace change, user credential or real host data.
TLS protects only client->relay here; the owned backend is plaintext loopback.
It is NOT a system VPN, IPsec, SOCKS conformance or general production gateway.
Fresh RSA private keys stay 0600 in a 0700 temp directory and are deleted; none
are exported. Only the owned lab root is explicitly trusted in that client;
no system/browser store changes. The HTTP allow-list is not a full HTTP parser,
WAF or production proxy. Logical models omit full TCP sequences/retransmission,
NAT, fragments and real kernel enforcement. Do not deploy them as protection.

## Guided tools are NOT reported as run
Wireshark GUI/live capture and Cisco Packet Tracer VLAN/DMZ/firewall are GUIDED
ONLY. See the four Markdown guides: their expected tests are not observations.
No .pkt/.pka file is fabricated; obtain your authorized simulator through its
official channel and record your own results. Interface/device features vary.
Router ACLs in the guide are stateless/minimal, not a stateful ASA/NGFW or a
complete ingress/egress design. Use only an authorized lab, never production.
Snort/Suricata, an NGFW appliance and a deployed HIDS/NIDS are NOT executed.
A hash change/pattern match does not confirm an intruder. Six boolean cases
provide a teaching confusion matrix only, not real network detection accuracy.

## Study/journal
Record tool/version, command/fixture, observation, interpretation and limits in
journal.csv. Never fabricate missing outputs or enable extra capture/host
privileges to force a result. Notes include 18 lessons, 10 SVGs, 14 cards, 36 viva
and 16 original answered practice questions. Suggested 3/4/7-mark sizes are not
GTU official questions/allocations/paper predictions. Course scheme remains
70+30 theory and 20+30 practical=150;20% unit weight is not guaranteed marks.

37 files: 12 scripts, 12 actual outputs, 4 helpers,synthetic.pcap,runtime.json,
packet_manifest.csv,journal.csv,README and 4 guided-only Markdown lab documents.
No private keys, binaries, real captured traffic or heavy runtimes are shipped.
'''

def csv_text(rows):
 f=io.StringIO();csv.writer(f,lineterminator='\n').writerows(rows);return f.getvalue()

def export(path=OUT):
 unit=json.loads((ROOT/'content/computer/sem5/DI05007021/unit4.json').read_text())
 files={'README.md':README,'runtime.json':json.dumps(unit['runtime_evidence'],indent=2)+'\n',
  'synthetic.pcap':(ROOT/'tools/fixtures_DI05007021_u4/synthetic.pcap').read_bytes()}
 files.update({name:(ROOT/'tools'/source).read_text() for name,source in HELPERS.items()})
 files.update(GUIDES)
 data=unit['worked_data'];files['packet_manifest.csv']=csv_text([data['manifest_fields']]+data['manifest_rows'])
 files['journal.csv']=csv_text([['Example / guide','Tool/version / evidence class','Observed result','Interpretation','Limitation']]+[
  [p['id'],'','','',''] for p in unit['programs']])
 for p in unit['programs']:
  files[p['id']+'.py']=p['code']['en'];files['expected/'+p['id']+'.txt']=p['out']
 assert len(files)==37
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for name,data in files.items():
   info=zipfile.ZipInfo(name,(2026,10,29,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   z.writestr(info,data if isinstance(data,bytes) else data.encode())
 print('Unit 4 practical kit:',path.stat().st_size,'bytes / 37 files');return str(path)

if __name__=='__main__':export()
