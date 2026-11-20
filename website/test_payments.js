// Offline real helper with HTTP/Checkout/SDK boundaries replaced. Never makes
// a Razorpay/Firebase/cloud request and never uses owner credentials.
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const source=fs.readFileSync(path.join(__dirname,'auth/payment-client.js'),'utf8');
const helper=import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
const id='DI03000161--summer-2026',other='DI03000171--summer-2026',origin='https://www.diplomaone.in';
const token='offlineFixture.onlyNotReal.signature',keyId='rzp_live_OfflineFixtureOnly';
const selected={id,title:'Manufacturing – I · Summer 2026',branch:'mechanical',amount:2900,currency:'INR'};
const configuration={mode:'live',enabled:true,keyId,currency:'INR',products:[selected]};
const order={mode:'live',keyId,orderId:'order_OfflineFixture',productId:id,amount:2900,currency:'INR'};
const proof={razorpay_order_id:order.orderId,razorpay_payment_id:'pay_OfflineFixture',razorpay_signature:'0'.repeat(64)};
const reader=Buffer.from('<main><details><summary>Question</summary><div class="answer">PRIVATE OFFLINE FIXTURE</div></details></main>');
const readerId='a'.repeat(64),imageId='b'.repeat(64),pdfId='c'.repeat(64),image=Buffer.from('offline fixture image'),pdf=Buffer.from('%PDF-fixture');
const assets=[{id:readerId,path:'summer-2026.html',mime:'text/plain; charset=utf-8',bytes:reader.length},
 {id:imageId,path:'summer-2026.assets/0001.webp',mime:'image/webp',bytes:image.length},
 {id:pdfId,path:'summer-2026.solution.pdf',mime:'application/pdf',bytes:pdf.length}];
const manifest={mode:'live',productId:id,readerAsset:readerId,assets};
const purchase={productId:id,title:selected.title,branch:'mechanical',amount:2900,currency:'INR',active:true,purchasedAt:'2026-10-30T00:00:00.000Z'};
const deferred=()=>{let resolve,reject;const promise=new Promise((a,b)=>{resolve=a;reject=b;});return {resolve,reject,promise};};
const tick=()=>new Promise(resolve=>setImmediate(resolve)),failure=code=>({ok:false,code});
async function fixture(options={}){
 const calls={token:0,http:[],checkout:[],open:0,close:0,scripts:[],blobs:[],revoked:[]};
 const state={user:{getIdToken(){++calls.token;return options.getToken?options.getToken():Promise.resolve(token);}}};
 const location={origin:options.origin??origin,hash:options.hash??'#/paper/'+id.replace('--','/')};
 const win={},document={head:{appendChild(script){calls.scripts.push(script);options.script?.(script,win);}},createElement(){return {remove(){this.removed=true;}};}};
 class Checkout {constructor(settings){this.settings=settings;this.events={};calls.checkout.push(this);}
  on(name,cb){this.events[name]=cb;}open(){++calls.open;options.open?.(this);}close(){++calls.close;this.settings.modal.ondismiss();}}
 if(!options.loadScript)win.Razorpay=Checkout;
 const defaultResponse=(url)=>{
  if(url.endsWith('/config'))return Response.json(configuration);
  if(url.endsWith('/orders'))return Response.json(order,{status:201});
  if(url.endsWith('/verify'))return Response.json({mode:'live',productId:id,owned:true});
  if(url.endsWith('/purchases'))return Response.json({mode:'live',purchases:[purchase]});
  if(url.endsWith('/content/'+id))return Response.json(manifest);
  const asset=assets.find(a=>url.endsWith('/'+a.id));
  if(asset)return new Response(asset.id===readerId?reader:asset.id===imageId?image:pdf,{headers:{'Content-Type':asset.mime}});
  throw Error('Unexpected offline endpoint');
 };
 const {createPaymentClient}=await helper;
 const client=createPaymentClient(()=>state.user,{location,window:win,document,timeoutMs:options.timeoutMs??1000,checkoutTimeoutMs:options.checkoutTimeoutMs??1000,
  url:{createObjectURL(blob){calls.blobs.push(blob);return 'blob:offline-fixture-'+calls.blobs.length;},revokeObjectURL(value){calls.revoked.push(value);}},
  fetcher(url,init){calls.http.push([url,init]);return options.fetch?options.fetch(url,init,defaultResponse):Promise.resolve(defaultResponse(url));}});
 return {client,calls,state,location,window:win};
}
async function checkout(f){const result=f.client.buy(id);await tick();assert.equal(f.calls.checkout.length,1);return {result,instance:f.calls.checkout[0]};}

