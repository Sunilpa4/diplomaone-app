"""DI04000031 Unit 2: 20 English-only lessons and real mongosh examples.
The official practical-only course does not have a fabricated theory paper.
"""
from nosql_content import make_T, table

SOURCES = [
    ('GTU DI04000031 syllabus (2025-26)', 'https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf'),
    ('MongoDB Community installation by OS', 'https://www.mongodb.com/docs/manual/installation/'),
    ('Official Linux installation: select Debian / your distribution', 'https://www.mongodb.com/docs/manual/administration/install-community-linux/'),
    ('Install mongosh', 'https://www.mongodb.com/docs/mongodb-shell/install/'),
    ('MongoDB documents and BSON', 'https://www.mongodb.com/docs/manual/core/document/'),
    ('MongoDB CRUD', 'https://www.mongodb.com/docs/manual/crud/'),
    ('Projection rules', 'https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/'),
    ('Embedding and references', 'https://www.mongodb.com/docs/manual/data-modeling/best-practices/'),
    ('Indexes', 'https://www.mongodb.com/docs/manual/indexes/'),
    ('Aggregation pipelines', 'https://www.mongodb.com/docs/manual/core/aggregation-pipeline/'),
    ('Replication concepts', 'https://www.mongodb.com/docs/manual/replication/'),
    ('Sharding concepts', 'https://www.mongodb.com/docs/manual/sharding/'),
]

SN = {
    'document': '''{
  _id: ObjectId("65a1b2c3d4e5f60718293040"),
  name: "Asha",
  skills: ["MongoDB", "Python"],
  address: {city: "Surat"}
}''',
    'versions': '''# Operating-system terminal, not inside mongosh:
mongod --version
mongosh --version''',
    'apt': '''# Debian 13 x86_64 reference only; select your OS guide.
sudo apt-get install -y gnupg curl
curl -fsSL https://pgp.mongodb.com/server-9.asc \\
  | sudo gpg --dearmor \\
      -o /usr/share/keyrings/mongodb-server-9.gpg
# Add the official trixie/mongodb-org/9.0 APT source
# with signed-by=/usr/share/keyrings/mongodb-server-9.gpg.
# The exact line is in the linked official Debian guide.
sudo apt-get update
sudo apt-get install -y \\
  mongodb-org-server=9.0.4 mongodb-mongosh=2.14.0''',
    'local_server': '''# Terminal A: private local learning server, not production.
mkdir -p "$HOME/mongo-lab-data"
mongod --dbpath "$HOME/mongo-lab-data" \\
  --bind_ip 127.0.0.1 --port 27027 --auth
# Keep this terminal running; stop cleanly after the lab.''',
    'first_user': '''// Only on a new private server with no users yet.
// Connect locally to admin; use the localhost exception.
db = db.getSiblingDB("admin");
db.createUser({
  user: "labBootstrapAdmin",
  pwd: passwordPrompt(),
  roles: [{role: "root", db: "admin"}]
});''',
    'login': '''# Terminal B: password is prompted, not embedded in a URI.
mongosh "mongodb://127.0.0.1:27027/di04000031_u2_manual" \\
  --username labBootstrapAdmin \\
  --authenticationDatabase admin --password''',
    'shell': '''// Inside mongosh: interactive helpers
use di04000031_u2_manual
show collections
db.getName()
db.runCommand({ping: 1})
// In a .js file use JavaScript instead of `use`:
db = db.getSiblingDB("di04000031_u2_manual");''',
    'filter': '''{marks: {$gt: 80}}
{marks: {$lt: 70}}
{city: {$in: ["Surat", "Bharuch"]}}
{$and: [{age: {$gt: 18}}, {marks: {$gt: 80}}]}
{$or: [{city: "Surat"}, {marks: {$lt: 60}}]}''',
    'query': '''db.students.find({}, {_id: 0, name: 1, marks: 1})
  .sort({marks: -1, _id: 1})
  .limit(3)
  .toArray();''',
    'update': '''db.students.updateOne(
  {_id: 2},
  {$set: {city: "Surat"}, $inc: {marks: 5}}
);''',
    'aggregation': '''db.orders.aggregate([
  {$match: {status: "paid"}},
  {$group: {
    _id: "$category",
    count: {$sum: 1},
    total: {$sum: "$amount"},
    average: {$avg: "$amount"}
  }},
  {$sort: {_id: 1}}
]);''',
    'journal': '''Aim and practical number\nOS / architecture and installation method\nActual mongod and mongosh versions\nLocal connection, authentication and ping evidence\nScratch database and collection names\nActual input, commands and observed output\nPositive + negative checks\nModel/index decisions and one limitation\nSafe cleanup, conclusion and sources''',
}
T = make_T(SN)

