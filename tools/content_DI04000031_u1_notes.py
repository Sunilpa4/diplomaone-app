"""GTU NoSQL Unit 1: 14 English-only lessons, including Practical 1.

Models are illustrations for comparative study, not claimed engine output.
"""
from nosql_content import (make_T, table, json_text, DOCUMENTS, CACHE,
                           SENSOR_ROWS, MODELS, CASES, SOURCES)

SN = {
    'doc_sensor': json_text(DOCUMENTS[0]),
    'doc_book': json_text(DOCUMENTS[1]),
    'kv': 'Known key: recs:U42:v1\nValue: ["P101", "P102"]\nExpiry policy: 300 seconds\nOn a miss: recompute or fetch the source',
    'wc': 'Partition key: (sensor_id, day)\nClustering / order within partition: ts\nQuery shape: one sensor + one day\n             + bounded time interval',
    'graph': 'Ravi -LIKES-> P101 <-LIKES- Asha\nAsha -LIKES-> P102\nCandidate for Ravi: P102\nReason: a shared-interest path',
    'report': 'Aim and application scenario\nData shape and main access pattern\nComparison of all four NoSQL types\nChosen type + example product\nTwo reasons + one trade-off\nSketch and illustrative records\nCAP analogy + acceptable failure behaviour\nConclusion and sources\nEvidence: study, not a runtime benchmark',
}
T = make_T(SN)

SEC_1_1 = {
    'title': {'en': '1.1 Why NoSQL? Modern Workloads and RDBMS Trade-offs'},
    'items': [
        T('What NoSQL Means — and What This Unit Requires', """
<p><b>NoSQL</b> is a broad family of database approaches beyond the traditional relational model. It is often expanded as <b>Not Only SQL</b>. It is not one product, one query language or a rule that SQL must never be used.</p>
<p>The four models in this course are <b>Document, Key-Value, Wide-Column and Graph</b>. MongoDB, Redis, Apache Cassandra and Neo4j are representative products; products can have features beyond their main category.</p>
<p><b>Learning outcome CO1:</b> select and justify a suitable NoSQL type for an application. A strong answer connects <b>data shape + access pattern + required guarantees</b> to the model, and states a trade-off. Naming a popular database alone is not a justification.</p>
<p><b>Scope:</b> Unit 1 is 8 hours with 13% content weightage. Practical 1 is a <b>study and comparison</b>. Illustrative records and diagrams below are not database-server output. Installation and executed queries start in the later product-specific units.</p>
<p><b>Assessment:</b> GTU lists 0 theory ESE, 0 theory PA, 20 practical PA and 30 practical ESE: <b>50 total marks, 3 credits</b>. Practice tasks in these notes are revision and lab preparation, not an official theory paper or a per-question GTU marking scheme.</p>
"""),
        T('Why Applications Consider NoSQL — Without Dismissing RDBMS', """
<p>An RDBMS stores related facts in tables and provides SQL, constraints, joins and transaction facilities. It remains a strong default for ledgers, order/payment records and many reporting systems.</p>
<p>Modern applications can introduce pressures that make a different model worth evaluating:</p>
<ul><li><b>Varying nested records:</b> a book and a sensor have different attributes. A document may map to the application object more directly than many attribute tables.</li>
<li><b>Large event streams:</b> millions of device readings with known sensor/time queries may benefit from query-first, partition-oriented storage.</li>
<li><b>Known-key low-latency access:</b> sessions or short-lived recommendation caches can fit key-value operations.</li>
<li><b>Relationship-heavy questions:</b> following several account-device-person connections can be expressed naturally as graph paths.</li>
<li><b>Distributed growth:</b> adding nodes may help capacity, but creates communication, coordination and operational costs.</li></ul>
<p>These are <b>trade-offs, not absolute limitations</b>. Relational products can support JSON, replication, partitioning and distributed deployments. NoSQL products can provide validation, indexes and transactions. Evaluate the actual product and configuration.</p>
<p><b>Example:</b> keep authoritative payments in an RDBMS while considering a document catalog and a key-value cache. Do not replace a working relational system merely because the application is called modern or AI-based.</p>
""", diagram='ns1_workload'),
        T('Scale Up, Scale Out, Partitioning and Replication', """
<ul><li><b>Scale up:</b> increase one server's CPU, RAM or storage. It can be simple, but a single machine has capacity and cost limits.</li>
<li><b>Scale out:</b> add machines and distribute work or data. Benefits depend on workload, partitioning and coordination overhead; speed does not automatically multiply by the node count.</li>
<li><b>Data partitioning / sharding:</b> place different subsets of records on different nodes. For example, readings for different sensor/day keys can be placed in different partitions.</li>
<li><b>Replication:</b> keep copies of the same data on more than one node. It can support fault tolerance and read placement, but replicas must exchange updates.</li></ul>
<p><b>Do not confuse:</b> splitting 100 records into two groups of 50 is partitioning; holding two copies of all 100 is replication. A distributed system may do both.</p>
<p>A <b>data partition</b> is a storage grouping. A <b>network partition</b> in CAP is a communication failure between groups of nodes. The same word has different meanings.</p>
<p>NoSQL does not imply that every installation is a distributed cluster. A one-node demonstration cannot establish how a multi-node system behaves during a network partition. Replication is also not a substitute for an independent, restorable backup.</p>
""", diagram='ns1_scale'),
    ],
}

