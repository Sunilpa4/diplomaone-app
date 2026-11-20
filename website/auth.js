/* Authentication state only, never payment authorization. The small controller
   loads the self-hosted SDK when the account screen is first opened. */
(function(root, factory) {
  'use strict';
  const createAuthController=factory();
  if(typeof module==='object'&&module.exports)module.exports={createAuthController};
  else root.DiplomaOneAuth=createAuthController(()=>import('./assets/firebase-auth.js'));
})(typeof window!=='undefined'?window:globalThis, function() {
  'use strict';
  function publicUser(value) {
    if(!value||typeof value.uid!=='string'||!value.uid)return null;
    return Object.freeze({
      uid:value.uid.slice(0,128),
      displayName:typeof value.displayName==='string'?value.displayName.slice(0,200):'',
      email:typeof value.email==='string'?value.email.slice(0,320):'',
      emailVerified:value.emailVerified===true,
    });
  }
  const errorCode=error=>/^auth\/[a-z0-9-]+$/.test(error?.code||'')?error.code:'auth/unavailable';
  const checkCodes=new Set(['sign_in_required','invalid_or_expired_session','tester_not_allowed','disable_test_checkout',
    'firestore_not_configured','firestore_check_failed','connection_check_rate_limited','connection_check_unavailable',
    'connection_timeout','test_site_required','session_changed']);
  const checkFailure=code=>Object.freeze({ok:false,code});
  return function createAuthController(loadModule, timeoutMs=15000) {
    let state={status:'idle',user:null,busy:null,error:null},client=null,pending=null,generation=0,sessionVersion=0,checkPending=null,paymentVersion=0;
    const paymentPending=new Map();
    const listeners=new Set();
    const snapshot=()=>Object.freeze({...state,error:state.error?Object.freeze({...state.error}):null});
    const deliver=(listener,value)=>{try{listener(value);}catch(_){/* A view cannot break auth state. */}};
    const notify=()=>{const value=snapshot();for(const listener of listeners)deliver(listener,value);};
    const dispose=candidate=>{try{candidate?.dispose?.();}catch(_){/* Best-effort observer cleanup, never a new login. */}};
    const fail=(error,operation)=>{state.error={code:errorCode(error),operation};notify();};
    function initialize() {
      if(pending)return pending;
      if(client)return Promise.resolve(true);
      const version=++generation;let candidate=null,timer,observedUser=null,active=false;
      state={status:'loading',user:null,busy:null,error:null};
      const attempt=(async()=>{
        const sdk=await loadModule();
        if(version!==generation)return false;
        candidate=sdk.createClient(user=>{
          if(version!==generation)return;
          cancelTestConnection();cancelPayments();
          observedUser=publicUser(user);
          if(active){state.user=observedUser;state.status=observedUser?'signed-in':'signed-out';state.error=null;notify();}
        },error=>{if(version===generation){cancelTestConnection();cancelPayments();fail(error,'session');}});
        await candidate.ready();
        if(version!==generation){dispose(candidate);return false;}
        return true;
      })();
      const deadline=new Promise((_,reject)=>{timer=setTimeout(()=>reject({code:'auth/network-request-failed'}),timeoutMs);});
      pending=Promise.race([attempt,deadline]).then(ok=>{
        if(!ok)return false;
        client=candidate;active=true;state={status:observedUser?'signed-in':'signed-out',user:observedUser,busy:null,error:null};notify();return true;
      }).catch(error=>{
        ++generation;dispose(candidate);state={status:'unavailable',user:null,busy:null,error:{code:errorCode(error),operation:'initialize'}};notify();return false;
      }).finally(()=>{clearTimeout(timer);pending=null;});
      // Publish loading only after pending is set, including re-entrant views.
      notify();return pending;
    }
    function run(operation,language) {
      if(state.busy)return Promise.resolve(false);
      if(!client||!['signed-in','signed-out'].includes(state.status))return Promise.resolve(false);
      if(operation==='signIn'&&state.user)return Promise.resolve(true);
      if(operation==='signOut'&&!state.user)return Promise.resolve(true);
      if(operation==='signOut'){cancelTestConnection();cancelPayments();}
      state.busy=operation;state.error=null;notify();
      let result;
      // Invoke directly in the user's click, not after an await or SDK import.
      try{result=operation==='signIn'?client.signIn(language):client.signOut();}
      catch(error){result=Promise.reject(error);}
      return Promise.resolve(result).then(()=>true,error=>{fail(error,operation);return false;}).finally(()=>{state.busy=null;notify();});
    }
    function cancelTestConnection(){
      ++sessionVersion;checkPending=null;
      try{client?.cancelTestConnection?.();}catch(_){/* No raw adapter error reaches a view. */}
    }
    function checkTestConnection(){
      if(!client||state.status!=='signed-in'||!state.user||state.busy)return Promise.resolve(checkFailure('sign_in_required'));
      if(checkPending)return checkPending;
      if(typeof client.checkTestConnection!=='function')return Promise.resolve(checkFailure('connection_check_unavailable'));
      const version=sessionVersion,activeClient=client;let result;
      try{result=activeClient.checkTestConnection();}catch(_){result=Promise.resolve(checkFailure('connection_check_unavailable'));}
      const request=Promise.resolve(result).then(value=>{
        if(version!==sessionVersion||client!==activeClient||state.status!=='signed-in')return checkFailure('session_changed');
        if(value?.ok===true)return Object.freeze({ok:true});
        return checkFailure(checkCodes.has(value?.code)?value.code:'connection_check_unavailable');
      },()=>checkFailure('connection_check_unavailable')).finally(()=>{if(checkPending===request)checkPending=null;});
      checkPending=request;return request;
    }
    function cancelPayments(){
      ++paymentVersion;paymentPending.clear();
      try{client?.cancelPayments?.();}catch(_){/* No raw adapter errors. */}
    }
    function payment(method,args=[]){
      if(!client||state.busy||!['signed-in','signed-out'].includes(state.status))return Promise.resolve(checkFailure('sign_in_required'));
      if(method!=='paymentConfiguration'&&!state.user)return Promise.resolve(checkFailure('sign_in_required'));
      const key=method+JSON.stringify(args);if(paymentPending.has(key))return paymentPending.get(key);
      if(typeof client[method]!=='function')return Promise.resolve(checkFailure('payments_unavailable'));
      const version=paymentVersion,activeClient=client;
      const result=Promise.resolve().then(()=>{
        if(version!==paymentVersion||activeClient!==client)return checkFailure('session_changed');
        return activeClient[method](...args);
      }).then(value=>version===paymentVersion&&activeClient===client?value:checkFailure('session_changed'),()=>checkFailure('payments_unavailable'))
        .finally(()=>{if(paymentPending.get(key)===result)paymentPending.delete(key);});
      paymentPending.set(key,result);return result;
    }
    return Object.freeze({
      snapshot,initialize,checkTestConnection,cancelTestConnection,cancelPayments,
      paymentConfiguration:()=>payment('paymentConfiguration'),
      loadPurchases:()=>payment('loadPurchases'),
      readPurchasedPaper:id=>payment('readPurchasedPaper',[id]),
      readPurchasedAsset:(id,asset)=>payment('readPurchasedAsset',[id,asset]),
      buyPaper:id=>payment('buyPaper',[id]),
      subscribe(listener){if(typeof listener!=='function')throw new TypeError('Auth listener must be a function');listeners.add(listener);deliver(listener,snapshot());return()=>listeners.delete(listener);},
      signIn:language=>run('signIn',language),signOut:()=>run('signOut'),
    });
  };
});
