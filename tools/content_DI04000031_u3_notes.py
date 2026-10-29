"""Cassandra Unit 3: eighteen English lessons, Practicals 4–6 and CO3.
No official theory question paper or cluster-operations lab is invented.
"""
from nosql_content import make_T, table

BASE = 'https://cassandra.apache.org/doc/5.0.9/cassandra/'
SOURCES = [
    ('GTU DI04000031 syllabus, effective 2025–26', 'https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf'),
    ('Apache Cassandra official downloads', 'https://cassandra.apache.org/_/download.html'),
    ('Installing Cassandra 5.0.9', BASE + 'installing/installing.html'),
    ('CQL data definition: keyspaces, keys and tables', BASE + 'developing/cql/ddl.html'),
    ('CQL data manipulation: reads and writes', BASE + 'developing/cql/dml.html'),
    ('CQL data types', BASE + 'developing/cql/types.html'),
    ('Query-first Cassandra versus relational modeling', BASE + 'developing/data-modeling/data-modeling_rdbms.html'),
    ('Physical data-model design', BASE + 'developing/data-modeling/data-modeling_physical.html'),
    ('cqlsh commands, credentials and COPY', BASE + 'managing/tools/cqlsh.html'),
    ('nodetool status: read-only cluster information', BASE + 'managing/tools/nodetool/status.html'),
    ('Cassandra security and network boundaries', BASE + 'managing/operating/security.html'),
    ('CQL built-in aggregate functions', BASE + 'developing/cql/functions.html'),
]

