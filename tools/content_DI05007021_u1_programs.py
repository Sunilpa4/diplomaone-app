"""Six small executed illustrations: standard library + existing Linux utilities.
No programs execute on import; build/test calls run_program explicitly.
"""
import subprocess,sys,textwrap
from subject_DI05007021 import tr

def example(n,title,code,explanation):
 return {'id':f'sec1p{n:02d}','title':tr(title),'code':tr(textwrap.dedent(code).strip()+'\n'),
         'expl':tr(explanation)}

EXAMPLES=[
 example(1,'Integrity check against a trusted reference',r'''
 import hashlib

 original = b"Student S01: attendance=80"
 changed = b"Student S01: attendance=30"
 trusted_digest = hashlib.sha256(original).digest()

 def matches_reference(data):
     return hashlib.sha256(data).digest() == trusted_digest

 print("unchanged_matches:", matches_reference(original))
 print("changed_matches:", matches_reference(changed))
 print("sha256_bytes:", len(trusted_digest))
 ''','SHA-256 really hashes both byte strings. A mismatch detects this change only because the reference digest is trusted. A bare hash does not identify the sender, encrypt data or prevent an attacker replacing both message and digest.'),
 example(2,'Message integrity with HMAC — not encryption or a signature',r'''
 import hashlib
 import hmac
 import secrets

 secret = secrets.token_bytes(32)
 message = b"Student S01: attendance=80"
 changed = b"Student S01: attendance=30"
 tag = hmac.new(secret, message, hashlib.sha256).digest()

 def verifies(data):
     candidate = hmac.new(secret, data, hashlib.sha256).digest()
     return hmac.compare_digest(candidate, tag)

 print("original_verifies:", verifies(message))
 print("changed_verifies:", verifies(changed))
 print("tag_bytes:", len(tag))
 ''','The program genuinely computes and verifies HMAC-SHA256 with a fresh in-memory key that is never printed or saved. It illustrates integrity and authentication among key holders, not confidentiality, replay protection or public non-repudiation. This is a small supporting illustration, not an official Unit 1 cipher practical.'),
 example(3,'One private loopback TCP exchange',r'''
 import socket
 import threading

 def receive_exact(conn, count):
     data = bytearray()
     while len(data) < count:
         chunk = conn.recv(count - len(data))
         if not chunk:
             raise ConnectionError("Incomplete teaching message")
         data.extend(chunk)
     return bytes(data)

 with socket.socket() as listener:
     listener.bind(("127.0.0.1", 0))
     listener.listen(1)
     listener.settimeout(3)
     address = listener.getsockname()
     errors = []

     def serve_one():
         try:
             conn, _ = listener.accept()
             with conn:
                 conn.settimeout(3)
                 data = receive_exact(conn, 5)
                 conn.sendall(data)
         except Exception as error:
             errors.append(type(error).__name__)

     worker = threading.Thread(target=serve_one)
     worker.start()
     try:
         with socket.create_connection(address, timeout=3) as client:
             client.sendall(b"UNIT1")
             reply = receive_exact(client, 5)
     finally:
         worker.join(4)
     assert not worker.is_alive() and not errors, errors
     assert reply == b"UNIT1"
     print("loopback_only:", address[0] == "127.0.0.1")
     print("tcp_reply:", reply.decode())
     print("worker_stopped:", not worker.is_alive())
 print("listener_closed:", listener.fileno() == -1)
 ''','One real client connects to one private TCP listener on 127.0.0.1 and an OS-assigned port. The worker, client and listener finish inside the program. A successful exchange demonstrates this local service at that moment; plain TCP does not itself provide confidentiality or authenticate a user. It is not a DoS experiment or production server.'),
 example(4,'Inspect only the loopback interface and local route',r'''
 import json
 import subprocess

 def ip_json(*parts):
     result = subprocess.run(
         ["ip", "-j", *parts], check=True,
         text=True, capture_output=True, timeout=3)
     return json.loads(result.stdout)

 interface = ip_json("address", "show", "dev", "lo")[0]
 ipv4 = sorted(a["local"] for a in interface["addr_info"]
               if a["family"] == "inet")
 route = ip_json("route", "get", "127.0.0.1")[0]
 neighbors = ip_json("neigh", "show", "dev", "lo")
 print("interface:", interface["ifname"])
 print("administratively_up:", "UP" in interface["flags"])
 print("loopback_ipv4:", ",".join(ipv4))
 print("route_device:", route["dev"])
 print("loopback_neighbor_entries:", len(neighbors))
 ''','These are actual read-only iproute2 queries. Only the loopback interface, loopback route and its neighbour table are inspected, so no real network addresses are published. No ARP neighbour is needed for a loopback exchange. Interface state and routing do not prove application-level security.'),
 example(5,'Attempt one localhost ping and report its real status',r'''
 import re
 import subprocess

 result = subprocess.run(
     ["ping", "-n", "-c", "1", "-W", "2", "127.0.0.1"],
     text=True, capture_output=True, timeout=4)
 if result.returncode == 0:
     stats = re.search(r"(\d+) packets transmitted, (\d+) received",
                       result.stdout)
     assert stats and stats.groups() == ("1", "1")
     status = "one_local_echo_reply"
 elif "operation not permitted" in result.stderr.lower():
     status = "blocked_by_lab_permissions"
 else:
     raise RuntimeError("Unexpected ping failure: " + result.stderr)
 print("target: 127.0.0.1")
 print("requested_echoes: 1")
 print("observed_status:", status)
 ''','The reference sandbox actually denied the ping socket operation. The output records that denial; no successful ICMP reply is invented. On a machine with the required permissions the same bounded command may receive one reply instead. Missing replies alone cannot establish a DoS attack. Never use flood mode or public targets for this exercise.'),
 example(6,'Local name resolution and an owned listening socket',r'''
 import socket
 import subprocess

 def run(*args):
     return subprocess.run(args, check=True, text=True,
                           capture_output=True, timeout=3).stdout

 records = run("getent", "ahostsv4", "localhost")
 addresses = sorted({line.split()[0]
                     for line in records.splitlines() if line.strip()})
 with socket.socket() as listener:
     listener.bind(("127.0.0.1", 0))
     listener.listen(1)
     port = listener.getsockname()[1]
     rows = run("ss", "-ltnH", f"sport = :{port}")
     found = f"127.0.0.1:{port}" in rows
     print("localhost_ipv4:", ",".join(addresses))
     print("owned_listener_visible:", found)
 print("owned_listener_closed:", listener.fileno() == -1)
 ''','getent resolves localhost using the system name-service configuration (not necessarily DNS); ss reads the real kernel socket table for the program\'s own ephemeral port only. The socket closes on exit. No foreign hosts, processes or credentials are inspected. Windows ipconfig/netstat and DNS tools remain separately labelled guided commands.')]

def run_program(example):
 source=example['code']['en']
 compile(source,example['id'],'exec')
 result=subprocess.run([sys.executable,'-I','-c',source],text=True,capture_output=True,timeout=12)
 assert result.returncode==0,(example['id'],result.stderr)
 assert not result.stderr,(example['id'],result.stderr)
 return dict(example,out=result.stdout)

def execute_all():return [run_program(p) for p in EXAMPLES]
