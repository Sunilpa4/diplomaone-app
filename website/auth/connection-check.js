// Bundled into the self-hosted Auth SDK; not a second public script. The
// caller gets only a small status, never an ID token, raw response or error.
const testOrigin='https://vermillion-pothos-520a34.netlify.app';
const endpoint='/api/payments/test/connection';
const testPage='#/test-connection';
const codes=new Set(['sign_in_required','invalid_or_expired_session','tester_not_allowed','disable_test_checkout',
  'firestore_not_configured','firestore_check_failed','connection_check_rate_limited','connection_check_unavailable']);
const failure=code=>Object.freeze({ok:false,code});
async function responseBody(response){
  if(!/^application\/json(?:\s*;|$)/i.test(response.headers.get('content-type')||''))return null;
  const reader=response.body?.getReader();if(!reader)return null;
  const chunks=[];let length=0;
  try{
    while(true){const {done,value}=await reader.read();if(done)break;
      length+=value.length;if(length>4096){await reader.cancel();return null;}chunks.push(value);}
    const bytes=new Uint8Array(length);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
    return JSON.parse(new TextDecoder().decode(bytes));
  }finally{reader.releaseLock();}
}
export function createConnectionCheck(currentUser,{fetcher=globalThis.fetch,location=globalThis.location,timeoutMs=15000}={}){
  let active=null,disposed=false;
  function cancel(){if(active){active.cancelled=true;active.abort.abort();active.finishCancellation();}}
  function check(){
    if(disposed)return Promise.resolve(failure('session_changed'));
    // Do not even request a token on GitHub Pages, other sites, localhost or
    // arbitrary preview hosts. This UI restriction is NOT server authorization.
    if(location?.origin!==testOrigin)return Promise.resolve(failure('test_site_required'));
    if(location?.hash!==testPage)return Promise.resolve(failure('connection_check_unavailable'));
    let user;try{user=currentUser();}catch(_){return Promise.resolve(failure('sign_in_required'));}
    if(!user||typeof user.getIdToken!=='function')return Promise.resolve(failure('sign_in_required'));
    if(active?.user===user&&!active.cancelled)return active.promise;
    cancel();
    const record={user,abort:new AbortController(),cancelled:false,promise:null,finishCancellation:null};active=record;
    const cancellation=new Promise(resolve=>{record.finishCancellation=()=>resolve(failure('session_changed'));});
    let timer;
    const operation=(async()=>{
      let token;
      try{token=await user.getIdToken();}catch(_){return failure('sign_in_required');}
      // Location changes before the hashchange handler necessarily runs. Check
      // the live route again so a late token cannot start a read after leaving.
      if(record.cancelled||disposed||location?.origin!==testOrigin||location?.hash!==testPage||currentUser()!==user)return failure('session_changed');
      if(record.abort.signal.aborted)return failure('connection_timeout');
      if(typeof token!=='string'||token.length<20||token.length>16000||/[^A-Za-z0-9_.-]/.test(token))return failure('sign_in_required');
      const response=await fetcher(endpoint,{method:'POST',headers:{'Content-Type':'application/json',Authorization:'Bearer '+token},
        body:'{}',cache:'no-store',redirect:'error',credentials:'same-origin',signal:record.abort.signal});
      // Hosting-gate cookies may accompany same-origin requests, but are NEVER
      // application authorization; the server also verifies Google + tester UID.
      if(response.redirected)return failure('connection_check_unavailable');
      const body=await responseBody(response);
      if(record.cancelled||disposed||location?.origin!==testOrigin||location?.hash!==testPage||currentUser()!==user)return failure('session_changed');
      if(body?.mode!=='test')return failure('connection_check_unavailable');
      if(!response.ok)return failure(codes.has(body.error)?body.error:'connection_check_unavailable');
      if(body.database!=='firestore'||body.readable!==true||body.readOnly!==true||
        body.checkoutEnabled!==false||body.paymentsVerified!==false)return failure('connection_check_unavailable');
      return Object.freeze({ok:true});
    })();
    const deadline=new Promise(resolve=>{timer=setTimeout(()=>{record.abort.abort();resolve(failure('connection_timeout'));},timeoutMs);});
    record.promise=Promise.race([operation,deadline,cancellation]).catch(()=>failure(record.cancelled||disposed?'session_changed':'connection_check_unavailable'))
      .finally(()=>{clearTimeout(timer);if(active===record)active=null;});
    return record.promise;
  }
  return Object.freeze({check,cancel,dispose(){disposed=true;cancel();}});
}
