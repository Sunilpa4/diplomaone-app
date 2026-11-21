import {productionHandler} from '../../backend/src/runtime.mjs';
const handlers=new Map();
export default async request=>{
  const mode=new URL(request.url).pathname.startsWith('/api/payments/live/')?'live':'test';
  try{
    if(!handlers.has(mode))handlers.set(mode,productionHandler(process.env,mode));
    return await handlers.get(mode)(request);
  }catch(_){
    return Response.json({mode,error:'backend_not_configured'},{status:503,
      headers:{'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});
  }
};
// Both modes are explicit, isolated, same-origin and OFF by default.
export const config={path:'/api/payments/*'};
