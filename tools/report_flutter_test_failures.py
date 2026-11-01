"""Summarize Flutter's JSON test events as GitHub Actions annotations."""
import json
import sys
from pathlib import Path


def escape(message):
    return str(message).replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')


def main(path):
    tests, output, errors, failed = {}, {}, {}, set()
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind, test_id = event.get('type'), event.get('testID')
        if kind == 'testStart':
            test = event.get('test', {})
            tests[test.get('id')] = test.get('name', 'Unknown test')
        elif kind == 'error':
            errors.setdefault(test_id, []).append(event.get('error', 'Unknown error'))
        elif kind == 'print':
            output.setdefault(test_id, []).append(event.get('message', ''))
        elif kind == 'testDone' and event.get('result') in ('failure', 'error'):
            failed.add(test_id)
    for test_id in failed | set(errors):
        name = tests.get(test_id, 'Unknown test')
        details = '\n'.join(output.get(test_id, []) + errors.get(test_id, []))
        print(f"::error::{escape(name)}: {escape(details[:6000])}")
    if not failed and not errors:
        print('No detailed test failure events were reported; see the workflow log.')


if __name__ == '__main__':
    main(sys.argv[1])
