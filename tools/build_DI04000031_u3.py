"""Build Cassandra Unit 3 with real executed CQL and full CSV verification."""
import copy
import hashlib
import json
from pathlib import Path
import sys

from subject_DI04000031 import SUBJECT, ROOT, DIAG_DIR, check_and_write
from content_DI04000031_u3_notes import NOTES, SOURCES
from content_DI04000031_u3_extras import SYNTAX, VIVA, PRACTICE_QS
from content_DI04000031_u3_programs import PROGRAMS
from content_DI04000031_u3_shared import CSV, expected_readings
from diagrams_DI04000031_u3 import TITLES, main as draw_diagrams
from cassandra_content import assert_runtime, scratch_keyspaces, nodetool_status
from nosql_content import tr
from preview_builder import build_preview


def main():
    runtime = assert_runtime(); nodetool_status()
    assert scratch_keyspaces() == [], 'Inspect prior scratch keyspaces; never bulk-drop them'
    imported = next(p['out'] for p in PROGRAMS if p['id'] == 'ns3p12')
    rows = json.loads(next(line.removeprefix('imported_rows: ') for line in imported.splitlines()
                           if line.startswith('imported_rows: ')))
    as_key = lambda row: tuple(row[k] for k in ('device_id', 'day', 'reading_at', 'temperature_c', 'status'))
    assert sorted(map(as_key, rows)) == sorted(map(as_key, expected_readings())), 'CSV stored key/value/time mismatch'
    assert len(rows) == 8
    partitions = {(r['device_id'], r['day']) for r in rows}; assert len(partitions) == 4
    draw_diagrams()
    unit = {
        'subject': 'DI04000031', 'unit': 3, 'format': 'notes',
        'title': tr('Wide-Column Databases: Cassandra'), 'hours': 12, 'weightage': 20,
        'tabs': ['notes', 'programs', 'diagrams', 'syntax', 'viva'],
        'intro_text': tr('Cassandra architecture/setup and cqlsh, keyspaces/tables/partitions, partition and clustering keys, typed CQL DDL/CRUD and WHERE/ORDER BY/LIMIT. Includes 14 real CQL programs and a verified synthetic CSV dataset for Practicals 4–6. nodetool/cluster health remains awareness only; the reference uses one physical node.'),
        'notes': copy.deepcopy(NOTES) + [{
            'title': tr('Answered Practical Revision Tasks — Not a Theory Question Paper'),
            'role': 'practice',
            'items': [{'h': q['q'], 'body': q['a']} for q in PRACTICE_QS],
        }],
        'programs': PROGRAMS, 'diagrams': list(TITLES), '_diagram_titles': TITLES,
        'syntax': SYNTAX, 'viva': VIVA, 'exam_questions': [],
        'lesson_count': 18, 'practice_task_count': 16,
        'learning_outcomes': [tr('Design and implement distributed datasets using Cassandra’s data model and CQL (CO3).')],
        'practical_numbers': [4, 5, 6], 'content_kind': 'real_cassandra_practical',
        'assessment_note': tr('Practical PA 20 + practical ESE 30 = 50; theory ESE/PA are 0. Tasks carry no invented official theory-paper marks.'),
        'runtime_evidence': {
            'server': 'Apache Cassandra', 'server_version': runtime['server'],
            'shell': 'cqlsh', 'shell_version': runtime['cqlsh'], 'cql_version': runtime['cql'],
            'driver_version': runtime['driver'], 'native_protocol': runtime['protocol'],
            'java': runtime['java'], 'python': sys.version.split()[0], 'os': 'Debian 13 x86_64',
            'authenticated': runtime['authenticated'], 'factory_login_disabled': runtime['factory_login_disabled'],
            'physical_nodes': runtime['physical_nodes'], 'data_center': runtime['data_center'],
            'partitioner': runtime['partitioner'], 'lab_replication_factor': 1,
            'public_database_endpoint': False, 'multi_node_distribution_tested': False,
            'failover_tested': False, 'cluster_operations_performed': False,
            'nodetool_observation': runtime['nodetool_status'], 'programs_executed': len(PROGRAMS),
            'output_origin': 'Real Cassandra native-protocol results via bundled driver; COPY FROM delegated to actual cqlsh; JSON preserves result order; dynamic COPY timing/rates omitted',
            'fixture': {'file': 'sensors.csv', 'synthetic': True, 'live_ingestion': False,
                        'sha256': hashlib.sha256(CSV.encode()).hexdigest(),
                        'source_rows': len(expected_readings()), 'stored_rows': len(rows),
                        'logical_partitions': len(partitions), 'actual_cqlsh_copy': True,
                        'all_keys_values_times_match': True},
        },
        'sources': [{'title': title, 'url': url} for title, url in SOURCES],
    }
    path = check_and_write(unit)
    unit = json.loads(Path(path).read_text())
    preview = Path(ROOT, 'preview/DI04000031_unit3_preview.html')
    build_preview(unit, SUBJECT, DIAG_DIR, str(preview))
    from export_DI04000031_u3_practicals import export
    export()
    print('Cassandra Unit 3: 18 lessons / 14 real programs / 13 diagrams / 14 reference cards / 52 viva / 16 answered tasks')
    print('Real runtime:', json.dumps(unit['runtime_evidence']))
    print('Remaining owned-prefix keyspaces:', len(scratch_keyspaces()))
    print('Preview:', preview, preview.stat().st_size, 'bytes')


if __name__ == '__main__': main()
