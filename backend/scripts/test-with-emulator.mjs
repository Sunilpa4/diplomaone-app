// Invoked by the pinned local-emulator runner, never a real Firebase project.
import assert from 'node:assert/strict';
import {readdir} from 'node:fs/promises';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
assert(/^(127\.0\.0\.1|localhost):\d+$/.test(process.env.FIRESTORE_EMULATOR_HOST||''),'Refuse tests without a loopback emulator');
const env={...process.env,DIPLOMAONE_TEST_FIRESTORE_EMULATOR:'1'};
// Files share one demo namespace, so run files sequentially; tests within a
// file explicitly exercise concurrent callbacks/reservations where intended.
const tests=(await readdir(path.join(root,'backend/test'))).filter(n=>n.endsWith('.test.mjs')).sort().map(n=>'backend/test/'+n);
for(const args of [['--test','--test-concurrency=1',...tests],['backend/scripts/check-bundle.mjs']]){
  const result=spawnSync(process.execPath,args,{cwd:root,env,encoding:'utf8',timeout:480000});
  process.stdout.write(result.stdout||'');process.stderr.write(result.stderr||'');
  if(result.status!==0){
    const failures=(result.stdout||'').match(/^not ok [\s\S]*?(?=^# Subtest:|^1\.\.|$(?![\s\S]))/gm)||[];
    const detail=(failures.join('\n')||result.stderr||result.error?.message||'See emulator/test logs').slice(-14000);
    console.error('::error::Firestore DEMO emulator validation failed: '+detail.replaceAll('%','%25').replaceAll('\r','%0D').replaceAll('\n','%0A'));
    process.exit(result.status||1);
  }
}
