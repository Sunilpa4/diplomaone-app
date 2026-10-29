"""Real authenticated Cassandra execution for DI04000031 Unit 3.

No mocking. Private runtime data/credentials are outside the synchronized
project and excluded from snapshots. Public CQL and observed JSON outputs are
built using cassandra_lab_runner, which is also shipped in the student ZIP.
"""
import json
import os
from pathlib import Path
import re
import secrets
import subprocess
import sys
import tempfile

from cassandra_lab_runner import load_driver, connect, run_source
from setup_cassandra_runtime import CACHE, HOME, JAVA, CONF

CREDENTIALS = CACHE / 'credentials.json'
HOST = '127.0.0.1'
PORT = 9043


def credentials(): return json.loads(CREDENTIALS.read_text())


def open_session():
    value = credentials()
    return connect(value['username'], value['password'], HOST, PORT, HOME)


def private_files(value):
    config = CACHE / 'cqlshrc'
    config.write_text('[auth_provider]\nmodule = cassandra.auth\nclassname = PlainTextAuthProvider\n[protocol]\nversion = 4\n[ui]\ncolor = off\ntimezone = UTC\n')
    file = CACHE / 'credentials.ini'
    fd = os.open(file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    os.fchmod(fd, 0o600)
    with os.fdopen(fd, 'w') as out:
        out.write('[PlainTextAuthProvider]\nusername = ' + value['username'] + '\npassword = ' + value['password'] + '\n')
    return config, file


def bootstrap_runtime():
    if CREDENTIALS.exists():
        print('Private Cassandra credentials already configured.'); return
    # The factory default is used ONLY on the brand-new loopback-bound lab.
    cluster, session = connect('cassandra', 'cassandra', HOST, PORT, HOME)
    value = {'username': 'diploma_u3_runtime', 'password': secrets.token_urlsafe(32)}
    try:
        session.execute('CREATE ROLE diploma_u3_runtime WITH PASSWORD = %s AND LOGIN = true AND SUPERUSER = true', (value['password'],))
    finally: cluster.shutdown()
    cluster, session = connect(value['username'], value['password'], HOST, PORT, HOME)
    try:
        # Persist privately before revoking factory access; never display secrets.
        fd = os.open(CREDENTIALS, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'w') as out: json.dump(value, out)
        private_files(value)
        session.execute('ALTER ROLE cassandra WITH LOGIN = false AND SUPERUSER = false AND PASSWORD = %s', (secrets.token_urlsafe(32),))
    finally: cluster.shutdown()
    print('Private administrator created; factory role disabled/rotated; credentials stored outside the project.')


def cqlsh(source):
    value = credentials(); config, file = private_files(value)
    env = os.environ.copy(); env['CQLSH_PYTHON'] = sys.executable; env['CQL_HISTORY'] = os.devnull
    r = subprocess.run([str(HOME / 'bin/cqlsh'), HOST, str(PORT), '--no-color', '--disable-history',
         '--cqlshrc', str(config), '--credentials', str(file), '--execute', source],
         env=env, text=True, capture_output=True, timeout=45)
    if r.returncode or r.stderr.strip():
        raise RuntimeError('cqlsh reference failed: ' + (r.stderr + r.stdout).replace(value['password'], '<private password>'))
    return r.stdout.strip()


def nodetool_status():
    env = os.environ.copy(); env['JAVA_HOME'] = str(JAVA); env['CASSANDRA_HOME'] = str(HOME); env['CASSANDRA_CONF'] = str(CONF)
    r = subprocess.run([str(HOME / 'bin/nodetool'), '-h', HOST, '-p', '7199', 'status'], env=env,
                       text=True, capture_output=True, timeout=40)
    if r.returncode: raise RuntimeError('Read-only nodetool status failed: ' + r.stderr)
    assert re.search(r'^UN\s+127\.0\.0\.1\s', r.stdout, re.M), 'Expected single local Up/Normal node'
    return r.stdout.strip()


def assert_runtime():
    cluster, session = open_session()
    try:
        row = session.execute("SELECT release_version,cql_version,data_center,partitioner FROM system.local WHERE key='local'").one()
        peers = list(session.execute('SELECT peer FROM system.peers_v2'))
        factory = session.execute("SELECT can_login,is_superuser FROM system_auth.roles WHERE role='cassandra'").one()
        assert row['release_version'] == '5.0.9' and row['data_center'] == 'datacenter1'
        assert peers == [] and factory['can_login'] is False and factory['is_superuser'] is False
    finally: cluster.shutdown()
    show = cqlsh('SHOW VERSION;')
    shell_version = re.search(r'cqlsh ([0-9.]+)', show).group(1)
    assert 'Cassandra 5.0.9' in show and 'Native protocol v4' in show
    java_output = subprocess.check_output([str(JAVA / 'bin/java'), '-version'], stderr=subprocess.STDOUT, text=True)
    java_version = re.search(r'Temurin-([0-9.+]+)', java_output).group(1)
    assert java_version == '17.0.21+9'
    return {'server': row['release_version'], 'cql': row['cql_version'], 'cqlsh': shell_version,
            'driver': load_driver(HOME)[0].__version__, 'java': 'Temurin ' + java_version,
            'data_center': row['data_center'], 'partitioner': row['partitioner'].split('.')[-1],
            'authenticated': True, 'factory_login_disabled': True, 'physical_nodes': 1,
            'protocol': 4, 'nodetool_status': 'UN (single local node)'}


def scratch_keyspaces():
    cluster, session = open_session()
    try:
        return sorted(r['keyspace_name'] for r in session.execute('SELECT keyspace_name FROM system_schema.keyspaces')
                      if r['keyspace_name'].startswith('di04000031_u3_'))
    finally: cluster.shutdown()


def run_script(source):
    from content_DI04000031_u3_shared import CSV
    value = credentials(); cluster, session = open_session()
    try:
        with tempfile.TemporaryDirectory(prefix='cassandra-fixture-') as tmp:
            Path(tmp, 'sensors.csv').write_text(CSV)
            return run_source(source, session, value['username'], value['password'], HOME, HOST, PORT, tmp)
    finally: cluster.shutdown()


def P(id_, title, body, expl):
    keyspace = 'di04000031_u3_' + id_
    source = ('-- Independent private lab; the guarded runner refuses existing keyspaces.\n'
        'CREATE KEYSPACE ' + keyspace + '\n'
        "WITH replication = {'class':'NetworkTopologyStrategy',\n"
        "                    'datacenter1':1};\n"
        'USE ' + keyspace + ';\n\n' + body.strip() + '\n\n'
        '-- Drop only the new keyspace created by this independent example.\n'
        'USE system;\nDROP KEYSPACE ' + keyspace + ';\n')
    # The keyspace placeholder is an authoring convenience, not shipped unresolved.
    source = source.replace('@@KS@@', keyspace)
    output = run_script(source)
    return {'id': id_, 'title': {'en': title}, 'code': {'en': source.rstrip('\n')},
            'out': output, 'expl': {'en': expl}}


if __name__ == '__main__':
    if '--bootstrap' in sys.argv: bootstrap_runtime()
    print(json.dumps(assert_runtime(), indent=2))
    print('Actual authenticated cqlsh:', cqlsh('SHOW VERSION;'))
    print('Read-only nodetool status:\n' + nodetool_status())
    print('Remaining scoped scratch keyspaces:', len(scratch_keyspaces()))
