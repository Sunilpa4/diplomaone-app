// Runs only against an extracted Netlify ZIP in a temporary directory OUTSIDE
// the checkout. Built-ins only: repository node_modules must not rescue it.
import assert from 'node:assert/strict';
import {createRequire,syncBuiltinESMExports} from 'node:module';
import http from 'node:http';
import https from 'node:https';
import net from 'node:net';
import tls from 'node:tls';
import {realpath,readFile} from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {PassThrough} from 'node:stream';
import {finished} from 'node:stream/promises';

const directory=await realpath(process.argv[2]);
const configured=process.argv[3]==='configured-disabled';
// NFT preserves the common ancestor of traced files. Once runtime packages are
// included, the user module may be nested rather than a root payments.mjs.
const entry=await readFile(path.join(directory,'___netlify-entry-point.mjs'),'utf8');
const match=/getLambdaHandler\((['"])(\.\/[^'"]+)\1\)/.exec(entry);
assert(match,'generated Lambda entry must point to the packaged user module');
const main=await realpath(path.resolve(directory,match[2]));
assert(main.startsWith(directory+path.sep));
const resolve=createRequire(main);
for(const name of ['@google-cloud/firestore','@netlify/blobs','jose']){
  const file=await realpath(resolve.resolve(name));
  assert(file.startsWith(directory+path.sep),`${name} must come from the deployed ZIP, not the checkout`);
}
// Block both fetch and the Node transports used by Google/Blobs SDKs. Safe
// disabled startup must not discover ADC, fetch JWKs or contact any service.
const forbidden=()=>{throw new Error('Network is forbidden in the disabled artifact smoke');};
globalThis.fetch=async()=>forbidden();
http.request=http.get=https.request=https.get=net.connect=net.createConnection=tls.connect=forbidden;
net.Socket.prototype.connect=forbidden;
syncBuiltinESMExports();
const mod=await import(pathToFileURL(main));
assert.deepEqual(mod.config,{path:'/api/payments/*'});
const prefix='https://unit-test.netlify.app/api/payments/test';
const response=await mod.default(new Request(prefix+'/config'));
assert.equal(response.status,200,'the actual package must initialize successfully, not hide an import/startup failure');
assert.deepEqual(await response.json(),{mode:'test',enabled:false,reason:'setup_required',currency:'INR'});
const unauthorized=await mod.default(new Request(prefix+'/purchases'));
assert.equal(unauthorized.status,configured?401:503);
assert.equal((await unauthorized.json()).error,configured?'sign_in_required':'backend_not_configured');

// The diagnostic must exist independently of Razorpay secrets, but never query
// Firestore or fetch JWKs before an authorized identity. Network is still blocked.
const testOrigin='https://vermillion-pothos-520a34.netlify.app';
const connection=await mod.default(new Request(testOrigin+'/api/payments/test/connection',{
  method:'POST',headers:{Origin:testOrigin,'Content-Type':'application/json'},body:'{}'}));
assert.equal(connection.status,process.argv[3]==='no-secret'?404:401);
assert.equal((await connection.json()).error,process.argv[3]==='no-secret'?'connection_check_unavailable':'sign_in_required');
const wrongSite=await mod.default(new Request(prefix+'/connection',{
  method:'POST',headers:{Origin:new URL(prefix).origin,'Content-Type':'application/json'},body:'{}'}));
assert.equal(wrongSite.status,404);assert.equal((await wrongSite.json()).error,'connection_check_unavailable');
const live=await mod.default(new Request(testOrigin+'/api/payments/live/config'));
assert.equal(live.status,process.argv[3]==='no-secret'?404:200);
assert.equal((await live.json()).mode,'live');
const liveOrder=await mod.default(new Request(testOrigin+'/api/payments/live/orders',{
 method:'POST',headers:{Origin:testOrigin,'Content-Type':'application/json'},body:'{}'}));
assert.equal(liveOrder.status,process.argv[3]==='no-secret'?404:process.argv[3]==='live-configured-disabled'?401:503);
const livePurchases=await mod.default(new Request(testOrigin+'/api/payments/live/purchases'));
assert.equal(livePurchases.status,process.argv[3]==='no-secret'?404:401,'existing-owner route initializes without live gateway keys, but still requires Google identity');

// Exercise Netlify's generated Lambda v2 bootstrap/entry as well as our default
// export. Only AWS's response-stream primitive is simulated, not the app code.
globalThis.awslambda={streamifyResponse:fn=>fn,HttpResponseStream:{
  from(stream,metadata){stream.responseMetadata=metadata;return stream;},
}};
const {handler}=await import(pathToFileURL(path.join(directory,'___netlify-entry-point.mjs')));
assert.equal(typeof handler,'function');
for(const [mode,rawUrl,expectedStatus] of [['test',prefix+'/config',200],
  ['live',testOrigin+'/api/payments/live/config',process.argv[3]==='no-secret'?404:200]]){
  const stream=new PassThrough(),chunks=[];
  stream.on('data',chunk=>chunks.push(chunk));const complete=finished(stream);
  await handler({rawUrl,httpMethod:'GET',headers:{},body:null,isBase64Encoded:false},stream,
    {awsRequestId:'unit-test-artifact',getRemainingTimeInMillis:()=>30000});
  await complete;assert.equal(stream.responseMetadata.statusCode,expectedStatus);
  const value=JSON.parse(Buffer.concat(chunks).toString('utf8'));
  assert.deepEqual(value,expectedStatus===200?{mode,enabled:false,reason:'setup_required',currency:'INR'}:{mode,error:'not_found'});
}
console.log(`Isolated Netlify ZIP: ${process.argv[3]} ESM import, bundled dependencies, isolated disabled live/test routes, diagnostic gates and native Lambda v2 bootstrap passed`);
