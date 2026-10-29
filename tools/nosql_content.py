"""Language-neutral NoSQL teaching fixtures and English-only HTML helpers.

These are illustrative models for the Unit 1 comparison, NOT data exported
from running MongoDB, Redis, Cassandra or Neo4j servers. Tests validate the
fixtures and the reasoning. Real engine runners belong to later units.
"""
import html
import json
import re

DOCUMENTS = [
    {'_id': 'P101', 'name': 'Sensor Node', 'category': 'electronics',
     'attributes': {'sample_rate_hz': 10, 'battery_powered': True}},
    {'_id': 'P102', 'name': 'NoSQL Guide', 'category': 'book',
     'attributes': {'pages': 320, 'language': 'en'}},
]
CACHE = {'key': 'recs:U42:v1', 'value': ['P101', 'P102'], 'ttl_seconds': 300}
SENSOR_ROWS = [
    {'sensor_id': 'S01', 'day': '2026-10-29', 'ts': '09:00', 'reading_c': 30.5},
    {'sensor_id': 'S01', 'day': '2026-10-29', 'ts': '09:01', 'reading_c': 31.0},
    {'sensor_id': 'S02', 'day': '2026-10-29', 'ts': '09:00', 'reading_c': 29.0},
]
GRAPH_NODES = [
    {'id': 'U42', 'label': 'Person', 'name': 'Ravi'},
    {'id': 'U77', 'label': 'Person', 'name': 'Asha'},
    {'id': 'P101', 'label': 'Product', 'name': 'Sensor Node'},
    {'id': 'P102', 'label': 'Product', 'name': 'NoSQL Guide'},
]
GRAPH_EDGES = [('U42', 'LIKES', 'P101'), ('U77', 'LIKES', 'P101'), ('U77', 'LIKES', 'P102')]

MODELS = [
    {'type': 'Document', 'example': 'MongoDB',
     'shape': 'A document with fields, arrays and nested objects; grouped into collections',
     'access': 'Read a product/profile and query selected fields with suitable indexes',
     'advantage': 'Natural representation of varying, nested application records',
     'tradeoff': 'Plan validation, embedding size, duplicated fields and indexes',
     'application': 'Product catalogs, content and AI user profiles',
     'not_for': 'Assuming every relationship should be one giant embedded document'},
    {'type': 'Key-Value', 'example': 'Redis',
     'shape': 'A unique key maps to a value; Redis supports several value data structures',
     'access': 'Read/update a known key; use appropriate operations for its value type',
     'advantage': 'Simple low-latency access for known-key workloads; expiry is useful for caches',
     'tradeoff': 'Design keys, expiry, memory use, persistence and stale-cache handling',
     'application': 'Sessions, cached recommendations and online feature lookups',
     'not_for': 'Treating a cache as the only authoritative payment or stock record'},
    {'type': 'Wide-Column', 'example': 'Apache Cassandra',
     'shape': 'Typed tables organized into partitions and ordered rows within a partition',
     'access': 'Read one sensor/day partition and a timestamp range',
     'advantage': 'Scalable distributed writes and predictable partition-oriented queries',
     'tradeoff': 'Query-first tables, good partition sizes, duplication and limited ad-hoc joins',
     'application': 'IoT events, telemetry and AI feature-history data',
     'not_for': 'Confusing a wide-column store with a columnar analytical warehouse'},
    {'type': 'Graph', 'example': 'Neo4j',
     'shape': 'Nodes and directed typed relationships, both with properties',
     'access': 'Follow relationship paths such as people sharing a device',
     'advantage': 'Expresses connected-data and multi-hop traversal questions naturally',
     'tradeoff': 'Model meaningful relationships, index entry points and bound traversals',
     'application': 'Fraud-pattern exploration, recommendations and knowledge graphs',
     'not_for': 'Assuming a graph diagram or a database alone is a trained AI system'},
]

