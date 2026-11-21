// Real request helper, offline HTTP/SDK boundaries. No owner keys, tokens,
// project, Firestore client, real network, account settings or rule changes.
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const source=fs.readFileSync(path.join(__dirname,'auth/connection-check.js'),'utf8');
const helper=import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
const origin='https://vermillion-pothos-520a34.netlify.app';
const token='offlineFixture.onlyNotReal.signature';
const success={mode:'test',database:'firestore',readable:true,readOnly:true,checkoutEnabled:false,paymentsVerified:false};
const deferred=()=>{let resolve,reject;const promise=new Promise((a,b)=>{resolve=a;reject=b;});return {promise,resolve,reject};};
const tick=()=>new Promise(resolve=>setImmediate(resolve));
const failure=code=>({ok:false,code});
async function fixture(options={}){
  const calls={token:0,http:[]},state={user:{getIdToken(){++calls.token;return options.getToken?options.getToken():Promise.resolve(token);}}};
  const {createConnectionCheck}=await helper;
  const location={origin:options.origin??origin,hash:options.hash??'#/test-connection'};
  const check=createConnectionCheck(()=>state.user,{location,timeoutMs:options.timeoutMs??1000,
    fetcher(...args){calls.http.push(args);return options.fetch?options.fetch(...args):Promise.resolve(Response.json(success));}});
  return {calls,state,check,location};
}

test('helper is lazy and sends one ID token only to the fixed relative same-origin POST',async()=>{
  const f=await fixture();assert.equal(f.calls.token,0);assert.equal(f.calls.http.length,0);
  const result=await f.check.check();assert.deepEqual(result,{ok:true});assert.equal(Object.isFrozen(result),true);
  assert.equal(f.calls.token,1);assert.equal(f.calls.http.length,1);
  const [url,options]=f.calls.http[0];assert.equal(url,'/api/payments/test/connection');
  assert.equal(options.method,'POST');assert.equal(options.body,'{}');assert.equal(options.cache,'no-store');
  assert.equal(options.redirect,'error');assert.equal(options.credentials,'same-origin');assert(options.signal instanceof AbortSignal);
  assert.deepEqual(options.headers,{'Content-Type':'application/json',Authorization:'Bearer '+token});
  assert.deepEqual(Object.keys(f.check).sort(),['cancel','check','dispose']);
  assert(!JSON.stringify(result).includes(token));
});

test('non-test origins cannot even request a token, and missing sessions cannot send HTTP',async()=>{
  for(const wrong of ['https://www.diplomaone.in','https://sunilpa4.github.io','http://localhost:8000',
    'https://deploy-preview-37--vermillion-pothos-520a34.netlify.app',origin+'.evil.invalid',origin+':444',origin.replace('https:','http:')]){
    const f=await fixture({origin:wrong});assert.deepEqual(await f.check.check(),failure('test_site_required'));
    assert.equal(f.calls.token,0);assert.equal(f.calls.http.length,0);
  }
  const f=await fixture();for(const user of [null,{}, {getIdToken:'not-a-function'}]){
    f.state.user=user;assert.deepEqual(await f.check.check(),failure('sign_in_required'));
  }
  assert.equal(f.calls.http.length,0);
});

test('wrong route and navigation before hashchange dispatch cannot start a request with a late token',async()=>{
  const wrong=await fixture({hash:'#/account'});assert.deepEqual(await wrong.check.check(),failure('connection_check_unavailable'));
  assert.equal(wrong.calls.token,0);assert.equal(wrong.calls.http.length,0);
  const gate=deferred(),f=await fixture({getToken:()=>gate.promise});const request=f.check.check();
  // Deliberately DO NOT dispatch cancel/hashchange yet: the URL has changed but
  // browser event delivery can lag a resolving getIdToken promise.
  f.location.hash='#/privacy';gate.resolve(token);
  assert.deepEqual(await request,failure('session_changed'));assert.equal(f.calls.http.length,0);
  const response=deferred(),g=await fixture({fetch:()=>response.promise}),pending=g.check.check();await tick();
  g.location.hash='#/privacy';response.resolve(Response.json(success));assert.deepEqual(await pending,failure('session_changed'));
});

test('duplicate clicks share one pending token/request and never auto-retry',async()=>{
  const gate=deferred(),f=await fixture({fetch:()=>gate.promise});
  const first=f.check.check(),second=f.check.check();assert.equal(first,second);assert.equal(f.calls.token,1);
  await tick();assert.equal(f.calls.http.length,1);assert.equal(f.check.check(),first);
  gate.resolve(Response.json(success));assert.deepEqual(await first,{ok:true});
  await tick();assert.equal(f.calls.token,1);assert.equal(f.calls.http.length,1);
});

test('session change before token resolution stops any request and never returns token details',async()=>{
  const gate=deferred(),f=await fixture({getToken:()=>gate.promise});
  const request=f.check.check();f.state.user={getIdToken:()=>Promise.resolve('other-offline-fixture-token')};
  gate.resolve(token);assert.deepEqual(await request,failure('session_changed'));assert.equal(f.calls.http.length,0);
});