SN = {
    'versions': '''# Operating-system terminal, from the extracted release:
java -version
python3 --version
bin/cassandra -v
bin/cqlsh --version''',
    'private_yaml': '''# Private learning instance only: cassandra.yaml settings
listen_address: 127.0.0.1
rpc_address: 127.0.0.1
native_transport_port: 9043
authenticator: PasswordAuthenticator
authorizer: CassandraAuthorizer
# Keep internode and local JMX access private too.
# This is not a complete production/TLS configuration.''',
    'start': '''# Terminal A, after private settings and Java compatibility:
# Run from the extracted Cassandra distribution.
bin/cassandra -f
# A package installation may use the OS service manager.
# Do not start two servers against the same data directory.''',
    'connect': '''# Terminal B: your own authorized private lab account.
bin/cqlsh 127.0.0.1 9043 -u YOUR_LAB_USER --disable-history
# Enter the password at the hidden prompt; never use -p SECRET.
# Default native CQL port is 9042; the reference uses 9043.''',
    'shell': '''-- Inside cqlsh, not in the operating-system terminal:
SHOW VERSION;
SHOW HOST;
DESCRIBE KEYSPACES;
SELECT release_version, cql_version, data_center
FROM system.local WHERE key='local';''',
    'keyspace': '''-- Fresh disposable lab namespace; never a production keyspace.
CREATE KEYSPACE di04000031_u3_manual
WITH replication = {'class':'NetworkTopologyStrategy',
                    'datacenter1':1};
USE di04000031_u3_manual;
ALTER KEYSPACE di04000031_u3_manual WITH durable_writes=true;
-- After your lab, drop ONLY the namespace you created:
-- USE system;
-- DROP KEYSPACE di04000031_u3_manual;''',
    'keys': '''PRIMARY KEY (device_id, day, reading_at)
-- Partition key: device_id
-- Clustering columns: day, reading_at

PRIMARY KEY ((device_id, day), reading_at)
-- Composite partition key: device_id AND day together
-- Clustering column: reading_at''',
    'schema': '''CREATE TABLE readings_by_device_day (
  device_id text, day date, reading_at timestamp,
  temperature_c double, status text,
  PRIMARY KEY ((device_id, day), reading_at)
) WITH CLUSTERING ORDER BY (reading_at DESC);''',
    'typed': '''-- Sample literals, not a complete INSERT statement:
int:       82
text:      'Asha'
boolean:   true
date:      '2026-10-29'
timestamp: '2026-10-29T09:00:00Z'
uuid:      11111111-1111-4111-8111-111111111111
text with apostrophe: 'Asha''s sensor' ''',
    'where': '''SELECT name, city FROM learners_by_id WHERE learner_id=2;
SELECT learner_id, name FROM learners_by_id
WHERE learner_id IN (1,3);
-- A missing key returns an empty result set, not a new row.''',
    'range': '''SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29'
  AND reading_at >= '2026-10-29T09:00:00Z'
  AND reading_at <  '2026-10-29T09:02:00Z';

SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29'
ORDER BY reading_at ASC LIMIT 2;''',
    'upsert': '''-- Assumes the learners_by_id schema in the independent demo.
INSERT INTO learners_by_id (learner_id, name)
VALUES (1, 'Asha Patel');
-- Same key: supplied name changes; existing city/marks remain.

UPDATE learners_by_id SET name='Jai', marks=68
WHERE learner_id=99;
-- Missing key: normal UPDATE can create a row.''',
    'update': '''UPDATE learners_by_id SET city='Surat', marks=75
WHERE learner_id=2;
-- Read back; CQL does not return matchedCount/modifiedCount.
SELECT name, city, marks FROM learners_by_id WHERE learner_id=2;
-- marks=marks+5 is NOT ordinary int arithmetic in CQL.
-- Counter columns are a separate feature with restrictions.''',
    'delete': '''DELETE city FROM learners_by_id WHERE learner_id=1;
DELETE FROM learners_by_id WHERE learner_id=2;
DELETE FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29'
  AND reading_at='2026-10-29T09:02:00Z';
DELETE FROM readings_by_device_day
WHERE device_id='S02' AND day='2026-10-29';''',
    'alter': '''ALTER TABLE learner_schema ADD city text;
ALTER TABLE learner_schema WITH comment='Small schema-change lab';
ALTER TABLE learner_schema DROP city;
DROP TABLE learner_schema;
-- Requires the disposable table created in the full demo.
-- These are separate changes, not a primary-key migration.''',
    'filter': '''-- Expected rejection: no suitable index/query-first key here.
SELECT device_id, temperature_c FROM readings_by_device_day
WHERE temperature_c > 30.0 LIMIT 1;

-- Tiny fixture only: three rows in this selected partition.
SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29'
  AND temperature_c > 30.0 ALLOW FILTERING;''',
    'copy': '''-- cqlsh-only command, from the folder with sensors.csv:
COPY readings_by_device_day
  (device_id, day, reading_at, temperature_c, status)
FROM 'sensors.csv' WITH HEADER=TRUE AND NUMPROCESSES=1
  AND DATETIMEFORMAT='%Y-%m-%dT%H:%M:%S%z'
  AND MAXPARSEERRORS=0 AND MAXINSERTERRORS=0
  AND MINBATCHSIZE=1 AND MAXBATCHSIZE=1;
-- Verify stored row count AND timestamps, not just import progress.''',
    'features': '''SELECT count(*) AS samples, sum(temperature_c) AS total,
  avg(temperature_c) AS mean, min(temperature_c) AS minimum,
  max(temperature_c) AS maximum
FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29';''',
    'nodetool': '''# OS terminal; read-only awareness, not a repair procedure:
bin/nodetool -h 127.0.0.1 -p 7199 status
# U = Up, D = Down
# N = Normal, L = Leaving, J = Joining, M = Moving
# Reference observation: one UN local node.
# UUID/load/ownership figures are environment-dependent.''',
    'journal': '''Aim and official practical number
Actual OS / Java / Python / Cassandra / cqlsh versions
Authorized private connection + stored write/read evidence
Query requirements -> partition and clustering key rationale
CQL / CSV input, actual output, negative cases
Eight stored rows, four logical partitions, correct UTC times
Bounded analytic calculation and AI/IoT relevance
Read-only health interpretation; single-node evidence limit
Owned scratch cleanup; no credentials in submission
Conclusion and official references''',
}
T = make_T(SN)

