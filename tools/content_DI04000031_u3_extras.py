"""Cassandra Unit 3: fourteen reference cards, 52 viva answers, sixteen tasks.
Practical PA/ESE revision, not an invented official theory paper.
"""
from nosql_content import SX, V, Q, tr


def G(title, items): return {'title': tr(title), 'items': items}

SYNTAX = [
    G('Foundations and Private Setup', [
        SX('Server, cqlsh and nodetool', 'Cassandra = database server\ncqlsh = CQL client shell\nnodetool = management/JMX tool\nreference: one private authenticated node',
           'A shell version is not proof of authorized data access. nodetool status was read-only; no cluster-operations experiment is claimed.'),
        SX('Version and connection checks', 'OS: java -version\nOS: bin/cqlsh --version\ncqlsh: SHOW VERSION;\ncqlsh: SHOW HOST;',
           'Context-labelled commands, not one CQL script. The reference used Cassandra 5.0.9, cqlsh 6.2.0 and CQL 3.4.7. Record actual versions for your lab.'),
        SX('Keyspace DDL', "CREATE KEYSPACE di04000031_u3_manual\nWITH replication={'class':'NetworkTopologyStrategy',\n                  'datacenter1':1};\nUSE di04000031_u3_manual;\nALTER KEYSPACE di04000031_u3_manual\nWITH durable_writes=true;",
           'Use a newly owned scratch namespace and the actual DC name. RF 1 is the one-node reference, not a production availability recommendation. DROP only your own lab after use.'),
        SX('Parentheses define the key', 'PRIMARY KEY (a,b,c)\n  partition: a; clustering: b,c\nPRIMARY KEY ((a,b),c)\n  partition: a+b; clustering: c',
           'Reference key shapes, not complete CREATE TABLE statements. The full primary key identifies one row; a partition is not a physical machine.'),
    ]),
    G('Typed DDL and CRUD', [
        SX('Sensor table shape', 'CREATE TABLE readings_by_device_day (\n  device_id text, day date, reading_at timestamp,\n  temperature_c double, status text,\n  PRIMARY KEY ((device_id,day),reading_at)\n) WITH CLUSTERING ORDER BY (reading_at DESC);',
           'Requires an authorized fresh lab keyspace. Both device and day select the intended partition; the time column orders rows inside it.'),
        SX('INSERT and UPDATE upserts', "INSERT INTO learners_by_id (learner_id,name)\nVALUES (1,'Asha Patel');\nUPDATE learners_by_id SET name='Jai',marks=68\nWHERE learner_id=99;",
           'Assumes the demo schema. The first writes supplied values for an existing identity; the second can create missing data. No normal duplicate-key or matched/modified count is returned.'),
        SX('Cell, row and partition deletion', 'DELETE city FROM learners_by_id\nWHERE learner_id=1;\nDELETE FROM learners_by_id WHERE learner_id=2;\n-- Sensor: device+day+time -> one row.\n-- Sensor: device+day -> selected partition.',
           'The last two comments summarize key scope. Deletes use tombstones; do not equate absence from SELECT with immediate physical erasure. Never use system/application data for this exercise.'),
        SX('ALTER and DROP table', 'ALTER TABLE learner_schema ADD city text;\nALTER TABLE learner_schema DROP city;\nDROP TABLE learner_schema;',
           'Requires the disposable demo table. Old rows initially show null for an added regular column. Key-layout changes are not arbitrary in-place ALTER edits.'),
    ]),
    G('Partition Queries and Modeling', [
        SX('WHERE, IN and projection', 'SELECT name,city FROM learners_by_id\nWHERE learner_id=2;\nSELECT learner_id,name FROM learners_by_id\nWHERE learner_id IN (1,3);',
           'Known-key queries return selected columns. A missing-key SELECT is empty. IN can fan out; its output is not a global sort by name/marks.'),
        SX('Range, ORDER BY and LIMIT', "SELECT reading_at,temperature_c\nFROM readings_by_device_day\nWHERE device_id='S01' AND day='2026-10-29'\nORDER BY reading_at ASC LIMIT 2;",
           'This is an allowed reverse clustering order within the selected partition: 30.0 then 31.0. A half-open time range can select contiguous clustering rows.'),
        SX('Filtering and query-first access', 'temperature-only query -> InvalidRequest here\nLIMIT 1 does not legalize that WHERE\nselected tiny partition + ALLOW FILTERING\n  -> residual scan is explicitly permitted\nnew read pattern -> deliberate access table/index',
           'Behaviour summaries, not executable CQL. The allowed demo scans only the known three-row fixture partition; it is not an index or scalable-latency promise.'),
    ]),
    G('Dataset, Analytical Features and Health Awareness', [
        SX('CSV import verification', "COPY readings_by_device_day\n(device_id,day,reading_at,temperature_c,status)\nFROM 'sensors.csv' WITH HEADER=TRUE\nAND NUMPROCESSES=1\nAND DATETIMEFORMAT='%Y-%m-%dT%H:%M:%S%z';",
           'cqlsh-only, after table creation. The full program also has explicit error/batch options. Verify all eight stored records and UTC times, not just the import progress count.'),
        SX('Small bounded aggregate', "SELECT count(*) AS samples,\n  avg(temperature_c) AS mean\nFROM readings_by_device_day\nWHERE device_id='S01' AND day='2026-10-29';",
           'Returns three samples and mean 31.0. sum/min/max add simple features. This is not training, a full warehouse workload or a distributed throughput benchmark.'),
        SX('Interpret nodetool status', 'OS: bin/nodetool status\nU/D = Up/Down\nN/L/J/M = Normal/Leaving/Joining/Moving\nUN = Up/Normal; reference has one node',
           'Read-only awareness. Keep management access private. A UN line is not proof of all application, replica, backup or performance guarantees; do not run repair/decommission for this unit.'),
    ]),
]
assert sum(len(g['items']) for g in SYNTAX) == 14

