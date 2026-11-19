// Offline tests: no credentials, live Firebase changes or real Google logins.
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const {createAuthController}=require(path.resolve(process.argv[2]||path.join(__dirname,'auth.js')));
const deferred=()=>{let resolve,reject;const promise=new Promise((a,b)=>{resolve=a;reject=b;});return {promise,resolve,reject};};
const tick=()=>new Promise(resolve=>setImmediate(resolve));
const student={uid:'test-uid',displayName:'Test Student',email:'student@example.test',emailVerified:true};
function fixture(initialUser=null) {
  const calls={load:0,create:0,signIn:[],signOut:0,dispose:0},observers=[],handlers={};
  const sdk={createClient(onUser,onError) {
    ++calls.create;observers.push({onUser,onError});
    return {
      ready(){onUser(initialUser);return handlers.ready?.()||Promise.resolve();},
      signIn(language){calls.signIn.push(language);return handlers.signIn?.()||Promise.resolve();},
      signOut(){++calls.signOut;return handlers.signOut?.()||Promise.resolve();},
      dispose(){++calls.dispose;handlers.dispose?.();},
    };
  }};
  return {calls,observers,handlers,sdk,loader:()=>{++calls.load;return Promise.resolve(sdk);},
    emit:user=>observers.at(-1).onUser(user),error:error=>observers.at(-1).onError(error)};
}

test('lazy, deduplicated initialization, safe subscribers and immutable snapshots',async()=>{
  const f=fixture(),auth=createAuthController(f.loader),states=[];
  assert.equal(f.calls.load,0);
  assert.equal(auth.snapshot().status,'idle');
  assert.equal(Object.isFrozen(auth.snapshot()),true);
  auth.subscribe(()=>{throw Error('A broken view must not break auth');});
  const unsubscribe=auth.subscribe(s=>states.push(s.status));
  let reentrant;
  auth.subscribe(s=>{if(s.status==='loading')reentrant=auth.initialize();});
  const first=auth.initialize();
  assert.equal(auth.initialize(),first);
  assert.equal(reentrant,first,'pending must be assigned before notifying views');
  assert.equal(await first,true);
  assert.equal(auth.snapshot().status,'signed-out');
  assert.deepEqual(states,['idle','loading','signed-out']);
  assert.equal(await auth.initialize(),true);
  assert.equal(f.calls.load,1);assert.equal(f.calls.create,1);
  unsubscribe();f.emit(student);
  assert.deepEqual(states,['idle','loading','signed-out']);
  assert.throws(()=>auth.subscribe(null),TypeError);
});

test('readiness waits for session restoration and projects only display metadata',async()=>{
  const raw={...student,uid:'u'.repeat(180),displayName:'n'.repeat(220),email:'e'.repeat(350),
    accessToken:'never-expose',refreshToken:'never-expose',stsTokenManager:{refreshToken:'never-expose'},
    photoURL:'https://untrusted.invalid/profile.png',getIdToken(){throw Error('Do not ask for a token');}};
  const f=fixture(raw),gate=deferred();f.handlers.ready=()=>gate.promise;
  const auth=createAuthController(f.loader),pending=auth.initialize();await tick();
  assert.equal(auth.snapshot().status,'loading');assert.equal(auth.snapshot().user,null);
  gate.resolve();assert.equal(await pending,true);
  const s=auth.snapshot();
  assert.equal(s.status,'signed-in');assert.equal(Object.isFrozen(s.user),true);
  assert.deepEqual(Object.keys(s.user).sort(),['displayName','email','emailVerified','uid']);
  assert.equal(s.user.uid.length,128);assert.equal(s.user.displayName.length,200);assert.equal(s.user.email.length,320);
  assert(!JSON.stringify(s).includes('never-expose'));
  raw.displayName='changed outside';assert.equal(auth.snapshot().user.displayName.length,200);
  f.emit({uid:'id',displayName:4,email:null,emailVerified:'true'});
  assert.deepEqual(auth.snapshot().user,{uid:'id',displayName:'',email:'',emailVerified:false});
  for(const invalid of [null,{}, {uid:''},{uid:123}]){f.emit(invalid);assert.equal(auth.snapshot().user,null);}
});

