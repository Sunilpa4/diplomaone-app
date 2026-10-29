"""Neo4j Unit 4: twenty English lessons, CO4 and Practicals 7–8.
Desktop/Aura/Browser guidance is explicitly separated from real server evidence.
Graph-algorithm families are examples only, never implementations or proofs.
"""
from nosql_content import make_T, table

SOURCES=[
 ('GTU DI04000031 syllabus, effective 2025–26','https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf'),
 ('Neo4j property-graph concepts','https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/'),
 ('Neo4j deployment choices and releases','https://neo4j.com/deployment-center/'),
 ('Neo4j 5 system and Java requirements','https://neo4j.com/docs/operations-manual/5/installation/requirements/'),
 ('Neo4j 5 Linux tarball installation','https://neo4j.com/docs/operations-manual/5/installation/linux/tarball/'),
 ('Neo4j Desktop installation','https://neo4j.com/docs/desktop/current/installation/'),
 ('Aura: create an instance','https://neo4j.com/docs/aura/getting-started/create-instance/'),
 ('Neo4j Browser: connect to an instance','https://neo4j.com/docs/browser/operations/dbms-connection/'),
 ('Cypher Shell client guide — reference client 5.26.32','https://neo4j.com/docs/operations-manual/current/cypher-shell/'),
 ('Cypher 5 MATCH','https://neo4j.com/docs/cypher-manual/5/clauses/match/'),
 ('Cypher 5 CREATE','https://neo4j.com/docs/cypher-manual/5/clauses/create/'),
 ('Cypher 5 MERGE','https://neo4j.com/docs/cypher-manual/5/clauses/merge/'),
 ('Cypher 5 SET','https://neo4j.com/docs/cypher-manual/5/clauses/set/'),
 ('Cypher 5 DELETE','https://neo4j.com/docs/cypher-manual/5/clauses/delete/'),
 ('Cypher 5 OPTIONAL MATCH','https://neo4j.com/docs/cypher-manual/5/clauses/optional-match/'),
 ('Cypher 5 constraints and edition boundaries','https://neo4j.com/docs/cypher-manual/5/constraints/'),
 ('Cypher 5 parameters','https://neo4j.com/docs/cypher-manual/5/syntax/parameters/'),
 ('Neo4j Graph Data Science algorithm families — conceptual reference only','https://neo4j.com/docs/graph-data-science/current/algorithms/'),
]

