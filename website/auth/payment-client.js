// This lives INSIDE the self-hosted Auth bundle. No generic token getter,
// arbitrary URL fetch, Firestore SDK, browser entitlement or token storage API.
const origins=new Set(['https://www.diplomaone.in','https://vermillion-pothos-520a34.netlify.app']);
const prefix='/api/payments/live',checkoutSrc='https://checkout.razorpay.com/v1/checkout.js';
const prices=Object.freeze({computer:1900,mechanical:2900,electrical:2900,civil:2900,chemical:3900});
const full=(pattern,value)=>typeof value==='string'&&pattern.exec(value)?.[0]===value;
const productId=value=>full(/^(?:DI[0-9]{8}|[0-9]{7})--[a-z][a-z0-9]*-[0-9]{4}$/,value)&&
  !['DI01000021','DI01000121'].includes(value.split('--')[0]);
const assetId=value=>full(/^[a-f0-9]{64}$/,value);
const pageFor=id=>'#/paper/'+id.replace('--','/');
const codes=new Set(['sign_in_required','invalid_or_expired_session','purchase_required','already_owned','paper_unavailable',
 'private_paper_not_ready','live_checkout_disabled','live_pilot_only','backend_not_configured','order_limit','order_being_created',
 'order_pending_operator_review','payment_not_captured_or_mismatch','payment_revoked','payment_timeout','session_changed',
 'checkout_unavailable','checkout_closed','payment_failed','payments_unavailable','payment_site_required']);
