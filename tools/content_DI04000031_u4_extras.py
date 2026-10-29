"""16 Neo4j reference cards, 56 answered viva and 18 practical revision tasks.
No official theory question paper or per-question marks are invented.
"""
from nosql_content import SX,V,Q,tr,code
from content_DI04000031_u4_notes import SN


def G(title,items):return {'title':tr(title),'items':items}

SYNTAX=[
 G('Tools, Graph Elements and Read Queries',[
  SX('Verify the real server',SN['version'],'Server metadata and connectivity checks. Also perform a stored write/read. Desktop, Browser, driver and server version numbers are different evidence.'),
  SX('Property-graph pattern',"(p:Person:Student {person_id:'P01'})\n(a)-[r:KNOWS {since:2024}]->(b)\n// Node labels may be multiple; relationship type is one.",
     'Pattern notation summary. Labels classify; properties describe; the arrow is the stored relationship direction. A label is not an automatic primary-key constraint.'),
  SX('MATCH, WHERE and RETURN',SN['match'],'On the reference six-person fixture, the result is P01 Asha 20 and P05 Imran 20. Complete files add the explicit disposable scope label.'),
  SX('Outgoing, incoming and undirected reads',SN['directions'],'The read pattern can ignore direction without changing stored arrows or creating reverse duplicate relationships.'),
 ]),
 G('Ordering, Creation and Updates',[
  SX('Sort, limit, distinct and grouping',"MATCH (p:Person)\nRETURN p.person_id AS id,p.age AS age\nORDER BY age DESC,id ASC LIMIT 3;\nMATCH (p:Person)\nRETURN DISTINCT p.city AS city ORDER BY city;",
     'Use a tie-breaker for stable top rows. DISTINCT deduplicates returned values/tuples; LIMIT is not a bound on every traversal cost.'),
  SX('CREATE versus identity MERGE',SN['merge'],'First MERGE creates Jai/visits 1; the second matches and sets visits 2. Match the intended complete identity pattern and enforce appropriate uniqueness.'),
  SX('SET and REMOVE',SN['update'],'Properties and labels can change without deleting the node. Missing MATCH plus SET is not an upsert. SET n=map replaces properties; SET n+=map changes supplied properties.'),
  SX('Relationship/node deletion',SN['delete'],'Plain connected-node DELETE is rejected; DELETE r preserves endpoints; DETACH DELETE removes the selected node and all its incident relationships. Preview and bound the owned scope.'),
 ]),
 G('Nulls, Identity and Safe Data Input',[
  SX('OPTIONAL MATCH and counts',"MATCH (p:Person)\nOPTIONAL MATCH (p)-[:MENTORS]->(m:Person)\nRETURN count(*) AS rows,count(m) AS linked;",
     'The reference has six person rows and one non-null mentee. Optional-match predicates and later non-null filtering have different row-preservation effects.'),
  SX('Business uniqueness',SN['constraint'],'Scope schema deliberately. Uniqueness has an index-backed implementation but alone does not require the property to exist; the example does not promise a timing speedup.'),
  SX('Parameters are client-supplied values',SN['params'],'The :param line is a client command. The Python runner instead sends a parameter dictionary; // @params annotations are ordinary comments, not server Cypher syntax.'),
  SX('Actual fixture import',SN['unwind'],'Program 15 supplies graph_fixture.json as driver parameters and really creates six people and six KNOWS edges. Verify every ID/property/endpoint/year, not only input length.'),
 ]),
 G('Application Patterns and Evidence Boundaries',[
  SX('Two-hop connection candidates',SN['friend'],'The fixture gives P04 Meera and P05 Imran. Exclude self/direct connections and deduplicate paths. This is an introductory pattern query, not a GDS algorithm or trained model.'),
  SX('Unseen movie candidates',SN['movie'],'Returns M02 Database Stories and M03 Space Signals, excluding already-liked M01. This does not evaluate ranking quality or establish Netflix’s actual deployment.'),
  SX('Shared-device review pairs',SN['bank'],'D01 yields A01–A02, A01–A04 and A02–A04; single-account D02 yields no pair. A shared device is a review signal, not a fraud verdict.'),
  SX('Algorithm and execution scope',"EXECUTED: basic Cypher on private Community 5.26.32\nGUIDED: your own Desktop/Aura and Browser workflow\nCONCEPTUAL: graph-algorithm families and AI use cases\nNOT CLAIMED: GDS implementation, training or benchmarks",
     'Use actual observations in the journal. LinkedIn-like/Netflix-like are workload analogies, not verified company Neo4j deployment claims. No official theory-paper marks exist for this practical course.'),
 ]),
]
assert sum(len(g['items']) for g in SYNTAX)==16

