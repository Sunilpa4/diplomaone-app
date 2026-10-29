# DI04000031 — Source and scope record

Checked: **29 October 2026**. The materials cover **Units 1–3**; Units 4–5 remain pending.

## Authoritative curriculum

- [GTU official DI04000031 PDF](https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf), effective 2025–26; local transcription `tools/syllabus_DI04000031.txt`.
- Computer/CSE, semester 4; practical subject; 3 credits; L0/T1/PR4.
- Theory ESE 0, theory PA 0, practical PA 20, practical ESE 30: total 50.
- Units: Introduction 8h/13%; MongoDB 18h/30%; Cassandra 12h/20%; Neo4j 12h/20%; Redis 10h/17%. Total 60h/100%.
- Unit 1: why NoSQL and RDBMS trade-offs; CAP basics with analogy only; four models; AI uses. CO1 selects and justifies a model.
- Practical 1 is **comparative study**, not installation of all four engines. MongoDB setup starts in Practical 2.
- Later scope limits: MongoDB replication/sharding conceptual; Cassandra health awareness; graph recommendation/fraud algorithm examples, not implementations.

## Technical references used for Unit 1

1. [Gilbert and Lynch — Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services](https://users.ece.cmu.edu/~adrian/731-sp04/readings/GL-cap.pdf). CAP C is linearizability, distinct from ACID C. Availability is eventual operation completion, not a fixed latency promise. The theorem concerns partition executions; no proof is taught here.
2. [MongoDB — Data Modeling](https://www.mongodb.com/docs/manual/data-modeling/). Flexible documents, nested fields, validation and access-pattern design. BSON is not simply JSON text.
3. [Apache Cassandra — Introduction to Data Modeling](https://cassandra.apache.org/doc/latest/cassandra/developing/data-modeling/intro.html). Query-driven typed tables, partition/clustering keys, denormalization and no relational joins. This does not imply a columnar analytical warehouse.
4. [Neo4j — Graph Database Concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/). Nodes, labels, directed typed relationships, properties and paths.
5. [Redis — Data Types](https://redis.io/docs/latest/develop/data-types/). Redis supports multiple data structures rather than only plain string values. Unit 5 retains the syllabus's basic strings/lists/sets/hashes scope.

## Unit 1 evidence boundaries

- Document records, key/value entries, sensor partitions and graph paths are **illustrative teaching fixtures**.
- Tests check valid JSON, field/key consistency, the illustrated shared-interest candidate, source/diagram integrity, safe HTML, preview JavaScript and the workbook. These are **not database engine runs** or performance measurements.
- No named-company deployment claims, latest-version claims or fabricated benchmark numbers.
- The course is practical-only. The unit has no official-theory-paper tab, no allocated per-question marks, and 16 answered revision tasks in Notes.
- The workbook contains worked comparison/selection/CAP sheets and a blank editable journal. A defensible alternative model is allowed when the workload reasoning supports it.

## Deliverables

- `content/computer/sem4/DI04000031/subject.json` and `unit1.json`
- Ten self-contained SVG diagrams in the subject's `diagrams/` directory
- `preview/DI04000031_unit1_preview.html`
- `preview/DI04000031_unit1_practical1_worksheet.xlsx`

Rebuild: `python3 tools/build_DI04000031_u1.py`.
Validate: `python3 tools/test_DI04000031_u1.py`.
Release only after the established exact-commit app-render CI succeeds.


## Unit 2 — MongoDB reference and execution record

- Official Unit 2: **18 hours / 30%**; CO2: apply MongoDB features for effective data modeling and management. Practicals **2–3** cover installation/connectivity and CRUD/filter/sort/projection work.
- Documents, collections, BSON and architecture; ObjectId/String/Array/embedded values; insert/find/update/delete; $gt/$lt/$in/$and/$or; sort/limit/projection; embedding/references; basic indexing/optimization; $match/$group/$sum/$avg.
- Replication and sharding are **conceptual only**. The reference server is standalone; there is no configured/failover-tested replica set, sharded cluster or external application deployment.
- Real tested runtime: **MongoDB Community Server 9.0.4**, **mongosh 2.14.0**, **Debian 13 x86_64**. Packages came from MongoDB’s signed trixie/9.0 repository. These are reference versions, not a timeless latest-release/security claim.
- Private server: localhost port 27027, authentication enabled, small WiredTiger cache. Data and credential files are outside the project in an excluded runtime cache; none are shipped in notes or the download.
- Fourteen displayed scripts were actually executed through mongosh with fresh prefix-guarded databases. Cleanup captures the original database and removes only that namespace.
- Observed examples include duplicate key **11000**, matched no-op **1/0**, absent update **0/0**, mixed-projection error **31254**, and client-side **MongoInvalidArgumentError** for a non-operator updateOne.
- Forced explain comparison: identical 3 results; natural scan examines 6 documents, named compound index examines 3 documents and 3 keys. Hints are explicit; no guaranteed wall-clock speedup is claimed.
- Aggregation: paid book count 3 / total 600 / average 200; tool count 2 / total 1000 / average 500. All 6 source orders remain.
- Guarded stock example: two sequential successes from stock 2, then zero matched; final stock 0. Not a concurrent load test or payment-plus-stock transaction.
- A missing course reference is deliberately accepted and handled as null; no automatic foreign-key enforcement is implied.
- The downloadable ZIP has exact displayed sources, real observed outputs, a credential-free mongosh runner, synthetic student CSV and non-secret runtime metadata.

### Unit 2 primary technical references

- [MongoDB official installation](https://www.mongodb.com/docs/manual/installation/) and [Linux OS selector](https://www.mongodb.com/docs/manual/administration/install-community-linux/). Checked Debian 13 support and the signed 9.0 APT procedure in the Debian section.
- [Install mongosh](https://www.mongodb.com/docs/mongodb-shell/install/).
- [Documents/BSON](https://www.mongodb.com/docs/manual/core/document/).
- [CRUD](https://www.mongodb.com/docs/manual/crud/) and [projection rules](https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/).
- [Data modeling best practices](https://www.mongodb.com/docs/manual/data-modeling/best-practices/).
- [Indexes](https://www.mongodb.com/docs/manual/indexes/) and [aggregation pipelines](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/).
- [Replication](https://www.mongodb.com/docs/manual/replication/) and [sharding](https://www.mongodb.com/docs/manual/sharding/), used for concepts only, not setup instructions.

Reproduce the private runtime: `bash tools/setup_mongodb_runtime.sh`; start the printed server command through the process manager; then `python3 tools/mongodb_content.py --bootstrap`.
Build: `python3 tools/build_DI04000031_u2.py`.
Validate: `python3 tools/test_DI04000031_u2.py` and the Unit 1 regression suite.


## Unit 3 — Cassandra reference and execution record

- Official Unit 3: **12 hours / 20%**; CO3: “Design and implement distributed datasets using Cassandra’s data model and CQL.” Practicals **4–6** cover setup/system keyspaces/key design, CQL CRUD/query restrictions, and an AI-related sensor/recommendation dataset with distribution/simple analytical query demonstrations.
- Covers installation/cqlsh; keyspaces, typed tables/columns and logical partitions; partition versus clustering keys; Create/Alter/Drop keyspaces/tables; int/text/timestamp and supporting native types; INSERT/SELECT/UPDATE/DELETE; WHERE, IN, ORDER BY, LIMIT and filtering restrictions. Query-first denormalization, bounded buckets and tombstones are explained at the needed learning level.
- **nodetool/cluster health is awareness only**. The only management observation is read-only status: one local **UN** node. No repair, compaction, decommission, replica-failure injection, multi-node availability, cloud deployment or cluster-operations lab is claimed.
- Actual runtime: **Apache Cassandra 5.0.9**, **CQL 3.4.7**, **cqlsh 6.2.0**, bundled Python driver **3.29.0**, explicit native protocol **v4**, **Temurin 17.0.21+9 JRE**, **Python 3.13.16**, **Debian 13 x86_64**. These are observed reference versions, not a timeless latest/security guarantee. Docs specify Java 11/17 and list older cqlsh Python ranges; the shipped 5.0.9 client was actually tested on this Python rather than assuming compatibility.
- Downloads came from official Apache/Adoptium locations. The Apache 5.0.9 tarball was verified against its published SHA-512; the Temurin runtime against SHA-256. `tools/setup_cassandra_runtime.py` contains the pinned digests. This is checksum verification, **not** a claim of PGP signature verification.
- The reference runs on one private local node, `datacenter1`, with NetworkTopologyStrategy/RF **1** in each disposable lab keyspace. The unusual reference CQL port is **9043**; the normal default is **9042**. CQL/internode/JMX remain private. CQL authentication alone is not production TLS/management hardening.
- A private admin was created outside the project; private credential files are mode **0600**. Factory credentials were rotated, login disabled and superuser status removed. Actual anonymous and old-default native-protocol connection attempts were rejected with **AuthenticationFailed**. No real password or database/runtime files are in the deliverables.
- Fourteen complete independent CQL scripts were actually executed with the real native driver; cqlsh-specific **COPY FROM** was delegated to real matching cqlsh. Displayed result rows are returned server rows, serialized as JSON preserving server row order; timestamps render ISO UTC and CQL date/UUID values display as strings. No fake server result generator is used.
- Guarding is for the **trusted prepared teaching files**, not arbitrary untrusted SQL or a security sandbox. The runner accepts one fresh `di04000031_u3_…` keyspace, refuses a pre-existing name, records ownership only after CREATE succeeds, and finally cleans its captured owned namespace. Tests preserve a sentinel in a pre-existing namespace; a deterministic real-DDL CREATE interleaving also verifies that **AlreadyExists** does not confer cleanup ownership. An unexpected post-CREATE failure cleans the runner’s own namespace only.
- The shared synthetic CSV has **8 rows / 4 logical device-day partitions**: S01/day29 three rows 30/31/32; S02/day29 two 28/29; S01/day30 two 33/34; S03/day29 one 27. Times are fixed explicit UTC. Four logical partitions are **not** four physical machines/replicas or empirical distribution/failover evidence.
- A real CSV import defect was caught during development: the default date parser accepted the date prefix and assigned midnight, so eight processed inputs upserted into four full keys. The published source specifies **DATETIMEFORMAT='%Y-%m-%dT%H:%M:%S%z'**; the runner uses UTC for its COPY subprocess. Tests compare **every stored key/value/time** against the fixture, rather than trusting the processed-row message. Current source and ZIP runs store all eight correctly; latest S01/day29 is **09:02 UTC -> 32.0**. The exported runner also matches under an outer **Asia/Kolkata** timezone.
- Observed ordinary INSERT/UPDATE upserts retain omitted existing columns, create missing-key rows, and do not produce MongoDB-style modified/deleted counts. Actual rejected non-key/type/null-key/order/key-mutation queries report **InvalidRequest**; bad syntax reports **SyntaxException**. These are true server classes, not invented numeric codes or mislabeled client errors.
- A 32 -> 35 correction in the base query table leaves its denormalized second table at 32 until the explicit second write. No automatic cross-table correction, foreign-key/cascade enforcement or SQL transaction is claimed.
- Bounded per-partition features are actual CQL aggregates: S01/day29 **count 3 / sum 93 / mean 31 / min 30 / max 32**; other means **28.5 / 33.5 / 27.0**. They illustrate report/model input features, not a trained model, real live hardware, an ingestion benchmark or a cluster-wide real-time SLA.
- The downloadable deterministic ZIP contains **32 files**: 14 exact CQL scripts, 14 real captured outputs, credential-free guarded runner, synthetic sensors.csv, non-secret runtime.json and README. No dependency binaries or runtime data are bundled; ZIPs are workspace downloads, not automatically hosted public URLs.
- Content inventory: **18 lessons**, **13 self-contained mobile SVGs**, **14 executable examples**, **14 reference cards**, **52 answered viva**, **16 answered practical revision tasks**. Tasks are in Notes; `exam_questions` is empty and no official theory-paper marks are invented.
- Unit 3 validation has **32 groups**: real source runs and exact outputs; all stored CSV values/timestamps; genuine rejections; denied anonymous/factory logins; namespace collision/creation ownership/failure cleanup; lexer/guard/driver fallback checks; safe English HTML and links; all SVG raster/text bounds and visual review; five preview views; all 14 exported ZIP executions; catalog/hash/embedded SVG integration with prior units preserved; timezone portability; byte-identical rebuild and secret exclusions. Native app-render CI and post-publication live-byte/hash checks are additionally required for release.

### Unit 3 primary technical references

- [GTU DI04000031 syllabus, effective 2025–26](https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf)
- [Apache Cassandra official downloads](https://cassandra.apache.org/_/download.html)
- [Installing Cassandra 5.0.9](https://cassandra.apache.org/doc/5.0.9/cassandra/installing/installing.html)
- [CQL data definition: keyspaces, keys and tables](https://cassandra.apache.org/doc/5.0.9/cassandra/developing/cql/ddl.html)
- [CQL data manipulation: reads and writes](https://cassandra.apache.org/doc/5.0.9/cassandra/developing/cql/dml.html)
- [CQL data types](https://cassandra.apache.org/doc/5.0.9/cassandra/developing/cql/types.html)
- [Query-first Cassandra versus relational modeling](https://cassandra.apache.org/doc/5.0.9/cassandra/developing/data-modeling/data-modeling_rdbms.html)
- [Physical data-model design](https://cassandra.apache.org/doc/5.0.9/cassandra/developing/data-modeling/data-modeling_physical.html)
- [cqlsh commands, credentials and COPY](https://cassandra.apache.org/doc/5.0.9/cassandra/managing/tools/cqlsh.html)
- [nodetool status: read-only cluster information](https://cassandra.apache.org/doc/5.0.9/cassandra/managing/tools/nodetool/status.html)
- [Cassandra security and network boundaries](https://cassandra.apache.org/doc/5.0.9/cassandra/managing/operating/security.html)
- [CQL built-in aggregate functions](https://cassandra.apache.org/doc/5.0.9/cassandra/developing/cql/functions.html)

For the exact reference environment: `python3 tools/setup_cassandra_runtime.py` verifies/extracts pinned official downloads and prints a private foreground start command. Start it with the managed process tool, then `python3 tools/cassandra_content.py --bootstrap` to set private authentication; do not expose or run duplicate servers. The private runtime is excluded from the project and the public ZIP does not silently install/modify an account.

Build: `python3 tools/build_DI04000031_u3.py` (real Cassandra required).
Validate: `python3 tools/test_DI04000031_u3.py` and prior-unit regressions.
Export the already built practical ZIP without a DB connection: `python3 tools/export_DI04000031_u3_practicals.py`.
Release only after exact-new-commit native app CI, then publication and fresh live JSON/SVG/catalog-byte/hash verification. Units 4–5 remain pending.
