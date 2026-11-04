"""Add the site's authorised sellers without silently deleting other entries."""
import sys
from pathlib import Path


def record_key(line):
    record = line.split('#', 1)[0].strip()
    return tuple(part.strip().lower() for part in record.split(',')) if record else ()


def merge_ads(existing, additions):
    lines = existing.splitlines()
    known = {record_key(line) for line in lines} - {()}
    for line in additions.splitlines():
        key = record_key(line)
        if not key or key in known:
            continue
        lines.append(line.strip())
        known.add(key)
    return '\n'.join(lines) + ('\n' if lines else '')


if __name__ == '__main__':
    source, destination = (Path(arg) for arg in sys.argv[1:])
    previous = destination.read_text(encoding='utf-8') if destination.exists() else ''
    destination.write_text(merge_ads(previous, source.read_text(encoding='utf-8')), encoding='utf-8')
