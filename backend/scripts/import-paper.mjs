// OWNER-OPERATED only. Default is a no-network dry run. Never commit private
// manifests/assets or paste Netlify/database credentials into chat.
import {getStore} from '@netlify/blobs';
import {prepareImport,applyImport} from '../src/import.mjs';
import {Repository} from '../src/repository.mjs';
import {firestoreDatabase} from '../src/firestore.mjs';
import {PRIVATE_STORE} from '../src/assets.mjs';

const args=process.argv.slice(2),apply=args.includes('--apply'),file=args.find(a=>!a.startsWith('--'));
if(!file||args.some(a=>a.startsWith('--')&&a!=='--apply')){
  console.error('Usage: npm run import:paper -- /PRIVATE/path/paper.json [--apply]');process.exitCode=1;
}else{
  let database;
  try{
    const prepared=await prepareImport(file);
    console.log(JSON.stringify({mode:'test',dryRun:!apply,productId:prepared.product.id,
      assets:prepared.files.length,bytes:prepared.files.reduce((n,f)=>n+f.bytes,0)}));
    if(apply){
      for(const name of ['NETLIFY_SITE_ID','NETLIFY_AUTH_TOKEN'])if(!process.env[name])throw Error('Owner environment required');
      database=firestoreDatabase();
      const store=getStore({name:PRIVATE_STORE,siteID:process.env.NETLIFY_SITE_ID,token:process.env.NETLIFY_AUTH_TOKEN,consistency:'strong'});
      await applyImport(prepared,{store,repository:new Repository(database)});
      console.log('Private test import verified. Checkout remains controlled by separate server flags.');
    }
  }catch(_){console.error('Import did not complete. Check the private manifest, owner environment and storage/database configuration. No credentials are logged.');process.exitCode=1;}
  finally{await database?.terminate();}
}
