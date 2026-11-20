// Offline/genuine DEMO-emulator only. All keys, users and payments are fixtures.
import {test,beforeEach,after} from 'node:test';
import assert from 'node:assert/strict';
import {randomUUID} from 'node:crypto';
import {store} from './store.mjs';
import {fixtureFirestoreEnv} from './credentials.mjs';
import {Repository} from '../src/repository.mjs';
import {createHandler} from '../src/api.mjs';
import {razorpayClient} from '../src/razorpay.mjs';
import {readConfig,Problem,TEST_SITE_ORIGIN,digest,hmac} from '../src/domain.mjs';
const {database,repository:testing,reset}=store(),live=new Repository(database,{mode:'live'});
const bytes=Buffer.from('PRIVATE LIVE FIXTURE, NOT REAL CONTENT'),asset=digest(bytes),id='DI03000161--summer-2026';
const product={id,title:'Fixture paper',branch:'mechanical',reader_asset:asset,
 assets:[{id:asset,path:'reader.html',mime:'text/plain; charset=utf-8',bytes:bytes.length}]};
const env={...fixtureFirestoreEnv,CONTEXT:'production',RAZORPAY_LIVE_KEY_ID:'rzp_live_OnlyFixture12345',
 RAZORPAY_LIVE_KEY_SECRET:'live-fixture-only-not-real-00000',RAZORPAY_LIVE_WEBHOOK_SECRET:'live-webhook-fixture-not-real-00000',
 PAYMENTS_LIVE_ENABLED:'true',PAYMENTS_LIVE_PRIVATE_MIGRATION_CONFIRMED:'true',PAYMENTS_LIVE_MERCHANT_CONFIRMED:'true',PAYMENTS_LIVE_POLICIES_CONFIRMED:'true'};
