"""Summarize Flutter's JSON test events as GitHub Actions annotations."""
import json
import sys
from pathlib import Path


def escape(message):
    return str(message).replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')


def main(path):
    tests = {}
    errors = []
    bad_parts = []
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = event.get('type')
        if kind == 'testStart':
            test = event.get('test', {})
            tests[test.get('id')] = test.get('name', 'Unknown test')
        elif kind == 'error':
            errors.append((event.get('testID'), event.get('error', 'Unknown error')))
        elif kind == 'print' and 'BAD ' in event.get('message', ''):
            bad_parts.append((event.get('testID'), event['message']))
    for test_id, message in errors + bad_parts:
        print(f"::error::{escape(tests.get(test_id, 'Unknown test'))}: {escape(message)}")
    if not errors and not bad_parts:
        print('No detailed test failure events were reported; see the workflow log.')


if __name__ == '__main__':
    main(sys.argv[1])