SEC_1_2 = {
    'title': {'en': '1.2 CAP Basics — Definitions and a Booking Analogy'},
    'items': [
        T('CAP: Consistency, Availability and Partition Tolerance', """
<p>CAP describes a fundamental limit for a distributed read/write service when communication can fail. This unit requires the <b>basic idea and an analogy</b>, not a proof or a quorum algorithm.</p>
<ul><li><b>C — Consistency:</b> operations behave like one up-to-date logical copy. In the basic read/write example, a read that begins after a write has completed must not return the older value. The formal notion is linearizability; overlapping operations require an order consistent with real time.</li>
<li><b>A — Availability:</b> every valid data operation received by a non-failed node eventually completes with a valid result. Merely returning a communication error or refusing an operation is not enough. The formal definition does not set a fixed response-time bound.</li>
<li><b>P — Partition tolerance:</b> the design must account for messages lost or indefinitely delayed between groups of nodes, even though those nodes may still be running.</li></ul>
<p><b>Core conclusion:</b> during a network partition, a service cannot guarantee <b>both C and A for every affected operation</b>. It must sometimes defer/refuse an operation to protect one consistent history, or complete an operation without guaranteeing the latest shared state.</p>
<p>When the network is healthy, consistency and availability can coexist. A practical design should explain its failure behaviour, not simply repeat “choose any two”.</p>
""", diagram='ns1_cap'),
        T('CAP Analogy: Two Booking Offices and One Last Seat', """
<p><b>Starting state:</b> Surat and Bharuch offices both know one seat remains. Assume they normally coordinate with one booking authority. The link between the offices fails; a clerk can still use the local office system.</p>
<p><b>Consistency-first behaviour (CP-style):</b> only the side that can safely maintain the authoritative booking history may confirm the last seat. An isolated office that cannot verify that history must defer the affected booking/check instead of issuing a potentially conflicting confirmation. Some client operations lose availability. Depending on the design, even the other side may need to pause; CP does not mean one office can always proceed.</p>
<p><b>Availability-first behaviour (AP-style):</b> each side continues from its local information. Both may still see one seat and issue a local confirmation. After communication returns, two confirmations can conflict over one seat. A reconciliation policy is needed, and a cancellation later does not make the earlier confirmations strongly consistent.</p>
<p><b>Application decision:</b> confirmed scarce-seat allocation usually values a single booking history more than accepting conflicting sales. A temporary stale recommendation list is often less harmful and may justify serving local cached data. The correct choice follows the business consequence.</p>
<p><b>Important distinction:</b> declining a booking because an authoritative record says “sold out” is a legitimate business result. Deferring it because the isolated office cannot establish the authoritative state is the availability sacrifice in this analogy.</p>
""", diagram='ns1_booking'),
        T('CAP Misconceptions and Eventual Convergence', """
<ul><li><b>Not an unconditional “choose any two” triangle:</b> the C/A conflict matters when a partition occurs. Ignoring partitions does not remove real network failures.</li>
<li><b>C is not the C of ACID:</b> CAP consistency concerns one-copy/real-time operation behaviour; ACID consistency concerns preservation of application/database constraints through transactions.</li>
<li><b>A is not “the website shows an error page”:</b> the requested data operation must complete with a valid result. A running process alone is not proof of availability.</li>
<li><b>P is not sharding:</b> network isolation is different from splitting stored data into groups.</li>
<li><b>NoSQL is not one fixed CAP category:</b> product behaviour depends on topology, operation, read/write settings and failure conditions. Avoid unconditional labels such as “every Redis deployment is AP”.</li>
<li><b>Eventual consistency:</b> with no further updates, restored communication and an appropriate replication/conflict policy, replicas can converge. It does not promise that every read was current during the failure or that conflicts resolve correctly without a policy.</li></ul>
<p><b>Quick example:</b> office A completes a profile update; a later read at isolated office B returns an older profile. The read stayed available, but the pair of operations did not provide CAP's strong consistency. A later repair cannot change what that read returned.</p>
<p>CAP does not select a database by itself, rank performance, or prove that all NoSQL systems lack transactions.</p>
"""),
    ],
}

