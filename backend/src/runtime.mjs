import {firestoreDatabase} from './firestore.mjs';
import {getStore} from '@netlify/blobs';
import {readConfig} from './domain.mjs';
import {PRIVATE_STORE,privateAssets} from './assets.mjs';
export {PRIVATE_STORE,privateKey} from './assets.mjs';
import {Repository} from './repository.mjs';
import {firebaseVerifier} from './firebase.mjs';
import {razorpayClient} from './razorpay.mjs';
import {createHandler} from './api.mjs';
import {firestoreConnectionCheck} from './connection.mjs';

export function productionHandler(env=process.env,mode='test'){
  const config=readConfig(env,mode);
  let repository=null,provider=null,assets=null,database=null;
  const getDatabase=()=>database??=firestoreDatabase(env);
  if(config.configured||(mode==='live'&&config.firestoreConfigured)){
    repository=new Repository(getDatabase(),{mode});
    if(config.configured)provider=razorpayClient(config);
    assets=privateAssets(()=>getStore({name:mode==='live'?'diplomaone-private-live':PRIVATE_STORE,consistency:'strong'}));
  }
  return createHandler({config,repository,provider,assets,verifyIdentity:firebaseVerifier(config.firebaseProject),
    connectionCheck:firestoreConnectionCheck(getDatabase),log:code=>console.warn(mode+'_payments',code)});
}