_A = [
    V('What type of NoSQL database is Cassandra?', 'A distributed wide-column database with typed CQL tables organized into partitions and clustered rows.'),
    V('Is wide-column the same as a columnar analytical warehouse?', 'No. Cassandra is designed around partition-oriented access and distributed storage; do not infer unrestricted analytical scans from the word column.'),
    V('Give a suitable workload for the reference model.', 'A device/day sensor history with frequent timestamped writes and reads for one device over a bounded time range.'),
    V('What does query-first design mean?', 'Write the required read patterns first, then choose partition/clustering keys and access tables that serve them predictably.'),
    V('Is there one mandatory global write-primary?', 'No. Cassandra peers can coordinate requests; a coordinator is a per-request role, not a single cluster-wide primary.'),
    V('Partitioning versus replication?', 'Partitioning divides logical data subsets; replication stores extra copies. Four partition keys do not imply four nodes or four replicas.'),
    V('What is a keyspace?', 'A namespace for tables and related schema with options such as replication policy and durable writes.'),
    V('What is a partition?', 'The rows sharing the complete partition-key value. A physical node may store many partitions.'),
    V('What identifies one logical row?', 'The entire primary key: partition-key component(s) plus any clustering columns.'),
    V('What does PRIMARY KEY ((a,b),c) mean?', 'a and b together form a composite partition key; c is the clustering column. Without the extra parentheses, a alone would be the partition key.'),
]
_B = [
    V('What exact runtime was tested?', 'Cassandra 5.0.9, cqlsh 6.2.0, CQL 3.4.7, bundled Python driver 3.29.0, Python 3.13.16 and Temurin Java 17.0.21+9 on Debian 13 x86_64.'),
    V('How many physical nodes were tested?', 'One private authenticated local node, with lab keyspaces using datacenter1 and RF 1. No multi-node availability or throughput test is claimed.'),
    V('Why use matching cqlsh?', 'A client is generally guaranteed for its own Cassandra release; do not assume arbitrary old/new versions or Python interpreters are interchangeable.'),
    V('Does cqlsh --version prove a stored write worked?', 'No. Connect, inspect actual server versions and verify an authorized insert/read round-trip as well.'),
    V('What did SHOW VERSION report?', 'cqlsh 6.2.0, Cassandra 5.0.9, CQL spec 3.4.7 and native protocol v4. Protocol 4 is a selected wire-protocol version, not the Cassandra product version.'),
    V('Why does the replication map use datacenter1?', 'That is the actual local datacenter name verified from system.local. An unrelated DC name is not a universal template.'),
    V('Does RF 1 provide another node’s copy?', 'No. It is appropriate only for this one-node teaching reference and does not provide a replica for node loss.'),
    V('Name required/basic CQL types.', 'int, text and timestamp; the typed example also stores date, boolean, double and uuid with their real CQL types.'),
    V('Single quotes versus double quotes in CQL?', 'Single quotes delimit string values; double quotes delimit case-sensitive identifiers. Double an embedded apostrophe inside a string.'),
    V('What does adding city text do to existing rows?', 'It adds a regular typed column; the previous row shows city null until it is written. It does not invent a default city or repartition data.'),
]
_C = [
    V('What happens on a normal INSERT of an existing full key?', 'It upserts supplied values for that logical row. In the demo Asha becomes Asha Patel while the omitted existing Surat/82 values remain.'),
    V('Is normal INSERT a whole-row replacement?', 'No. It writes supplied values; omitted existing columns are not removed merely because they are absent from the INSERT list.'),
    V('What happens on a normal UPDATE of missing learner 99?', 'It creates Jai/68 with city null. Basic UPDATE does not require the row to have existed.'),
    V('Are matchedCount and modifiedCount returned by basic CQL updates?', 'No. Those are MongoDB-style result fields, not the normal CQL result. Handle errors and inspect the intended stored state.'),
    V('Can marks=marks+5 update an ordinary int?', 'Not as ordinary CQL int arithmetic. Counter columns and collection operations have separate rules; do not translate MongoDB $inc mechanically.'),
    V('What does deleting just city leave for learner 1?', 'The row still has Asha and marks 82, while city reads as null.'),
    V('What key deletes one sensor reading?', 'The complete device_id/day/reading_at row identity. Supplying just device/day intentionally targets that entire partition.'),
    V('What is a tombstone?', 'A logical deletion marker. A missing read result does not prove immediate physical byte erasure from disk.'),
    V('Can SET change a primary-key field into another ID?', 'No. The real server rejects that mutation. A key is row identity; changing identity/model needs deliberate new data and cleanup.'),
    V('How are null and wrong-type primary keys handled?', 'The shown null key and quoted one-as-int are rejected with real InvalidRequest exceptions; no extra valid row is inserted.'),
]
_D = [
    V('What does a missing-key SELECT return?', 'An empty result set, not a new row and not a MongoDB findOne-style null value.'),
    V('What do the latest-two and earliest-two queries return?', 'For S01/day29, descending latest values are 32.0 then 31.0; allowed ascending reverse order gives 30.0 then 31.0.'),
    V('What does [09:00,09:02) include here?', '09:00 and 09:01, but not 09:02. The declared descending clustering order returns 31.0 then 30.0.'),
    V('Can ORDER BY sort any regular column globally?', 'No. The shown ORDER BY uses a clustering column with required partition restrictions. ORDER BY marks in the learner table is rejected.'),
    V('Does LIMIT 1 legalize the temperature-only WHERE?', 'No. That demonstrated unindexed non-key query remains invalid. LIMIT restricts returned rows; it does not create the access path.'),
    V('What does ALLOW FILTERING mean in this fixture?', 'It explicitly permits residual filtering after selecting the known three-row partition. It is not an index or a guarantee of scalable performance.'),
    V('Why use a status/day table as well as a device/day table?', 'They serve different read patterns without a join or broad scan; the intentional duplication requires coordinated correction/deletion policies.'),
    V('What did the denormalization correction demonstrate?', 'The base reading changed from 32.0 to 35.0 while the second table stayed at 32.0 until a separate explicit write updated it. There is no automatic cross-table correction.'),
]
_E = [
    V('How many sensor rows and logical partitions are in sensors.csv?', 'Eight synthetic rows in four device/day partitions: S01/day29 has 3, S02/day29 has 2, S01/day30 has 2 and S03/day29 has 1.'),
    V('Is COPY FROM native CQL?', 'No. It is a cqlsh special command. The reference runner delegates it to real matching cqlsh rather than pretending a driver supports it.'),
    V('Why use DATETIMEFORMAT with %z?', 'To parse the CSV’s explicit UTC Z suffix correctly. Wrong parsing or duplicate full keys can collapse distinct records into upserts.'),
    V('Is eight processed/imported rows enough verification?', 'No. Verify eight distinct stored rows, all full keys/values/times, four logical partition keys and the correct latest UTC reading.'),
    V('What is the S01/day29 aggregate?', 'Three samples, sum 93.0, mean 31.0, minimum 30.0 and maximum 32.0.'),
    V('What are the other per-partition means?', 'S02/day29 is 28.5, S01/day30 is 33.5 and S03/day29 is 27.0.'),
    V('Is the CSV example a live stream or trained AI system?', 'No. It is a reproducible synthetic snapshot with real database import and simple feature/report calculations, not live hardware, model training or a throughput benchmark.'),
    V('Why are time buckets not automatically safe at every rate?', 'Partition size and hotness depend on writes per time unit, row size and access load. A daily bucket may need to be smaller or differently designed for a much faster stream.'),
]
_F = [
    V('What does nodetool status use?', 'Management/JMX, not a CQL statement inside cqlsh. Management access must be private and authorized.'),
    V('What do UN and DN mean?', 'U/D indicate Up/Down; N indicates Normal. The actual reference observed one local UN node. Other state letters include L/J/M for Leaving/Joining/Moving.'),
    V('Does UN prove every application and availability guarantee?', 'No. It is one signal; correlate application reads/writes and operational evidence. It does not prove backups, multiple replicas or latency objectives.'),
    V('Were repair, decommission or failure injection tested?', 'No. The syllabus asks for nodetool/cluster-health awareness only. The only management observation was read-only status.'),
    V('How does the guarded runner protect existing keyspaces?', 'It validates the dedicated prefix, refuses an existing namespace, records ownership only after CREATE succeeds and finally drops only that captured newly owned keyspace.'),
    V('What assessment and completion boundary should the journal state?', 'Practical PA 20 + ESE 30 = 50 with no theory ESE/PA. Record Practicals 4–6 and real single-node evidence; no official theory paper, multi-node proof or external hosting is claimed.'),
]
VIVA = [G('Foundations and Keys', _A), G('Setup and Typed Schema', _B), G('CRUD and Negative Cases', _C),
        G('Queries and Modeling', _D), G('Dataset and Analytical Features', _E), G('Health, Safety and Evidence', _F)]