SEC_2_1 = {
    'title': {'en': '2.1 MongoDB Architecture, Documents, Collections and BSON'},
    'items': [
        T('MongoDB in the Application Stack and This Unit’s Scope', """
<p><b>MongoDB</b> is a document database. The <b>mongod</b> server accepts commands, executes queries/updates, manages indexes and stores BSON data. <b>mongosh</b> is a JavaScript-based client shell; an application normally uses an appropriate driver. Compass is an optional graphical client, not a replacement for the database server.</p>
<p>Basic path: <b>client/driver or mongosh → connection → mongod → collections/indexes/storage → result</b>. A localhost address in these examples is a database connection from the same machine, not a browser API or a publicly hosted service.</p>
<p><b>Official scope:</b> 18 hours / 30% content weightage; documents, collections, BSON, architecture, installation, mongosh, CRUD, listed filters, sort/limit/projection, embedding/references, basic indexes and $match/$group/$sum/$avg. Replication and sharding are <b>conceptual only</b>.</p>
<p><b>CO2:</b> apply MongoDB features for effective data modeling and management. Practicals 2 and 3 cover installation/connectivity and CRUD with filters, sorting and projection.</p>
<p><b>Reference execution:</b> all 14 displayed programs were run using a real authenticated MongoDB 9.0.4 standalone server and mongosh 2.14.0 on Debian 13 x86_64. No database emulator, replica-set configuration, sharded-cluster configuration or external application deployment is claimed.</p>
""", diagram='ns2_arch'),
        T('Database → Collection → Document', """
<p>A deployment contains <b>databases</b>; a database groups <b>collections</b>; a collection stores <b>documents</b>. An ordinary collection is loosely comparable to a relational table, but documents can contain nested structures and need not all have identical fields.</p>
<p>A document is a set of named field/value pairs. Values can include strings, numbers, arrays and embedded documents. The following is <b>mongosh JavaScript/BSON-constructor syntax</b>, not strict JSON:</p>
@@document@@
<ul><li><b>Database:</b> for example, a disposable di04000031_u2_manual learning database.</li>
<li><b>Collection:</b> students, products or orders.</li>
<li><b>Document:</b> one bounded student/product/order record.</li>
<li><b>Field:</b> name, marks or address; <b>dot notation</b> such as "address.city" targets a nested field.</li></ul>
<p><b>Creation:</b> selecting a database does not immediately persist an empty database. Explicit createCollection or a first write creates storage. insertOne/insertMany can create an ordinary collection implicitly.</p>
<p><b>Flexible schema still needs design:</b> agree on required fields, types, units and bounded arrays; validation can be added. Avoid duplicate field names and surprising type changes. A BSON document has a 16 MiB size limit; it is not an unlimited container for every event in a user’s lifetime.</p>
""", diagram='ns2_hierarchy'),
        T('BSON Types, _id and ObjectId', """
<p><b>BSON</b> is a typed binary representation used by MongoDB. It supports types beyond JSON’s basic text representation. The course explicitly includes ObjectId, String, Array and Embedded Document; Boolean, numeric and Date examples provide useful context.</p>
""" + table(['Value / constructor', 'Meaning / common mistake'], [
    ['ObjectId("65a1b2c3d4e5f60718293040")', 'An ObjectId value, not an ordinary string with the same text.'],
    ['"Asha"', 'String; quote a text ID rather than assuming it equals a numeric or ObjectId ID.'],
    ['["MongoDB", "Python"]', 'Array; an array can contain multiple values.'],
    ['{city: "Surat"}', 'Embedded document, not a foreign-key relationship by itself.'],
    ['NumberInt(19), 82.5, true', 'Explicit Int32, a fractional number, and a Boolean; numeric precision needs care.'],
    ['ISODate("2026-01-15T00:00:00Z")', 'A BSON Date via mongosh, not merely an arbitrary date string.'],
]) + """
<p><b>_id:</b> the identifier field is unique and immutable within an ordinary collection. It is not restricted to ObjectId; the student demos use small integer IDs deliberately. When _id is omitted, a normal insert receives a generated ObjectId.</p>
<p><b>Type-sensitive filters:</b> ObjectId("65a1…") and "65a1…" are different values. The type example verifies stored types with $type, and shows zero string-ID matches but one ObjectId match. It records a fixed UTC date for reproducible output.</p>
<p>Use suitable exact numeric representations for real financial quantities, such as integer minor units or a deliberately designed Decimal128 policy; do not assume floating-point arithmetic is exact currency accounting.</p>
""", diagram='ns2_bson', programs=['ns2p02']),
    ],
}

