import {test} from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,writeFile,rm,symlink,mkdir} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {prepareImport,applyImport} from '../src/import.mjs';
import {digest,MAX_ASSET_BYTES} from '../src/domain.mjs';

async function fixture(t,changes={},html='<main><details><summary>Unit test fixture</summary><p>Not a real published answer</p></details></main>'){
  const dir=await mkdtemp(path.join(tmpdir(),'diplomaone-private-test-'));
  t.after(()=>rm(dir,{recursive:true,force:true}));
  const manifest={version:1,id:'DI03000161--summer-2026',title:'Manufacturing Engineering-I',branch:'mechanical',reader:'reader.html',files:['reader.html'],...changes};
  await writeFile(path.join(dir,'reader.html'),html);
  const file=path.join(dir,'manifest.json');await writeFile(file,JSON.stringify(manifest));
  return {dir,file,manifest};
}

test('private import preserves exact source bytes, hashes and explicit branch identity without fabricating content',async t=>{
  const f=await fixture(t),prepared=await prepareImport(f.file);
  assert.equal(prepared.product.id,f.manifest.id);assert.equal(prepared.product.branch,'mechanical');
  assert.equal(prepared.files.length,1);assert.equal(prepared.product.reader_asset,digest(prepared.files[0].content));
  assert.equal(prepared.product.assets[0].content,undefined);
  assert.equal(prepared.product.assets[0].mime,'text/plain; charset=utf-8');
});

test('default owner command is a no-network dry run and never echoes credentials',async t=>{
  const f=await fixture(t);
  const result=spawnSync(process.execPath,[new URL('../scripts/import-paper.mjs',import.meta.url).pathname,f.file],{
    encoding:'utf8',env:{...process.env,NETLIFY_AUTH_TOKEN:'DO_NOT_PRINT_TOKEN',FIREBASE_CLIENT_EMAIL:'DO_NOT_PRINT_EMAIL',FIREBASE_PRIVATE_KEY:'DO_NOT_PRINT_KEY'}});
  assert.equal(result.status,0,result.stderr);assert(result.stdout.includes('"dryRun":true'));
  assert(!result.stdout.includes('DO_NOT_PRINT'));assert(!result.stderr.includes('DO_NOT_PRINT'));
});

test('owner read-only Firestore probe refuses invalid setup without printing secrets',()=>{
  const result=spawnSync(process.execPath,[new URL('../scripts/check-firestore.mjs',import.meta.url).pathname],{
    encoding:'utf8',env:{PATH:process.env.PATH,FIREBASE_PROJECT_ID:'diplomaone-53b4e',FIREBASE_CLIENT_EMAIL:'DO_NOT_PRINT_EMAIL',FIREBASE_PRIVATE_KEY:'DO_NOT_PRINT_KEY'}});
  assert.equal(result.status,1);assert(result.stderr.includes('Firestore read check failed'));
  assert(!result.stdout.includes('DO_NOT_PRINT'));assert(!result.stderr.includes('DO_NOT_PRINT'));
});

test('assets must upload and strong-read verify before a product can be activated',async t=>{
  const f=await fixture(t),prepared=await prepareImport(f.file),saved=new Map(),steps=[];
  await applyImport(prepared,{store:{async set(key,bytes){steps.push('set');saved.set(key,bytes);},
    async get(key){steps.push('verify');return new Uint8Array(saved.get(key)).buffer;}},repository:{async importProduct(p){steps.push('activate');assert.equal(p.id,f.manifest.id);}}});
  assert.deepEqual(steps,['set','verify','activate']);
  let activated=false;
  await assert.rejects(applyImport(prepared,{store:{async set(){},async get(){return new Uint8Array([1]).buffer;}},
    repository:{async importProduct(){activated=true;}}}),/private_upload_not_verified/);
  assert.equal(activated,false);
});

test('common free subjects, unsupported branches and duplicate/missing reader paths are rejected',async t=>{
  for(const patch of [{id:'DI01000021--summer-2026'},{id:'DI01000121--winter-2025'},{branch:'it'},
    {files:['reader.html','reader.html']},{reader:'absent.html'},{version:2},{files:[]}]){
    const f=await fixture(t,patch);await assert.rejects(prepareImport(f.file));
  }
});

test('import cannot escape its private folder or read symlinked external files',async t=>{
  for(const name of ['../reader.html','/etc/passwd','dir/../reader.html','a\\reader.html','reader.html?token=x','%2e%2e/reader.html']){
    const f=await fixture(t,{files:[name]});await assert.rejects(prepareImport(f.file),/invalid_asset_path/);
  }
  const f=await fixture(t,{files:['reader.html','outside.png']});
  const outside=await fixture(t);await symlink(path.join(outside.dir,'reader.html'),path.join(f.dir,'outside.png'));
  await assert.rejects(prepareImport(f.file),/asset_outside_import/);
});

test('old PDF frames, non-card documents and missing/private-external image references fail import',async t=>{
  for(const [html,code] of [
    ['<main><iframe src="paper.pdf"></iframe></main>','question_card_reader_required'],
    ['<main>PDF placeholder only</main>','question_card_reader_required'],
    ['<main><details><img src="missing.png"></details></main>','missing_private_image'],
    ['<main><details><img src="https://public.invalid/answers.png"></details></main>','image_must_be_private'],
    ['<main><details><img src="//public.invalid/answers.png"></details></main>','image_must_be_private'],
    ['<main><details><img src="image.png" srcset="public.png 2x"></details></main>','unsupported_image_reference'],
  ]){
    const f=await fixture(t,{},html);await assert.rejects(prepareImport(f.file),new RegExp(code));
  }
});

test('all relative reader diagrams must be included, retaining nested asset paths',async t=>{
  const html='<main><details><img src="reader.assets/diagram.png"></details></main>';
  const f=await fixture(t,{files:['reader.html','reader.assets/diagram.png']},html);
  await mkdir(path.join(f.dir,'reader.assets'));await writeFile(path.join(f.dir,'reader.assets/diagram.png'),Buffer.from('unit-test-image-bytes'));
  const prepared=await prepareImport(f.file);assert.equal(prepared.product.assets.length,2);
  assert.equal(prepared.product.assets[1].path,'reader.assets/diagram.png');
});

test('unsupported active assets and over-limit files cannot be made purchasable',async t=>{
  const f=await fixture(t,{files:['reader.html','active.svg']});await writeFile(path.join(f.dir,'active.svg'),'<svg><script>bad()</script></svg>');
  await assert.rejects(prepareImport(f.file),/unsupported_asset/);
  const big=await fixture(t,{files:['reader.html','huge.pdf']});await writeFile(path.join(big.dir,'huge.pdf'),Buffer.alloc(MAX_ASSET_BYTES+1));
  await assert.rejects(prepareImport(big.file),/unsupported_asset/);
});