S1 = {'title': {'en': '3.1 Cassandra Foundations, Architecture and Keys'}, 'items': [
    T('Cassandra Uses, Query-First Thinking and Peer Architecture', '''
<p><b>Apache Cassandra</b> is a distributed wide-column database suited to partition-oriented workloads such as sensor histories, application events and high-write-volume telemetry. CQL exposes typed tables; “wide-column” does not mean it is a columnar analytical warehouse.</p>
<p><b>Query first:</b> write the required reads before choosing keys. “Latest readings for one device on one day” suggests a device/day partition and a time clustering column. Cassandra is not a drop-in SQL engine with arbitrary joins, subqueries and free sorting of every column.</p>
<p><b>Architecture, conceptually:</b> peers own token ranges; a contacted node can coordinate an operation and communicate with replicas. There is no mandatory single write-primary for the whole Cassandra cluster. Partitioning decides data subsets; replication maintains additional copies. Replication/consistency settings affect guarantees—avoid a universal product-wide CP/AP slogan or a claim of perfect availability.</p>
<p><b>CO3:</b> design and implement distributed datasets using Cassandra’s data model and CQL. Practicals 4–6 cover setup, query-shaped CRUD and an AI-related dataset.</p>
<p><b>Actual reference:</b> real Cassandra 5.0.9, cqlsh 6.2.0, CQL 3.4.7, Python 3.13.16 and Temurin Java 17.0.21+9 on Debian 13 x86_64. Fourteen CQL scripts were executed on one private authenticated node. Logical partition results are real; multi-machine distribution, replication failover, production capacity and external hosting were not tested.</p>
''', diagram='ns3_arch'),
    T('Keyspace → Table → Partition → Row → Typed Column', '''
<p>A <b>keyspace</b> is a namespace for tables and defines options such as replication policy and durable writes. A <b>table</b> defines columns and a primary-key layout. A <b>partition</b> contains rows sharing the complete partition-key value.</p>
''' + table(['Level', 'Sensor-history example'], [
    ['Keyspace', 'One disposable di04000031_u3_... lab namespace'],
    ['Table', 'readings_by_device_day'],
    ['Partition', '(S01, 2026-10-29)'],
    ['Row within partition', 'One reading_at timestamp, such as 09:01 UTC'],
    ['Regular column', 'temperature_c double; status text'],
]) + '''
<p>Partitions are logical data units; a node may store many partitions and a partition may have replicas. The reference has four logical device/day partitions but only one physical node. Four partitions are not four machines or four copies.</p>
<p>Keyspaces/tables do not appear merely because a shell connects. Use explicit DDL, verify it with read-only system schema or DESCRIBE, and make an authorized stored-data round-trip. Do not modify system keyspaces.</p>
''', diagram='ns3_hierarchy'),
    T('Partition Key versus Clustering Columns: Parentheses Matter', '''
<p>A complete <b>primary key</b> uniquely identifies a logical row. Its first component is the partition key; the remaining components are clustering columns. Extra parentheses make a multi-column composite partition key.</p>
@@keys@@
<p>For PRIMARY KEY ((device_id,day),reading_at), both device and day must match to select the intended partition. Different days for S01 form different partitions; time orders rows inside each one. In PRIMARY KEY (device_id,day,reading_at), day is instead the first clustering column inside a device-only partition.</p>
<p><b>Growth matters:</b> time bucketing bounds history only relative to the actual write rate and record size. Two readings/minute produce 2,880 readings/day; a much faster stream may need smaller buckets or another deliberate design. Estimate size, query load and skew—“one day” is not automatically safe at every rate.</p>
<p><b>Identity:</b> two samples with exactly the same full key upsert the same row. If several events can share a millisecond timestamp, consider a justified tie-breaker and its query implications. SET cannot mutate the key into a new identity; key-layout changes require a new model/migration.</p>
''', diagram='ns3_keys'),
]}