test('helper is lazy, narrow and sends Google tokens only in fixed same-origin Authorization headers',async()=>{
 const f=await fixture();assert.equal(f.calls.token,0);assert.equal(f.calls.http.length,0);
 assert.deepEqual(Object.keys(f.client).sort(),['buy','cancel','configuration','dispose','purchases','readAsset','readPaper']);
 const config=await f.client.configuration();assert(config.ok);assert.equal(f.calls.token,0);
 const paper=await f.client.readPaper(id);assert(paper.ok);assert.equal(paper.html,reader.toString());
 for(const [url,init] of f.calls.http){
  assert(url.startsWith('/api/payments/live/'));assert(!url.includes(token));assert.equal(init.cache,'no-store');assert.equal(init.redirect,'error');
  assert.equal(init.credentials,'same-origin');assert(init.signal instanceof AbortSignal);
  if(!url.endsWith('/config'))assert.equal(init.headers.Authorization,'Bearer '+token);
  assert(!String(init.body).includes(token));
 }
 assert(!JSON.stringify(paper).includes(token));f.client.dispose();
});
test('non-production origins, wrong pages, free subjects, traversal and missing sessions cannot send a token or create an order',async()=>{
 for(const wrong of ['https://sunilpa4.github.io','https://diplomaone.in','http://localhost:8000',origin+'.evil.invalid',origin+':444',
  'https://deploy-preview-37--vermillion-pothos-520a34.netlify.app']){
  const f=await fixture({origin:wrong});assert.deepEqual(await f.client.buy(id),failure('payment_site_required'));
  assert.equal(f.calls.token,0);assert.equal(f.calls.http.length,0);
 }
 const f=await fixture();for(const bad of ['DI01000021--summer-2026','DI01000121--summer-2026','../'+id,id+'\n','x',id+'/../x']){
  assert.deepEqual(await f.client.buy(bad),failure('paper_unavailable'));assert.equal(f.calls.http.length,0);
 }
 f.location.hash='#/account';assert.deepEqual(await f.client.buy(id),failure('session_changed'));assert.equal(f.calls.token,0);
 f.location.hash='#/paper/'+id.replace('--','/');f.state.user=null;assert.deepEqual(await f.client.buy(id),failure('sign_in_required'));
 assert.equal(f.calls.http.length,0);
});
test('an off, malformed, test-mode or unavailable config cannot load Checkout or create orders',async()=>{
 for(const body of [{mode:'live',enabled:false},{...configuration,mode:'test'}, {...configuration,keyId:'rzp_test_OfflineFixtureOnly'},
  {...configuration,products:[{...selected,amount:1}]},{...configuration,products:[{...selected,id:other}]},
  {...configuration,products:[selected,selected]}, {...configuration,enabled:'true'}]){
  const f=await fixture({fetch:async()=>Response.json(body)});assert.equal((await f.client.buy(id)).ok,false);
  assert.equal(f.calls.checkout.length,0);assert.equal(f.calls.http.length,1);
 }
});
test('buy uses only the server order/price/live key; duplicate clicks share one order and a second paper cannot start concurrently',async()=>{
 const f=await fixture(),promise=f.client.buy(id);assert.equal(f.client.buy(id),promise);
 assert.deepEqual(await f.client.buy(other),failure('checkout_unavailable'));await tick();
 const options=f.calls.checkout[0].settings;assert.equal(options.order_id,order.orderId);assert.equal(options.amount,2900);assert.equal(options.key,keyId);
 assert(!JSON.stringify(options).includes(token));assert(!JSON.stringify(options).includes('Authorization'));assert.equal(options.prefill,undefined);
 const body=JSON.parse(f.calls.http.find(([url])=>url.endsWith('/orders'))[1].body);
 assert.deepEqual(Object.keys(body).sort(),['productId','requestId']);assert.equal(body.productId,id);
 assert.match(body.requestId,/^[a-f0-9-]{36}$/);assert.equal(f.calls.http.filter(([url])=>url.endsWith('/orders')).length,1);
 options.modal.ondismiss();assert.deepEqual(await promise,failure('checkout_closed'));f.client.dispose();
});
test('a Checkout callback cannot unlock until the server confirms this exact selected paper',async()=>{
 const gate=deferred(),f=await fixture({fetch:async(url,init,defaultResponse)=>url.endsWith('/verify')?gate.promise:defaultResponse(url)});
 const {result,instance}=await checkout(f);let settled=false;result.then(()=>{settled=true;});
 instance.settings.handler(proof);await tick();assert.equal(settled,false);
 const verify=f.calls.http.find(([url])=>url.endsWith('/verify'));assert(verify);
 assert.deepEqual(JSON.parse(verify[1].body),{orderId:order.orderId,paymentId:proof.razorpay_payment_id,signature:proof.razorpay_signature});
 instance.settings.modal.ondismiss();await tick();assert.equal(settled,false,'automatic dismissal must not cancel capture verification');
 gate.resolve(Response.json({mode:'live',productId:id,owned:true,token:'NEVER_RETURN',documents:['NEVER_RETURN']}));
 assert.deepEqual(await result,{ok:true,productId:id});f.client.dispose();
});
test('callback spoofing, cross-paper success, authorized-only/capture failures and test grants never unlock',async()=>{
 for(const response of [{mode:'live',productId:other,owned:true},{mode:'live',productId:id,owned:false},{mode:'test',productId:id,owned:true},
  {mode:'live',error:'payment_not_captured_or_mismatch'}]){
  const f=await fixture({fetch:async(url,init,defaultResponse)=>url.endsWith('/verify')?Response.json(response,{status:response.error?409:200}):defaultResponse(url)});
  const {result,instance}=await checkout(f);instance.settings.handler(proof);assert.equal((await result).ok,false);f.client.dispose();
 }
 for(const patch of [{razorpay_order_id:'order_OtherFixture'},{razorpay_signature:'bad'},{razorpay_payment_id:'pay_bad\n'}]){
  const f=await fixture(),{result,instance}=await checkout(f);instance.settings.handler({...proof,...patch});assert.equal((await result).ok,false);
  assert(!f.calls.http.some(([url])=>url.endsWith('/verify')));f.client.dispose();
 }
});
test('cancellation, account change and navigation before hashchange prevent late tokens, callbacks and content',async()=>{
 const gate=deferred(),f=await fixture({getToken:()=>gate.promise});const pending=f.client.readPaper(id);
 f.location.hash='#/privacy';gate.resolve(token);assert.deepEqual(await pending,failure('session_changed'));assert.equal(f.calls.http.length,0);
 const g=await fixture(),{result,instance}=await checkout(g);g.state.user={getIdToken:async()=>token};
 instance.settings.handler(proof);assert.deepEqual(await result,failure('session_changed'));assert(!g.calls.http.some(([url])=>url.endsWith('/verify')));g.client.dispose();
 const response=deferred(),h=await fixture({fetch:()=>response.promise}),read=h.client.readPaper(id);await tick();h.client.cancel();
 assert.deepEqual(await read,failure('session_changed'));assert(h.calls.http[0][1].signal.aborted);
 response.resolve(Response.json(manifest));await tick();assert.equal(h.calls.http.length,1);h.client.dispose();
});
test('private images/PDFs are authorized fetches, manifest-scoped object URLs, revoked on navigation/logout; no public fallback',async()=>{
 const f=await fixture();assert.deepEqual(await f.client.readAsset(id,imageId),failure('purchase_required'));assert.equal(f.calls.http.length,0);
 await f.client.readPaper(id);const first=f.client.readAsset(id,imageId),second=f.client.readAsset(id,imageId);assert.equal(first,second);
 assert.deepEqual(await first,{ok:true,url:'blob:offline-fixture-1'});assert.equal(f.calls.blobs.length,1);
 assert.deepEqual(await f.client.readAsset(id,imageId),{ok:true,url:'blob:offline-fixture-1'});assert.equal(f.calls.blobs.length,1);
 assert.equal((await f.client.readAsset(id,pdfId)).url,'blob:offline-fixture-2');
 assert.deepEqual(await f.client.readAsset(other,imageId),failure('session_changed'));
 assert.deepEqual(await f.client.readAsset(id,'d'.repeat(64)),failure('purchase_required'));
 assert(f.calls.http.every(([url])=>url.startsWith('/api/payments/live/')));
 f.client.cancel();assert.deepEqual(f.calls.revoked,['blob:offline-fixture-1','blob:offline-fixture-2']);
 assert.deepEqual(await f.client.readAsset(id,imageId),failure('purchase_required'));f.client.dispose();
});
test('My purchases is a safe projection, never an empty success on failure or browser-trusted entitlement',async()=>{
 const f=await fixture({hash:'#/purchases'}),result=await f.client.purchases();assert.deepEqual(result,{ok:true,purchases:[purchase]});
 assert(Object.isFrozen(result.purchases));assert(Object.isFrozen(result.purchases[0]));
 for(const body of [{mode:'test',purchases:[purchase]},{mode:'live',purchases:[{...purchase,active:'yes'}]},
  {mode:'live',purchases:[{...purchase,productId:'../'+id}]},{mode:'live',purchases:[{...purchase,amount:1}]},
  {mode:'live',error:'NEVER_ECHO',documents:['NEVER_ECHO']}]){
  const g=await fixture({hash:'#/purchases',fetch:async()=>Response.json(body)});assert.equal((await g.client.purchases()).ok,false);g.client.dispose();
 }
 f.client.dispose();
});
test('HTML login gates, redirects, malformed/oversized JSON/assets and missing images fail closed without public retry',async()=>{
 const responses=[()=>new Response('<html>NEVER_ECHO</html>',{headers:{'Content-Type':'text/html'}}),
  ()=>new Response('x'.repeat(256*1024+1),{headers:{'Content-Type':'application/json'}}),
  ()=>new Response('bad',{headers:{'Content-Type':'application/json'}}),
  ()=>({redirected:true,ok:true}),()=>Response.json({mode:'live',error:'NEVER_ECHO'},{status:503})];
 for(const response of responses){const f=await fixture({fetch:async()=>response()});assert.deepEqual(await f.client.configuration(),failure('payments_unavailable'));f.client.dispose();}
 for(const assetResponse of [()=>new Response(image,{headers:{'Content-Type':'image/svg+xml'}}),
  ()=>new Response(Buffer.concat([image,Buffer.from('x')]),{headers:{'Content-Type':'image/webp'}}),
  ()=>Response.json({mode:'live',error:'asset_unavailable'},{status:503})]){
  const f=await fixture({fetch:async(url,init,defaultResponse)=>url.endsWith('/'+imageId)?assetResponse():defaultResponse(url)});
  await f.client.readPaper(id);assert.deepEqual(await f.client.readAsset(id,imageId),failure('payments_unavailable'));assert.equal(f.calls.blobs.length,0);
  assert.equal(f.calls.http.length,3);f.client.dispose();
 }
});
test('malformed manifests and tokens cannot expose paths or send credential headers',async()=>{
 for(const patch of [{productId:other},{readerAsset:'bad'},{assets:[]},{assets:[{...assets[0],path:'../reader.html'}]},
  {assets:[{...assets[0],bytes:5*1024*1024}]},{assets:[assets[0],assets[0]]},{assets:[{...assets[0],mime:'text/html'}]}]){
  const f=await fixture({fetch:async()=>Response.json({...manifest,...patch})});assert.equal((await f.client.readPaper(id)).ok,false);assert.equal(f.calls.http.length,1);f.client.dispose();
 }
 for(const value of ['',null,4,'x'.repeat(16001),token+'\n',token+'\r',token+' space']){
  const f=await fixture({getToken:async()=>value});assert.deepEqual(await f.client.readPaper(id),failure('sign_in_required'));assert.equal(f.calls.http.length,0);f.client.dispose();
 }
});
test('network, token and Checkout deadlines abort without automatic retries; failure closes the modal',async()=>{
 const gate=deferred(),f=await fixture({timeoutMs:10,getToken:()=>gate.promise}),pending=f.client.buy(id);
 assert.deepEqual(await pending,failure('payment_timeout'));gate.resolve(token);await tick();assert.equal(f.calls.http.length,0);f.client.dispose();
 const g=await fixture({timeoutMs:10,fetch:()=>new Promise(()=>{})});assert.deepEqual(await g.client.readPaper(id),failure('payment_timeout'));
 assert.equal(g.calls.http.length,1);assert(g.calls.http[0][1].signal.aborted);g.client.dispose();
 const h=await fixture(),{result,instance}=await checkout(h);instance.events['payment.failed']();assert.deepEqual(await result,failure('payment_failed'));assert.equal(h.calls.close,1);h.client.dispose();
 const j=await fixture({checkoutTimeoutMs:10}),r=j.client.buy(id);await tick();assert.equal((await r).ok,false);assert.equal(j.calls.close,1);j.client.dispose();
});
test('Checkout is loaded lazily from the exact provider script and never before live config permits it',async()=>{
 const f=await fixture({loadScript:true,script(script,win){win.Razorpay=class {constructor(settings){this.settings=settings;}on(){}open(){this.settings.modal.ondismiss();}close(){}};script.onload();}});
 assert.equal(f.calls.scripts.length,0);await f.client.configuration();assert.equal(f.calls.scripts.length,0);
 assert.deepEqual(await f.client.buy(id),failure('checkout_closed'));assert.equal(f.calls.scripts.length,1);
 const script=f.calls.scripts[0];assert.equal(script.src,'https://checkout.razorpay.com/v1/checkout.js');assert.equal(script.referrerPolicy,'no-referrer');
 assert.equal(script.async,true);assert.equal(f.calls.http.filter(([url])=>url.endsWith('/orders')).length,1);f.client.dispose();
});
