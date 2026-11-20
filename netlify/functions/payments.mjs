import {productionHandler} from '../../backend/src/runtime.mjs';
let handler;
export default async request=>{
  try{handler??=productionHandler();return await handler(request);}
  catch(_){
    // Configuration/runtime errors must not reveal connection strings or keys.
    return Response.json({mode:'test',error:'backend_not_configured'},{status:503,
      headers:{'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});
  }
};
// A same-origin API, not a browser call to localhost or to another service.
export const config={path:'/api/payments/test/*'};