VIVA=[
 G('Property-Graph Foundations',[
  V('What is Neo4j?', 'A graph database using a property-graph model: nodes, directed typed relationships, labels and properties, queried with Cypher.'),
  V('What does a node represent?', 'An entity such as a Person, Movie, Account or Device. Choose independently meaningful entities rather than making every scalar a separate node automatically.'),
  V('How many labels can a node have?', 'Zero to many. A Person can also be a Student; this is one node with multiple classifications, not two duplicated people.'),
  V('What is required of a stored relationship?', 'It connects source and target endpoints, has a direction and exactly one relationship type. Endpoints can be the same node, and properties are optional.'),
  V('Can a relationship have properties?', 'Yes. A KNOWS relationship may store since=2024; that value describes the connection rather than either endpoint’s identity.'),
  V('What are a path and a hop?', 'A path alternates nodes and relationships; one hop is one relationship step. Asha–Ravi–Meera is a two-hop example.'),
  V('Does a Person label automatically make person_id unique?', 'No. Labels classify nodes. Define an appropriate uniqueness constraint when business identity requires one.'),
  V('Does graph mean relational databases cannot store connections?', 'No. Relational systems can store and join related data. A graph is a workload/modeling choice when connection paths are central, not a universal replacement.'),
 ]),
 G('Installation, Tools and Evidence',[
  V('Desktop versus Community Server?', 'Desktop is a local development/management application with its own developer-license edition/tooling. Community Server is the database edition actually used in this reference.'),
  V('What is AuraDB?', 'A managed Neo4j database service. The student uses an authorized account, checks tier/cost terms, saves credentials privately and follows the provided encrypted connection details.'),
  V('What is Neo4j Browser?', 'An interactive query/visualization client connecting to a database. It is not the storage engine, and opening it is not proof that a database write worked.'),
  V('Which versions were really tested?', 'Neo4j Community and Cypher Shell 5.26.32, official Python driver 5.28.8, Temurin Java 21.0.13+9 and Python 3.13.16 on Debian 13 x86_64.'),
  V('Was Desktop or Aura provisioned by the reference?', 'No. Those routes and Browser exploration are guided procedures. Actual evidence comes from the private Community server, real driver runs and matching Cypher Shell.'),
  V('What are the usual local Browser/Bolt ports?', 'Browser HTTP commonly uses 7474 and Bolt 7687. The private reference deliberately uses 7475 and 7688; use the actual settings of your own instance.'),
  V('Why is a stored write/read stronger than a version command?', 'It proves an authorized connection can store and retrieve the expected data. A client binary version alone does not establish a working server or storage round-trip.'),
  V('How should database credentials be handled?', 'Use a hidden prompt or private manager/environment, keep interfaces private and retain TLS verification for remote services. Do not embed passwords in shared code, public URIs, screenshots or submissions.'),
 ]),
 G('Reading with Cypher',[
  V('What do MATCH, WHERE and RETURN do?', 'MATCH binds a graph pattern; WHERE restricts matches; RETURN selects entities/expressions and optionally aliases the output columns.'),
  V('What are parentheses, brackets and braces used for?', 'Parentheses describe nodes, square brackets describe relationships and braces contain property maps within a graph pattern.'),
  V('Is the variable p a permanent stored node name?', 'No. It is a query-local variable referring to matched/created elements. Carry needed variables through WITH when moving to a later pipeline stage.'),
  V('What happens for a valid missing-node match?', 'It returns no rows. That is different from an invalid query, undefined variable or syntax error.'),
  V('Does an undirected KNOWS read create reverse relationships?', 'No. It traverses either stored orientation for that query while leaving the graph unchanged.'),
  V('How do you make top-three output deterministic?', 'Use ORDER BY with an appropriate secondary business-ID tie-breaker, then LIMIT 3. Without ordering, do not promise a particular row sequence.'),
  V('What exactly does DISTINCT remove?', 'Duplicate returned values or tuples. It does not delete stored duplicate nodes and is not automatically the correct choice when the question counts paths.'),
  V('Does LIMIT 1 guarantee little query work?', 'No. Limiting returned rows is not a universal bound on scanning/expansion work. Use selective entry points and bounded patterns, then measure when necessary.'),
 ]),
 G('Graph Writes and Deletion',[
  V('CREATE versus MATCH?', 'CREATE makes new elements; MATCH binds existing patterns. Missing MATCH does not automatically create a node.'),
  V('What is the exact role of MERGE?', 'It matches the complete specified pattern, otherwise creates it. ON CREATE/ON MATCH can perform branch-specific SET actions.'),
  V('Why is a changing name a poor identity MERGE component?', 'When that property changes, the whole pattern may not match and a new node can be attempted. Match a stable business identity and SET mutable attributes deliberately.'),
  V('Is MERGE alone a universal concurrent uniqueness guarantee?', 'No. Use an appropriate uniqueness constraint and consider transaction/concurrency requirements; the displayed two sequential MERGEs are not a concurrent load test.'),
  V('Does MATCH plus SET on P99 upsert a new person?', 'No. In the reference the missing match returns no rows and all six existing people remain, unlike ordinary Cassandra UPDATE’s missing-key upsert behaviour.'),
  V('SET n=map versus SET n+=map?', 'The first replaces all node properties; the second updates/merges the supplied properties. Labels are separate from the property map.'),
  V('What happens when a property is removed or set to null?', 'It is absent and a read of that property evaluates to null. Null is not stored as an ordinary property value.'),
  V('DELETE r, DELETE n and DETACH DELETE n?', 'DELETE r removes a selected relationship only. DELETE n requires no remaining incident relationships; DETACH DELETE n also removes all incident relationships, while other endpoints remain unless selected.'),
 ]),
 G('Nulls, Identity, Transactions and Input',[
  V('Why use OPTIONAL MATCH?', 'To preserve already matched rows when an optional relationship/pattern is missing, returning null for the optional elements rather than discarding the row.'),
  V('count(*) versus count(mentee) in the reference?', 'There are six rows and one non-null mentee. count(*) counts all rows; count(mentee) ignores null.'),
  V('Does uniqueness require the property to exist?', 'No. The demonstrated Community uniqueness rule accepts a Person without person_id; required-property/key/type rules have separate edition/version requirements.'),
  V('What does P98 count 0 after the duplicate prove?', 'The valid P98 creation and conflicting P01 creation were in one failed statement transaction; P98 was rolled back. It does not prove that all earlier separate statements were undone.'),
  V('Is the entire runner file one transaction?', 'No. Each statement is an implicit auto-commit transaction. Finally cleanup is an owned lab safeguard, not a replacement for application transaction design or backups.'),
  V('Why use query parameters?', 'To keep the query structure fixed and supply values separately. The selector-shaped name remains a literal value rather than becoming an injected WHERE clause.'),
  V('Are :param and // @params the same as native Cypher?', 'No. :param is a client command; // @params is a comment interpreted by this Python runner. A native query uses the supplied value through $name.'),
  V('Can a map be a stored property because UNWIND uses maps?', 'No. A parameter/query map can supply valid primitive properties via SET n=map, but nested map-valued properties are rejected with a real TypeError.'),
 ]),
 G('Recommendation, Banking and AI Examples',[
  V('Who are Asha’s two-hop candidates?', 'Meera/P04 and Imran/P05, after excluding Asha and her direct connections and applying DISTINCT. Dev/P06 is three hops away in this fixture.'),
  V('Why can Meera otherwise appear twice?', 'Two different two-hop routes reach her: through Ravi and through Neha. Deduplicate only when the desired output is a distinct candidate rather than a path count.'),
  V('Which movies are unseen candidates for Asha?', 'M02 Database Stories and M03 Space Signals, liked by known people and not already liked by Asha. M01 Graph Journeys is excluded.'),
  V('Does the movie example train a recommender?', 'No. It is a transparent basic pattern lookup. There is no trained model, graph-algorithm implementation, ranking-quality result or latency claim.'),
  V('Do the LinkedIn/Netflix examples establish those companies use Neo4j?', 'No. They are syllabus-named workload analogies. A claim about an actual company deployment would need verified primary evidence and is not made here.'),
  V('Which device/accounts generate review pairs?', 'D01 has A01, A02 and A04, giving A01–A02, A01–A04 and A02–A04. D02 has only A03 and generates no shared pair.'),
  V('Why is a shared device not a fraud verdict?', 'Legitimate family/public-device usage, reassignment and data errors can create overlaps. Context, consent, false-positive evaluation and human review are essential.'),
  V('Are graph algorithms or GDS implemented in this unit?', 'No. Similarity, centrality, community detection, path finding and link-prediction ideas are conceptual examples. Only introductory Cypher patterns are executed; no GDS algorithm or mathematical proof is implemented.'),
 ]),
 G('Practical Safety, Verification and Assessment',[
  V('What exactly is imported in program 15?', 'The actual JSON people/friendships arrays: six people with ID/name/city/age, then six KNOWS edges with endpoints/since. Movie/banking arrays are present but used separately, not imported by that program.'),
  V('Why compare every imported element instead of a count only?', 'Correct counts can hide wrong properties or edges. Verify each business ID/value and each source/target/year triple against the synthetic input.'),
  V('What does the fresh ownership constraint protect?', 'Its uniquely named CREATE is an atomic namespace claim. Ownership begins only after success; a pre-existing or failed claim must not authorize removing somebody else’s scope/schema.'),
  V('Why not use IF NOT EXISTS for the ownership claim?', 'A non-creating success could mean the object already belonged to another run. It would not establish new cleanup ownership.'),
  V('Is this runner a general Cypher security sandbox?', 'No. It guards trusted prepared teaching files and captured scope cleanup; arbitrary untrusted Cypher requires a different security/authorization design.'),
  V('Does visible deletion prove immediate disk erasure?', 'No. Logical deletion and space reuse are not an immediate physical-byte-erasure guarantee, nor is a normal delete an undo/backup mechanism.'),
  V('What must the Practical 7–8 journal distinguish?', 'Your actual Desktop/Aura/Browser setup/observations, the executed reference server output, synthetic inputs, positive/negative queries, candidate/AI limits and owned cleanup. Never label guided GUI steps as performed evidence.'),
  V('What is the official assessment and what remains pending?', 'Theory ESE/PA 0; course practical PA 20 plus ESE 30 gives 50. Tasks have no invented theory-paper marks. This release is Unit 4 only; Redis Unit 5 is still a separate pending unit.'),
 ]),
]
assert sum(len(g['items']) for g in VIVA)==56