test('session change during HTTP discards a late success',async()=>{
  const gate=deferred(),f=await fixture({fetch:()=>gate.promise});
  const first=f.check.check();await tick();f.state.user=null;
  gate.resolve(Response.json({...success,email:'NEVER_ECHO',token:'NEVER_ECHO'}));
  assert.deepEqual(await first,failure('session_changed'));assert.equal(f.calls.http.length,1);
  assert.deepEqual(await f.check.check(),failure('sign_in_required'));
});

test('explicit navigation/logout cancellation promptly resolves even if token refresh is stuck',async()=>{
  const gate=deferred(),f=await fixture({getToken:()=>gate.promise});
  const request=f.check.check();f.check.cancel();assert.deepEqual(await request,failure('session_changed'));
  gate.resolve(token);await tick();assert.equal(f.calls.http.length,0);
});

test('cancellation/disposal abort HTTP and a disposed helper cannot be reused',async()=>{
  const f=await fixture({fetch:()=>new Promise(()=>{})});
  const request=f.check.check();await tick();assert.equal(f.calls.http[0][1].signal.aborted,false);
  f.check.dispose();assert.deepEqual(await request,failure('session_changed'));assert.equal(f.calls.http[0][1].signal.aborted,true);
  assert.deepEqual(await f.check.check(),failure('session_changed'));assert.equal(f.calls.token,1);assert.equal(f.calls.http.length,1);
});

test('timeouts stop a late token from sending and abort a slow HTTP response, without retry',async()=>{
  const gate=deferred(),tokenWait=await fixture({timeoutMs:10,getToken:()=>gate.promise});
  assert.deepEqual(await tokenWait.check.check(),failure('connection_timeout'));
  gate.resolve(token);await tick();assert.equal(tokenWait.calls.http.length,0);
  const httpWait=await fixture({timeoutMs:10,fetch:()=>new Promise(()=>{})});
  assert.deepEqual(await httpWait.check.check(),failure('connection_timeout'));
  assert.equal(httpWait.calls.http[0][1].signal.aborted,true);assert.equal(httpWait.calls.http.length,1);
});

test('malformed token values and SDK token errors are safe, with no network request',async()=>{
  for(const value of [undefined,null,3,'','short','x'.repeat(16001),'bad\n'+token,token+' space',token+'\n',token+'\r',token+'\u007f',token+'<script>']){
    const f=await fixture({getToken:()=>Promise.resolve(value)});
    assert.deepEqual(await f.check.check(),failure('sign_in_required'));assert.equal(f.calls.http.length,0);
  }
  for(const getToken of [()=>{throw Error('NEVER_ECHO');},()=>Promise.reject({message:'NEVER_ECHO',token:'NEVER_ECHO'})]){
    const f=await fixture({getToken});assert.deepEqual(await f.check.check(),failure('sign_in_required'));assert.equal(f.calls.http.length,0);
  }
});

test('only allowlisted safe server errors pass through, never raw exception/PII/configuration payloads',async()=>{
  for(const code of ['sign_in_required','invalid_or_expired_session','tester_not_allowed','disable_test_checkout',
    'firestore_not_configured','firestore_check_failed','connection_check_rate_limited','connection_check_unavailable']){
    const f=await fixture({fetch:async()=>Response.json({mode:'test',error:code,message:'NEVER_ECHO',uid:'NEVER_ECHO',email:'NEVER_ECHO',private_key:'NEVER_ECHO'},{status:503})});
    assert.deepEqual(await f.check.check(),failure(code));
  }
  for(const code of ['NEVER_ECHO','<img src=x onerror=alert(1)>','__proto__',null,{code:'NEVER_ECHO'}]){
    const f=await fixture({fetch:async()=>Response.json({mode:'test',error:code},{status:403})});
    assert.deepEqual(await f.check.check(),failure('connection_check_unavailable'));
  }
  const f=await fixture({fetch:async()=>{throw {message:'NEVER_ECHO',authorization:token};}});
  assert.deepEqual(await f.check.check(),failure('connection_check_unavailable'));
});

test('HTML hosting gates, redirects, malformed/oversized/non-test/incomplete successes cannot be shown as success',async()=>{
  const responses=[
    ()=>new Response('<html>NEVER_ECHO Netlify login</html>',{headers:{'Content-Type':'text/html'}}),
    ()=>new Response('NEVER_ECHO',{headers:{'Content-Type':'application/json'}}),
    ()=>new Response('x'.repeat(4097),{headers:{'Content-Type':'application/json'}}),
    ()=>new Response(null,{status:204}),
    ()=>Response.json({...success,mode:'live'}),()=>Response.json({...success,checkoutEnabled:true}),
    ()=>Response.json({...success,readOnly:false}),()=>Response.json({...success,paymentsVerified:true}),
    ()=>Response.json({mode:'test',readable:true}),()=>Response.json(success,{status:503}),
    ()=>({redirected:true,ok:true,headers:new Headers({'Content-Type':'application/json'}),body:null}),
  ];
  for(const response of responses){
    const f=await fixture({fetch:async()=>response()});assert.deepEqual(await f.check.check(),failure('connection_check_unavailable'));
    assert.equal(f.calls.http.length,1);
  }
  const f=await fixture({fetch:async()=>Response.json({...success,uid:'NEVER_ECHO',private_key:'NEVER_ECHO',documents:['NEVER_ECHO']})});
  assert.deepEqual(await f.check.check(),{ok:true},'success is a projection, not an SDK/provider/configuration response');
});
