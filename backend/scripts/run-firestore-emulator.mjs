// One-shot, credential-free TEST runner. Does not download, deploy, log in or
// provision a Google service. CI downloads the checksum-pinned official JAR.
import assert from 'node:assert/strict';
import {readFile,mkdir,stat} from 'node:fs/promises';
import {createReadStream,createWriteStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {spawn} from 'node:child_process';
import {createConnection} from 'node:net';
import {fileURLToPath} from 'node:url';
import {setTimeout as delay} from 'node:timers/promises';
import {finished} from 'node:stream/promises';
import path from 'node:path';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const manifest=JSON.parse(await readFile(path.join(root,'backend/test/firestore-emulator.json'),'utf8'));
const jar=path.resolve(process.env.FIRESTORE_EMULATOR_JAR||path.join(root,'build/test-tools/cloud-firestore-emulator-v'+manifest.version+'.jar'));
assert.equal((await stat(jar)).size,manifest.bytes,'Wrong Firestore emulator JAR size');
const hash=createHash('sha256');for await(const bytes of createReadStream(jar))hash.update(bytes);
assert.equal(hash.digest('hex'),manifest.sha256,'Firestore emulator JAR checksum mismatch');
const host='127.0.0.1',port=8085;
const open=()=>new Promise(resolve=>{
  const socket=createConnection({host,port}),finish=ok=>{socket.destroy();resolve(ok);};
  socket.once('connect',()=>finish(true));socket.once('error',()=>finish(false));socket.setTimeout(500,()=>finish(false));
});
assert(!await open(),'Refuse to test against an existing server on port 8085');
// Do not forward private owner/CI credentials. The SDK is pinned to a demo
// project on loopback, and deployed Firestore configuration refuses emulators.
const env=Object.fromEntries(['PATH','JAVA_HOME','HOME','TMPDIR','LANG','SYSTEMROOT'].filter(k=>process.env[k]).map(k=>[k,process.env[k]]));
Object.assign(env,{NODE_ENV:'test',FIRESTORE_EMULATOR_HOST:host+':'+port,GCLOUD_PROJECT:'demo-diplomaone-payments',GOOGLE_CLOUD_PROJECT:'demo-diplomaone-payments'});
await mkdir(path.join(root,'build'),{recursive:true});
const logFile=path.join(root,'build/firestore-emulator.log'),log=createWriteStream(logFile);
const java=spawn('java',['-Duser.language=en','-jar',jar,'--host',host,'--port',String(port),
  '--project_id','demo-diplomaone-payments','--rules',path.join(root,'backend/test/firestore-deny.rules')],{cwd:root,env,stdio:['ignore','pipe','pipe']});
java.stdout.pipe(log,{end:false});java.stderr.pipe(log,{end:false});
let ended=false,startError=null;
java.once('error',error=>{startError=error;ended=true;});
const exited=new Promise(resolve=>java.once('close',()=>{ended=true;resolve();}));
try{
  const deadline=Date.now()+60000;
  while(!await open()){
    if(ended)throw new Error('Firestore emulator exited before startup: '+(startError?.message||'see build/firestore-emulator.log'));
    assert(Date.now()<deadline,'Firestore emulator startup timeout');await delay(200);
  }
  console.log('Official Firestore emulator '+manifest.version+' ready on loopback; DEMO project only');
  const result=await new Promise(resolve=>{
    const child=spawn(process.execPath,['backend/scripts/test-with-emulator.mjs'],{cwd:root,env,stdio:'inherit'});
    child.once('error',()=>resolve(1));child.once('close',code=>resolve(code??1));
  });
  process.exitCode=result;
}catch(error){
  console.error('::error::'+String(error.message).replaceAll('%','%25').replaceAll('\n','%0A'));
  process.exitCode=1;
}finally{
  java.kill('SIGTERM');
  if(!ended){await Promise.race([exited,delay(4000)]);if(!ended){java.kill('SIGKILL');await exited;}}
  log.end();await finished(log);
  if(process.exitCode){
    const detail=(await readFile(logFile,'utf8')).slice(-8000);
    console.error(detail);
    console.error('::error::DEMO emulator diagnostics: '+detail.replaceAll('%','%25').replaceAll('\r','%0D').replaceAll('\n','%0A'));
  }
}
