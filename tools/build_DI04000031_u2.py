"""Build MongoDB Unit 2 using real server-executed programs, not simulations."""
import copy
import json
import os
from subject_DI04000031 import SUBJECT, ROOT, DIAG_DIR, check_and_write
from content_DI04000031_u2_notes import NOTES, SOURCES
from content_DI04000031_u2_extras import SYNTAX, VIVA, PRACTICE_QS
from content_DI04000031_u2_programs import PROGRAMS
from diagrams_DI04000031_u2 import TITLES, main as draw_diagrams
from mongodb_content import assert_runtime, scratch_databases
from nosql_content import tr
from preview_builder import build_preview


def main():
    runtime = assert_runtime()
    assert not scratch_databases(), 'Unclean prior scratch database(s); inspect before release'
    draw_diagrams()
    unit = {
        'subject': 'DI04000031', 'unit': 2, 'format': 'notes',
        'title': tr('Document Databases: MongoDB'), 'hours': 18, 'weightage': 30,
        'tabs': ['notes', 'programs', 'diagrams', 'syntax', 'viva'],
        'intro_text': tr('MongoDB architecture, installation/mongosh, BSON, CRUD and filters, sorting/projection, data modeling, indexes and basic aggregation. Includes 14 real server-executed programs and Practicals 2–3. Replication and sharding are conceptual only; practice tasks are not an official theory paper.'),
        'notes': copy.deepcopy(NOTES) + [{
            'title': tr('Answered Practice Tasks — Lab and Viva Preparation, Not a Theory Paper'),
            'role': 'practice',
            'items': [{'h': q['q'], 'body': q['a']} for q in PRACTICE_QS],
        }],
        'programs': PROGRAMS, 'diagrams': list(TITLES), '_diagram_titles': TITLES,
        'syntax': SYNTAX, 'viva': VIVA, 'exam_questions': [],
        'learning_outcomes': [tr('Apply MongoDB features for effective data modeling and management (CO2).')],
        'practical_numbers': [2, 3], 'content_kind': 'real_mongodb_practical',
        'lesson_count': 20, 'practice_task_count': 18,
        'runtime_evidence': {
            'server': 'MongoDB Community Server', 'server_version': runtime['server'],
            'shell': 'mongosh', 'shell_version': runtime['shell'],
            'os': 'Debian 13 x86_64', 'authenticated': runtime['authenticated'],
            'mode': 'standalone', 'public_database_endpoint': False,
            'replication_configured': False, 'sharding_configured': False,
            'programs_executed': len(PROGRAMS),
            'output_origin': 'Captured from exact displayed scripts on real mongod via mongosh',
        },
        'assessment_note': tr('Practical PA 20 + practical ESE 30 = 50; theory ESE/PA are 0. No per-question theory marks are assigned.'),
        'sources': [{'title': title, 'url': url} for title, url in SOURCES],
    }
    path = check_and_write(unit)
    unit = json.load(open(path, encoding='utf-8'))
    preview = os.path.join(ROOT, 'preview', 'DI04000031_unit2_preview.html')
    build_preview(unit, SUBJECT, DIAG_DIR, preview)
    from export_DI04000031_u2_practicals import export
    export()
    print('MongoDB Unit 2: 20 lessons / 14 real programs / 13 diagrams / 16 reference cards / 56 viva / 18 answered tasks')
    print('Real runtime:', json.dumps(unit['runtime_evidence']))
    print('Remaining scratch databases:', len(scratch_databases()))
    print('Preview:', preview, os.path.getsize(preview), 'bytes')


if __name__ == '__main__': main()