beforeEach(async()=>{await reset();await live.importProduct(product);});
after(()=>database.terminate());
function fixture({changes={},ready=true}={}){
 const config=readConfig({...env,...changes},'live'),orders=new Map(),payments=new Map(),calls={create:0,read:0};
 const provider={async createOrder(o){++calls.create;const p={id:'order_liveFixture123',receipt:o.receipt,amount:o.amount,
 currency:'INR',status:'created',partial_payment:false};orders.set(p.id,p);return p;},
 async order(id){++calls.read;return orders.get(id);},async payment(id){++calls.read;return payments.get(id);}};
 const handler=createHandler({config,repository:live,provider,
  verifyIdentity:async header=>{if(!/^Bearer customer-[ab]$/.test(header||''))throw new Problem(401,'sign_in_required');return {uid:header.slice(7)};},
  assets:{ready:async()=>ready,get:async()=>new Uint8Array(bytes).buffer}});
 async function request(path,{method='GET',user='customer-a',body,url=TEST_SITE_ORIGIN+'/api/payments/live'+path,headers={}}={}){
  const r=await handler(new Request(url,{method,headers:{...(user?{Authorization:'Bearer '+user}:{}),
   ...(method==='POST'?{Origin:new URL(url).origin,'Content-Type':'application/json'}:{}),...headers},
   ...(body!==undefined?{body:typeof body==='string'?body:JSON.stringify(body)}:{})}));
  return {status:r.status,headers:r.headers,body:r.headers.get('Content-Type')?.startsWith('application/json')?await r.json():await r.text()};
 }
 async function order(){return request('/orders',{method:'POST',body:{productId:id,requestId:randomUUID()}});}
 function capture(){const o=orders.get('order_liveFixture123');Object.assign(o,{status:'paid',amount_paid:o.amount,amount_due:0});
 const p={id:'pay_liveFixture123',order_id:o.id,status:'captured',captured:true,amount:o.amount,currency:'INR',amount_refunded:0};payments.set(p.id,p);return p;}
 async function verify(user='customer-a'){return request('/verify',{method:'POST',user,body:{orderId:'order_liveFixture123',paymentId:'pay_liveFixture123',signature:hmac(config.keySecret,'order_liveFixture123|pay_liveFixture123')}});}
 return {config,calls,request,order,capture,verify,orders,payments};
}
test('live is explicit, OFF by default, separately credentialed and cannot fall back to test keys',()=>{
 assert.equal(readConfig({},'live').enabled,false);assert.equal(readConfig(env,'live').enabled,true);
 assert.equal(readConfig(env).configured,false);assert.equal(readConfig({...env,RAZORPAY_LIVE_KEY_ID:'rzp_test_OnlyFixture12345'},'live').configured,false);
 for(const field of ['PAYMENTS_LIVE_ENABLED','PAYMENTS_LIVE_PRIVATE_MIGRATION_CONFIRMED','PAYMENTS_LIVE_MERCHANT_CONFIRMED','PAYMENTS_LIVE_POLICIES_CONFIRMED'])
  for(const value of ['',undefined,'false','TRUE'])assert.equal(readConfig({...env,[field]:value},'live').enabled,false,field);
 for(const context of ['deploy-preview','branch-deploy','',undefined])assert.equal(readConfig({...env,CONTEXT:context},'live').enabled,false);
 assert.throws(()=>readConfig(env,'other'),/invalid_payment_mode/);
 assert.throws(()=>razorpayClient({...readConfig(env,'live'),keyId:'rzp_test_OnlyFixture12345'}),/live_keys_required/);
 assert.throws(()=>razorpayClient({...readConfig(env),keyId:env.RAZORPAY_LIVE_KEY_ID}),/test_keys_required/);
 assert.equal(readConfig({...env,PAYMENTS_TEST_ENABLED:'false',PAYMENTS_PRIVATE_MIGRATION_CONFIRMED:'false'}).checkoutFlagsOff,false);
});
test('live and test products/orders/ownership are in distinct fixed namespaces',async()=>{
 assert.equal(live.root.path,'diplomaone_live/v1');assert.equal(testing.root.path,'diplomaone_test/v1');
 assert.equal(await testing.product(id),null);const f=fixture();assert.equal((await f.order()).status,201);
 f.capture();assert.equal((await f.verify()).body.mode,'live');assert.equal(await live.owns('customer-a',id),true);
 assert.equal(await testing.owns('customer-a',id),false);assert.equal((await testing.purchases('customer-a')).length,0);
 assert((await live.order('order_liveFixture123')).receipt.startsWith('dl_'));
});
test('live creates the exact selected paper at server price and opens only after canonical capture',async()=>{
 const f=fixture();const created=await f.order();assert.equal(created.status,201);assert.equal(created.body.mode,'live');assert.equal(created.body.amount,2900);
 assert.equal((await f.request('/content/'+id+'/'+asset)).status,403);
 const p=f.capture();p.status='authorized';p.captured=false;
 assert.equal((await f.verify()).status,409);assert.equal(await live.owns('customer-a',id),false);
 p.status='captured';p.captured=true;assert.equal((await f.verify('customer-b')).status,404);
 assert.equal((await f.verify()).status,200);assert.equal((await f.verify()).status,200);
 const content=await f.request('/content/'+id+'/'+asset);assert.equal(content.body,bytes.toString());assert.equal(content.headers.get('Cache-Control'),'private, no-store');
 assert.equal((await f.request('/content/'+id+'/'+asset,{user:'customer-b'})).status,403);
 const purchases=await f.request('/purchases');assert.equal(purchases.body.purchases.length,1);assert.equal(purchases.body.purchases[0].productId,id);
 assert.equal((await f.request('/purchases',{user:'customer-b'})).body.purchases.length,0);
 assert.equal(await live.owns('customer-a','DI03000171--winter-2025'),false);
});
test('live rejects arbitrary prices, unsigned sessions, wrong origin/context/host and missing private delivery before provider creation',async()=>{
 const f=fixture();assert.equal((await f.request('/orders',{method:'POST',user:null,body:{}})).status,401);
 assert.equal((await f.request('/orders',{method:'POST',body:{productId:id,requestId:randomUUID(),amount:1}})).status,400);
 assert.equal((await f.request('/orders',{method:'POST',body:{},headers:{Origin:'https://evil.invalid'}})).status,403);
 assert.equal((await f.request('/config',{url:'https://evil.invalid/api/payments/live/config'})).status,404);
 assert.equal((await fixture({changes:{CONTEXT:'deploy-preview'}}).request('/config')).status,404);
 assert.equal(f.calls.create,0);
 const missing=fixture({ready:false});assert.equal((await missing.order()).body.error,'private_paper_not_ready');assert.equal(missing.calls.create,0);
});
test('disabled live config has no database/provider work and each missing launch approval blocks order creation',async()=>{
 for(const field of ['PAYMENTS_LIVE_ENABLED','PAYMENTS_LIVE_PRIVATE_MIGRATION_CONFIRMED','PAYMENTS_LIVE_MERCHANT_CONFIRMED','PAYMENTS_LIVE_POLICIES_CONFIRMED']){
  const f=fixture({changes:{[field]:'false'}});const r=await f.request('/config',{user:null});assert.equal(r.body.enabled,false);assert.equal(r.body.products,undefined);
  assert.equal((await f.order()).body.error,'live_checkout_disabled');assert.equal(f.calls.create,0);
 }
});
test('paid live access survives pausing checkout, removing gateway keys and unlisting a product',async()=>{
 const f=fixture();await f.order();f.capture();await f.verify();
 await live.collection('products').doc(id).update({active:false});
 const paused=fixture({changes:{PAYMENTS_LIVE_ENABLED:'false',RAZORPAY_LIVE_KEY_SECRET:''}});
 assert.equal((await paused.request('/purchases')).body.purchases.length,1);
 assert.equal((await paused.request('/content/'+id+'/'+asset)).body,bytes.toString());
 assert.equal((await paused.order()).status,503);
});
test('an optional private pilot UID list limits only new live orders and invalid lists fail closed',async()=>{
 const pilot=fixture({changes:{PAYMENTS_LIVE_PILOT_UIDS:'customer-b'}});
 assert.equal((await pilot.order()).body.error,'live_pilot_only');assert.equal(pilot.calls.create,0);
 const created=await pilot.request('/orders',{method:'POST',user:'customer-b',body:{productId:id,requestId:randomUUID()}});
 assert.equal(created.status,201);pilot.capture();assert.equal((await pilot.verify('customer-b')).status,200);
 const changed=fixture({changes:{PAYMENTS_LIVE_PILOT_UIDS:'customer-a',PAYMENTS_LIVE_ENABLED:'false'}});
 assert.equal((await changed.request('/purchases',{user:'customer-b'})).body.purchases.length,1);
 assert.equal((await changed.request('/content/'+id+'/'+asset,{user:'customer-b'})).body,bytes.toString());
 assert.equal(readConfig({...env,PAYMENTS_LIVE_PILOT_UIDS:' , '},'live').enabled,false);
 assert.equal(readConfig({...env,PAYMENTS_LIVE_PILOT_UIDS:'x'.repeat(129)},'live').enabled,false);
 assert(!JSON.stringify((await pilot.request('/config')).body).includes('customer-b'));
});
test('signed live webhook fulfills a stored customer order even without browser callback; unrelated/test orders cannot unlock',async()=>{
 const f=fixture();await f.order();const p=f.capture();
 const raw=JSON.stringify({event:'payment.captured',payload:{payment:{entity:p}}});
 assert.equal((await f.request('/webhook',{method:'POST',user:null,body:raw,headers:{'x-razorpay-event-id':'evt_liveFixture',
  'x-razorpay-signature':hmac(f.config.webhookSecret,raw)}})).status,200);
 assert.equal(await live.owns('customer-a',id),true);
 assert.equal(await testing.owns('customer-a',id),false);
});
