import {test} from 'node:test';
import assert from 'node:assert/strict';
import {generateKeyPair,SignJWT} from 'jose';
import {createHandler} from '../src/api.mjs';
import {firestoreConnectionCheck} from '../src/connection.mjs';
import {firebaseVerifier} from '../src/firebase.mjs';
import {Problem,PREFIX,TEST_SITE_ORIGIN,readConfig} from '../src/domain.mjs';
import {FIRESTORE_ROOT} from '../src/firestore-config.mjs';
import {fixtureFirestoreEnv} from './credentials.mjs';

// All identities, keys and database responses here are locally generated test
// fixtures. No real Firebase project, JWK endpoint, IAM or provider is called.
const setup={...fixtureFirestoreEnv,CONTEXT:'production',PAYMENTS_TESTER_UIDS:'approved-fixture',
  PAYMENTS_TEST_ENABLED:'false',PAYMENTS_PRIVATE_MIGRATION_CONFIRMED:'false'};
const success={mode:'test',database:'firestore',readable:true,readOnly:true,checkoutEnabled:false,paymentsVerified:false};
function fixture({env={},probe,verifier}={}){
  const calls={verify:0,probe:0,other:0},logs=[];
  const unused=new Proxy({}, {get(){++calls.other;throw Error('Do not use a payment/storage/repository adapter');}});
  const config=readConfig({...setup,...env});
  const handler=createHandler({config,repository:unused,provider:unused,assets:unused,
    verifyIdentity:async header=>{++calls.verify;
      if(verifier)return verifier(header);
      if(!['Bearer fixture-approved','Bearer fixture-other'].includes(header))throw new Problem(401,'sign_in_required');
      return {uid:header==='Bearer fixture-approved'?'approved-fixture':'uninvited-fixture'};},
    connectionCheck:probe===null?undefined:async()=>{++calls.probe;return probe?probe():{uid:'NEVER_ECHO',email:'NEVER_ECHO',document:'NEVER_ECHO'};},
    log:code=>logs.push(code)});
  async function request(path='/connection',{method='POST',url=TEST_SITE_ORIGIN+PREFIX+path,
    origin=new URL(url).origin,authorization='Bearer fixture-approved',body='{}',headers={}}={}){
    const response=await handler(new Request(url,{method,headers:{'Content-Type':'application/json',
      ...(origin!==null?{Origin:origin}:{}),...(authorization!==null?{Authorization:authorization}:{}),...headers},
      ...(!['GET','HEAD'].includes(method)&&body!==null?{body:typeof body==='string'?body:JSON.stringify(body)}:{})}));
    return {status:response.status,headers:response.headers,body:await response.json()};
  }
  return {config,calls,logs,request};
}
function queryFixture(get=async()=>({docs:[{data(){throw Error('Probe must not inspect document contents');}}]})){
  const calls=[];
  const database={doc(root){calls.push(['doc',root]);return {
    collection(name){calls.push(['collection',name]);return {limit(n){calls.push(['limit',n]);return {
      get(){calls.push(['get']);return get();}
    };}};}
  };}};
  return {calls,database,probe:options=>firestoreConnectionCheck(()=>database,options)};
}
const problem=(status,code)=>error=>error instanceof Problem&&error.status===status&&error.code===code&&error.message===code;

test('diagnostic configuration is independent of Razorpay and fails closed for partial/on/invalid flags',()=>{
  const config=readConfig(setup);
  assert.equal(config.firestoreConfigured,true);assert.equal(config.configured,false);assert.equal(config.enabled,false);
  assert.equal(config.checkoutFlagsOff,true);
  for(const field of ['PAYMENTS_TEST_ENABLED','PAYMENTS_PRIVATE_MIGRATION_CONFIRMED']){
    for(const value of ['true','TRUE','False','0',' false ',null])assert.equal(readConfig({...setup,[field]:value}).checkoutFlagsOff,false);
    for(const value of ['false','',undefined])assert.equal(readConfig({...setup,[field]:value}).checkoutFlagsOff,true);
  }
  assert.equal(readConfig({...setup,FIREBASE_PRIVATE_KEY:''}).firestoreConfigured,false);
  assert.equal(readConfig({...setup,FIRESTORE_DATABASE_ID:'other'}).firestoreConfigured,false);
});

