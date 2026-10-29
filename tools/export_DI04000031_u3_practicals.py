"""Export exact built CQL sources and real outputs; no database dependency."""
import json
from pathlib import Path
import zipfile
from content_DI04000031_u3_shared import CSV

ROOT = Path(__file__).resolve().parent.parent
UNIT = ROOT / 'content/computer/sem4/DI04000031/unit3.json'
OUT = ROOT / 'preview/DI04000031_unit3_practicals.zip'

README = '''# DI04000031 · Unit 3 · Wide-Column Databases: Cassandra

English-only GTU Computer/CSE Semester 4, effective 2025–26.
12 hours / 20% content weightage. Practicals 4–6; CO3: design and implement
distributed datasets using Cassandra’s data model and CQL.
Practical PA 20 + ESE 30 = 50; no theory ESE/PA or invented theory-paper marks.

## Actual reference execution and honest boundaries

All fourteen CQL files were executed against real Apache Cassandra 5.0.9.
The runtime used cqlsh 6.2.0, CQL 3.4.7, the bundled Python driver 3.29.0,
Python 3.13.16 and Temurin Java 17.0.21+9 on Debian 13 x86_64.
The server was private, localhost-bound and authenticated; factory access was
rotated/disabled. The native protocol was explicitly v4 for this client run.

There was ONE physical Cassandra node, with datacenter1 / RF 1 for these lab
keyspaces. Four logical device/day partitions are real query results, NOT
four machines or proof of replicated/multi-node placement. No failover,
cluster-operations lab, external hosting, throughput or latency guarantee is
claimed. Only read-only nodetool status was observed (one local UN node).

Result rows in expected/ are from the actual server, JSON-serialized without
client sorting. Dates/UUIDs become display strings; timestamps are ISO UTC.
The negative examples capture actual server InvalidRequest/SyntaxException
classes. The @result/@expect lines are ordinary comments interpreted by the
runner; they are not new CQL syntax or mocked server behaviour.

COPY is a cqlsh special command: the runner invokes the actual matching
cqlsh for it, not a pretend driver implementation. Its changing timing/rate
text is omitted; completion and the subsequent stored-data verification are
real. All eight stored full keys/values/times were compared with sensors.csv.

## Bundle contents (32 files)

- examples/ns3p01.cql ... ns3p14.cql — complete independent CQL scripts
- expected/ns3p01.txt ... ns3p14.txt — actual captured reference outputs
- run_lab.py — guarded real-driver runner, delegating COPY to actual cqlsh
- sensors.csv — eight SYNTHETIC readings in four device/day partitions
- runtime.json — non-secret version/scope/fixture verification evidence
- README.md — this guide

No passwords, database files, Java binaries or driver packages are included.

## Install and authorize your own private learning instance (Practical 4)

1. Select your platform/release and follow:
   https://cassandra.apache.org/doc/5.0.9/cassandra/installing/installing.html
   https://cassandra.apache.org/doc/5.0.9/cassandra/managing/operating/security.html
2. Use supported Java for that server and Python for its matching cqlsh.
   Cassandra 5.0 documentation specifies Java 11 or 17. The exact 5.0.9 client
   was tested with Python 3.13.16; do not assume older clients support it.
3. Download an official release and verify its published checksum. The
   reference Apache tarball was SHA-512 verified and its Java runtime archive
   SHA-256 verified. Recorded patch versions are reference evidence, not a
   timeless latest-version or security-hardening claim.
4. Before launch, keep CQL, internode and management/JMX interfaces private.
   Enable appropriate authentication/authorization. Rotate/disable factory
   access through an authorized private bootstrap procedure. Do not expose
   default credentials or an unauthenticated database on public interfaces.
5. Start by your package’s service procedure or `bin/cassandra -f` for a
   tarball. Do not start a second server on the same data directory.
6. Record Java/Python/server/cqlsh versions, connect as your own lab account
   and verify an authorized stored write/read round-trip (ns3p01).

These exact reference scripts assume the ACTUAL DC name is datacenter1 and
use NetworkTopologyStrategy with RF 1 for a single-node lab. First verify
`SELECT data_center FROM system.local WHERE key='local';`. If your instructor’s
DC differs, adapt the explicit replication maps and client policy deliberately;
do not pretend increasing RF creates more machines.

The reference used port 9043; Cassandra’s usual native CQL default is 9042.
GTU recommends an 8 GB learning computer. The constrained reference’s tiny
512 MiB heap is not production sizing/tuning advice.

## Run a complete example safely

Requirements: Python, a compatible real Python Cassandra driver and a
reachable private learning server. Preferred: use the driver/pyasyncore
bundled in the official distribution by setting CASSANDRA_HOME to its root.
The scripts do not download packages or use an emulator.

    export CASSANDRA_HOME=/path/to/apache-cassandra-5.0.9
    python3 run_lab.py examples/ns3p06.cql --port 9043 --username YOUR_LAB_USER

The password is prompted without echo. An optional private environment manager
can provide CASSANDRA_USERNAME/CASSANDRA_PASSWORD. Never paste a real password
into a public command, notebook, history or submission. The runner uses a
short-lived permission-0600 credentials file for its actual cqlsh COPY call.

The account needs authority to create/use/drop these lab keyspaces. Such lab
administration privilege is NOT a production application role recommendation.
This reference runner targets a local private learning instance, not an
unreviewed production/cloud connection or general TLS/security configuration.

Each complete file creates its own `di04000031_u3_ns3pXX` keyspace and drops it.
The runner refuses a pre-existing namespace, marks ownership only after its
CREATE succeeds and uses the captured name in finally cleanup. A failed
CREATE cannot cause this runner to drop somebody else’s keyspace. Do not
remove this safeguard or bulk-drop matching names after interrupted runs.

If running manually in cqlsh, inspect a new authorized disposable namespace
first and STOP after any unexpected setup error. Do not feed the entire file
into an existing keyspace: a shell may continue after a failed CREATE and
later execute the DROP footer. Prefer the guarded runner for these complete
teaching scripts. A prefix is not authorization, a backup or a security parser.

## Dataset and Practical 6

Run ns3p12 from this bundle’s root (or pass --fixtures with the folder holding
sensors.csv). That example creates an empty table and ACTUALLY imports the
file with matching cqlsh. It does not have an extra hidden insert seed.

- S01 / 2026-10-29: 30,31,32 at 09:00/09:01/09:02 UTC (3 rows)
- S02 / 2026-10-29: 28,29 at 09:00/09:01 UTC (2 rows)
- S01 / 2026-10-30: 33,34 at 09:00/09:01 UTC (2 rows)
- S03 / 2026-10-29: 27 at 09:00 UTC (1 row)

DATETIMEFORMAT uses %z to parse the explicit UTC Z suffix. A processed-row
message alone is insufficient: wrong time parsing or duplicate full keys can
upsert several inputs into fewer rows. Check the actual eight stored rows,
every full key/value/time, four logical partition keys and latest S01/day29
09:02 -> 32.0. The CSV is synthetic, not real personal data or live hardware.

## Program map

01 connection/system versions, keyspace create/alter/drop, storage round-trip
02 typed int/text/timestamp/date/boolean/double/uuid record
03 composite partition key and ordered rows in four logical partitions
04 INSERT upsert with retained omitted existing values
05 WHERE equality, IN, selected columns and missing-key empty results
06 default/reversed clustering order, half-open time range and LIMIT
07 UPDATE existing data and creation from a missing key
08 cell/row/partition DELETE scopes and observed read-back
09 ALTER TABLE add/drop regular field/comment and DROP TABLE
10 two query-shaped tables and an explicit stale-copy correction
11 rejected non-key queries, LIMIT not fixing them, bounded ALLOW FILTERING
12 actual cqlsh CSV import and full stored-key/value/time verification
13 bounded per-partition count/sum/avg/min/max analytical features
14 actual server type/null-key/order/key-mutation/syntax rejections

## Interpretation and journal

- CQL is not general SQL: no arbitrary joins/subqueries or global ORDER BY
  any field. IN output across partitions is not a lexical ordering promise.
- A normal INSERT/UPDATE upserts, not a MongoDB duplicate-ID/matched-count
  operation. Omitted existing columns are not whole-row replacement.
- Key choice determines access and growth; a daily bucket is not safe at every
  write rate. Large scans/IN fan-out and ALLOW FILTERING need deliberation.
- The two query tables do not correct themselves atomically. A 32 -> 35 base
  correction leaves a stale 32 in the second until its explicit second write.
- Simple aggregates are possible report/model input features, not trained AI.
  S01/day29: count 3, total 93, mean 31, min 30, max 32. Other means: 28.5,
  33.5 and 27.0. This does not benchmark cluster-wide real-time analytics.
- Tombstones are logical deletion; disappearance from a read is not immediate
  physical disk erasure. No repair/compaction/decommission procedure is taught.
- nodetool awareness: U/D = Up/Down; N/L/J/M = Normal/Leaving/Joining/Moving.
  UN is one signal, not all application/backup/availability guarantees.
- Preserve actual observations. Other versions/data may change output order
  or details; investigate rather than editing expected files to fake agreement.

Journal: aim/practical number, actual setup/versions, authorized round-trip,
query requirements -> key rationale, input/CQL/CSV/observed output, negative
cases, full dataset checks, arithmetic, single-node evidence boundary,
read-only health interpretation, owned cleanup, conclusion and official sources.
'''


def export(path=OUT):
    unit = json.loads(UNIT.read_text())
    files = {'README.md': README,
             'run_lab.py': (ROOT / 'tools/cassandra_lab_runner.py').read_text(),
             'sensors.csv': CSV,
             'runtime.json': json.dumps(unit['runtime_evidence'], indent=2) + '\n'}
    for p in unit['programs']:
        files['examples/' + p['id'] + '.cql'] = p['code']['en'] + '\n'
        files['expected/' + p['id'] + '.txt'] = p['out'] + '\n'
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, text in files.items():
            info = zipfile.ZipInfo(name, (2026, 10, 29, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED; info.external_attr = 0o644 << 16
            z.writestr(info, text.encode('utf-8'))
    print('Cassandra practical download:', path, path.stat().st_size, 'bytes /', len(files), 'files')
    return str(path)


if __name__ == '__main__': export()