SEC_2_2 = {
    'title': {'en': '2.2 Installation, mongosh and Safe Lab Setup — Practical 2'},
    'items': [
        T('Install the Server and mongosh; Verify a Real Connection', """
<ol><li><b>Check platform:</b> use an OS/architecture supported by the selected MongoDB release. The tested reference uses Debian 13 x86_64 and the official signed MongoDB 9.0 APT repository. Do not copy this repository line onto an unrelated Ubuntu/Debian release.</li>
<li><b>Install:</b> install MongoDB Community Server and mongosh separately if the chosen installer does not bundle both. Windows uses the official server installer/service plus mongosh as needed; Linux uses the matching vendor repository; follow the vendor guide for macOS. Compass is optional.</li>
<li><b>Record both versions:</b> a working mongosh executable does not prove mongod is installed, running or reachable.</li></ol>
@@versions@@
<p><b>Tested versions:</b> server 9.0.4 and shell 2.14.0. These identify the actual reference run, not a promise that these will remain the newest secure production patches.</p>
@@apt@@
<p>Use the linked official guide for the complete repository line and signing-key procedure. On a standard systemd installation, the service is managed with systemctl. The reference sandbox has no normal systemd service, so a process-managed standalone instance was used instead.</p>
@@local_server@@
<p><b>Authentication:</b> for a new private instance with no users, the localhost exception allows initial administrator creation. Connect locally to admin and use an interactive hidden password prompt. This is a <b>bootstrap administrator</b>, not an application identity:</p>
@@first_user@@
<p>Do not repeat first-user creation on an existing deployment. Follow your lab administrator’s account policy; production applications require least privilege, TLS/network controls and tested backups. The reference harness keeps its credentials outside all lesson files and downloads.</p>
@@login@@
<p><b>Verify:</b> select a fresh scratch database, ping, create a collection, insert a message and read it back. A ping alone does not prove authorization to read/write. Program 1 records the actual successful storage round-trip and collection cleanup.</p>
<p><b>Troubleshoot:</b> command not found → installation/PATH; connection refused → server/port; authentication failure → user/authentication database/password; unauthorized → roles; data-directory error → path/permissions. Do not solve connectivity by exposing an unauthenticated public port.</p>
""", diagram='ns2_setup', programs=['ns2p01']),
        T('mongosh Context, Interactive Helpers, Cursors and Script Execution', """
<p><b>Two contexts:</b> commands such as mongod --version belong to the OS terminal. Commands such as db.students.find belong inside mongosh. Interactive helpers like <b>use</b> and <b>show collections</b> are not ordinary JavaScript statements for a .js script.</p>
@@shell@@
<p><b>Connection versus current database:</b> getSiblingDB selects another database on the same connection; it does not create a new server. Authentication may use admin even when data operations use a different scratch database.</p>
<p><b>find:</b> returns a cursor. Interactive display may show only a batch. For a small lab, toArray materializes the results for deterministic JSON printing. Limit real workloads rather than loading an unbounded result into client memory. <b>findOne:</b> returns one document or null.</p>
<p><b>Scripts:</b> run a .js file using mongosh --file after selecting an authorized disposable database. The practical download includes an isolated runner that supplies a fresh database to each exact displayed script. Seeds are inside each program; examples are independent, not a sequence to paste into one already-populated collection.</p>
<p>Every displayed script checks the di04000031_u2_ prefix. That guard reduces accidental targeting mistakes; it is not authorization, a substitute for backups, or permission to reset real work merely because its name has that prefix.</p>
"""),
    ],
}

