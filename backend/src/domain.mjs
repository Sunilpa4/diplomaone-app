import {createHash,createHmac,timingSafeEqual} from 'node:crypto';
import {firestoreOptions} from './firestore-config.mjs';

export const MODE='test';
export const PREFIX='/api/payments/test';
export const TEST_SITE_ORIGIN='https://vermillion-pothos-520a34.netlify.app';
export const PRICES=Object.freeze({computer:1900,mechanical:2900,electrical:2900,civil:2900,chemical:3900});
export const FREE_CODES=Object.freeze(['DI01000021','DI01000121']); // Maths-I, Applied Physics only.
export const MAX_ASSET_BYTES=4*1024*1024; // Below buffered Functions response limits.
// Absolute end, not JS `$` (which also permits a final newline).
export const productPattern=/^(DI[0-9]{8}|[0-9]{7})--([a-z][a-z0-9]*-[0-9]{4})(?![\s\S])/;
export const providerOrderPattern=/^order_[A-Za-z0-9]{5,80}(?![\s\S])/;
export const providerPaymentPattern=/^pay_[A-Za-z0-9]{5,80}(?![\s\S])/;
export const assetPattern=/^[a-f0-9]{64}(?![\s\S])/;
export const uuidPattern=/^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}(?![\s\S])/i;
export const MIME=Object.freeze({'.html':'text/plain; charset=utf-8','.png':'image/png','.webp':'image/webp','.jpg':'image/jpeg','.jpeg':'image/jpeg','.pdf':'application/pdf'});
export class Problem extends Error {
  constructor(status,code){super(code);this.status=status;this.code=code;}
}
export const reject=(condition,status,code)=>{if(condition)throw new Problem(status,code);};
export const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
export const hmac=(secret,body)=>createHmac('sha256',secret).update(body).digest('hex');
export function validSignature(secret,body,signature){
  return typeof signature==='string'&&signature.length===64&&/^[a-f0-9]{64}$/i.test(signature)&&
    timingSafeEqual(Buffer.from(hmac(secret,body),'hex'),Buffer.from(signature,'hex'));
}
export function validateProduct(product){
  const match=productPattern.exec(product?.id||'');
  reject(!match||match[0]!==product.id||typeof product.title!=='string'||!product.title.trim()||product.title.length>200,400,'invalid_product');
  reject(!Object.hasOwn(PRICES,product.branch),400,'invalid_branch');
  reject(FREE_CODES.includes(match[1]),400,'common_subject_is_free');
  return {...product,code:match[1],session:match[2],amount:PRICES[product.branch],currency:'INR'};
}
export const LIVE_ORIGINS=Object.freeze(['https://www.diplomaone.in',TEST_SITE_ORIGIN]);
export function readConfig(env=process.env,mode='test'){
  reject(!['test','live'].includes(mode),503,'invalid_payment_mode');
  const live=mode==='live';
  const keyId=live?(env.RAZORPAY_LIVE_KEY_ID||''):(env.RAZORPAY_KEY_ID||'rzp_test_ToAdJ9DdVMFeM2');
  const keySecret=live?env.RAZORPAY_LIVE_KEY_SECRET:env.RAZORPAY_KEY_SECRET;
  const webhookSecret=live?env.RAZORPAY_LIVE_WEBHOOK_SECRET:env.RAZORPAY_WEBHOOK_SECRET;
  const context=env.CONTEXT||'';
  const testers=[...new Set((env.PAYMENTS_TESTER_UIDS||'').split(',').map(value=>value.trim()).filter(Boolean))];
  const validTesters=testers.length>0&&testers.length<=10&&testers.every(uid=>uid.length<=128&&!/[\x00-\x1f]/.test(uid));
  // Optional owner-controlled soft launch. Invalid nonempty values fail shut;
  // this limits NEW orders only, never existing owners or signed webhooks.
  const pilots=[...new Set((env.PAYMENTS_LIVE_PILOT_UIDS||'').split(',').map(value=>value.trim()).filter(Boolean))];
  const validPilots=!(env.PAYMENTS_LIVE_PILOT_UIDS||'').trim()||pilots.length>0&&pilots.length<=10&&pilots.every(uid=>uid.length<=128&&!/[\x00-\x1f]/.test(uid));
  const firestoreConfigured=!!firestoreOptions(env);
  // Setup diagnostics must work without a Razorpay secret, but cannot be used
  // while either checkout switch is on (including partial/invalid settings).
  const checkoutFlagsOff=[env.PAYMENTS_TEST_ENABLED,env.PAYMENTS_PRIVATE_MIGRATION_CONFIRMED,env.PAYMENTS_LIVE_ENABLED]
    .every(value=>value===undefined||value===''||value==='false');
  // Separate keys, namespaces and launch gates. Live NEVER falls back to test
  // keys/records. A missing setup performs no DB/provider work at /config.
  const configured=!/[^A-Za-z0-9_]/.test(keyId)&&(live?/^rzp_live_[A-Za-z0-9]{10,50}$/:/^rzp_test_[A-Za-z0-9]{10,50}$/).test(keyId)&&
    (live||env.RAZORPAY_KEY_ID===keyId)&&typeof keySecret==='string'&&keySecret.length>=16&&
    typeof webhookSecret==='string'&&webhookSecret.length>=32&&firestoreConfigured;
  const launch=live?['PAYMENTS_LIVE_ENABLED','PAYMENTS_LIVE_PRIVATE_MIGRATION_CONFIRMED',
    'PAYMENTS_LIVE_MERCHANT_CONFIRMED','PAYMENTS_LIVE_POLICIES_CONFIRMED'].every(name=>env[name]==='true'):
    validTesters&&env.PAYMENTS_TEST_ENABLED==='true'&&env.PAYMENTS_PRIVATE_MIGRATION_CONFIRMED==='true';
  return Object.freeze({mode,prefix:'/api/payments/'+mode,keyId,keySecret,webhookSecret,
    firebaseProject:'diplomaone-53b4e',context,configured,firestoreConfigured,checkoutFlagsOff,testers:Object.freeze(validTesters?testers:[]),
    livePilots:Object.freeze(validPilots?pilots:[]),enabled:configured&&context==='production'&&launch&&(!live||validPilots)});
}
export function confirmCaptured(order,payment,stored){
  reject(!order||!payment||order.id!==stored.razorpay_order_id||order.receipt!==stored.receipt||
    order.amount!==stored.amount||order.currency!=='INR'||order.status!=='paid'||order.amount_paid!==stored.amount||
    order.amount_due!==0||order.partial_payment===true||payment.order_id!==order.id||
    payment.amount!==stored.amount||payment.currency!=='INR'||payment.status!=='captured'||payment.captured!==true||
    payment.amount_refunded!==0,409,'payment_not_captured_or_mismatch');
}
