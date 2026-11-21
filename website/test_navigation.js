// Actual SPA navigation, entirely offline. A frozen full catalog proves that
// UI filtering never deletes future branches, semesters, files or saved data.
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {JSDOM,VirtualConsole}=require('jsdom'),fixture=require('./test_navigation_fixture');
const site=path.resolve(process.argv[2]||__dirname),html=fs.readFileSync(path.join(site,'index.html'),'utf8'),app=fs.readFileSync(path.join(site,'app.js'),'utf8');
const freeze=value=>{if(value&&typeof value==='object'){Object.values(value).forEach(freeze);Object.freeze(value);}return value;};
async function waitFor(fn,label='view'){
 const deadline=Date.now()+5000;
 do{if(fn())return;await new Promise(resolve=>setTimeout(resolve,5));}while(Date.now()<deadline);
 throw Error('Timed out waiting for '+label);
}
async function boot(t,{hash='#/',language='en',saved=[],owner=false}={}){
 const errors=[],vc=new VirtualConsole();vc.on('jsdomError',error=>errors.push(error.message));
 const dom=new JSDOM(html,{url:'https://www.diplomaone.in/'+hash,runScripts:'outside-only',virtualConsole:vc});
 const w=dom.window,d=w.document,catalog=freeze(fixture.catalog()),before=JSON.stringify(catalog),calls={http:[],auth:0,privateReads:0};
 const savedValue=JSON.stringify(saved),ownedId=fixture.codes.hiddenSemester+'--'+fixture.session;
 w.localStorage.setItem('diplomaone.website.lang',JSON.stringify(language));w.localStorage.setItem('diplomaone.website.saved',savedValue);
 w.scrollTo=()=>{};w.console.error=error=>errors.push(error?.message||String(error));
 w.fetch=async(url)=>{
  const value=String(url);calls.http.push(value);
  if(value.startsWith('data/catalog.json'))return {ok:true,json:async()=>catalog};
  if(value.startsWith('https://api.github.com/'))return {ok:true,json:async()=>fixture.tree()};
  if(value==='/api/payments/live/config')return {ok:true,json:async()=>({mode:'live',enabled:false,products:[]})};
  const subject=/^data\/subjects\/([A-Z0-9]+)\.json/.exec(value);
  if(subject)return {ok:true,json:async()=>fixture.subject(subject[1],catalog)};
  const unit=/^data\/units\/([A-Z0-9]+)_u([0-9]+)\.json/.exec(value);
  if(unit)return {ok:true,json:async()=>fixture.unit(unit[1],unit[2])};
  if([fixture.codes.maths,fixture.codes.physics].some(code=>value.startsWith('https://sunilpa4.github.io/diplomaone-content/papers/'+code+'/')))
   return {ok:true,text:async()=>fixture.freeReader};
  throw Error('Unexpected network/public paid request: '+value);
 };
 const state={status:owner?'signed-in':'idle',user:owner?{uid:'offline-owner'}:null,busy:null,error:null};let notify;
 w.DiplomaOneAuth={subscribe(next){notify=next;next(state);},initialize(){++calls.auth;notify({...state,status:'signed-out'});return Promise.resolve();},
  cancelPayments(){},paymentConfiguration:async()=>({ok:true,enabled:false,products:[]}),
  async readPurchasedPaper(id){++calls.privateReads;if(!owner||id!==ownedId)return {ok:false,code:'purchase_required'};
   return {ok:true,productId:id,html:fixture.ownedReader,readerPath:fixture.session+'.html',assets:[{id:'a'.repeat(64),path:fixture.session+'.html',mime:'text/plain; charset=utf-8',bytes:Buffer.byteLength(fixture.ownedReader)}]};},
  loadPurchases:async()=>({ok:true,purchases:owner?[{productId:ownedId,title:'Owned historical paper',branch:'computer',amount:1900,currency:'INR',active:true,purchasedAt:'2026-10-30T00:00:00.000Z'}]:[]})};
 w.eval(app);
 t.after(()=>{try{assert.equal(JSON.stringify(catalog),before,'complete catalog must remain untouched');assert.deepEqual(errors,[]);}finally{dom.window.close();}});
 const main=d.querySelector('main');
 return {w,d,main,calls,catalog,savedValue,ownedId,
  async ready(selector){await waitFor(()=>d.querySelector(selector),selector);},
  async go(value,selector){const previous=main.firstElementChild;w.location.hash=value;await waitFor(()=>main.firstElementChild!==previous&&d.querySelector(selector),value);},
  click(selector){const target=d.querySelector(selector);assert(target,selector+' missing');target.click();return target;},
  input(selector,value){const input=d.querySelector(selector);input.value=value;input.dispatchEvent(new w.Event('input',{bubbles:true}));},
  change(selector,value){const input=d.querySelector(selector);input.value=value;input.dispatchEvent(new w.Event('change',{bubbles:true}));}};
}
const branchKeys=b=>[...b.main.querySelectorAll('.branch-card')].map(a=>a.dataset.branch);
const links=b=>[...b.main.querySelectorAll('a')].map(a=>a.getAttribute('href'));

