"""Export the already tested concise Redis kit; no running Redis required."""
import json
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'preview/DI04000031_unit5_practicals.zip'
README='''# DI04000031 · Unit 5 · Redis — concise practical kit

Required topics only: Strings, Lists, Sets, Hashes, basic commands,
MULTI/EXEC/DISCARD, expiry/caching, AI use cases and simple integration.
Practical 9 / CO5; 10 hours / 17% content weightage. No theory-paper marks.

## Run
1. Install Redis using the official instructions for your OS:
   https://redis.io/docs/latest/operate/oss_and_stack/install/
2. Use your OWN private, authenticated learning instance. Usual port: 6379.
3. Install the official Python client: python3 -m pip install -r requirements.txt
4. From this extracted folder: python3 ns5p01.py
   Enter your password at the hidden prompt.

Optional environment: REDIS_HOST, REDIS_PORT, REDIS_USERNAME, REDIS_PASSWORD.
For your authorized TLS endpoint use REDIS_TLS=1 and the correct secure port;
retain certificate verification. Never put passwords in shared source/URIs.
The published notes app is NOT a public Redis endpoint.

## Reference and output
Actually executed: Redis server/redis-cli 8.10.3, redis-py 8.1.0, Python 3.13.16,
Debian 13 x86_64. Source archive SHA256:
edde778f6bdee7581e42fc139ca9e07e2822212092f7501f99989656e3629d02
Verified against the official redis/redis-hashes list (not signature verification).
The private reference uses authenticated loopback port 6385, restricted lab ACLs,
no persistence and no optional modules. This is not production hardening/sizing.
No server binaries/passwords are included.

Each script really uses Redis. expected/*.txt records actual client outputs;
PING/SET success is true in Python, PONG/OK in redis-cli. Sets/hash fields are
sorted only for readable display. Temporal TTL is reported as an observed range,
not an invented exact countdown. Redis transactions do NOT roll back successful
commands on runtime errors; program 6 demonstrates the later successful SET.

The shared helper creates a fresh course-prefixed namespace and SET NX claim,
refuses collisions and removes ONLY its declared keys while checking ownership.
Never use FLUSHDB/FLUSHALL in a shared database. Interrupted/ambiguous runs need
inspection, not blanket cleanup. These are trusted prepared Python scripts,
NOT an arbitrary-code security sandbox or distributed-lock implementation.

Programs 01 keys/connect; 02 strings/TTL; 03 lists; 04 sets; 05 hashes;
06 transactions; 07 recommendation-cache IDs/invalidation; 08 cache-aside app.
Program 8's source is a LOCAL dictionary fixture, not a live MongoDB/Cassandra
connection. No AI training, cluster test, durability or speed benchmark is claimed.

20 files: 8 examples, 8 actual outputs, lab.py, requirements.txt, runtime.json,
and this README. Notes/diagrams/viva are in the unit preview/live app.
'''


def export(path=OUT):
    unit=json.loads((ROOT/'content/computer/sem4/DI04000031/unit5.json').read_text())
    files={'README.md':README,'lab.py':(ROOT/'tools/redis_lab_runner.py').read_text(),
        'requirements.txt':'redis==8.1.0\n','runtime.json':json.dumps(unit['runtime_evidence'],indent=2)+'\n'}
    for p in unit['programs']:
        files[p['id']+'.py']=p['code']['en']+'\n'
        files['expected/'+p['id']+'.txt']=p['out']+'\n'
    assert len(files)==20
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for name,text in files.items():
            info=zipfile.ZipInfo(name,(2026,10,29,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o644<<16;z.writestr(info,text.encode())
    print('Redis practical kit:',path.stat().st_size,'bytes / 20 files');return str(path)


if __name__=='__main__':export()
