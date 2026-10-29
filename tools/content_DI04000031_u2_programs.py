"""Fourteen MongoDB programs executed against a real authenticated mongod.

All seeds and displayed sources are explicit. Each run uses a fresh scratch
DB; no hidden seed, fake output, emulated query engine or cluster setup.
"""
from mongodb_content import P, GUARD

from content_DI04000031_u2_shared import STUDENTS, SEED, IDS

PROGRAMS = [
    P('ns2p01', 'Verify Connection, Database Selection and Collection Creation', '''
print("Server: " + db.version());
print("Ping: " + db.runCommand({ping: 1}).ok);
print("Scratch selected: " + db.getName()
  .startsWith("di04000031_u2_"));
db.createCollection("probe");
print("Collection exists: " + db.getCollectionNames()
  .includes("probe"));
db.probe.insertOne({_id: 1, message: "MongoDB connected"});
print("Stored message: " + db.probe.findOne({_id: 1}).message);
print("Collection dropped: " + db.probe.drop());
''', '<p>Real connectivity and collection operations on MongoDB. Selecting a database is a client-side choice; createCollection/insert materializes storage. The harness supplies a fresh prefix-guarded database and removes only that database afterward. Server and mongosh versions are recorded separately; the shell version is not the server version.</p>'),

    P('ns2p02', 'BSON Types and ObjectId versus String', '''
const oid = ObjectId("65a1b2c3d4e5f60718293040");
db.profiles.insertOne({
  _id: oid, name: "Asha", age: NumberInt(19),
  skills: ["MongoDB", "Python"],
  address: {city: "Surat"}, active: true,
  joined: ISODate("2026-01-15T00:00:00Z"), score: 82.5
});
const types = [
  ["_id", "objectId"], ["name", "string"],
  ["age", "int"], ["skills", "array"],
  ["address", "object"], ["active", "bool"],
  ["joined", "date"], ["score", "double"]
];
for (const [field, kind] of types) {
  const n = db.profiles.countDocuments({
    [field]: {$type: kind}
  });
  print(field + " / " + kind + ": " + n);
}
print("String ID matches: " + db.profiles.countDocuments({
  _id: "65a1b2c3d4e5f60718293040"
}));
print("ObjectId matches: " + db.profiles.countDocuments({
  _id: ObjectId("65a1b2c3d4e5f60718293040")
}));
print("UTC date: " + db.profiles.findOne({_id: oid})
  .joined.toISOString());
''', '<p>The $type filters inspect stored BSON types, not only JavaScript typeof. The same hexadecimal text is not equal to an ObjectId value. ISODate and NumberInt are mongosh constructors; this script is JavaScript for mongosh, not strict JSON. Fixed values make the captured output reproducible.</p>'),

    P('ns2p03', 'Insert One, Insert Many and Reject a Duplicate ID', '''
const one = db.students.insertOne({
  _id: 1, name: "Asha", marks: 82
});
print("insertOne acknowledged: " + one.acknowledged);
const many = db.students.insertMany([
  {_id: 2, name: "Ravi", marks: 70},
  {_id: 3, name: "Neha", marks: 92}
]);
print("insertMany count: " + Object.keys(many.insertedIds)
  .length);
let duplicateRejected = false;
try {
  db.students.insertOne({_id: 1, name: "Duplicate"});
} catch (e) {
  if (e.code !== 11000) throw e;
  duplicateRejected = true;
  print("Duplicate ID error: " + e.code);
}
if (!duplicateRejected) throw new Error("Expected duplicate ID");
print("Stored rows: " + db.students.countDocuments({}));
''', '<p>Integer _id values are deliberate for this lab; MongoDB does not require _id to be an ObjectId. An omitted _id normally receives an ObjectId. The default unique _id index rejects the duplicate with server error 11000. An acknowledged write is not a backup or evidence of replication on this standalone server.</p>'),

    P('ns2p04', 'Query Filters: $gt, $lt, $in, $and and $or', SEED + IDS + '''
print("gt80: " + JSON.stringify(ids({marks: {$gt: 80}})));
print("lt70: " + JSON.stringify(ids({marks: {$lt: 70}})));
print("inCities: " + JSON.stringify(ids({
  city: {$in: ["Surat", "Bharuch"]}
})));
print("and: " + JSON.stringify(ids({$and: [
  {age: {$gt: 18}}, {marks: {$gt: 80}}
]})));
print("or: " + JSON.stringify(ids({$or: [
  {city: "Surat"}, {marks: {$lt: 60}}
]})));
print("implicitAnd: " + JSON.stringify(ids({
  city: "Surat", marks: {$gt: 80}
})));
''', '<p>Every query runs against the six explicit seed documents. IDs are projected and sorted to make comparisons unambiguous. $gt/$lt are strict comparisons; $in tests membership; $and requires all clauses and $or at least one. Different ordinary fields in the same filter are implicitly ANDed.</p>'),

    P('ns2p05', 'Deterministic Sort, Limit and Projections', SEED + '''
const top = db.students.find({}, {
  _id: 0, name: 1, marks: 1
}).sort({marks: -1, _id: 1}).limit(3).toArray();
print("Top three: " + JSON.stringify(top));
const excluded = db.students.findOne({_id: 2}, {
  age: 0, active: 0, skills: 0, address: 0
});
print("Exclusion: " + JSON.stringify(excluded));
print("find returns cursor: " +
  (typeof db.students.find({}).toArray === "function"));
print("Missing findOne: " + JSON.stringify(
  db.students.findOne({_id: 999})
));
''', '<p>marks:-1 sorts descending; _id:1 breaks the 82-mark tie consistently. limit(3) is applied to the sorted query result. The inclusion projection hides _id explicitly; the exclusion projection retains unspecified fields. Do not mix ordinary inclusion and exclusion fields. find returns a cursor; findOne returns one document or null. toArray is suitable for this small fixture, not an unbounded production result.</p>'),

    P('ns2p06', 'Query Array Members and Embedded Fields', SEED + IDS + '''
print("MongoDB skill: " + JSON.stringify(ids({
  skills: "MongoDB"
})));
print("Python or Java: " + JSON.stringify(ids({
  skills: {$in: ["Python", "Java"]}
})));
print("Nested pin: " + JSON.stringify(ids({
  "address.pin": "395001"
})));
print("Whole-object match: " + JSON.stringify(ids({
  address: {pin: "395001"}
})));
print("Two skills: " + JSON.stringify(ids({$and: [
  {skills: "MongoDB"}, {skills: "Python"}
]})));
''', '<p>A scalar equality query can match an element of an array. Quoted dot notation targets a field inside an embedded object. Whole-object equality is different: the seed address also has state, so the shorter object is not an exact match. The two separate skill clauses require both values in the array, not the same single array element.</p>'),

    P('ns2p07', 'Update One/Many, $set/$inc and Result Counts', SEED + '''
const one = db.students.updateOne({_id: 2}, {
  $set: {city: "Surat"}, $inc: {marks: 5}
});
print("One: " + one.matchedCount + "/" + one.modifiedCount);
const many = db.students.updateMany({active: false}, {
  $inc: {marks: 2}
});
print("Many: " + many.matchedCount + "/" + many.modifiedCount);
const noop = db.students.updateOne({_id: 2}, {
  $set: {marks: 75}
});
print("No-op: " + noop.matchedCount + "/" + noop.modifiedCount);
const miss = db.students.updateOne({_id: 999}, {
  $set: {marks: 99}
});
print("Missing: " + miss.matchedCount + "/" + miss.modifiedCount);
print("Ravi: " + JSON.stringify(db.students.findOne(
  {_id: 2}, {_id: 0, name: 1, city: 1, marks: 1}
)));
''', '<p>$set changes named fields without replacing the whole document; $inc changes a numeric field. matchedCount and modifiedCount are different: setting 75 when 75 is already stored is a matched no-op. updateMany changes each matched document atomically, but the entire multi-document operation is not automatically one transaction.</p>'),

    P('ns2p08', 'Explicit Upsert versus Whole-Document Replacement', '''
const first = db.profiles.updateOne({_id: 7}, {
  $set: {name: "Jai", city: "Surat", marks: 60}
}, {upsert: true});
print("Created by upsert: " + first.upsertedCount);
const second = db.profiles.updateOne({_id: 7}, {
  $set: {marks: 65}
}, {upsert: true});
print("Second matched: " + second.matchedCount);
print("Profiles: " + db.profiles.countDocuments({}));
db.profiles.replaceOne({_id: 7}, {
  name: "Jai", marks: 70
});
const replaced = db.profiles.findOne({_id: 7});
print("ID retained: " + replaced._id);
print("City removed: " + !Object.hasOwn(replaced, "city"));
print("Remaining fields: " + Object.keys(replaced)
  .sort().join(","));
''', '<p>upsert:true inserts if there is no match, otherwise updates a match. A stable unique key is important; upsert is not a substitute for uniqueness constraints. replaceOne removes omitted non-_id fields; the existing _id is retained when it is omitted from the replacement. Prefer $set for a partial change. Never include a different _id in a replacement.</p>'),

    P('ns2p09', 'Targeted Deletes and Missing-Record Results', SEED + '''
print("Preview inactive: " + db.students.countDocuments({
  active: false
}));
print("deleteOne: " + db.students.deleteOne({_id: 6})
  .deletedCount);
print("deleteMany: " + db.students.deleteMany({active: false})
  .deletedCount);
print("Missing delete: " + db.students.deleteOne({_id: 999})
  .deletedCount);
print("Remaining IDs: " + JSON.stringify(db.students.find(
  {}, {_id: 1}
).sort({_id: 1}).toArray().map(x => x._id)));
''', '<p>Only the selected scratch collection is changed. deletedCount is zero for an absent record. deleteMany({}) would remove every document in that collection, while drop removes the collection and its indexes. Preview a filter and confirm the active database before destructive work. A preview count is not a lock against concurrent changes.</p>'),

    P('ns2p10', 'Embedded Address and Explicit Referenced-Course Lookup', '''
db.courses.insertOne({_id: "C1", title: "MongoDB Basics"});
db.learners.insertOne({
  _id: "L1", name: "Asha",
  address: {city: "Surat", pin: "395001"},
  courseId: "C1"
});
const learner = db.learners.findOne({_id: "L1"});
const course = db.courses.findOne({_id: learner.courseId});
print("Embedded city: " + learner.address.city);
print("Referenced course: " + course.title);
db.learners.insertOne({
  _id: "L2", name: "Ravi", courseId: "UNKNOWN"
});
const other = db.learners.findOne({_id: "L2"});
const missing = db.courses.findOne({_id: other.courseId});
print("Missing reference: " + (missing === null));
print("Reference inserted: " + db.learners.countDocuments({
  _id: "L2"
}));
''', '<p>The bounded address is embedded because it is read with its learner. Shared course details are referenced by an ID and fetched explicitly. MongoDB does not automatically join these documents or enforce a relational foreign key: the missing course reference is accepted. Application logic must handle absence and define consistency rules. This is not a $lookup or multi-document transaction demo.</p>'),

    P('ns2p11', 'Indexes, Forced Explain Comparison and Unique Email', SEED + '''
const filter = {city: "Surat", marks: {$gt: 80}};
const scan = db.students.find(filter)
  .hint({$natural: 1}).explain("executionStats");
db.students.createIndex({city: 1, marks: -1}, {
  name: "city_marks"
});
const indexed = db.students.find(filter)
  .hint("city_marks").explain("executionStats");
print("Scan returned/examined: " +
  scan.executionStats.nReturned + "/" +
  scan.executionStats.totalDocsExamined);
print("Index returned/examined: " +
  indexed.executionStats.nReturned + "/" +
  indexed.executionStats.totalDocsExamined);
print("Index keys examined: " +
  indexed.executionStats.totalKeysExamined);
print("Indexes: " + db.students.getIndexes()
  .map(x => x.name).sort().join(","));
db.accounts.createIndex({email: 1}, {unique: true});
db.accounts.insertOne({_id: 1, email: "asha@example.test"});
let rejected = false;
try {
  db.accounts.insertOne({_id: 2, email: "asha@example.test"});
} catch (e) {
  if (e.code !== 11000) throw e;
  rejected = true;
  print("Unique email error: " + e.code);
}
if (!rejected) throw new Error("Expected duplicate email");
print("Accounts: " + db.accounts.countDocuments({}));
''', '<p>The two hints deliberately force a natural scan and the named compound index so a six-document lab can compare examined-document counters. This does not claim the optimizer would always choose the index, nor a guaranteed time speedup. The query returns the same three documents. A separate unique index rejects a duplicate email with server error 11000. Indexes cost storage and write work; case normalization/collation policy still needs design.</p>'),

    P('ns2p12', 'Aggregation: $match, $group, $sum and $avg', '''
db.orders.insertMany([
  {_id: 1, category: "book", status: "paid", amount: 200},
  {_id: 2, category: "book", status: "paid", amount: 300},
  {_id: 3, category: "tool", status: "paid", amount: 400},
  {_id: 4, category: "tool", status: "cancelled", amount: 100},
  {_id: 5, category: "book", status: "paid", amount: 100},
  {_id: 6, category: "tool", status: "paid", amount: 600}
]);
const summary = db.orders.aggregate([
  {$match: {status: "paid"}},
  {$group: {
    _id: "$category", count: {$sum: 1},
    total: {$sum: "$amount"}, average: {$avg: "$amount"}
  }},
  {$sort: {_id: 1}}
]).toArray();
print(JSON.stringify(summary));
print("Source documents unchanged: " +
  db.orders.countDocuments({}));
''', '<p>$match keeps five paid orders from six inputs. $group produces two category summaries; $sum:1 counts documents and $sum:"$amount" adds their values. $avg computes the group average. "$category" is a field path, not a literal category name. $sort makes the output order deterministic. This read-only pipeline does not modify orders; integer demo amounts avoid floating-point currency claims.</p>'),

    P('ns2p13', 'Practical 3 Mini-Catalog with Guarded Stock Update', '''
db.products.insertMany([
  {_id: "B101", name: "NoSQL Guide", category: "book",
   pricePaise: 25000, stock: 2, attributes: {pages: 320}},
  {_id: "E101", name: "Sensor Node", category: "electronics",
   pricePaise: 129900, stock: 5,
   attributes: {sampleRateHz: 10}}
]);
print("Books: " + JSON.stringify(db.products.find(
  {category: "book"}, {_id: 0, name: 1, pricePaise: 1}
).sort({name: 1, _id: 1}).limit(5).toArray()));
for (let attempt = 1; attempt <= 3; attempt++) {
  const r = db.products.updateOne({
    _id: "B101", stock: {$gte: 1}
  }, {$inc: {stock: -1}});
  print("Sale " + attempt + " matched: " + r.matchedCount);
}
print("Final stock: " + db.products.findOne({_id: "B101"})
  .stock);
print("Missing delete: " + db.products.deleteOne({
  _id: "UNKNOWN"
}).deletedCount);
''', '<p>A small product catalog combines different nested attributes with insert/find/sort/limit/projection/update/delete. Price is stored in integer paise for this lab. The filter and decrement occur in one atomic single-document update; after two successes the third attempt matches nothing, so stock does not go negative. This is not a transaction covering payment plus stock, a concurrency stress test, an AI model or a hosted application.</p>'),

    P('ns2p14', 'Null/Missing, Type Mismatch and Rejected Query Shapes', '''
db.notes.insertMany([
  {_id: 1, tag: null}, {_id: 2}, {_id: 3, tag: "mongodb"}
]);
const ids = q => db.notes.find(q, {_id: 1})
  .sort({_id: 1}).toArray().map(x => x._id);
print("Null equality: " + JSON.stringify(ids({tag: null})));
print("Explicit null: " + JSON.stringify(ids({
  tag: {$type: 10}
})));
print("Missing field: " + JSON.stringify(ids({
  tag: {$exists: false}
})));
print("String ID matches: " + JSON.stringify(ids({_id: "1"})));
let mixedRejected = false;
try {
  db.notes.find({}, {tag: 1, other: 0}).toArray();
} catch (e) {
  mixedRejected = true;
  print("Mixed projection rejected: " + e.code);
}
if (!mixedRejected) throw new Error("Expected projection error");
let updateRejected = false;
try {
  db.notes.updateOne({_id: 1}, {tag: "changed"});
} catch (e) {
  updateRejected = true;
  print("Non-operator update rejected: " + e.name);
}
if (!updateRejected) throw new Error("Expected update error");
const incoming = {$ne: null};
print("Selector-shaped input rejected: " +
  (typeof incoming !== "string"));
''', '<p>{tag:null} matches explicit null and missing fields; $type:10 selects BSON null and $exists:false selects absence. A string "1" does not match numeric _id:1. The server rejects mixed ordinary projection modes; mongosh rejects an update document without atomic operators for updateOne. Validate external scalar types and build an allowlisted filter rather than passing an arbitrary user-supplied selector object. The final check is a type-validation illustration, not a complete login/API implementation.</p>'),
]

SOURCES = {p['id']: p['code']['en'] + '\n' for p in PROGRAMS}
assert len(PROGRAMS) == 14
assert all(s.startswith(GUARD) for s in SOURCES.values())