test('clean bilingual home shows exactly five branches and useful shortcuts, not repeated promotional sections',async t=>{
 for(const language of ['en','gu']){
  const b=await boot(t,{language});await b.ready('#home-search');
  assert.deepEqual(branchKeys(b),fixture.keys);assert.equal(b.main.querySelectorAll('h1').length,1);
  assert(b.main.querySelector('.study-shortcut[href="#/branches"]'));assert(b.main.querySelector('.study-shortcut[href="#/papers"]'));
  assert(b.main.querySelector('.purchases-shortcut[href="#/purchases"]'));assert.equal(b.main.querySelectorAll('.common-links a').length,2);
  assert.equal(b.main.querySelectorAll('.how-section,.trust-strip,.cta-band,.hero-image,img,iframe').length,0);
  assert(!b.main.querySelector('a[href*="releases"],a[href="app/"]'));
  assert.equal(b.d.querySelector('.footer-tools').open,false,'legacy app links stay available but collapsed');
  assert(b.d.querySelector('.footer-tools a[href="app/"]')||b.d.querySelector('.footer-tools a[href$="/app/"]'));
  assert.equal(b.d.documentElement.lang,language);assert.equal(b.calls.auth,0);
  assert.equal(b.calls.http.length,1,'home is catalog-only: no Auth, gateway or paper-index preload');
  assert.equal(b.main.querySelector('.branch-card[data-branch="computer"] p').textContent.trim(),language==='en'?'4 subjects ready':'4 વિષયો તૈયાર','shared subjects are counted once, excluding deferred semesters');
 }
});

test('branch search and semester pages expose only the agreed branches and first five semesters',async t=>{
 const b=await boot(t,{hash:'#/branches'});await b.ready('#results .branch-card');assert.deepEqual(branchKeys(b),fixture.keys);
 b.input('#search-input','Information Technology');assert.equal(branchKeys(b).length,0);
 b.input('#search-input','કેમિકલ');assert.deepEqual(branchKeys(b),['chemical']);
 await b.go('#/branch/computer','.semester-card');
 assert.deepEqual([...b.main.querySelectorAll('.semester-card')].map(a=>a.getAttribute('href')),['1','2','3','4','5'].map(s=>'#/branch/computer/'+s));
 assert(!b.main.textContent.includes('Semester 6'));assert(!links(b).some(link=>link?.endsWith('/6')));
 for(const hash of ['#/branch/computer/6','#/branch/it','#/branch/it/4']){
  await b.go(hash,'[data-catalog-limited]');assert.equal(b.main.querySelectorAll('.semester-card,.subject-card').length,0);
 }
 assert.equal(b.calls.auth,0);assert(!b.calls.http.some(value=>value.startsWith('data/subjects/')||value.startsWith('data/units/')));
});