SEC_2_3 = {
    'title': {'en': '2.3 CRUD, Filters, Sorting, Projections and Data-Type Pitfalls'},
    'items': [
        T('Create Documents: insertOne, insertMany and Duplicate Keys', """
<p><b>CRUD Create</b> means inserting documents; it is not limited to creating a database or collection. insertOne inserts one document, while insertMany takes an array of documents. Inspect acknowledged/inserted identifiers rather than assuming the write succeeded.</p>
<p>An omitted _id is normally generated. An explicitly supplied _id can be an appropriate supported scalar value. The default unique _id index prevents two documents from sharing the same _id in this ordinary lab collection.</p>
<p><b>Observed example:</b> insert one student, then two more; a duplicate _id:1 attempt is rejected with <b>11000</b> and the collection still has three records. Only the expected duplicate error is caught; another error is rethrown.</p>
<p>insertMany is not automatically an all-or-nothing multi-document transaction. If a batch fails, examine its error/result and the actual stored state rather than blindly replaying the entire batch. Plan idempotency and uniqueness for repeated imports.</p>
""", diagram='ns2_crud', programs=['ns2p03']),
        T('Read Documents with Comparison and Logical Filters', """
<p>A <b>filter</b> is a document describing which records match. An empty filter {} matches all documents, which is useful for a tiny read fixture but dangerous for bulk writes.</p>
@@filter@@
""" + table(['Operator', 'Meaning', 'Observed student IDs'], [
    ['$gt:80 on marks', 'Strictly greater than 80', '1, 3, 5'],
    ['$lt:70 on marks', 'Strictly less than 70', '4, 6'],
    ['$in on city', 'Either Surat or Bharuch', '1, 2, 3, 5'],
    ['$and: age >18 and marks >80', 'All listed clauses', '1, 5'],
    ['$or: Surat or marks <60', 'At least one listed clause', '1, 3, 5, 6'],
]) + """
<p>Different ordinary field conditions in one filter are implicitly ANDed. For repeated conditions on one field, use one operator object or explicit $and rather than duplicate JavaScript keys that overwrite each other.</p>
<p><b>Boundary:</b> $gt does not include equality and $lt does not include equality. $gte/$lte include the boundary when required; the catalog later uses $gte:1 for a guarded stock decrement.</p>
""", diagram='ns2_filters', programs=['ns2p04']),
        T('Sort, Limit and Projection Are Different Controls', """
<ul><li><b>Filter:</b> which documents?</li><li><b>sort:</b> in what order? 1 is ascending and -1 descending.</li><li><b>limit:</b> how many returned documents?</li><li><b>Projection:</b> which fields? 1 includes and 0 excludes.</li></ul>
@@query@@
<p><b>Observed top three:</b> Neha 92, Asha 82, Meera 82. The _id tie-breaker makes the equal-mark order deterministic. Without a complete sort, “first three” is not a dependable ranking.</p>
<p><b>Projection rule:</b> do not mix ordinary inclusion and exclusion fields. The special _id exclusion can accompany an inclusion projection, such as {_id:0,name:1,marks:1}. Exclusion-only projections retain unspecified fields. Projection changes the returned shape, not stored data or field-level authorization.</p>
<p>The diagram shows logical result shaping, not a fixed physical execution order of the database optimizer. The full program also demonstrates a cursor and a missing findOne result.</p>
""", diagram='ns2_query', programs=['ns2p05']),
        T('Array Membership, Dot Notation and Whole-Document Equality', """
<p>{skills:"MongoDB"} can match an element inside an array. {skills:{$in:["Python","Java"]}} matches a document with at least one listed value. Two separate membership conditions can require both values to be present.</p>
<p><b>Nested field:</b> {"address.pin":"395001"} targets the pin inside the address object. Quote the dotted path. In the seed, this returns student 1.</p>
<p><b>Whole-object equality:</b> {address:{pin:"395001"}} is not the same query. The stored address also has state, so the shorter object is not an exact match and the observed result is empty. Do not use whole-object equality when you intend to filter one nested field.</p>
<p>For more complex arrays of embedded documents, multiple conditions may accidentally match different elements; $elemMatch is a later refinement when conditions must apply to the same element. This unit’s executable example keeps scalar array membership and one nested object simple.</p>
""", programs=['ns2p06']),
        T('Update One/Many with $set and $inc; Read the Result Counts', """
@@update@@
<p>$set assigns named fields without removing unrelated fields. $inc adds to a numeric field. updateOne changes at most one matched document; updateMany applies the operation to all matches.</p>
""" + table(['Observed case', 'matchedCount', 'modifiedCount', 'Meaning'], [
    ['Ravi: change city and add 5 marks', 1, 1, 'Found and changed'],
    ['Add 2 marks to two inactive students', 2, 2, 'Both documents changed'],
    ['Set Ravi to the already stored 75', 1, 0, 'Matched no-op'],
    ['Update nonexistent _id:999', 0, 0, 'No match; no insert by default'],
]) + """
<p><b>Atomicity:</b> a write to one document is atomic. updateMany is not automatically one transaction across all matched documents. Acknowledge that distinction before adapting a classroom update to a payment/inventory workflow.</p>
<p>Check the intended database, collection and filter. Do not pass an arbitrary unvalidated client object directly as a filter or update definition.</p>
""", diagram='ns2_update', programs=['ns2p07']),
        T('Upsert Is Explicit; Replacement Removes Omitted Fields', """
<p><b>upsert:true:</b> insert when no document matches; otherwise update a match. The reference uses _id:7 as a stable unique key: the first operation reports one upserted record, and the second matches it rather than creating another profile.</p>
<p><b>replaceOne:</b> supplies a replacement document, not a partial patch. Replacing Jai’s profile with name and marks removes the old city field. The existing _id is retained when omitted from the replacement. An attempt to change _id is invalid.</p>
<p><b>Choose deliberately:</b> use $set/$inc for field-level modifications, replaceOne for an intentional full replacement, and upsert only when creating a missing record is actually desired. Unique indexes still matter when concurrent operations rely on an alternate business key.</p>
<p>The program prints the retained ID and sorted field names to prove what is stored after replacement.</p>
""", programs=['ns2p08']),
        T('Delete Documents Safely; Distinguish deleteMany from drop', """
<p>deleteOne removes at most one matching document and deleteMany removes all matches. Inspect deletedCount: zero can simply mean the target did not exist.</p>
<p><b>Observed fixture:</b> two students are inactive. Delete student 6, then the remaining inactive student 4; a missing-ID delete reports zero. IDs 1, 2, 3 and 5 remain.</p>
<ul><li><b>deleteMany({}):</b> deletes every document in the current collection.</li><li><b>collection.drop():</b> removes that collection and its indexes.</li><li><b>database.dropDatabase():</b> destroys the selected database; the automated harness uses it only for its own freshly captured scratch database.</li></ul>
<p>Preview the filter, verify the context and have an appropriate recovery plan. A preview count is not a concurrency lock. Never practice destructive commands against real records or use the scratch-name prefix as a substitute for authorization.</p>
""", programs=['ns2p09']),
        T('Null versus Missing, Type Mismatch and Rejected Query Shapes', """
<p><b>Observed records:</b> _id:1 has tag:null; _id:2 has no tag field; _id:3 has a string tag.</p>
""" + table(['Filter', 'Observed IDs', 'Meaning'], [
    ['{tag:null}', '1, 2', 'Null equality also matches a missing field'],
    ['{tag:{$type:10}}', '1', 'Explicit BSON null'],
    ['{tag:{$exists:false}}', '2', 'Field absent'],
    ['{_id:"1"}', 'none', 'String does not match numeric ID'],
]) + """
<p>The full negative-test example also records server error <b>31254</b> for mixed ordinary projection modes, and a mongosh <b>MongoInvalidArgumentError</b> when updateOne is given a non-operator document. Error identifiers may differ for a different invalid form/version; the lesson explains the operation rather than relying on error text.</p>
<p><b>Selector-shaped input:</b> a user-supplied object such as {$ne:null} is not a scalar username or ID. Validate expected types/ranges, authorize the operation and construct the allowed filter yourself. The small type check is not a complete secure login/API implementation.</p>
""", programs=['ns2p14']),
    ],
}

