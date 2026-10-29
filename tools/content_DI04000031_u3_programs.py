"""Fourteen exact CQL scripts executed on real Cassandra 5.0.9.

Import executes all examples using prefix-scoped ownership-aware cleanup.
Result rows come from the server, JSON-serialized in server result order.
The CSV program calls actual cqlsh COPY FROM; timing/rate noise is omitted.
"""
from cassandra_content import P
from content_DI04000031_u3_shared import STUDENT_DDL, STUDENT_SEED, SENSOR_DDL, SENSOR_SEED, READINGS, quoted

ALT_DDL = '''CREATE TABLE readings_by_status_day (
  status text, day date, device_id text,
  reading_at timestamp, temperature_c double,
  PRIMARY KEY ((status, day), device_id, reading_at)
) WITH CLUSTERING ORDER BY (device_id ASC, reading_at DESC);
'''
ALT_SEED = ALT_DDL
for row in READINGS:
    ALT_SEED += ('INSERT INTO readings_by_status_day\n'
        '  (status, day, device_id, reading_at, temperature_c)\n'
        'VALUES (' + ', '.join(quoted(row[k]) for k in ('status', 'day', 'device_id'))
        + ',\n        ' + quoted(row['reading_at']) + ', ' + str(row['temperature_c']) + ');\n')

