"""Build the DI01005011 (Plant Utilities) Summer 2026 solved paper."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from paperkit import write_paper
import DI01005011_summer2026_a as a
import DI01005011_summer2026_b as b

meta = json.loads((HERE / 'data' / 'DI01005011_summer2026_meta.json').read_text())['meta']
groups = [a.Q1, a.Q2, b.Q3, b.Q4, b.Q5]
total = sum(len(g['cards']) for g in groups)
assert total == meta['part_count'], f"part count {total} != {meta['part_count']}"

out = HERE.parents[1] / 'papers-upload' / 'papers' / 'DI01005011' / 'summer-2026.html'
write_paper(out, meta, groups)
print(f'wrote {out} with {total} answer parts')
