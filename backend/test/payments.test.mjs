import {test,before,after,beforeEach} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {randomUUID} from 'node:crypto';
import {PGlite} from '@electric-sql/pglite';
import {Repository} from '../src/repository.mjs';
import {createHandler} from '../src/api.mjs';
import {readConfig,Problem,PREFIX,hmac,digest,MAX_ASSET_BYTES} from '../src/domain.mjs';

let database,repository;
const id='DI03000161--summer-2026',other='DI03000171--winter-2025';
const bytes=Buffer.from('PRIVATE UNIT TEST FIXTURE - NOT A PUBLISHED SOLUTION'),assetId=digest(bytes);
const product={id,title:'Manufacturing Engineering-I',branch:'mechanical',reader_asset:assetId,
  assets:[{id:assetId,path:'reader.html',mime:'text/plain; charset=utf-8',bytes:bytes.length}]};
const env={RAZORPAY_KEY_ID:'rzp_test_OnlyUnitTest123',RAZORPAY_KEY_SECRET:'test-only-key-secret-0123456789',
  RAZORPAY_WEBHOOK_SECRET:'test-only-webhook-secret-0123456789',NETLIFY_DB_URL:'postgres://unit.invalid/db',
  FIREBASE_PROJECT_ID:'diplomaone-53b4e',CONTEXT:'production',PAYMENTS_TEST_ENABLED:'true',PAYMENTS_PRIVATE_MIGRATION_CONFIRMED:'true',
  PAYMENTS_TESTER_UIDS:"alice,bob,u' OR 1=1--"};
const config=readConfig(env);

before(async()=>{
  database=new PGlite();
  await database.exec(await readFile(new URL('../../netlify/database/migrations/0001_test_payments.sql',import.meta.url),'utf8'));
  repository=new Repository({query:(...args)=>database.query(...args),
    transaction:fn=>database.transaction(tx=>fn((...args)=>tx.query(...args)))});
});
after(async()=>database?.close());
beforeEach(async()=>{
  await database.exec('TRUNCATE diplomaone_test.events,diplomaone_test.entitlements,diplomaone_test.orders,diplomaone_test.products CASCADE');
  await repository.importProduct(product);
});

function fixture(options={}){
  const calls={create:0,order:0,payment:0,asset:0},orders=new Map(),payments=new Map(),logs=[];
  const provider={
    async createOrder(stored){++calls.create;if(options.createError)throw options.createError;
      const order={id:'order_'+String(calls.create).padStart(12,'0'),receipt:stored.receipt,amount:stored.amount,currency:'INR',
        status:'created',amount_paid:0,amount_due:stored.amount,partial_payment:false,...options.createOverride};
      orders.set(order.id,order);return order;},
    async order(id){++calls.order;if(options.providerError)throw Error('DATABASE_PASSWORD_NEVER_RETURN');return orders.get(id);},
    async payment(id){++calls.payment;return payments.get(id);},
  };
  const handler=createHandler({config:options.config||config,repository,provider,
    verifyIdentity:async header=>{if(!/^Bearer (alice|bob|sql-user)$/.test(header||''))throw new Problem(401,'sign_in_required');
      return {uid:header.slice(7)==='sql-user'?"u' OR 1=1--":header.slice(7)};},
    assets:{async ready(){if(options.storageError)throw Error('PRIVATE_STORAGE_DETAIL');return !options.missingAssets;},
      async get(){++calls.asset;return options.badAsset?new Uint8Array([1]).buffer:new Uint8Array(bytes).buffer;}},
    log:code=>logs.push(code)});
  async function request(path,{user='alice',method='GET',body,headers={}}={}){
    const response=await handler(new Request('https://www.diplomaone.in'+PREFIX+path,{method,
      headers:{...(user?{Authorization:'Bearer '+user}:{}),...(method==='POST'?{Origin:'https://www.diplomaone.in','Content-Type':'application/json'}:{}),...headers},
      ...(body!==undefined?{body:typeof body==='string'?body:JSON.stringify(body)}:{})}));
    return {status:response.status,headers:response.headers,body:response.headers.get('content-type')?.includes('application/json')?await response.json():await response.text()};
  }
  async function order(user='alice',productId=id,requestId=randomUUID()){
    const result=await request('/orders',{method:'POST',user,body:{productId,requestId}});
    assert([200,201].includes(result.status),JSON.stringify(result));return result.body;
  }
  function capture(orderId,paymentId='pay_123456789012',changes={}){
    const o=orders.get(orderId);Object.assign(o,{status:'paid',amount_paid:o.amount,amount_due:0});
    const payment={id:paymentId,order_id:orderId,amount:o.amount,currency:'INR',status:'captured',captured:true,amount_refunded:0,...changes};
    payments.set(payment.id,payment);return payment;
  }
  async function verify(o,paymentId='pay_123456789012',user='alice',signature=hmac(config.keySecret,o.orderId+'|'+paymentId)){
    return request('/verify',{method:'POST',user,body:{orderId:o.orderId,paymentId,signature}});
  }
  async function webhook(body,eventId=randomUUID(),signature){
    const raw=typeof body==='string'?body:JSON.stringify(body);
    return request('/webhook',{method:'POST',user:null,body:raw,headers:{'x-razorpay-event-id':eventId,
      'x-razorpay-signature':signature||hmac(config.webhookSecret,raw),Origin:'https://razorpay.com'}});
  }
  return {request,order,capture,verify,webhook,calls,orders,payments,logs};
}

