// Integration check for the TWO FREE subjects only. Never require public paid
// answers (or fetch them) as a CI prerequisite: they must migrate privately.
const assert=require('node:assert/strict');
const codes=['DI01000021','DI01000121'];
(async()=>{
 const listing=await fetch('https://api.github.com/repos/Sunilpa4/diplomaone-content/git/trees/main?recursive=1',{
  headers:{Origin:'https://www.diplomaone.in'},redirect:'error',signal:AbortSignal.timeout(20000)});
 assert(listing.ok,`GitHub free-paper discovery: HTTP ${listing.status}`);
 assert.equal(listing.headers.get('access-control-allow-origin'),'*');
 const tree=await listing.json();assert.equal(tree.truncated,false,'Public metadata tree must not be truncated');
 for(const code of codes)for(const session of ['summer-2026','winter-2025']){
  assert(tree.tree.some(item=>item.path===`papers/${code}/${session}.html`&&item.type==='blob'),`${code}/${session}: free reader missing`);
  const response=await fetch(`https://sunilpa4.github.io/diplomaone-content/papers/${code}/${session}.html`,{
   headers:{Origin:'https://www.diplomaone.in'},redirect:'error',signal:AbortSignal.timeout(20000)});
  assert(response.ok,`${code}/${session}: HTTP ${response.status}`);
  assert.equal(response.headers.get('access-control-allow-origin'),'*');
  const html=await response.text();assert(/<main[\s>]/i.test(html)&&/<details[\s>]/i.test(html),'Free question-card reader required');
  console.log(`${code}/${session}: free cards remain publicly readable`);
 }
})().catch(error=>{console.error(error);process.exitCode=1;});