const failure=code=>Object.freeze({ok:false,code:codes.has(code)?code:'payments_unavailable'});
const fail=code=>{throw {code};};
const pathSafe=value=>typeof value==='string'&&value.length>0&&value.length<=220&&!/[\\\x00-\x1f?#%]/.test(value)&&
  value.split('/').every(part=>part&&part!=='.'&&part!=='..');
const mimes=new Set(['text/plain; charset=utf-8','image/png','image/webp','image/jpeg','application/pdf']);
const product=value=>value&&productId(value.id)&&typeof value.title==='string'&&value.title.trim()&&value.title.length<=200&&
 Object.hasOwn(prices,value.branch)&&value.amount===prices[value.branch]&&value.currency==='INR';
async function bounded(response,limit){
 const declared=response.headers.get('content-length');
 if(declared!==null&&(!/^\d+$/.test(declared)||Number(declared)>limit))fail('payments_unavailable');
 const reader=response.body?.getReader();if(!reader)fail('payments_unavailable');
 const chunks=[];let length=0;
 try{while(true){const {done,value}=await reader.read();if(done)break;length+=value.length;
  if(length>limit){await reader.cancel();fail('payments_unavailable');}chunks.push(value);}
 }finally{reader.releaseLock();}
 const out=new Uint8Array(length);let offset=0;for(const chunk of chunks){out.set(chunk,offset);offset+=chunk.length;}return out;
}
export function createPaymentClient(currentUser,{fetcher=globalThis.fetch,location=globalThis.location,
 document=globalThis.document,window=globalThis.window,url=globalThis.URL,timeoutMs=20000,checkoutTimeoutMs=15*60*1000}={}){
 let disposed=false,generation=0,checkout=null,loading=null,buying=null;
 const operations=new Set(),manifests=new Map(),blobURLs=new Map(),assetRequests=new Map();
 function current(record){
  if(disposed||record.generation!==generation||record.abort.signal.aborted||!origins.has(location?.origin)||
   location.hash!==record.page||(record.user&&currentUser()!==record.user))fail('session_changed');
 }
 function cancel(){
  ++generation;for(const op of operations){op.abort.abort();op.cancel();}operations.clear();
  try{checkout?.close();}catch(_){}checkout=null;
  for(const value of blobURLs.values())url.revokeObjectURL(value);
  blobURLs.clear();manifests.clear();assetRequests.clear();buying=null;
 }
 function run(operation,{authenticated=true,page=location?.hash,timeout=timeoutMs}={}){
  if(disposed)return Promise.resolve(failure('session_changed'));
  if(!origins.has(location?.origin))return Promise.resolve(failure('payment_site_required'));
  let user;try{user=authenticated?currentUser():null;}catch(_){return Promise.resolve(failure('sign_in_required'));}
  if(authenticated&&(!user||typeof user.getIdToken!=='function'))return Promise.resolve(failure('sign_in_required'));
  const record={generation,user,page,abort:new AbortController(),cancel:null};let timer;
  const cancelled=new Promise(resolve=>{record.cancel=()=>resolve(failure('session_changed'));});operations.add(record);
  const deadline=new Promise(resolve=>{timer=setTimeout(()=>{record.abort.abort();resolve(failure('payment_timeout'));},timeout);});
  const promise=(async()=>{current(record);const value=await operation(record);current(record);return value;})();
  return Promise.race([promise,cancelled,deadline]).catch(error=>failure(error?.code)).finally(()=>{clearTimeout(timer);operations.delete(record);});
 }
 async function request(record,path,options={}){
  let timer;
  const operation=requestBytes(record,path,options);
  const deadline=new Promise((_,reject)=>{timer=setTimeout(()=>{record.abort.abort();reject({code:'payment_timeout'});},timeoutMs);});
  try{return await Promise.race([operation,deadline]);}finally{clearTimeout(timer);}
 }
 async function requestBytes(record,path,{method='GET',body,asset}={}){
  current(record);const headers={};
  if(record.user){
   let token;try{token=await record.user.getIdToken();}catch(_){fail('sign_in_required');}
   current(record);
   if(typeof token!=='string'||token.length<20||token.length>16000||/[^A-Za-z0-9_.-]/.test(token))fail('sign_in_required');
   headers.Authorization='Bearer '+token;
  }
  if(body!==undefined)headers['Content-Type']='application/json';
  const response=await fetcher(prefix+path,{method,headers,...(body===undefined?{}:{body:JSON.stringify(body)}),
   cache:'no-store',credentials:'same-origin',redirect:'error',signal:record.abort.signal});
  current(record);if(response.redirected)fail('payments_unavailable');
  const mime=response.headers.get('content-type')||'';
  if(asset&&response.ok){
   if(mime.toLowerCase()!==asset.mime.toLowerCase())fail('payments_unavailable');
   const bytes=await bounded(response,asset.bytes);current(record);
   if(bytes.length!==asset.bytes)fail('payments_unavailable');return bytes;
  }
  if(!/^application\/json(?:\s*;|$)/i.test(mime))fail('payments_unavailable');
  const bytes=await bounded(response,256*1024);current(record);
  let data;try{data=JSON.parse(new TextDecoder().decode(bytes));}catch(_){fail('payments_unavailable');}
  if(data?.mode!=='live')fail('payments_unavailable');
  if(!response.ok)fail(data.error);
  return data;
 }
 async function config(record){
  const data=await request(record,'/config');
  if(data.enabled===false)return {enabled:false,products:[]};
  if(data.enabled!==true||data.currency!=='INR'||!full(/^rzp_live_[A-Za-z0-9]{10,50}$/,data.keyId)||
   !Array.isArray(data.products)||data.products.length<1||data.products.length>100||data.products.some(p=>!product(p))||
   new Set(data.products.map(p=>p.id)).size!==data.products.length)fail('payments_unavailable');
  return {enabled:true,keyId:data.keyId,products:data.products.map(({id,title,branch,amount,currency})=>({id,title,branch,amount,currency}))};
 }
 function loadCheckout(){
  if(typeof window.Razorpay==='function')return Promise.resolve(window.Razorpay);
  if(loading)return loading;
  loading=new Promise((resolve,reject)=>{
   const script=document.createElement('script');script.src=checkoutSrc;script.async=true;script.referrerPolicy='no-referrer';
   let timer;
   const finish=ok=>{clearTimeout(timer);script.onload=script.onerror=null;
    if(ok&&typeof window.Razorpay==='function')resolve(window.Razorpay);
    else{script.remove();loading=null;reject({code:'checkout_unavailable'});}};
   script.onload=()=>finish(true);script.onerror=()=>finish(false);timer=setTimeout(()=>finish(false),20000);document.head.appendChild(script);
  });return loading;
 }
 async function purchases(){return run(async record=>{
  const data=await request(record,'/purchases');
  if(!Array.isArray(data.purchases)||data.purchases.length>100)fail('payments_unavailable');
  const purchases=data.purchases.map(p=>{
   if(!product({...p,id:p.productId})||typeof p.active!=='boolean'||!full(/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{3}Z$/,p.purchasedAt)||
    !Number.isFinite(Date.parse(p.purchasedAt)))fail('payments_unavailable');
   return Object.freeze({productId:p.productId,title:p.title,branch:p.branch,amount:p.amount,currency:p.currency,active:p.active,purchasedAt:p.purchasedAt});
  });return Object.freeze({ok:true,purchases:Object.freeze(purchases)});
 },{page:'#/purchases'});}
 function readPaper(id){
  if(!productId(id))return Promise.resolve(failure('paper_unavailable'));
  return run(async record=>{
   const manifest=await request(record,'/content/'+id);
   if(manifest.productId!==id||!assetId(manifest.readerAsset)||!Array.isArray(manifest.assets)||manifest.assets.length<1||manifest.assets.length>300)fail('payments_unavailable');
   const assets=manifest.assets.map(a=>{
    if(!assetId(a?.id)||!pathSafe(a.path)||!mimes.has(a.mime)||!Number.isInteger(a.bytes)||a.bytes<1||a.bytes>4*1024*1024)fail('payments_unavailable');
    return Object.freeze({id:a.id,path:a.path,mime:a.mime,bytes:a.bytes});
   });
   if(new Set(assets.map(a=>a.path)).size!==assets.length)fail('payments_unavailable');
   const reader=assets.find(a=>a.id===manifest.readerAsset&&a.mime==='text/plain; charset=utf-8'&&a.path.endsWith('.html'));
   if(!reader)fail('payments_unavailable');
   const bytes=await request(record,'/content/'+id+'/'+reader.id,{asset:reader});
   const html=new TextDecoder('utf-8',{fatal:true}).decode(bytes);current(record);
   manifests.set(id,{user:record.user,page:record.page,generation:record.generation,assets});
   return Object.freeze({ok:true,productId:id,html,readerPath:reader.path,assets:Object.freeze(assets)});
  },{page:pageFor(id)});
 }
 function readAsset(id,hash){
  if(!productId(id)||!assetId(hash))return Promise.resolve(failure('paper_unavailable'));
  const key=id+'/'+hash;
  if(assetRequests.has(key))return assetRequests.get(key);
  const result=run(async record=>{
   const manifest=manifests.get(id),asset=manifest?.assets.find(a=>a.id===hash);
   if(!manifest||manifest.user!==record.user||manifest.page!==record.page||manifest.generation!==record.generation||
    !asset||!['image/png','image/webp','image/jpeg','application/pdf'].includes(asset.mime))fail('purchase_required');
   if(!blobURLs.has(key)){
    const bytes=await request(record,'/content/'+id+'/'+hash,{asset});current(record);
    const blobURL=url.createObjectURL(new Blob([bytes],{type:asset.mime}));blobURLs.set(key,blobURL);
   }
   return Object.freeze({ok:true,url:blobURLs.get(key)});
  },{page:pageFor(id)}).finally(()=>{if(assetRequests.get(key)===result)assetRequests.delete(key);});
  assetRequests.set(key,result);return result;
 }
 function buy(id){
  if(!productId(id))return Promise.resolve(failure('paper_unavailable'));
  if(buying)return buying.id===id?buying.promise:Promise.resolve(failure('checkout_unavailable'));
  const pending=run(async record=>{
   // Only the server supplies the order, price and live public key. Listing
   // prices are informative, never inputs to authorization or fulfillment.
   const settings=await config(record),selected=settings.products.find(p=>p.id===id);
   if(!settings.enabled)fail('live_checkout_disabled');if(!selected)fail('paper_unavailable');
   const Razorpay=await loadCheckout();current(record);
   const order=await request(record,'/orders',{method:'POST',body:{productId:id,requestId:globalThis.crypto.randomUUID()}});
   if(order.productId!==id||order.keyId!==settings.keyId||order.currency!=='INR'||order.amount!==selected.amount||
    !full(/^order_[A-Za-z0-9]{5,80}$/,order.orderId))fail('payments_unavailable');
   const result=await new Promise(resolve=>{
    let settled=false,verifying=false;
    const finish=value=>{if(!settled){settled=true;checkout=null;resolve(value);}};
    const instance=new Razorpay({key:order.keyId,order_id:order.orderId,amount:order.amount,currency:'INR',name:'DiplomaOne',
     description:selected.title,modal:{ondismiss:()=>{if(!verifying)finish(failure('checkout_closed'));}},
     handler:async value=>{
      if(settled||verifying)return;verifying=true;
      try{
       current(record);
       if(value?.razorpay_order_id!==order.orderId||!full(/^pay_[A-Za-z0-9]{5,80}$/,value?.razorpay_payment_id)||
        !full(/^[a-f0-9]{64}$/i,value?.razorpay_signature))fail('payments_unavailable');
       const verified=await request(record,'/verify',{method:'POST',body:{orderId:order.orderId,paymentId:value.razorpay_payment_id,signature:value.razorpay_signature}});
       if(verified.productId!==id||verified.owned!==true)fail('payments_unavailable');
       finish(Object.freeze({ok:true,productId:id}));
      }catch(error){finish(failure(error?.code));}
     }});
    checkout=instance;
    instance.on('payment.failed',()=>{finish(failure('payment_failed'));try{instance.close();}catch(_){}});
    record.abort.signal.addEventListener('abort',()=>{finish(failure('session_changed'));try{instance.close();}catch(_){}},{once:true});
    try{instance.open();}catch(_){finish(failure('checkout_unavailable'));}
   });return result;
  },{page:pageFor(id),timeout:checkoutTimeoutMs}).finally(()=>{if(buying?.promise===pending)buying=null;});
  buying={id,promise:pending};return pending;
 }
 return Object.freeze({purchases,readPaper,readAsset,buy,cancel,
  configuration:()=>run(async record=>Object.freeze({ok:true,...await config(record)}),{authenticated:false}),
  dispose(){disposed=true;cancel();}});
}