test('popup is invoked synchronously in the click path and duplicate actions are ignored',async()=>{
  const f=fixture(),auth=createAuthController(f.loader),gate=deferred();
  assert.equal(await auth.signIn('en'),false,'must not import a module during a click');
  assert.equal(f.calls.load,0);
  await auth.initialize();
  let inClick=false;f.handlers.signIn=()=>{assert.equal(inClick,true);return gate.promise;};
  inClick=true;const first=auth.signIn('gu');inClick=false;
  assert.deepEqual(f.calls.signIn,['gu']);assert.equal(auth.snapshot().busy,'signIn');
  assert.equal(await auth.signIn('en'),false);assert.equal(await auth.signOut(),false);
  f.emit(student);assert.equal(auth.snapshot().status,'signed-in');assert.equal(auth.snapshot().busy,'signIn');
  gate.resolve({accessToken:'not-a-profile'});assert.equal(await first,true);
  assert.equal(auth.snapshot().busy,null);
  assert.equal(await auth.signIn('en'),true);assert.equal(f.calls.signIn.length,1);
});

test('credentials returned by a popup do not become an account or an entitlement',async()=>{
  const f=fixture(),auth=createAuthController(f.loader);await auth.initialize();
  f.handlers.signIn=()=>Promise.resolve({user:student,accessToken:'sensitive',purchased:true});
  assert.equal(await auth.signIn('en'),true);
  assert.equal(auth.snapshot().user,null,'only onAuthStateChanged is authoritative');
  assert.equal(auth.snapshot().status,'signed-out');
  assert(!JSON.stringify(auth.snapshot()).includes('sensitive'));
  assert.equal(await auth.signOut(),true);assert.equal(f.calls.signOut,0);
});

test('popup, storage and configuration failures never retain raw error details',async()=>{
  const f=fixture(),auth=createAuthController(f.loader);await auth.initialize();
  for(const code of ['auth/popup-blocked','auth/popup-closed-by-user','auth/unauthorized-domain','auth/operation-not-allowed','auth/network-request-failed','auth/web-storage-unsupported']) {
    f.handlers.signIn=()=>Promise.reject({code,message:'secret-user@example.test',credential:{idToken:'sensitive'}});
    assert.equal(await auth.signIn('en'),false);
    const s=auth.snapshot();assert.equal(s.status,'signed-out');assert.equal(s.busy,null);
    assert.deepEqual(s.error,{code,operation:'signIn'});assert.equal(Object.isFrozen(s.error),true);
    assert(!JSON.stringify(s).includes('sensitive'));assert(!JSON.stringify(s).includes('secret-user'));
  }
  f.handlers.signIn=()=>{throw {code:'<img src=x onerror=alert(1)>',message:'sensitive'};};
  assert.equal(await auth.signIn('en'),false);
  assert.equal(auth.snapshot().error.code,'auth/unavailable');
  f.handlers.signIn=()=>Promise.resolve();f.emit(student);
  assert.equal(auth.snapshot().error,null);
});

test('failed sign-out keeps the account; successful sign-out waits for the SDK observer',async()=>{
  const f=fixture(student),auth=createAuthController(f.loader);await auth.initialize();
  f.handlers.signOut=()=>Promise.reject({code:'auth/network-request-failed',message:'internal'});
  assert.equal(await auth.signOut(),false);assert.equal(auth.snapshot().status,'signed-in');
  assert.equal(auth.snapshot().user.email,student.email);
  assert.deepEqual(auth.snapshot().error,{code:'auth/network-request-failed',operation:'signOut'});
  const gate=deferred();f.handlers.signOut=()=>gate.promise;
  const request=auth.signOut();assert.equal(auth.snapshot().user.email,student.email);
  f.emit(null);assert.equal(auth.snapshot().status,'signed-out');
  gate.resolve();assert.equal(await request,true);assert.equal(auth.snapshot().user,null);
  assert.equal(auth.snapshot().error,null);assert.equal(auth.snapshot().busy,null);
});