test('approved manual check returns only bounded safe status without Razorpay credentials or payment adapters',async()=>{
  const f=fixture(),result=await f.request();
  assert.equal(result.status,200);assert.deepEqual(result.body,success);
  assert(JSON.stringify(result.body).length<200);assert(!JSON.stringify(result.body).includes('NEVER_ECHO'));
  assert.equal(result.headers.get('Cache-Control'),'private, no-store');
  assert.equal(result.headers.get('Vary'),'Authorization, Origin');assert.equal(result.headers.get('X-Content-Type-Options'),'nosniff');
  assert.equal(result.headers.get('Access-Control-Allow-Origin'),null);assert.equal(result.headers.get('Set-Cookie'),null);
  assert.deepEqual(f.calls,{verify:1,probe:1,other:0});assert.deepEqual(f.logs,[]);
});

test('anonymous, invalid and uninvited callers cannot trigger the diagnostic read',async()=>{
  const f=fixture();
  for(const authorization of [null,'','Basic fixture-approved','Bearer invalid']){
    const result=await f.request('/connection',{authorization});assert.equal(result.status,401);assert.equal(result.body.error,'sign_in_required');
  }
  const denied=await f.request('/connection',{authorization:'Bearer fixture-other'});
  assert.equal(denied.status,403);assert.deepEqual(denied.body,{mode:'test',error:'tester_not_allowed'});
  assert.equal(f.calls.probe,0);assert.equal(f.calls.other,0);
});

test('empty, malformed and oversized tester allowlists never authorize a read',async()=>{
  for(const testers of ['',Array.from({length:11},(_,i)=>'fixture-'+i).join(','),'u'.repeat(129),'approved-fixture,invalid\nuid']){
    const f=fixture({env:{PAYMENTS_TESTER_UIDS:testers}}),result=await f.request();
    assert.equal(result.status,403);assert.equal(result.body.error,'tester_not_allowed');assert.equal(f.calls.probe,0);
  }
});

test('wrong deployment context, URL host and scheme are rejected before authentication/database access',async()=>{
  for(const context of ['',undefined,'deploy-preview','branch-deploy','dev','Production']){
    const f=fixture({env:{CONTEXT:context}}),result=await f.request();
    assert.equal(result.status,404);assert.equal(result.body.error,'connection_check_unavailable');
    assert.deepEqual(f.calls,{verify:0,probe:0,other:0});
  }
  for(const origin of ['https://www.diplomaone.in','https://unit-test.netlify.app',
    'https://deploy-preview-37--vermillion-pothos-520a34.netlify.app',
    'https://old-id--vermillion-pothos-520a34.netlify.app','https://vermillion-pothos-520a34.netlify.app.evil.invalid',
    'http://vermillion-pothos-520a34.netlify.app','https://vermillion-pothos-520a34.netlify.app:444']){
    const f=fixture(),result=await f.request('/connection',{url:origin+PREFIX+'/connection',
      headers:{'X-Forwarded-Host':'vermillion-pothos-520a34.netlify.app','X-Forwarded-Proto':'https'}});
    assert.equal(result.status,origin.startsWith('http:')?400:404,origin);
    assert.deepEqual(f.calls,{verify:0,probe:0,other:0});
  }
});

test('same-origin POST is mandatory; links, preflights and cross-origin forms cannot trigger a read',async()=>{
  const f=fixture();
  for(const method of ['GET','HEAD','OPTIONS','PUT','PATCH','DELETE']){
    const result=await f.request('/connection',{method});assert.equal(result.status,405);assert.equal(result.body.error,'method_not_allowed');
  }
  for(const origin of [null,'','null','https://evil.invalid','http://vermillion-pothos-520a34.netlify.app']){
    const result=await f.request('/connection',{origin});assert.equal(result.status,403);
  }
  assert.deepEqual(f.calls,{verify:0,probe:0,other:0});
});

