import {randomUUID} from 'node:crypto';
import {reject,validateProduct,digest,productPattern,providerOrderPattern,providerPaymentPattern,uuidPattern,assetPattern,MIME,MAX_ASSET_BYTES} from './domain.mjs';
import {FIRESTORE_ROOT} from './firestore-config.mjs';

const hash=(...values)=>digest(JSON.stringify(values));
const data=snapshot=>snapshot.exists?snapshot.data():null;
const activeStates=['reserving','created','unknown'];
function identity(uid){reject(typeof uid!=='string'||!uid||uid.length>128,400,'invalid_user');}
function productId(id){reject(typeof id!=='string'||!productPattern.test(id)||id.includes('/')||id.trim()!==id,400,'invalid_product');}
function eventCheck(stored,event){reject(stored&&stored.body_hash!==event.hash,409,'event_id_conflict');}

// All durable state lives under one TEST namespace. No SQL service, in-memory
// production fallback, background scan, collection-group query or live records.
// Every transaction reads before writing; retries do not call Razorpay/storage.
export class Repository {
  constructor(firestore,{clock=()=>Date.now()}={}){this.db=firestore;this.root=firestore.doc(FIRESTORE_ROOT);this.clock=clock;}
  collection(name){return this.root.collection(name);}
  ownerRef(uid,id){identity(uid);productId(id);return this.collection('users').doc(hash(uid)).collection('purchases').doc(id);}
  activeRef(uid,id){return this.collection('activeOrders').doc(hash(uid,id));}
  eventRef(id){return this.collection('events').doc(hash(id));}
  transaction(fn){return this.db.runTransaction(fn,{maxAttempts:5});}
  async products(){
    const result=await this.collection('products').where('active','==',true).limit(101).get();
    reject(result.docs.length>100,503,'pilot_catalog_limit');
    return result.docs.map(doc=>validateProduct({...doc.data(),id:doc.id})).sort((a,b)=>a.id.localeCompare(b.id));
  }
  async product(id){
    productId(id);const stored=data(await this.collection('products').doc(id).get());
    return stored?.active===true?validateProduct({...stored,id}):null;
  }
  async importProduct(product){
    const p=validateProduct(product),ref=this.collection('products').doc(p.id),paths=new Set();
    reject(!Array.isArray(p.assets)||!p.assets.length||p.assets.length>300,400,'invalid_assets');
    const assets=p.assets.map(a=>{
      reject(!a||!assetPattern.test(a.id||'')||typeof a.path!=='string'||!a.path||a.path.length>220||
        /[\\\x00-\x1f?#%]/.test(a.path)||a.path.split('/').some(part=>!part||part==='.'||part==='..')||paths.has(a.path)||
        !Object.values(MIME).includes(a.mime)||!Number.isInteger(a.bytes)||a.bytes<1||a.bytes>MAX_ASSET_BYTES,400,'invalid_assets');
      paths.add(a.path);return {id:a.id,path:a.path,mime:a.mime,bytes:a.bytes};
    });
    reject(!assets.some(a=>a.id===p.reader_asset&&a.mime===MIME['.html']&&a.path.endsWith('.html')),400,'reader_required');
    // The importer has already strong-read verified all private blobs. Store
    // only bounded allowlisted metadata, never manifest fields/answer bytes.
    return this.transaction(async tx=>{
      reject((await tx.get(ref)).exists,409,'product_already_imported_review_required');
      tx.create(ref,{id:p.id,title:p.title,branch:p.branch,assets,reader_asset:p.reader_asset,active:true,created_at:this.clock()});
    });
  }
  async reserve(uid,product,requestId){
    identity(uid);productId(product.id);reject(!uuidPattern.test(requestId||''),400,'invalid_order_request');
    requestId=requestId.toLowerCase();
    const requestRef=this.collection('requests').doc(hash(uid,requestId)),activeRef=this.activeRef(uid,product.id);
    const ownerRef=this.ownerRef(uid,product.id),globalRef=this.collection('limits').doc('all'),userRef=this.collection('limits').doc(hash(uid));
    const id=randomUUID(),orderRef=this.collection('orders').doc(id);
    return this.transaction(async tx=>{
      const request=data(await tx.get(requestRef));
      if(request){
        reject(request.uid!==uid||request.product_id!==product.id,409,'idempotency_conflict');
        const order=data(await tx.get(this.collection('orders').doc(request.order_id)));
        reject(!order||order.uid!==uid||order.product_id!==product.id,409,'order_state_conflict');
        return {created:false,order};
      }
      const owner=data(await tx.get(ownerRef));reject(owner?.active===true,409,'already_owned');
      const active=data(await tx.get(activeRef));
      if(active){
        const order=data(await tx.get(this.collection('orders').doc(active.order_id)));
        reject(!order||order.uid!==uid||order.product_id!==product.id||!activeStates.includes(order.status),409,'order_state_conflict');
        return {created:false,order};
      }
      const stored=data(await tx.get(this.collection('products').doc(product.id)));
      reject(stored?.active!==true,404,'paper_unavailable');
      const canonical=validateProduct({...stored,id:product.id});
      const global=data(await tx.get(globalRef)),user=data(await tx.get(userRef)),now=this.clock();
      // Bounded rolling timestamp arrays: no paid count query or growing scan.
      const recent=(global?.times||[]).filter(t=>t>now-86400000),mine=(user?.times||[]).filter(t=>t>now-3600000);
      reject(recent.length>=50||mine.length>=5,429,'test_order_limit');
      const order={id,uid,product_id:canonical.id,request_id:requestId,receipt:'dt_'+id.replaceAll('-',''),
        amount:canonical.amount,currency:'INR',title:canonical.title,branch:canonical.branch,
        status:'reserving',razorpay_order_id:null,payment_id:null,created_at:now,paid_at:null};
      tx.create(orderRef,order);
      tx.create(requestRef,{uid,product_id:canonical.id,order_id:id});
      tx.create(activeRef,{uid,product_id:canonical.id,order_id:id});
      tx.set(globalRef,{times:[...recent,now]});tx.set(userRef,{times:[...mine,now]});
      return {created:true,order};
    });
  }
  async attachOrder(id,providerId){
    reject(!providerOrderPattern.test(providerId||''),400,'invalid_order');
    const ref=this.collection('orders').doc(id),index=this.collection('orderIds').doc(providerId);
    return this.transaction(async tx=>{
      const stored=data(await tx.get(ref)),mapped=data(await tx.get(index));
      reject(!stored||stored.status!=='reserving',409,'order_state_conflict');
      reject(mapped,409,'provider_order_conflict');
      const order={...stored,status:'created',razorpay_order_id:providerId};
      tx.create(index,{order_id:id});tx.set(ref,order);return order;
    });
  }
  async pending(id,status){
    const ref=this.collection('orders').doc(id);
    return this.transaction(async tx=>{
      const stored=data(await tx.get(ref));if(stored?.status!=='reserving')return;
      const active=this.activeRef(stored.uid,stored.product_id),pointer=data(await tx.get(active));
      tx.update(ref,{status});
      if(status==='failed'&&pointer?.order_id===id)tx.delete(active);
    });
  }
  unavailable(id){return this.pending(id,'failed');}
  uncertain(id){return this.pending(id,'unknown');}
  async order(id){
    reject(!providerOrderPattern.test(id||''),400,'invalid_order');
    const mapped=data(await this.collection('orderIds').doc(id).get());
    if(!mapped)return null;
    const order=data(await this.collection('orders').doc(mapped.order_id).get());
    reject(!order||order.razorpay_order_id!==id,409,'order_state_conflict');return order;
  }
  async event(id,hash){
    if(!id)return false;const stored=data(await this.eventRef(id).get());eventCheck(stored,{hash});return !!stored;
  }
  async settle(orderId,paymentId,event,revoke){
    reject(!providerOrderPattern.test(orderId||'')||!providerPaymentPattern.test(paymentId||''),400,'invalid_payment');
    const index=this.collection('orderIds').doc(orderId),paymentRef=this.collection('payments').doc(paymentId);
    return this.transaction(async tx=>{
      const mapped=data(await tx.get(index));reject(!mapped,404,'order_not_found');
      const orderRef=this.collection('orders').doc(mapped.order_id),stored=data(await tx.get(orderRef));
      reject(!stored||stored.razorpay_order_id!==orderId,409,'order_state_conflict');
      const ownerRef=this.ownerRef(stored.uid,stored.product_id),activeRef=this.activeRef(stored.uid,stored.product_id);
      const payment=data(await tx.get(paymentRef)),owner=data(await tx.get(ownerRef)),active=data(await tx.get(activeRef));
      const eventRef=event?this.eventRef(event.id):null,eventData=event?data(await tx.get(eventRef)):null;
      if(event)eventCheck(eventData,event);
      reject(payment&&payment.order_id!==stored.id,409,'payment_conflict');
      reject(stored.payment_id&&stored.payment_id!==paymentId,409,'payment_conflict');
      if(!revoke){
        reject(stored.status==='revoked',409,'payment_revoked');
        reject(!['created','paid'].includes(stored.status),409,'order_state_conflict');
        reject(owner?.active===true&&owner.order_id!==stored.id,409,'entitlement_conflict');
      }
      const now=this.clock();
      tx.update(orderRef,{status:revoke?'revoked':'paid',payment_id:paymentId,paid_at:revoke?stored.paid_at:(stored.paid_at??now)});
      if(!payment)tx.create(paymentRef,{order_id:stored.id});
      if(revoke){
        // An old refunded order must not revoke a newer repurchase. Recording a
        // refund even before the first capture also blocks late re-grants.
        if(owner?.order_id===stored.id)tx.update(ownerRef,{active:false});
      }else tx.set(ownerRef,{uid:stored.uid,product_id:stored.product_id,order_id:stored.id,active:true,
        title:stored.title,branch:stored.branch,amount:stored.amount,currency:'INR',
        created_at:owner?.active===true?owner.created_at:now});
      if(active?.order_id===stored.id)tx.delete(activeRef);
      if(event&&!eventData)tx.create(eventRef,{body_hash:event.hash,created_at:now});
      return {productId:stored.product_id,owned:!revoke,mode:'test'};
    });
  }
  grant(orderId,paymentId,event=null){return this.settle(orderId,paymentId,event,false);}
  revoke(orderId,paymentId,event){return this.settle(orderId,paymentId,event,true);}
  async purchases(uid){
    identity(uid);
    const result=await this.collection('users').doc(hash(uid)).collection('purchases').orderBy('created_at','desc').limit(100).get();
    return result.docs.map(doc=>{
      const p=doc.data();reject(p.uid!==uid||p.product_id!==doc.id,409,'entitlement_conflict');
      return {productId:p.product_id,title:p.title,branch:p.branch,active:p.active,amount:p.amount,
        currency:p.currency,purchasedAt:new Date(p.created_at).toISOString()};
    });
  }
  async owns(uid,id){const stored=data(await this.ownerRef(uid,id).get());return stored?.uid===uid&&stored?.product_id===id&&stored?.active===true;}
}