S2 = {'title': {'en': '3.2 Installation and cqlsh — Practical 4'}, 'items': [
    T('Install a Compatible Private Server and Matching cqlsh', '''
<ol><li><b>Identify platform:</b> follow the selected release’s official Linux/package/tarball instructions. On Windows, use an instructor-approved Linux/WSL2 or container environment rather than assuming a native Windows server install; only the Debian reference was tested here.</li>
<li><b>Check prerequisites:</b> Cassandra 5.0 documentation specifies Java 11 or 17; the reference deliberately uses patched Temurin 17.0.21+9, not an unrelated Java default. Use a Python version supported by the bundled cqlsh. The actual 5.0.9 client was verified with Python 3.13.16; do not assume older cqlsh packages support it.</li>
<li><b>Obtain official binaries:</b> download the selected release and verify its published checksum before extracting. The reference Apache 5.0.9 tarball was SHA-512 verified; its Java runtime archive was SHA-256 verified. These identify the tested run, not a timeless latest-release claim.</li>
<li><b>Configure private access before starting:</b> keep CQL, internode and management/JMX interfaces private; enable appropriate authentication/authorization. Do not expose factory defaults or an unauthenticated server publicly.</li>
<li><b>Initialize authorized lab access:</b> on a brand-new private instance, use the vendor’s administrative role procedure to create unique private credentials, verify the new login, then rotate/disable the factory role. The reference did so before any teaching scripts; no private password is shipped.</li>
<li><b>Start and connect:</b> use the service manager for your package, or a foreground process for a tarball. Record versions and verify a real authorized write/read, not only a client executable.</li></ol>
@@versions@@
@@private_yaml@@
@@start@@
<p><b>Resource boundary:</b> GTU recommends an 8 GB learning computer. The reference used a reduced 512 MiB Java heap for tiny synthetic fixtures in a constrained sandbox; this is not a production sizing or tuning recommendation. Binaries, database state and credentials stayed outside the project in an excluded private cache.</p>
''', diagram='ns3_setup'),
    T('Connect with cqlsh and Create/Alter/Drop Keyspaces', '''
<p><b>cqlsh</b> is a client shell, not the database server. Use the client bundled with the chosen Cassandra release, because cross-version compatibility is not universally guaranteed. Enter a private password at a prompt or use a correctly permissioned private credentials file; never submit a password-bearing command, file or history.</p>
@@connect@@
@@shell@@
<p>The authenticated reference SHOW VERSION reported <b>cqlsh 6.2.0 | Cassandra 5.0.9 | CQL spec 3.4.7 | Native protocol v4</b>. Native protocol version 4 was explicitly selected for this client run; it is not the Cassandra product version.</p>
@@keyspace@@
<p><b>Replication map:</b> NetworkTopologyStrategy refers to the actual datacenter name, verified as datacenter1 here. RF 1 fits the single-node lab and offers no extra replica for node loss. Do not copy a DC name or raise RF and pretend it creates machines/copies by itself. durable_writes=true retains commit-log use; this lab does not disable durability.</p>
<p><b>Shell versus CQL:</b> SHOW, DESCRIBE, COPY and SOURCE are cqlsh commands; application drivers send native CQL statements. CQL uses semicolons, single-quoted string values and typed column definitions.</p>
<p><b>Safety:</b> each full example creates a distinct di04000031_u3_ namespace. Use the supplied runner: it refuses a pre-existing name, marks ownership only after successful CREATE and drops only that captured namespace. A prefix alone is neither authorization nor a backup. If running manually, stop immediately after an unexpected CREATE/setup error—do not continue into an existing keyspace and its DROP footer.</p>
''', programs=['ns3p01']),
]}

