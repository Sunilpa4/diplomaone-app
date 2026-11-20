import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFile,readdir} from 'node:fs/promises';
import {spawnSync} from 'node:child_process';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import paymentFunction,{config} from '../../netlify/functions/payments.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');

test('actual entry supports the native same-origin test route and is disabled without private environment',async()=>{
  assert.equal(config.path,'/api/payments/test/*');
  const response=await paymentFunction(new Request('https://www.diplomaone.in/api/payments/test/config'));
  const body=await response.json();assert.equal(body.enabled,false);assert.equal(body.mode,'test');
  assert(!JSON.stringify(body).includes('NETLIFY_DB_URL'));
  const insecure=await paymentFunction(new Request('http://www.diplomaone.in/api/payments/test/config'));
  assert.equal(insecure.status,400);assert.equal((await insecure.json()).error,'https_required');
});

test('runtime dependencies and lockfile live at the Netlify base so native tracing includes pg and the other packages',async()=>{
  const manifest=JSON.parse(await readFile(path.join(root,'package.json'),'utf8'));
  const lock=JSON.parse(await readFile(path.join(root,'package-lock.json'),'utf8'));
  assert.equal(manifest.type,'commonjs','existing tools/*.js must keep their CommonJS semantics; server entry is explicitly .mjs');
  for(const name of ['pg','jose','@netlify/blobs']){
    assert(manifest.dependencies[name],`${name} must be a runtime dependency at the function base`);
    assert.equal(lock.packages[''].dependencies[name],manifest.dependencies[name]);
  }
  for(const name of ['backend/package.json','backend/package-lock.json'])
    await assert.rejects(readFile(path.join(root,name)),{code:'ENOENT'});
  const result=spawnSync('python3',['-c',`import tomllib
c=tomllib.load(open('netlify.toml','rb'))
assert c['build'].get('base','.') in ('','.')
assert c['build']['functions']=='netlify/functions'
assert 'npm ci --include=dev' in c['build']['command']
assert '--prefix backend' not in c['build']['command']
`],{cwd:root,encoding:'utf8'});
  assert.equal(result.status,0,result.stderr);
});

test('Git-connected publish output contains only the same twelve public frontend files, never backend/secrets/papers',async()=>{
  const result=spawnSync('python3',['tools/build_netlify_site.py'],{cwd:root,encoding:'utf8'});
  assert.equal(result.status,0,result.stderr);
  const output=path.join(root,'build/netlify-site');
  const files=await readdir(output,{recursive:true});
  assert(files.includes('auth.js'));assert(files.includes('assets/firebase-auth.js'));
  assert(!files.some(name=>/\.env|node_modules|backend|private|\.sql|netlify\/functions|papers\//.test(name)));
  const compare=spawnSync('python3',['-c',`from zipfile import ZipFile
from pathlib import Path
out=Path('build/netlify-site')
with ZipFile('DiplomaOne-Netlify.zip') as z:
 assert len(z.namelist())==12
 assert {p.relative_to(out).as_posix() for p in out.rglob('*') if p.is_file()}==set(z.namelist())
 for name in z.namelist(): assert (out/name).read_bytes()==z.read(name),name
`],{cwd:root,encoding:'utf8'});
  assert.equal(compare.status,0,compare.stderr);
  const redirects=await readFile(path.join(output,'_redirects'),'utf8');
  assert(redirects.includes('/data/*'));assert(redirects.includes('/papers/*'));assert(!redirects.includes('127.0.0.1'));
  const invalid=spawnSync('python3',['tools/build_netlify_site.py',root],{cwd:root,encoding:'utf8'});
  assert.notEqual(invalid.status,0);assert(invalid.stderr.includes('Publish output must be'));
  const unsafe=spawnSync('python3',['-c',`import sys
sys.path.insert(0,'tools')
from pathlib import Path
from zipfile import ZipFile
from unittest.mock import patch
import build_netlify_site as b
def unsafe_package(dest):
 with ZipFile(dest,'w') as z:
  for name in b.PUBLIC_FILES: z.writestr(name,'unit fixture')
  z.writestr('backend/.env','UNIT_FIXTURE_NOT_A_SECRET')
 return dest
with patch.object(b,'build_package',unsafe_package):
 try: b.build_site('build/rejected-private-publish')
 except ValueError: pass
 else: raise AssertionError('unexpected private file was not rejected')
assert not (Path('build/rejected-private-publish')/'backend/.env').exists()
`],{cwd:root,encoding:'utf8'});
  assert.equal(unsafe.status,0,unsafe.stderr);
});

test('environment example contains the public supplied test key only and checkout flags stay off',async()=>{
  const example=await readFile(path.join(root,'backend/.env.example'),'utf8');
  assert(example.includes('RAZORPAY_KEY_ID=rzp_test_ToAdJ9DdVMFeM2'));
  for(const key of ['RAZORPAY_KEY_SECRET','RAZORPAY_WEBHOOK_SECRET'])assert(example.includes(key+'=\n'));
  assert(example.includes('PAYMENTS_TEST_ENABLED=false'));assert(example.includes('PAYMENTS_PRIVATE_MIGRATION_CONFIRMED=false'));
  const sql=await readFile(path.join(root,'netlify/database/migrations/0001_test_payments.sql'),'utf8');
  assert(!/DROP\s+(?:TABLE|SCHEMA)|DELETE\s+FROM|INSERT\s+INTO/i.test(sql),'additive migration, no fake purchases/products');
  assert(sql.includes('REVOKE ALL ON SCHEMA diplomaone_test FROM PUBLIC'));
});
