import {test} from 'node:test';
import assert from 'node:assert/strict';
import {generateKeyPair,SignJWT} from 'jose';
import {readConfig,validateProduct,FREE_CODES,PRICES,hmac,validSignature} from '../src/domain.mjs';
import {firebaseVerifier} from '../src/firebase.mjs';
import {razorpayClient} from '../src/razorpay.mjs';
import {privateKey} from '../src/assets.mjs';
import {firestoreDatabase} from '../src/firestore.mjs';
import {firestoreOptions} from '../src/firestore-config.mjs';
import {fixtureFirestoreEnv} from './credentials.mjs';

const secrets={RAZORPAY_KEY_ID:'rzp_test_TestPublic123456',RAZORPAY_KEY_SECRET:'only-a-unit-test-secret-000',
  RAZORPAY_WEBHOOK_SECRET:'only-a-unit-test-webhook-secret-000',...fixtureFirestoreEnv,
  FIREBASE_PROJECT_ID:'diplomaone-53b4e',CONTEXT:'production',PAYMENTS_TEST_ENABLED:'true',PAYMENTS_PRIVATE_MIGRATION_CONFIRMED:'true',PAYMENTS_TESTER_UIDS:'test-user'};

test('configuration fails closed, refuses live keys, and separates preview/production',()=>{
  assert.equal(readConfig({}).enabled,false);
  assert.equal(readConfig(secrets).enabled,true);
  for(const name of Object.keys(secrets))assert.equal(readConfig({...secrets,[name]:''}).enabled,false,name);
  for(const change of [{RAZORPAY_KEY_ID:'rzp_live_LivePublic123456'},{CONTEXT:'deploy-preview'},
    {CONTEXT:'branch-deploy'},{FIREBASE_PROJECT_ID:'diplomaone'},{PAYMENTS_TEST_ENABLED:'TRUE'}])assert.equal(readConfig({...secrets,...change}).enabled,false);
  assert.equal(Object.isFrozen(readConfig(secrets)),true);assert.equal(Object.isFrozen(readConfig(secrets).testers),true);
  assert.equal(readConfig({...secrets,PAYMENTS_TESTER_UIDS:Array.from({length:11},(_,i)=>'user'+i).join(',')}).enabled,false);
  assert.equal(readConfig({...secrets,PAYMENTS_TESTER_UIDS:'u'.repeat(129)}).enabled,false);
});

test('server owns exact per-paper INR/paise pricing and common papers cannot be charged',()=>{
  for(const [branch,amount] of Object.entries(PRICES)){
    const p=validateProduct({id:'DI03000161--summer-2026',title:'Manufacturing Engineering-I',branch,amount:1,currency:'USD'});
    assert.equal(p.amount,amount);assert.equal(p.currency,'INR');
  }
  for(const code of FREE_CODES)assert.throws(()=>validateProduct({id:code+'--summer-2026',title:'Common',branch:'chemical'}),/common_subject_is_free/);
  for(const patch of [{id:'../../private'},{id:'DI03000161--Summer-2026'},{branch:'it'},{title:''}])
    assert.throws(()=>validateProduct({id:'DI03000161--summer-2026',title:'Title',branch:'mechanical',...patch}));
});

test('HMAC signatures are checked as 32-byte digests, not string prefixes',()=>{
  const secret='unit-test-only',body=Buffer.from('{"event":"payment.captured"}'),sig=hmac(secret,body);
  assert(validSignature(secret,body,sig));assert(validSignature(secret,body,sig.toUpperCase()));
  for(const invalid of [null,'',sig.slice(0,-1),sig+'0','g'.repeat(64),sig+', '+sig,sig+'\n'])assert(!validSignature(secret,body,invalid));
  assert(!validSignature(secret,Buffer.concat([body,Buffer.from(' ')]),sig));assert(!validSignature('other-secret',body,sig));
});

