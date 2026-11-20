// OWNER-OPERATED, read-only connection probe. No products/purchases are seeded
// or modified, no checkout flag changes, no credential or raw SDK error output.
import {firestoreDatabase} from '../src/firestore.mjs';
import {FIRESTORE_ROOT} from '../src/firestore-config.mjs';
let database;
try{
  database=firestoreDatabase();
  await database.doc(FIRESTORE_ROOT).collection('products').limit(1).get();
  console.log(JSON.stringify({mode:'test',database:'firestore',readable:true,checkoutChanged:false}));
}catch(_){
  console.error('Firestore read check failed. Review the private server environment, project/database and service-account IAM. No credentials are logged.');
  process.exitCode=1;
}finally{await database?.terminate();}
