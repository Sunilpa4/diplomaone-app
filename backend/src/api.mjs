import {Problem,PRICES,MAX_ASSET_BYTES,TEST_SITE_ORIGIN,LIVE_ORIGINS,productPattern,providerOrderPattern,providerPaymentPattern,
  assetPattern,uuidPattern,reject,validSignature,digest,confirmCaptured} from './domain.mjs';

const headers={'Cache-Control':'private, no-store','Vary':'Authorization, Origin',
  'X-Content-Type-Options':'nosniff','Referrer-Policy':'no-referrer','Content-Security-Policy':"default-src 'none'; sandbox"};
const json=(value,status=200,extra={})=>Response.json(value,{status,headers:{...headers,...extra}});
async function rawBody(request,limit){
  const declared=request.headers.get('content-length');
  reject(declared!==null&&(!/^\d+$/.test(declared)||Number(declared)>limit),413,'body_too_large');
  if(!request.body)return Buffer.alloc(0);
  const reader=request.body.getReader(),chunks=[];let total=0;
  while(true){const {value,done}=await reader.read();if(done)break;total+=value.length;
    if(total>limit){await reader.cancel();throw new Problem(413,'body_too_large');}chunks.push(Buffer.from(value));}
  return Buffer.concat(chunks);
}
async function parseBody(request,keys){
  reject(!/^application\/json(?:\s*;|$)/i.test(request.headers.get('content-type')||''),415,'json_required');
  let body;try{body=JSON.parse((await rawBody(request,4096)).toString('utf8'));}
  catch(error){if(error instanceof Problem)throw error;throw new Problem(400,'invalid_json');}
  reject(!body||typeof body!=='object'||Array.isArray(body)||Object.keys(body).some(key=>!keys.includes(key))||keys.some(key=>typeof body[key]!=='string'),400,'invalid_fields');
  return body;
}