test('default config endpoint is disabled and does not touch payment/storage adapters',async()=>{
  const f=fixture({config:readConfig({})}),result=await f.request('/config',{user:null});
  assert.equal(result.status,200);assert.equal(result.body.enabled,false);assert.equal(result.body.mode,'test');
  assert.equal(result.body.keyId,undefined);assert.equal(result.body.products,undefined);
  assert.equal((await f.request('/orders',{method:'POST',body:{}})).status,503);
  assert.deepEqual(f.calls,{create:0,order:0,payment:0,asset:0});
});

test('config exposes only reviewed public metadata, fixed price and public test key',async()=>{
  const f=fixture(),result=await f.request('/config',{user:null});
  assert.equal(result.body.enabled,true);assert.equal(result.body.products[0].amount,2900);
  assert.equal(result.body.keyId,env.RAZORPAY_KEY_ID);
  assert.equal(result.body.products[0].assets,undefined);
  assert(!JSON.stringify(result.body).includes(env.RAZORPAY_KEY_SECRET));
  await database.exec('UPDATE diplomaone_test.products SET active=false');
  assert.equal((await f.request('/config',{user:null})).body.reason,'no_private_papers');
});

test('authentication, same-origin, methods, strict JSON, request size and body fields are enforced',async()=>{
  const f=fixture();
  assert.equal((await f.request('/purchases',{user:null})).status,401);
  assert.equal((await f.request('/purchases',{headers:{Origin:'https://evil.invalid'}})).status,403);
  assert.equal((await f.request('/orders',{method:'POST',body:{},headers:{Origin:''}})).status,403);
  assert.equal((await f.request('/orders',{method:'POST',body:'x',headers:{'Content-Type':'text/plain'}})).status,415);
  assert.equal((await f.request('/orders',{method:'POST',body:'x'})).status,400);
  assert.equal((await f.request('/orders',{method:'POST',body:'x'.repeat(5000)})).status,413);
  assert.equal((await f.request('/orders',{method:'POST',body:{productId:id,requestId:randomUUID(),amount:1,uid:'bob'}})).status,400);
  assert.equal((await f.request('/orders',{method:'POST',body:{productId:'../../private',requestId:randomUUID()}})).status,400);
  assert.equal((await f.request('/orders',{method:'DELETE'})).status,405);
  assert.equal((await f.request('/purchases?token=secret')).status,404);
  assert.equal((await f.request('/content/a%2fb/'+assetId)).status,404);
  assert.equal(f.calls.create,0);
});

test('only explicitly invited Firebase test UIDs may order or read private test purchases',async()=>{
  const f=fixture({config:{...config,testers:['alice']}});
  assert.equal((await f.request('/orders',{method:'POST',user:'bob',body:{productId:id,requestId:randomUUID()}})).body.error,'tester_not_allowed');
  assert.equal((await f.request('/purchases',{user:'bob'})).status,403);
  assert.equal((await f.request('/content/'+id+'/'+assetId,{user:'bob'})).status,403);
  assert.equal(f.calls.create,0);assert.equal((await f.request('/config',{user:null})).body.testers,undefined);
});

test('server creates exactly one INR order per active paper and retries reuse it',async()=>{
  const f=fixture(),requestId=randomUUID(),first=await f.request('/orders',{method:'POST',body:{productId:id,requestId}});
  assert.equal(first.status,201);assert.equal(first.body.amount,2900);assert.equal(first.body.currency,'INR');assert.equal(first.body.mode,'test');
  const same=await f.request('/orders',{method:'POST',body:{productId:id,requestId}});
  const anotherRequest=await f.order();
  assert.equal(same.status,200);assert.equal(same.body.orderId,first.body.orderId);assert.equal(anotherRequest.orderId,first.body.orderId);
  assert.equal(f.calls.create,1);assert.equal((await repository.order(first.body.orderId)).uid,'alice');
  assert.equal((await repository.order(first.body.orderId)).receipt.length,35);
  const bob=await f.order('bob');assert.notEqual(bob.orderId,first.body.orderId);
  assert.equal((await repository.order(bob.orderId)).uid,'bob');
});