test('module import, client creation and initial-session errors are recoverable',async()=>{
  for(const phase of ['import','create','ready']) {
    const f=fixture();let broken=true;
    f.handlers.ready=()=>broken&&phase==='ready'?Promise.reject({code:'auth/network-request-failed'}):Promise.resolve();
    const auth=createAuthController(()=>{
      if(broken&&phase==='import')return Promise.reject(Error('private error text'));
      if(broken&&phase==='create')return Promise.resolve({createClient(){throw {code:'auth/invalid-api-key'};}});
      return f.loader();
    });
    assert.equal(await auth.initialize(),false);assert.equal(auth.snapshot().status,'unavailable');
    assert.equal(auth.snapshot().error.operation,'initialize');assert.equal(auth.snapshot().user,null);
    broken=false;assert.equal(await auth.initialize(),true);assert.equal(auth.snapshot().status,'signed-out');
    assert.equal(auth.snapshot().error,null);
    if(phase==='ready')assert.equal(f.calls.dispose,1);
  }
});

test('a module-load deadline cannot create a late observer or overwrite a retry',async()=>{
  const old=deferred(),f=fixture(student);let loads=0;
  const auth=createAuthController(()=>++loads===1?old.promise:f.loader(),25);
  assert.equal(await auth.initialize(),false);
  assert.equal(auth.snapshot().status,'unavailable');
  assert.equal(auth.snapshot().error.code,'auth/network-request-failed');
  assert.equal(await auth.initialize(),true);assert.equal(auth.snapshot().user.email,student.email);
  old.resolve({createClient(){throw Error('timed-out module must not be used');}});await tick();
  assert.equal(auth.snapshot().status,'signed-in');assert.equal(f.calls.create,1);
});

test('initial-session timeout disposes stale observers and ignores their late results',async()=>{
  const gate=deferred(),f=fixture();f.handlers.ready=()=>gate.promise;
  const auth=createAuthController(f.loader,25),request=auth.initialize();await tick();
  const stale=f.observers[0];assert.equal(await request,false);assert.equal(f.calls.dispose,1);
  f.handlers.ready=()=>Promise.resolve();assert.equal(await auth.initialize(),true);
  stale.onUser(student);stale.onError({code:'auth/user-disabled'});gate.resolve();await tick();
  assert.equal(auth.snapshot().status,'signed-out');assert.equal(auth.snapshot().user,null);assert.equal(auth.snapshot().error,null);
});

test('an observer-cleanup failure cannot hide a failed initialization',async()=>{
  const f=fixture();f.handlers.ready=()=>Promise.reject(Error('not ready'));
  f.handlers.dispose=()=>{throw Error('cleanup');};
  const auth=createAuthController(f.loader);assert.equal(await auth.initialize(),false);
  assert.equal(auth.snapshot().status,'unavailable');assert.equal(auth.snapshot().error.code,'auth/unavailable');
});

test('session observer errors expose a safe code, not tokens or an invented logout',async()=>{
  const f=fixture(student),auth=createAuthController(f.loader);await auth.initialize();
  f.error({code:'auth/user-token-expired',message:'private detail',accessToken:'sensitive'});
  assert.equal(auth.snapshot().user.uid,student.uid);
  assert.deepEqual(auth.snapshot().error,{code:'auth/user-token-expired',operation:'session'});
  assert(!JSON.stringify(auth.snapshot()).includes('sensitive'));
  f.emit(null);assert.equal(auth.snapshot().user,null);assert.equal(auth.snapshot().error,null);
});