SEC_2_4 = {
    'title': {'en': '2.4 Data Modeling, Basic Indexes and Aggregation'},
    'items': [
        T('Embed Bounded Related Data or Reference Shared Entities', """
<p><b>Embedding:</b> keep a bounded address inside a learner when the address is read with that learner. One document can be retrieved and updated atomically. The model is natural for has-a/contains relationships and data read together.</p>
<p><b>Referencing:</b> put shared course details in a courses collection and store courseId in each learner. This avoids duplicating a frequently shared course record but requires explicit related-data retrieval and missing-reference handling.</p>
""" + table(['Prefer embedding when…', 'Prefer references when…'], [
    ['The related data is bounded and usually accessed together', 'The relationship grows without a sensible bound'],
    ['One-document updates suit the consistency boundary', 'Many parents share a separately managed entity'],
    ['Duplication is limited and acceptable', 'Duplication/update coordination would become costly'],
]) + """
<p><b>Observed example:</b> the learner’s embedded city is Surat; an explicit second query resolves C1 to MongoDB Basics. A different learner with courseId:UNKNOWN is still inserted; the lookup returns null. There is no automatically enforced relational foreign key.</p>
<p>Do not embed an unlimited comment/history stream. Do not assume references are automatically joined or that two separate reads/writes form one transaction. $lookup and multi-document transaction configuration are not required implementations here.</p>
""", diagram='ns2_model', programs=['ns2p10']),
        T('Basic Indexing, Unique Constraints and an Honest Explain Comparison', """
<p>An <b>index</b> stores ordered field information that can reduce the work needed for a suitable query. An ordinary collection has the unique _id index. createIndex can add a single-field or compound index; getIndexes lists the definitions.</p>
<p><b>Example index:</b> {city:1,marks:-1} with name city_marks. The query asks for Surat students with marks greater than 80. The reference deliberately forces a natural scan and then the named index with <b>hint</b> so the tiny fixture illustrates a controlled comparison:</p>
""" + table(['Plan deliberately requested', 'Returned', 'Documents examined', 'Index keys examined'], [
    ['Natural collection scan', 3, 6, 'Not used for this comparison'],
    ['city_marks index', 3, 3, 3],
]) + """
<p><b>Interpretation:</b> same result, fewer examined documents in this observed run. This is not a guarantee about wall-clock speed or what the optimizer would choose without hints. Execution plans/counters vary with data, query and server version; do not claim that every query always uses every index.</p>
<p><b>Unique email:</b> a separate {email:1} unique index rejects an identical email with 11000. Plan normalization/collation and missing/null policies if adapting this to users; uniqueness is not validation of a real email address.</p>
<p><b>Cost:</b> indexes consume storage and must be maintained during writes. Add indexes for real access patterns; too many indexes can hurt write-heavy workloads.</p>
""", diagram='ns2_index', programs=['ns2p11']),
        T('Aggregation Pipeline: $match → $group → $sum / $avg', """
<p>An aggregation pipeline passes documents through ordered stages. A stage can filter, reshape or group its input; it need not output one document for each input document.</p>
@@aggregation@@
<ul><li><b>$match:</b> keep only paid orders, reducing six inputs to five.</li><li><b>$group:</b> group those documents by the category field. "<b>$category</b>" is a field path; "category" without $ would be a literal string.</li><li><b>$sum:1:</b> count documents in each group.</li><li><b>$sum:"$amount":</b> add the numeric amounts.</li><li><b>$avg:"$amount":</b> compute a mean of the numeric amounts.</li><li><b>$sort:</b> make the two output rows deterministic; grouping alone does not promise output order.</li></ul>
""" + table(['Category', 'Count', 'Total', 'Average'], [['book', 3, 600, 200], ['tool', 2, 1000, 500]]) + """
<p>This pipeline is read-only and leaves all six source orders unchanged. Pipelines that explicitly use write stages are a different case. The integer demo amounts avoid an implied claim of exact general floating-point money arithmetic.</p>
""", diagram='ns2_pipeline', programs=['ns2p12']),
        T('Practical 3 Mini-Catalog: CRUD with a Guarded Stock Decrement', """
<p>The mini-catalog stores a book with a pages attribute and a sensor with a sample-rate attribute. Both share identifying fields, a category, an integer pricePaise value and stock. The examples demonstrate a plausible document-model choice without building a hosted web service.</p>
<p><b>Read:</b> filter books, project name/price, sort and limit. <b>Update:</b> filter by the product ID <b>and stock ≥1</b>, then $inc stock by -1 in the same operation.</p>
<p><b>Observed:</b> starting stock is 2; the first two attempted sales each match one record, the third matches zero, and final stock is 0. A missing-ID delete reports zero.</p>
<p><b>Guarantee boundary:</b> the conditional update is atomic for that one document. These are sequential reference attempts, not a concurrent stress test. There is no atomic payment-plus-stock workflow or multi-document transaction in this example.</p>
<p><b>Student extension:</b> add a new catalog type, validate its required fields, query a nested attribute and justify an index. Record actual commands and negative cases; do not claim AI training or remote deployment from a local CRUD demonstration.</p>
""", programs=['ns2p13']),
    ],
}