test('Firebase token verification needs the exact project, issuer, signature, claims and Google provider',async()=>{
  const {publicKey,privateKey}=await generateKeyPair('RS256');
  const {privateKey:wrongKey}=await generateKeyPair('RS256');
  const now=Math.floor(Date.UTC(2026,9,30)/1000),project='diplomaone-53b4e';
  const claims={sub:'google-user',aud:project,iss:'https://securetoken.google.com/'+project,iat:now,exp:now+3600,
    auth_time:now-30,firebase:{sign_in_provider:'google.com'}};
  const verifier=firebaseVerifier(project,publicKey,()=>now*1000);
  const sign=(patch={},key=privateKey)=>new SignJWT({...claims,...patch}).setProtectedHeader({alg:'RS256'}).sign(key);
  assert.deepEqual(await verifier('Bearer '+await sign()),{uid:'google-user'});
  for(const patch of [{sub:''},{sub:'u'.repeat(129)},{aud:'diplomaone'},{aud:[project]},
    {iss:'https://evil.invalid/'+project},{exp:now-30},{iat:now+100},{auth_time:now+100},
    {auth_time:-1},{auth_time:undefined},{exp:undefined},{firebase:{sign_in_provider:'anonymous'}}])
    await assert.rejects(verifier('Bearer '+await sign(patch)),/invalid_or_expired_session/);
  await assert.rejects(verifier('Bearer '+await sign({},wrongKey)),/invalid_or_expired_session/);
  for(const authorization of [null,'','Basic abc','bearer '+await sign(),'Bearer '+('x'.repeat(17000))])
    await assert.rejects(verifier(authorization),/sign_in_required/);
  assert.throws(()=>firebaseVerifier('diplomaone'),/Unexpected Firebase/);
});

test('provider client uses test-only Basic auth, INR and receipt from server, with no redirect or money-moving fallback',async()=>{
  const calls=[],config=readConfig(secrets);
  const provider=razorpayClient(config,async(url,options)=>{calls.push({url,options});return {ok:true,json:async()=>({id:'order_example'})};});
  await provider.createOrder({amount:2900,receipt:'dt_server_receipt'});
  assert.equal(calls[0].url,'https://api.razorpay.com/v1/orders');assert.equal(calls[0].options.redirect,'error');
  assert.equal(calls[0].options.headers.Authorization,'Basic '+Buffer.from(config.keyId+':'+config.keySecret).toString('base64'));
  assert.deepEqual(JSON.parse(calls[0].options.body),{amount:2900,currency:'INR',receipt:'dt_server_receipt',partial_payment:false});
  await provider.order('order_12345');await provider.payment('pay_12345');
  assert.equal(calls[1].options.method,'GET');assert.equal(calls[2].options.method,'GET');
  assert.equal(provider.refund,undefined);assert.equal(provider.capture,undefined);
  assert.throws(()=>provider.order('../payments'),/invalid_order/);
  assert.throws(()=>razorpayClient({...config,keyId:'rzp_live_NotPermitted'}),/test_keys_required/);
  const failing=razorpayClient(config,async()=>{throw Error('private provider detail');});
  await assert.rejects(failing.order('order_12345'),error=>error.code==='payment_provider_unavailable'&&!error.message.includes('private'));
});

test('private file paths are content-addressed and Firestore uses explicit project credentials',async()=>{
  assert.equal(privateKey('DI03000161--summer-2026','a'.repeat(64)),'DI03000161--summer-2026/'+'a'.repeat(64));
  assert.throws(()=>privateKey('../private','a'.repeat(64)));
  assert.throws(()=>privateKey('DI03000161--summer-2026','../reader.html'));
  assert.throws(()=>firestoreDatabase({}),/firestore_not_configured/);
  if(process.env.FIRESTORE_EMULATOR_HOST)assert.throws(()=>firestoreDatabase(fixtureFirestoreEnv),/firestore_not_configured/);
  else{
    const database=firestoreDatabase(fixtureFirestoreEnv);
    assert.equal(database.projectId,'diplomaone-53b4e');assert.equal(database.databaseId,'(default)');
    await database.terminate();
  }
});


test('Firestore credential parsing is strict, TLS-pinned, private and rejects emulator/other projects',()=>{
  const options=firestoreOptions(fixtureFirestoreEnv);
  assert.equal(options.ssl,true);assert.equal(options.apiEndpoint,'firestore.googleapis.com');assert.equal(options.preferRest,true);
  assert.equal(firestoreOptions({...fixtureFirestoreEnv,FIREBASE_PRIVATE_KEY:fixtureFirestoreEnv.FIREBASE_PRIVATE_KEY.replaceAll('\n','\\n')}).credentials.private_key,options.credentials.private_key);
  for(const change of [{FIREBASE_PROJECT_ID:'diplomaone'},
    {FIREBASE_CLIENT_EMAIL:'other@diplomaone.iam.gserviceaccount.com'},
    {FIREBASE_CLIENT_EMAIL:'https://evil.invalid/'},{FIREBASE_PRIVATE_KEY:'not a private key'},
    {FIREBASE_PRIVATE_KEY:'x'.repeat(20000)},{FIRESTORE_EMULATOR_HOST:'127.0.0.1:8085'},
    {FIRESTORE_DATABASE_ID:'another-database'}]){
    assert.equal(firestoreOptions({...fixtureFirestoreEnv,...change}),null);
    assert.equal(readConfig({...secrets,...change}).configured,false);
  }
});