test('home search supports Gujarati and codes, ignores blank input and escapes hostile query markup',async t=>{
 const b=await boot(t);await b.ready('#home-search');const form=b.d.querySelector('#home-search');
 form.dispatchEvent(new b.w.Event('submit',{bubbles:true,cancelable:true}));assert.equal(b.w.location.hash,'#/');assert.equal(b.d.activeElement.id,'home-search-input');
 b.input('#home-search-input','કમ્પ્યુટર');form.dispatchEvent(new b.w.Event('submit',{bubbles:true,cancelable:true}));
 await waitFor(()=>b.main.querySelector('#results a[href="#/subject/'+fixture.codes.computer+'"]'));
 assert.equal(b.d.querySelector('#search-input').value,'કમ્પ્યુટર');
 await b.go('#/search/'+fixture.codes.civil,'#results .subject-card');assert.equal(b.main.querySelectorAll('.subject-card').length,1);
 const hostile='<img src=x onerror="window.attacked=true">';await b.go('#/search/'+encodeURIComponent(hostile),'#search-input');
 assert.equal(b.d.querySelector('#search-input').value,hostile);assert(!b.main.querySelector('img,script,[onerror]'));assert.equal(b.w.attacked,undefined);assert.equal(b.calls.auth,0);
});

test('subject search hides known deferred-only placements but preserves shared and unregistered material',async t=>{
 const b=await boot(t,{hash:'#/search'});await b.ready('#search-input');
 for(const code of [fixture.codes.hiddenSemester,fixture.codes.hiddenBranch]){
  b.input('#search-input',code);assert.equal(b.main.querySelectorAll('.subject-card').length,0);
 }
 for(const key of ['shared','computer','unmapped','maths','physics']){
  b.input('#search-input',fixture.codes[key]);assert(b.main.querySelector('a[href="#/subject/'+fixture.codes[key]+'"]'));
  assert(!b.main.textContent.includes('Information Technology'));assert(!b.main.textContent.includes('Semester 6'));
 }
 assert.equal(b.calls.auth,0);
});

test('all paper filters exclude deferred-only catalog placements without guessing codes or losing legacy sessions',async t=>{
 const b=await boot(t,{hash:'#/papers'});await b.ready('#paper-results .paper-subject-group');
 assert.deepEqual([...b.d.querySelector('#paper-branch-filter').options].map(o=>o.value),['',...fixture.keys]);
 assert.deepEqual([...b.d.querySelector('#paper-semester-filter').options].map(o=>o.value),['','1','2','3','4','5']);
 const shown=links(b);
 for(const code of [fixture.codes.hiddenSemester,fixture.codes.hiddenBranch])assert(!shown.some(link=>link?.includes('/paper/'+code+'/')));
 for(const code of [fixture.codes.computer,fixture.codes.shared,fixture.codes.unmapped,'4350501'])assert(shown.some(link=>link?.includes('/paper/'+code+'/'+fixture.session)));
 assert(!b.main.textContent.includes('Information Technology'));assert(!b.main.textContent.includes('Semester 6'));
 assert(b.main.querySelector('a[href*="/paper/4350501/"]').textContent.includes('Older scheme'));
 b.change('#paper-branch-filter','computer');b.change('#paper-semester-filter','2');
 assert(b.main.querySelector('a[href*="/paper/'+fixture.codes.shared+'/"]'));assert(!links(b).some(link=>link?.includes('/paper/'+fixture.codes.hiddenSemester+'/')));
 await b.go('#/papers/computer/6','#paper-results');assert.equal(b.d.querySelector('#paper-semester-filter').value,'');
 assert(!b.main.querySelector('a[href*="/paper/'+fixture.codes.hiddenSemester+'/"]'));assert.equal(b.calls.auth,0);
 assert.equal(b.calls.http.filter(value=>value.startsWith('https://api.github.com/')).length,1,'no background polling or repeated tab index');
});