SEC_2_5 = {
    'title': {'en': '2.5 Replication and Sharding — Conceptual Overview Only'},
    'items': [
        T('Replication: Copies of the Same Dataset', """
<p>A <b>replica set</b> is a group of mongod instances maintaining copies of the same dataset. In the basic architecture, a primary receives writes and secondaries replicate its changes. An eligible replacement primary can be elected when the current primary is unavailable.</p>
<ul><li><b>Purpose:</b> redundancy and potential failover/data locality, not splitting the collection into distinct subsets.</li><li><b>Lag:</b> secondaries apply changes asynchronously and can be behind. Read/write settings affect what a successful operation guarantees.</li><li><b>Failure:</b> an election or a partition can interrupt service. Do not promise zero downtime, immediate current secondary reads or a fixed CP/AP brand label for every operation.</li><li><b>Backup:</b> replicated deletion/corruption can propagate; independent backups and tested restores still matter.</li></ul>
<p><b>Scope/evidence:</b> the syllabus explicitly requires concepts only. The reference programs use a standalone server: no replica set was configured, no election was triggered and no failover test is claimed.</p>
""", diagram='ns2_replica'),
        T('Sharding: Different Subsets across Shards', """
<p><b>Sharding</b> distributes a collection’s data across multiple shards to support horizontal growth. A <b>shard key</b> influences data placement and query routing. In the standard self-managed architecture, mongos routes requests using metadata maintained by config servers; each shard is itself deployed as a replica set.</p>
<ul><li><b>Replication:</b> copies of the same data. <b>Sharding:</b> different subsets distributed across shards. A sharded system can use both.</li><li><b>Key choice matters:</b> an uneven or hotspot-producing key can concentrate work instead of balancing it.</li><li><b>Query routing matters:</b> a suitable key-directed query may target relevant shards; an unrelated query may need broader work.</li><li><b>Cost:</b> more routing, monitoring, security and maintenance complexity. Horizontal scaling is not a promise of linear speedup.</li></ul>
<p><b>Scope/evidence:</b> explain the diagram and distinguish copies from subsets. No mongos/config-server/shard setup, shard-key experiment or sharding benchmark is required or claimed. A standalone CRUD result cannot establish distributed behaviour.</p>
""", diagram='ns2_shard'),
    ],
}