test('URL query tokens, ambiguous paths and non-JSON/oversized/arbitrary request fields are refused',async()=>{
  const f=fixture();
  for(const path of ['/connection?token=NEVER_ECHO','/connection?uid=approved-fixture','/connection%2fprivate','/connection%5cprivate']){
    const result=await f.request(path);assert.equal(result.status,404);assert.equal(f.calls.probe,0);
  }
  for(const body of ['null','[]','false','1','"fixture"','{"broken":','',
    {uid:'approved-fixture'},{email:'private@example.test'},{collection:'products'},{productId:'private'},{limit:100},{token:'NEVER_ECHO'}]){
    const result=await f.request('/connection',{body});assert.equal(result.status,400);assert.equal(f.calls.probe,0);
  }
  for(const mime of ['text/plain','application/x-www-form-urlencoded','multipart/form-data']){
    assert.equal((await f.request('/connection',{headers:{'Content-Type':mime}})).status,415);
  }
  assert.equal((await f.request('/connection',{body:'x'.repeat(4097)})).status,413);
  assert.equal((await f.request('/connection',{headers:{'Content-Length':'5000'}})).status,413);
  assert.equal(f.calls.probe,0);assert.equal(f.calls.other,0);
});

test('either on/partial/invalid checkout flag blocks the check without a database or provider call',async()=>{
  for(const field of ['PAYMENTS_TEST_ENABLED','PAYMENTS_PRIVATE_MIGRATION_CONFIRMED'])for(const value of ['true','TRUE','invalid']){
    const f=fixture({env:{[field]:value}}),result=await f.request();
    assert.equal(result.status,409);assert.equal(result.body.error,'disable_test_checkout');
    assert.deepEqual(f.calls,{verify:1,probe:0,other:0});
  }
});

test('authorized setup errors are safe and no missing/invalid configuration causes a database attempt',async()=>{
  for(const change of [{FIREBASE_PROJECT_ID:'other'},{FIREBASE_CLIENT_EMAIL:''},{FIREBASE_PRIVATE_KEY:''},
    {FIRESTORE_DATABASE_ID:'other'},{FIRESTORE_EMULATOR_HOST:'127.0.0.1:8085'}]){
    const f=fixture({env:change}),result=await f.request();
    assert.equal(result.status,503);assert.deepEqual(result.body,{mode:'test',error:'firestore_not_configured'});
    assert.equal(f.calls.probe,0);assert.equal(f.calls.other,0);
    assert.equal((await f.request('/connection',{authorization:null})).status,401,'no configuration dump for an anonymous caller');
  }
  const f=fixture({probe:null}),result=await f.request();
  assert.equal(result.status,503);assert.equal(result.body.error,'connection_check_unavailable');assert.equal(f.calls.probe,0);
});

test('connection probe is lazy, fixes its namespace/query/limit and never inspects or returns contents',async()=>{
  const q=queryFixture(),probe=q.probe();assert.deepEqual(q.calls,[]);
  assert.equal(await probe(),undefined);
  assert.deepEqual(q.calls,[['doc',FIRESTORE_ROOT],['collection','products'],['limit',1],['get']]);
});

test('connection probe sanitizes constructor/SDK failures and holds its cooldown after failure',async()=>{
  let now=0,reads=0;
  const probe=firestoreConnectionCheck(()=>{++reads;throw Error('NEVER_ECHO_PRIVATE_KEY_OR_SDK_DETAIL');},{clock:()=>now});
  await assert.rejects(probe(),problem(503,'firestore_check_failed'));
  await assert.rejects(probe(),problem(429,'connection_check_rate_limited'));assert.equal(reads,1);
  now=30000;await assert.rejects(probe(),problem(503,'firestore_check_failed'));assert.equal(reads,2);
  const q=queryFixture(async()=>{throw Object.assign(Error('NEVER_ECHO'),{code:7,metadata:{private:'NEVER_ECHO'}});});
  await assert.rejects(q.probe()(),problem(503,'firestore_check_failed'));
});