PRACTICE_QS=[
 Q('practical','Plan and record the official Practical 7 setup without overstating the reference.',
   '<p>Choose your authorized Desktop or AuraDB route, check current OS/security/tier terms, install/create your learning instance, keep credentials private, start/connect and record actual server/edition/version/database. The reference is Community Server 5.26.32, not a performed Desktop/Aura installation. Include your own Browser observations rather than submitting CLI evidence as a GUI screenshot.</p>'),
 Q('practical','Create a small Browser graph and explain why another query shows only a table.',
   '<p>In a fresh authorized disposable graph, create the two PracticePerson nodes and KNOWS relationship. Return entities for graph visualization, then scalar properties for table output. Inspect arrows, labels and since=2024.</p>'+code(SN['first_graph'])+code(SN['graph_view'])+code(SN['table_view'])),
 Q('design','Model a user-to-movie-to-user question and justify properties versus nodes.',
   '<p>Use Person nodes with stable person_id and Movie nodes with stable movie_id/title, connected by LIKES. A simple age/city can be a Person property; use separate City entities only if city-specific identity/relationships matter. Define direction and identity rules. Do not turn every scalar into a node or claim a graph always outperforms relational joins.</p>'),
 Q('practical','Store two people and one relationship with a relationship property.',
   '<p>Use program 3. The actual stored row is Asha / KNOWS / Ravi / since 2024. The relationship has exactly one type and a source/target direction; it can be read in reverse/either direction without creating another relationship.</p>'),
 Q('query','Find Surat people aged at least 20 and predict the exact reference result.',
   code(SN['match'])+'<p>Expected P01 Asha 20 and P05 Imran 20, ordered by ID. Neha is 19 and is excluded. Program 4 also verifies age-string equality is not integer equality and a valid missing match is empty.</p>'),
 Q('query','Explain Ravi’s incoming versus either-direction KNOWS neighbours.',
   '<p>Incoming to P02 finds Asha/P01. Either-direction at P02 finds Asha/P01, Meera/P04 and Imran/P05. The stored graph is not modified and no reciprocal-consent fact is inferred.</p>'),
 Q('query','Produce the oldest three and a per-city person count.',
   code(SN['sort'])+'<p>Top three: Dev 23, Meera 22, Ravi 21. City counts: Bharuch 1, Rajkot 1, Surat 3, Vadodara 1. The secondary ID order handles equal ages deterministically; LIMIT does not guarantee cheap execution.</p>'),
 Q('practical','Run the same identity MERGE twice and compare it with CREATE.',
   code(SN['merge'])+'<p>Observed Jai/P09 visits 1 then 2 and one business node. CREATE would create a new node unless a constraint prevented duplication. MERGE matches the whole specified pattern; do not put mutable name/city fields into identity casually.</p>'),
 Q('practical','Update Ravi, remove a property/label and attempt a missing-key update.',
   '<p>Program 8 updates Ravi to Surat/22; REMOVE city leaves city null and age 22. Graduate is true after SET and false after REMOVE. MATCH plus SET for absent P99 returns no rows and creates no person; all six people remain. This is not Cassandra UPDATE upsert behaviour.</p>'),
 Q('practical','Demonstrate relationship-only deletion, connected-node rejection and DETACH safely.',
   '<p>Program 9’s connected Asha DELETE is rejected with the actual Neo.ClientError.Schema.ConstraintValidationFailed code. DELETE r removes one KNOWS edge while endpoints remain; deleting now-isolated Asha removes one node. Later DETACH Ravi removes one node and one incident relationship, leaving P03 Neha. Preview scope; do not use a whole-database wipe.</p>'),
 Q('query','Use OPTIONAL MATCH and explain six rows versus one non-null link.',
   code(SN['optional'])+'<p>Asha/P01 has mentee Ravi; P02–P06 return null. count(*) is 6 and count(mentee) is 1. A later WITH/WHERE mentee IS NOT NULL intentionally leaves only Asha/Ravi.</p>'),
 Q('practical','Show a uniqueness rejection and prove the failed statement did not partly persist.',
   '<p>Program 11 creates a scoped person_id uniqueness rule and observes its ONLINE backing index. One statement tries P98 then conflicting P01; it fails and P98 count is 0. A later No ID person is accepted, showing uniqueness alone is not existence. Earlier separate commits are not automatically rolled back.</p>'),
 Q('security','Pass a quote/operator-shaped name safely as data.',
   code(SN['params'])+'<p>The driver supplies the value separately to fixed query text. Asha matches; the literal name containing an apostrophe and OR true // returns no rows. Do not concatenate user input into Cypher. Parameters do not replace authorization, validation or privacy controls.</p>'),
 Q('practical','Import graph_fixture.json and verify every social element.',
   '<p>Run the guarded program 15 with the supplied fixture folder. Actual counters show six people and six KNOWS relationships. Compare every person ID/name/city/age and every directed endpoint/since triple with the input. The file’s movie/banking arrays are not imported by this program; no hidden seed or live/AI pipeline is claimed.</p>'),
 Q('application','Explain the actual two-hop candidates and Meera’s duplicate paths.',
   code(SN['friend'])+'<p>Return Meera/P04 and Imran/P05. Asha and direct neighbours are excluded. Meera is reachable through Ravi and Neha, so DISTINCT removes repeated candidate rows. Dev/P06 is three hops away. This is a basic candidate pattern, not an implementation of GDS/similarity algorithms or a trained recommender.</p>'),
 Q('application','Find unseen movie candidates and state what the result does not prove.',
   code(SN['movie'])+'<p>M02 Database Stories and M03 Space Signals are returned; already-liked M01 is excluded. No ranking quality, model training, Netflix deployment, watch-history completeness or real-time benchmark is established.</p>'),
 Q('application','List shared-device review pairs and two reasons not to call them fraud.',
   code(SN['bank'])+'<p>D01 gives A01–A02, A01–A04 and A02–A04; D02/A03 gives no shared pair. Family/public computers and device reassignment/data errors can be legitimate explanations. Use authorized context, false-positive evaluation, consent/retention and human review; a pattern is not a verdict.</p>'),
 Q('journal','Prepare an honest CO4 demonstration and revision checklist.',
   '<p>Include actual Desktop/Aura/Browser setup evidence, versions/edition, password-free connection details, model/key rationale, input and parameters, exact Cypher, real read-back/counters and server rejection codes, all-element import checks, recommendation exclusions, banking/AI limits and owned cleanup. Describe algorithm families conceptually only; no GDS implementation or graph proof is required. This is a practical course with PA 20 + ESE 30 = 50 and no official theory-paper marks.</p>'),
]
assert len(PRACTICE_QS)==18
