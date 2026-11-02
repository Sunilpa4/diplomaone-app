"""Validate the Chemical subjects imported from the uploaded publisher."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJECTS = {
    'DI01005011': (1, 3), 'DI01005021': (1, 7),
    'DI02005021': (2, 6), 'DI02005011': (2, 5),
    'DI03005041': (3, 6), 'DI03005031': (3, 7),
    'DI03005021': (3, 7), 'DI03005061': (3, 5),
    'DI03005011': (3, 6), 'DI04005011': (4, 6),
    'DI04005021': (4, 6), 'DI05005051': (5, 6),
}


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def main():
    import export_app_content as exporter

    total = 0
    for code, (semester, count) in SUBJECTS.items():
        folder = ROOT / 'content' / 'chemical' / f'sem{semester}' / code
        subject = read(folder / 'subject.json')
        if (subject.get('code'), subject.get('branch'), subject.get('semester')) != (code, 'chemical', semester):
            raise ValueError(f'{code}: invalid subject identity')
        if code not in exporter.SUBJECTS or code not in exporter.BRANCH_SEMS.get('chemical', {}).get(semester, []):
            raise ValueError(f'{code}: missing catalog registration')
        units = {unit['no']: unit for unit in subject['units']}
        for number in range(1, count + 1):
            if number not in units:
                raise ValueError(f'{code}: unit {number} missing from subject')
            unit = read(folder / (units[number].get('file') or f'unit{number}.json'))
            if unit.get('subject') != code or unit.get('unit') != number:
                raise ValueError(f'{code}: invalid unit {number} identity')
            for diagram in unit.get('diagrams', []):
                if not (folder / 'diagrams' / (diagram['id'] + '.svg')).is_file():
                    raise ValueError(f'{code} unit {number}: missing diagram {diagram["id"]}')
            total += 1
    print(f'Chemical catalog validated: {len(SUBJECTS)} subjects, {total} units.')


if __name__ == '__main__':
    main()