test('idempotency key cannot be re-used for another paper and concurrent reserve stays single',async()=>{
  await repository.importProduct({...product,id:other,title:'Fluid Mechanics'});
  const f=fixture(),requestId=randomUUID();await f.order('alice',id,requestId);
  assert.equal((await f.request('/orders',{method:'POST',body:{productId:other,requestId}})).body.error,'idempotency_conflict');
  const results=await Promise.all([1,2].map(()=>f.request('/orders',{method:'POST',user:'bob',body:{productId:id,requestId:randomUUID()}})));
  assert(results.some(r=>r.status===201));
  assert(results.every(r=>[200,201].includes(r.status)||(r.status===409&&r.body.error==='order_being_created')));
  const retried=await f.order('bob');
  assert.equal(retried.orderId,results.find(r=>r.status===201).body.orderId);assert.equal(f.calls.create,2);
});

test('missing or unavailable private assets block provider order creation and keep ownership off',async()=>{
  for(const options of [{missingAssets:true},{storageError:true}]){
    await database.exec('TRUNCATE diplomaone_test.orders CASCADE');
    const f=fixture(options),result=await f.request('/orders',{method:'POST',body:{productId:id,requestId:randomUUID()}});
    assert.equal(result.status,503);assert.equal(result.body.error,'private_paper_not_ready');
    assert.equal(f.calls.create,0);assert.equal(await repository.owns('alice',id),false);
    assert(!JSON.stringify(result).includes('PRIVATE_STORAGE_DETAIL'));
    assert.equal((await database.query('SELECT status FROM diplomaone_test.orders')).rows[0].status,'failed');
  }
});

test('uncertain provider errors do not create duplicate retries or grant access',async()=>{
  const f=fixture({createError:new Error('SECRET_IN_PROVIDER_ERROR')}),body={productId:id,requestId:randomUUID()};
  assert.equal((await f.request('/orders',{method:'POST',body})).status,503);
  const second=await f.request('/orders',{method:'POST',body:{...body,requestId:randomUUID()}});
  assert.equal(second.body.error,'order_pending_operator_review');assert.equal(f.calls.create,1);
  assert.equal(await repository.owns('alice',id),false);
  assert(!JSON.stringify(second).includes('SECRET_IN_PROVIDER_ERROR'));assert(!f.logs.includes('SECRET_IN_PROVIDER_ERROR'));
});

test('mismatched provider-created amount, currency or receipt is never returned to checkout',async()=>{
  for(const override of [{amount:1},{currency:'USD'},{receipt:'other_receipt'},{partial_payment:true},{status:'paid'}]){
    await database.exec('TRUNCATE diplomaone_test.orders CASCADE');
    const f=fixture({createOverride:override}),result=await f.request('/orders',{method:'POST',body:{productId:id,requestId:randomUUID()}});
    assert.equal(result.status,503);assert.equal(result.body.error,'provider_order_mismatch');
  }
});

test('an unverified, authorized-only or client-success payment cannot unlock a paper',async()=>{
  const f=fixture(),o=await f.order();
  assert.equal((await f.verify(o,undefined,'alice','0'.repeat(64))).status,401);
  assert.equal(f.calls.order,0,'bad signatures must not cause provider API reads');
  f.capture(o.orderId,undefined,{status:'authorized',captured:false});
  assert.equal((await f.verify(o)).status,409);assert.equal(await repository.owns('alice',id),false);
  assert.equal((await f.request('/content/'+id+'/'+assetId)).status,403);assert.equal(f.calls.asset,0);
});

test('signed callback is bound to the stored order UID and canonical captured order/payment',async()=>{
  const f=fixture(),o=await f.order();f.capture(o.orderId);
  assert.equal((await f.verify(o,undefined,'bob')).status,404);assert.equal(f.calls.payment,0);
  const success=await f.verify(o);assert.equal(success.status,200);assert.equal(success.body.owned,true);
  assert.equal(success.body.mode,'test');assert.equal(await repository.owns('alice',id),true);assert.equal(await repository.owns('bob',id),false);
  assert.equal((await f.verify(o)).status,200,'callback replay is idempotent');
  assert.equal((await f.request('/orders',{method:'POST',body:{productId:id,requestId:randomUUID()}})).body.error,'already_owned');
});