S3 = {'title': {'en': '3.3 Typed CQL DDL and Safe Schema Changes'}, 'items': [
    T('CREATE TABLE, Basic Types and UTC Values', '''
<p>CQL is a <b>typed</b> language. Define column types and the primary key explicitly; a wrong int literal is not silently accepted as a different string identifier.</p>
@@schema@@
@@typed@@
''' + table(['Type', 'Purpose / care'], [
    ['int / bigint', 'Signed 32-bit / 64-bit integers; choose a suitable range.'],
    ['text', 'UTF-8 text; string values use single quotes.'],
    ['timestamp', 'Date and time with millisecond precision; include an explicit zone.'],
    ['date', 'Calendar date without a time-of-day component.'],
    ['boolean / double', 'true/false and approximate binary fractional numeric data.'],
    ['uuid', 'An identifier value; a UUID is not necessarily a time-sorting timeuuid.'],
]) + '''
<p>Unquoted identifiers are case-insensitive/lowercased in normal CQL usage; double quotes name identifiers rather than ordinary string values. Escape a string apostrophe by doubling it. Primary-key components cannot be null.</p>
<p>The typed example stores a fixed UUID and UTC timestamp. Its JSON display converts dates/UUIDs to strings and timestamps to ISO UTC; these formatting choices do not change the stored CQL types. Use an appropriate exact numeric policy for money rather than assuming double is exact currency.</p>
''', programs=['ns3p02']),
    T('ALTER TABLE, New Null Values and DROP TABLE', '''
<p><b>CREATE TABLE</b> defines a new schema; <b>ALTER TABLE ADD</b> adds a regular column. Existing rows do not acquire invented default data: the example’s newly added city reads as null until it is written.</p>
@@alter@@
<p>The executable example creates its disposable table first, adds/writes/removes city, changes a comment and verifies schema metadata after DROP. A successful ALTER command is not proof that applications have migrated their data or validation rules.</p>
<p><b>Key limitation:</b> do not treat ALTER as arbitrary repartitioning. Adding a primary-key component or changing a partition key is not an in-place data-model edit. Primary-key-column rename support changes a name, not which data is grouped together. Plan a new table and controlled migration when access requirements change.</p>
<p><b>Destruction:</b> dropping a regular column removes that column’s data logically; dropping a table removes the table; dropping a keyspace removes all its contents. Do not experiment with these commands in system or real application namespaces, and do not assume they provide an undo action.</p>
''', programs=['ns3p09']),
]}

