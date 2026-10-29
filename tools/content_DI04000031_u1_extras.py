"""NoSQL Unit 1: 12 reference cards, 48 viva answers, 16 practice tasks.

No invented theory-paper marks: DI04000031 has practical assessment only.
Practice tasks are shown as answered note cards, not an official exam tab.
"""
from nosql_content import SX, V, Q, tr


def G(title, items): return {'title': tr(title), 'items': items}

SYNTAX = [
    G('Model and Design Reference Cards', [
        SX('Selection rule', 'data shape + access pattern\n+ scale/retention + guarantees\n-> model + reasons + trade-off',
           'A product name alone is not a design justification. Write the actual reads and writes first.'),
        SX('Relational and NoSQL are options, not enemies', 'RDBMS: tables, relations, SQL, constraints\nNoSQL: several non-relational models\nBoth: evaluate actual product guarantees',
           'Do not claim that relational systems cannot distribute data, or that every NoSQL system lacks transactions or schema.'),
        SX('Scaling versus copies', 'scale up: increase one server\nscale out: add machines\npartition: different subsets\nreplicate: copies of the same data',
           'A network partition is a communication failure, not a data-partition key. A replica is not an independent backup.'),
        SX('Document model illustration', '{\n  "_id": "P102",\n  "name": "NoSQL Guide",\n  "attributes": {"pages": 320}\n}',
           'Valid illustrative JSON, not captured MongoDB output. MongoDB stores BSON and can enforce validation.'),
        SX('Known-key cache illustration', 'key: recs:U42:v1\nvalue: ["P101", "P102"]\nTTL policy: 300 seconds\nmiss -> source or recomputation',
           'Conceptual layout, not a Redis command transcript. Include model version, expiry and stale-data policy.'),
        SX('Wide-column query-first layout', 'partition: (sensor_id, day)\norder inside partition: ts\nquery: one sensor/day + time interval',
           'Conceptual layout, not executable CQL. Cassandra uses typed columns; partition size and hot keys need review.'),
        SX('Graph relationship illustration', 'Ravi -LIKES-> P101 <-LIKES- Asha\nAsha -LIKES-> P102\npossible candidate for Ravi: P102',
           'A connection-path heuristic, not a trained recommendation model or executed Cypher query.'),
    ]),
    G('CAP, AI and Practical Reference Cards', [
        SX('CAP definitions', 'C: one current logical copy\nA: valid operations eventually complete\n   at non-failed nodes\nP: account for communication partitions',
           'C means linearizable operation behaviour in CAP. A has no fixed latency bound in the formal definition.'),
        SX('During a partition', 'protect C -> some operations may wait/fail\nprotect A -> latest shared state may fail\nhealthy link -> C and A may coexist',
           'This is a basic trade-off summary, not an unconditional choose-any-two slogan or a fixed product classification.'),
        SX('AI data roles', 'profiles -> Document\nknown-key cache -> Key-Value\npartitioned event history -> Wide-Column\nconnected patterns -> Graph',
           'Starting points under the stated access patterns. A database supports AI data work; it does not itself train the model.'),
        SX('Polyglot persistence', 'orders: authoritative relational store\nproducts: optional document store\nrecs: optional key-value cache\nmore stores -> more operational cost',
           'Use multiple stores only when their benefit justifies synchronization, backup, security and maintenance work.'),
        SX('Practical 1 journal', 'aim -> scenario -> access pattern\n-> four-type comparison -> model sketch\n-> choice + 2 reasons + 1 trade-off\n-> CAP analogy -> conclusion + sources',
           'Comparative study evidence is not a benchmark. No theory-paper marks are assigned to these reference cards or practice tasks.'),
    ]),
]

