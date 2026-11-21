// UI + real auth-controller tests with an offline Firebase boundary double.
// Optional argument: extracted Netlify package directory (not just app.js).
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const {JSDOM,VirtualConsole}=require('jsdom');
const site=path.resolve(process.argv[2]||__dirname);
const {createAuthController}=require(path.join(site,'auth.js'));
const html=fs.readFileSync(path.join(site,'index.html'),'utf8'),app=fs.readFileSync(path.join(site,'app.js'),'utf8');
const student={uid:'not-for-display',displayName:'Test Student',email:'student@example.test',emailVerified:true};
const deferred=()=>{let resolve,reject;const promise=new Promise((a,b)=>{resolve=a;reject=b;});return {promise,resolve,reject};};
const settle=async()=>{await new Promise(resolve=>setImmediate(resolve));await new Promise(resolve=>setImmediate(resolve));};
function boot(t,{hash='#/account',origin='https://www.diplomaone.in',language='en',initialUser=null,ready,loadError=false,service=true,fetch}={}) {
  const errors=[],vc=new VirtualConsole();vc.on('jsdomError',error=>errors.push(error.message));
  const dom=new JSDOM(html,{url:origin+'/'+hash,runScripts:'outside-only',virtualConsole:vc});
  const w=dom.window,d=w.document,calls={load:0,signIn:[],signOut:0,fetch:[],check:0,cancel:0},handlers={};
  const saved='[{"code":"DI03000161","unit":1,"title":{"en":"Saved unit"}}]';
  w.localStorage.setItem('diplomaone.website.lang',JSON.stringify(language));
  w.localStorage.setItem('diplomaone.website.saved',saved);
  w.scrollTo=()=>{};w.console.error=error=>errors.push(error?.message||String(error));
  w.fetch=(...args)=>{calls.fetch.push(String(args[0]));return fetch?fetch(...args):Promise.resolve({ok:true,json:async()=>({branches:[],subjects:{}})});};
  let onUser;
  const sdk={createClient(next){onUser=next;return {
    ready(){next(initialUser);return ready?.()||Promise.resolve();},
    signIn(lang){calls.signIn.push(lang);return handlers.signIn?.()||Promise.resolve();},
    signOut(){++calls.signOut;return handlers.signOut?.()||Promise.resolve();},
    checkTestConnection(){++calls.check;return handlers.check?.()||Promise.resolve({ok:true});},
    cancelTestConnection(){++calls.cancel;handlers.cancel?.();},dispose(){},
  };}};
  let importFails=loadError;
  if(service)w.DiplomaOneAuth=createAuthController(()=>{++calls.load;return importFails?Promise.reject(Error('internal-import-detail')):Promise.resolve(sdk);});
  w.eval(app);
  t.after(()=>dom.window.close());
  return {w,d,calls,handlers,errors,saved,emit:user=>onUser(user),setImportFailure(value){importFails=value;},
    async go(hash){w.location.hash=hash;await new Promise(resolve=>w.setTimeout(resolve,0));await settle();}};
}
const mainText=b=>b.d.querySelector('main').textContent;
const click=(b,selector)=>{const element=b.d.querySelector(selector);assert(element,selector+' is missing');element.click();return element;};
const unchangedPreferences=b=>assert.equal(b.w.localStorage.getItem('diplomaone.website.saved'),b.saved);

