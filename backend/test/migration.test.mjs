import {test} from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,mkdir,writeFile,readFile,readdir,stat,symlink,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {spawnSync} from 'node:child_process';
import path from 'node:path';
import {prepareMigration,writeMigration} from '../src/migration.mjs';
import {auditPublicPapers} from '../src/public-audit.mjs';
import {digest} from '../src/domain.mjs';
async function fixture(t){
 const directory=await mkdtemp(path.join(tmpdir(),'diplomaone-offline-migration-'));t.after(()=>rm(directory,{recursive:true,force:true}));
 const source=path.join(directory,'source'),code='DI03000161',subject=path.join(source,code);
 await mkdir(path.join(subject,'summer-2026.assets'),{recursive:true});
 await writeFile(path.join(subject,'summer-2026.html'),'<main><details><summary>Question</summary><div class="answer"><img src="summer-2026.assets/0001.webp">PRIVATE FIXTURE</div></details></main>');
 await writeFile(path.join(subject,'summer-2026.assets/0001.webp'),'fixture');await writeFile(path.join(subject,'summer-2026.solution.pdf'),'%PDF-fixture');
 await mkdir(path.join(source,'DI01000021'));await writeFile(path.join(source,'DI01000021/summer-2026.html'),'FREE FIXTURE');
 const mapping=path.join(directory,'mapping.json');await writeFile(mapping,JSON.stringify({version:1,subjects:{[code]:{title:'Manufacturing I',branch:'mechanical'}}}));
 return {directory,source,subject,mapping};
}
test('offline planner preserves selected codes/sessions and source bytes; never imports or writes in dry run',async t=>{
 const f=await fixture(t),before=await readdir(f.directory),plan=await prepareMigration(f.source,f.mapping);
 assert.equal(plan.mode,'live');assert.equal(plan.products.length,1);assert.equal(plan.products[0].manifest.id,'DI03000161--summer-2026');
 assert.equal(plan.products[0].manifest.branch,'mechanical');assert.equal(plan.products[0].sourceFiles.length,3);
 assert.equal(plan.publicMetadata[0].amount,2900);assert.deepEqual(await readdir(f.directory),before);
 const output=path.join(f.directory,'PRIVATE-export'),journal=await writeMigration(plan,output);
 assert.equal(journal.privateImportApplied,false);assert.equal(journal.products.length,1);
 const filename=path.join(output,'DI03000161--summer-2026/paper.json'),manifest=JSON.parse(await readFile(filename,'utf8'));
 for(const file of plan.products[0].sourceFiles){
  const saved=await readFile(path.join(path.dirname(filename),file.path));assert.equal(digest(saved),file.sha256);
  assert.deepEqual(await readFile(path.join(f.subject,file.path)),saved);
 }
 assert.deepEqual(manifest.files,['summer-2026.html','summer-2026.assets/0001.webp','summer-2026.solution.pdf']);
 assert(!JSON.stringify(plan.publicMetadata).includes('PRIVATE FIXTURE'));
 assert.equal((await stat(filename)).mode&0o777,0o600);
 await assert.rejects(writeMigration(plan,output),{code:'EEXIST'});
});
test('write CLI confines a synthetic private export to real ignored build directories, not public paths or symlink parents',async t=>{
 const f=await fixture(t),root=path.resolve(import.meta.dirname,'../..');await mkdir(path.join(root,'build'),{recursive:true});
 const output=await mkdtemp(path.join(root,'build/migration-cli-test-'));t.after(()=>rm(output,{recursive:true,force:true}));
 const run=destination=>spawnSync(process.execPath,['backend/scripts/prepare-live-migration.mjs',f.source,
  '--mapping='+f.mapping,'--write','--out='+destination],{cwd:root,encoding:'utf8',timeout:15000});
 const safe=run(path.join(output,'safe'));assert.equal(safe.status,0,safe.stderr);assert.equal(JSON.parse(safe.stdout).exported,true);
 assert.equal(JSON.parse(await readFile(path.join(output,'safe/migration.json'),'utf8')).privateImportApplied,false);
 await symlink(f.directory,path.join(output,'linked'));const before=await readdir(f.directory);
 assert.notEqual(run(path.join(output,'linked','forbidden')).status,0);assert.deepEqual(await readdir(f.directory),before);
 assert.notEqual(run(path.join(f.directory,'outside-build')).status,0);assert.deepEqual(await readdir(f.directory),before);
});
test('optional PDFs can be explicitly excluded without removing cards or diagrams',async t=>{
 const f=await fixture(t),plan=await prepareMigration(f.source,f.mapping,{withoutPdfs:true});
 assert.equal(plan.withoutPdfs,true);assert.equal(plan.products[0].sourceFiles.length,2);
 assert(!plan.products[0].manifest.files.some(p=>p.endsWith('.pdf')));
});
test('unknown/ambiguous branch, missing private images, symlinks and PDF-only papers fail before export',async t=>{
 const f=await fixture(t);await writeFile(f.mapping,JSON.stringify({version:1,subjects:{}}));
 await assert.rejects(prepareMigration(f.source,f.mapping),/paper_branch_review_required/);
 await writeFile(f.mapping,JSON.stringify({version:1,subjects:{DI03000161:{title:'Fixture',branch:'mechanical'}}}));
 const asset=path.join(f.subject,'summer-2026.assets/0001.webp');await rm(asset);
 await assert.rejects(prepareMigration(f.source,f.mapping),/missing_private_image/);
 await symlink(path.join(f.subject,'summer-2026.solution.pdf'),asset);
 await assert.rejects(prepareMigration(f.source,f.mapping),/unsupported_asset/);
 await rm(asset);await writeFile(asset,'fixture');await rm(path.join(f.subject,'summer-2026.html'));
 await assert.rejects(prepareMigration(f.source,f.mapping),/question_card_reader_required/);
});
test('launch audit fails on a mistyped/missing checkout and reports root/free-folder symlinks without following them',async t=>{
 const f=await fixture(t);await assert.rejects(auditPublicPapers(path.join(f.directory,'absent-checkout')),{code:'ENOENT'});
 const root=path.join(f.directory,'audit-checkout');await mkdir(root);
 await symlink(f.source,path.join(root,'papers'));
 let audit=await auditPublicPapers(root);assert.equal(audit.ready,false);assert.deepEqual(audit.findings.map(f=>[f.path,f.reason]),[['papers','symlink']]);
 await rm(path.join(root,'papers'));await mkdir(path.join(root,'papers'));
 await symlink(f.subject,path.join(root,'papers/DI01000021'));
 audit=await auditPublicPapers(root);assert.equal(audit.ready,false);assert.deepEqual(audit.findings.map(f=>[f.path,f.reason]),[['papers/DI01000021','symlink']]);
});
test('launch audit distinguishes safe public metadata/free papers from paid HTML/images/PDFs and original source copies',async t=>{
 const f=await fixture(t),plan=await prepareMigration(f.source,f.mapping),output=path.join(f.directory,'private');await writeMigration(plan,output);
 const publicRoot=path.join(output,'public-metadata');
 assert.equal((await auditPublicPapers(publicRoot)).ready,true);
 const metadataPath=path.join(publicRoot,'papers/DI03000161/summer-2026.json'),metadata=JSON.parse(await readFile(metadataPath,'utf8'));
 for(const change of [{amount:1},{title:'',branch:'unknown'},{answer:'never metadata'},{branch:'unknown'}]){
  await writeFile(metadataPath,JSON.stringify({...metadata,...change}));assert.equal((await auditPublicPapers(publicRoot)).ready,false);
 }
 await writeFile(metadataPath,JSON.stringify({version:1,private:true,id:metadata.id}));
 assert.equal((await auditPublicPapers(publicRoot)).ready,true,'minimal publisher listing is safe');
 await mkdir(path.join(publicRoot,'papers/DI01000121'),{recursive:true});await writeFile(path.join(publicRoot,'papers/DI01000121/winter-2025.html'),'FREE');
 assert.equal((await auditPublicPapers(publicRoot)).ready,true);
 const privateCopy=path.join(publicRoot,'papers/DI03000161/summer-2026.html');await writeFile(privateCopy,'PAID ANSWER');
 let audit=await auditPublicPapers(publicRoot);assert.equal(audit.ready,false);assert.equal(audit.historyErased,false);
 assert.deepEqual(audit.findings.map(f=>f.path),['papers/DI03000161/summer-2026.html']);
 assert.equal(audit.findings[0].sha256,digest('PAID ANSWER'));
 await mkdir(path.join(publicRoot,'papers-upload/originals/4351902'),{recursive:true});
 await writeFile(path.join(publicRoot,'papers-upload/originals/4351902/english.html'),'ORIGINAL ANSWERS');
 audit=await auditPublicPapers(publicRoot);assert.equal(audit.findings.length,2);
 await symlink(privateCopy,path.join(publicRoot,'papers/DI03000161/winter-2025.json'));
 assert((await auditPublicPapers(publicRoot)).findings.some(f=>f.reason==='symlink'));
});