test('every canonical capture/money/receipt mismatch fails closed',async()=>{
  const f=fixture(),o=await f.order(),payment=f.capture(o.orderId),order=f.orders.get(o.orderId);
  for(const [object,patch] of [[payment,{id:'pay_different'}],[payment,{order_id:'order_different'}],
    [payment,{amount:19}],[payment,{currency:'USD'}],[payment,{amount_refunded:1}],[payment,{captured:false}],
    [order,{status:'attempted'}],[order,{amount_paid:1}],[order,{amount_due:1}],[order,{receipt:'someone_else'}],
    [order,{amount:1}],[order,{currency:'USD'}],[order,{partial_payment:true}]]){
    const original={...object};Object.assign(object,patch);
    assert.equal((await f.verify(o)).status,409,JSON.stringify(patch));assert.equal(await repository.owns('alice',id),false);
    Object.assign(object,original);
  }
});

test('raw-body signed captured webhook grants ownership without a browser callback and deduplicates replay',async()=>{
  const f=fixture(),o=await f.order(),payment=f.capture(o.orderId),eventId='evt_captured_1';
  const body={event:'payment.captured',payload:{payment:{entity:payment}}};
  assert.equal((await f.webhook(body,eventId,'0'.repeat(64))).status,401);
  assert.equal(await repository.owns('alice',id),false);
  const raw=JSON.stringify(body),signature=hmac(config.webhookSecret,raw);
  assert.equal((await f.webhook(raw+' ',eventId,signature)).status,401,'must not parse/re-serialize before signature verification');
  assert.equal((await f.webhook(raw,eventId,signature)).status,200);assert.equal(await repository.owns('alice',id),true);
  const count=f.calls.payment;assert.equal((await f.webhook(raw,eventId,signature)).body.duplicate,true);assert.equal(f.calls.payment,count);
  assert.equal((await f.webhook({...body,extra:true},eventId)).status,409);
});

test('signed malformed webhooks and oversized raw bodies cannot mutate purchases',async()=>{
  const f=fixture();
  for(const value of ['null','[]','{"event":5}','{"event":'])assert.equal((await f.webhook(value)).status,400);
  assert.equal((await f.webhook('x'.repeat(128*1024+1))).status,413);
  assert.equal(await repository.owns('alice',id),false);
});

test('webhook notes cannot create purchases for an unrelated or missing local order',async()=>{
  const f=fixture(),body={event:'payment.captured',payload:{payment:{entity:{id:'pay_unrelated',order_id:'order_unrelated',notes:{uid:'alice',productId:id}}}}};
  assert.equal((await f.webhook(body)).body.ignored,true);assert.equal(await repository.owns('alice',id),false);
  assert.equal(f.calls.payment,0);
  assert.equal((await f.webhook({event:'payment.failed'})).body.ignored,true);
});

test('disabling new checkout still allows already-created verified payments to be fulfilled',async()=>{
  const f=fixture({config:{...config,enabled:false}});
  // Reserve/attach as if the order was legitimately created before the operator disabled checkout.
  const reserve=await repository.reserve('alice',{...product,amount:2900},randomUUID());
  f.orders.set('order_beforeDisable',{id:'order_beforeDisable',receipt:reserve.order.receipt,amount:2900,currency:'INR',partial_payment:false});
  await repository.attachOrder(reserve.order.id,'order_beforeDisable');f.capture('order_beforeDisable');
  assert.equal((await f.request('/orders',{method:'POST',body:{productId:id,requestId:randomUUID()}})).status,503);
  assert.equal((await f.verify({orderId:'order_beforeDisable'})).status,200);
});

test('purchases are UID-scoped, parameterized and not invented when the database fails',async()=>{
  const f=fixture(),o=await f.order('sql-user');f.capture(o.orderId);await f.verify(o,undefined,'sql-user');
  assert.equal((await f.request('/purchases',{user:'sql-user'})).body.purchases.length,1);
  assert.equal((await f.request('/purchases',{user:'alice'})).body.purchases.length,0);
  const row=(await f.request('/purchases',{user:'sql-user'})).body.purchases[0];
  assert.equal(row.productId,id);assert.equal(row.active,true);assert.equal(row.uid,undefined);
  const handler=createHandler({config,repository:{async purchases(){throw Error('PRIVATE_DB_PASSWORD');}},verifyIdentity:async()=>({uid:'alice'})});
  const response=await handler(new Request('https://www.diplomaone.in'+PREFIX+'/purchases'));
  assert.equal(response.status,503);const error=await response.json();assert.equal(error.purchases,undefined);assert(!JSON.stringify(error).includes('PRIVATE_DB_PASSWORD'));
});

