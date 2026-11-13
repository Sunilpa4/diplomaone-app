"""Assemble the DI01005011 Plant Utilities (Winter 2025) solved paper."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from paperkit import write_paper  # noqa: E402
import DI01005011_parts_a as a  # noqa: E402
import DI01005011_parts_b as b  # noqa: E402

DATA = HERE / 'data' / 'DI01005011_winter2025_meta.json'
OUT = HERE.parents[1] / 'papers-upload' / 'papers' / 'DI01005011' / 'winter-2025.html'


def main():
    meta = json.loads(DATA.read_text(encoding='utf-8'))['meta']
    groups = [a.Q1, a.Q2, b.Q3, b.Q4, b.Q5]
    total = sum(len(g['cards']) for g in groups)
    assert total == meta['part_count'], (total, meta['part_count'])
    write_paper(OUT, meta, groups)
    print('wrote', OUT, 'with', total, 'answer parts')


if __name__ == '__main__':
    main()