_SOURCE_HTML = '<ol>' + ''.join('<li><a href="' + url + '">' + title + '</a></li>' for title, url in SOURCES) + '</ol>'
SEC_LAB = {
    'title': {'en': 'Practicals 2–3 — Evidence, Journal and Source Checklist'},
    'items': [
        T('Practical Journal, Acceptance Checks and References', """
<p><b>Practical 2:</b> install Community Server and mongosh; configure the local environment; record both versions and a successful connection plus authorized write/read evidence. The tested private environment used authentication; no real personal data or public database endpoint was used.</p>
<p><b>Practical 3:</b> create/use collections and carry out insert/find/update/delete with the listed comparison/logical filters, sorting and projection. Use the six-student fixture and the independent mini-catalog to explain both expected results and negative cases.</p>
@@journal@@
<h4>Acceptance checklist</h4>
<ul><li>Actual server and shell versions and storage round-trip recorded.</li><li>Correct BSON/ID types, deterministic sort and intended projection.</li><li>All five syllabus operators demonstrated; array/nested filters understood.</li><li>Matched/modified/deleted counts and duplicate/missing/no-op outcomes checked.</li><li>Embedding/reference choice justified; missing reference handled.</li><li>Index comparison explained as forced counters, not a timer claim.</li><li>Aggregation totals/averages verified and source rows preserved.</li><li>Scratch databases cleaned; credentials excluded from notes/downloads.</li><li>Replication/sharding labeled conceptual, not configured.</li></ul>
<p><b>Assessment:</b> this is a practical-only subject (PA 20 + ESE 30 = 50; 0 theory ESE/PA). The answered practice tasks below prepare the lab/journal/viva and do not invent official theory-paper question marks.</p>
<h4>References</h4>
<p>Official syllabus and MongoDB documentation, checked 29 October 2026. Installation instructions are platform/version-specific; the recorded versions identify the reference run.</p>
""" + _SOURCE_HTML),
    ],
}

NOTES = [SEC_2_1, SEC_2_2, SEC_2_3, SEC_2_4, SEC_2_5, SEC_LAB]
assert sum(len(s['items']) for s in NOTES) == 20
