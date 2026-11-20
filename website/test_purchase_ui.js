// Real SPA + auth controller + private payment helper, entirely offline.
// Only Firebase, HTTP service and Razorpay window boundaries are simulated.
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {JSDOM,VirtualConsole}=require('jsdom');
const site=path.resolve(process.argv[2]||__dirname),{createAuthController}=require(path.join(site,'auth.js'));
const helper=import('data:text/javascript;base64,'+Buffer.from(fs.readFileSync(path.join(__dirname,'auth/payment-client.js'),'utf8')).toString('base64'));
const code='DI03000161',session='summer-2026',id=code+'--'+session,other='DI03000171',hash='#/paper/'+code+'/'+session;
const keyId='rzp_live_OfflineFixtureOnly',imageId='b'.repeat(64),readerId='a'.repeat(64),pdfId='c'.repeat(64);
const privateHTML='<main><section><h2>Question 1</h2><details class="card"><summary><strong class="en">Q.1 (c) OR · Selected question</strong><strong class="gu">Q.1 (c) OR · પસંદ કરેલો પ્રશ્ન</strong></summary><div class="answer"><div class="en"><p>PRIVATE SELECTED ANSWER <span class="frac"><span class="num">a</span><span class="den">b</span></span></p></div><div class="gu"><p>ખાનગી પસંદ કરેલો જવાબ</p></div><figure><img src="summer-2026.assets/0001.webp" alt="Protected diagram"></figure></div></details></section></main>';
const images=Buffer.from('offline fixture image'),pdf=Buffer.from('%PDF-fixture'),reader=Buffer.from(privateHTML);
const assets=[{id:readerId,path:session+'.html',mime:'text/plain; charset=utf-8',bytes:reader.length},
 {id:imageId,path:session+'.assets/0001.webp',mime:'image/webp',bytes:images.length},{id:pdfId,path:session+'.solution.pdf',mime:'application/pdf',bytes:pdf.length}];
const user=uid=>({uid,displayName:'Offline Student',email:'fixture@example.test',emailVerified:true,getIdToken:async()=>uid+'.offlineFixture.signature'});
const catalog={branches:[{key:'mechanical',code:'19',name:{en:'Mechanical',gu:'મિકેનિકલ'},semesters:{'3':[code,other]}},
 {key:'computer',code:'07',name:{en:'Computer'},semesters:{'1':['DI01000131']}},{key:'electrical',code:'09',name:{en:'Electrical'},semesters:{'3':['DI03009011']}},
 {key:'civil',code:'06',name:{en:'Civil'},semesters:{'3':['DI03006011']}},{key:'chemical',code:'05',name:{en:'Chemical'},semesters:{'3':['DI03005011']}}],
 subjects:{[code]:{code,name:{en:'Manufacturing I',gu:'મેન્યુફેક્ચરિંગ I'},status:'available'},[other]:{code:other,name:{en:'Metrology'},status:'available'},DI01000021:{code:'DI01000021',name:{en:'Maths I'}}}};
