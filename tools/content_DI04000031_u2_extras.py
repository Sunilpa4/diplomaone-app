"""MongoDB Unit 2: 16 reference cards, 56 viva answers, 18 answered tasks.
Practical-only course: no invented theory-paper marks.
"""
from nosql_content import SX, V, Q, tr


def G(title, items): return {'title': tr(title), 'items': items}

SYNTAX = [
    G('Architecture, Setup and BSON', [
        SX('Server versus shell', 'mongod = database server\nmongosh = client shell\ndriver = application client library\nCompass = optional graphical client',
           'Record server and shell versions separately. A running client does not prove a reachable, authorized database.'),
        SX('Terminal versus mongosh', 'OS terminal: mongod --version\nOS terminal: mongosh --version\nmongosh: db.runCommand({ping: 1})\nscript: db = db.getSiblingDB("scratch_name")',
           'Interactive use/show helpers are not ordinary JavaScript for a .js file. Select a di04000031_u2_ scratch name for the supplied examples.'),
        SX('BSON and identifier type', 'ObjectId("65a1b2c3d4e5f60718293040")\nNumberInt(19)\nISODate("2026-01-15T00:00:00Z")\n["MongoDB", "Python"]\n{city: "Surat"}',
           'mongosh constructors are not strict JSON. A string with the same hexadecimal text is not an ObjectId value. _id need not always be an ObjectId.'),
        SX('Database and collection creation', 'use di04000031_u2_manual\ndb.createCollection("students")\n// Or first insert creates an ordinary collection.\ndb.students.insertOne({_id: 1, name: "Asha"})',
           'The first line is an interactive helper. Selecting a database alone does not persist an empty database. Run each independent demo in a fresh authorized scratch database.'),
    ]),
    G('Insert and Read', [
        SX('Insert results', 'insertOne(document)\ninsertMany([document1, document2])\ncheck: acknowledged + inserted IDs\nduplicate unique key -> error 11000',
           'The program inserts one then two students; the duplicate is rejected and three remain. A batch is not automatically a multi-document transaction.'),
        SX('Comparison and logical filters', '{marks: {$gt: 80}}\n{marks: {$lt: 70}}\n{city: {$in: ["Surat", "Bharuch"]}}\n{$and: [condition1, condition2]}\n{$or: [condition1, condition2]}',
           'Reference filter shapes: supply concrete condition documents. $gt/$lt exclude equality; ordinary different-field conditions are implicitly ANDed.'),
        SX('Sort, limit and projection', 'db.students.find({}, {_id: 0, name: 1, marks: 1})\n  .sort({marks: -1, _id: 1})\n  .limit(3).toArray()',
           'Descending marks plus an ascending unique tie-breaker gives stable ranking. Projection shapes the returned fields; it is not a write or a permission check.'),
        SX('Nested and array queries', '{"address.pin": "395001"}\n{skills: "MongoDB"}\n{skills: {$in: ["Python", "Java"]}}',
           'A scalar array condition can match an array element. Dot notation targets one embedded field; whole-object equality has different semantics.'),
    ]),
    G('Updates, Deletes and Pitfalls', [
        SX('Partial update and counts', 'updateOne(filter, {$set: {city: "Surat"}})\nupdateMany(filter, {$inc: {marks: 2}})\nmatched 1 / modified 0 = possible no-op\nmatched 0 / modified 0 = no match',
           'Reference signatures require a real filter document. One-document atomicity does not make every multi-document operation one transaction.'),
        SX('Upsert versus replacement', 'updateOne(filter, {$set: fields}, {upsert: true})\nreplaceOne(filter, replacementDocument)\nreplacement removes omitted non-_id fields',
           'These are reference signatures, not standalone scripts. Upsert explicitly permits insertion; a stable unique key and correct filter still matter.'),
        SX('Deletion scope', 'deleteOne(filter) -> at most one\ndeleteMany(filter) -> all matches\ndeleteMany({}) -> all collection documents\ncollection.drop() -> collection + indexes',
           'The arrow lines summarize behaviour, not executable JavaScript. Check deletedCount and the active scratch context before destructive work.'),
        SX('Null, missing and projection', '{tag: null} -> explicit null OR missing\n{tag: {$type: 10}} -> explicit BSON null\n{tag: {$exists: false}} -> field absent\n{_id: 0, name: 1} -> allowed inclusion form',
           'Reference summaries, not standalone programs. Do not mix ordinary included/excluded fields. The null fixture returns IDs [1,2], [1], and [2].'),
    ]),
    G('Modeling, Indexes, Aggregation and Distribution', [
        SX('Embed or reference', 'embed: bounded data read together\nreference: shared / independently managed data\nreference lookup can return null\nno automatic relational foreign key',
           'Avoid unbounded embedded histories. Define missing-reference handling and the consistency boundary explicitly.'),
        SX('Basic index and explain', 'db.students.createIndex(\n  {city: 1, marks: -1}, {name: "city_marks"}\n)\nfind(filter).hint("city_marks")\n  .explain("executionStats")',
           'Reference query shape: use db.students.find(filter) with a real filter. Hints force the teaching comparison; examined counters are not a guaranteed timing speedup.'),
        SX('Aggregation group', '{$match: {status: "paid"}}\n{$group: {\n  _id: "$category", count: {$sum: 1},\n  total: {$sum: "$amount"}, avg: {$avg: "$amount"}\n}}',
           'Individual stage shapes belong in an aggregate([...]) pipeline. $sum:1 counts documents; "$amount" is a field path. Sort for deterministic group output.'),
        SX('Replication versus sharding', 'replication: copies of the same dataset\nsharding: different subsets across shards\nmongos: query routing for a sharded cluster\nthis unit: concepts only, no cluster setup',
           'The real examples ran on a standalone server. Replication is not an independent backup; key choice and settings affect distributed behaviour.'),
    ]),
]

