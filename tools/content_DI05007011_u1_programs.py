"""Four small actual software examples, never presented as physical servicing."""
import subprocess,sys,tempfile,textwrap
from pathlib import Path
from subject_DI05007011 import ROOT,tr
HELPER=ROOT/'tools/hardware_u1_helper.py'
REFERENCE=ROOT/'tools/fixtures_DI05007011_u1/reference_specs.json'

def example(n,title,code,expl):
 return {'id':f'hw1p{n:02d}','title':tr(title),'code':tr(textwrap.dedent(code).strip()+'\n'),'expl':tr(expl)}
EXAMPLES=[
 example(1,'Actual read-only sandbox inventory — not a physical laptop specification',r'''
 import json
 from hardware_lab import environment_inventory

 print(json.dumps(environment_inventory(), sort_keys=True, indent=2))
 ''','Actually reads generic OS/kernel architecture, logical CPU count and exposed Linux MemTotal. These are sandbox-reported resources, not proof of physical CPU cores, installed DIMMs, laptop model, battery, ports, BIOS mode or the learner’s computer. No hostname, DMI serial, MAC address, firmware setting or device manipulation is queried.'),
 example(2,'Computed capacity units: GB is not GiB',r'''
 from hardware_lab import decimal_gb_to_gib

 print("16_GiB_bytes:", 16 * 1024 ** 3)
 print("512_decimal_GB_as_GiB:", round(decimal_gb_to_gib(512), 3))
 print("1_TB_decimal_bytes:", 10 ** 12)
 print("physical_drive_or_RAM_measured:", False)
 ''','Real arithmetic converts a declared512-billion-byte capacity to approximately476.837GiB and16GiB to17,179,869,184 bytes. This is a units exercise, not measurement of an installed device or a guarantee of usable formatted capacity. Manufacturer memory labels and filesystem overhead must not be guessed from this calculation.'),
 example(3,'Declared USB-C profiles: shape does not determine every feature',r'''
 from hardware_lab import connector_fixture

 profiles = [
     {"name": "Fictional A", "connector": "USB-C",
      "video_documented": False, "charging_documented": None},
     {"name": "Fictional B", "connector": "USB-C",
      "video_documented": True, "charging_documented": None}]
 for field, value in connector_fixture(profiles).items():
     print(field + ":", value)
 ''','Executes a logical check on two explicitly fictional specification rows, not a port probe. Both use USB-C while their declared video capability differs and charging is unspecified. This is not USB/Thunderbolt certification, cable testing, actual Power Delivery negotiation or a model-specific inference that an undocumented feature is absent.'),
 example(4,'Validate specification-sheet completeness, not hardware compatibility',r'''
 import json
 from pathlib import Path
 from hardware_lab import missing_spec_fields

 data = json.loads((Path(__file__).resolve().parent /
                    "reference_specs.json").read_text())
 for row in data["profiles"]:
     print(row["id"] + "_missing:", missing_spec_fields(row))
 draft = {"model": "Unverified student draft", "processor": "Model only"}
 print("draft_missing_count:", len(missing_spec_fields(draft)))
 print("compatibility_or_benchmark_proven:", False)
 ''','Actually checks the required CPU/memory/storage/GPU/display/ports/connectivity/OS/source/date fields in two dated manufacturer-listed reference profiles and an incomplete draft. Their first/base configurations were separately reviewed against official pages on29Oct2026. A complete row is not proof of physical ownership, worldwide latest status, local stock/price, compatibility, upgradeability or measured performance. The examples are Apple Silicon/macOS, not Windows x86 assembly/BIOS instructions.')]

def run_program(example):
 with tempfile.TemporaryDirectory(prefix='hardware-u1-example-') as td:
  folder=Path(td);(folder/'hardware_lab.py').write_text(HELPER.read_text());(folder/'reference_specs.json').write_text(REFERENCE.read_text())
  script=folder/(example['id']+'.py');script.write_text(example['code']['en'])
  r=subprocess.run([sys.executable,'-E',str(script)],cwd=folder,text=True,capture_output=True,timeout=10)
  assert r.returncode==0,(example['id'],r.stderr);assert not r.stderr,(example['id'],r.stderr)
 return dict(example,out=r.stdout)

def execute_all():return [run_program(p) for p in EXAMPLES]
