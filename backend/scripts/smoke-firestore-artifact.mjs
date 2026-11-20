// Emulator-only dynamic SDK/proto smoke FROM THE ACTUAL EXTRACTED ZIP.
// Built-ins only; it refuses any non-loopback host and always uses a demo ID.
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {readFile,realpath} from 'node:fs/promises';
import path from 'node:path';
import {randomUUID} from 'node:crypto';
assert(/^(127\.0\.0\.1|localhost):\d+$/.test(process.env.FIRESTORE_EMULATOR_HOST||''),'A local Firestore emulator is required');
const directory=await realpath(process.argv[2]);
const entry=await readFile(path.join(directory,'___netlify-entry-point.mjs'),'utf8');
const main=/getLambdaHandler\((['"])(\.\/[^'"]+)\1\)/.exec(entry);
assert(main);
const require=createRequire(path.resolve(directory,main[2]));
assert((await realpath(require.resolve('@google-cloud/firestore'))).startsWith(directory+path.sep));
const {Firestore}=require('@google-cloud/firestore');
const db=new Firestore({projectId:'demo-diplomaone-payments',databaseId:'(default)',universeDomain:'googleapis.com',preferRest:false});
const id=randomUUID(),ref=db.doc('diplomaone_test/artifact_smoke/probes/'+id);
try{
  await ref.set({counter:0,probe:id});
  await db.runTransaction(async tx=>{const doc=await tx.get(ref);tx.update(ref,{counter:doc.data().counter+1});});
  const result=await ref.get();assert.equal(result.data().counter,1);
  assert.equal((await ref.parent.where('probe','==',id).get()).docs.length,1);
  await ref.delete();
  console.log('Actual ZIP Firestore SDK: local demo-emulator read/write/query/transaction/delete passed');
}finally{await db.terminate();}
