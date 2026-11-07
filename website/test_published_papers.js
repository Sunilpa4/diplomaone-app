// Integration check: these published pages must be readable cross-origin by Netlify.
const assert = require('node:assert/strict');
const codes = ['DI03000141','DI03000151','DI03000161','DI03000171','DI03000201','DI03019011'];
(async()=>{
  const listing=await fetch('https://api.github.com/repos/Sunilpa4/diplomaone-content/git/trees/main?recursive=1',{headers:{Origin:'https://diplomaone.in'},redirect:'error',signal:AbortSignal.timeout(20000)});
  assert(listing.ok,`GitHub paper discovery: HTTP ${listing.status}`);
  assert.equal(listing.headers.get('access-control-allow-origin'),'*','GitHub API must allow cross-origin reads');
  const tree=await listing.json();
  assert.equal(tree.truncated,false,'GitHub repository tree must not be truncated');
  for(const code of codes)assert(tree.tree.some(item=>item.path===`papers/${code}/summer-2026.html` && item.type==='blob'),`${code}: paper missing from tree`);
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
