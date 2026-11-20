import assert from 'node:assert/strict';
import {Firestore} from '@google-cloud/firestore';
import {MemoryFirestore} from './memory-firestore.mjs';
import {Repository} from '../src/repository.mjs';
import {FIRESTORE_ROOT} from '../src/firestore-config.mjs';
export const DEMO_PROJECT='demo-diplomaone-payments';
export const usingEmulator=process.env.DIPLOMAONE_TEST_FIRESTORE_EMULATOR==='1';
export function store(){
  if(usingEmulator)assert(/^(127\.0\.0\.1|localhost):\d+$/.test(process.env.FIRESTORE_EMULATOR_HOST||''),'Refuse non-local emulator or real-project tests');
  const database=usingEmulator?new Firestore({projectId:DEMO_PROJECT,databaseId:'(default)',preferRest:true}):new MemoryFirestore();
  return {database,repository:new Repository(database),async reset(){await database.recursiveDelete(database.doc(FIRESTORE_ROOT));}};
}
