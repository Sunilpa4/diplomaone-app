"""Deterministic export of built Neo4j sources/results, no running DB needed."""
import json
from pathlib import Path
import zipfile
from content_DI04000031_u4_shared import FIXTURE_JSON

ROOT=Path(__file__).resolve().parent.parent
UNIT=ROOT/'content/computer/sem4/DI04000031/unit4.json'
OUT=ROOT/'preview/DI04000031_unit4_practicals.zip'
REQUIREMENTS='neo4j==5.28.8\n'
README='''# DI04000031 · Unit 4 · Graph Databases: Neo4j

English-only GTU Computer/CSE Semester 4, effective 2025–26.
12 hours / 20% CONTENT weightage; CO4: utilize Neo4j to solve
relationship-based problems with graph queries. Practicals 7–8.
Course assessment: practical PA 20 + ESE 30 = 50, theory ESE/PA 0.
No official theory-paper questions/marks or graph-algorithm implementations.

## Bundle (37 files)

- examples/ns4p01.cypher ... ns4p16.cypher — complete independent scripts
- expected/ns4p01.txt ... ns4p16.txt — actual reference server outputs
- run_lab.py — credential-free guarded real-driver runner
- graph_fixture.json — synthetic people/relationships/movies/accounts/devices
- requirements.txt — official Python Neo4j driver 5.28.8
- runtime.json — non-secret observed runtime/scope/verification metadata
- README.md — this guide

The server/Java binaries, database files and passwords are NOT bundled.
The archive is exported from already built real results without importing
or reconnecting to the database program module.

## What was actually executed

Private Neo4j COMMUNITY 5.26.32, matching Cypher Shell 5.26.32,
official Python driver 5.28.8, Temurin Java 21.0.13+9, Python 3.13.16,
Debian 13 x86_64; one physical instance, Bolt protocol 5.8.

All sixteen exact scripts were sent to the real authenticated server
through the official driver. Result rows/summary counters are actual;
JSON preserves returned order and temporal display is normalized to ISO UTC.
Non-error notifications, changing internal IDs and timing are not published
as stable output. No fake engine/result generator is used.

Matching Cypher Shell independently connected and queried the actual server;
the validation also runs full positive scripts with it. This is not a claim
that a shell interprets the runner’s comment annotations.

The server binary and Java archive were checked against official published
SHA-256 digests; the private setup source has the pinned values. Checksum
verification is not a claim of separate signature verification.

The initial password was set privately BEFORE first launch. Anonymous and
old-default-password connections were actually denied. Server usage reporting
and driver telemetry are disabled. CQL from Cassandra is not Cypher.

The loopback reference used Bolt 7688 and HTTP 7475; usual local defaults
are Bolt 7687 and Browser HTTP 7474. There is NO public database endpoint.
Unencrypted local Bolt here is not production TLS/security hardening.
Small memory settings are a constrained lab, not a production sizing recipe.

## Practical 7: Desktop/Aura and Browser — guided, not fabricated evidence

The official practical asks for Desktop OR Aura setup and Browser exploration.
The reference is a headless Community Server, NOT an installed Desktop,
provisioned Aura instance or an automated Browser GUI demonstration.
Do not submit its CLI/server output as proof that you performed those GUI steps.

Desktop: check current supported OS/security notices and license conditions,
install from the official deployment center, create/start a compatible learning
instance, set private credentials and open Browser/Query. Desktop’s included
developer-license edition is not identical to Community Server or an
unrestricted production license.

Aura: use your own authorized account, choose an appropriate AuraDB learning
tier, check current costs/limits BEFORE creating resources, save credentials
privately and use the service-provided encrypted URI. This kit does not create
cloud accounts, paid resources or graph-analytics services.

Browser: connect to YOUR actual instance/database. A usual local address is
http://localhost:7474/browser and bolt://localhost:7687; localhost means YOUR
computer, not the hosted notes app or a remote workspace. Return graph entities
(nodes/relationships) for a graph view and scalar properties for a table view.
Inspect labels, arrows, properties and the relationship type in your interface.

Official procedures:
https://neo4j.com/docs/desktop/current/installation/
https://neo4j.com/docs/aura/getting-started/create-instance/
https://neo4j.com/docs/browser/operations/dbms-connection/
https://neo4j.com/docs/operations-manual/5/installation/requirements/
https://neo4j.com/docs/operations-manual/5/installation/linux/tarball/

The exact database reference is the 5.26 LTS branch. Newer calendar-version
releases coexist and may have different default Cypher versions/UI details.
Match your server/language/version documentation rather than assuming all
products/version numbers are interchangeable. Versioned requirements support
Java 17/21 for 5.26; this reference uses Java 21. Tested Debian 13 is an
observation, not vendor certification for a platform absent from that matrix.
GTU recommends an 8 GB learning computer.

## Run against your own PRIVATE disposable learning instance

Install compatible Python and the official driver:

    python3 -m pip install -r requirements.txt

Then, from this extracted bundle’s root:

    python3 run_lab.py examples/ns4p13.cypher

Defaults: bolt://127.0.0.1:7687, database neo4j, username neo4j. A hidden
password prompt is used. For the unusual reference port or another authorized
instance, set NEO4J_URI or pass --uri. NEO4J_USERNAME/NEO4J_DATABASE are optional;
a private environment manager may supply NEO4J_PASSWORD. Never commit it.
For Aura, use its provided TLS URI (usually neo4j+s://...), not a plaintext
replacement or a certificate-verification bypass. Follow your deployment’s
security requirements; these examples are NOT a production authorization setup.
Unix shell examples need equivalent environment syntax on Windows.

For the JSON example:

    python3 run_lab.py examples/ns4p15.cypher --fixtures .

Program 15 really reads graph_fixture.json and passes arrays as parameters.
It imports ONLY people/friendships: 6 people and 6 directed KNOWS edges.
The movie and banking sections are used in separate example seeds, not hidden
extra rows in that import. Verify every stored ID/property/edge/year.

## Namespace ownership and cleanup — read before running

Community reference scripts share the neo4j database; they do NOT create
sixteen databases. Each file has its own NS4_ns4pXX scope label and explicit
fresh `di04000031_u4_ns4pXX_owner` uniqueness constraint as an ATOMIC CLAIM.
The claim property is separate from the business person_id policy.

The runner refuses existing scope nodes OR scope-named constraints, creates
the new claim without IF NOT EXISTS and marks ownership ONLY after actual
CREATE success. A competing/pre-existing failed claim is not owned. A unique
constraint name provides an atomic server-side claim, unlike a plain node
creation which would permit duplicate markers in a race.

All example nodes carry the captured scope label. Cleanup deletes only that
newly owned scope and drops only successfully created captured constraints;
the claim is released last. It never recreates/drops the database. The account
needs permission for this private lab schema work; this is not a production
application-role recommendation or general untrusted-Cypher security sandbox.

Do NOT manually feed an entire file into an existing graph and continue after
a failed setup claim. A client that continues can later execute the destructive
footer. Prefer run_lab.py; stop on unexpected setup errors. After interrupted
or ambiguous network failures, investigate ownership/remaining artifacts rather
than bulk-deleting every similar label/schema. A prefix is not authorization,
a backup or proof of ownership by itself.

## Transactions, annotations and actual errors

Each statement is its own implicit AUTO-COMMIT transaction. A failure rolls
back that statement; the whole file is NOT one atomic transaction. Finally
cleanup is a lab safeguard, not an application transaction or undo service.
Program 11 actually creates P98 then attempts conflicting P01 IN ONE statement;
the rejection leaves P98 count 0. Earlier separate commits are not undone.

The following are ordinary Cypher comments, interpreted by this runner:

- // @result label — name the following returned values/counters
- // @expect Neo.ClientError... — require the actual server failure code
- // @params {...} — supply next-statement driver parameters separately
- // @params_file graph_fixture.json — load next-statement input arrays
- // @stats — publish actual summary counters for that statement

A bare Browser/Cypher Shell user must set parameters with the CLIENT parameter
facility, such as :param name => 'Asha'. An annotation is not server Cypher.
Several files intentionally contain rejected statements: that is not a failed
lab setup, fake output or permission to ignore unexpected errors.

Actual rejections include Neo.ClientError.Schema.ConstraintValidationFailed
(connected DELETE/duplicate ID), Statement.TypeError (nested property map),
Statement.SyntaxError (unbound variable/bad pattern), Statement.SemanticError
(null MERGE identity). Complete codes are captured, not invented numeric IDs.
Other versions can differ: investigate rather than editing expected files to
fake agreement. The runner does not log real credentials.

## Program map

01 actual server/edition, committed probe and stored read-back/counters
02 multiple labels and primitive/list/date/datetime property values
03 directed KNOWS relationship with since property
04 MATCH/WHERE/RETURN, AND/OR/IN and typed equality
05 outgoing/incoming/undirected reads without changing stored arrows
06 ORDER BY/LIMIT, DISTINCT and small grouped counts
07 complete-pattern MERGE, ON CREATE/ON MATCH, visits 1 -> 2
08 SET/REMOVE properties and labels; missing MATCH does NOT upsert
09 connected-node rejection, relationship-only delete and DETACH scopes
10 OPTIONAL MATCH, six rows versus one non-null mentee
11 scoped business uniqueness/ONLINE index and failed-statement rollback
12 official-driver parameters; selector-shaped text remains a literal value
13 two-hop connection and unseen-movie candidates using basic Cypher patterns
14 synthetic shared-device review pairs, NOT fraud verdicts
15 actual JSON/UNWIND import; every person and edge read back/verified
16 real type/syntax/null-MERGE rejections and unchanged valid people

## Exact synthetic observations and scope limits

People: P01 Asha/Surat/20; P02 Ravi/Bharuch/21; P03 Neha/Surat/19;
P04 Meera/Vadodara/22; P05 Imran/Surat/20; P06 Dev/Rajkot/23.
Stored KNOWS: P01->P02, P01->P03, P02->P04, P03->P04, P02->P05, P04->P06.
Two-hop candidates for Asha: Meera/P04 and Imran/P05 after exclusions/DISTINCT.
Dev is three hops away. Different paths to Meera are not two different people.

Asha likes M01 Graph Journeys; Ravi likes M01 and M02 Database Stories;
Neha likes M03 Space Signals. Unseen movies via known people: M02 and M03.
This is a transparent candidate query, not trained or ranked AI.

D01 is used by A01/A02/A04, yielding A01–A02, A01–A04, A02–A04.
D02 is used only by A03, yielding no shared pair. Family/public devices,
reassignment and data errors can create legitimate overlaps. Context, consent,
retention, false-positive evaluation and human review are essential.

Graph-algorithm families (similarity, centrality, communities, path finding,
link prediction) are CONCEPTUAL EXAMPLES ONLY: no proof, pseudocode/custom
implementation, GDS algorithm call, model training or performance guarantee.
Practical 8’s basic pattern queries are not implementations of those families.
LinkedIn-like/Netflix-like are syllabus workload analogies, NOT verified claims
about those companies’ actual Neo4j deployments. No real bank/profile records.

RETURN graph entities for Browser graph views; scalar returns are tables.
A label is not automatic uniqueness/existence; null is not a stored property.
MERGE matches a whole pattern and is not universal concurrent uniqueness.
An undirected read does not add edges. DETACH can remove ALL incident edges,
not just the one that motivated the selection; deletion is not immediate
physical erasure. ONLINE index state is not a latency benchmark.

Journal: actual setup/GUI evidence, versions/edition, model/identity rationale,
input/parameters, Cypher and observed outputs/errors, full import checks,
recommendation exclusions/fraud false positives, algorithm/AI limits,
owned cleanup, conclusion and official references. No theory-paper marks.
'''


def export(path=OUT):
    unit=json.loads(UNIT.read_text())
    files={'README.md':README,'run_lab.py':(ROOT/'tools/neo4j_lab_runner.py').read_text(),
           'requirements.txt':REQUIREMENTS,'graph_fixture.json':FIXTURE_JSON,
           'runtime.json':json.dumps(unit['runtime_evidence'],indent=2)+'\n'}
    for program in unit['programs']:
        files['examples/'+program['id']+'.cypher']=program['code']['en']+'\n'
        files['expected/'+program['id']+'.txt']=program['out']+'\n'
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as archive:
        for name,text in files.items():
            entry=zipfile.ZipInfo(name,(2026,10,29,0,0,0))
            entry.compress_type=zipfile.ZIP_DEFLATED;entry.external_attr=0o644<<16
            archive.writestr(entry,text.encode('utf-8'))
    assert len(files)==37
    print('Neo4j practical download:',path,path.stat().st_size,'bytes /',len(files),'files')
    return str(path)


if __name__=='__main__':export()