S4 = {'title': {'en': '3.4 CQL CRUD and Partition-Oriented Queries — Practical 5'}, 'items': [
    T('INSERT and the Default Upsert Rule', '''
<p>A normal Cassandra <b>INSERT is an upsert</b>: a new complete primary key creates a row; an existing key writes the specified regular columns. It does not normally throw a duplicate-key error, and it is not whole-row replacement.</p>
@@upsert@@
<p>For learner 1, name becomes Asha Patel but existing Surat/82 remain. Inserting learner 4 with just a name creates a row with city/marks null. Repeating a complete row identity does not create another logical row with that key.</p>
<p>Conditional clauses such as IF NOT EXISTS/IF EXISTS use different lightweight-transaction semantics and have costs; they are not implicit in these basic operations. Ordinary writes do not return MongoDB-style matchedCount, modifiedCount or deletedCount, so query the intended state and handle errors deliberately.</p>
''', diagram='ns3_upsert', programs=['ns3p04']),
    T('SELECT Projection, WHERE Equality and Bounded IN', '''
<p><b>SELECT</b> retrieves the named columns. Use WHERE with the designed key rather than assuming every regular field can be filtered like SQL.</p>
@@where@@
<p>The fixture returns Ravi/Bharuch for ID 2, names for IDs 1 and 3, and no rows for 999. Selecting only needed columns reduces returned data; it does not modify storage or implement authorization.</p>
<p>IN on supported key positions can select multiple known values, but large lists may fan out to many partitions. Do not rely on IN result order as a global lexical/marks order. For composite partition keys, supply the intended values of every component; for multiple clustering columns, respect their left-to-right restrictions.</p>
<p>CQL is SQL-like but does not provide general joins/subqueries or unrestricted OR-style ad-hoc predicates. Use the documented CQL syntax and design another access table when the required read does not fit the key.</p>
''', programs=['ns3p05']),
    T('Inspect the Eight-Reading Fixture and Four Logical Partitions', '''
<p>The synthetic sensor data is fixed, reproducible and not measured from live devices. The default time order within a partition is descending. Every independent sensor example includes its seed explicitly, except the CSV example, which actually imports its supplied file.</p>
''' + table(['Device / day', 'UTC minute → temperature °C'], [
    ['S01 / 2026-10-29', '09:00 → 30.0; 09:01 → 31.0; 09:02 → 32.0'],
    ['S02 / 2026-10-29', '09:00 → 28.0; 09:01 → 29.0'],
    ['S01 / 2026-10-30', '09:00 → 33.0; 09:01 → 34.0'],
    ['S03 / 2026-10-29', '09:00 → 27.0'],
]) + '''
<p>The partition row counts are 3, 2, 2 and 1, totaling 8. SELECT DISTINCT device_id,day lists the four partition-key values, not four server addresses. Hash/token placement is not alphabetical ordering of the device IDs.</p>
<p><b>Observed versus inferred:</b> the reference queries really retrieve the selected partitions, but they all reside on one physical local node with RF 1. This simulates partition-oriented dataset design; it is not an experiment proving distribution over a multi-node cluster.</p>
''', diagram='ns3_partitions', programs=['ns3p03']),
    T('WHERE Time Ranges, Clustering ORDER BY and LIMIT', '''
<p>For a device/day partition, use the clustering timestamp to select a contiguous time interval. The table specifies reading_at DESC; the latest two readings are therefore 32.0 at 09:02 followed by 31.0 at 09:01.</p>
@@range@@
<p>The half-open interval [09:00,09:02) returns 31.0 and 30.0 in descending clustering order. Reversing to ASC with LIMIT 2 returns 30.0 then 31.0. Include a timezone; “09:00” without a zone can be ambiguous across machines.</p>
<p><b>ORDER BY is constrained:</b> it uses permitted clustering order (or its supported reverse) with the required key restrictions. It is not “sort any field in any table.” With multiple clustering columns, their declared sequence matters.</p>
<p><b>LIMIT:</b> controls returned row count; it does not build an index, fix an invalid WHERE or guarantee a fixed number of underlying reads. Avoid unbounded full-table reads merely because this eight-row fixture is small.</p>
''', diagram='ns3_query', programs=['ns3p06']),
    T('UPDATE, Missing Rows and the Correct Key Scope', '''
@@update@@
<p>The observed Ravi update reads back Surat/75. A separate UPDATE of missing learner 99 stores Jai/68 with city null: normal UPDATE can create data. Do not interpret success as proof that the row existed before the write.</p>
<p>For the shown regular-row updates, specify the intended complete row key. Static columns, counters and conditional writes have different rules and are not shortcuts for the simple schema. A primary-key value is row identity, not a mutable ordinary attribute.</p>
<p>Changing multiple tables or combining external actions is not automatically one SQL transaction. The examples are sequential and do not claim concurrency stress testing, payment integration or cross-node consistency experiments.</p>
''', programs=['ns3p07']),
    T('DELETE a Cell, a Row or a Selected Partition', '''
@@delete@@
<p>These four statements have different scopes: delete Asha’s city cell; delete learner 2; delete one full-key S01 reading; delete all rows in the selected S02/day partition. In the reference, Asha retains name/82 with city null, learner 2 returns no rows, S01/day29 retains two readings, and S02/day29 retains zero.</p>
<p><b>Tombstones:</b> logical deletion uses markers. Disappearance from SELECT is not proof of immediate physical disk erasure; physical cleanup depends on storage lifecycle and safe maintenance conditions. Do not teach repair/compaction procedures as part of this awareness-level unit.</p>
<p><b>Safety:</b> check the keyspace and every key component. Read-back proves the selected fixture result, not that a pre-read count locked data against concurrent changes. The supplied ownership-aware runner cleans only its newly created lab namespace.</p>
''', diagram='ns3_delete', programs=['ns3p08']),
]}

