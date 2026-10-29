"""Checksum-pinned PRIVATE Neo4j Community 5.26 LTS teaching runtime.

Debian/Linux x86_64 reference, no root/service changes and no public bind.
Archives/runtime/secrets live outside the project in the excluded home cache.
The administrator secret is set OFFLINE BEFORE the first database launch.
This installs a tiny reference server, not Neo4j Desktop/Aura or a production
security/sizing template. Start the printed command using the process manager.
"""
import hashlib
import json
import os
from pathlib import Path
import platform
import secrets
import shlex
import shutil
import subprocess
import tarfile
import urllib.request

CACHE = Path.home() / '.cache/diplomaone-neo4j-u4'
HOME = CACHE / 'neo4j-community-5.26.32'
JAVA = CACHE / 'jdk-21.0.13+9-jre'
CONF = CACHE / 'conf'
CREDENTIALS = CACHE / 'credentials.json'
DOWNLOADS = [
    ('https://dist.neo4j.org/neo4j-community-5.26.32-unix.tar.gz',
     'neo4j-community-5.26.32-unix.tar.gz',
     'd279ae6a9b38034280681a558b0cd222dce89f87cc3d9867f1f7bd28ef5ebc30'),
    ('https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.13%2B9/OpenJDK21U-jre_x64_linux_hotspot_21.0.13_9.tar.gz',
     'OpenJDK21U-jre_x64_linux_hotspot_21.0.13_9.tar.gz',
     'a535a1df9c6284d9618872984e026ae0352d1f7e9e0605425c0e6114f47351dd'),
]


def environment():
    env = os.environ.copy()
    env.update({'JAVA_HOME': str(JAVA), 'NEO4J_HOME': str(HOME), 'NEO4J_CONF': str(CONF)})
    return env


def main():
    assert platform.system() == 'Linux' and platform.machine() == 'x86_64', 'Use the official guide for your OS'
    CACHE.mkdir(parents=True, exist_ok=True); CACHE.chmod(0o700)
    pidfile = CACHE / 'run/neo4j.pid'
    if pidfile.exists():
        pid = pidfile.read_text().strip()
        proc = Path('/proc') / pid / 'cmdline'
        if proc.exists() and str(CACHE).encode() in proc.read_bytes():
            raise RuntimeError('Stop the existing managed teaching server before changing its setup.')
    for url, name, wanted in DOWNLOADS:
        path = CACHE / name
        if not path.exists():
            request = urllib.request.Request(url, headers={'User-Agent':'diplomaone-teaching-runtime'})
            with urllib.request.urlopen(request, timeout=60) as source, path.open('wb') as dest:
                shutil.copyfileobj(source, dest, 1024 * 1024)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == wanted, 'Official archive checksum mismatch'
        print('Verified SHA-256:', name)
        target = JAVA if name.startswith('OpenJDK') else HOME
        if not target.exists():
            with tarfile.open(path) as archive:
                for member in archive.getmembers():
                    assert not member.name.startswith('/') and '..' not in Path(member.name).parts
                archive.extractall(CACHE, filter='data')
            assert target.is_dir()
    CONF.mkdir(exist_ok=True)
    for src in (HOME / 'conf').iterdir():
        if src.is_file() and src.name != 'neo4j.conf': shutil.copy2(src, CONF / src.name)
    settings = {
        'server.default_listen_address':'127.0.0.1',
        'server.default_advertised_address':'127.0.0.1',
        'server.bolt.enabled':'true',
        'server.bolt.listen_address':'127.0.0.1:7688',
        'server.bolt.advertised_address':'127.0.0.1:7688',
        'server.http.enabled':'true',
        'server.http.listen_address':'127.0.0.1:7475',
        'server.http.advertised_address':'127.0.0.1:7475',
        'server.https.enabled':'false', 'dbms.security.auth_enabled':'true',
        'dbms.usage_report.enabled':'false',
        'server.memory.heap.initial_size':'256m', 'server.memory.heap.max_size':'384m',
        'server.memory.pagecache.size':'128m', 'dbms.memory.transaction.total.max':'64m',
        'server.directories.data':str(CACHE / 'data'),
        'server.directories.logs':str(CACHE / 'logs'),
        'server.directories.run':str(CACHE / 'run'),
        'server.directories.import':str(CACHE / 'import'),
        'db.tx_log.rotation.retention_policy':'1 days', 'db.tx_log.rotation.size':'16M',
    }
    base = (HOME / 'conf/neo4j.conf').read_text()
    lines = [line for line in base.splitlines() if line.split('=',1)[0].strip() not in settings]
    lines += ['\n# Private single-instance teaching reference; NOT production sizing.']
    lines += [key + '=' + value for key, value in settings.items()]
    lines += ['server.jvm.additional=-XX:ActiveProcessorCount=2',
              'server.jvm.additional=-XX:MaxDirectMemorySize=128m']
    (CONF / 'neo4j.conf').write_text('\n'.join(lines) + '\n')
    for folder in ('data','logs','run','import'): (CACHE / folder).mkdir(exist_ok=True)
    if not CREDENTIALS.exists():
        if (CACHE / 'data/databases').exists() or (CACHE / 'data/dbms/auth.ini').exists():
            raise RuntimeError('Existing authentication/data without the private credential record: inspect, do not reset.')
        password = secrets.token_urlsafe(36)
        fd = os.open(CREDENTIALS, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        with os.fdopen(fd, 'w') as file: json.dump({'username':'neo4j','password':password},file)
        result = subprocess.run([str(HOME/'bin/neo4j-admin'),'dbms','set-initial-password',password,
                                  '--require-password-change=false'], env=environment(),
                                text=True, capture_output=True, timeout=45)
        if result.returncode:
            raise RuntimeError('Offline password initialization failed; inspect before retrying: '
                               + (result.stdout + result.stderr).replace(password,'<private password>'))
        print('Private initial administrator password configured before launch; not displayed/exported.')
    else:
        assert CREDENTIALS.stat().st_mode & 0o777 == 0o600
        print('Retained private authentication; no password reset performed.')
    print(subprocess.check_output([str(JAVA/'bin/java'),'-version'],stderr=subprocess.STDOUT,text=True).strip())
    command = ' '.join(' '.join([key + '=' + shlex.quote(str(value))]) for key,value in
        [('JAVA_HOME',JAVA),('NEO4J_HOME',HOME),('NEO4J_CONF',CONF)])
    command += ' ' + shlex.quote(str(HOME/'bin/neo4j')) + ' console'
    (CACHE/'foreground-command.txt').write_text(command+'\n')
    print('Foreground command (use managed process tool):\n' + command)


if __name__ == '__main__': main()