const tick=()=>new Promise(resolve=>setImmediate(resolve));
async function waitFor(fn,label='view'){for(let n=0;n<200;n++){if(fn())return;await tick();}throw Error('Timed out: '+label);}
const deferred=()=>{let resolve;const promise=new Promise(r=>{resolve=r;});return {resolve,promise};};
async function boot(t,{initialUser=null,enabled=true,owned=new Set(),initialHash=hash,origin='https://www.diplomaone.in',verifyGate=null,captured=true,assetFailure=false,failTree=false,extraProduct=null}={}){
 const errors=[],vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e.message));
 const dom=new JSDOM(fs.readFileSync(path.join(site,'index.html'),'utf8'),{url:origin+'/'+initialHash,runScripts:'outside-only',virtualConsole:vc});
 const w=dom.window,d=w.document,calls={http:[],public:[],orders:0,verify:0,load:0,signIn:0,checkout:[],blobs:[],revoked:[]};
 const state={user:initialUser,enabled,owned,captured},on={};w.scrollTo=()=>{};w.console.error=e=>errors.push(e?.message||String(e));
 const product=(productId=id)=>({id:productId,title:'Manufacturing I · Summer 2026',branch:'mechanical',amount:2900,currency:'INR'});
 const config=()=>({mode:'live',enabled:state.enabled,keyId,currency:'INR',products:state.enabled?[product(),product(other+'--'+session),...(extraProduct?[{...product(extraProduct),title:'New private import'}]:[])]:[]});
 async function http(url,init={}){
  calls.http.push([url,init]);
  if(url.endsWith('/config'))return Response.json(config());
  assert.equal(init.headers.Authorization,'Bearer '+state.user.uid+'.offlineFixture.signature');
  if(url.endsWith('/orders')){++calls.orders;const body=JSON.parse(init.body);assert.equal(body.productId,id);assert.equal(body.amount,undefined);
   return Response.json({mode:'live',keyId,orderId:'order_OfflineFixture',productId:id,amount:2900,currency:'INR'},{status:201});}
  if(url.endsWith('/verify')){++calls.verify;if(verifyGate)await verifyGate.promise;
   if(!state.captured)return Response.json({mode:'live',error:'payment_not_captured_or_mismatch'},{status:409});
   state.owned.add(state.user.uid+':'+id);return Response.json({mode:'live',productId:id,owned:true});}
  if(url.endsWith('/purchases'))return Response.json({mode:'live',purchases:state.owned.has(state.user.uid+':'+id)?[
   {productId:id,title:'Manufacturing I',branch:'mechanical',amount:2900,currency:'INR',active:true,purchasedAt:'2026-10-30T00:00:00.000Z'}]:[]});
  const content=/\/content\/([^/]+)(?:\/([^/]+))?$/.exec(url);assert(content,'unexpected offline API path');
  if(!state.owned.has(state.user.uid+':'+content[1]))return Response.json({mode:'live',error:'purchase_required'},{status:403});
  if(!content[2])return Response.json({mode:'live',productId:content[1],readerAsset:readerId,assets});
  const asset=assets.find(a=>a.id===content[2]);assert(asset);
  if(assetFailure&&asset.id===imageId)return Response.json({mode:'live',error:'asset_unavailable'},{status:503});
  return new Response(asset.id===readerId?reader:asset.id===imageId?images:pdf,{headers:{'Content-Type':asset.mime}});
 }
 w.fetch=async(url,init)=>{
  if(String(url).startsWith('/api/'))return http(url,init);
  calls.public.push(String(url));
  if(String(url).startsWith('data/catalog'))return Response.json(catalog);
  if(String(url).startsWith('https://api.github.com/'))return failTree?new Response(null,{status:503}):Response.json({truncated:false,tree:[code,other,'DI01000021','DI01000121','DI01000131','DI03009011','DI03006011','DI03005011'].flatMap(c=>[
   {path:`papers/${c}/${session}.json`,type:'blob',mode:'100644'},
   ...(c.startsWith('DI01000')&&['DI01000021','DI01000121'].includes(c)?[{path:`papers/${c}/${session}.html`,type:'blob',mode:'100644'}]:[])])});
  if(String(url).includes('/papers/DI01000021/')||String(url).includes('/papers/DI01000121/'))return new Response('<main><details><summary>Free question</summary><div class="answer">FREE ANSWER</div></details></main>');
  throw Error('Public paid-answer fallback attempted');
 };
 class Checkout{constructor(settings){this.settings=settings;this.events={};calls.checkout.push(this);}on(name,cb){this.events[name]=cb;}open(){}close(){this.settings.modal.ondismiss();}}
 w.Razorpay=Checkout;
 const {createPaymentClient}=await helper;
 w.DiplomaOneAuth=createAuthController(async()=>{++calls.load;return {createClient(emit){
  on.emit=emit;emit(state.user);const payments=createPaymentClient(()=>state.user,{fetcher:http,location:w.location,window:w,document:d,timeoutMs:1000,checkoutTimeoutMs:2000,
   url:{createObjectURL(){const value='blob:offline-ui-'+(calls.blobs.length+1);calls.blobs.push(value);return value;},revokeObjectURL(value){calls.revoked.push(value);}}});
  on.payments=payments;return {ready:async()=>{},dispose(){payments.dispose();},signIn(){++calls.signIn;state.user=user('alice');payments.cancel();emit(state.user);return Promise.resolve();},
   signOut(){state.user=null;payments.cancel();emit(null);return Promise.resolve();},
   cancelPayments:()=>payments.cancel(),paymentConfiguration:()=>payments.configuration(),loadPurchases:()=>payments.purchases(),
   readPurchasedPaper:value=>payments.readPaper(value),readPurchasedAsset:(value,asset)=>payments.readAsset(value,asset),buyPaper:value=>payments.buy(value)};
 }};});
 w.eval(fs.readFileSync(path.join(site,'app.js'),'utf8'));
 t.after(()=>{on.payments?.dispose();dom.window.close();});
 const go=async value=>{w.location.hash=value;await tick();await tick();};
 return {w,d,calls,state,errors,on,go,emit(value){state.user=value;on.payments.cancel();on.emit(value);},
  click(selector){const element=d.querySelector(selector);assert(element,'missing '+selector);element.click();return element;},
  async capture(){const instance=calls.checkout.at(-1);assert(instance);await instance.settings.handler({razorpay_order_id:'order_OfflineFixture',razorpay_payment_id:'pay_OfflineFixture',razorpay_signature:'0'.repeat(64)});}};
}
test('price labels are per real selected paper; all paid answer fetches stay locked before sign-in',async t=>{
 const b=await boot(t,{initialHash:'#/papers'});await waitFor(()=>b.d.querySelector('.paper-access-label'));
 const labels=[...b.d.querySelectorAll('.paper-access-label')].map(e=>e.textContent).join(' ');for(const price of ['₹19','₹29','₹39','Free'])assert(labels.includes(price));
 assert.equal(b.calls.load,0,'listing metadata must not initialize Firebase');assert.equal(b.calls.orders,0);
 await b.go(hash);await waitFor(()=>b.d.querySelector('#paper-signin')&&!b.d.querySelector('#paper-signin').disabled);
 assert(b.d.querySelector('.paper-price').textContent.includes('₹29'));assert(!b.d.querySelector('.solved-paper'));
 assert.equal(b.calls.orders,0);assert(!b.calls.public.some(url=>url.includes('/papers/'+code+'/')));
 assert.equal(b.w.sessionStorage.length,0);assert.equal(b.w.localStorage.length,0);assert.deepEqual(b.errors,[]);
});
test('Google → server order → Checkout → server capture → only selected cards; purchases persist after navigation/reload',async t=>{
 const gate=deferred(),b=await boot(t,{verifyGate:gate});await waitFor(()=>b.d.querySelector('#paper-signin')&&!b.d.querySelector('#paper-signin').disabled);
 b.click('#paper-signin');await waitFor(()=>b.d.querySelector('#buy-paper')&&!b.d.querySelector('#buy-paper').disabled);
 assert.equal(b.calls.signIn,1);assert.equal(b.calls.orders,0);
 const old=b.click('#buy-paper');old.click();await waitFor(()=>b.calls.checkout.length===1);assert.equal(b.calls.orders,1);
 b.capture();await waitFor(()=>b.calls.verify===1);assert(!b.d.querySelector('.solved-paper'),'callback alone is not content authorization');
 gate.resolve();await waitFor(()=>b.d.querySelector('.solved-paper details'));
 assert(b.d.querySelector('.solved-paper').textContent.includes('PRIVATE SELECTED ANSWER'));
 assert(b.d.querySelector('.frac .num'));assert(b.d.querySelector('summary').textContent.includes('OR'));
 const img=b.d.querySelector('img[data-private-asset]');assert(img&&!img.getAttribute('src'));
 b.click('[data-paper-expand="true"]');await waitFor(()=>img.getAttribute('src')?.startsWith('blob:'));
 assert.equal(b.calls.blobs.length,1);assert(!b.d.querySelector('.paper-downloads a[href^="https:"]'));
 b.click('#lang-toggle');await waitFor(()=>b.d.querySelector('.solved-paper')?.textContent.includes('ખાનગી પસંદ કરેલો જવાબ'));
 assert(!b.d.querySelector('.solved-paper').textContent.includes('PRIVATE SELECTED ANSWER'));
 await b.go('#/purchases');await waitFor(()=>b.d.querySelector('.purchase-item a'));
 assert(b.d.querySelector('.purchase-item a').href.endsWith(hash));assert.equal(b.calls.revoked.length,1);
 await b.go('#/paper/'+other+'/'+session);await waitFor(()=>b.d.querySelector('#buy-paper')&&!b.d.querySelector('#buy-paper').disabled);
 assert(!b.d.querySelector('.solved-paper'));assert.equal(b.calls.orders,1);
 await b.go(hash);await waitFor(()=>b.d.querySelector('.solved-paper details'));assert.equal(b.calls.orders,1);
 const reloaded=await boot(t,{initialUser:user('alice'),owned:b.state.owned,initialHash:'#/purchases'});
 await waitFor(()=>reloaded.d.querySelector('.purchase-item a'));assert.equal(reloaded.calls.orders,0);
 assert(!b.calls.public.some(url=>url.includes('/papers/'+code+'/')));
 assert(b.calls.http.filter(([url])=>url.includes('/content/')).every(([,init])=>init.headers.Authorization));
 assert(!b.d.body.textContent.includes('offlineFixture.signature'));assert.equal(b.w.localStorage.length,1);assert.equal(b.w.sessionStorage.length,0);
 assert.deepEqual(b.errors,[]);assert.deepEqual(reloaded.errors,[]);
});
test('new private products remain discoverable during a public GitHub outage without initializing Auth or reading public paid answers',async t=>{
 const newId='DI03999999--winter-2029',b=await boot(t,{initialHash:'#/papers',failTree:true,extraProduct:newId});
 await waitFor(()=>b.d.querySelector('a[href="#/paper/DI03999999/winter-2029"]'));
 const card=b.d.querySelector('a[href="#/paper/DI03999999/winter-2029"]');assert(card.textContent.includes('₹29'));
 assert(b.d.querySelector('.reader-notice').textContent.includes('could not be updated'));
 assert.equal(b.calls.load,0);assert.equal(b.calls.orders,0);
 assert(!b.calls.public.some(url=>url.includes('/papers/DI03999999/')));
 assert(b.errors.every(message=>message==='Paper list unavailable'));
});
test('off checkout still shows the agreed price and never creates orders or loads Checkout',async t=>{
 const b=await boot(t,{initialUser:user('alice'),enabled:false});await waitFor(()=>b.d.querySelector('#paper-payment-status')?.textContent.includes('not open yet'));
 assert(b.d.querySelector('#buy-paper').disabled);assert(b.d.querySelector('.paper-price').textContent.includes('₹29'));
 b.click('#buy-paper');assert.equal(b.calls.orders,0);assert.equal(b.calls.checkout.length,0);
 assert(!b.d.querySelector('script[src*="razorpay"]'));assert(!b.d.querySelector('.solved-paper'));assert.deepEqual(b.errors,[]);
});
test('authorized/pending capture never opens answers; My purchases refresh handles later webhook confirmation without another payment',async t=>{
 const b=await boot(t,{initialUser:user('alice'),captured:false});await waitFor(()=>b.d.querySelector('#buy-paper')&&!b.d.querySelector('#buy-paper').disabled);
 b.click('#buy-paper');await waitFor(()=>b.calls.checkout.length);await b.capture();
 await waitFor(()=>b.d.querySelector('#paper-payment-status')?.textContent.includes('not been confirmed as fully captured'));
 assert(!b.d.querySelector('.solved-paper'));assert.equal(b.calls.orders,1);
 await b.go('#/purchases');await waitFor(()=>b.d.querySelector('[data-purchases-panel]')?.textContent.includes('No confirmed purchases'));
 // Simulate the independently tested captured webhook, not a browser write.
 b.state.owned.add('alice:'+id);b.click('#purchases-refresh');await waitFor(()=>b.d.querySelector('.purchase-item a'));
 b.click('.purchase-item a');await waitFor(()=>b.d.querySelector('.solved-paper details'));assert.equal(b.calls.orders,1);assert.deepEqual(b.errors,[]);
});
test('another account/logout removes private bytes and revokes object URLs; no stale callback or public fallback can re-open them',async t=>{
 const owned=new Set(['alice:'+id]),b=await boot(t,{initialUser:user('alice'),owned});await waitFor(()=>b.d.querySelector('.solved-paper details'));
 b.click('[data-paper-expand="true"]');await waitFor(()=>b.calls.blobs.length===1);
 b.emit(user('bob'));assert(!b.d.querySelector('.solved-paper')?.textContent.includes('PRIVATE SELECTED ANSWER'));
 await waitFor(()=>b.d.querySelector('#buy-paper')&&!b.d.querySelector('#buy-paper').disabled);
 assert(!b.d.querySelector('.solved-paper'));assert.equal(b.calls.revoked.length,1);
 await b.go('#/purchases');await waitFor(()=>b.d.querySelector('[data-purchases-panel]')?.textContent.includes('No confirmed purchases'));
 assert(!b.d.querySelector('.purchase-item'));assert.equal(b.calls.orders,0);assert.deepEqual(b.errors,[]);
});
test('failed private images never request public copies; free Maths/Physics still read without account',async t=>{
 const b=await boot(t,{initialUser:user('alice'),owned:new Set(['alice:'+id]),assetFailure:true});await waitFor(()=>b.d.querySelector('.solved-paper details'));
 b.click('[data-paper-expand="true"]');await waitFor(()=>b.d.querySelector('#private-asset-status')?.textContent.includes('no public copy'));
 assert.equal(b.calls.blobs.length,0);assert(!b.calls.public.some(url=>url.includes('/papers/'+code+'/')));
 const f=await boot(t,{initialHash:'#/paper/DI01000021/'+session});await waitFor(()=>f.d.querySelector('.solved-paper details'));
 assert(f.d.querySelector('.solved-paper').textContent.includes('FREE ANSWER'));assert.equal(f.calls.load,0);assert.equal(f.calls.orders,0);
 assert.deepEqual(b.errors,[]);assert.deepEqual(f.errors,[]);
});
test('unapproved hosts remain locked without loading auth, and purchase information does not invent launch policies',async t=>{
 const b=await boot(t,{origin:'https://deploy-preview-37--example.netlify.app'});await waitFor(()=>b.d.querySelector('[data-paid-paper]'));
 assert.equal(b.calls.load,0);assert.equal(b.calls.orders,0);assert(!b.d.querySelector('#buy-paper'));
 assert(b.d.querySelector('a[href^="https://www.diplomaone.in/#/paper/"]'));
 await b.go('#/purchase-info');await waitFor(()=>b.d.querySelector('h2')?.textContent==='Sales are not open yet');
 assert(b.d.querySelector('#main').textContent.includes('access duration'));assert.equal(b.calls.load,0);assert.deepEqual(b.errors,[]);
});