export function createHandler({config,repository,provider,verifyIdentity,assets,connectionCheck,log=()=>{}}){
  const MODE=config.mode||'test',PREFIX='/api/payments/'+MODE;
  const requireSetup=()=>reject(!config.configured,503,'backend_not_configured');
  async function grant(stored,paymentId,event){
    reject(!stored,404,'order_not_found');
    reject(stored.status==='revoked',409,'payment_revoked');
    const [order,payment]=await Promise.all([provider.order(stored.razorpay_order_id),provider.payment(paymentId)]);
    reject(payment?.id!==paymentId,409,'payment_mismatch');
    confirmCaptured(order,payment,stored);
    return repository.grant(stored.razorpay_order_id,paymentId,event);
  }
  async function webhook(request){
    requireSetup();
    // Authenticate EXACT bytes before parsing. Never Firebase-authenticate the
    // provider's webhook, and never trust a browser-generated payment event.
    const raw=await rawBody(request,128*1024);
    reject(!validSignature(config.webhookSecret,raw,request.headers.get('x-razorpay-signature')),401,'invalid_webhook_signature');
    let body;try{body=JSON.parse(raw.toString('utf8'));}catch(_){throw new Problem(400,'invalid_json');}
    reject(!body||typeof body!=='object'||Array.isArray(body)||typeof body.event!=='string',400,'invalid_event');
    const eventId=request.headers.get('x-razorpay-event-id');
    reject(!eventId||!/^[A-Za-z0-9_-]{1,200}$/.test(eventId),400,'invalid_event_id');
    const event={id:eventId,hash:digest(raw)};
    if(await repository.event(event.id,event.hash))return json({mode:MODE,received:true,duplicate:true});
    if(body.event==='payment.captured'){
      const p=body.payload?.payment?.entity;
      reject(!providerOrderPattern.test(p?.order_id||'')||!providerPaymentPattern.test(p?.id||''),400,'invalid_payment_event');
      const stored=await repository.order(p.order_id);
      // This merchant may also have unrelated test integrations. They cannot
      // create ownership here merely by putting a UID/product in payment notes.
      if(!stored)return json({mode:MODE,received:true,ignored:true});
      await grant(stored,p.id,event);
    }else if(body.event==='refund.processed'){
      const id=body.payload?.refund?.entity?.payment_id;
      reject(!providerPaymentPattern.test(id||''),400,'invalid_refund_event');
      const payment=await provider.payment(id);
      reject(payment?.id!==id||!providerOrderPattern.test(payment.order_id||''),409,'refund_not_confirmed');
      const stored=await repository.order(payment.order_id);
      if(!stored)return json({mode:MODE,received:true,ignored:true});
      reject(payment.amount!==stored.amount||payment.currency!=='INR'||!Number.isInteger(payment.amount_refunded)||
        payment.amount_refunded<=0,409,'refund_not_confirmed');
      // Fail closed on a confirmed refund; this is access reconciliation, not
      // a refund-eligibility promise. No money-moving refund API is called.
      await repository.revoke(stored.razorpay_order_id,id,event);
    }else return json({mode:MODE,received:true,ignored:true});
    return json({mode:MODE,received:true});
  }
  return async request=>{
    try{
      const url=new URL(request.url),path=url.pathname.slice(PREFIX.length);
      reject(url.protocol!=='https:',400,'https_required');
      reject(!url.pathname.startsWith(PREFIX+'/')||/%2f|%5c/i.test(url.pathname)||url.search,404,'not_found');
      const methods=['/orders','/verify','/webhook','/connection'].includes(path)?['POST']:['GET'];
      reject(!methods.includes(request.method),405,'method_not_allowed');
      if(MODE==='live')reject(config.context!=='production'||!LIVE_ORIGINS.includes(url.origin),404,'not_found');
      if(path==='/webhook')return await webhook(request);
      // Same-origin API. No wildcard CORS or token-in-query support. Hosting
      // cookies never authorize application access; Google Bearer tokens do.
      const origin=request.headers.get('origin');
      reject(origin!==null&&origin!==url.origin,403,'origin_not_allowed');
      if(request.method==='POST')reject(origin!==url.origin,403,'origin_required');
      if(path==='/config'){
        // Off means no DB/API/storage work and no credits consumed by probes
        // beyond the one Function invocation. It does not promise readiness.
        if(!config.enabled)return json({mode:MODE,enabled:false,reason:'setup_required',currency:'INR'});
        const products=await repository.products();
        return json({mode:MODE,enabled:products.length>0,reason:products.length?'ready':'no_private_papers',
          keyId:config.keyId,currency:'INR',products:products.map(({id,title,branch,amount,currency})=>({id,title,branch,amount,currency}))});
      }
      if(path==='/connection'){
        // This is not a public readiness endpoint. Even an empty query consumes
        // a read; never touch Firestore before Google/UID authorization. POST
        // requires same-origin JSON and cannot be triggered by an image/link.
        reject(MODE!=='test'||config.context!=='production'||url.origin!==TEST_SITE_ORIGIN,404,'connection_check_unavailable');
        const user=await verifyIdentity(request.headers.get('authorization'));
        reject(!config.testers.includes(user.uid),403,'tester_not_allowed');
        await parseBody(request,[]);
        reject(!config.checkoutFlagsOff,409,'disable_test_checkout');
        reject(!config.firestoreConfigured,503,'firestore_not_configured');
        reject(typeof connectionCheck!=='function',503,'connection_check_unavailable');
        await connectionCheck();
        return json({mode:MODE,database:'firestore',readable:true,readOnly:true,checkoutEnabled:false,paymentsVerified:false});
      }
      // Existing LIVE purchases remain readable when new checkout is paused or
      // gateway keys need attention. Provider-backed routes still require keys.
      if(MODE==='live'&&(path==='/purchases'||path.startsWith('/content/')))
        reject(!config.firestoreConfigured,503,'backend_not_configured');
      else requireSetup();
      const user=await verifyIdentity(request.headers.get('authorization'));
      if(MODE==='test')reject(!config.testers.includes(user.uid),403,'tester_not_allowed');
      if(path==='/orders'){
        reject(!config.enabled,503,MODE==='live'?'live_checkout_disabled':'test_checkout_disabled');
        if(MODE==='live')reject(config.livePilots?.length&&!config.livePilots.includes(user.uid),403,'live_pilot_only');
        const body=await parseBody(request,['productId','requestId']);
        reject(!productPattern.test(body.productId)||!uuidPattern.test(body.requestId),400,'invalid_order_request');
        const product=await repository.product(body.productId);reject(!product,404,'paper_unavailable');
        // Price is ALWAYS derived on the server, never from caller fields.
        reject(product.amount!==PRICES[product.branch],503,'product_configuration_invalid');
        const reserved=await repository.reserve(user.uid,product,body.requestId);
        let stored=reserved.order;
        if(reserved.created){
          // Do not even create a provider order for a paper whose private files
          // are missing. An import record alone is not evidence of availability.
          let available=false;try{available=await assets.ready(product);}catch(_){}
          if(!available){await repository.unavailable(stored.id);throw new Problem(503,'private_paper_not_ready');}
          try{
            const order=await provider.createOrder(stored);
            reject(!providerOrderPattern.test(order?.id||'')||order.amount!==stored.amount||order.currency!=='INR'||
              order.receipt!==stored.receipt||order.partial_payment===true||order.status!=='created',503,'provider_order_mismatch');
            stored=await repository.attachOrder(stored.id,order.id);
          }catch(error){await repository.uncertain(stored.id);throw error;}
        }
        reject(stored.status==='reserving',409,'order_being_created');
        reject(stored.status!=='created'||!stored.razorpay_order_id,409,'order_pending_operator_review');
        return json({mode:MODE,keyId:config.keyId,orderId:stored.razorpay_order_id,productId:stored.product_id,
          amount:stored.amount,currency:'INR'},reserved.created?201:200);
      }
      if(path==='/verify'){
        const body=await parseBody(request,['orderId','paymentId','signature']);
        reject(!providerOrderPattern.test(body.orderId)||!providerPaymentPattern.test(body.paymentId),400,'invalid_payment');
        const stored=await repository.order(body.orderId);
        // Never let one signed-in user claim, inspect or reassign another's order.
        reject(!stored||stored.uid!==user.uid,404,'order_not_found');
        reject(!validSignature(config.keySecret,stored.razorpay_order_id+'|'+body.paymentId,body.signature),401,'invalid_payment_signature');
        return json(await grant(stored,body.paymentId));
      }
      if(path==='/purchases')return json({mode:MODE,purchases:await repository.purchases(user.uid)});
      const content=/^\/content\/([^/]+)(?:\/([a-f0-9]{64}))?$/.exec(path);
      if(content){
        const [,id,assetId]=content;reject(!productPattern.test(id),404,'not_found');
        reject(!await repository.owns(user.uid,id),403,'purchase_required');
        const product=await repository.product(id,MODE==='live');reject(!product,404,'paper_unavailable');
        if(!assetId)return json({mode:MODE,productId:id,readerAsset:product.reader_asset,
          assets:product.assets.map(({id,path,mime,bytes})=>({id,path,mime,bytes}))});
        const asset=product.assets.find(a=>a.id===assetId&&assetPattern.test(a.id));
        reject(!asset||!Number.isInteger(asset.bytes)||asset.bytes<1||asset.bytes>MAX_ASSET_BYTES,404,'asset_unavailable');
        const value=await assets.get(id,asset.id);
        reject(!value||value.byteLength!==asset.bytes||digest(Buffer.from(value))!==asset.id,503,'asset_unavailable');
        return new Response(value,{headers:{...headers,'Content-Type':asset.mime,
          'Content-Disposition':'attachment; filename="'+asset.id+'"'}});
      }
      throw new Problem(404,'not_found');
    }catch(error){
      const status=error instanceof Problem?error.status:503;
      const code=error instanceof Problem?error.code:'backend_unavailable';
      // No raw errors, Authorization headers, keys, body/PII, database URLs or
      // provider response objects reach responses or the application log.
      try{log(code);}catch(_){}
      return json({mode:MODE,error:code},status,status===429?{'Retry-After':code==='connection_check_rate_limited'?'30':'3600'}:{});
    }
  };
}