_BASICS = [
    V('What does NoSQL mean?', 'A broad group of database approaches beyond the traditional relational model, often expanded as Not Only SQL. It is not one language or one product.'),
    V('Name the four models in this syllabus.', 'Document, Key-Value, Wide-Column and Graph.'),
    V('Give one course product for each model.', 'MongoDB: Document; Redis: Key-Value/data structures; Apache Cassandra: Wide-Column; Neo4j: Graph.'),
    V('Does NoSQL mean SQL must never be used?', 'No. The category concerns data models and approaches. CQL, for example, has SQL-like syntax without being a relational query model.'),
    V('Does every NoSQL database have no schema?', 'No. Cassandra CQL tables have declared types, MongoDB supports validation, and every application still needs a deliberate data model.'),
    V('Does every NoSQL product lack transactions?', 'No. Transaction support and its scope depend on the product, version and configuration. Evaluate the actual guarantees.'),
    V('Give two reasons to consider a NoSQL model.', 'Varying nested records may fit documents; relationship-heavy multi-hop questions may fit a graph. The access pattern must justify the choice.'),
    V('When can an RDBMS remain the better default?', 'Stable relational data with constraints, joins, atomic multi-row updates and routine SQL reporting, especially when one database already serves the workload well.'),
    V('What is an access pattern?', 'A specific way the application reads or writes data, such as fetching a profile by user ID or reading one sensor/day time interval.'),
    V('Scale up versus scale out?', 'Scale up increases one machine\'s resources; scale out adds machines and distributes work or data. Neither guarantees a particular speedup.'),
    V('Partitioning versus replication?', 'Partitioning places different data subsets in different groups; replication keeps additional copies of the same data. A deployment can use both.'),
    V('Can a one-node lab prove partition tolerance?', 'No. It can exercise local operations but cannot establish how multiple isolated node groups handle a network partition.'),
]
_CAP = [
    V('Expand CAP.', 'Consistency, Availability and Partition tolerance.'),
    V('What does C mean in CAP?', 'Operations behave as one current logical copy, formally linearizability. A read started after a completed write must not return the older value in the basic read/write example.'),
    V('What does A mean in CAP?', 'Every valid data operation received by a non-failed node eventually completes with a valid result; the formal definition does not impose a fixed latency bound.'),
    V('What is a network partition?', 'A communication failure that prevents groups of nodes from exchanging messages, although nodes on both sides may still be running.'),
    V('State the basic CAP limitation.', 'During a network partition, a distributed read/write service cannot guarantee both a single up-to-date operation history and completion of every affected operation.'),
    V('Why is “choose any two, always” misleading?', 'The C/A conflict concerns partition conditions. When communication is healthy, a system may provide both consistency and availability; real networks cannot simply be assumed never to partition.'),
    V('How does the last-seat booking analogy protect consistency?', 'An isolated office that cannot safely verify the authoritative booking history defers the affected operation. A side may proceed only if the design can maintain its guarantee.'),
    V('What can happen if both isolated offices confirm from local data?', 'Both may confirm the same last seat. Reconciling later may require rejecting one confirmation and does not make the original operations strongly consistent.'),
    V('Is a “sold out” result necessarily a CAP availability failure?', 'No. An authoritative sold-out decision is a legitimate result. Deferring because authoritative state cannot be established during isolation is the availability sacrifice in the analogy.'),
    V('Is CAP consistency the same as ACID consistency?', 'No. CAP C is one-copy/real-time operation behaviour; ACID consistency is preservation of application/database constraints across transactions.'),
    V('What is eventual consistency in a basic explanation?', 'If updates stop, communication recovers and replication/conflict resolution operate appropriately, replicas can converge. It does not promise every earlier read was current.'),
    V('Should a database brand always be labeled CP or AP?', 'No. Explain topology, operations, settings and failure conditions. A brand label alone is insufficient to establish the guarantees.'),
]
_MODELS = [
    V('What is a document?', 'A record of named fields that can include nested objects and arrays. In MongoDB, documents are grouped in collections and stored as BSON.'),
    V('JSON versus BSON at this level?', 'JSON is a text representation used in the illustrations. BSON is MongoDB\'s typed binary document representation and supports more types than JSON.'),
    V('Why does a product catalog fit documents?', 'Products may have different nested attributes while common identifying fields remain consistent; one product can be read as a bounded record.'),
    V('What is the main lookup handle in a key-value model?', 'A unique key. In the example, recs:U42:v1 selects the cached recommendation IDs for a user and model version.'),
    V('What is TTL?', 'Time to live: a configured lifetime after which an entry expires. It is not proof that the value stayed correct during that lifetime.'),
    V('Is Redis limited to plain strings?', 'No. Redis supports data structures including the strings, lists, sets and hashes studied in Unit 5.'),
    V('What is query-driven Cassandra modeling?', 'Designing tables and keys from the application\'s queries, rather than expecting arbitrary relational joins to reconstruct normalized entities.'),
    V('What is a partition key in the sensor illustration?', 'The conceptual pair (sensor_id, day), grouping readings for one sensor and one date. The timestamp orders rows within that partition.'),
    V('Is wide-column the same as an analytical columnar warehouse?', 'No. Cassandra\'s partition-oriented wide-column model is not the same concept as columnar storage layouts optimized for analytical scans.'),
    V('What are the main parts of a property graph?', 'Nodes, labels, directed typed relationships and properties. Neo4j nodes and relationships can both have properties.'),
    V('Why use a graph for shared-device investigation?', 'The question follows account-to-device-to-account paths, making the relationships central to the access pattern.'),
    V('Does a graph guarantee every relationship query is fast?', 'No. Entry-point indexes, traversal depth, high-degree nodes, data volume and the actual query all affect cost.'),
]
_AI_LAB = [
    V('Which model is a starting point for evolving AI user profiles?', 'Document, when bounded nested profiles and selected field queries dominate. Validation and privacy still matter.'),
    V('Which model is a starting point for a known-key prediction cache?', 'Key-Value, with versioned keys, a TTL or invalidation rule, an acceptable staleness policy and a miss fallback.'),
    V('Which model can fit large sensor histories with sensor/day queries?', 'Wide-Column, using query-first time-bucketed partitions. Check hot sensors, retention and partition size.'),
    V('Which model can fit connected fraud patterns?', 'Graph, because paths among accounts, devices and payments are important. A suspicious path is not proof of fraud.'),
    V('Does choosing a NoSQL database train an AI model?', 'No. The database stores and serves data. Feature preparation, training/inference and model evaluation are separate tasks.'),
    V('What is polyglot persistence?', 'Using multiple storage technologies in one application, each for a justified workload, while managing ownership and synchronization.'),
    V('What is a source of truth?', 'The authoritative place for a fact, such as a committed payment record. A stale cache or copied view must not silently become authoritative.'),
    V('Name two costs of using several database products.', 'More backup/restore and monitoring work; more security/credential management and cross-store synchronization complexity.'),
    V('What is the official aim of Practical 1?', 'Study and compare the four NoSQL types, identifying their unique characteristics, advantages and application areas.'),
    V('Must Practical 1 install all four database servers?', 'No. Its official activity is comparative study. Installation and actual operations appear in the later product-specific practicals.'),
    V('What evidence belongs in a comparison journal?', 'An application/access pattern, a four-type matrix, model sketches, a justified choice with a trade-off, a CAP analogy, conclusion and sources. Clearly distinguish illustrations from measurements.'),
    V('Are these practice tasks an official GTU theory paper?', 'No. DI04000031 has 0 theory ESE and 0 theory PA, with 20 practical PA and 30 practical ESE. The tasks prepare understanding, journals and viva without invented question marks.'),
]
VIVA = [G('Foundations and Workload Selection', _BASICS), G('CAP and Failure Behaviour', _CAP),
        G('The Four Data Models', _MODELS), G('AI Uses and Practical 1', _AI_LAB)]
