"""Real mongosh -> authenticated local mongod teaching harness.

No emulator. Credentials and database storage live outside the project.
Every script receives a fresh prefix-guarded scratch database and drops only
that captured database in finally. Published source never contains a URI secret.
"""
import json
import os
from pathlib import Path
import re
import shutil
import secrets
import sys
import subprocess
import tempfile
from urllib.parse import quote
import uuid

PREFIX = 'di04000031_u2_'
CREDENTIALS = Path.home() / '.cache/diplomaone-mongodb-u2/credentials.json'
MONGOSH = shutil.which('mongosh') or 'mongosh'
GUARD = '''// Run only in a fresh, disposable lab database.
if (!db.getName().startsWith("di04000031_u2_")) {
  throw new Error("Select an isolated Unit 2 scratch database");
}
'''


def private_uri():
    c = json.loads(CREDENTIALS.read_text())
    return ('mongodb://' + quote(c['username'], safe='') + ':'
            + quote(c['password'], safe='')
            + '@127.0.0.1:27027/admin?authSource=admin&directConnection=true&serverSelectionTimeoutMS=5000')


def shell(code, uri=None, database='admin'):
    env = os.environ.copy()
    env['DIPLOMA_MONGO_URI'] = private_uri() if uri is None else uri
    env['DIPLOMA_MONGO_DB'] = database
    env['MONGOSH_DISABLE_TELEMETRY'] = '1'
    wrapper = '''const __diplomaConn = new Mongo(process.env.DIPLOMA_MONGO_URI);
db = __diplomaConn.getDB(process.env.DIPLOMA_MONGO_DB);
try {
''' + code + '''
} finally {
  __diplomaConn.close();
}
'''
    with tempfile.TemporaryDirectory(prefix='mongodb-lab-') as tmp:
        file = Path(tmp, 'execute.js'); file.write_text(wrapper)
        r = subprocess.run([MONGOSH, '--nodb', '--quiet', '--norc', '--file', str(file)],
                           env=env, text=True, capture_output=True, timeout=30)
    if r.returncode:
        # Credentials are never included in command arguments or error messages.
        raise RuntimeError('mongosh execution failed: ' + (r.stderr + r.stdout).replace(env['DIPLOMA_MONGO_URI'], '<private URI>'))
    if r.stderr.strip():
        raise RuntimeError('Unexpected mongosh diagnostic: ' + r.stderr.replace(env['DIPLOMA_MONGO_URI'], '<private URI>'))
    return r.stdout.rstrip('\n')


def run_script(code, label='demo'):
    label = re.sub(r'[^a-z0-9_]', '_', label.lower())[:30]
    name = PREFIX + label + '_' + uuid.uuid4().hex[:10]
    assert re.fullmatch(r'di04000031_u2_[a-z0-9_]+', name)
    # Capture the original DB so a script cannot redirect cleanup accidentally.
    wrapped = 'const __diplomaScratch = db;\ntry {\n' + code + '''
} finally {
  __diplomaScratch.dropDatabase();
}
'''
    return shell(wrapped, database=name)


def bootstrap_runtime():
    """Initialize only this private server's first local user; never replace one."""
    if CREDENTIALS.exists():
        assert_runtime()
        print('Private authenticated lab credentials already configured.')
        return
    password = secrets.token_urlsafe(32)
    env = os.environ.copy(); env['DIPLOMA_MONGO_BOOTSTRAP'] = password
    code = ('db.createUser({user:"diploma_u2_runtime",'
            'pwd:process.env.DIPLOMA_MONGO_BOOTSTRAP,'
            'roles:[{role:"root",db:"admin"}]});'
            'print("Private lab administrator created via localhost exception");')
    r = subprocess.run([MONGOSH,
        'mongodb://127.0.0.1:27027/admin?directConnection=true',
        '--quiet', '--norc', '--eval', code], env=env,
        text=True, capture_output=True, timeout=20)
    if r.returncode:
        raise RuntimeError('Private bootstrap failed. Do not reset an existing user/database: '
                           + r.stderr.replace(password, '<private password>'))
    CREDENTIALS.parent.mkdir(exist_ok=True, parents=True)
    # Create rather than overwrite; restrict permissions before writing a secret.
    fd = os.open(CREDENTIALS, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w') as file:
        json.dump({'username': 'diploma_u2_runtime', 'password': password}, file)
    print('Private credentials stored outside the project, not displayed/exported.')


def assert_runtime():
    out = shell('''const hello = db.hello();
print(JSON.stringify({
  server: db.version(),
  authenticated: db.runCommand({connectionStatus: 1})
    .authInfo.authenticatedUsers.length > 0,
  standalone: !hello.setName && hello.msg !== "isdbgrid",
  ping: db.runCommand({ping: 1}).ok
}));''')
    info = json.loads(out)
    info['shell'] = subprocess.check_output([MONGOSH, '--version'], text=True).strip()
    assert info['ping'] == 1 and info['authenticated'] and info['standalone'], info
    return info


def scratch_databases():
    return json.loads(shell('''print(JSON.stringify(
  db.adminCommand({listDatabases: 1, nameOnly: true}).databases
    .map(x => x.name).filter(x => x.startsWith("di04000031_u2_"))
));'''))


def P(id_, title, code, expl):
    code = GUARD + code.strip('\n') + '\n'
    out = run_script(code, id_)
    return {'id': id_, 'title': {'en': title}, 'code': {'en': code.rstrip('\n')},
            'out': out, 'expl': {'en': expl}}


if __name__ == '__main__':
    if '--bootstrap' in sys.argv: bootstrap_runtime()
    print(json.dumps(assert_runtime(), indent=2))
    print('Remaining scoped scratch databases:', len(scratch_databases()))
