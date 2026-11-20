import {Problem,reject,providerOrderPattern,providerPaymentPattern} from './domain.mjs';

// REST calls are server-side only. Test keys are mandatory, never a live fallback.
export function razorpayClient(config,fetcher=fetch){
  reject(!/^rzp_test_[A-Za-z0-9]+$/.test(config.keyId)||!config.keySecret,503,'test_keys_required');
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
    // No capture, refund, payout or live-money API is implemented in this phase.
  };
}