CASES = [
    {'id': 'S1', 'scenario': 'A shop adds books and electronics with different nested attributes.',
     'access': 'Read one product and filter selected attributes.', 'choice': 'Document',
     'reason': 'Different product fields fit documents while keeping one product together.',
     'tradeoff': 'Validate common fields and index real filters; avoid unbounded embedded reviews.'},
    {'id': 'S2', 'scenario': 'An app serves cached recommendation IDs for a known user and model version.',
     'access': 'Look up recs:U42:v1; refresh after a short lifetime.', 'choice': 'Key-Value',
     'reason': 'The key is known and temporary stale recommendations are acceptable by policy.',
     'tradeoff': 'Use a TTL, version keys and a cache-miss fallback; do not cache authorization blindly.'},
    {'id': 'S3', 'scenario': 'A large fleet writes sensor readings; reads ask for one sensor on one day.',
     'access': 'Partition by sensor/day and read a bounded timestamp interval.', 'choice': 'Wide-Column',
     'reason': 'A query-first, time-bucketed partition model fits high-volume event history.',
     'tradeoff': 'Check partition growth and hot sensors; add another query table only when justified.'},
    {'id': 'S4', 'scenario': 'An investigator follows account-to-device-to-account connections.',
     'access': 'Traverse several relationships to find shared devices.', 'choice': 'Graph',
     'reason': 'Relationships and paths are the main query, not just independent records.',
     'tradeoff': 'A shared device is evidence for investigation, not proof of fraud; control access.'},
    {'id': 'S5', 'scenario': 'A bank needs atomic transfers, constraints and auditable relational reports.',
     'access': 'Update two balances together and report linked ledger entries.', 'choice': 'Relational',
     'reason': 'An RDBMS is a strong default for relational constraints and multi-row transactions.',
     'tradeoff': 'This does not mean all NoSQL products lack transactions; evaluate actual guarantees.'},
    {'id': 'S6', 'scenario': 'A small college attendance app has stable tables and routine SQL reports.',
     'access': 'Join students, classes and attendance records.', 'choice': 'Relational',
     'reason': 'The current relational workload does not justify additional distributed-store complexity.',
     'tradeoff': 'Measure future pressures before replacing a working design.'},
    {'id': 'S7', 'scenario': 'An AI learning app stores evolving profiles with nested skills and preferences.',
     'access': 'Fetch or update a learner profile and selected preference fields.', 'choice': 'Document',
     'reason': 'A bounded nested profile maps naturally to a document.',
     'tradeoff': 'Enforce validation, consent and retention; separate ever-growing interaction logs.'},
    {'id': 'S8', 'scenario': 'A social app asks for friends-of-friends while excluding existing friends.',
     'access': 'Traverse a bounded two-hop connection pattern.', 'choice': 'Graph',
     'reason': 'The shape of the connection path determines the answer.',
     'tradeoff': 'Bound traversal depth and handle high-degree nodes; do not promise universal speedups.'},
]

CAP_CASES = [
    {'case': 'Link healthy', 'action': 'Coordinate writes and reads normally.',
     'result': 'Consistency and availability can both be provided; CAP is not a normal-operation choose-two rule.'},
    {'case': 'Partition: protect one confirmed seat',
     'action': 'Only the authorized side may confirm; isolated offices defer requests they cannot safely serve.',
     'result': 'Protects a single booking history but sacrifices availability for some requests.'},
    {'case': 'Partition: keep a recommendation cache serving',
     'action': 'Each side may answer from local data, accepting that it may be stale.',
     'result': 'Keeps reads available but cannot promise one latest value during the partition.'},
    {'case': 'Network heals after independent writes',
     'action': 'Exchange changes and apply a declared reconciliation/conflict policy.',
     'result': 'Convergence is not automatic evidence that all earlier responses were strongly consistent.'},
]

SOURCES = [
    ('GTU DI04000031 official syllabus (2025-26)', 'https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf'),
    ('Gilbert and Lynch: Brewer\'s Conjecture (CAP definitions)', 'https://users.ece.cmu.edu/~adrian/731-sp04/readings/GL-cap.pdf'),
    ('MongoDB: Data Modeling', 'https://www.mongodb.com/docs/manual/data-modeling/'),
    ('Apache Cassandra: Introduction to Data Modeling', 'https://cassandra.apache.org/doc/latest/cassandra/developing/data-modeling/intro.html'),
    ('Neo4j: Graph Database Concepts', 'https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/'),
    ('Redis: Data Types', 'https://redis.io/docs/latest/develop/data-types/'),
]


def tr(s):
    return {'en': s}


def code(text):
    return '<pre class="c">' + html.escape(text.strip('\n'), quote=False) + '</pre>'


def make_T(snips):
    def T(h, body, diagram=None, key=False, programs=None):
        body = re.sub(r'@@(\w+)@@', lambda m: code(snips[m.group(1)]), body)
        item = {'h': tr(h), 'body': tr(body)}
        if diagram: item['diagram'] = diagram
        if key: item['key'] = True
        if programs: item['programs'] = list(programs)
        return item
    return T


def table(headers, rows):
    def cell(x): return html.escape(str(x), quote=False)
    return ('<table><tr>' + ''.join('<th>' + cell(x) + '</th>' for x in headers) + '</tr>'
            + ''.join('<tr>' + ''.join('<td>' + cell(x) + '</td>' for x in row) + '</tr>' for row in rows)
            + '</table>')


def json_text(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


def V(q, a): return {'q': tr(q), 'a': tr(a)}

def SX(name, f, terms): return {'name': tr(name), 'f': f.strip(), 'terms': tr(terms)}

def Q(kind, q, a): return {'type': kind, 'q': tr(q), 'a': tr(a)}
