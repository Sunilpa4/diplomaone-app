import {test,beforeEach,after} from 'node:test';
import assert from 'node:assert/strict';
import {randomUUID} from 'node:crypto';
import {store,usingEmulator,DEMO_PROJECT} from './store.mjs';
import {Repository} from '../src/repository.mjs';
import {FIRESTORE_ROOT} from '../src/firestore-config.mjs';
import {digest} from '../src/domain.mjs';
const {database,repository,reset}=store();
const id='DI03000161--summer-2026',asset=digest('unit-test-only');
const product={id,title:'Unit test fixture, not a published paper',branch:'mechanical',reader_asset:asset,
  assets:[{id:asset,path:'reader.html',mime:'text/plain; charset=utf-8',bytes:14}]};
beforeEach(async()=>{await reset();await repository.importProduct(product);});
after(()=>database.terminate());
async function created(uid='alice',key=randomUUID(),providerId='order_'+randomUUID().replaceAll('-','')){
  const result=await repository.reserve(uid,product,key);
  return repository.attachOrder(result.order.id,providerId);
}

test('Firestore namespace and UID hashes cannot escape into another project or document tree',async()=>{
  assert.equal(repository.root.path,FIRESTORE_ROOT);
  const uid='../../other_user/purchases/private',ref=repository.ownerRef(uid,id);
  assert(ref.path.startsWith(FIRESTORE_ROOT+'/users/'));assert(!ref.path.includes(uid));
  await assert.rejects(repository.product('../orders/foreign'));
  assert.throws(()=>repository.ownerRef('alice','../../paid-content'));
  const p=await repository.product(id);assert.equal(p.amount,2900);
});

test('reservation re-reads canonical branch/price and normalizes UUID case inside the transaction',async()=>{
  const requestId=randomUUID(),first=await repository.reserve('alice',{...product,branch:'computer',amount:1},requestId);
  assert.equal(first.order.amount,2900);assert.equal(first.order.branch,'mechanical');
  const second=await repository.reserve('alice',product,requestId.toUpperCase());assert.equal(second.created,false);assert.equal(second.order.id,first.order.id);
  await repository.unavailable(first.order.id);
  await repository.collection('products').doc(id).update({active:false});
  await assert.rejects(repository.reserve('alice',product,randomUUID()),/paper_unavailable/);
});

test('atomic provider-order index rejects accidental reuse without changing either order',async()=>{
  const a=await created('alice',randomUUID(),'order_uniqueProvider');
  const b=await repository.reserve('bob',product,randomUUID());
  await assert.rejects(repository.attachOrder(b.order.id,a.razorpay_order_id),/provider_order_conflict/);
  assert.equal((await repository.collection('orders').doc(b.order.id).get()).data().status,'reserving');
  assert.equal((await repository.order(a.razorpay_order_id)).uid,'alice');
});

test('concurrent callbacks grant one stable record and one payment mapping',async()=>{
  const order=await created(),payment='pay_concurrentCapture';
  const results=await Promise.all([repository.grant(order.razorpay_order_id,payment),repository.grant(order.razorpay_order_id,payment)]);
  assert(results.every(r=>r.owned===true));
  const rows=await repository.purchases('alice');assert.equal(rows.length,1);
  const timestamp=rows[0].purchasedAt;
  await repository.grant(order.razorpay_order_id,payment);
  assert.equal((await repository.purchases('alice'))[0].purchasedAt,timestamp);
});

test('a refunded old order cannot revoke or re-grant a later independent repurchase',async()=>{
  const first=await created();await repository.grant(first.razorpay_order_id,'pay_oldPurchase');
  await repository.revoke(first.razorpay_order_id,'pay_oldPurchase',{id:'evt_oldRefund',hash:digest('old-refund')});
  const second=await created();await repository.grant(second.razorpay_order_id,'pay_newPurchase');
  await repository.revoke(first.razorpay_order_id,'pay_oldPurchase',{id:'evt_oldRefundAgain',hash:digest('old-refund-again')});
  assert.equal(await repository.owns('alice',id),true);
  await assert.rejects(repository.grant(first.razorpay_order_id,'pay_oldPurchase'),/payment_revoked/);
  assert.equal((await repository.ownerRef('alice',id).get()).data().order_id,second.id);
});