test('index loads controller before app with narrowly scoped Firebase/Checkout CSP',()=>{
  const doc=new JSDOM(html).window.document;
  assert.deepEqual([...doc.querySelectorAll('script[src]')].map(s=>s.getAttribute('src')),['auth.js','app.js']);
  assert([...doc.querySelectorAll('script')].every(s=>s.hasAttribute('defer')&&!s.textContent.trim()));
  const policy=doc.querySelector('[http-equiv="Content-Security-Policy"]').content;
  const directives=Object.fromEntries(policy.split(';').filter(x=>x.trim()).map(x=>{const [name,...values]=x.trim().split(/\s+/);return [name,values];}));
  assert.deepEqual(directives['script-src'],["'self'",'https://apis.google.com','https://checkout.razorpay.com/v1/checkout.js']);
  assert.deepEqual(directives['frame-src'],['https://diplomaone-53b4e.firebaseapp.com/__/auth/','https://api.razorpay.com','https://checkout.razorpay.com']);
  assert.deepEqual(directives['object-src'],["'none'"]);
  assert.deepEqual(directives['connect-src'],["'self'",'https://sunilpa4.github.io','https://api.github.com',
    'https://identitytoolkit.googleapis.com','https://securetoken.googleapis.com','https://diplomaone-53b4e.firebaseapp.com','https://api.razorpay.com','https://lumberjack.razorpay.com']);
  assert(!policy.includes('*'));assert(!policy.includes('unsafe-eval'));assert(!directives['script-src'].includes("'unsafe-inline'"));
  assert(!doc.querySelector('iframe,object,embed'));
  assert(doc.querySelector('.header-actions [href="#/account"]'));
  assert(doc.querySelector('#mobile-nav [href="#/account"]'));
  assert(doc.querySelector('#mobile-nav [href="#/purchases"]'));
  doc.defaultView.close();
});

test('ordinary reading does not load Firebase or require an account',async t=>{
  const b=boot(t,{hash:'#/'});await settle();
  assert(mainText(b).includes('Your diploma,'));assert.equal(b.calls.load,0);
  assert.equal(b.w.DiplomaOneAuth.snapshot().status,'idle');assert.equal(b.calls.fetch.length,1);
  assert.equal(b.d.querySelector('[data-account-link]').textContent,'My account','unknown session is not falsely labelled signed out');
  assert(!b.d.querySelector('[data-account-view]'));
  await b.go('#/saved');assert(mainText(b).includes('Your little study list.'));assert.equal(b.calls.load,0);
  unchangedPreferences(b);assert.deepEqual(b.errors,[]);
});

test('account route is usable without catalog/network and the button waits for readiness',async t=>{
  const gate=deferred(),b=boot(t,{ready:()=>gate.promise,fetch:()=>Promise.reject(Error('catalog offline'))});
  assert.equal(b.d.querySelector('#account-signin').disabled,true);assert.equal(b.calls.fetch.length,0);
  click(b,'#account-signin');assert.deepEqual(b.calls.signIn,[]);
  await settle();assert.equal(b.d.querySelector('.account-card').getAttribute('aria-busy'),'true');
  gate.resolve();await settle();
  assert.equal(b.d.querySelector('#account-signin').disabled,false);assert.equal(b.calls.load,1);
  assert.equal(b.d.querySelector('[data-account-link]').textContent,'Sign in');
  assert(mainText(b).includes('Individual paper access'));
  assert(mainText(b).includes('signing in does not sync them'));
  assert(mainText(b).includes('Sign out on shared devices'));
  assert.equal(b.calls.fetch.length,0);assert.deepEqual(b.errors,[]);
});

test('Google click is direct, duplicates are suppressed and hostile profile fields stay text',async t=>{
  const b=boot(t);await settle();
  const gate=deferred();let clickStack=false;
  b.handlers.signIn=()=>{assert(clickStack,'the popup was deferred outside the user click');return gate.promise;};
  const button=b.d.querySelector('#account-signin');clickStack=true;button.click();clickStack=false;
  assert.deepEqual(b.calls.signIn,['en']);assert.equal(b.d.querySelector('#account-signin').disabled,true);
  // Even a stale detached button cannot open another popup.
  button.click();assert.equal(b.calls.signIn.length,1);
  const malicious={...student,displayName:'<img src=x onerror="window.attacked=true">',email:'<script>window.attacked=true</script>',
    photoURL:'https://invalid.test/tracker',refreshToken:'NEVER-RENDER',accessToken:'NEVER-RENDER'};
  b.emit(malicious);gate.resolve({credential:{accessToken:'NEVER-RENDER'}});await settle();
  assert.equal(b.d.querySelector('.account-identity h2').textContent,malicious.displayName);
  assert.equal(b.d.querySelector('.account-details dd').textContent,malicious.email);
  assert(!b.d.querySelector('main img,main script,main [onerror]'));
  assert(!b.d.querySelector('main').innerHTML.includes('NEVER-RENDER'));assert.equal(b.w.attacked,undefined);
  assert(!mainText(b).includes('not-for-display'),'UID is not a student-facing display field');
  assert.equal(b.d.querySelector('[data-account-link]').textContent,'My account');
  assert.equal(b.d.activeElement.id,'account-signout');unchangedPreferences(b);
  assert.equal(b.w.localStorage.length,2,'no application-written tokens or fake purchase flags');
  assert.equal(b.w.sessionStorage.length,0,'the UI does not copy SDK tokens');
  assert.deepEqual(b.errors,[]);
});

