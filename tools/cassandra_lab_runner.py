"""Run trusted Unit 3 CQL examples on REAL Cassandra, not an emulator.

Credentials come from a hidden prompt/private environment. Each supplied file
creates one fixed, prefix-scoped lab keyspace. Refuse an existing namespace;
mark ownership ONLY after CREATE succeeds; finally drop only that owned KS.
Statements are sent unchanged (apart from ignored comments) to Cassandra.
Result sets are JSON-serialized; row order is preserved, not client-sorted.
COPY FROM is a cqlsh special command, delegated to the real bundled cqlsh.
This is a small private teaching runner, not a production SQL security parser.
"""
import argparse
from collections.abc import Mapping
from datetime import datetime, timezone
from decimal import Decimal
import getpass
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from uuid import UUID


def load_driver(home=None):
    home = Path(home or os.environ.get('CASSANDRA_HOME', '.')).expanduser().resolve()
    lib = home / 'lib'
    if lib.is_dir():
        for prefix in ('pure_sasl-', 'wcwidth-', 'pyasyncore-'):
            for z in lib.glob(prefix + '*.zip'): sys.path.insert(0, str(z))
        for z in lib.glob('cassandra-driver-internal-only-*.zip'):
            version = z.name.removeprefix('cassandra-driver-internal-only-').removesuffix('.zip')
            sys.path.insert(0, str(z) + '/cassandra-driver-' + version)
    try:
        import cassandra
        from cassandra.cluster import Cluster
        from cassandra.auth import PlainTextAuthProvider
        from cassandra.policies import DCAwareRoundRobinPolicy
        from cassandra.query import dict_factory
    except ImportError as e:
        raise RuntimeError('Set CASSANDRA_HOME to the official extracted distribution, or install a compatible cassandra-driver.') from e
    return cassandra, Cluster, PlainTextAuthProvider, DCAwareRoundRobinPolicy, dict_factory


def statements(source):
    """Small CQL lexer: single/double quotes, escaped quote pairs, -- comments.

    @result and @expect are human-readable comments consumed by this runner.
    Each must precede a statement. UDFs/block-comment scripts are not supported.
    """
    result = []; chars = []; quote = None; label = None; expected = None; i = 0
    while i < len(source):
        char = source[i]
        if quote:
            chars.append(char)
            if char == quote:
                if i + 1 < len(source) and source[i + 1] == quote:
                    chars.append(source[i + 1]); i += 1
                else: quote = None
        elif char in ("'", '"'):
            quote = char; chars.append(char)
        elif source[i:i + 2] == '--':
            end = source.find('\n', i)
            if end < 0: end = len(source)
            comment = source[i:end]
            match = re.search(r'@result\s+([a-z0-9_]+)', comment)
            if match: label = match.group(1)
            match = re.search(r'@expect\s+([A-Za-z]+)', comment)
            if match: expected = match.group(1)
            chars.append('\n'); i = end - 1
        elif char == ';':
            sql = ''.join(chars).strip()
            if sql: result.append((sql, label, expected))
            chars = []; label = None; expected = None
        else: chars.append(char)
        i += 1
    if quote or ''.join(chars).strip(): raise ValueError('Unterminated CQL string/statement; add the final semicolon.')
    return result


def safe_namespace(source):
    parsed = statements(source)
    creates = [re.match(r'^CREATE\s+KEYSPACE\s+(\w+)\s+WITH\b', sql, re.I) for sql, _, _ in parsed]
    names = [m.group(1) for m in creates if m]
    if len(names) != 1 or not re.fullmatch(r'di04000031_u3_[a-z0-9_]{1,30}', names[0]):
        raise ValueError('Expected exactly one new prefix-scoped Unit 3 keyspace, not a real application namespace.')
    name = names[0]
    for sql, _, _ in parsed:
        m = re.match(r'^(?:CREATE|ALTER|DROP)\s+KEYSPACE\s+(\w+)\b', sql, re.I)
        if m and m.group(1) != name: raise ValueError('Cross-keyspace schema operation rejected.')
        m = re.match(r'^USE\s+(\w+)\s*$', sql, re.I)
        if m and m.group(1) not in (name, 'system'): raise ValueError('Unexpected USE context.')
        if re.match(r'^(?:CREATE|ALTER|DROP)\s+(?:ROLE|USER)\b', sql, re.I):
            raise ValueError('Role/user management is not a course data example.')
    return name, parsed


