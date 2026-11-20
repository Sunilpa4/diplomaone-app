import {createHash,createHmac,timingSafeEqual} from 'node:crypto';

export const MODE='test';
export const PREFIX='/api/payments/test';
export const PRICES=Object.freeze({computer:1900,mechanical:2900,electrical:2900,civil:2900,chemical:3900});
export const FREE_CODES=Object.freeze(['DI01000021','DI01000121']); // Maths-I, Applied Physics only.
export const MAX_ASSET_BYTES=4*1024*1024; // Below buffered Functions response limits.
export const productPattern=/^(DI[0-9]{8}|[0-9]{7})--([a-z][a-z0-9]*-[0-9]{4})$/;
export const providerOrderPattern=/^order_[A-Za-z0-9]{5,80}$/;
export const providerPaymentPattern=/^pay_[A-Za-z0-9]{5,80}$/;
export const assetPattern=/^[a-f0-9]{64}$/;
export const uuidPattern=/^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$/i;
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
export function readConfig(env=process.env){
  const keyId=env.RAZORPAY_KEY_ID||'rzp_test_ToAdJ9DdVMFeM2';
  const context=env.CONTEXT||'';
  const testers=[...new Set((env.PAYMENTS_TESTER_UIDS||'').split(',').map(value=>value.trim()).filter(Boolean))];
  const validTesters=testers.length>0&&testers.length<=10&&testers.every(uid=>uid.length<=128&&!/[\x00-\x1f]/.test(uid));
  // A preview must never inherit an enabled production checkout accidentally.
  const configured=env.RAZORPAY_KEY_ID===keyId&&/^rzp_test_[A-Za-z0-9]{10,50}$/.test(keyId)&&
    typeof env.RAZORPAY_KEY_SECRET==='string'&&env.RAZORPAY_KEY_SECRET.length>=16&&
    typeof env.RAZORPAY_WEBHOOK_SECRET==='string'&&env.RAZORPAY_WEBHOOK_SECRET.length>=32&&
    !!env.NETLIFY_DB_URL&&env.FIREBASE_PROJECT_ID==='diplomaone-53b4e';
  return Object.freeze({keyId,keySecret:env.RAZORPAY_KEY_SECRET,webhookSecret:env.RAZORPAY_WEBHOOK_SECRET,
    firebaseProject:'diplomaone-53b4e',context,configured,testers:Object.freeze(validTesters?testers:[]),
    enabled:configured&&validTesters&&context==='production'&&env.PAYMENTS_TEST_ENABLED==='true'&&env.PAYMENTS_PRIVATE_MIGRATION_CONFIRMED==='true'});
}
export function confirmCaptured(order,payment,stored){
  reject(!order||!payment||order.id!==stored.razorpay_order_id||order.receipt!==stored.receipt||
    order.amount!==stored.amount||order.currency!=='INR'||order.status!=='paid'||order.amount_paid!==stored.amount||
    order.amount_due!==0||order.partial_payment===true||payment.order_id!==order.id||
    payment.amount!==stored.amount||payment.currency!=='INR'||payment.status!=='captured'||payment.captured!==true||
    payment.amount_refunded!==0,409,'payment_not_captured_or_mismatch');
}
