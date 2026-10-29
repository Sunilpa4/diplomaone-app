# DI04000031 — Source and scope record

Checked: **29 October 2026**. The materials cover **Units 1–5**; Unit 5 is intentionally concise at the user’s request.

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
Release only after exact-new-commit native app CI, then publication and fresh live JSON/SVG/catalog-byte/hash verification. At the Unit 3 release, Units 4–5 were still pending.


## Unit 4 — Neo4j reference and execution record

- Official Unit 4: **12 hours / 20% content weightage**; CO4: “Utilize Neo4j to solve relationship-based problems with graph queries.” Application-oriented graph concepts, installation, basic Cypher/graph operations; graph-algorithm **examples only, not implementations or mathematical proofs**. Syllabus-named LinkedIn/Netflix/banking contexts are taught as workload analogies, not verified company-deployment claims.
- **Practical 7** explicitly calls for Desktop or Aura setup and Browser exploration; **Practical 8** asks for nodes/relationships and MATCH/WHERE/RETURN plus friend-recommendation/fraud-use-case demonstrations. The material gives the official Desktop/Aura/Browser procedure and asks students for their own actual GUI observations. The reference is **not** an installed Desktop, provisioned Aura service or automated Browser GUI proof.
- Actual private reference: **Neo4j Community 5.26.32**, matching **Cypher Shell 5.26.32**, official Python **neo4j driver 5.28.8**, negotiated **Bolt 5.8**, **Temurin 21.0.13+9 JRE**, **Python 3.13.16**, **Debian 13 x86_64**. LTS 5.26 coexists with newer calendar-version releases; these patch versions are observations, not timeless latest/security guarantees. Tested Debian 13 does not imply vendor certification for an OS absent from the versioned matrix.
- Verified official `neo4j-community-5.26.32-unix.tar.gz` (152610441 bytes), SHA-256 **d279ae6a9b38034280681a558b0cd222dce89f87cc3d9867f1f7bd28ef5ebc30**. Verified official Adoptium `OpenJDK21U-jre_x64_linux_hotspot_21.0.13_9.tar.gz` (52181297 bytes), SHA-256 **a535a1df9c6284d9618872984e026ae0352d1f7e9e0605425c0e6114f47351dd**. `tools/setup_neo4j_runtime.py` pins/verifies these. This is checksum verification, not a separate signature-verification claim.
- CQL from Unit 3 is not Cypher. The server, Desktop, Browser, Aura and driver are distinct products/interfaces; version executable output alone is not storage/connectivity proof. Matching Cypher Shell actually queried the server and ran full positive probe/social scripts; all sixteen reference scripts also executed through the official native driver.
- One private local Community instance; no public database endpoint, cluster/failover test, real bank/customer data, performance benchmark or trained model. Reference Bolt/HTTP ports **7688/7475**, usual local defaults **7687/7474**. Authentication is enabled; a random private initial password was configured **before first launch**. Private credentials are mode **0600**, outside the project in the excluded runtime cache. Actual anonymous and old-default-password connections returned **Neo.ClientError.Security.Unauthorized**, while authorized access still succeeded. Configured server usage reporting and driver telemetry are disabled. Local unencrypted access is not production TLS/authorization hardening; remote/Aura instructions preserve TLS verification.
- The constrained reference heap/page cache is not production sizing advice; GTU recommends an 8 GB learning machine. No host service, system-wide Java replacement, root database service or commercial/cloud resource was automatically provisioned.
- Sixteen complete independent sources execute actual Cypher in per-statement implicit auto-commit transactions. Returned rows and summary counters are real, JSON-serialized preserving result order; date/datetime display is normalized. Unstable internal IDs, timings and non-error notifications are not invented as stable outputs. The whole file is **not** one atomic transaction.
- Community examples share the `neo4j` database; they do **not** create sixteen separate databases. Each prepared file first atomically CREATEs a uniquely named fresh ownership constraint and then a scoped marker. This avoids treating a non-unique plain marker-node CREATE as an atomic claim. Existing scope nodes/schema are refused; no IF NOT EXISTS is used to falsely infer ownership. Finally cleanup removes only captured owned nodes and successfully created constraints, releasing the claim last. The guard is for **trusted prepared scripts**, not arbitrary untrusted Cypher or production security/authorization.
- Tests preserve a sentinel in an existing-node scope and a constraint-only scope. A deterministic interleaving uses **real server DDL/rejections** to insert another creator after preflight; the failed CREATE does not gain ownership or delete that creator’s graph/schema. Unexpected post-claim failures and missing/invalid fixture cases clean only the owned scope. Ambiguous/interrupted runs require inspection, not blanket deletion.
- Typed graph properties include real strings/integers/floats/booleans/lists/date/datetime. Nodes can have several labels; relationships have one type and stored direction. An undirected read does not create reverse edges. Application IDs are not assumed stable internal IDs. A label alone does not create uniqueness/existence requirements.
- Actual MERGE example: Jai/P09 visits **1 -> 2**, one business node. MATCH+SET for absent P99 creates nothing and leaves six people, unlike Cassandra UPDATE upsert. SET/REMOVE retain the selected other data; plain connected-node DELETE is rejected; DELETE relationship preserves endpoints; DETACH removes the selected node and all incident relationships, not automatically all other endpoints or physical bytes.
- OPTIONAL MATCH actual observation: **six rows / one non-null mentee**. Asha mentors Ravi; other optional mentees are null. A later non-null filter deliberately removes unmatched rows.
- Business uniqueness is observed with an **ONLINE** backing index, not a speedup benchmark. A single statement creates P98 then attempts duplicate P01; the real rejection leaves **P98 count 0**, proving rollback of that statement. A later “No ID” person is accepted: uniqueness alone is not required-property enforcement. Enterprise-only key/existence/type policies are not claimed as implemented Community features.
- Real failure codes include **Neo.ClientError.Schema.ConstraintValidationFailed** (connected DELETE / duplicate ID), **Neo.ClientError.Statement.TypeError** (nested map-valued stored property), **Neo.ClientError.Statement.SyntaxError** (unbound variable / malformed pattern) and **Neo.ClientError.Statement.SemanticError** (null MERGE identity). No invented numeric codes or mock server class substitutions.
- Fixed official-driver query parameters really treat the selector-shaped name as a literal unmatched value, not query text. `:param` is a client command; `// @params`, `@params_file`, `@result`, `@expect`, `@stats` are ordinary comments interpreted by the exported runner, not new Cypher syntax. Parameterization does not replace authorization/validation/privacy.
- Actual JSON/UNWIND import verifies **every one of six people and six directed KNOWS edges**, including all business IDs/names/cities/ages and endpoints/since years, against `graph_fixture.json`. The same file’s movie/banking sections are separate scenario inputs, not secretly imported extras in program 15. The input is a synthetic snapshot, not LOAD CSV, live ingestion or an AI pipeline benchmark.
- Social fixture: P01 Asha/Surat/20; P02 Ravi/Bharuch/21; P03 Neha/Surat/19; P04 Meera/Vadodara/22; P05 Imran/Surat/20; P06 Dev/Rajkot/23. Stored KNOWS edges: P01->P02, P01->P03, P02->P04, P03->P04, P02->P05, P04->P06. Basic two-hop candidates for Asha are **P04 Meera / P05 Imran** after self/direct-link exclusion and DISTINCT; Meera has two paths, Dev is three hops away.
- Movie fixture: Asha likes M01 Graph Journeys; Ravi likes M01/M02 Database Stories; Neha likes M03 Space Signals. Unseen candidates via known people are **M02 / M03**, not a trained/ranked recommender or Netflix-deployment proof.
- Banking fixture: D01 used by A01/A02/A04 yields **A01–A02 / A01–A04 / A02–A04**. D02 used only by A03 yields no pair. Shared-device output is a **review candidate, not a fraud verdict**. Family/public devices, reassignment and data errors can be legitimate. Context, consent, retention, false positives, provenance and human review are explicit.
- Similarity/common-neighbour intuition, centrality, community detection, path finding and link-prediction ideas are **conceptual examples only**. The executed queries are introductory pattern demonstrations required by Practical 8, not implementations of those algorithm families. No GDS/APOC procedures are installed, no graph-algorithm implementation/pseudocode/proof is shipped, and no AI accuracy/relevance/latency uplift is claimed. A community is not automatically a fraud ring and a graph does not automatically make AI true/unbiased/authorized.
- Deliverables: **20 lessons / 16 real programs / 14 self-contained mobile SVGs / 16 reference cards / 56 viva answers / 18 answered practical tasks**. The practical-only course has `exam_questions: []`; tasks appear in Notes, without invented official theory-paper marks.
- Deterministic practical ZIP: **37 files** — 16 exact Cypher sources, 16 actual expected outputs, guarded runner, requirements, synthetic graph_fixture.json, non-secret runtime.json and README. Export is proven DB/network-independent and does not import the executable program module. The ZIP is a workspace download, not an invented hosted download URL.
- **36 Unit 4 validation groups** cover current real runs/outputs, full fixture equality, genuine failures and counters, actual Cypher Shell scripts, denied access, atomic creation ownership/collision/failure cleanup, lexer/context/fixture guards, safe English HTML/links, all SVG raster/text bounds and visual review, all 16 public ZIP reruns, five preview views, catalog/hash/app-font-normalized SVG integration, byte-identical rebuild/offline export and secret exclusions. Raster validation uses resvg-py **0.5.0** (older 0.2.4 does not accept fractional zoom).
- Unit 1’s **20 groups** are rerun. Units 1–3 source JSON and their exported public JSON are preserved against their prior verified SHA-256 values. MongoDB/Cassandra runtime suites are not relabeled as rerun after a snapshot discarded their excluded runtimes. Exact-new-commit native Flutter rendering additionally covers all released content before publishing, followed by fresh LIVE byte/hash checks. At the Unit 4 release, Unit 5 was still pending.

