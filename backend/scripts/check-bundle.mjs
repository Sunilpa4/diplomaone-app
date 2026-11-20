// Use Netlify's ACTUAL v2 packager (NFT + generated Lambda entry), not a
// standalone esbuild approximation. Never deploy or call a payment provider.
import assert from 'node:assert/strict';
import {zipFunctions} from '@netlify/zip-it-and-ship-it';
import {mkdir,mkdtemp,rm} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {execFileSync,spawnSync} from 'node:child_process';
import {generateKeyPairSync} from 'node:crypto';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const settings=JSON.parse(execFileSync('python3',['-c',
  "import json,tomllib;print(json.dumps(tomllib.load(open('netlify.toml','rb'))))"],{cwd:root,encoding:'utf8'}));
assert.equal(settings.build.functions,'netlify/functions');
const source=path.resolve(root,settings.build.functions),destination=path.join(root,'build/payments-netlify-package');
await mkdir(destination,{recursive:true});
const archives=await zipFunctions(source,destination,{archiveFormat:'zip',basePath:root,repositoryRoot:root,
  config:{'*':{nodeBundler:settings.functions.node_bundler,nodeVersion:settings.build.environment.NODE_VERSION}},
  manifest:path.join(destination,'manifest.json')});
assert.equal(archives.length,1);
const artifact=archives[0];
assert.equal(artifact.name,'payments');assert.equal(artifact.runtimeAPIVersion,2);
assert.equal(artifact.runtimeVersion,'nodejs22.x');
assert.equal(artifact.entryFilename,'___netlify-entry-point.mjs');
assert(artifact.routes.some(route=>route.pattern==='/api/payments/test/*'));
console.log(`Actual Netlify packager selected ${artifact.bundler} (${artifact.bundlerReason||'v2'}); archive ${artifact.size} bytes`);

const isolated=await mkdtemp(path.join(tmpdir(),'diplomaone-netlify-artifact-'));
try{
  // Archive inspection/extraction uses only Python's standard library. The
  // runtime subprocess cannot reach this checkout's node_modules via ancestors.
  execFileSync('python3',['-c',`
import sys
from pathlib import PurePosixPath
from zipfile import ZipFile
with ZipFile(sys.argv[1]) as z:
 names=z.namelist()
 for name in names:
  p=PurePosixPath(name)
  assert not p.is_absolute() and '..' not in p.parts, name
  assert not any(part in ('.env','.secrets','papers-upload','content','test','tests','@electric-sql') for part in p.parts), name
  assert not name.startswith(('backend/','website/')), name
 for package in ('@google-cloud/firestore','jose','@netlify/blobs'):
  assert 'node_modules/'+package+'/package.json' in names, 'Runtime dependency missing from ZIP: '+package
 z.extractall(sys.argv[2])
`,artifact.path,isolated]);
  const baseEnv={PATH:process.env.PATH,NODE_ENV:'production'};
  const fixtureKey=generateKeyPairSync('rsa',{modulusLength:2048,privateKeyEncoding:{format:'pem',type:'pkcs8'},publicKeyEncoding:{format:'pem',type:'spki'}}).privateKey;
  const firestoreEnv={...baseEnv,CONTEXT:'production',FIREBASE_PROJECT_ID:'diplomaone-53b4e',
    FIREBASE_CLIENT_EMAIL:'artifact-fixture@diplomaone-53b4e.iam.gserviceaccount.com',FIREBASE_PRIVATE_KEY:fixtureKey,PAYMENTS_TESTER_UIDS:'unit-test-user',
    PAYMENTS_TEST_ENABLED:'false',PAYMENTS_PRIVATE_MIGRATION_CONFIRMED:'false'};
  const cases=[{name:'no-secret',env:baseEnv},{name:'firestore-only-disabled',env:firestoreEnv},
    {name:'configured-disabled',env:{...firestoreEnv,RAZORPAY_KEY_ID:'rzp_test_UnitFixture12345',
      RAZORPAY_KEY_SECRET:'unit-fixture-key-secret-not-real',RAZORPAY_WEBHOOK_SECRET:'unit-fixture-webhook-secret-not-real-0000'}}];
  for(const scenario of cases){
    const result=spawnSync(process.execPath,[path.join(root,'backend/scripts/smoke-artifact.mjs'),isolated,scenario.name],
      {cwd:isolated,encoding:'utf8',env:scenario.env,timeout:20000});
    process.stdout.write(result.stdout||'');process.stderr.write(result.stderr||'');
    assert.equal(result.status,0,`Isolated Netlify archive smoke failed (${scenario.name})`);
  }
  if(process.env.DIPLOMAONE_TEST_FIRESTORE_EMULATOR==='1'){
    const result=spawnSync(process.execPath,[path.join(root,'backend/scripts/smoke-firestore-artifact.mjs'),isolated],
      {cwd:isolated,encoding:'utf8',env:{...baseEnv,FIRESTORE_EMULATOR_HOST:process.env.FIRESTORE_EMULATOR_HOST},timeout:30000});
    process.stdout.write(result.stdout||'');process.stderr.write(result.stderr||'');
    assert.equal(result.status,0,'Packaged Firestore SDK could not transact against the local demo emulator');
  }
}finally{await rm(isolated,{recursive:true,force:true});}