SN={
 'first_graph':"""CREATE (a:PracticePerson {person_id:'P01',name:'Asha'}),
       (b:PracticePerson {person_id:'P02',name:'Ravi'}),
       (a)-[:KNOWS {since:2024}]->(b);""",
 'graph_view':"""MATCH (a:PracticePerson)-[r:KNOWS]->(b:PracticePerson)
RETURN a,r,b;""",
 'table_view':"""MATCH (a:PracticePerson)-[r:KNOWS]->(b:PracticePerson)
RETURN a.name AS source,type(r) AS relation,
       b.name AS target,r.since AS since;""",
 'version':"""CALL dbms.components() YIELD name,versions,edition
RETURN name,versions,edition;
RETURN 1 AS connected;""",
 'shell':"""# On YOUR computer; use its actual connection settings.
export NEO4J_URI=bolt://127.0.0.1:7687
bin/cypher-shell --address "$NEO4J_URI" --username neo4j
# Enter YOUR password at the hidden prompt, not in shared notes.""",
 'typed':"""CREATE (:PracticePerson:Student {
  person_id:'P01',name:'Asha',age:20,active:true,
  skills:['Python','Cypher'],joined:date('2026-10-29')
});""",
 'match':"""MATCH (p:Person)
WHERE p.city='Surat' AND p.age>=20
RETURN p.person_id AS id,p.name AS name,p.age AS age
ORDER BY id;""",
 'directions':"""(a)-[:KNOWS]->(b)  // outgoing from a
(a)<-[:KNOWS]-(b)  // incoming to a
(a)-[:KNOWS]-(b)   // read either orientation
// Parentheses = nodes; brackets = relationship.""",
 'sort':"""MATCH (p:Person)
RETURN p.person_id AS id,p.name AS name,p.age AS age
ORDER BY age DESC,id ASC LIMIT 3;

MATCH (p:Person)
RETURN p.city AS city,count(p) AS people ORDER BY city;""",
 'merge':"""MERGE (p:Person {person_id:'P09'})
ON CREATE SET p.name='Jai',p.visits=1
ON MATCH SET p.visits=p.visits+1
RETURN p.person_id,p.name,p.visits;""",
 'update':"""MATCH (p:Person {person_id:'P02'})
SET p.city='Surat',p.age=22;
MATCH (p:Person {person_id:'P02'}) REMOVE p.city;
MATCH (p:Person {person_id:'P02'}) SET p:Graduate;
MATCH (p:Person {person_id:'P02'}) REMOVE p:Graduate;""",
 'delete':"""MATCH (a:PracticePerson {person_id:'P01'})
      -[r:KNOWS]->(:PracticePerson {person_id:'P02'})
DELETE r;
// An isolated node can be deleted without DETACH.
MATCH (p:PracticePerson {person_id:'P01'}) DELETE p;
// Preview the selected owned node before destructive DETACH.
MATCH (p:PracticePerson {person_id:'P02'}) DETACH DELETE p;""",
 'optional':"""MATCH (p:Person)
OPTIONAL MATCH (p)-[:MENTORS]->(mentee:Person)
RETURN p.person_id AS id,mentee.name AS mentee
ORDER BY id;""",
 'constraint':"""CREATE CONSTRAINT practice_person_id
FOR (p:PracticePerson) REQUIRE p.person_id IS UNIQUE;
SHOW CONSTRAINTS YIELD name,type,properties;
// Drop ONLY a constraint that you created/own.
DROP CONSTRAINT practice_person_id;""",
 'params':"""// Browser/cypher-shell client command, not server Cypher:
:param name => 'Asha'
// Server query; $name is supplied separately by the client.
MATCH (p:Person) WHERE p.name=$name
RETURN p.person_id AS id,p.name AS name;""",
 'unwind':"""// $people is a client-supplied array of property maps.
UNWIND $people AS row
CREATE (p:PracticePerson) SET p=row;
// A map can supply properties; it cannot be nested as
// a stored map-valued property such as p.payload={x:1}.""",
 'friend':"""MATCH (me:Person {person_id:'P01'})
      -[:KNOWS]-(:Person)-[:KNOWS]-(candidate:Person)
WHERE candidate<>me AND NOT (me)-[:KNOWS]-(candidate)
RETURN DISTINCT candidate.person_id AS id,
       candidate.name AS name ORDER BY id;""",
 'movie':"""MATCH (me:Person {person_id:'P01'})
      -[:KNOWS]-(friend:Person)-[:LIKES]->(m:Movie)
WHERE NOT (me)-[:LIKES]->(m)
RETURN DISTINCT m.movie_id AS id,m.title AS title
ORDER BY id;""",
 'bank':"""MATCH (a:Account)-[:USES_DEVICE]->(d:Device)
      <-[:USES_DEVICE]-(b:Account)
WHERE a.account_id<b.account_id
RETURN d.device_id AS device,a.account_id AS account_a,
       b.account_id AS account_b
ORDER BY device,account_a,account_b;""",
}
T=make_T(SN)
def S(title,items):return {'title':{'en':title},'items':items}

