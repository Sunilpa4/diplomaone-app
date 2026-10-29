"""Sixteen complete Cypher files: import executes all on REAL authenticated Neo4j.

Every example has a fresh constraint-backed namespace claim and owned cleanup.
Graph recommendation/fraud outputs are transparent basic pattern-query examples,
not implemented GDS algorithms, trained AI or verified company deployments.
"""
from neo4j_content import P
from content_DI04000031_u4_shared import PERSON_SEED, SOCIAL_SEED, MOVIE_SEED, BANK_SEED

PAIR_SEED='''CREATE (:@@L@@:Person {person_id:'P01',name:'Asha'});
CREATE (:@@L@@:Person {person_id:'P02',name:'Ravi'});
MATCH (a:@@L@@:Person {person_id:'P01'}),
      (b:@@L@@:Person {person_id:'P02'})
CREATE (a)-[:KNOWS {since:2024}]->(b);
'''

PROGRAMS=[
P('ns4p01','Verify Neo4j, Write a Node and Read it Back','''
// @result server_components
CALL dbms.components() YIELD name,versions,edition
RETURN name,versions,edition;
// @result created_probe
// @stats
CREATE (p:@@L@@:Probe {probe_id:1,message:'Graph connected'})
RETURN p.probe_id AS id,p.message AS message;
// @result stored_roundtrip
MATCH (p:@@L@@:Probe {probe_id:1}) RETURN p.message AS message;
''','<p>The version/edition come from the real server, followed by a committed node write and separate read-back. Counters are actual driver summary counters, not invented acknowledgements.</p><p>The administrative header atomically claims one disposable scope with a newly created named constraint. It is a safety wrapper, not a requirement to understand every graph query first. Only that owned graph/schema is removed at the end.</p>'),

P('ns4p02','Nodes, Multiple Labels and Typed Properties','''
CREATE (:@@L@@:Person:Student {
  person_id:'P01',name:'Asha',age:20,active:true,
  score:85.5,skills:['Python','Cypher'],
  joined:date('2026-10-29'),
  observed_at:datetime('2026-10-29T09:00:00Z')
});
// @result typed_person
MATCH (p:@@L@@:Person {person_id:'P01'})
RETURN p.name AS name,p.age AS age,p.active AS active,
  p.score AS score,p.skills AS skills,p.joined AS joined,
  p.observed_at AS observed_at,p:Student AS student_label;
''','<p>A node can carry several labels. String, integer, boolean, float, homogeneous string list, date and zoned datetime values are real stored properties. The runner displays temporal values as ISO text without changing their database types.</p><p>Use an application business ID, not an assumed durable internal node ID. Maps can be query values but cannot be stored as a nested property map; a genuine TypeError example appears in program 16.</p>'),

P('ns4p03','Create a Typed Directed Relationship with Properties',PAIR_SEED+'''
// @result stored_relationship
MATCH (a:@@L@@:Person)-[r:KNOWS]->(b:@@L@@:Person)
RETURN a.name AS source,type(r) AS relationship,
  b.name AS target,r.since AS since;
''','<p>The two existing scoped nodes become endpoints of one KNOWS relationship with since=2024. Every stored relationship has one direction and one type; its properties are optional.</p><p>The arrow represents the modeled direction, not a universal rule that real friendship is one-way. An undirected read can traverse either orientation without creating a reverse duplicate.</p>'),

P('ns4p04','MATCH, WHERE, RETURN and Value Filters',PERSON_SEED+'''
// @result surat_adults
MATCH (p:@@L@@:Person)
WHERE p.city='Surat' AND p.age>=20
RETURN p.person_id AS id,p.name AS name,p.age AS age ORDER BY id;
// @result selected_ages
MATCH (p:@@L@@:Person) WHERE p.age IN [19,23]
RETURN p.person_id AS id,p.name AS name ORDER BY id;
// @result either_condition
MATCH (p:@@L@@:Person) WHERE p.city='Bharuch' OR p.age>22
RETURN p.person_id AS id,p.name AS name ORDER BY id;
// @result string_is_not_integer
MATCH (p:@@L@@:Person) WHERE p.age='20'
RETURN p.person_id AS id ORDER BY id;
''','<p>MATCH finds a pattern, WHERE restricts it and RETURN chooses columns. Surat age-at-least-20 gives Asha and Imran; ages 19/23 give Neha and Dev. Typed numeric equality is not automatic string-to-number conversion.</p><p>These are declarative graph queries. The filtered rows and ordered output do not prove a latency improvement, and a missing match is an empty result rather than an error.</p>'),

P('ns4p05','Read Outgoing, Incoming and Undirected Connections',SOCIAL_SEED+'''
// @result asha_outgoing
MATCH (a:@@L@@:Person {person_id:'P01'})
      -[:KNOWS]->(b:@@L@@:Person)
RETURN b.person_id AS id,b.name AS name ORDER BY id;
// @result ravi_incoming
MATCH (a:@@L@@:Person {person_id:'P02'})
      <-[:KNOWS]-(b:@@L@@:Person)
RETURN b.person_id AS id,b.name AS name ORDER BY id;
// @result ravi_either_direction
MATCH (a:@@L@@:Person {person_id:'P02'})
      -[:KNOWS]-(b:@@L@@:Person)
RETURN b.person_id AS id,b.name AS name ORDER BY id;
''','<p>Asha has stored outgoing links to Ravi and Neha. Ravi has an incoming link from Asha; ignoring direction finds Asha, Meera and Imran.</p><p>The undirected read does not change the stored arrows or establish reciprocal business consent. Match direction according to the relationship meaning and query requirement.</p>'),

P('ns4p06','ORDER BY, LIMIT, DISTINCT and Simple Counts',PERSON_SEED+'''
// @result oldest_three
MATCH (p:@@L@@:Person)
RETURN p.person_id AS id,p.name AS name,p.age AS age
ORDER BY age DESC,id ASC LIMIT 3;
// @result distinct_cities
MATCH (p:@@L@@:Person)
RETURN DISTINCT p.city AS city ORDER BY city;
// @result people_per_city
MATCH (p:@@L@@:Person)
RETURN p.city AS city,count(p) AS people ORDER BY city;
// @result surat_count
MATCH (p:@@L@@:Person) WHERE p.city='Surat'
RETURN count(p) AS people;
''','<p>The oldest three are Dev 23, Meera 22 and Ravi 21. A secondary business-ID order makes ties deterministic. DISTINCT cities removes repeated values; grouping counts Surat=3 and the other listed cities=1 each.</p><p>Cypher ORDER BY and aggregation are not Cassandra partition-key rules. Without ORDER BY, a particular row order is not a result contract. LIMIT controls returned rows, not every possible traversal cost.</p>'),

P('ns4p07','MERGE, ON CREATE and ON MATCH','''
// @result first_merge
MERGE (p:@@L@@:Person {person_id:'P09'})
ON CREATE SET p.name='Jai',p.visits=1
ON MATCH SET p.visits=p.visits+1
RETURN p.person_id AS id,p.name AS name,p.visits AS visits;
// @result second_merge
MERGE (p:@@L@@:Person {person_id:'P09'})
ON CREATE SET p.name='Jai',p.visits=1
ON MATCH SET p.visits=p.visits+1
RETURN p.person_id AS id,p.name AS name,p.visits AS visits;
// @result one_business_node
MATCH (p:@@L@@:Person {person_id:'P09'}) RETURN count(p) AS people;
''','<p>The first MERGE creates Jai with visits 1; the second matches the same ID and changes visits to 2. There is one business node.</p><p>MERGE matches the complete specified pattern, not every human interpretation of identity. Use a stable identity pattern and an appropriate uniqueness constraint; MERGE alone is not a general concurrent uniqueness guarantee. CREATE normally creates a new element, while MATCH alone does not create a missing one.</p>'),

P('ns4p08','SET and REMOVE: Properties, Labels and a Missing Match',PERSON_SEED+'''
// @result updated_ravi
MATCH (p:@@L@@:Person {person_id:'P02'})
SET p.city='Surat',p.age=22
RETURN p.name AS name,p.city AS city,p.age AS age;
// @result removed_city
MATCH (p:@@L@@:Person {person_id:'P02'}) REMOVE p.city
RETURN p.name AS name,p.city AS city,p.age AS age;
// @result label_added
MATCH (p:@@L@@:Person {person_id:'P02'}) SET p:Graduate
RETURN p.name AS name,p:Graduate AS graduate;
// @result label_removed
MATCH (p:@@L@@:Person {person_id:'P02'}) REMOVE p:Graduate
RETURN p.name AS name,p:Graduate AS graduate;
// @result missing_update
MATCH (p:@@L@@:Person {person_id:'P99'}) SET p.city='Surat'
RETURN p.person_id AS id;
// @result people_unchanged
MATCH (p:@@L@@:Person) RETURN count(p) AS people;
''','<p>Ravi changes to Surat/22, then city is removed while age remains. An absent property reads as null; null is not a stored nested empty object. Graduate is added and removed without deleting the node.</p><p>MATCH plus SET on absent P99 returns no rows and creates no node: all six people remain. This is different from ordinary Cassandra UPDATE upsert semantics. SET n = map replaces all properties; SET n += map updates/merges the supplied properties.</p>'),

P('ns4p09','DELETE a Relationship, Reject Connected Deletion and DETACH',PAIR_SEED+'''
// @result connected_node_rejected
// @expect Neo.ClientError.Schema.ConstraintValidationFailed
MATCH (p:@@L@@:Person {person_id:'P01'}) DELETE p;
// @result asha_still_present
MATCH (p:@@L@@:Person {person_id:'P01'}) RETURN count(p) AS people;
// @result delete_relationship
// @stats
MATCH (a:@@L@@:Person {person_id:'P01'})
      -[r:KNOWS]->(:@@L@@:Person {person_id:'P02'}) DELETE r;
// @result delete_now_isolated_asha
// @stats
MATCH (p:@@L@@:Person {person_id:'P01'}) DELETE p;
MATCH (r:@@L@@:Person {person_id:'P02'})
CREATE (r)-[:KNOWS]->(:@@L@@:Person {person_id:'P03',name:'Neha'});
// @result detach_ravi
// @stats
MATCH (p:@@L@@:Person {person_id:'P02'}) DETACH DELETE p;
// @result remaining_people
MATCH (p:@@L@@:Person)
RETURN p.person_id AS id,p.name AS name ORDER BY id;
''','<p>Plain DELETE of connected Asha is genuinely rejected. Deleting the KNOWS relationship leaves its endpoint nodes; Asha can then be deleted as an isolated node. Later DETACH DELETE removes Ravi and his incident relationship, leaving Neha.</p><p>DETACH DELETE can remove relationships to other endpoints: preview and bound the target carefully. Never run a whole-database delete in a shared database. Logical disappearance is not a claim of immediate physical disk erasure.</p>'),

P('ns4p10','OPTIONAL MATCH and Null-Aware Relationship Counts',PERSON_SEED+'''
MATCH (a:@@L@@:Person {person_id:'P01'}),
      (b:@@L@@:Person {person_id:'P02'}) CREATE (a)-[:MENTORS]->(b);
// @result optional_mentees
MATCH (p:@@L@@:Person)
OPTIONAL MATCH (p)-[:MENTORS]->(mentee:@@L@@:Person)
RETURN p.person_id AS id,mentee.name AS mentee ORDER BY id;
// @result row_vs_linked_count
MATCH (p:@@L@@:Person)
OPTIONAL MATCH (p)-[:MENTORS]->(mentee:@@L@@:Person)
RETURN count(*) AS rows,count(mentee) AS linked;
// @result only_linked_people
MATCH (p:@@L@@:Person)
OPTIONAL MATCH (p)-[:MENTORS]->(mentee:@@L@@:Person)
WITH p,mentee WHERE mentee IS NOT NULL
RETURN p.name AS mentor,mentee.name AS mentee ORDER BY mentor;
''','<p>OPTIONAL MATCH preserves each person even without a matched outgoing MENTORS relationship; the optional value is null. Asha mentors Ravi in this fixture. There are six rows but only one non-null mentee.</p><p>count(*) counts rows and count(mentee) ignores null. A later WITH/WHERE that requires a non-null mentee removes the unmatched rows. Choose this behaviour deliberately rather than accidentally discarding isolated entities.</p>'),

P('ns4p11','A Scoped Uniqueness Constraint and Real Failed-Write Rollback','''
CREATE (:@@L@@:Person {person_id:'P01',name:'Asha'});
CREATE CONSTRAINT @@C@@
FOR (p:@@L@@) REQUIRE p.person_id IS UNIQUE;
CALL db.awaitIndexes(60);
// @result business_constraint
SHOW CONSTRAINTS YIELD name,type,properties
WHERE name='@@C@@' RETURN name,type,properties;
// @result backing_index
SHOW INDEXES YIELD state,owningConstraint
WHERE owningConstraint='@@C@@'
RETURN state,owningConstraint;
// @result duplicate_rejected
// @expect Neo.ClientError.Schema.ConstraintValidationFailed
CREATE (:@@L@@:Person {person_id:'P98',name:'Transient'})
CREATE (:@@L@@:Person {person_id:'P01',name:'Duplicate'});
// @result failed_statement_rolled_back
MATCH (p:@@L@@:Person {person_id:'P98'}) RETURN count(p) AS people;
CREATE (:@@L@@:Person {name:'No ID'});
// @result missing_id_is_allowed_by_uniqueness_only
MATCH (p:@@L@@:Person)
RETURN p.person_id AS id,p.name AS name ORDER BY id;
DROP CONSTRAINT @@C@@;
''','<p>The scoped uniqueness constraint has an ONLINE backing index. A duplicate ID is rejected; P98 from the same failed statement is absent, showing rollback of that single implicit transaction. A later statement creates a person with no ID: uniqueness alone is not a required-property constraint.</p><p>This is schema/identity awareness, not an execution-plan or timing benchmark. The separate lab-claim constraint protects ownership and is not a business-ID policy. Both the business constraint and lab claim are explicitly removed only when owned.</p>'),

P('ns4p12','Parameterized Queries: Input Remains a Value',PERSON_SEED+'''
// @params {"name":"Asha"}
// @result parameter_match
MATCH (p:@@L@@:Person) WHERE p.name=$name
RETURN p.person_id AS id,p.name AS name,p.city AS city ORDER BY id;
// @params {"name":"Asha' OR true //"}
// @result selector_shaped_text_is_not_query_code
MATCH (p:@@L@@:Person) WHERE p.name=$name
RETURN p.person_id AS id ORDER BY id;
// @params {"name":"Nobody"}
// @result missing_parameter_value
MATCH (p:@@L@@:Person) WHERE p.name=$name
RETURN p.person_id AS id ORDER BY id;
''','<p>The same fixed Cypher query is executed with official-driver parameters. Asha matches; the quote/operator-shaped string is treated as a literal name and returns no rows, not an expanded WHERE clause.</p><p>@params is a comment annotation for this runner. In Browser/cypher-shell, set the parameter through the client parameter facility first. Validate application input and keep credentials private; parameterization does not itself provide authorization, privacy policy or permission to run arbitrary source.</p>'),

P('ns4p13','Social and Movie Candidate Examples with Basic Patterns',MOVIE_SEED+'''
// @result friend_candidates
MATCH (me:@@L@@:Person {person_id:'P01'})
      -[:KNOWS]-(:@@L@@:Person)-[:KNOWS]-(c:@@L@@:Person)
WHERE c<>me AND NOT (me)-[:KNOWS]-(c)
RETURN DISTINCT c.person_id AS id,c.name AS name ORDER BY id;
// @result unseen_movies_liked_by_known_people
MATCH (me:@@L@@:Person {person_id:'P01'})
      -[:KNOWS]-(friend:@@L@@:Person)-[:LIKES]->(m:@@L@@:Movie)
WHERE NOT (me)-[:LIKES]->(m)
RETURN DISTINCT m.movie_id AS id,m.title AS title ORDER BY id;
''','<p>The two-hop basic pattern gives Meera/P04 and Imran/P05 after excluding self/direct connections and deduplicating paths. Friends’ liked movies not already liked by Asha give Database Stories/M02 and Space Signals/M03.</p><p>These are transparent candidate queries for Practical 8, not graph-algorithm implementations, GDS procedures, a trained recommender or a relevance/latency evaluation. LinkedIn-like connections and Netflix-like viewing are workload analogies; this lab does not establish those companies’ actual Neo4j deployments.</p>'),

P('ns4p14','Shared-Device Banking Patterns: Review Candidates, Not Fraud',BANK_SEED+'''
// @result accounts_per_device
MATCH (a:@@L@@:Account)-[:USES_DEVICE]->(d:@@L@@:Device)
RETURN d.device_id AS device,count(DISTINCT a) AS accounts
ORDER BY device;
// @result shared_device_pairs
MATCH (a:@@L@@:Account)-[:USES_DEVICE]->(d:@@L@@:Device)
      <-[:USES_DEVICE]-(b:@@L@@:Account)
WHERE a.account_id<b.account_id
RETURN d.device_id AS device,a.account_id AS account_a,
  b.account_id AS account_b ORDER BY device,account_a,account_b;
''','<p>D01 is used by A01, A02 and A04, giving three distinct unordered account pairs. D02 is used only by A03 and contributes no pair. The less-than condition excludes self and symmetric duplicate pairs.</p><p>A shared device is a possible review signal, not a fraud verdict: family/shared computers and public access can be legitimate. No real bank records, criminal identification, classifier, ring-detection algorithm or GDS library is used. Governance, consent, context, false positives and human review remain essential.</p>'),

P('ns4p15','Import a Synthetic JSON Fixture with Parameters and UNWIND','''
// @params_file graph_fixture.json
// @result imported_people
// @stats
UNWIND $people AS row
CREATE (p:@@L@@:Person) SET p=row;
// @params_file graph_fixture.json
// @result imported_friendships
// @stats
UNWIND $friendships AS row
MATCH (a:@@L@@:Person {person_id:row.from}),
      (b:@@L@@:Person {person_id:row.to})
CREATE (a)-[:KNOWS {since:row.since}]->(b);
// @result verify_every_person
MATCH (p:@@L@@:Person)
RETURN p.person_id AS id,p.name AS name,p.city AS city,p.age AS age
ORDER BY id;
// @result verify_every_relationship
MATCH (a:@@L@@:Person)-[r:KNOWS]->(b:@@L@@:Person)
RETURN a.person_id AS source,b.person_id AS target,r.since AS since
ORDER BY source,target;
''','<p>The runner actually reads the supplied JSON and passes its arrays as official-driver parameters; UNWIND creates six people, then six KNOWS relationships. Every stored person/edge/property is read back and compared with the fixture in validation.</p><p>The file also contains the separately demonstrated movie and banking fixtures; this program imports only people/friendships. It is not LOAD CSV, live ingestion or a trained AI data pipeline. SET p=row replaces properties but leaves the scope/domain labels intact. Each statement is its own implicit transaction, not one multi-statement atomic import.</p>'),

P('ns4p16','Actual Cypher Rejections, Flexible Types and Missing Results',PERSON_SEED+'''
// @result nested_property_map_rejected
// @expect Neo.ClientError.Statement.TypeError
CREATE (:@@L@@:Bad {payload:{nested:1}});
// @result unknown_variable_rejected
// @expect Neo.ClientError.Statement.SyntaxError
RETURN unknown.name AS name;
// @result null_merge_key_rejected
// @expect Neo.ClientError.Statement.SemanticError
MERGE (:@@L@@:Person {person_id:null});
// @result bad_pattern_syntax
// @expect Neo.ClientError.Statement.SyntaxError
MATCH (p:@@L@@:Person RETURN p.name;
// @result valid_people_unchanged
MATCH (p:@@L@@:Person) RETURN count(p) AS people;
// @result missing_person
MATCH (p:@@L@@:Person {person_id:'P99'}) RETURN p.name AS name;
''','<p>All four failure codes come from the actual Neo4j server. A nested property map is not a valid stored property; an unbound variable/bad pattern is a syntax error; MERGE cannot use a null identifying property.</p><p>Six valid people remain and missing P99 returns an empty list. Error messages, internal IDs, timings and non-error notifications are not invented as stable output. This is a flexible property-graph model, not a Cassandra table with mandatory column types.</p>'),
]
assert len(PROGRAMS)==16