_FOUNDATIONS = [
    V('What is MongoDB’s main data model?', 'Documents grouped in collections, stored as BSON within databases.'),
    V('mongod versus mongosh?', 'mongod is the database server; mongosh is a client shell that connects to it. Installing one does not prove the other is working.'),
    V('What does a driver do?', 'It lets application code communicate with MongoDB using a supported language API; it is a client, not the storage server.'),
    V('Is Compass required for these programs?', 'No. It is an optional graphical client. The reference uses mongosh and a real mongod server.'),
    V('What versions and platform were actually tested?', 'MongoDB Community Server 9.0.4 and mongosh 2.14.0 on Debian 13 x86_64, with a private authenticated standalone instance.'),
    V('Does mongosh --version prove database connectivity?', 'No. It proves the shell executable is available. Record server connectivity and an authorized write/read round-trip as well.'),
    V('Does a successful ping prove read/write authorization?', 'No. A ping is a liveness/connectivity check, not proof of permission to access application data.'),
    V('What is the database/collection/document hierarchy?', 'A database groups collections; an ordinary collection stores documents; each document contains named field/value pairs.'),
    V('Does use databaseName immediately persist an empty database?', 'No. It selects a client context; createCollection or a first write materializes storage.'),
    V('Why is BSON more than JSON text?', 'It is a typed binary representation with additional types such as ObjectId and Date, not just a JSON character string.'),
    V('Must every _id be an ObjectId?', 'No. The lab also uses integer and string IDs. In an ordinary collection _id must be unique and is immutable; omitting it normally generates an ObjectId.'),
    V('Why can an ObjectId lookup fail when given matching hex text?', 'A plain string containing the hex text is not an ObjectId value. Construct the correct type for the stored identifier.'),
]
_READS = [
    V('What does insertOne return that should be checked?', 'Acknowledgment and the inserted identifier; do not assume a write succeeded merely because a command was typed.'),
    V('What does duplicate-key error 11000 mean here?', 'A unique index, such as _id or the explicit email index, rejected a duplicate value. Catch that expected case and do not swallow unrelated failures.'),
    V('Is insertMany an automatic all-or-nothing transaction?', 'No. A batch error can leave some documents inserted. Examine the actual result and stored state before retrying.'),
    V('find versus findOne?', 'find returns a cursor over matching documents; findOne returns one document or null. A cursor is not automatically a full array.'),
    V('Why use toArray in these small demos?', 'It materializes a small bounded result so JSON output is reproducible. Do not materialize unbounded production results into client memory.'),
    V('What do $gt and $lt mean?', 'Strictly greater than and strictly less than; they exclude equality. Use an inclusive comparison when the boundary must match.'),
    V('What does $in test?', 'Whether a field value, or an element of an array field, matches at least one value in the supplied list.'),
    V('$and versus $or?', '$and requires all listed conditions; $or requires at least one. Ordinary conditions on different fields are implicitly ANDed.'),
    V('What IDs have marks greater than 80 in the fixture?', '1, 3 and 5: Asha 82, Neha 92 and Meera 82.'),
    V('Why sort by marks:-1 and _id:1?', 'Descending marks gives rank, and the unique ascending ID breaks the 82-mark tie deterministically.'),
    V('What does a projection control?', 'Which fields are returned. It does not modify stored records or implement field-level authorization.'),
    V('Can inclusion and exclusion be mixed in a basic projection?', 'Not for ordinary fields. The special _id exclusion may accompany inclusion, as in {_id:0,name:1}.'),
    V('How is a nested pin queried?', 'Use quoted dot notation, for example {"address.pin":"395001"}, rather than an unintended whole-address equality match.'),
    V('Why is address:{pin:"395001"} not equivalent in this fixture?', 'The stored object also includes state; the shorter object is not an exact whole-object match, while dot notation targets just pin.'),
]
_WRITES = [
    V('What does $set do?', 'Assigns specified field values without replacing the entire document; unrelated fields remain.'),
    V('What does $inc do?', 'Increments a numeric field by the supplied amount; -1 can decrement stock in a guarded update.'),
    V('matchedCount versus modifiedCount?', 'Matched counts documents satisfying the filter; modified counts documents whose stored values actually changed. A matched no-op can be 1/0.'),
    V('What happens when updateOne matches nothing by default?', 'Nothing is updated and no document is inserted. The result reports zero matches/changes unless an explicit upsert is requested.'),
    V('What does upsert:true permit?', 'Insert a document if none matches; otherwise update a match. Use a deliberate filter and stable unique business/ID key.'),
    V('Why did replaceOne remove Jai’s city?', 'The replacement omitted city, so it was removed. The existing _id was retained because it was omitted rather than changed.'),
    V('Is updateMany automatically atomic across every document?', 'No. Each single-document modification is atomic, but the entire multi-document operation is not automatically one transaction.'),
    V('What does deletedCount:0 mean?', 'No matching document was deleted; the target may simply have been absent.'),
    V('deleteMany({}) versus collection.drop()?', 'The former removes all documents in the selected collection; the latter removes the collection and its indexes.'),
    V('What does {tag:null} match?', 'Documents with explicit null and documents where the field is missing. Use $type:10 for BSON null or $exists:false for absence.'),
    V('Why reject an externally supplied selector object?', 'An object such as {$ne:null} is not the scalar value expected by a field. Validate types/ranges, authorize the action and build allowed query shapes yourself.'),
    V('Does the stock demo include payment and a concurrency stress test?', 'No. It demonstrates sequential guarded single-document updates: two successes, a zero-match third attempt and final stock zero. Payment transactions and concurrent load testing are separate.'),
]
_MODEL_AGG = [
    V('When is embedding a good starting choice?', 'Bounded related data, such as an address, is commonly read with its parent and fits the intended one-document consistency boundary.'),
    V('When are references useful?', 'Shared or independently managed entities, high-cardinality relationships and data that should not grow without bounds inside one parent document.'),
    V('Does storing courseId enforce a relational foreign key?', 'No. The reference fixture accepts UNKNOWN and the explicit course lookup returns null. The application must handle missing related data.'),
    V('What does an index help with?', 'A suitable index can reduce query work and may support ordering; it costs storage and maintenance during writes.'),
    V('What is a compound index?', 'An index on multiple fields, such as {city:1,marks:-1}. Field order and actual access patterns matter.'),
    V('Why were hints used for the index demonstration?', 'To force a natural scan and a named index on a tiny six-document fixture, making the examined-document comparison controlled rather than claiming the optimizer always chooses one plan.'),
    V('What were the observed examined counters?', 'Both plans returned three documents; the forced scan examined six documents, while the forced city_marks index examined three documents and three index keys.'),
    V('Does that prove a guaranteed timing speedup?', 'No. Data, query, cache state, plan and version matter. The demo reports work counters, not a promised wall-clock multiplier.'),
    V('What is an aggregation pipeline?', 'A sequence of stages that process documents; output from one stage becomes input to the next, and counts/shapes may change.'),
    V('$sum:1 versus $sum:"$amount"?', 'The first adds one per group input, counting documents; the second adds each input document’s numeric amount field.'),
    V('What are the two paid-order group results?', 'book: count 3, total 600, average 200; tool: count 2, total 1000, average 500. One cancelled order is excluded.'),
    V('Does the reference aggregation change its source orders?', 'No. The read-only pipeline leaves six source documents unchanged; it has no explicit write stage.'),
]
_DISTRIBUTION = [
    V('Replication versus sharding?', 'Replication maintains copies of the same dataset; sharding distributes different data subsets. A sharded system can use replica sets for its shards.'),
    V('What do primary and secondaries mean in the basic replica-set picture?', 'The primary receives writes; secondaries replicate changes and may lag. An eligible member can become primary after an election, which can interrupt service.'),
    V('Why is replication not a replacement for backups?', 'Unwanted deletion or corruption can propagate to replicas. Independent backups and tested restoration remain necessary.'),
    V('What do mongos and a shard key do conceptually?', 'mongos routes requests in a sharded cluster; a shard key influences placement and routing. Bad key choices can create hotspots or broad queries.'),
    V('Were replica sets, sharding or failover configured/tested in this unit?', 'No. The syllabus requests a conceptual overview only, and all real programs ran on a standalone server.'),
    V('What should the Practical 2/3 journal and assessment statement include?', 'Actual installation/version/connectivity and CRUD evidence, input/output and negative cases, design reasoning and safe cleanup. This course has practical PA 20 + ESE 30, no theory ESE/PA; revision tasks are not an official theory paper.'),
]
VIVA = [G('Foundations and Practical Setup', _FOUNDATIONS), G('Insert, Find and Query Shaping', _READS),
        G('Update, Delete and Negative Cases', _WRITES), G('Modeling, Indexes and Aggregation', _MODEL_AGG),
        G('Distribution Concepts and Practical Evidence', _DISTRIBUTION)]