def normalize(value):
    if isinstance(value, datetime):
        if value.tzinfo is None: value = value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')
    if isinstance(value, Mapping): return {str(k): normalize(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [normalize(v) for v in value]
    if isinstance(value, (set, frozenset)): return sorted(normalize(v) for v in value)
    if value is None or isinstance(value, (str, bool, int, float)): return value
    if isinstance(value, (UUID, Decimal)): return str(value)
    # Includes the driver's CQL date value, rendered as YYYY-MM-DD.
    return str(value)


def connect(username, password, host='127.0.0.1', port=9042, home=None):
    cassandra, Cluster, Auth, DCPolicy, factory = load_driver(home)
    cluster = Cluster([host], port=port, protocol_version=4,
                      auth_provider=Auth(username=username, password=password),
                      load_balancing_policy=DCPolicy(local_dc='datacenter1'),
                      connect_timeout=15)
    try:
        session = cluster.connect(); session.row_factory = factory
        session.default_timeout = 25
        return cluster, session
    except BaseException:
        cluster.shutdown(); raise


def copy_from(sql, keyspace, username, password, home, host, port, fixtures):
    if not home: raise RuntimeError('Set CASSANDRA_HOME to the matching distribution for real cqlsh COPY.')
    home = Path(home).resolve(); fixtures = Path(fixtures).resolve()
    executable = home / 'bin/cqlsh'
    if not executable.is_file(): raise RuntimeError('COPY requires the actual matching Cassandra cqlsh distribution.')
    match = re.search(r"\bFROM\s+'([^']+)'", sql, re.I)
    if not match or match.group(1) != 'sensors.csv' or not (fixtures / 'sensors.csv').is_file():
        raise ValueError('This teaching COPY expects the supplied sensors.csv fixture.')
    with tempfile.TemporaryDirectory(prefix='cassandra-copy-') as tmp:
        root = Path(tmp); config = root / 'cqlshrc'; credentials = root / 'credentials.ini'; script = root / 'copy.cql'
        config.write_text('[auth_provider]\nmodule = cassandra.auth\nclassname = PlainTextAuthProvider\n[protocol]\nversion = 4\n[ui]\ncolor = off\ntimezone = UTC\n')
        fd = os.open(credentials, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        with os.fdopen(fd, 'w') as f:
            f.write('[PlainTextAuthProvider]\nusername = ' + username + '\npassword = ' + password + '\n')
        script.write_text(sql + ';\n')
        env = os.environ.copy(); env['CQLSH_PYTHON'] = sys.executable; env['CQL_HISTORY'] = os.devnull; env['TZ'] = 'UTC'
        r = subprocess.run([str(executable), host, str(port), '--no-color', '--disable-history',
             '--cqlshrc', str(config), '--credentials', str(credentials), '--keyspace', keyspace,
             '--request-timeout', '30', '--file', str(script)], cwd=fixtures, env=env,
             text=True, capture_output=True, timeout=90)
        # cqlsh may not return nonzero for every statement/import failure.
        if r.returncode or re.search(r'\b(?:Error|Failed|Exception|Traceback|InvalidRequest|SyntaxException|AuthenticationFailed|Unauthorized)\b', r.stdout + r.stderr, re.I):
            raise RuntimeError('Real cqlsh COPY failed: ' + (r.stdout + r.stderr).replace(password, '<private password>'))
        if not re.search(r'\b8 rows imported\b', r.stdout):
            raise RuntimeError('Expected all eight synthetic CSV rows to be imported.')
        return r.stdout  # Actual raw stdout; callers omit dynamic rates/timings from published output.


def run_source(source, session, username, password, home, host='127.0.0.1', port=9042, fixtures='.'):
    name, parsed = safe_namespace(source)
    existing = session.execute('SELECT keyspace_name FROM system_schema.keyspaces WHERE keyspace_name=%s', (name,)).one()
    if existing: raise RuntimeError('Refusing pre-existing keyspace; nothing dropped: ' + name)
    created = False; output = []; current = None
    try:
        for sql, label, expected in parsed:
            creates = bool(re.match(r'^CREATE\s+KEYSPACE\b', sql, re.I))
            drops = bool(re.match(r'^DROP\s+KEYSPACE\b', sql, re.I))
            use = re.match(r'^USE\s+(\w+)\s*$', sql, re.I)
            if re.match(r'^(?:INSERT|UPDATE|DELETE|COPY|TRUNCATE)\b|^(?:CREATE|ALTER|DROP)\s+TABLE\b', sql, re.I):
                if current != name: raise ValueError('Data/schema write outside the captured scratch context.')
                # Only unqualified table names are used in the supplied write statements.
                table = re.search(r'^(?:INSERT\s+INTO|UPDATE|COPY|TRUNCATE(?:\s+TABLE)?|(?:CREATE|ALTER|DROP)\s+TABLE|DELETE(?:\s+\w+)?\s+FROM)\s+([\w.]+)', sql, re.I)
                if table and '.' in table.group(1): raise ValueError('Qualified cross-context write rejected.')
            try:
                if sql.upper().startswith('COPY '):
                    transcript = copy_from(sql, name, username, password, home, host, port, fixtures)
                    output.append((label or 'csv_import') + ': cqlsh COPY FROM completed (8 rows imported)')
                    result = None
                else: result = session.execute(sql)
            except Exception as e:
                if not expected or type(e).__name__ != expected: raise
                output.append((label or 'expected_error') + ': ' + type(e).__name__ + ' (server rejection)')
                continue
            if expected: raise AssertionError('Expected server error not raised: ' + expected)
            if creates: created = True
            if drops: created = False
            if use: current = use.group(1)
            if result is not None and result.column_names:
                rows = [normalize(row) for row in result]
                output.append((label or 'result') + ': ' + json.dumps(rows, ensure_ascii=False, separators=(',', ':')))
    finally:
        # Never use a mutable USE context to choose the cleanup target.
        if created: session.execute('DROP KEYSPACE ' + name)
    absent = session.execute('SELECT keyspace_name FROM system_schema.keyspaces WHERE keyspace_name=%s', (name,)).one() is None
    if not absent: raise RuntimeError('Scratch cleanup incomplete: ' + name)
    output.append('Scratch keyspace removed: true')
    return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('script', type=Path)
    parser.add_argument('--host', default='127.0.0.1'); parser.add_argument('--port', type=int, default=9042)
    parser.add_argument('--username', default=os.environ.get('CASSANDRA_USERNAME'))
    parser.add_argument('--cassandra-home', default=os.environ.get('CASSANDRA_HOME'))
    parser.add_argument('--fixtures', type=Path, default=Path.cwd())
    args = parser.parse_args()
    username = args.username or input('Private lab username: ')
    password = os.environ.get('CASSANDRA_PASSWORD') or getpass.getpass('Private lab password (hidden): ')
    if any('\n' in v or '\r' in v for v in (username, password)): raise ValueError('Invalid credential format.')
    cluster, session = connect(username, password, args.host, args.port, args.cassandra_home)
    try:
        print(run_source(args.script.read_text(), session, username, password, args.cassandra_home,
                         args.host, args.port, args.fixtures))
    finally: cluster.shutdown()


if __name__ == '__main__': main()