test('a restored session displays a profile; failed logout is not shown as logged out',async t=>{
  const b=boot(t,{initialUser:student});await settle();
  assert(mainText(b).includes(student.email));assert(!b.d.querySelector('#account-signin'));
  b.handlers.signOut=()=>Promise.reject({code:'auth/network-request-failed',message:'NEVER-RENDER'});
  click(b,'#account-signout');await settle();
  assert(mainText(b).includes(student.email));assert(b.d.querySelector('#account-signout'));
  assert(b.d.querySelector('[role="alert"]').textContent.includes('Check your connection'));
  assert(!mainText(b).includes('NEVER-RENDER'));assert.equal(b.d.activeElement.id,'account-signout');
  b.handlers.signOut=()=>{b.emit(null);return Promise.resolve();};
  click(b,'#account-signout');await settle();
  assert(!mainText(b).includes(student.email));assert(b.d.querySelector('#account-signin'));
  assert.equal(b.d.querySelector('[data-account-link]').textContent,'Sign in');
  assert(!b.d.querySelector('[role="alert"]'));assert.equal(b.d.activeElement.id,'account-signin');
  unchangedPreferences(b);assert.deepEqual(b.errors,[]);
});

test('popup and setup errors are actionable in both languages, with no raw exception messages',async t=>{
  const b=boot(t);await settle();
  for(const [code,phrase] of [
    ['auth/popup-blocked','Allow pop-ups'],['auth/popup-closed-by-user','window was closed'],
    ['auth/cancelled-popup-request','one window at a time'],['auth/unauthorized-domain','add this domain in Firebase'],
    ['auth/operation-not-allowed','must enable it in Firebase'],['auth/configuration-not-found','not complete'],
    ['auth/invalid-api-key','configuration needs attention'],['auth/web-storage-unsupported','normal browser tab'],
    ['auth/network-request-failed','Check your connection'],['auth/user-disabled','account is disabled'],
    ['auth/internal-error','content blocker'],['auth/operation-not-supported-in-this-environment','normal browser tab'],
    ['auth/user-token-expired','Sign out and sign in again'],['auth/invalid-user-token','could not be verified'],
    ['auth/too-many-requests','wait a little'],['auth/account-exists-with-different-credential','linking the accounts'],
    ['arbitrary exception','Sign-in is unavailable right now'],
  ]) {
    b.handlers.signIn=()=>Promise.reject({code,message:'NEVER-RENDER',customData:{email:'private@example.test'}});
    click(b,'#account-signin');await settle();
    const alert=b.d.querySelector('[role="alert"]');assert(alert.textContent.includes(phrase),code);
    assert(!alert.textContent.includes('NEVER-RENDER'));assert(!alert.textContent.includes('private@example.test'));
    assert.equal(b.d.querySelector('#account-signin').disabled,false);
  }
  click(b,'#lang-toggle');await settle();
  assert.equal(b.d.documentElement.lang,'gu');assert.equal(b.d.querySelector('[data-purchases-link]').textContent,'મારી ખરીદી');
  b.handlers.signIn=()=>Promise.reject({code:'auth/popup-blocked'});click(b,'#account-signin');await settle();
  assert.equal(b.calls.signIn.at(-1),'gu');assert(b.d.querySelector('[role="alert"]').textContent.includes('પોપ-અપને મંજૂરી'));
  assert(b.d.querySelector('#account-signin').textContent.includes('Google દ્વારા સાઇન ઇન'));
  assert.equal(b.calls.load,1);assert.deepEqual(b.errors,[]);
});

