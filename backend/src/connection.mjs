import {Problem} from './domain.mjs';
import {FIRESTORE_ROOT} from './firestore-config.mjs';

// A bounded READ ONLY setup probe. Call only after the API has verified the
// exact test origin, production context, Google identity and tester allowlist.
// No provider, repository transaction, document write, seeding or rule change.
export function firestoreConnectionCheck(getDatabase,{clock=()=>Date.now(),cooldownMs=30000}={}){
  let busy=false,nextAllowed=-Infinity;
  return async()=>{
    const now=clock();
    // Best-effort per-instance protection only, NOT a distributed billing cap.
    if(busy||now<nextAllowed)throw new Problem(429,'connection_check_rate_limited');
    busy=true;nextAllowed=now+cooldownMs;
    try{
      await getDatabase().doc(FIRESTORE_ROOT).collection('products').limit(1).get();
      // Do not read/return document contents or infer IAM write/payment access.
    }catch(_){throw new Problem(503,'firestore_check_failed');}
    finally{busy=false;}
  };
}