// Exercise the real Firebase adapter with explicit SDK boundary doubles. This
// verifies calls/scopes/persistence without a Firebase emulator or live project.
test('Firebase adapter uses the owner web config, session persistence and Google only',async()=>{
  const {build}=require('esbuild');
  const result=await build({entryPoints:[path.join(__dirname,'auth/firebase-client.js')],write:false,bundle:true,
    platform:'browser',format:'iife',globalName:'ClientAdapter',logLevel:'silent',plugins:[{
      name:'offline-firebase-sdk-boundary',setup(build){
        build.onResolve({filter:/^@firebase\//},args=>{
          assert(['@firebase/app','@firebase/auth'].includes(args.path),'no database/analytics/payments SDK');
          return {path:args.path,namespace:'fake-firebase'};
        });
        build.onLoad({filter:/.*/,namespace:'fake-firebase'},args=>({contents:args.path==='@firebase/app'
          ?'export const initializeApp=(...args)=>globalThis.sdk.initializeApp(...args);'
          :'export const {initializeAuth,browserSessionPersistence,browserPopupRedirectResolver,GoogleAuthProvider,onAuthStateChanged,signInWithPopup,signOut}=globalThis.sdk;'}));
      },
    }]});
  const calls={},auth={authStateReady:()=>{calls.ready=true;return Promise.resolve();}},app={},session={},resolver={};
  const sdk={
    initializeApp(config,name){calls.config=config;calls.name=name;return app;},
    initializeAuth(received,options){assert.equal(received,app);calls.options=options;return auth;},
    browserSessionPersistence:session,browserPopupRedirectResolver:resolver,
    GoogleAuthProvider:class {setCustomParameters(parameters){this.parameters=parameters;}},
    onAuthStateChanged(received,onUser,onError){assert.equal(received,auth);calls.onUser=onUser;calls.onError=onError;return()=>{calls.disposed=true;};},
    signInWithPopup(received,provider){assert.equal(received,auth);calls.provider=provider;return Promise.resolve({accessToken:'not-exposed'});},
    signOut(received){assert.equal(received,auth);calls.signedOut=true;return Promise.resolve();},
  };
  const context=vm.createContext({sdk});vm.runInContext(result.outputFiles[0].text,context);
  const onUser=()=>{},onError=()=>{},client=context.ClientAdapter.createClient(onUser,onError);
  assert.equal(calls.config.projectId,'diplomaone-53b4e');assert.equal(calls.config.authDomain,'diplomaone-53b4e.firebaseapp.com');
  assert.equal(calls.config.appId,'1:784760831297:web:4d682878a2efb0b4c075c0');assert.equal(calls.config.measurementId,undefined);
  assert.equal(calls.name,'diplomaone-website');assert.equal(calls.options.persistence,session);assert.equal(calls.options.popupRedirectResolver,resolver);
  assert.equal(calls.onUser,onUser);assert.equal(calls.onError,onError);await client.ready();assert.equal(calls.ready,true);
  const signIn=client.signIn('gu');assert(calls.provider,'popup must be invoked before returning to the event loop');
  assert.equal(JSON.stringify(calls.provider.parameters),JSON.stringify({prompt:'select_account'}));
  assert.equal(auth.languageCode,'gu');assert.equal(await signIn,undefined,'never return OAuth credentials to views');
  await client.signIn('unexpected-language');assert.equal(auth.languageCode,'en');
  await client.signOut();assert.equal(calls.signedOut,true);client.dispose();assert.equal(calls.disposed,true);
});

test('the checked-in SDK is ESM, self-hosted and exposes only createClient',()=>{
  const source=fs.readFileSync(path.join(__dirname,'assets/firebase-auth.js'),'utf8');
  assert(/export\{[^}]* as createClient\}/.test(source));
  assert(!/from["']https?:\/\//.test(source));
  assert(source.includes('diplomaone-53b4e.firebaseapp.com'));
  assert(fs.readFileSync(path.join(__dirname,'assets/firebase-auth.js.LEGAL.txt'),'utf8').includes('Apache License'));
});