test('failed module loading offers a genuine retry, not a popup outside a click',async t=>{
  const b=boot(t,{loadError:true});await settle();
  assert(b.d.querySelector('#account-retry'));assert(!b.d.querySelector('#account-signin'));
  assert(!mainText(b).includes('internal-import-detail'));
  b.setImportFailure(false);click(b,'#account-retry');await settle();
  assert.equal(b.calls.load,2);assert.deepEqual(b.calls.signIn,[]);
  assert.equal(b.d.querySelector('#account-signin').disabled,false);
  assert.equal(b.d.activeElement.id,'account-signin');assert.deepEqual(b.errors,[]);
});

test('missing auth controller does not crash reading or pretend sign-in works',async t=>{
  const b=boot(t,{service:false});await settle();
  assert(mainText(b).includes('Sign-in is unavailable right now'));assert(b.d.querySelector('#account-retry'));
  assert(!b.d.querySelector('#account-signin'));assert.deepEqual(b.errors,[]);
});

test('My purchases requires Google and never invents empty history when the service is unavailable',async t=>{
  for(const initialUser of [null,student]) {
    const b=boot(t,{hash:'#/purchases',initialUser});await settle();
    assert(mainText(b).includes('Only server-confirmed purchases appear here'));
    assert(mainText(b).includes('Sign-in alone does not unlock a paper'));
    if(initialUser)assert(mainText(b).includes('could not confirm access right now'));
    else assert(mainText(b).includes('Sign in with Google to buy or read your purchased paper'));
    assert(!b.d.querySelector('[data-checkout],form,input,script[src*="razorpay"],iframe,.purchase-item'));
    assert(!/purchase complete|you own|No confirmed purchases/i.test(mainText(b)));
    assert.equal(b.calls.fetch.length,0);assert.equal(b.calls.load,1);unchangedPreferences(b);
    assert.deepEqual(b.errors,[]);
  }
});

const testOrigin='https://vermillion-pothos-520a34.netlify.app';
test('test-site diagnostic is manual, signed-in, bilingual and never echoes a profile/token or invents purchases',async t=>{
  const b=boot(t,{hash:'#/test-connection',origin:testOrigin,fetch:()=>Promise.reject(Error('catalog offline'))});await settle();
  assert.equal(b.calls.fetch.length,0);assert.equal(b.calls.check,0);assert.equal(b.calls.load,1);
  assert.equal(b.d.querySelector('#connection-check').disabled,true);click(b,'#connection-check');assert.equal(b.calls.check,0);
  b.handlers.signIn=()=>{b.emit({...student,accessToken:'NEVER_RENDER'});return Promise.resolve();};
  click(b,'#account-signin');await settle();assert.equal(b.calls.check,0,'sign-in is not permission for an automatic database query');
  assert.equal(b.d.querySelector('#connection-check').disabled,false);
  for(const value of [student.uid,student.email,student.displayName,'NEVER_RENDER'])assert(!mainText(b).includes(value));
  const gate=deferred();b.handlers.check=()=>gate.promise;
  const button=click(b,'#connection-check');assert.equal(b.calls.check,1);assert.equal(b.d.querySelector('#connection-check').disabled,true);
  button.click();assert.equal(b.calls.check,1,'a detached duplicate click cannot re-request');
  click(b,'#lang-toggle');await settle();assert.equal(b.calls.check,1);assert(b.d.querySelector('#connection-result').textContent.includes('તપાસાઈ રહ્યું છે'));
  gate.resolve({ok:true,uid:'NEVER_RENDER',token:'NEVER_RENDER',documents:['NEVER_RENDER']});await settle();
  assert(b.d.querySelector('#connection-result').textContent.includes('વાંચન સફળ'));assert.equal(b.d.activeElement.id,'connection-result');
  click(b,'#lang-toggle');await settle();assert.equal(b.d.querySelector('#connection-result').textContent,'Firestore read succeeded. Checkout remains OFF.');
  assert(mainText(b).includes('not a billing cap'));assert(mainText(b).includes('does not test Razorpay'));
  assert(!b.d.querySelector('[data-checkout],form,input,iframe,script[src*="razorpay"]'));
  assert(!mainText(b).includes('NEVER_RENDER'));assert.equal(b.w.localStorage.length,2);assert.equal(b.w.sessionStorage.length,0);
  await b.go('#/purchases');assert(mainText(b).includes('Only server-confirmed purchases appear here'));assert.equal(b.calls.check,1);
  unchangedPreferences(b);assert.deepEqual(b.errors,[]);
});