test('shared rolling budgets remain bounded and expire by trusted server time without TTL/scans',async()=>{
  let now=Date.UTC(2026,9,30);const timed=new Repository(database,{clock:()=>now});
  for(let n=0;n<5;n++){const r=await timed.reserve('alice',product,randomUUID());await timed.unavailable(r.order.id);}
  await assert.rejects(timed.reserve('alice',product,randomUUID()),/test_order_limit/);
  now+=3600001;
  const r=await timed.reserve('alice',product,randomUUID());await timed.unavailable(r.order.id);
  const buckets=await timed.collection('limits').get();
  assert(buckets.docs.every(d=>d.data().times.length<=50));
  now+=86400001;await timed.reserve('bob',product,randomUUID());
  assert.equal((await timed.collection('limits').doc('all').get()).data().times.length,1);
});

test('parallel new users cannot overrun the last available global order slot',async()=>{
  await repository.collection('limits').doc('all').set({times:Array(49).fill(Date.now())});
  const results=await Promise.allSettled(['alice','bob'].map(uid=>repository.reserve(uid,product,randomUUID())));
  assert.equal(results.filter(r=>r.status==='fulfilled').length,1);
  assert.match(results.find(r=>r.status==='rejected').reason.message,/test_order_limit/);
  assert.equal((await repository.collection('limits').doc('all').get()).data().times.length,50);
  assert.equal((await repository.collection('orders').get()).docs.length,1);
});

test('concurrent capture/refund always finishes revoked, never re-granted',async()=>{
  const order=await created();
  const [grant,refund]=await Promise.allSettled([
    repository.grant(order.razorpay_order_id,'pay_racingRefund'),
    repository.revoke(order.razorpay_order_id,'pay_racingRefund',{id:'evt_racingRefund',hash:digest('racing-refund')}),
  ]);
  assert.equal(refund.status,'fulfilled');
  if(grant.status==='rejected')assert.match(grant.reason.message,/payment_revoked/);
  assert.equal((await repository.order(order.razorpay_order_id)).status,'revoked');
  assert.equal(await repository.owns('alice',id),false);
});

test('Firestore import strips extra fields and refuses unbounded or unsafe metadata',async()=>{
  const other='DI03000171--winter-2025';
  await repository.importProduct({...product,id:other,secret:'DO_NOT_STORE',assets:[{...product.assets[0],content:'DO_NOT_STORE'}]});
  assert(!JSON.stringify((await repository.collection('products').doc(other).get()).data()).includes('DO_NOT_STORE'));
  for(const patch of [{assets:[]},{assets:Array(301).fill(product.assets[0])},{reader_asset:'missing'},
    {assets:[{...product.assets[0],path:'../reader.html'}]},{assets:[{...product.assets[0],bytes:0}]}])
    await assert.rejects(repository.importProduct({...product,id:'DI03000201--summer-2026',...patch}));
});

test('existing imported source metadata cannot be silently replaced',async()=>{
  await assert.rejects(repository.importProduct({...product,title:'Replacement not reviewed'}),/product_already_imported_review_required/);
  assert.equal((await repository.product(id)).title,product.title);
});

test('actual emulator denies anonymous and signed-in browser writes/reads to purchase records',{skip:!usingEmulator},async()=>{
  const base='http://'+process.env.FIRESTORE_EMULATOR_HOST+'/v1/projects/'+DEMO_PROJECT+'/databases/(default)/documents/';
  const url=base+repository.ownerRef('alice',id).path;
  const now=Math.floor(Date.now()/1000),encode=value=>Buffer.from(JSON.stringify(value)).toString('base64url');
  const token=encode({alg:'none',typ:'JWT'})+'.'+encode({iss:'https://securetoken.google.com/'+DEMO_PROJECT,aud:DEMO_PROJECT,
    sub:'alice',user_id:'alice',iat:now,exp:now+3600,auth_time:now,firebase:{sign_in_provider:'google.com'}})+'.';
  for(const headers of [{},{Authorization:'Bearer '+token}]){
    const read=await fetch(url,{headers});assert.equal(read.status,403);
    const write=await fetch(url,{method:'PATCH',headers:{...headers,'Content-Type':'application/json'},body:JSON.stringify({fields:{active:{booleanValue:true}}})});
    assert.equal(write.status,403);
  }
});