_MODEL_MATRIX = table(
    ['Type / example', 'Main representation', 'Access pattern', 'Benefit / trade-off'],
    [[m['type'] + ' / ' + m['example'], m['shape'], m['access'],
      m['advantage'] + '. Trade-off: ' + m['tradeoff'] + '.'] for m in MODELS])
_SENSOR_TABLE = table(['Sensor', 'Day', 'Time', 'Reading (C)'],
                      [[r['sensor_id'], r['day'], r['ts'], r['reading_c']] for r in SENSOR_ROWS])

SEC_1_3 = {
    'title': {'en': '1.3 The Four NoSQL Database Models'},
    'items': [
        T('Document Databases — MongoDB as the Course Example', """
<p>A <b>document</b> stores a record as named fields whose values can include scalars, arrays and nested objects. A <b>collection</b> groups documents. MongoDB uses <b>BSON</b>, a typed binary representation; JSON-like text is used here to illustrate the shape.</p>
<p>These two products share an ID/name/category structure but have different nested attributes:</p>
@@doc_sensor@@
@@doc_book@@
<p><b>Typical access:</b> fetch a product by ID, or query selected fields with suitable indexes. A document model is useful for product catalogs, content and evolving AI user profiles.</p>
<p><b>Advantage:</b> data read together can often be kept together, reducing the need to assemble one record from many tables.</p>
<p><b>Trade-offs:</b> schema flexibility is not absence of design. Validate required fields and types, decide embedding versus references, avoid unbounded embedded arrays, and update duplicated facts carefully. MongoDB can enforce schema validation.</p>
<p><b>Illustration only:</b> these records are valid JSON fixtures, not captured MongoDB output. BSON types, installation and actual commands are studied in Unit 2.</p>
""", diagram='ns1_document'),
        T('Key-Value Databases — Redis as the Course Example', """
<p>A <b>key-value model</b> maps a unique key to a value. The key is the main lookup handle. The value may be a simple byte/string value or a richer supported data structure. Redis is a data-structure server, not only a store of plain text strings.</p>
@@kv@@
<p><b>Interpretation:</b> U42's recommendation result for model version v1 can be served by a known key. The application declares a 300-second expiry policy and handles a cache miss by fetching/recomputing the result.</p>
<p><b>Advantages:</b> simple known-key operations and low-latency access are useful for sessions, temporary counters, cached predictions and online features.</p>
<p><b>Trade-offs:</b> plan unique key names, memory use, invalidation, TTL and cache-miss behaviour. TTL is a configured lifetime, not a guarantee that every cached value remains correct until expiry. Persistence/durability depends on configuration.</p>
<p>Ordinary key lookup does not automatically solve arbitrary joins or every field-search requirement. Do not treat a possibly stale recommendation cache as the authoritative payment, authorization or stock record.</p>
<p><b>Illustration only:</b> the displayed key/value is not a Redis CLI transcript. Basic Redis strings, lists, sets, hashes and real commands belong to Unit 5.</p>
""", diagram='ns1_key_value'),
        T('Wide-Column Databases — Apache Cassandra as the Course Example', """
<p>A <b>wide-column store</b> organizes data for distributed access using row/column and partition concepts. In Cassandra's CQL interface, data is in <b>typed tables</b> with a primary-key design. Do not describe every wide-column product as having no schema.</p>
<p><b>Query-first example:</b> a monitoring application writes many sensor readings and normally asks for one sensor, one day and a bounded time interval.</p>
@@wc@@
""" + _SENSOR_TABLE + """
<p>The first two rows belong to one <b>(S01, 2026-10-29)</b> partition; the S02 row belongs to another. Within a partition, the clustering/time component supplies an order for range-oriented reads. Time buckets help bound growth, but a hot sensor or very high sample rate still needs sizing review.</p>
<p><b>Advantages:</b> high-volume distributed writes and predictable queries that target a planned partition.</p>
<p><b>Trade-offs:</b> design tables around queries; data may be duplicated for another access pattern. Cassandra does not provide relational joins and foreign-key integrity. Poor partition keys can produce hot or oversized partitions.</p>
<p><b>Do not confuse:</b> a wide-column database such as Cassandra is not the same concept as an analytical columnar warehouse that lays out column values for scans. CQL resembles SQL in spelling but does not imply full relational behaviour.</p>
<p>This is a conceptual model/table, not Cassandra query output. Installation, real CQL and partition/clustering-key syntax belong to Unit 3.</p>
""", diagram='ns1_wide_column'),
        T('Graph Databases — Neo4j as the Course Example', """
<p>A <b>property graph</b> represents entities as <b>nodes</b> and connections as <b>relationships</b>. Nodes may have labels; nodes and relationships can have properties. Neo4j relationships have a direction and a type.</p>
<p><b>Example:</b> Ravi and Asha like product P101; Asha also likes P102. Following the shared-interest path makes P102 a possible recommendation for Ravi:</p>
@@graph@@
<p><b>Typical access:</b> find friends-of-friends, shared account/device paths, dependencies, or connected knowledge entities. The connection path is central to the question.</p>
<p><b>Advantages:</b> relationship-heavy, multi-hop questions can be expressed directly in the model.</p>
<p><b>Trade-offs:</b> define meaningful relationship types, index starting nodes and bound traversal depth. Very broad traversals or high-degree nodes can still be expensive. A relational database can also store relationships; a graph is not always faster.</p>
<p>The drawn path is a <b>simple recommendation heuristic</b>, not a trained AI model and not a captured Neo4j query result. A shared device can indicate a pattern for investigation, not automatic proof of fraud. Actual Cypher and installation belong to Unit 4.</p>
""", diagram='ns1_graph'),
    ],
}

