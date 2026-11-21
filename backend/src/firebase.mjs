import {createRemoteJWKSet,jwtVerify} from 'jose';
import {Problem} from './domain.mjs';

const keys=createRemoteJWKSet(new URL('https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com'),
  {timeoutDuration:5000,cooldownDuration:30000,cacheMaxAge:600000});
// No Admin SDK/service-account key is necessary to verify Google's signed ID
// tokens. Revocation/disabled-user lookup is not claimed by this verifier.
export function firebaseVerifier(project='diplomaone-53b4e',keySet=keys,clock=()=>Date.now()){
  if(project!=='diplomaone-53b4e')throw new Error('Unexpected Firebase web project');
  return async authorization=>{
    const match=/^Bearer ([A-Za-z0-9_.-]{20,16000})$/.exec(authorization||'');
    if(!match)throw new Problem(401,'sign_in_required');
    try{
      const {payload:p}=await jwtVerify(match[1],keySet,{algorithms:['RS256'],audience:project,
        issuer:`https://securetoken.google.com/${project}`,currentDate:new Date(clock()),clockTolerance:5});
      const now=Math.floor(clock()/1000);
      if(typeof p.sub!=='string'||!p.sub||p.sub.length>128||p.aud!==project||
        !Number.isInteger(p.iat)||p.iat>now+5||!Number.isInteger(p.auth_time)||p.auth_time>now+5||p.auth_time<0||
        !Number.isInteger(p.exp)||p.firebase?.sign_in_provider!=='google.com')throw Error('Invalid identity');
      return Object.freeze({uid:p.sub});
    }catch(_){throw new Problem(401,'invalid_or_expired_session');}
  };
}