test('owned content is checked on every request, hash-verified, non-cacheable and not executable HTML',async()=>{
  const f=fixture(),o=await f.order();f.capture(o.orderId);await f.verify(o);
  const manifest=await f.request('/content/'+id);assert.equal(manifest.body.readerAsset,assetId);
  const result=await f.request('/content/'+id+'/'+assetId);assert.equal(result.status,200);assert.equal(result.body,bytes.toString());
  assert.equal(result.headers.get('cache-control'),'private, no-store');assert.equal(result.headers.get('x-content-type-options'),'nosniff');
  assert.equal(result.headers.get('content-type'),'text/plain; charset=utf-8');assert(result.headers.get('content-security-policy').includes('sandbox'));
  assert.equal((await f.request('/content/'+id+'/'+assetId,{user:'bob'})).status,403);
  assert.equal((await f.request('/content/'+id+'/'+'b'.repeat(64))).status,404);
  const bad=fixture({badAsset:true});assert.equal((await bad.request('/content/'+id+'/'+assetId)).status,503);
});

test('a confirmed refund revokes access, including refund-before-capture delivery ordering',async()=>{
  for(const before of [false,true]){
    await database.exec('TRUNCATE diplomaone_test.events,diplomaone_test.entitlements,diplomaone_test.orders CASCADE');
    const f=fixture(),o=await f.order(),payment=f.capture(o.orderId);
    if(!before)await f.verify(o);
    payment.amount_refunded=payment.amount;payment.status='refunded';
    const refund={event:'refund.processed',payload:{refund:{entity:{payment_id:payment.id}}}};
    assert.equal((await f.webhook(refund)).status,200);assert.equal(await repository.owns('alice',id),false);
    // Even a stale canonical capture snapshot arriving later cannot re-grant a revoked row.
    payment.amount_refunded=0;payment.status='captured';
    assert.equal((await f.verify(o)).body.error,'payment_revoked');
    assert.equal((await f.request('/content/'+id+'/'+assetId)).status,403);
  }
});

test('SQL constraints keep live/free products and reused payment IDs out of test entitlements',async()=>{
  await assert.rejects(repository.importProduct({...product,id:'DI01000021--summer-2026'}),/common_subject_is_free/);
  await assert.rejects(database.query(`INSERT INTO diplomaone_test.products(id,title,branch,assets,reader_asset)
    VALUES('DI01000121--summer-2026','Free Physics','chemical',$1::jsonb,$2)`,[JSON.stringify(product.assets),assetId]));
  const f=fixture(),alice=await f.order();f.capture(alice.orderId);await f.verify(alice);
  const bob=await f.order('bob');
  await assert.rejects(repository.grant(bob.orderId,'pay_123456789012'));
  assert.equal(await repository.owns('bob',id),false,'a failed unique payment constraint rolls back entitlement writes');
});

test('an event hash conflict atomically rolls back order/payment/ownership changes',async()=>{
  const f=fixture(),o=await f.order();f.capture(o.orderId);
  await database.query('INSERT INTO diplomaone_test.events(id,body_hash) VALUES($1,$2)',['evt_same','a'.repeat(64)]);
  await assert.rejects(repository.grant(o.orderId,'pay_123456789012',{id:'evt_same',hash:'b'.repeat(64)}),/event_id_conflict/);
  assert.equal(await repository.owns('alice',id),false);
  const stored=await repository.order(o.orderId);assert.equal(stored.status,'created');assert.equal(stored.payment_id,null);
});

test('free-tier pilot has durable per-user and global new-order budgets',async()=>{
  const p=await repository.product(id);
  for(let n=0;n<5;n++){
    const reserved=await repository.reserve('alice',p,randomUUID());
    await database.query("UPDATE diplomaone_test.orders SET status='failed' WHERE id=$1",[reserved.order.id]);
  }
  await assert.rejects(repository.reserve('alice',p,randomUUID()),/test_order_limit/);
  for(let n=0;n<45;n++){
    const reserved=await repository.reserve('other-user-'+n,p,randomUUID());
    await database.query("UPDATE diplomaone_test.orders SET status='failed' WHERE id=$1",[reserved.order.id]);
  }
  await assert.rejects(repository.reserve('another-user',p,randomUUID()),/test_order_limit/);
});