SEC_1_4 = {
    'title': {'en': '1.4 AI-Focused Use Cases and Responsible Selection'},
    'items': [
        T('How the Four Models Support an AI Application', """
<p>An AI application needs data collection, storage, feature preparation, model training or inference, and result delivery. A database supports these stages; choosing one does not itself train a model or guarantee accurate predictions.</p>
""" + table(['AI data role', 'Useful starting model', 'Why / caution'], [
    ['Evolving learner/user profiles', 'Document', 'Nested skills and preferences fit documents; validate types, consent and retention.'],
    ['Cached predictions or recommendation IDs', 'Key-Value', 'Known user/model key with short lifetime; handle stale results and cache misses.'],
    ['High-volume sensor/interaction history', 'Wide-Column', 'Time-bucketed partitions fit planned range reads; training may need a separate export/analytics pipeline.'],
    ['Fraud or recommendation connections', 'Graph', 'Follow account/device/item paths; investigate patterns and evaluate false positives.'],
]) + """
<p><b>Separate workload from buzzword:</b> storing text metadata or arrays of numbers does not automatically provide semantic vector search. Specialized indexing/search and model evaluation must be assessed separately; they are not required by this introductory unit.</p>
<p><b>Data quality matters:</b> missing values, wrong units, duplicated events and train/serve mismatch can harm an AI system regardless of database choice. Protect personal data, apply least privilege, and define deletion/retention policies.</p>
<p>These are illustrative architectures, not claims that a named company currently runs a particular product.</p>
""", diagram='ns1_ai_fit'),
        T('Polyglot Persistence — Use More Than One Store Only When Justified', """
<p><b>Polyglot persistence</b> means using more than one storage technology within an application, assigning each a workload it handles well.</p>
<p><b>Example shop:</b> an RDBMS keeps the authoritative orders/payments; a document store holds products with different attributes; a key-value store caches recommendation IDs. A small shop might still be best served by one relational database. The diagram is an option, not a requirement to deploy three systems.</p>
<ul><li><b>Define ownership:</b> which store is the source of truth for each fact? A cache is not the source of truth for a confirmed payment.</li>
<li><b>Define synchronization:</b> how are copied fields or cached results refreshed? What happens when an update is delayed?</li>
<li><b>Define failure behaviour:</b> may the shop show an old recommendation, and must it stop confirming a payment it cannot safely record?</li>
<li><b>Count operational cost:</b> backups, monitoring, security, credentials, staff expertise and cross-store consistency become harder as stores increase.</li></ul>
<p><b>Selection checklist:</b> identify entities and relationships; write the top reads/writes; estimate size/rate and retention; state consistency/durability needs; choose the simplest suitable model; test actual product behaviour later.</p>
""", diagram='ns1_polyglot'),
    ],
}

