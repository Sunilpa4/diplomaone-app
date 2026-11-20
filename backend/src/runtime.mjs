import pg from 'pg';
import {getStore} from '@netlify/blobs';
import {readConfig} from './domain.mjs';
import {PRIVATE_STORE,privateAssets} from './assets.mjs';
export {PRIVATE_STORE,privateKey} from './assets.mjs';
import {Repository,pgDatabase} from './repository.mjs';
import {firebaseVerifier} from './firebase.mjs';
import {razorpayClient} from './razorpay.mjs';
import {createHandler} from './api.mjs';

export function databasePool(url){
  const parsed=new URL(url);
  if(!['postgres:','postgresql:'].includes(parsed.protocol))throw new Error('Invalid database protocol');
  // Never use rejectUnauthorized:false or NODE_TLS_REJECT_UNAUTHORIZED=0.
  parsed.searchParams.set('sslmode','verify-full');
  return new pg.Pool({connectionString:parsed.toString(),max:2,connectionTimeoutMillis:5000,
    idleTimeoutMillis:10000,statement_timeout:5000,query_timeout:6000});
}
export function productionHandler(env=process.env){
  const config=readConfig(env);
  let repository=null,provider=null,assets=null;
  if(config.configured){
    repository=new Repository(pgDatabase(databasePool(env.NETLIFY_DB_URL)));
    provider=razorpayClient(config);
    assets=privateAssets(()=>getStore({name:PRIVATE_STORE,consistency:'strong'}));
  }
  return createHandler({config,repository,provider,assets,verifyIdentity:firebaseVerifier(config.firebaseProject),
    log:code=>console.warn('test_payments',code)});
}