assert all(len(g['items']) == 12 for g in VIVA)

PRACTICE_QS = [
    Q('concept', 'Explain why an application may consider NoSQL. Give two situations where keeping an RDBMS is reasonable.',
      '<p>Consider NoSQL when the workload favors nested varying records, known-key caches, large partition-oriented event streams or multi-hop relationships. Explain the specific reads/writes, not just the data size.</p><p>Keep an RDBMS as a strong default for an auditable transfer ledger needing atomic multi-row updates, or a small stable college system needing constraints and SQL joins/reports. Relational products may also support JSON and distributed deployments; NoSQL is not universally faster.</p>'),
    Q('comparison', 'Distinguish scale up, scale out, data partitioning, replication and a network partition using one example each.',
      '<ul><li>Scale up: add RAM to one server.</li><li>Scale out: add storage/compute nodes.</li><li>Data partitioning: group readings by sensor/day and distribute groups.</li><li>Replication: keep additional copies of each group.</li><li>Network partition: a failed link prevents two running node groups from exchanging updates.</li></ul><p>Partitioning is not copying, and neither is the communication failure described by CAP.</p>'),
    Q('CAP', 'Define C, A and P in CAP. Explain why a healthy network is not an unconditional choose-two situation.',
      '<p>C: one current logical operation history; a read following a completed write cannot return the earlier value in the basic example. A: every valid operation received by a non-failed node eventually completes with a valid result. P: account for lost/delayed communication between groups.</p><p>During a partition, a service cannot guarantee both C and A for all affected operations. With healthy communication, both may be provided. No proof or quorum calculation is required in this unit.</p>'),
    Q('CAP analogy', 'Use Surat and Bharuch booking offices to explain the last-seat conflict and a consistency-first response.',
      '<p>Both offices start with one seat visible. The inter-office link fails. If each confirms from its local copy, two confirmations may claim one seat. A consistency-first design makes an office that cannot verify the authoritative history defer that operation; only a side able to maintain the guarantee may proceed.</p><p>The sacrifice is availability for some requests. Declining because a known authoritative record is sold out is different from deferring because authoritative state cannot be established.</p>'),
    Q('CAP application', 'A completed profile update at one office is followed by an old profile read at an isolated office. Which guarantee is missing?',
      '<p>The isolated read may have completed, preserving availability for that operation, but it did not behave like a current single copy after the completed update, so CAP strong consistency was not provided for the sequence.</p><p>Eventual repair does not change the old value already returned. Decide whether such staleness is acceptable for that profile field; do not assume it is acceptable for authorization or payment facts.</p>'),
    Q('CAP application', 'After two isolated caches accept updates, what must happen when communication returns?',
      '<p>They exchange changes and apply an explicit reconciliation/conflict policy. For a disposable recommendation cache, recomputing from the source may be suitable. For authoritative state, the policy must respect its business rules.</p><p>Restored communication alone is not proof of correct conflict resolution, and later convergence is not retroactive strong consistency.</p>'),
    Q('modeling', 'Sketch a document model for a book and an electronic sensor with different attributes. State one benefit and two design checks.',
      '<p>Use product documents with common _id, name and category fields. Put pages/language inside a book attributes object and sample_rate_hz/battery_powered inside the sensor attributes object.</p><p>The model keeps one bounded product together while allowing different fields. Validate common required fields/types and index actual query fields. Do not embed an unlimited review/event history in one document. These are model illustrations, not execution evidence.</p>'),
    Q('modeling', 'Design a known-user recommendation cache key and explain TTL, versioning and a cache miss.',
      '<p>Example key: recs:U42:v1; value: a small list of product IDs; expiry policy: 300 seconds. The user ID identifies the target and v1 identifies the model/result version.</p><p>TTL limits residence time, not correctness until expiry. Invalidate or version when required; on a miss fetch/recompute from the appropriate source. Do not use this cached list as an authoritative permission or stock decision.</p>'),
    Q('modeling', 'A sensor fleet is queried by sensor, date and time interval. Suggest a wide-column layout and one risk.',
      '<p>Use a conceptual (sensor_id, day) partition key and timestamp ordering inside the partition. A request targets one sensor/day and a bounded time range, matching a query-first access pattern.</p><p>Very high-rate sensors can still create hot or oversized partitions; estimate growth and retention. Another query may require another deliberately maintained table. This is not a claim of full SQL joins or measured performance.</p>'),
    Q('modeling', 'Draw the Ravi/Asha product graph and explain a simple candidate recommendation.',
      '<p>Draw Ravi -LIKES-&gt; P101, Asha -LIKES-&gt; P101, and Asha -LIKES-&gt; P102. The shared interest in P101 connects the people; Asha\'s additional interest makes P102 a candidate for Ravi, who does not already like it in the illustration.</p><p>Label nodes, relationship types and directions. This is a path-based heuristic, not a trained model, a guarantee of user preference or an executed Cypher result.</p>'),
    Q('comparison', 'Complete a four-row comparison with representation, example, typical access, advantage and trade-off.',
      '<ul><li>Document / MongoDB: nested document; product/profile reads; flexible bounded records; validate and plan embedding/indexes.</li><li>Key-Value / Redis: key to supported value; known-key access; simple low-latency operations; handle expiry, persistence and misses.</li><li>Wide-Column / Cassandra: typed partitioned tables; sensor/day ranges; distributed query-first writes; avoid hot partitions and unplanned joins.</li><li>Graph / Neo4j: nodes and typed relationships; bounded path traversal; connected-pattern queries; plan indexes/depth/high-degree nodes.</li></ul><p>State that these are typical fits, not universal performance rankings.</p>'),
    Q('AI application', 'Map four AI data needs to the four NoSQL types and explain why the database alone is not an AI model.',
      '<p>Nested learner profiles: Document. Known-key cached predictions: Key-Value. High-volume sensor/event history with planned partition queries: Wide-Column. Shared-device or recommendation paths: Graph.</p><p>Storage/querying is separate from feature generation, training, inference and evaluation. Enforce data quality, consent, retention and least privilege. A suspicious graph path is evidence to review, not proof of fraud.</p>'),
    Q('architecture', 'Propose a minimal polyglot shop design and identify the source of truth for payments.',
      '<p>Option: an RDBMS owns committed orders/payments; a document store owns product details if varied nested attributes justify it; a key-value cache stores disposable recommendation IDs.</p><p>Define ownership, refresh/miss behaviour, failure handling, backups and security. Payment confirmation must use the authoritative transaction record, not a cache. If one RDBMS already meets the workload, keep the simpler design.</p>'),
    Q('Practical 1', 'Prepare the journal structure and acceptance checklist for the official comparative practical.',
      '<p>Record aim; scenario; data/access pattern; all-four-type matrix; model sketches; chosen type; two reasons and a trade-off; a basic CAP analogy; conclusion and sources.</p><p>Check that all four types have characteristics, advantages and application areas. Distinguish illustrative records from actual observed runtime evidence. The official first practical does not require installing all four engines or inventing benchmark numbers.</p>'),
    Q('misconceptions', 'Correct these claims: “NoSQL has no schema”, “all NoSQL is AP”, “wide-column means an analytical columnar warehouse”, and “a graph database trains AI”.',
      '<ul><li>NoSQL covers several models; Cassandra CQL has typed schemas and MongoDB can validate documents.</li><li>CAP behaviour depends on deployment, operation, settings and failure conditions, not one label for every product.</li><li>Wide-column partition/query modeling is distinct from columnar analytical storage.</li><li>A graph stores/query relationships; model training/inference is separate, though graph data can support it.</li></ul>'),
    Q('selection', 'Choose a starting model for a changing catalog, known-key cache, sensor/day history, shared-device investigation and an atomic bank ledger. Justify each.',
      '<p>Catalog: Document for varying nested product records. Cache: Key-Value for known-key temporary results. Sensor/day history: Wide-Column for planned partition/time access. Shared devices: Graph for connection paths. Ledger: keep an RDBMS as a strong default for relational constraints and atomic multi-row transactions.</p><p>Each choice assumes the stated priorities; include its limitation and evaluate actual guarantees. A defensible alternative may be valid, and some NoSQL products do support transactions.</p>'),
]
assert len(PRACTICE_QS) == 16
assert sum(len(g['items']) for g in SYNTAX) == 12