_CASE_TEXT = ''.join(
    '<h4>' + c['id'] + ': ' + c['scenario'] + '</h4>'
    + '<p><b>Access:</b> ' + c['access'] + '<br><b>Suggested starting type:</b> ' + c['choice']
    + '. <b>Reason:</b> ' + c['reason'] + '<br><b>Trade-off:</b> ' + c['tradeoff'] + '</p>'
    for c in CASES)
_SOURCE_TEXT = '<ol>' + ''.join('<li><a href="' + url + '">' + name + '</a></li>' for name, url in SOURCES) + '</ol>'

SEC_P1 = {
    'title': {'en': 'Practical 1 — Comparative Study and Solved Selection Cases'},
    'items': [
        T('Practical 1: Aim, Procedure, Comparison Matrix and Journal', """
<p><b>Official aim:</b> study and compare Document, Key-Value, Wide-Column and Graph databases, identifying their unique characteristics, advantages and application areas.</p>
<p><b>Resources:</b> this unit, the official syllabus, product documentation and a notebook/worksheet. Installing all four engines or publishing runtime benchmarks is not required for this comparative practical.</p>
<h4>Procedure</h4>
<ol><li>Choose an application and state its main read/write requests.</li>
<li>Sketch one representative record/model for each of the four types.</li>
<li>Complete the comparison matrix with type, example, shape, access, advantage, trade-off and application area.</li>
<li>Select a type for your application and justify it with two workload-specific reasons and one limitation.</li>
<li>Explain the CAP booking analogy and name an operation that may be deferred or may return stale data.</li>
<li>Record sources and write a conclusion. Label illustrative data as illustrative; record measured results only if you actually run and measure a system.</li></ol>
<h4>Worked comparison</h4>
""" + _MODEL_MATRIX + """
<h4>Suggested journal outline</h4>
@@report@@
<p><b>Completion check:</b> all four types compared; the access pattern is explicit; one model sketch and representative record are included; the choice has two reasons plus a trade-off; CAP is explained under a partition; study observations are not presented as runtime measurements.</p>
<p><b>Conclusion example:</b> “For changing nested product details, a document model is a suitable starting choice because it keeps one product together and supports varying attributes. We must still validate fields and design indexes. A relational ledger remains appropriate for authoritative payments.”</p>
"""),
        T('Eight Worked Selection Cases, Revision Checks and Sources', """
<p>Each recommendation below assumes the stated access pattern and priorities. A well-justified alternative can be valid; the product name alone does not decide suitability.</p>
""" + _CASE_TEXT + """
<h4>Before the practical viva</h4>
<ul><li>Explain all four models without saying that every NoSQL system has no schema or transactions.</li>
<li>Distinguish partitioning from replication, and both from a network partition.</li>
<li>Explain why an isolated office cannot promise both current shared data and completion of every affected request.</li>
<li>Choose a model from the query, not simply because the app uses AI.</li>
<li>State one situation where keeping an RDBMS is the better default.</li></ul>
<h4>Sources and scope</h4>
<p>The GTU syllabus fixes the unit scope and practical-only assessment. Product documentation supports the model descriptions; the Gilbert-Lynch paper is a reference for accurate CAP definitions, <b>not a required theorem proof</b>. Sources checked on 29 October 2026; no database-version claim or performance benchmark is made here.</p>
""" + _SOURCE_TEXT),
    ],
}

NOTES = [SEC_1_1, SEC_1_2, SEC_1_3, SEC_1_4, SEC_P1]
assert sum(len(s['items']) for s in NOTES) == 14