S5 = {'title': {'en': '3.5 Query-First Modeling, Filtering and CSV Input'}, 'items': [
    T('One Access Pattern per Table and Denormalization Costs', '''
<p>Start with two read requirements: (1) recent readings for one device/day, and (2) high-status readings for one day. The first uses readings_by_device_day; the second uses a separate readings_by_status_day table whose composite partition key is (status,day) and whose clustering columns are device_id then reading_at.</p>
<p>Deliberate duplication avoids a join or a broad scan for the shown reads. It also creates a consistency obligation: writes/corrections/deletions may need to update more than one representation.</p>
<p><b>Real demonstration:</b> the high S01/day29 reading starts at 32.0 in both tables. Updating the base table makes it 35.0 there while the lookup table still reads 32.0. Only the explicit second write makes the lookup table read 35.0. These two updates are not automatically one cross-table SQL transaction.</p>
<p>No foreign-key constraint or cascade updates the second table for you. Define retry, correction and missing-data handling in a real application. The status labels here are synthetic input, not predictions from a trained AI model. Do not use a logged multi-partition batch as a universal bulk-loading or transaction shortcut.</p>
''', diagram='ns3_model', programs=['ns3p10']),
    T('Unsupported Filters, ALLOW FILTERING and Real Negative Cases', '''
<p>Without a suitable index or access-table design, the demonstrated temperature-only query is rejected with InvalidRequest. The version with LIMIT 1 is also rejected; a small output limit does not legalize that query.</p>
@@filter@@
<p>The allowed example fixes one known three-row partition and returns 32.0 and 31.0. ALLOW FILTERING permits residual work; it is not an index, a modeling repair or a latency promise. Prefer an appropriate query-first table or deliberately selected index when an access pattern must scale.</p>
<p><b>Additional real server rejections:</b> a string where int is required; null primary key; ORDER BY an ordinary marks column; SET on the primary key; malformed SELECT syntax. Expected InvalidRequest/SyntaxException outcomes are captured from the server; the three valid rows remain unchanged.</p>
<p><b>Runner comments:</b> @result labels display observed result sets; @expect marks an intentionally rejected statement. These are ordinary comments, not extra CQL syntax, and unexpected exceptions still fail the run. JSON preserves server result order rather than silently sorting on the client.</p>
''', diagram='ns3_filter', programs=['ns3p11', 'ns3p14']),
    T('Import the AI/IoT Sensor CSV and Verify Stored Keys — Practical 6', '''
<p>The companion sensors.csv contains eight synthetic, explicitly UTC readings in the same four logical partitions. COPY FROM is a <b>cqlsh-only</b> import command; it is not sent as native CQL through an application driver.</p>
@@copy@@
<p><b>Why check timestamps:</b> date/time parsing or duplicate full primary keys can collapse distinct input records into upserts. A message saying eight rows were processed/imported is not enough. The tested program verifies eight stored rows, every stored reading against the CSV, four distinct device/day partitions and latest S01/day29 time 09:02 UTC with 32.0.</p>
<p><b>Explicit format:</b> DATETIMEFORMAT with %z recognizes the CSV’s UTC Z suffix. Do not depend on a permissive date-only fallback or an unrelated system timezone. HEADER, column mapping and error limits are deliberate; the single worker is for a tiny reference, not an import-throughput recommendation.</p>
<p><b>Honest scope:</b> this fixed snapshot simulates time-stamped AI/IoT input. It is not live sensor ingestion, a trained model, a production ETL job or a multi-machine distribution benchmark. COPY’s varying timing/rate text is omitted from published output; completion and subsequent server-read results are real.</p>
''', diagram='ns3_csv', programs=['ns3p12']),
]}