PROGRAMS = [
    P('ns3p01', 'Connect, Create/Alter/Drop a Keyspace and Verify Storage', '''
-- @result server_versions
SELECT release_version, cql_version FROM system.local WHERE key='local';
-- @result local_datacenter
SELECT data_center FROM system.local WHERE key='local';
ALTER KEYSPACE @@KS@@ WITH durable_writes = true;
-- @result keyspace_options
SELECT replication, durable_writes FROM system_schema.keyspaces
WHERE keyspace_name='@@KS@@';
CREATE TABLE connection_probe (id int PRIMARY KEY, message text);
INSERT INTO connection_probe (id, message) VALUES (1, 'Cassandra connected');
-- @result stored_roundtrip
SELECT id, message FROM connection_probe WHERE id=1;
DROP TABLE connection_probe;
-- @result tables_after_drop
SELECT table_name FROM system_schema.tables
WHERE keyspace_name='@@KS@@';
''', '<p>The complete script creates one lab keyspace, selects it, alters a keyspace option, creates/writes/reads/drops a table and finally drops that newly created keyspace. NetworkTopologyStrategy uses the observed datacenter1 with RF 1 for one local node.</p><p>System tables are queried read-only. An authenticated storage round-trip is stronger evidence than a version executable alone. The public runner refuses existing namespaces and tracks successful creation before allowing cleanup.</p>'),

    P('ns3p02', 'Typed CQL Columns, Fixed UTC Timestamp and UUID', '''
CREATE TABLE learner_profile (
  learner_id int PRIMARY KEY, name text, active boolean,
  joined_at timestamp, exam_day date, score double, profile_id uuid
);
INSERT INTO learner_profile
  (learner_id, name, active, joined_at, exam_day, score, profile_id)
VALUES (1, 'Asha', true, '2026-10-29T09:00:00Z', '2026-10-29', 85.5,
        11111111-1111-4111-8111-111111111111);
-- @result typed_profile
SELECT learner_id, name, active, joined_at, exam_day, score, profile_id
FROM learner_profile WHERE learner_id=1;
''', '<p>CQL tables have an explicit typed schema. int, text, timestamp, date, boolean, double and uuid are genuine stored types; strings use single quotes and the UUID literal is unquoted.</p><p>The runner displays timestamps in ISO UTC and date/UUID values as JSON strings. That display conversion does not change their CQL storage types. A fixed timestamp avoids machine-local timezone ambiguity.</p>'),

    P('ns3p03', 'Composite Partition Keys and Ordered Rows', SENSOR_SEED + '''
-- @result logical_partitions
SELECT DISTINCT device_id, day FROM readings_by_device_day;
-- @result s01_day29
SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29';
-- @result s01_day30
SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-30';
-- @result s02_day29
SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S02' AND day='2026-10-29';
''', '<p>Eight explicit seed records occupy four logical device/day partitions. PRIMARY KEY ((device_id,day),reading_at) uses both fields as the partition key; reading_at is the clustering column in descending order.</p><p>The same device on another day belongs to another partition. DISTINCT partition-key output is not a global lexical sort, and four logical partitions on this single physical node do not prove multi-node distribution.</p>'),

    P('ns3p04', 'INSERT is an Upsert, Not a Duplicate-Key Error', STUDENT_SEED + '''
INSERT INTO learners_by_id (learner_id, name) VALUES (1, 'Asha Patel');
-- @result same_primary_key
SELECT learner_id, name, city, marks FROM learners_by_id WHERE learner_id=1;
INSERT INTO learners_by_id (learner_id, name) VALUES (4, 'Imran');
-- @result new_primary_key
SELECT learner_id, name, city, marks FROM learners_by_id WHERE learner_id=4;
-- @result one_row_for_id1
SELECT count(*) AS n FROM learners_by_id WHERE learner_id=1;
''', '<p>A normal INSERT with an existing complete primary key updates the supplied columns: Asha becomes Asha Patel while city and marks remain. No ordinary duplicate-key error is expected.</p><p>A new primary key creates a new row; missing non-key values display as null. This is not whole-row replacement and does not return MongoDB-style inserted/modified counts.</p>'),

    P('ns3p05', 'WHERE, IN and Selecting Only Required Columns', STUDENT_SEED + '''
-- @result exact_id
SELECT name, city FROM learners_by_id WHERE learner_id=2;
-- @result two_known_ids
SELECT learner_id, name FROM learners_by_id WHERE learner_id IN (1,3);
-- @result missing_id
SELECT learner_id, name FROM learners_by_id WHERE learner_id=999;
''', '<p>WHERE targets a known partition key; IN explicitly selects two keys. SELECT lists the returned columns and does not modify stored records.</p><p>The missing key yields an empty result set. Multiple partitions do not acquire a global ORDER BY name/marks; large IN lists can fan out work. CQL uses AND conditions and typed SQL-like literals, not MongoDB dollar operators.</p>'),

    P('ns3p06', 'Clustering Order, Time Range, ORDER BY and LIMIT', SENSOR_SEED + '''
-- @result latest_two
SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29' LIMIT 2;
-- @result earliest_two
SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29'
ORDER BY reading_at ASC LIMIT 2;
-- @result bounded_range
SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29'
  AND reading_at >= '2026-10-29T09:00:00Z'
  AND reading_at < '2026-10-29T09:02:00Z';
''', '<p>The table-defined descending clustering order returns 32.0 then 31.0 for the latest two. An allowed reverse ORDER BY returns 30.0 then 31.0. The half-open interval includes 09:00 and excludes 09:02.</p><p>ORDER BY here applies to the clustering column in a selected partition, not arbitrary regular columns or a general cross-partition SQL sort. LIMIT bounds returned rows, not every possible cost.</p>'),

    P('ns3p07', 'UPDATE Existing Data and Observe a Missing-Key Upsert', STUDENT_SEED + '''
UPDATE learners_by_id SET city='Surat', marks=75 WHERE learner_id=2;
-- @result ravi_after_update
SELECT name, city, marks FROM learners_by_id WHERE learner_id=2;
UPDATE learners_by_id SET name='Jai', marks=68 WHERE learner_id=99;
-- @result missing_key_created
SELECT learner_id, name, city, marks FROM learners_by_id WHERE learner_id=99;
''', '<p>UPDATE changes specified regular columns. The missing-key UPDATE creates Jai with city null; normal UPDATE is also an upsert, not “zero matches” in the MongoDB sense.</p><p>Supply the appropriate complete row key for these regular-column updates. Ordinary int values do not support marks=marks+5; counter columns have different restrictions. Conditional/LWT operations are separate from this basic lab.</p>'),

    P('ns3p08', 'Delete a Cell, One Row and a Whole Partition', STUDENT_SEED + SENSOR_SEED + '''
DELETE city FROM learners_by_id WHERE learner_id=1;
-- @result city_cell_deleted
SELECT learner_id, name, city, marks FROM learners_by_id WHERE learner_id=1;
DELETE FROM learners_by_id WHERE learner_id=2;
-- @result learner_row_deleted
SELECT learner_id FROM learners_by_id WHERE learner_id=2;
DELETE FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29'
  AND reading_at='2026-10-29T09:02:00Z';
-- @result one_sensor_row_deleted
SELECT count(*) AS n FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29';
DELETE FROM readings_by_device_day
WHERE device_id='S02' AND day='2026-10-29';
-- @result whole_partition_deleted
SELECT count(*) AS n FROM readings_by_device_day
WHERE device_id='S02' AND day='2026-10-29';
''', '<p>Deleting city removes that cell, leaving Asha’s other values. Deleting learner 2 removes its row. The full sensor/day/time key removes one reading; the device/day partition key without a time removes the whole selected partition.</p><p>Deletes create logical deletion markers (tombstones); disappearance from a read is not proof of immediate physical byte erasure. No deletedCount is returned. Confirm key scope and never use a real application keyspace for this lab.</p>'),

    P('ns3p09', 'ALTER TABLE, Nullable New Columns and DROP TABLE', '''
CREATE TABLE learner_schema (learner_id int PRIMARY KEY, name text);
INSERT INTO learner_schema (learner_id, name) VALUES (1, 'Asha');
ALTER TABLE learner_schema ADD city text;
-- @result added_column_initially_null
SELECT learner_id, name, city FROM learner_schema WHERE learner_id=1;
UPDATE learner_schema SET city='Surat' WHERE learner_id=1;
-- @result added_column_written
SELECT name, city FROM learner_schema WHERE learner_id=1;
ALTER TABLE learner_schema WITH comment='Small schema-change lab';
-- @result table_comment
SELECT comment FROM system_schema.tables
WHERE keyspace_name='@@KS@@' AND table_name='learner_schema';
ALTER TABLE learner_schema DROP city;
-- @result columns_after_drop
SELECT column_name, kind, type FROM system_schema.columns
WHERE keyspace_name='@@KS@@' AND table_name='learner_schema';
DROP TABLE learner_schema;
-- @result table_removed
SELECT table_name FROM system_schema.tables
WHERE keyspace_name='@@KS@@' AND table_name='learner_schema';
''', '<p>ADD introduces a typed regular column; older rows initially display null. The example writes it, changes a table comment, drops the regular column and drops the table.</p><p>ALTER TABLE does not let you append an arbitrary new primary-key component or change partitioning in place. Create a query-shaped new table and migrate deliberately when the key design changes; primary-key-column rename support is not a repartitioning operation.</p>'),

    P('ns3p10', 'Query-First Tables and Denormalization Consistency', SENSOR_SEED + ALT_SEED + '''
-- @result high_day29
SELECT device_id, reading_at, temperature_c FROM readings_by_status_day
WHERE status='high' AND day='2026-10-29';
UPDATE readings_by_device_day SET temperature_c=35.0
WHERE device_id='S01' AND day='2026-10-29'
  AND reading_at='2026-10-29T09:02:00Z';
-- @result base_corrected
SELECT temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29'
  AND reading_at='2026-10-29T09:02:00Z';
-- @result second_table_still_old
SELECT temperature_c FROM readings_by_status_day
WHERE status='high' AND day='2026-10-29' AND device_id='S01'
  AND reading_at='2026-10-29T09:02:00Z';
UPDATE readings_by_status_day SET temperature_c=35.0
WHERE status='high' AND day='2026-10-29' AND device_id='S01'
  AND reading_at='2026-10-29T09:02:00Z';
-- @result second_table_corrected
SELECT temperature_c FROM readings_by_status_day
WHERE status='high' AND day='2026-10-29' AND device_id='S01'
  AND reading_at='2026-10-29T09:02:00Z';
''', '<p>Device/day history and status/day lookup are different access patterns, so two intentionally duplicated tables serve them. No join is needed for the shown reads.</p><p>Correcting the base table to 35.0 leaves the second table at 32.0 until the explicit second write. These writes are not automatically one cross-table SQL transaction, and no automatic foreign key/cascade is provided. The status labels are fixture data, not predictions from a trained model.</p>'),

    P('ns3p11', 'Rejected Non-Key Filters and a Tiny Bounded Filtering Example', SENSOR_SEED + '''
-- @result non_key_filter_rejected
-- @expect InvalidRequest
SELECT device_id, temperature_c FROM readings_by_device_day
WHERE temperature_c > 30.0;
-- @result limit_does_not_legalize_filter
-- @expect InvalidRequest
SELECT device_id, temperature_c FROM readings_by_device_day
WHERE temperature_c > 30.0 LIMIT 1;
-- @result bounded_partition_filter
SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29'
  AND temperature_c > 30.0 ALLOW FILTERING;
''', '<p>The two unindexed non-key queries are deliberately rejected by the server. Adding LIMIT 1 does not make this unsupported access path valid.</p><p>ALLOW FILTERING is demonstrated only after fixing the device/day partition, which contains three known fixture rows. It permits residual filtering; it does not create an index or guarantee scalable latency. Prefer query-first tables or a suitable deliberately chosen index for real access patterns.</p>'),

    P('ns3p12', 'Import the Synthetic Sensor CSV with Actual cqlsh COPY FROM', SENSOR_DDL + '''
-- COPY is a cqlsh special command, not a native CQL statement.
-- The runner delegates this exact command to real matching cqlsh.
-- Run from the folder containing the supplied sensors.csv.
-- @result csv_import
COPY readings_by_device_day
  (device_id, day, reading_at, temperature_c, status)
FROM 'sensors.csv' WITH HEADER=TRUE AND NUMPROCESSES=1
  AND DATETIMEFORMAT='%Y-%m-%dT%H:%M:%S%z'
  AND MAXPARSEERRORS=0 AND MAXINSERTERRORS=0
  AND MINBATCHSIZE=1 AND MAXBATCHSIZE=1;
-- @result imported_row_count
SELECT count(*) AS n FROM readings_by_device_day;
-- @result imported_partitions
SELECT DISTINCT device_id, day FROM readings_by_device_day;
-- @result imported_rows
SELECT device_id, day, reading_at, temperature_c, status
FROM readings_by_device_day;
-- @result latest_imported_reading
SELECT reading_at, temperature_c FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29' LIMIT 1;
''', '<p>Eight synthetic CSV records are actually imported by cqlsh COPY FROM, then verified through Cassandra reads: eight rows, four logical partitions and latest S01/day29 value 32.0. There is no hidden extra seed for this example. Explicit DATETIMEFORMAT with %z preserves the UTC times; a processed-row message alone is not proof of distinct stored rows.</p><p>The runner captures COPY completion while omitting changing rates/timings from the published output; JSON rows are real server results. This small snapshot simulates time-stamped AI/IoT input, not a live stream, a trained model, an ETL benchmark or placement across multiple machines.</p>'),

    P('ns3p13', 'Small Per-Partition Analytical Features for AI/IoT', SENSOR_SEED + '''
-- @result s01_day29_features
SELECT count(*) AS samples, sum(temperature_c) AS total,
  avg(temperature_c) AS mean, min(temperature_c) AS minimum,
  max(temperature_c) AS maximum
FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-29';
-- @result s02_day29_features
SELECT count(*) AS samples, avg(temperature_c) AS mean
FROM readings_by_device_day
WHERE device_id='S02' AND day='2026-10-29';
-- @result s01_day30_features
SELECT count(*) AS samples, avg(temperature_c) AS mean
FROM readings_by_device_day
WHERE device_id='S01' AND day='2026-10-30';
-- @result s03_day29_features
SELECT count(*) AS samples, avg(temperature_c) AS mean
FROM readings_by_device_day
WHERE device_id='S03' AND day='2026-10-29';
''', '<p>S01/day29 contains 30,31,32: count 3, total 93, mean 31, minimum 30 and maximum 32. Other means are 28.5, 33.5 and 27.0 in their own selected partitions.</p><p>These bounded aggregates can form input features or simple reports. They do not train a classifier or turn Cassandra into an unrestricted columnar data warehouse. Large scans/analytics need an appropriate workload architecture; eight samples do not establish distributed throughput or real-time guarantees.</p>'),

    P('ns3p14', 'Real Server Rejections: Types, Null Key, ORDER BY and Key Mutation', STUDENT_SEED + '''
-- @result wrong_int_type
-- @expect InvalidRequest
INSERT INTO learners_by_id (learner_id, name) VALUES ('one', 'Invalid');
-- @result null_primary_key
-- @expect InvalidRequest
INSERT INTO learners_by_id (learner_id, name) VALUES (null, 'Invalid');
-- @result regular_column_ordering
-- @expect InvalidRequest
SELECT name, marks FROM learners_by_id WHERE learner_id=1
ORDER BY marks DESC;
-- @result primary_key_set_rejected
-- @expect InvalidRequest
UPDATE learners_by_id SET learner_id=9 WHERE learner_id=1;
-- @result bad_cql_syntax
-- @expect SyntaxException
SELECT FROM learners_by_id;
-- @result valid_rows_unchanged
SELECT count(*) AS n FROM learners_by_id;
-- @result missing_is_empty
SELECT learner_id, name FROM learners_by_id WHERE learner_id=999;
''', '<p>Expected InvalidRequest and SyntaxException outcomes come from the actual server, not a Python substitute. @expect is a runner annotation inside an ordinary comment, so the intended negative tests are visible to a student.</p><p>Wrong int literals, null primary keys, arbitrary regular-column ordering and SET on a primary-key field are rejected. Three valid rows remain and a missing-key SELECT is empty. A manual cqlsh user should distinguish these deliberate failures from unexpected setup errors.</p>'),
]
assert len(PROGRAMS) == 14