test('diagnostic route is unavailable without loading auth on public/preview hosts; setup link is test-site-only',async t=>{
  for(const origin of ['https://www.diplomaone.in','https://sunilpa4.github.io',
    'https://deploy-preview-37--vermillion-pothos-520a34.netlify.app']){
    const b=boot(t,{hash:'#/test-connection',origin});await settle();
    assert(mainText(b).includes('only on the protected test site'));assert(!b.d.querySelector('#connection-check,#account-signin,[data-account-view]'));
    assert.equal(b.calls.load,0);assert.equal(b.calls.check,0);assert.equal(b.calls.fetch.length,0);assert.deepEqual(b.errors,[]);
  }
  const normal=boot(t);await settle();assert(!normal.d.querySelector('a[href="#/test-connection"]'));
  const approvedSite=boot(t,{origin:testOrigin});await settle();assert(approvedSite.d.querySelector('a[href="#/test-connection"]'));
  assert.equal(approvedSite.calls.check,0);assert.deepEqual(approvedSite.errors,[]);
});

test('diagnostic errors use only safe actionable local copy in both languages, with no raw payload display or auto-retry',async t=>{
  const b=boot(t,{hash:'#/test-connection',origin:testOrigin,initialUser:student});await settle();
  const cases=[['tester_not_allowed','PAYMENTS_TESTER_UIDS'],['invalid_or_expired_session','Sign out'],
    ['disable_test_checkout','both payment flags false'],['firestore_not_configured','missing or invalid'],
    ['firestore_check_failed','could not read Firestore'],['connection_check_rate_limited','30 seconds'],
    ['connection_timeout','No success is confirmed'],['connection_check_unavailable','current Production deployment'],
    ['<img src=x onerror=alert(1)>','check is unavailable']];
  for(const [code,phrase] of cases){
    const count=b.calls.check;b.handlers.check=()=>Promise.resolve({ok:false,code,message:'NEVER_RENDER',private_key:'NEVER_RENDER'});
    click(b,'#connection-check');await settle();
    const result=b.d.querySelector('#connection-result');assert.equal(result.getAttribute('role'),'alert');assert(result.textContent.includes(phrase),code);
    assert.equal(b.calls.check,count+1);assert(!mainText(b).includes('NEVER_RENDER'));assert(!b.d.querySelector('main img,main [onerror]'));
    assert.equal(b.d.querySelector('#connection-check').disabled,false);
  }
  click(b,'#lang-toggle');await settle();b.handlers.check=()=>Promise.resolve({ok:false,code:'tester_not_allowed'});
  click(b,'#connection-check');await settle();assert(b.d.querySelector('#connection-result').textContent.includes('મંજૂર ટેસ્ટર નથી'));
  b.handlers.check=()=>Promise.reject(Error('NEVER_RENDER'));click(b,'#connection-check');await settle();
  assert(!mainText(b).includes('NEVER_RENDER'));assert.deepEqual(b.errors,[]);
});

