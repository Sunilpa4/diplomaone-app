// Offline test runner only, never bundled/deployed. Preserve the first failing
// exit code and expose safe fixture diagnostics via GitHub's annotation API.
import {spawnSync} from 'node:child_process';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const website=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
for(const test of ['test_auth.js','test_connection.js','test_payments.js','test_account.js','test_purchase_ui.js']){
 const result=spawnSync(process.execPath,[path.join(website,test)],{cwd:website,encoding:'utf8',timeout:120000});
 process.stdout.write(result.stdout||'');process.stderr.write(result.stderr||'');
 if(result.status!==0){
  const failures=(result.stdout||'').match(/^not ok [\s\S]*?(?=^# Subtest:|^1\.\.|$(?![\s\S]))/gm)||[];
  const detail=('Offline frontend '+test+': '+(failures.join('\n')||result.stderr||result.error?.message||'Test exited without a success status')).slice(-12000);
  console.error('::error::'+detail.replaceAll('%','%25').replaceAll('\r','%0D').replaceAll('\n','%0A'));
  process.exit(result.status||1);
 }
}
