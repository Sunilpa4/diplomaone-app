import {firestoreDatabase} from './firestore.mjs';
import {getStore} from '@netlify/blobs';
import {readConfig} from './domain.mjs';
import {PRIVATE_STORE,privateAssets} from './assets.mjs';
export {PRIVATE_STORE,privateKey} from './assets.mjs';
import {Repository} from './repository.mjs';
import {firebaseVerifier} from './firebase.mjs';
import {razorpayClient} from './razorpay.mjs';
import {createHandler} from './api.mjs';

export function productionHandler(env=process.env){
  const config=readConfig(env);
  let repository=null,provider=null,assets=null;
  if(config.configured){
    repository=new Repository(firestoreDatabase(env));
    provider=razorpayClient(config);
    assets=privateAssets(()=>getStore({name:PRIVATE_STORE,consistency:'strong'}));
  }
  return createHandler({config,repository,provider,assets,verifyIdentity:firebaseVerifier(config.firebaseProject),
    log:code=>console.warn('test_payments',code)});
}