assert sum(len(g['items']) for g in VIVA) == 56
assert sum(len(g['items']) for g in SYNTAX) == 16

PRACTICE_QS = [
    Q('architecture', 'Draw the client-to-storage MongoDB architecture. Distinguish mongod, mongosh, a driver and Compass.',
      '<p>Draw application/driver or mongosh → connection → mongod → BSON collections, indexes and storage → result. mongod executes server operations; mongosh is a JavaScript-based client; a driver serves application code; Compass is an optional GUI client.</p><p>Installing mongosh does not establish a running server or data access. The local reference is not a hosted application, replica set or sharded cluster.</p>'),
    Q('Practical 2', 'Prepare an installation and connectivity procedure for your actual OS without exposing an unauthenticated database.',
      '<p>Identify OS/architecture; select its vendor-supported packages; install Community Server and mongosh; record both versions; start a localhost-bound server with appropriate private access; authenticate; select a disposable database; ping and verify an authorized insert/read round-trip.</p><p>Record actual observations. The reference used Debian 13 x86_64, server 9.0.4 and shell 2.14.0. Do not paste its Debian repository into an unrelated OS, put passwords in the journal or treat ping as proof of write permission.</p>'),
    Q('BSON', 'Explain database, collection, document, BSON and four required document value types. Include a type-mismatch example.',
      '<p>A database groups collections; a collection stores documents of named fields. BSON is typed binary storage. Required examples are ObjectId, String, Array and Embedded Document.</p><p>ObjectId("65a1b2c3d4e5f60718293040") differs from the plain string of that hex value. The fixture finds zero string-ID matches and one ObjectId match. _id can also be another suitable supported type, as in the integer student IDs.</p>'),
    Q('insert', 'Insert one record and then two records, attempt a duplicate ID, and explain the observed counts.',
      '<p>Use insertOne for _id:1 and insertMany for _id:2 and 3. Inspect acknowledgement and inserted IDs. The second insertMany has two inserted identifiers.</p><p>The attempted duplicate _id:1 is rejected with 11000, so three records remain. Catch only the expected error; do not hide unrelated failures. A batch is not automatically an all-or-nothing transaction.</p>'),
    Q('filters', 'Using the six students, derive the results for marks >80, marks <70, city in Surat/Bharuch, age >18 AND marks >80, and Surat OR marks <60.',
      '<p>Sorted ID results are [1,3,5], [4,6], [1,2,3,5], [1,5] and [1,3,5,6] respectively. Use $gt, $lt, $in, explicit $and and explicit $or.</p><p>State the strict boundaries. Conditions on different ordinary fields are implicitly ANDed; avoid duplicate JavaScript keys that overwrite earlier conditions.</p>'),
    Q('query shaping', 'Return only names and marks for the top three students with deterministic tie handling.',
      '<p>Use find({}, {_id:0,name:1,marks:1}).sort({marks:-1,_id:1}).limit(3).toArray() on the student collection.</p><p>Observed order: Neha 92, Asha 82, Meera 82. _id resolves the tie. Projection shapes the returned fields and does not alter stored data. Do not mix ordinary inclusion/exclusion modes; _id:0 is the allowed special case here.</p>'),
    Q('nested data', 'Compare a MongoDB skill query, a dotted pin query and whole-address equality.',
      '<p>{skills:"MongoDB"} matches IDs [1,3]. {"address.pin":"395001"} matches [1]. {address:{pin:"395001"}} matches none because the stored address also has state.</p><p>Array membership can match an element; dot notation targets a nested field. Whole-object equality is not a substitute for querying one nested property.</p>'),
    Q('updates', 'Apply $set/$inc, update inactive students, repeat a no-op update and update a missing ID. Explain matched/modified counts.',
      '<p>Ravi’s city change plus marks +5 reports 1/1. Adding 2 marks to the two inactive students reports 2/2. Setting Ravi to the already stored 75 reports 1/0; updating _id:999 reports 0/0.</p><p>matchedCount and modifiedCount answer different questions. Single-document updates are atomic, but updateMany is not automatically a transaction over all matched records.</p>'),
    Q('upsert/replacement', 'Explain the two upserts for _id:7 and the replacement that removes city.',
      '<p>The first upsert inserts Jai and reports upsertedCount:1; the second matches that same unique _id and updates marks, leaving one profile.</p><p>replaceOne with only name and marks removes city while retaining the existing _id. Use $set for partial updates; request upsert only when creating a missing document is intended.</p>'),
    Q('deletes', 'Delete student 6, then inactive students, and then an absent ID. State the remaining IDs and safety checks.',
      '<p>The operations report deleted counts 1, 1 and 0; IDs [1,2,3,5] remain. Preview the intended filter and confirm the current scratch database/collection.</p><p>deleteMany({}) removes all collection documents; drop removes the collection plus indexes. A preview count is not a lock, and a scratch-name prefix is not authorization or a recovery plan.</p>'),
    Q('negative cases', 'For explicit null, a missing tag and a string tag, explain three filters and two rejected command shapes.',
      '<p>{tag:null} returns [1,2]; {tag:{$type:10}} returns [1]; {tag:{$exists:false}} returns [2]. A string "1" does not match numeric _id:1.</p><p>The mixed projection is rejected by the server (31254 in this run). updateOne with a non-operator update is rejected by mongosh with MongoInvalidArgumentError. Validate external scalar types and build allowed query shapes rather than accepting arbitrary selector objects.</p>'),
    Q('modeling', 'Choose embedding or references for learner addresses and shared course details, and handle an unknown course ID.',
      '<p>Embed a bounded address when it is read with the learner. Reference a shared course by courseId to avoid copying its separately managed details into every learner.</p><p>Retrieve the course explicitly and handle null. The fixture accepts UNKNOWN because MongoDB does not automatically enforce a relational foreign key. Avoid unbounded embedded histories and do not assume two documents form one atomic transaction.</p>'),
    Q('indexing', 'Explain the city_marks index comparison and unique-email rejection without claiming a universal speedup.',
      '<p>The forced natural scan and forced compound index both return three documents. The scan examines six; the index examines three documents and three keys. Hints control this tiny fixture; no wall-clock multiplier or automatic optimizer choice is claimed.</p><p>A separate unique email index rejects an identical value with 11000. Indexes use storage and write work; real applications still need normalization, validation and a deliberate uniqueness policy.</p>'),
    Q('aggregation', 'Compute paid-order count, total and average per category; explain every required aggregation operator.',
      '<p>$match excludes the cancelled order, leaving five. $group uses _id:"$category"; $sum:1 counts inputs; $sum:"$amount" totals amounts; $avg:"$amount" computes the mean.</p><p>book has three paid orders 200+300+100 = 600, average 200. tool has two paid orders 400+600 = 1000, average 500. $sort fixes group output order and the read-only pipeline leaves six source orders unchanged.</p>'),
    Q('mini-catalog', 'Explain the three stock-decrement attempts from starting stock 2. State the atomicity boundary.',
      '<p>Filter {_id:"B101",stock:{$gte:1}} and apply {$inc:{stock:-1}} in one updateOne. The first two attempts each match one document, the third matches zero, and final stock is zero.</p><p>The server evaluates the guarded single-document update atomically. These reference attempts are sequential; there is no claimed concurrent stress test, payment-plus-stock transaction, trained model or remote deployment.</p>'),
    Q('replication', 'Draw a primary and two secondaries. Explain lag, possible election and why copies are not independent backups.',
      '<p>Show the same dataset on all three members. The primary accepts writes and secondaries replicate changes asynchronously; they can lag. An eligible member may become primary when the primary is unavailable, with a possible service interruption.</p><p>Deletion/corruption can replicate, so independent backups and restore testing are still necessary. The diagram is conceptual; this unit did not configure or failover-test a replica set.</p>'),
    Q('sharding', 'Draw a mongos router and two shards. Explain subsets, the shard key and the difference from replication.',
      '<p>Show different data subsets in the two shards, with mongos routing using configuration metadata. A shard key influences placement/routing and each shard in the standard self-managed design is a replica set.</p><p>Sharding distributes different subsets; replication copies the same dataset. Poor keys can create hotspots and unrelated queries may require broad work. No cluster setup or sharding benchmark is claimed.</p>'),
    Q('Practical 3', 'Prepare an acceptance-test journal for the independent CRUD scripts and mini-catalog.',
      '<p>Record actual versions, authorized connection/storage checks, fresh scratch contexts, input documents and observed output. Include all five listed filters, stable sort/limit/projection, nested/array queries, matched/no-op/missing results, duplicate keys, null/missing/type cases and targeted deletion.</p><p>Explain model/index decisions and aggregation totals, preserve credentials outside submissions and clean only the captured scratch databases. Replication/sharding remain conceptual. These tasks prepare practical PA/ESE and are not an official theory question paper.</p>'),
]
assert len(PRACTICE_QS) == 18