test('saved units outside the selection are hidden, not deleted from local storage',async t=>{
 const saved=['computer','hiddenSemester','hiddenBranch'].map(key=>({code:fixture.codes[key],unit:1,title:{en:key}}));
 const b=await boot(t,{hash:'#/saved',saved});await b.ready('.subject-card');
 assert.equal(b.main.querySelectorAll('.subject-card').length,1);assert(links(b).includes('#/unit/'+fixture.codes.computer+'/1'));
 assert(b.main.querySelector('.reader-notice').textContent.includes('has not been deleted'));
 assert.equal(b.w.localStorage.getItem('diplomaone.website.saved'),b.savedValue);
 await b.go('#/','#home-search');assert.equal(b.w.localStorage.getItem('diplomaone.website.saved'),b.savedValue);assert.equal(b.calls.auth,0);
});

test('direct deferred subject/unit routes do not fetch their content; a sixth unit of a visible subject still works',async t=>{
 const b=await boot(t);await b.ready('#home-search');
 for(const code of [fixture.codes.hiddenSemester,fixture.codes.hiddenBranch])for(const prefix of ['subject','unit']){
  await b.go('#/'+prefix+'/'+code+(prefix==='unit'?'/1':''),'[data-catalog-limited]');
 }
 assert(!b.calls.http.some(value=>value.startsWith('data/subjects/')||value.startsWith('data/units/')));
 await b.go('#/unit/'+fixture.codes.maths+'/6','#save-unit');assert(b.main.querySelector('.reader-title').textContent.includes('Offline unit 6'));
 assert(b.calls.http.some(value=>value.startsWith('data/units/'+fixture.codes.maths+'_u6.json')));assert.equal(b.calls.auth,0);
});

test('translated menu is keyboard-closeable, shows active parent routes and keeps account/support links',async t=>{
 const b=await boot(t);await b.ready('#home-search');b.click('#menu-toggle');
 assert.equal(b.d.querySelector('#mobile-nav').hidden,false);assert.equal(b.d.querySelector('#menu-toggle').getAttribute('aria-expanded'),'true');
 b.w.dispatchEvent(new b.w.KeyboardEvent('keydown',{key:'Escape',cancelable:true}));
 assert.equal(b.d.querySelector('#mobile-nav').hidden,true);assert.equal(b.d.activeElement.id,'menu-toggle');
 b.click('#menu-toggle');b.click('#mobile-nav a[href="#/branches"]');await b.ready('#results .branch-card');
 assert.equal(b.d.querySelector('#mobile-nav').hidden,true);
 await b.go('#/branch/mechanical/3','.subject-card');
 assert.equal(b.d.querySelector('.desktop-nav [data-nav="branches"]').getAttribute('aria-current'),'page');
 b.click('#lang-toggle');await waitFor(()=>b.d.documentElement.lang==='gu'&&b.main.textContent.includes('સેમેસ્ટર'));
 assert.equal(b.d.querySelector('.desktop-nav [data-nav="branches"]').textContent,'અભ્યાસ નોટ્સ');
 assert.equal(b.d.querySelector('.footer-tools summary').textContent,'વધુ સાધનો');assert.equal(b.d.querySelector('#menu-toggle').getAttribute('aria-label'),'નેવિગેશન ખોલો');
 for(const href of ['#/account','#/purchases','#/privacy','#/purchase-info'])assert(b.d.querySelector('a[href="'+href+'"]'));
 assert.equal(b.calls.auth,0);
});

test('catalog visibility is not an ownership gate: existing owners can reopen a hidden historical paper while sales are off',async t=>{
 const b=await boot(t,{owner:true,hash:'#/purchases'});await b.ready('.purchase-item a');assert(b.main.querySelector('.purchase-item a').href.endsWith('#/paper/'+fixture.codes.hiddenSemester+'/'+fixture.session));
 await b.go('#/paper/'+fixture.codes.hiddenSemester+'/'+fixture.session,'.solved-paper details.card');
 assert(b.main.querySelector('.solved-paper').textContent.includes('OWNED PRIVATE FIXTURE'));assert(b.calls.privateReads>0);
 assert(!b.calls.http.some(value=>value.includes('/papers/'+fixture.codes.hiddenSemester+'/')),'never re-open a paid public source');
 assert(!b.calls.http.some(value=>value.endsWith('/orders')));assert(!b.d.querySelector('script[src*="razorpay"]'));
});
