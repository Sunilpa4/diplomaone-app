"""Export exact built MongoDB sources/real outputs without a DB dependency."""
import csv
import io
import json
from pathlib import Path
import zipfile
from content_DI04000031_u2_shared import STUDENTS

ROOT = Path(__file__).resolve().parent.parent
UNIT = ROOT / 'content/computer/sem4/DI04000031/unit2.json'
OUT = ROOT / 'preview/DI04000031_unit2_practicals.zip'

README = '''# DI04000031 · Unit 2 · MongoDB reference practicals

English-only GTU Computer Semester 4 material. Unit 2: 18 hours / 30% content
weightage; Practicals 2–3. This is a practical-only subject, not a fabricated
theory question paper. The full unit includes 20 lessons, 13 diagrams,
16 reference cards, 56 viva answers and 18 answered revision tasks.

## What was actually executed

All fourteen numbered/reference .js programs were executed using real MongoDB
Community Server 9.0.4 and mongosh 2.14.0 on Debian 13 x86_64. The server was a
private, authenticated, localhost-bound standalone. Sources are exactly the
ones displayed in the lesson, including their explicit seed records. Files
in expected/ contain captured real program output, not fabricated results.

No replica set, sharded cluster, failover or external application hosting was
configured/tested. Replication and sharding are conceptual syllabus topics.
The stock example contains sequential attempts, not a concurrent stress test
or a payment-plus-stock transaction. The index example forces plans with
hints and reports work counters, not a guaranteed wall-clock speedup.

## Contents

- examples/ns2p01.js ... ns2p14.js — independent mongosh scripts
- expected/ns2p01.txt ... ns2p14.txt — actual reference outputs
- run_lab.py — credential-free isolated execution/cleanup wrapper
- students.csv — synthetic six-student reference dataset, not an extra seed
- runtime.json — non-secret reference runtime/version/scope evidence

Each script includes its own required setup. Do NOT combine all seeds in one
already-populated collection. The CSV is for inspection; the scripts do not
need an additional import step.

## Installation and private connection (Practical 2)

1. Use a vendor-supported platform and the official instructions for that OS:
   https://www.mongodb.com/docs/manual/installation/
   https://www.mongodb.com/docs/mongodb-shell/install/
2. Install Community Server (mongod) and mongosh. Record both versions using
   `mongod --version` and `mongosh --version` in the operating-system terminal.
3. Start a private server. Bind to localhost; configure authentication. For a
   brand-new instance use the official localhost-exception procedure to create
   an initial administrator, using passwordPrompt() rather than a hardcoded
   password. Do not repeat this on an already initialized deployment.
4. Authenticate to your own authorized learning instance. Do not bind an
   unauthenticated database publicly or put private credentials in submissions.
5. Run ns2p01 for a ping plus a real collection/write/read check. A ping alone
   does not prove permission to read/write data.

A standard systemd installation can manage mongod as a service; the reference
sandbox instead used a process-managed server on port 27027. Select your OS
instructions rather than copying a Debian repository onto another release.
The recorded patch versions are reference evidence, not a timeless latest-
version or production-security recommendation.

## Execute an independent demo

Requirements: Python 3 (standard library), mongosh on PATH and a reachable,
authorized private MongoDB learning instance.

    python3 run_lab.py examples/ns2p04.js

The runner prompts for a private MongoDB connection URI without echoing it.
Alternatively supply MONGODB_URI through your private environment manager.
Do not paste a password-bearing URI into public notes or shell history.
For a cloud lab use only your own authorized teaching deployment and its
vendor-recommended TLS/network settings.

The runner creates a random `di04000031_u2_...` database, executes exactly the
selected script and drops only that captured scratch database in finally.
Your learning account therefore needs permission to create, use and drop
that scratch database. Such lab-administration access is NOT the recommended
privilege for a production application. If cleanup is interrupted by process
termination/network failure, ask the lab administrator to inspect only the
reported prefix-scoped scratch namespaces; never bulk-drop real databases.

For manual execution instead, select a newly created, authorized disposable
database beginning `di04000031_u2_`, run one script and clean up only your own
lab context. The prefix guard is not authorization or a backup. Follow your
instructor's account/cleanup policy.

## Program map

01 connection, database context, create/drop collection, stored round-trip
02 BSON types, ObjectId/string mismatch and fixed UTC Date
03 insertOne/insertMany, acknowledged writes and duplicate _id error 11000
04 $gt/$lt/$in/$and/$or and implicit AND
05 stable sort, limit, inclusion/exclusion projection, cursor and null findOne
06 array membership, nested dot notation and whole-object equality
07 updateOne/updateMany, $set/$inc, real/no-op/missing result counts
08 explicit upsert and field-removing replaceOne
09 targeted deletes, missing record and remaining IDs
10 embedding, explicit reference lookup and missing reference
11 compound/unique indexes, forced explain counters and duplicate email
12 $match/$group/$sum/$avg aggregation with unchanged source rows
13 small document catalog and guarded single-document stock decrement
14 null/missing/type pitfalls, invalid projection/update and scalar validation

## Interpreting results and safety

- Sorting and fixed IDs/dates make the reference outputs reproducible. Server
  version strings, error details and explain counters can differ with another
  version, plan or dataset. Investigate differences; do not edit output to fake
  agreement.
- `find` returns a cursor; `toArray()` is used for small bounded fixtures only.
- `matchedCount` differs from `modifiedCount`; zero deletion can be a missing
  record rather than a database failure.
- Single-document writes are atomic; a whole insertMany/updateMany batch or
  separate payment/stock documents are not automatically one transaction.
- The stored references are not automatic relational foreign keys.
- Prices in the mini-catalog are integer paise; demo order amounts are small
  integers, not a general floating-point currency design.
- Inputs are synthetic. Keep credentials, personal data and production backups
  out of this folder and version control.

Journal: record aim, actual platform/versions, authorized connection and
storage proof, fresh scratch context, input/commands/observed output, negative
cases, design decisions, cleanup, conclusion and official sources.
'''


def export(path=OUT):
    unit = json.loads(UNIT.read_text(encoding='utf-8'))
    buffer = io.StringIO(newline='')
    writer = csv.writer(buffer)
    writer.writerow(['_id', 'name', 'age', 'city', 'marks', 'active', 'skills', 'state', 'pin'])
    for r in STUDENTS:
        writer.writerow([r['_id'], r['name'], r['age'], r['city'], r['marks'],
                         str(r['active']).lower(), '|'.join(r['skills']),
                         r['address']['state'], r['address']['pin']])
    files = {'README.md': README,
             'run_lab.py': (ROOT / 'tools/mongodb_lab_runner.py').read_text(),
             'students.csv': buffer.getvalue(),
             'runtime.json': json.dumps(unit['runtime_evidence'], indent=2) + '\n'}
    for p in unit['programs']:
        files['examples/' + p['id'] + '.js'] = p['code']['en'] + '\n'
        files['expected/' + p['id'] + '.txt'] = p['out'] + '\n'
    path = Path(path); path.parent.mkdir(exist_ok=True, parents=True)
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, text in files.items():
            # Stable timestamps make the archive deterministic too.
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 29, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, text.encode('utf-8'))
    print('MongoDB practical download:', path, path.stat().st_size, 'bytes /', len(files), 'files')
    return str(path)


if __name__ == '__main__': export()
