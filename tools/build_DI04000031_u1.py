"""Build GTU NoSQL Unit 1: notes, SVGs, self-contained preview and worksheet.

This is the official introductory comparative practical, not a fake engine
execution. No database server is installed or invoked by this builder.
"""
import copy
import os

from subject_DI04000031 import SUBJECT, ROOT, DIAG_DIR, check_and_write
from content_DI04000031_u1_notes import NOTES
from content_DI04000031_u1_extras import SYNTAX, VIVA, PRACTICE_QS
from diagrams_DI04000031_u1 import TITLES, main as draw_diagrams
from nosql_content import tr, SOURCES
from preview_builder import build_preview

UNIT = {
    'subject': 'DI04000031', 'unit': 1, 'format': 'notes',
    'title': tr('Introduction to NoSQL'), 'hours': 8, 'weightage': 13,
    'intro_text': tr('Why NoSQL, CAP with a booking analogy, the four data models and AI use cases. Includes Practical 1 comparison, eight worked selection cases, 16 answered practice tasks and viva. Illustrations are not database-server output; no official theory-paper marks are assigned.'),
    'notes': copy.deepcopy(NOTES) + [{
        'title': tr('Practice Tasks with Answer Guides — Not an Official Theory Paper'),
        'role': 'practice',
        'items': [{'h': q['q'], 'body': q['a']} for q in PRACTICE_QS],
    }],
    'diagrams': list(TITLES), '_diagram_titles': TITLES,
    'syntax': SYNTAX, 'viva': VIVA, 'exam_questions': [],
    'learning_outcomes': [tr('Select and justify an appropriate NoSQL database type for an application (CO1).')],
    'practical_numbers': [1],
    'content_kind': 'conceptual_comparison',
    'lesson_count': 14, 'worked_selection_cases': 8, 'practice_task_count': 16,
    'assessment_note': tr('Practical-only assessment: PA 20 + ESE 30 = 50. No theory ESE/PA; practice tasks are not an official question paper.'),
    'sources': [{'title': name, 'url': url} for name, url in SOURCES],
}


def main():
    draw_diagrams()
    path = check_and_write(copy.deepcopy(UNIT))
    import json
    with open(path, encoding='utf-8') as f: unit = json.load(f)
    preview = os.path.join(ROOT, 'preview', 'DI04000031_unit1_preview.html')
    os.makedirs(os.path.dirname(preview), exist_ok=True)
    build_preview(unit, SUBJECT, DIAG_DIR, preview)
    from export_DI04000031_u1_worksheet import export
    export()
    print('Unit 1: 14 lessons / 8 solved selection cases / 16 answered practice tasks')
    print('Diagrams:', len(unit['diagrams']), '/ reference cards:', sum(len(g['items']) for g in SYNTAX),
          '/ viva:', sum(len(g['items']) for g in VIVA))
    print('Assessment: practical-only; no fabricated theory question marks.')
    print('Preview:', preview, os.path.getsize(preview), 'bytes')


if __name__ == '__main__': main()