assert sum(len(g['items']) for g in VIVA) == 52

PRACTICE_QS = [
    Q('architecture', 'Explain a Cassandra peer, coordinator, partition and replica without claiming the local lab is a three-node cluster.',
      '<p>A peer can coordinate a request and communicate with the relevant replica nodes. Partitioning divides data subsets using partition-key placement; replication keeps additional copies according to the keyspace policy.</p><p>The diagram is conceptual. The actual reference used one authenticated node and RF 1, so four logical device/day partitions do not establish multi-machine placement, replicated failover or global throughput.</p>'),
    Q('Practical 4', 'Prepare a compatible, private Cassandra/cqlsh setup and a real storage-verification journal.',
      '<p>Identify OS/architecture and the selected release; install supported Java and matching cqlsh/Python; verify the official download checksum; configure private interfaces and authorized lab access; start the server; connect with a hidden password or protected credentials; record actual versions and an insert/read round-trip.</p><p>The tested reference was Debian 13 x86_64, Cassandra 5.0.9, cqlsh 6.2.0, Python 3.13.16 and Temurin 17.0.21+9. The factory role was disabled/rotated. Do not claim those steps are production hardening or use public default credentials.</p>'),
    Q('keys', 'Compare PRIMARY KEY (device_id,day,reading_at) with PRIMARY KEY ((device_id,day),reading_at).',
      '<p>The first partitions on device_id and clusters by day then reading_at; all days of one device share that partition. The second partitions on the pair device_id/day and clusters only by reading_at; a new day creates another logical partition.</p><p>Both complete keys identify one row. Choose the layout from required reads and expected size/load. A partition is not a server, and a daily bucket is not automatically bounded safely for every write rate.</p>'),
    Q('types', 'Design the sensor-history table and explain int, text, date and timestamp literals.',
      '<p>Use device_id text, day date, reading_at timestamp, temperature_c double and status text with PRIMARY KEY ((device_id,day),reading_at) and descending time order.</p><p>int is a signed 32-bit integer; text uses single-quoted UTF-8 string values; date stores a calendar day; timestamp stores date/time with millisecond precision. Include an explicit zone such as Z, and do not confuse double-quoted identifiers with string values. Wrong-type and null primary keys are rejected.</p>'),
    Q('DDL', 'Demonstrate Create/Alter/Drop keyspaces and tables, and state the safety/primary-key limitations.',
      '<p>Create a new owned prefix-scoped keyspace with NetworkTopologyStrategy, the actual datacenter1 and RF 1 for this single-node lab. Select it; retain durable writes; create a typed table, add/write/drop a regular column, change a comment and drop the table/keyspace after verification.</p><p>Refuse pre-existing namespaces. ALTER is not arbitrary primary-key repartitioning; a key-layout change needs a new model/migration. Stop after unexpected setup failures rather than continuing into someone else’s data and a DROP footer.</p>'),
    Q('INSERT', 'Insert learner 1 again using only a new name. Contrast the observed CQL behaviour with a MongoDB duplicate _id insertion.',
      '<p>The normal CQL INSERT upserts: learner 1 becomes Asha Patel while existing city Surat and marks 82 remain; the logical row count for that key is one. Omitted existing regular columns are not removed.</p><p>That is not a normal MongoDB insertOne duplicate-ID error or whole-document replacement. Conditional/LWT variants have separate semantics and costs; do not assume they are implicit.</p>'),
    Q('WHERE', 'Query ID 2, then IDs 1 and 3, then an absent ID, selecting only required columns.',
      '<p>WHERE learner_id=2 returns Ravi/Bharuch; WHERE learner_id IN (1,3) returns the two known identities/names; WHERE learner_id=999 returns an empty result set.</p><p>SELECT column lists shape returned data, not storage or authorization. Do not infer global name/marks ordering from a multi-partition result. Large IN fan-out and unsupported regular-field predicates need deliberate design.</p>'),
    Q('range/order/limit', 'Derive latest two, earliest two and the [09:00,09:02) query for S01/day29.',
      '<p>The partition contains 30.0 at 09:00, 31.0 at 09:01 and 32.0 at 09:02 UTC. Default descending time with LIMIT 2 returns 32.0 then 31.0. Allowed ORDER BY reading_at ASC LIMIT 2 returns 30.0 then 31.0.</p><p>The half-open interval includes 09:00 and 09:01, excludes 09:02 and follows the default descending order: 31.0 then 30.0. This is not an unrestricted SQL ORDER BY on any regular field.</p>'),
    Q('UPDATE', 'Update Ravi’s city/marks and update previously absent learner 99. Explain the real results.',
      '<p>SET city=Surat and marks=75 for ID 2 reads back Ravi/Surat/75. SET name=Jai and marks=68 for missing ID 99 creates that row with city null.</p><p>Normal UPDATE is an upsert and does not return matchedCount/modifiedCount. Use the correct complete row identity; do not use ordinary-int marks=marks+5 as a mechanical translation of MongoDB $inc.</p>'),
    Q('DELETE', 'Compare deleting a city cell, learner row, one sensor row and a device/day partition.',
      '<p>DELETE city leaves Asha/82 with city null. Deleting ID 2 yields no learner row. Deleting the full S01/day29/09:02 key leaves two readings; deleting S02/day29 without a time removes that entire selected partition.</p><p>These scopes are different. Deletes use tombstones, so missing SELECT data is not immediate physical-erasure proof. No deletedCount is returned and no repair/compaction operation is required for this lesson.</p>'),
    Q('modeling', 'Design device/day and status/day access paths and explain the 32.0 → 35.0 stale-copy experiment.',
      '<p>Use readings_by_device_day for one device’s history and readings_by_status_day partitioned by status/day for a different lookup. Deliberate duplicated rows avoid a join or broad scan for these queries.</p><p>The base correction reads 35.0 while the second table still has 32.0. A separate explicit second write produces 35.0 there. There is no automatic foreign-key/cascade correction or implicit cross-table SQL transaction; applications must define retry/correction policies.</p>'),
    Q('filtering', 'Explain the rejected temperature-only queries, the bounded ALLOW FILTERING example and the negative type/order/key tests.',
      '<p>The unindexed temperature-only WHERE is rejected with InvalidRequest, even with LIMIT 1. After fixing S01/day29, ALLOW FILTERING explicitly scans its three known rows and returns 32.0/31.0.</p><p>It is not an index or performance promise. Wrong int literal, null primary key, regular-column ORDER BY and SET on a primary-key field are also rejected; malformed SELECT yields SyntaxException. The three valid learner rows remain unchanged.</p>'),
    Q('Practical 6 import', 'Import sensors.csv with actual cqlsh and prove that distinct event keys and UTC times survived.',
      '<p>Create the empty sensor table, run cqlsh COPY FROM with the explicit column list, HEADER, one worker, zero tolerated import/parse errors and DATETIMEFORMAT using %z for the Z suffix.</p><p>Verify eight stored rows against every CSV key/value/time, four logical partition values and latest S01/day29 time 09:02 with 32.0. A processed-row message is not enough: incorrect timestamp parsing or duplicate full keys can collapse rows through upserts. This is a synthetic snapshot, not live ingestion.</p>'),
    Q('analytics', 'Calculate the per-partition feature summaries and explain their honest AI relevance.',
      '<p>S01/day29 has 30+31+32 = 93 over three samples: mean 31, min 30, max 32. S02/day29 has mean 28.5; S01/day30 has mean 33.5; S03/day29 has mean 27.</p><p>These bounded real CQL aggregates can feed a report or later model. They do not train a classifier, guarantee real-time decisions, benchmark distributed throughput or justify unrestricted production full-table scans.</p>'),
    Q('health awareness', 'Interpret the actual UN observation and describe what is outside the health-awareness syllabus.',
      '<p>nodetool status uses management/JMX. U/D are Up/Down; N/L/J/M are Normal/Leaving/Joining/Moving. The actual private reference showed one local UN node in datacenter1.</p><p>It is one useful observation, not proof of all application/backup/replica/latency guarantees. Keep management access private. No repair, decommission, join/leave, forced compaction, failure injection or multi-node deployment is required or claimed.</p>'),
    Q('acceptance journal', 'Prepare a Practical 4–6 acceptance checklist and explain why these tasks are not a theory paper.',
      '<p>Record actual platform/versions, private authorized storage evidence, query-to-key reasoning, all DDL/CRUD/WHERE/ORDER BY/LIMIT outputs, expected errors and owned scratch cleanup. For the dataset verify every CSV row/time, four logical partitions and the bounded analytic calculations; record read-only health interpretation.</p><p>Keep credentials out of submissions and state single-node/synthetic limits. Official assessment is practical PA 20 + practical ESE 30 = 50 with zero theory ESE/PA. These answered revision tasks carry no invented official theory-paper marks.</p>'),
]
assert len(PRACTICE_QS) == 16
