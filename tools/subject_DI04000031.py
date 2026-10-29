"""GTU DI04000031: English-only NoSQL metadata and content validation.

Unit 1 is a comparative study, not an engine-installation lab. Later units
may add programs; a neutral language avoids calling CQL/Cypher/Redis C code.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SUBJ_DIR = os.path.join(ROOT, 'content', 'computer', 'sem4', 'DI04000031')
DIAG_DIR = os.path.join(SUBJ_DIR, 'diagrams')
os.makedirs(DIAG_DIR, exist_ok=True)
# No theory-exam tab: this is a practical-only course. Answered practice
# tasks appear in Notes, beside the Practical 1 comparison worksheet.
TABS = ['notes', 'diagrams', 'syntax', 'viva']
INTRO = {'en': 'GTU-aligned concepts, data-model diagrams, worked database-selection cases, reference cards and practical viva. Unit 1 covers Practical 1: a comparative study; engine setup and executed queries begin in later units.'}
SUBJECT = {
    'code': 'DI04000031', 'name': {'en': 'Introduction to NoSQL'},
    'branch': 'computer', 'semester': 4, 'syllabus_year': '2025-26',
    'type': 'practical', 'languages': ['en'], 'code_lang': 'nosql',
    'syllabus_url': 'https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf',
    'teaching': {'lecture': 0, 'tutorial': 1, 'practical': 4},
    'exam': {'theory_ese': 0, 'theory_pa': 0, 'practical_pa': 20,
             'practical_ese': 30, 'total': 50, 'credits': 3},
    'units': [
        {'no': 1, 'title': {'en': 'Introduction to NoSQL'}, 'hours': 8, 'weightage': 13,
         'topics': ['1.1 Why NoSQL? RDBMS limitations and trade-offs for modern applications',
                    '1.2 CAP theorem: basic concepts with an analogy only',
                    '1.3 Overview of Document, Key-Value, Wide-Column and Graph databases',
                    '1.4 AI-focused use cases of NoSQL databases'], 'file': None},
        {'no': 2, 'title': {'en': 'Document Databases: MongoDB'}, 'hours': 18, 'weightage': 30,
         'topics': ['2.1 Documents, collections, BSON and MongoDB architecture',
                    '2.2 Installation, mongosh and basic operations',
                    '2.3 CRUD, data types, query operators, sorting and projection',
                    '2.4 Embedding and references; basic indexing and aggregation',
                    '2.5 Replication and sharding: conceptual overview only'], 'file': None},
        {'no': 3, 'title': {'en': 'Wide-Column Databases: Cassandra'}, 'hours': 12, 'weightage': 20,
         'topics': ['3.1 Cassandra installation and cqlsh',
                    '3.2 Keyspaces, tables, columns and partitions',
                    '3.3 Partition keys and clustering keys',
                    '3.4 CQL DDL, CRUD, filtering, ordering and limits',
                    '3.5 nodetool and cluster-health awareness only'], 'file': None},
        {'no': 4, 'title': {'en': 'Graph Databases: Neo4j'}, 'hours': 12, 'weightage': 20,
         'topics': ['4.1 Graph concepts: nodes, relationships, labels and properties',
                    '4.2 Neo4j installation and tools',
                    '4.3 Basic Cypher and graph queries',
                    '4.4 Recommendation and fraud examples: no graph-algorithm implementations',
                    '4.5 AI-focused graph scenarios'], 'file': None},
        {'no': 5, 'title': {'en': 'Key-Value Databases: Redis'}, 'hours': 10, 'weightage': 17,
         'topics': ['5.1 Redis installation and basic commands',
                    '5.2 Strings, lists, sets and hashes',
                    '5.3 Basic operations, transactions and caching',
                    '5.4 AI, real-world and application-integration examples'], 'file': None},
    ],
    'practicals': [
        'Study and compare Document, Key-Value, Wide-Column and Graph databases: characteristics, advantages and application areas',
        'Install MongoDB Community Edition and mongosh; verify versions and connectivity',
        'MongoDB CRUD with query filters, sorting, projection and logical operators',
        'Install Cassandra and connect with cqlsh; explore keyspaces, partition and clustering keys',
        'Cassandra data modeling and CRUD using WHERE, ORDER BY and LIMIT',
        'Use an AI-related dataset in Cassandra for distribution and simple analytical queries',
        'Install Neo4j and explore nodes, relationships and properties',
        'Basic Neo4j Cypher queries and recommendation or fraud examples',
        'Redis installation and basic Strings, Lists, Sets and Hashes operations',
    ],
    'books': [
        'Shannon Bradshaw, Eoin Brazil and Kristina Chodorow — MongoDB: The Definitive Guide',
        'Pramod J. Sadalage and Martin Fowler — NoSQL Distilled',
        'Jeff Carpenter and Eben Hewitt — Cassandra: The Definitive Guide',
        'Ian Robinson, Jim Webber and Emil Eifrem — Graph Databases',
        'Josiah L. Carlson — Redis in Action',
    ],
}


def write_subject():
    for unit in SUBJECT['units']:
        name = f"unit{unit['no']}.json"
        unit['file'] = name if os.path.isfile(os.path.join(SUBJ_DIR, name)) else None
    with open(os.path.join(SUBJ_DIR, 'subject.json'), 'w', encoding='utf-8') as f:
        json.dump(SUBJECT, f, ensure_ascii=False, indent=1)


def check_and_write(unit):
    import xml.etree.ElementTree as ET
    n = unit['unit']
    spec = SUBJECT['units'][n - 1]
    assert (unit['hours'], unit['weightage']) == (spec['hours'], spec['weightage'])
    assert unit['title'] == spec['title']
    unit.setdefault('tabs', TABS[:])
    unit.setdefault('intro_text', INTRO.copy())
    ds = unit.get('diagrams', [])
    if ds and isinstance(ds[0], str):
        titles = unit.pop('_diagram_titles')
        unit['diagrams'] = [{'id': id_, 'title': {'en': titles[id_]},
                            'file': f'diagrams/{id_}.svg'} for id_ in ds]
    diagram_ids = {d['id'] for d in unit.get('diagrams', [])}
    program_ids = {p['id'] for p in unit.get('programs', [])}
    assert len(diagram_ids) == len(unit.get('diagrams', [])), 'Duplicate diagram IDs'
    assert len(program_ids) == len(unit.get('programs', [])), 'Duplicate program IDs'
    used = set()
    for section in unit['notes']:
        for topic in section['items']:
            assert 'en' in topic['h'] and 'en' in topic['body']
            assert not re.search(r'@@\w+@@', topic['body']['en']), 'Unexpanded snippet'
            if topic.get('diagram'):
                assert topic['diagram'] in diagram_ids, topic['diagram']
                used.add(topic['diagram'])
            for id_ in topic.get('programs', []):
                assert id_ in program_ids, id_
    assert used == diagram_ids, f'Unused diagrams: {diagram_ids - used}'
    def english_only(obj):
        if isinstance(obj, dict):
            assert 'gu' not in obj, 'Unexpected Gujarati translation'
            for val in obj.values(): english_only(val)
        elif isinstance(obj, list):
            for val in obj: english_only(val)
        elif isinstance(obj, str):
            assert not re.search(r'[\u0a80-\u0aff]', obj), 'Non-English content'
    english_only(unit)
    for d in unit.get('diagrams', []):
        path = os.path.join(SUBJ_DIR, d['file'])
        root = ET.parse(path).getroot()
        assert root.tag.endswith('svg'), path
        raw = open(path, encoding='utf-8').read()
        assert all(x not in raw for x in ('<marker', '<foreignObject', '<script', '<image')), path
    path = os.path.join(SUBJ_DIR, f'unit{n}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    write_subject()
    return path