### Unit 4 primary references

- [GTU DI04000031 syllabus, effective 2025–26](https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf)
- [Neo4j property-graph concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/)
- [Neo4j deployment choices and releases](https://neo4j.com/deployment-center/)
- [Neo4j 5 system and Java requirements](https://neo4j.com/docs/operations-manual/5/installation/requirements/)
- [Neo4j 5 Linux tarball installation](https://neo4j.com/docs/operations-manual/5/installation/linux/tarball/)
- [Neo4j Desktop installation](https://neo4j.com/docs/desktop/current/installation/)
- [Aura: create an instance](https://neo4j.com/docs/aura/getting-started/create-instance/)
- [Neo4j Browser: connect to an instance](https://neo4j.com/docs/browser/operations/dbms-connection/)
- [Cypher Shell client guide — reference client 5.26.32](https://neo4j.com/docs/operations-manual/current/cypher-shell/)
- [Cypher 5 MATCH](https://neo4j.com/docs/cypher-manual/5/clauses/match/)
- [Cypher 5 CREATE](https://neo4j.com/docs/cypher-manual/5/clauses/create/)
- [Cypher 5 MERGE](https://neo4j.com/docs/cypher-manual/5/clauses/merge/)
- [Cypher 5 SET](https://neo4j.com/docs/cypher-manual/5/clauses/set/)
- [Cypher 5 DELETE](https://neo4j.com/docs/cypher-manual/5/clauses/delete/)
- [Cypher 5 OPTIONAL MATCH](https://neo4j.com/docs/cypher-manual/5/clauses/optional-match/)
- [Cypher 5 constraints and edition boundaries](https://neo4j.com/docs/cypher-manual/5/constraints/)
- [Cypher 5 parameters](https://neo4j.com/docs/cypher-manual/5/syntax/parameters/)
- [Neo4j Graph Data Science algorithm families — conceptual reference only](https://neo4j.com/docs/graph-data-science/current/algorithms/)

The older `.../operations-manual/5/cypher-shell/` and `.../cypher-shell/current/` locations returned not-found pages; use the verified Operations Manual **current** Cypher Shell link above for client guidance, while recording the actually tested 5.26.32 client. `.../constraints/managing-constraints/` is obsolete; the versioned constraints index links create/list/drop pages.

Reproduce the private reference: `python3 tools/setup_neo4j_runtime.py` verifies/extracts official downloads and initializes a private password before the first launch; start its printed foreground command through the managed process tool. Do not reset an existing authentication store, run duplicate processes or publish the credential file.
Build: `python3 tools/build_DI04000031_u4.py` (real authenticated Neo4j required).
Validate: `python3 tools/test_DI04000031_u4.py` plus Unit 1 regression / prior-unit preservation checks.
Export the already built ZIP without database/network access: `python3 tools/export_DI04000031_u4_practicals.py`.
Release: source sync -> exact-new-SHA native app CI -> publication -> fresh live bytes/catalog hash verification. Redis was not included in that Unit 4 release.


## Unit 5 — concise Redis coverage

- User requested topic coverage without extended detail: **8 short lessons / 8 executed examples / 4 diagrams / 8 reference cards / 12 viva / 5 brief tasks**. Official scope is 10 hours / 17%, CO5, Practical 9: Strings, Lists, Sets, Hashes, basic commands, transactions/caching, AI/real-world uses and simplified integration. No advanced extras or theory-paper marks.
- Actual reference: **Redis server and redis-cli 8.10.3**, official **redis-py 8.1.0**, Python 3.13.16 on Debian 13 x86_64. Official source archive (21647086 bytes) SHA256 **edde778f6bdee7581e42fc139ca9e07e2822212092f7501f99989656e3629d02**, matched the official redis/redis-hashes entry. A browser-style User-Agent was needed after the first download request returned 403. Core/CLI were built with libc/-O2, no optional modules or TLS build; checksum verification is not a separate signature-verification claim.
- Private authenticated loopback **6385**, default user disabled, restricted course-key lab ACL and separate private admin. Passwords/ACL files remain mode 0600 outside the project/cache snapshot. No persistence, public endpoint, cluster, model training, benchmark or live second-database integration is claimed. The nonfatal host-overcommit warning was not “fixed” by changing host settings; no background-save/replication demonstration is made.
- Real outcomes: string/counter 10 -> 11; list load/train/evaluate then pop load; set duplicate removal; hash named string fields; MULTI/EXEC returns [11,"11"]; a real execution-time integer error still permits the later SET. Actual redis-cli tests also verify four structures, EXEC and DISCARD. No rollback guarantee is invented.
- Expiry is genuinely checked both immediately and with elapsed TTL; -2 means missing. Cache hit/miss/invalidation and versioned recommendation IDs are demonstrated. Python + Redis cache-aside really runs; its authoritative source is explicitly a **local dictionary fixture**, not MongoDB/Cassandra or a trained model.
- Shared helper uses a fresh prefixed namespace, SET NX ownership claim, declared-key-only cleanup and watched ownership. Pre-existing scope/collision/claim-race data are preserved; changed ownership is not deleted. This is trusted prepared Python, not an arbitrary-code sandbox or a distributed-lock implementation. No FLUSH cleanup.
- **24 validation groups passed**: real versions/results, all 8 extracted-ZIP reruns, four real structures, transaction/error semantics, natural expiry, actual CLI, auth/ACL denials, ownership/failure cleanup, safe English HTML, four SVGs rasterized/bounds-checked/visually reviewed, five preview tabs, deterministic rebuild, offline export and secrets checks. Rasterization uses app-normalized DejaVu fonts explicitly; a first diagnostic lacking the sans-serif fallback rendered empty text and was corrected before visual approval.
- **20-file ZIP** contains 8 short Python examples, 8 actual outputs, shared lab.py, requirements, non-secret runtime and a brief README. Export is database/network independent. No private server binaries or credentials ship.
- Units 1–3 remain byte-identical. Unit 4 changes only **three text leaves** (one Notes paragraph and one viva question/answer) to replace obsolete “Unit 5 pending” wording with a timeless Redis-scope statement. Its 16 programs, actual outputs, runtime evidence and 14 diagrams are unchanged; reversing those three wording edits reproduces both original source/public SHA256 values. Its metadata tests now allow Unit 5. No old database suite is falsely claimed as re-executed for those wording changes.
- Companion Unit 1 comparative-study regression: **20 groups passed**; its workbook rebuild changed only package creation/modification timestamps, so the original workbook bytes were restored. Final Redis scoped-key scan was empty, and the private Redis process shut down cleanly before database-independent export/CI.
- Publication remains gated on exact-new-commit native app rendering, followed by fresh live bytes/catalog/hash verification. Full subject availability is **[1,2,3,4,5]** only after that gate.

Primary Redis references: official installation/data-types/commands/transactions/expiry/security and redis-py guides listed in unit5.json; curriculum remains the original GTU DI04000031 PDF. Redis-cli guide path `/docs/latest/develop/cli/` returned not found and is not published as a reference.
