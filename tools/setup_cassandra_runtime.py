"""Reproducible tiny, private Cassandra teaching runtime (Debian 13 x86_64).

Downloads verified official Apache/Temurin binaries into excluded user cache,
not the project. Does NOT launch a background process. This memory-reduced
single-node configuration is for small synthetic labs, NOT production sizing,
cluster operations, TLS hardening or availability/performance benchmarking.
Start the printed foreground command through the process manager, then run
`python3 tools/cassandra_content.py --bootstrap` to replace default access.
"""
from pathlib import Path
import hashlib
import os
import re
import shlex
import shutil
import tarfile
import urllib.request

CACHE = Path.home() / '.cache/diplomaone-cassandra-u3'
HOME = CACHE / 'apache-cassandra-5.0.9'
JAVA = CACHE / 'jdk-17.0.21+9-jre'
CONF = CACHE / 'conf'
CASSANDRA_URL = 'https://downloads.apache.org/cassandra/5.0.9/apache-cassandra-5.0.9-bin.tar.gz'
CASSANDRA_SHA512 = 'beaf3df6342ef1a0ccc83fa80214f250b32c35cfbb1af591b00e3fd539eef0915bc3b89f0e7ae73f6d50cbb03f6075c4e4cf32d3c46ff9c33f745542fcc925df'
JAVA_URL = 'https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.21%2B9/OpenJDK17U-jre_x64_linux_hotspot_17.0.21_9.tar.gz'
JAVA_SHA256 = '9f41bf88c7900c7097444a1bdeb84146ae692bc08842490ab098063c74bf9a8a'


def archive(name, url, algorithm, expected, target):
    file = CACHE / name
    if not file.exists():
        with urllib.request.urlopen(url, timeout=60) as response, file.open('wb') as out:
            shutil.copyfileobj(response, out)
    with file.open('rb') as inp: actual = hashlib.file_digest(inp, algorithm).hexdigest()
    if actual != expected: raise RuntimeError('Checksum mismatch: ' + name)
    print('Verified official archive:', name, algorithm, actual)
    if not target.exists():
        with tarfile.open(file) as tar: tar.extractall(CACHE, filter='data')


def prepare():
    if os.uname().machine != 'x86_64': raise SystemExit('This binary recipe is Linux x86_64 only.')
    CACHE.mkdir(parents=True, exist_ok=True)
    archive('apache-cassandra-5.0.9-bin.tar.gz', CASSANDRA_URL, 'sha512', CASSANDRA_SHA512, HOME)
    archive('temurin17-jre.tar.gz', JAVA_URL, 'sha256', JAVA_SHA256, JAVA)
    if not CONF.exists(): shutil.copytree(HOME / 'conf', CONF)
    source = (HOME / 'conf/cassandra.yaml').read_text()
    settings = {
        'cluster_name': "'DiplomaOne U3 private lab'", 'num_tokens': '16',
        'listen_address': '127.0.0.1', 'rpc_address': '127.0.0.1',
        'native_transport_port': '9043', 'endpoint_snitch': 'GossipingPropertyFileSnitch',
        'authenticator': 'PasswordAuthenticator', 'authorizer': 'CassandraAuthorizer',
        'concurrent_reads': '4', 'concurrent_writes': '4', 'concurrent_counter_writes': '2',
        'concurrent_materialized_view_writes': '2',
        'key_cache_size': '8MiB', 'index_summary_capacity': '16MiB',
        'commitlog_segment_size': '8MiB',
    }
    for key, value in settings.items():
        source, count = re.subn(r'^' + re.escape(key) + r':[^\n]*$', key + ': ' + value, source, flags=re.M)
        if count != 1: raise RuntimeError('Unexpected official YAML structure: ' + key)
    # These override commented defaults. Paths remain inside the private cache.
    source += '\n# Small synthetic single-node reference lab only.\n'
    source += '\n'.join([
        'data_file_directories:', '    - ' + str(CACHE / 'data'),
        'commitlog_directory: ' + str(CACHE / 'commitlog'),
        'saved_caches_directory: ' + str(CACHE / 'saved_caches'),
        'hints_directory: ' + str(CACHE / 'hints'),
        'cdc_raw_directory: ' + str(CACHE / 'cdc_raw'),
        'commitlog_total_space: 64MiB', 'file_cache_size: 32MiB',
        'memtable_heap_space: 32MiB', 'memtable_offheap_space: 32MiB',
        'memtable_flush_writers: 1', 'concurrent_compactors: 1',
    ]) + '\n'
    (CONF / 'cassandra.yaml').write_text(source)
    (CONF / 'cassandra-rackdc.properties').write_text('dc=datacenter1\nrack=rack1\nprefer_local=true\n')
    for folder in ('data', 'commitlog', 'saved_caches', 'hints', 'cdc_raw', 'logs'):
        (CACHE / folder).mkdir(exist_ok=True)
    env = {
        'JAVA_HOME': str(JAVA), 'CASSANDRA_HOME': str(HOME), 'CASSANDRA_CONF': str(CONF),
        'CASSANDRA_LOG_DIR': str(CACHE / 'logs'),
        'MAX_HEAP_SIZE': '512M', 'HEAP_NEWSIZE': '100M', 'LOCAL_JMX': 'yes',
        'JVM_EXTRA_OPTS': '-XX:ActiveProcessorCount=2 -XX:MaxDirectMemorySize=192m -Djava.rmi.server.hostname=127.0.0.1',
    }
    command = 'env ' + ' '.join(k + '=' + shlex.quote(v) for k, v in env.items())
    command += ' ' + shlex.quote(str(HOME / 'bin/cassandra')) + ' -f'
    (CACHE / 'foreground-command.txt').write_text(command + '\n')
    print('Foreground start command (private loopback, no public preview):\n' + command)
    print('Once ready: python3 tools/cassandra_content.py --bootstrap')


if __name__ == '__main__': prepare()