_REF = '<ol>' + ''.join('<li><a href="' + url + '">' + title + '</a></li>' for title, url in SOURCES) + '</ol>'
S6 = {'title': {'en': '3.6 Simple Analytics, Health Awareness and Practical Evidence'}, 'items': [
    T('Bounded Per-Partition Analytical Features, Not a Trained Model', '''
<p>Counts, totals, means and extrema can summarize a small sensor/day history for a report or later model input. Query the intended bounded partition rather than assuming Cassandra is an unrestricted analytical warehouse.</p>
@@features@@
''' + table(['Selected partition', 'Observed summary'], [
    ['S01 / 29 October', '3 samples; total 93.0; mean 31.0; min 30.0; max 32.0'],
    ['S02 / 29 October', '2 samples; mean 28.5'],
    ['S01 / 30 October', '2 samples; mean 33.5'],
    ['S03 / 29 October', '1 sample; mean 27.0'],
]) + '''
<p><b>Calculation:</b> (30+31+32)/3 = 31; (28+29)/2 = 28.5. These are simple measured-feature calculations on the synthetic fixture. A mean/threshold flag is not a trained anomaly detector or a guaranteed real-time decision system.</p>
<p>For real analytics, consider data volume, query frequency, retention, partition growth and suitable downstream tools. Small full-table COUNT queries used only to verify the eight-row import are not advice to scan a production cluster for every request.</p>
''', diagram='ns3_features', programs=['ns3p13']),
    T('nodetool Awareness, Cluster Health and the Practical 4–6 Journal', '''
<p><b>Scope:</b> the syllabus requests a conceptual overview of cluster health and nodetool, at awareness level only. nodetool is a management tool that uses JMX, not a CQL query typed into cqlsh.</p>
@@nodetool@@
<p><b>Actual observation:</b> a read-only nodetool status command reported one local UN node in datacenter1. U means Up and N means Normal. DN would describe Down/Normal; Joining/Leaving/Moving are other states to interpret, not instructions to trigger them.</p>
<p>A UN entry is one useful signal, not proof of application correctness, replicas, backups, latency objectives or full cluster health. Correlate authorized connection/read-write checks and operational signals. Load, UUID and ownership figures vary by environment. JMX/internode ports must remain private; enabling a CQL password alone is not complete production hardening.</p>
<p><b>No operations lab:</b> no repair, forced compaction, decommission, join/leave, failure injection or multi-node deployment is required or claimed. Token ownership/replication is explained conceptually; the real dataset was tested on one physical node only.</p>
<h4>Journal and acceptance evidence</h4>
@@journal@@
<ul><li><b>Practical 4:</b> actual installation, cqlsh connection, system-keyspace awareness, keyspace definition and key interpretation.</li>
<li><b>Practical 5:</b> a query-shaped table; INSERT/UPDATE/DELETE/SELECT; correct WHERE, ORDER BY and LIMIT; retrieval from distinct logical partitions.</li>
<li><b>Practical 6:</b> import the synthetic AI-related sensor CSV; verify all eight keys/values/times; explain four logical partitions and calculate bounded summaries. State the single-node simulation boundary.</li></ul>
<p><b>Assessment:</b> practical PA 20 + practical ESE 30 = 50; theory ESE/PA are 0. The answered tasks are lab/viva revision, not an official theory question paper or invented per-question marking scheme.</p>
<h4>Official references</h4><p>Checked 29 October 2026; use platform- and release-specific instructions. Recorded versions identify the reference execution.</p>
''' + _REF, diagram='ns3_health'),
]}

NOTES = [S1, S2, S3, S4, S5, S6]
assert sum(len(s['items']) for s in NOTES) == 18