NOTES=[
S('1. Graph Foundations, Scope and Modeling',[
 T('1.1 Official scope, practical assessment and honest evidence','''
<p><b>Unit 4: Graph Databases — Neo4j, 12 hours / 20% content weightage.</b> CO4 is “Utilize Neo4j to solve relationship-based problems with graph queries.” The emphasis is application-oriented graph concepts, installation, basic Cypher and graph operations. There are no mathematical graph proofs or graph-algorithm implementations in this unit.</p>
<p><b>Practical 7</b> asks for Neo4j Desktop or Aura setup and exploration of nodes, relationships and properties in Browser. <b>Practical 8</b> asks for node/relationship creation and MATCH, WHERE, RETURN queries with friend-recommendation or fraud-use-case demonstrations. The guided Desktop/Aura/Browser procedure and the executed reference are not the same evidence.</p>
<p>The reference actually runs a private authenticated <b>Neo4j Community 5.26.32</b> server with <b>Cypher Shell 5.26.32</b>, official Python driver <b>5.28.8</b>, <b>Temurin Java 21.0.13+9</b> and Python 3.13.16 on Debian 13 x86_64. All 16 full programs are sent to the real database. The reference does <b>not</b> claim Desktop installation, Aura provisioning, Browser GUI automation, clustering, a GDS installation, model training or a performance benchmark.</p>
<p>This is a practical-only course: theory ESE/PA are 0; practical PA 20 + ESE 30 = 50 for the <b>course</b>. Twenty percent is unit content weightage, not an invented theory-paper allocation or per-question mark scheme. Use the answered tasks and viva to prepare your actual journal and demonstration.</p>''',programs=['ns4p01']),
 T('1.2 Property graph: nodes, labels, relationships and properties','''
<p>A <b>node</b> represents an entity such as a person, film, account or device. A node can have zero, one or several <b>labels</b>, such as Person and Student. Labels classify nodes; a label is not an automatic primary-key or required-property declaration.</p>
<p>A <b>relationship</b> connects a source node to a target node, has exactly one type such as KNOWS or LIKES, and always has a stored direction. The endpoints may even be the same node. Multiple relationships between the same pair can exist when the model permits them.</p>
<p>Both nodes and relationships can have <b>properties</b>, for example a person’s name/age or a KNOWS relationship’s since year. The property graph is not a drawing format: it is a data model supporting stored entities and connection queries.</p>'''+table(['Component','Reference meaning'],[
 ('Person node P01','Asha, age 20, city Surat'),('Person/Student labels','Several classifications can describe one node'),
 ('P01 -[KNOWS]-> P02','One stored directed typed relationship'),('since: 2024','A property of that relationship, not another endpoint'),
 ('person_id: P01','Application business ID; enforce intended uniqueness explicitly')])+'''
<p>Default schema flexibility does not remove the need for consistent naming, validation, identity rules and access controls. Keep application IDs stable; do not assume an internal node identifier is a permanent external business key.</p>''','ns4_property',programs=['ns4p02','ns4p03']),
 T('1.3 Direction, paths, hops and application-oriented graph theory','''
<p>A <b>path</b> alternates nodes and relationships. A traversal follows relationships according to the pattern and conditions. A <b>hop</b> is one relationship step; Asha → Ravi → Meera is two hops. A node’s degree is about incident relationships, not automatically popularity, trust or a prediction.</p>
@@directions@@
<p>The first two patterns respect the selected direction; the third reads either orientation while leaving storage unchanged. In the fixture, Asha has outgoing KNOWS links to Ravi and Neha. Ravi’s incoming link is from Asha; ignoring direction finds Asha, Meera and Imran.</p>
<p>Decide the business meaning. FOLLOWS may be intentionally asymmetric. “KNOWS” in this tiny fixture is stored once and read without direction for a connection-suggestion example; that is not proof of reciprocal consent or friendship quality. An undirected query is not a command to create reverse duplicate relationships.</p>
<p>Bound the question and path length. Two hops through a high-degree node can still produce many candidates. A graph sketch or short query does not prove asymptotic/runtime performance, and this unit does not implement BFS, DFS, PageRank or community-detection procedures.</p>''','ns4_direction',programs=['ns4p05','ns4p13']),
 T('1.4 Design a graph from relationship questions, not from circles alone','''
<p>Start with the questions: Who is connected to Asha? What do known people like that she has not liked? Which account pairs share a device? Then choose entities, relationship types/direction and properties that make those paths meaningful.</p>
<ol><li>Give independently identifiable entities appropriate node labels and stable business IDs.</li><li>Name relationship types by meaning: Person KNOWS Person, Person LIKES Movie, Account USES_DEVICE Device.</li><li>Place an attribute on its owner: birth/age on a person; since year on a connection.</li><li>Choose a uniqueness rule and decide how updates/deletions affect relationships.</li><li>Use a selective entry condition and bounded traversal; review access, retention and bias.</li></ol>
<p>Do not turn every scalar into a node automatically. City may be a Person property for simple filtering; a City node with LIVES_IN relationships can be justified if city entities and their connections matter. Avoid both an enormous opaque property blob and meaningless relationship proliferation.</p>
<p>Relational databases can also store and query relationships. A graph is attractive when connection paths are central; it is not a universal replacement for stable tables, transactional ledgers or ordinary reporting. Evaluate constraints, data volume, query patterns, operational cost and actual measured behaviour.</p>''',programs=['ns4p03','ns4p14']),
]),
S('2. Installation, Desktop/Aura and the Browser Workbench',[
 T('2.1 Practical 7 setup: choose Desktop or Aura deliberately','''
<p><b>Desktop route:</b> check the official OS requirements and current security notices, download from the Neo4j deployment center, install the application, create a local database instance/project as supported by that Desktop version, set a private password, choose a compatible database version and start it. Desktop is a development/management application; its included Developer-license edition is not the same thing as Community Server or an unrestricted production license.</p>
<p><b>Aura route:</b> use your own authorized account in the Aura console, choose a suitable <b>AuraDB</b> learning instance/tier, check any billing/limits before creating resources, save the generated credentials privately and wait for the instance to be ready. Use the service-provided encrypted connection URI. Do not create paid resources, activate algorithm services or share database credentials merely to follow a note.</p>
<p>Record the actual deployment, edition, server version, connection URI without a password, database name and successful write/read. UI labels and availability change; follow the linked official instructions for your release. This reference has <b>not</b> installed Desktop or provisioned Aura, and its server output must not be submitted as if it were your Browser/desktop screenshot evidence.</p>
<p><b>Reference server alternative:</b> a checksum-verified official Community 5.26.32 tarball and Temurin 21 runtime run on loopback only. Authentication is enabled and a random private initial password is set before launch. A tiny heap/page cache is a constrained teaching choice, not recommended production sizing. The GTU resource list recommends an 8 GB learning computer. Debian 13 was actually used here; that observation is not a claim of vendor certification for an OS absent from the versioned support matrix.</p>''','ns4_setup'),
 T('2.2 Browser exploration: connection, graph view and table view','''
<p>Open Browser/Query from your own Desktop/Aura instance, or the bundled Browser address of your own local server. For an ordinary local installation, the usual Browser URL is <b>http://localhost:7474/browser</b> and Bolt URI <b>bolt://localhost:7687</b>. Those addresses refer to <b>your computer</b>, not this published notes app or a remote workspace. Check the instance’s actual ports and encryption settings.</p>
<ol><li>Choose the matching connection scheme, supply your authorized username/password and select the intended database.</li><li>Run RETURN 1 and the component query; inspect the reported server/edition rather than just an application version.</li><li>In an empty, authorized disposable learning database, create a small graph with a unique practice label.</li><li>Return nodes/relationships for graph visualization; select elements to inspect labels, properties, type and arrow direction.</li><li>Return scalar columns for table-style observations, and compare the results with the model.</li><li>Record screenshots/observations from your own actual interface and remove only owned practice data.</li></ol>
@@first_graph@@
@@graph_view@@
@@table_view@@
<p><b>Important:</b> RETURN a,r,b supplies graph entities; RETURN a.name,b.name supplies values. A scalar result appearing as a table is not a broken database or missing relationships. Browser is a client, not the database engine. No Browser GUI test or fabricated screenshot is claimed by the reference.</p>
<p>The bundled local Browser may use an unencrypted local connection in this private lab. For remote/Aura connections, retain the supported TLS scheme/certificate verification; do not bypass certificate errors or expose a default-password service publicly.</p>''','ns4_browser',programs=['ns4p01','ns4p03']),
 T('2.3 Separate tools, verify a stored round-trip and protect access','''
@@version@@
@@shell@@
<p><b>Neo4j Server</b> stores the graph. <b>Desktop</b> manages local development instances/tools. <b>AuraDB</b> is a managed database service. <b>Browser</b> is an interactive query/visualization client. <b>Cypher Shell</b> is a command-line client; the <b>official Python driver</b> is an application client. They are not interchangeable installation/edition claims.</p>
<p>The reference really observes Server/Community and Cypher Shell <b>5.26.32</b>, Java <b>21.0.13+9</b> and Python driver <b>5.28.8</b>. It uses Bolt <b>127.0.0.1:7688</b> and local HTTP <b>127.0.0.1:7475</b>, not the usual default ports. These exact patch versions are reference evidence, not a timeless latest-release guarantee. Neo4j 5.26 LTS and newer calendar-version releases coexist; match the documentation/Cypher language version to your server.</p>
<p>Java 17/21 are supported by the versioned 5.26 requirements; this lab uses Java 21. Desktop manages its own compatible runtime. Use platform instructions rather than copying Linux paths to Windows or assuming that a different default Java is sufficient.</p>
<p>Passwords belong in a protected manager/private environment or a hidden client prompt, never a public URI, source file, screenshot or submission. Keep database and management interfaces private. Default-password/anonymous rejection and a successful committed write/read are stronger evidence than a version command alone; they do not by themselves establish production TLS, backup, authorization design or security hardening.</p>''',programs=['ns4p01']),
]),
S('3. Basic Cypher and Graph CRUD',[
 T('3.1 CREATE, labels, properties and values that can be stored','''
@@typed@@
<p>CREATE makes a new graph element; repeated CREATE can produce duplicates unless a relevant constraint prevents them. The example uses two labels on one node, not two copies of Asha. Scalar strings, numbers, booleans, temporal values and suitable homogeneous property arrays are supported.</p>
<p>A query can construct a map or receive a list of maps as parameters. That does <b>not</b> mean a nested map can be stored as a property value: CREATE (:Bad {payload:{nested:1}}) is actually rejected with a server TypeError in program 16. Choose properties or related nodes for structured graph data.</p>
<p>Absent properties evaluate as null. Setting a property to null removes it; null is not stored as an ordinary property value. A label does not make every node have the same fields/types. This flexible model differs from Cassandra’s explicit table columns and fixed primary-key design.</p>
<p>Use consistent business IDs and property naming, and deliberately add appropriate identity constraints. A normal node CREATE is not an INSERT upsert; ordinary MATCH is a read/bind operation, while MERGE has separate complete-pattern semantics.</p>''',programs=['ns4p02','ns4p03','ns4p16']),
 T('3.2 MATCH → WHERE → RETURN: pattern, filter and projection','''
@@match@@
<p>Parentheses describe nodes, colon introduces a label/type, square brackets describe a relationship, braces hold properties, and a variable names a matched element. Variables such as p are local to the query/pipeline; a stored node is not literally named “p.”</p>
<p>MATCH binds the requested graph pattern. WHERE applies conditions such as equality, comparisons, IN, AND or OR. RETURN selects entities or expressions and aliases columns. With the six-person fixture, Surat and age at least 20 gives <b>P01 Asha 20</b> and <b>P05 Imran 20</b>. Ages 19/23 select Neha/Dev; Bharuch or age greater than 22 selects Ravi/Dev.</p>
<p>p.age='20' does not equal integer 20 in the demonstrated equality filter; it returns no rows rather than silently converting the string. Missing P99 is an empty result, not automatically an error. Use parameters for application-supplied values.</p>
<p>The arrows/pattern matter as much as the properties. Avoid accidentally matching unrelated independent variables and forming a Cartesian product. A syntactically valid query can still answer the wrong business question.</p>''','ns4_query',programs=['ns4p04','ns4p05']),
 T('3.3 Stable ordering, limiting, DISTINCT and aggregation','''
@@sort@@
<p>The oldest-three query returns <b>Dev 23, Meera 22, Ravi 21</b>. Add a stable ID tie-breaker when primary sort values may tie. Without ORDER BY, do not promise the same row order across plans, data or versions. LIMIT is useful for small displays but is not a guarantee that little traversal work occurred.</p>
<p>DISTINCT removes duplicate returned values/tuples, not necessarily duplicate stored nodes or relationships. Different paths can reach the same recommendation candidate. Decide whether your question counts paths, relationships or distinct entities.</p>
<p>Grouping by city gives <b>Surat 3</b> and <b>Bharuch/Rajkot/Vadodara 1 each</b>. count(*) counts rows; count(expression) ignores null expressions. A WITH clause can carry selected variables/aggregates to a later part of the query, and variables not carried forward are no longer available there.</p>
<p>These are tiny-query observations, not graph-wide analytic performance evidence. Query-specific indexes can help entry lookups, but high-degree expansion and large result sets still need a workload-appropriate design.</p>''',programs=['ns4p06','ns4p10','ns4p13']),
 T('3.4 CREATE versus MATCH versus MERGE','''
@@merge@@
<p>On a new P09, the first MERGE creates Jai with visits 1; the second finds that complete ID pattern and changes visits to 2. The read-back counts one business node.</p>'''+table(['Clause/approach','Meaning and caution'],[
 ('CREATE','Create a new element/pattern; repeated data can duplicate without constraints'),
 ('MATCH','Bind existing patterns; no match produces no row and no automatic creation'),
 ('MERGE','Match the complete specified pattern, otherwise create it'),
 ('ON CREATE / ON MATCH','Apply selected SET actions on the corresponding MERGE branch'),
 ('Business-ID uniqueness','An explicit schema rule, not an assumption from a Person label')])+'''
<p>Do not put every changeable field into an identity MERGE pattern. Changing name/city can mean the whole pattern no longer matches and a new node is attempted. Match/merge the intended stable identity, then SET changeable values. A null identifying property is not allowed in the demonstrated MERGE.</p>
<p>MERGE alone is not a universal concurrent-uniqueness guarantee. Use the appropriate constraint for identity and consider transaction/concurrency requirements. This simple sequential example does not benchmark races or implement an enterprise transaction workflow.</p>''','ns4_merge',programs=['ns4p07','ns4p11','ns4p16']),
 T('3.5 SET, REMOVE, DELETE and destructive scope','''
@@update@@
<p>SET updates properties or adds a label. REMOVE can remove a property or a label while preserving the node. An absent city reads as null; the other age/name properties remain. SET n = map replaces all properties; SET n += map changes the supplied properties. Labels are not property-map entries.</p>
<p>Unlike Cassandra’s ordinary UPDATE, MATCH plus SET for absent P99 creates nothing. Six people remain in the fixture. Select the intended graph entities first and inspect the match before changing or deleting them.</p>
@@delete@@
<p>A connected node cannot be deleted by ordinary DELETE while leaving incident relationships behind: program 9 receives a genuine ConstraintValidationFailed rejection. DELETE r removes the selected relationship but retains its endpoints. DETACH DELETE removes the selected node <b>and all its incident relationships</b>; other endpoints remain unless separately selected.</p>
<p>Never copy a whole-database delete into a shared/production graph. The provided complete files claim and clean only an isolated owned scope. Deleting visible graph records does not imply immediate physical byte erasure, undo availability or removal of all schema objects.</p>''','ns4_delete',programs=['ns4p08','ns4p09']),
]),
S('4. Nulls, Identity, Safe Input and Fixture Import',[
 T('4.1 OPTIONAL MATCH: preserve unmatched entities deliberately','''
@@optional@@
<p>After MATCH identifies each person, OPTIONAL MATCH tries the outgoing MENTORS pattern. If that whole optional pattern cannot be matched, the optional variable is null rather than removing the existing person row.</p>
<p>Only Asha has a stored outgoing mentor relationship, to Ravi. The fixture therefore returns <b>P01 → Ravi</b> and <b>P02–P06 → null</b>. There are <b>six rows</b> but <b>one non-null mentee</b>: count(*) and count(mentee) answer different questions.</p>
<p>WHERE attached to an OPTIONAL MATCH is part of that optional pattern’s matching conditions. By contrast, a later WITH p,mentee WHERE mentee IS NOT NULL intentionally removes the unmatched rows. The demonstrated later filter leaves Asha/Ravi only.</p>
<p>Use IS NULL/IS NOT NULL for null tests rather than treating null like an ordinary equality value. Optional patterns are useful for profiles with missing relationships, but are not automatic proof that a missing connection means a negative real-world fact.</p>''','ns4_optional',programs=['ns4p10']),
 T('4.2 Business identity, scoped uniqueness and statement rollback','''
@@constraint@@
<p>A Person label does not automatically make name or person_id unique. A uniqueness constraint on the chosen property/label can prevent conflicting IDs and has an index-backed implementation. The reference business constraint is scoped to its own disposable label rather than changing every Person in a shared database.</p>
<p>Program 11 observes the constraint and its <b>ONLINE</b> backing index. One write statement creates transient P98 then attempts duplicate P01; the server rejects the duplicate and <b>P98 is absent afterward</b>. That is evidence of rollback of that single implicit transaction. A later independent statement still works.</p>
<p>Uniqueness alone permits a node without person_id; the example creates “No ID” and reads null for the absent property. Required-property, key and type constraints have edition/version boundaries; the basic Community uniqueness example does not claim to implement Enterprise-only policies.</p>
<p>The runner uses one separate newly created named <b>ownership constraint</b> as an atomic namespace claim, then a marker node. A pre-existing name/scope is refused. Cleanup ownership begins only after CREATE succeeds; IF NOT EXISTS is not used to pretend an existing constraint belongs to this run. Only captured owned nodes/schema are removed. This is a guard for trusted prepared files, not a sandbox/parser for arbitrary untrusted Cypher.</p>
<p>Each runner statement is an auto-commit transaction. The entire multi-statement program is <b>not</b> one atomic transaction; a later failure does not magically undo earlier commits. Owned finally cleanup is a lab safeguard, not an application transaction or backup strategy.</p>''','ns4_identity',programs=['ns4p11']),
 T('4.3 Parameters and actual JSON-to-graph fixture import','''
@@params@@
<p>Keep query structure fixed and send values separately. Program 12 really supplies the name parameter to the official driver: Asha matches, while the quote/operator-shaped text <b>Asha' OR true //</b> is only a literal unmatched name. Do not build a WHERE clause by concatenating untrusted input.</p>
<p>Client commands such as :param are not native server Cypher. The downloadable runner’s // @params and // @params_file lines are ordinary comments interpreted by that runner. A manual client user must set parameters using the client’s facility. Dynamic labels/types have version-specific syntax; do not assume a value placeholder can replace arbitrary Cypher clauses.</p>
@@unwind@@
<p>Program 15 reads the actual bundled <b>graph_fixture.json</b>, supplies its arrays as parameters and uses UNWIND to create <b>six people and six KNOWS relationships</b>. A second read verifies every person ID/name/city/age and every source/target/since triple against the input. There is no hidden duplicate seed. The file also contains separate movie/banking data, but this import program intentionally imports only the social arrays.</p>
<p>UNWIND turns list elements into rows; it does not promise an input-result ordering without ORDER BY. Data maps can be expanded into primitive properties with SET p=row; they cannot be stored as nested map properties. This is a synthetic snapshot, not LOAD CSV, live hardware, an ETL benchmark or a trained AI pipeline.</p>
<p>Parameterization does not replace authentication, authorization, input validation or privacy policies. Use only the authorized disposable graph; never put real bank/account/profile records into a public learning submission.</p>''','ns4_import',programs=['ns4p12','ns4p15']),
]),
S('5. Relationship-Based Application Examples',[
 T('5.1 Friend candidates: a bounded pattern with explicit exclusions','''
<p>The shared synthetic social fixture has six people and six stored KNOWS links. For Asha/P01, the direct connections are Ravi/P02 and Neha/P03. Ravi connects to Meera/P04 and Imran/P05; Neha also connects to Meera. Meera connects onward to Dev/P06.</p>
@@friend@@
<p>The basic two-hop pattern gives <b>Meera/P04</b> and <b>Imran/P05</b>. Excluding the starting person and direct connections prevents unsuitable trivial suggestions. DISTINCT prevents Meera being returned twice through Ravi and Neha. Dev is three hops from Asha on these links, so this two-hop question does not return him.</p>
<p>This implements a <b>basic Cypher candidate query</b> required by Practical 8, not a graph-algorithm implementation, a trained recommendation model or a measured ranking system. Common-neighbour/similarity ideas are discussed conceptually; no similarity score, PageRank, custom BFS or GDS algorithm is implemented.</p>
<p>Real suggestions require consent, blocks, eligibility, deduplication, freshness, abuse controls and relevance evaluation. A relationship path is a traceable reason for a candidate, not proof that a connection should be recommended to a user.</p>''','ns4_social',programs=['ns4p13']),
 T('5.2 Movie candidates and the LinkedIn/Netflix workload analogies','''
<p>Asha likes Graph Journeys/M01. Ravi likes M01 and Database Stories/M02; Neha likes Space Signals/M03. Asha’s known people therefore supply M02 and M03 as unseen candidate titles.</p>
@@movie@@
<p>The returned titles are <b>Database Stories</b> and <b>Space Signals</b>. The NOT pattern excludes M01 because Asha already likes it; DISTINCT removes duplicate candidate paths. The query does not establish a user’s full watch history, personal consent or a relevance score.</p>
<p>The GTU syllabus names <b>LinkedIn, Netflix and banking</b> as AI-use-case contexts. Here, <b>LinkedIn-like</b> means professional connection/skill relationship questions, and <b>Netflix-like</b> means user-to-content preference/candidate questions. These are <b>workload analogies, not verified claims that those companies use Neo4j</b>, and no company dataset or deployment is reproduced.</p>
<p>A graph can support feature/context retrieval for an AI application, but a full recommender additionally needs eligibility rules, training or ranking if used, evaluation, monitoring and responsible data handling. This small example has no trained model, claimed accuracy uplift or throughput/latency result.</p>''','ns4_movies',programs=['ns4p13']),
 T('5.3 Shared-device banking patterns: investigation signals, not verdicts','''
@@bank@@
<p>The synthetic fixture has four accounts and two devices. D01 is used by A01, A02 and A04; D02 is used only by A03. The query returns exactly <b>(A01,A02), (A01,A04), (A02,A04)</b> on D01. It does not return A03 or self-pairs.</p>
<p>The condition a.account_id &lt; b.account_id selects one canonical orientation and excludes self/symmetric duplicates. Three account pairs do not mean three independent fraud incidents. The observed relationship means only “uses the same modeled device.”</p>
<p>Shared family devices, public computers, test accounts, data errors and device reassignment can all create legitimate overlaps. A result is a <b>review candidate, not a fraud verdict or accusation</b>. Add authorized context, time windows, provenance, consent/retention rules, analyst review and fairness/false-positive evaluation before any real decision.</p>
<p>Fraud-ring/community/anomaly techniques are conceptual application examples only. This unit does not implement ring detection, graph analytics, a classifier, identity surveillance or real financial transaction processing. All account/device records are synthetic.</p>''','ns4_fraud',programs=['ns4p14']),
]),
S('6. Algorithm Awareness, Troubleshooting and the Journal',[
 T('6.1 Graph-algorithm families and AI: examples only, no implementation','''
<p>The syllabus asks for graph-algorithm <b>examples, not implementations</b>. Recognize the kinds of relationship question an algorithm family can support; no mathematical proof, pseudocode or GDS installation/call is required here.</p>'''+table(['Family/example','Possible application question — conceptual only'],[
 ('Similarity / common-neighbour intuition','Which users/items have related connection patterns?'),
 ('Centrality / ranking intuition','Which entities occupy influential positions in this chosen graph?'),
 ('Community detection','Which densely connected groups might merit exploration?'),
 ('Path finding','What connection route links two entities under stated rules?'),
 ('Link-prediction intuition','Which missing relationship might be plausible, subject to evaluation?')])+'''
<p>Centrality is not human worth or trust; a community is not automatically a fraud ring; a short path is not causation. Graph Data Science is a separate optional library/service, not something automatically executed by a MATCH query. The reference does not install GDS or run its algorithms.</p>
<p>The executed friend/movie/shared-device queries are <b>basic pattern demonstrations</b> for Practical 8. They are not implementations of the algorithm families above and do not train AI. A knowledge graph can organize entities/relationships for search or model context, but it does not automatically make an AI answer true, current, unbiased or authorized.</p>
<p>Bound traversal depth, choose selective starting points, handle high-degree nodes and compare actual plans/measurements when optimization is needed. This unit observes an index state and tiny result sets, not distributed scaling, cluster failover, model accuracy, causal inference or real-time performance guarantees.</p>''','ns4_ai'),
 T('6.2 Troubleshooting, practical journal and primary references','''
<p><b>Cannot connect:</b> distinguish a stopped instance/wrong port from bad credentials, required password change, wrong database or a TLS/certificate mismatch. A URI for your local computer cannot magically reach a private remote workspace. Check the selected deployment’s actual settings; do not disable authentication or certificate validation as a shortcut.</p>
<p><b>Unexpected empty result:</b> check labels/types, property spelling, ID types, arrow direction, WHERE conditions and whether the seed was actually created. An undefined variable/bad pattern is a syntax rejection, whereas a valid absent match is empty. An absent property can read as null.</p>
<p><b>Unexpected duplicate candidate:</b> inspect path multiplicity and use DISTINCT only if the desired unit is an entity. <b>MERGE duplication:</b> inspect the complete identity pattern and constraints. <b>DELETE rejection:</b> inspect incident relationships and destructive scope before selecting DETACH. <b>Map-property error:</b> expand valid primitive properties or model related entities.</p>
<p><b>Journal for Practicals 7–8:</b> aim/CO4, actual Desktop/Aura setup evidence, versions/edition/OS, password-free URI/database, Browser graph/table observations, entity/relationship/property design, input/parameters, exact Cypher, actual positive and deliberate-negative results, candidate exclusions, full import verification, false-positive/AI limits, owned cleanup and conclusion. Do not relabel guided steps as completed GUI actions, edit output to imitate success or assign invented official theory marks.</p>
<p><b>Reproduce the reference:</b> use the guarded practical ZIP and your own private compatible instance. Complete files contain an administrative claim header and cleanup footer; prefer the runner, which stops on unexpected setup errors. A manual client that continues after a failed claim could later run a destructive footer, so inspect a fresh disposable scope and stop on unexpected errors. Interrupted/ambiguous runs need investigation, not a bulk deletion of every matching label.</p>
<p><b>Primary sources checked 29 October 2026:</b></p><ul>'''+''.join('<li><a href="'+url+'">'+title+'</a></li>' for title,url in SOURCES)+'''</ul>
<p>The unit contains no official theory-question-paper tab. The final Notes section provides answered practical revision tasks; Redis is covered separately in Unit 5; this unit focuses on Neo4j.</p>''',programs=['ns4p15','ns4p16']),
]),
]
assert sum(len(section['items']) for section in NOTES)==20
