// Build and execute the actual Netlify entry WITHOUT secrets/network. Artifacts
// stay under ignored build/. This is not a Netlify deployment or live payment.
import {build} from 'esbuild';
import {mkdir} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const output=path.join(root,'build/payments-bundle-smoke/payments.cjs');
await mkdir(path.dirname(output),{recursive:true});
await build({absWorkingDir:root,entryPoints:['netlify/functions/payments.mjs'],outfile:output,
  bundle:true,platform:'node',target:'node22',format:'cjs',external:['pg-native'],logLevel:'warning'});
const script=`const assert=require('node:assert/strict');const mod=require(${JSON.stringify(output)});
assert.deepEqual(mod.config,{path:'/api/payments/test/*'});
(async()=>{const response=await mod.default(new Request('https://www.diplomaone.in/api/payments/test/config'));
assert.equal(response.status,200);const body=await response.json();assert.equal(body.mode,'test');assert.equal(body.enabled,false);
assert.equal(body.products,undefined);console.log('Actual function bundle: no-secret startup, native route and disabled checkout passed');})().catch(e=>{console.error(e);process.exitCode=1;});`;
const result=spawnSync(process.execPath,['-e',script],{encoding:'utf8',env:{PATH:process.env.PATH,NODE_ENV:'test'}});
process.stdout.write(result.stdout);process.stderr.write(result.stderr);
if(result.status!==0)throw new Error('Function bundle smoke failed');
