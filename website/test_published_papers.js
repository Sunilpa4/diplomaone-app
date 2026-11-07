// Integration check: these published pages must be readable cross-origin by Netlify.
const assert = require('node:assert/strict');
const codes = ['DI03000141','DI03000151','DI03000161','DI03000171','DI03000201','DI03019011'];
(async()=>{
  for(const code of codes){
    const url=`https://sunilpa4.github.io/diplomaone-content/papers/${code}/summer-2026.html`;
    const response=await fetch(url,{headers:{Origin:'https://diplomaone.in'},redirect:'error',signal:AbortSignal.timeout(20000)});
    assert(response.ok,`${code}: HTTP ${response.status}`);
    assert.equal(response.headers.get('access-control-allow-origin'),'*',`${code}: GitHub Pages must allow cross-origin reads`);
    const html=await response.text();
    assert(/<main[\s>]/i.test(html)&&/<details[\s>]/i.test(html),`${code}: unexpected paper format`);
    console.log(`${code}: accessible with wildcard CORS`);
  }
})().catch(error=>{console.error(error);process.exitCode=1});
