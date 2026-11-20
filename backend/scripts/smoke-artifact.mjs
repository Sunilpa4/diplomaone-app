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
assert.deepEqual(mod.config,{path:'/api/payments/test/*'});
const prefix='https://unit-test.netlify.app/api/payments/test';
const response=await mod.default(new Request(prefix+'/config'));
assert.equal(response.status,200,'the actual package must initialize successfully, not hide an import/startup failure');
assert.deepEqual(await response.json(),{mode:'test',enabled:false,reason:'setup_required',currency:'INR'});
const unauthorized=await mod.default(new Request(prefix+'/purchases'));
assert.equal(unauthorized.status,configured?401:503);
assert.equal((await unauthorized.json()).error,configured?'sign_in_required':'backend_not_configured');

// Exercise Netlify's generated Lambda v2 bootstrap/entry as well as our default
// export. Only AWS's response-stream primitive is simulated, not the app code.
globalThis.awslambda={streamifyResponse:fn=>fn,HttpResponseStream:{
  from(stream,metadata){stream.responseMetadata=metadata;return stream;},
}};
const {handler}=await import(pathToFileURL(path.join(directory,'___netlify-entry-point.mjs')));
assert.equal(typeof handler,'function');
const stream=new PassThrough(),chunks=[];
stream.on('data',chunk=>chunks.push(chunk));
const complete=finished(stream);
await handler({rawUrl:prefix+'/config',httpMethod:'GET',headers:{},body:null,isBase64Encoded:false},stream,
  {awsRequestId:'unit-test-artifact',getRemainingTimeInMillis:()=>30000});
await complete;
assert.equal(stream.responseMetadata.statusCode,200);
assert.deepEqual(JSON.parse(Buffer.concat(chunks).toString('utf8')),
  {mode:'test',enabled:false,reason:'setup_required',currency:'INR'});
console.log(`Isolated Netlify ZIP: ${configured?'configured but disabled':'no-secret'} ESM import, bundled dependencies, route and native Lambda v2 bootstrap passed`);