test('logout or account changes clear pending/results and cannot show a late diagnostic success',async t=>{
  const b=boot(t,{hash:'#/test-connection',origin:testOrigin,initialUser:student});await settle();
  const gate=deferred();b.handlers.check=()=>gate.promise;click(b,'#connection-check');
  b.handlers.signOut=()=>{b.emit(null);return Promise.resolve();};click(b,'#account-signout');await settle();
  gate.resolve({ok:true});await settle();assert.equal(b.d.querySelector('#connection-result').textContent,'');
  assert.equal(b.d.querySelector('#connection-check').disabled,true);assert(!mainText(b).includes('read succeeded'));
  b.emit(student);await settle();assert.equal(b.calls.check,1);
  b.handlers.check=()=>Promise.resolve({ok:true});click(b,'#connection-check');await settle();assert(mainText(b).includes('read succeeded'));
  b.emit({...student,uid:'a-different-account'});await settle();
  assert.equal(b.d.querySelector('#connection-result').textContent,'');assert.equal(b.calls.check,2);assert.deepEqual(b.errors,[]);
});

test('navigation cancels diagnostics, ignores late success and never replays on return or a stale button',async t=>{
  const b=boot(t,{hash:'#/test-connection',origin:testOrigin,initialUser:student});await settle();
  const gate=deferred();b.handlers.check=()=>gate.promise;const button=click(b,'#connection-check');
  await b.go('#/privacy');assert(mainText(b).includes('Protected test-site check'));assert(b.calls.cancel>0);
  gate.resolve({ok:true});await settle();assert(!b.d.querySelector('[data-account-view]'));assert(!mainText(b).includes('read succeeded'));
  await b.go('#/test-connection');assert.equal(b.calls.check,1);assert.equal(b.d.querySelector('#connection-result').textContent,'');
  button.click();assert.equal(b.calls.check,1,'a detached old-route button must not start another query');
  unchangedPreferences(b);assert.deepEqual(b.errors,[]);
});

test('privacy is bilingual, independent of the catalog, and does not initialize auth',async t=>{
  const b=boot(t,{hash:'#/privacy',fetch:()=>Promise.reject(Error('offline'))});await settle();
  for(const phrase of ['Optional Google sign-in','Firebase Authentication keeps an account identity record',
    'signing out does not delete','session storage','do not sync across devices','Payments','does not add an analytics']) {
    // The payments section uses sentence case in production copy.
    assert(mainText(b).toLowerCase().includes(phrase.toLowerCase()),phrase);
  }
  assert.equal(b.calls.load,0);assert.equal(b.calls.fetch.length,0);
  click(b,'#lang-toggle');await settle();assert(mainText(b).includes('વૈકલ્પિક Google સાઇન ઇન'));
  assert(mainText(b).includes('સાઇન આઉટ કરવાથી તે રેકોર્ડ કાઢી નાખવામાં આવતો નથી'));
  assert.equal(b.calls.load,0);assert.equal(b.calls.fetch.length,0);assert.deepEqual(b.errors,[]);
});

test('late catalog failures and sign-in completion do not steal navigation',async t=>{
  const data=deferred(),b=boot(t,{hash:'#/',fetch:()=>data.promise});
  await b.go('#/account');assert(b.d.querySelector('[data-account-view]'));assert.equal(b.calls.load,1);
  data.reject(Error('catalog offline'));await settle();
  assert(b.d.querySelector('[data-account-view]'),'stale catalog failure must not overwrite account screen');
  const gate=deferred();b.handlers.signIn=()=>gate.promise;click(b,'#account-signin');
  await b.go('#/privacy');b.emit(student);gate.resolve();await settle();
  assert(mainText(b).includes('Optional Google sign-in'));assert(!b.d.querySelector('[data-account-view]'));
  assert.equal(b.d.querySelector('[data-account-link]').textContent,'My account');
  assert(!mainText(b).includes(student.email));assert.deepEqual(b.errors,['catalog offline']);
});