test('in-flight and short-interval repeated reads are rejected, with a bounded retry-after response',async()=>{
  let now=0,finish;
  const q=queryFixture(()=>new Promise(resolve=>{finish=resolve;})),probe=q.probe({clock:()=>now}),f=fixture({probe});
  const first=f.request();await new Promise(resolve=>setImmediate(resolve));
  let result=await f.request();assert.equal(result.status,429);assert.equal(result.headers.get('Retry-After'),'30');
  now=60000;result=await f.request();assert.equal(result.status,429,'busy must still block after cooldown elapsed');
  finish();assert.equal((await first).status,200);assert.equal(q.calls.filter(c=>c[0]==='get').length,1);
  const next=f.request();await new Promise(resolve=>setImmediate(resolve));finish();assert.equal((await next).status,200);
  result=await f.request();assert.equal(result.status,429);assert.equal(result.body.error,'connection_check_rate_limited');
});

test('rejected calls do not spend the read cooldown and actual read failures expose/log only a safe code',async()=>{
  const q=queryFixture(async()=>{throw Error('NEVER_ECHO_DATABASE_DETAIL');}),f=fixture({probe:q.probe()});
  assert.equal((await f.request('/connection',{authorization:null})).status,401);
  assert.equal((await f.request('/connection',{authorization:'Bearer fixture-other'})).status,403);
  assert.equal(q.calls.length,0);
  const result=await f.request();assert.equal(result.status,503);assert.deepEqual(result.body,{mode:'test',error:'firestore_check_failed'});
  assert.deepEqual(f.logs,['sign_in_required','tester_not_allowed','firestore_check_failed']);
  assert(!JSON.stringify({body:result.body,logs:f.logs}).includes('NEVER_ECHO'));
  assert.equal((await f.request()).status,429);
});

test('real signed Firebase/Google identity verification is enforced before the browser diagnostic',async()=>{
  const {publicKey,privateKey}=await generateKeyPair('RS256'),wrong=await generateKeyPair('RS256');
  const project='diplomaone-53b4e',now=Math.floor(Date.UTC(2026,9,30)/1000);
  const claims={sub:'approved-fixture',aud:project,iss:'https://securetoken.google.com/'+project,
    iat:now,exp:now+3600,auth_time:now-10,firebase:{sign_in_provider:'google.com'}};
  const sign=(patch={},key=privateKey)=>new SignJWT({...claims,...patch}).setProtectedHeader({alg:'RS256'}).sign(key);
  const f=fixture({verifier:firebaseVerifier(project,publicKey,()=>now*1000)});
  for(const [patch,key] of [[{exp:now-60}], [{aud:'diplomaone'}], [{iss:'https://evil.invalid'}],
    [{firebase:{sign_in_provider:'password'}}], [{firebase:{sign_in_provider:'anonymous'}}], [{},wrong.privateKey]]){
    const result=await f.request('/connection',{authorization:'Bearer '+await sign(patch,key)});
    assert.equal(result.status,401);assert.equal(f.calls.probe,0);
  }
  assert.equal((await f.request('/connection',{authorization:'Bearer '+await sign({sub:'not-invited'})})).status,403);
  assert.equal(f.calls.probe,0);
  const result=await f.request('/connection',{authorization:'Bearer '+await sign()});
  assert.equal(result.status,200);assert.deepEqual(result.body,success);assert.equal(f.calls.probe,1);assert.equal(f.calls.other,0);
});

test('disabled public config remains a no-read startup check, not a connection check or payment readiness claim',async()=>{
  const f=fixture(),result=await f.request('/config',{method:'GET',authorization:null,origin:null});
  assert.equal(result.status,200);assert.deepEqual(result.body,{mode:'test',enabled:false,reason:'setup_required',currency:'INR'});
  assert.deepEqual(f.calls,{verify:0,probe:0,other:0});
  const order=await f.request('/orders',{body:{productId:'DI03000161--summer-2026',requestId:'fixture'}});
  assert.equal(order.status,503);assert.equal(order.body.error,'backend_not_configured');assert.equal(f.calls.probe,0);
});
