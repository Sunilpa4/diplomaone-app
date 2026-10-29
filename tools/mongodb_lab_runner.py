"""Run one supplied .js lesson in a fresh MongoDB scratch database.

Public, credential-free runner for the practical download. Uses mongosh,
not a Python MongoDB emulator/driver. A private URI comes from MONGODB_URI
or a hidden prompt, never a checked-in password or command-line argument.
The URI must authorize creation and cleanup of a fresh lab DB. Use a private
learning server/account, not a production server or application identity.
"""
import argparse
import getpass
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import uuid


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('script', type=Path, help='One supplied independent .js program')
    args = parser.parse_args()
    executable = shutil.which('mongosh')
    if not executable: raise SystemExit('Install mongosh and put it on PATH first.')
    code = args.script.read_text(encoding='utf-8')
    if 'di04000031_u2_' not in code:
        raise SystemExit('Expected a prefix-guarded Unit 2 reference script.')
    uri = os.environ.get('MONGODB_URI')
    if not uri:
        uri = getpass.getpass('Private lab MongoDB URI (hidden): ')
    if not uri or not uri.startswith(('mongodb://', 'mongodb+srv://')):
        raise SystemExit('Provide a valid private lab URI; no database was changed.')
    label = re.sub(r'[^a-z0-9_]', '_', args.script.stem.lower())[:28]
    database = 'di04000031_u2_' + label + '_' + uuid.uuid4().hex[:10]
    if not re.fullmatch(r'di04000031_u2_[a-z0-9_]+', database):
        raise SystemExit('Invalid scratch database name.')
    env = os.environ.copy()
    env['DIPLOMA_MONGO_URI'] = uri
    env['DIPLOMA_MONGO_DB'] = database
    env['MONGOSH_DISABLE_TELEMETRY'] = '1'
    wrapper = '''const __diplomaConn = new Mongo(process.env.DIPLOMA_MONGO_URI);
const __diplomaScratch = __diplomaConn.getDB(process.env.DIPLOMA_MONGO_DB);
db = __diplomaScratch;
try {
''' + code + '''
} finally {
  try { __diplomaScratch.dropDatabase(); }
  finally { __diplomaConn.close(); }
}
'''
    with tempfile.TemporaryDirectory(prefix='mongodb-reference-') as tmp:
        file = Path(tmp, 'execute.js'); file.write_text(wrapper, encoding='utf-8')
        r = subprocess.run([executable, '--nodb', '--quiet', '--norc', '--file', str(file)],
                           env=env, text=True, capture_output=True, timeout=40)
    # stdout contains only the actual program output, for comparison with expected/.
    sys.stdout.write(r.stdout.replace(uri, '<private URI>'))
    if r.stderr: sys.stderr.write(r.stderr.replace(uri, '<private URI>'))
    return r.returncode


if __name__ == '__main__': raise SystemExit(main())
