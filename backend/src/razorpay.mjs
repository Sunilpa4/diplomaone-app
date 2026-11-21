import {Problem,reject,providerOrderPattern,providerPaymentPattern} from './domain.mjs';

// Server-side only. Explicit mode-specific credentials; NEVER a mode fallback.
export function razorpayClient(config,fetcher=fetch){
  const live=config.mode==='live';
  reject((config.mode!==undefined&&!['test','live'].includes(config.mode))||
    !(live?/^rzp_live_[A-Za-z0-9]+$/:/^rzp_test_[A-Za-z0-9]+$/).test(config.keyId)||!config.keySecret,
    503,live?'live_keys_required':'test_keys_required');
  const authorization='Basic '+Buffer.from(config.keyId+':'+config.keySecret).toString('base64');
  async function request(path,body){
    let response;
    try{response=await fetcher('https://api.razorpay.com/v1/'+path,{method:body?'POST':'GET',redirect:'error',
      headers:{Authorization:authorization,'Content-Type':'application/json'},
      ...(body?{body:JSON.stringify(body)}:{}),signal:AbortSignal.timeout(8000)});}
    catch(_){throw new Problem(503,'payment_provider_unavailable');}
    if(!response.ok)throw new Problem(503,'payment_provider_unavailable');
    try{return await response.json();}catch(_){throw new Problem(503,'payment_provider_unavailable');}
  }
  return {
    createOrder:stored=>request('orders',{amount:stored.amount,currency:'INR',receipt:stored.receipt,partial_payment:false}),
    order(id){reject(!providerOrderPattern.test(id),400,'invalid_order');return request('orders/'+id);},
    payment(id){reject(!providerPaymentPattern.test(id),400,'invalid_payment');return request('payments/'+id);},
    // No manual capture, refund, payout or arbitrary money-moving API. The
    // merchant must configure automatic full capture before opening sales.
  };
}
