// Real staged-file/catalog-snapshot regression for the Mechanical recheck.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{JSDOM}=require('jsdom');
const root=path.resolve(__dirname,'..'),base=path.join(root,'papers-upload'),staged=path.join(base,'papers');
const audit=JSON.parse(fs.readFileSync(path.join(base,'mechanical-placement-audit.json'),'utf8'));
const catalog=audit.catalog_snapshot,codes=audit.mechanical_semester_3_codes,newCodes=['DI03000161','DI03000171','DI03000201','DI03019011'];
const tree={truncated:false,tree:fs.readdirSync(staged,{recursive:true}).filter(rel=>fs.statSync(path.join(staged,rel)).isFile()).map(rel=>({path:'papers/'+rel.split(path.sep).join('/'),type:'blob',mode:'100644'}))};
const dom=new JSDOM(fs.readFileSync(path.join(__dirname,'index.html'),'utf8'),{url:'https://diplomaone.in/#/branch/mechanical/3',runScripts:'outside-only'}),w=dom.window,requests=[];
w.scrollTo=()=>{};
w.fetch=async url=>{
 const s=String(url);requests.push(s);
 if(s.startsWith('data/catalog'))return {ok:true,json:async()=>catalog};
 if(s.startsWith('data/subjects/')) {const code=s.split('/').pop().split('?')[0].replace('.json','');return {ok:true,json:async()=>({code,name:catalog.subjects[code]?.name,units:[{no:1,title:{en:'Preserved study notes'}}],available_units:[1]})};}
 if(s.startsWith('https://api.github.com/'))return {ok:true,json:async()=>tree};
 if(s.startsWith('https://sunilpa4.github.io/diplomaone-content/papers/')) {
  const rel=s.split('/papers/')[1].split('?')[0];assert(!rel.includes('..'));return {ok:true,text:async()=>fs.readFileSync(path.join(staged,rel),'utf8')};
 }
 throw Error('Unexpected request '+s);
};
w.eval(fs.readFileSync(process.argv[2]||path.join(__dirname,'app.js'),'utf8'));
const wait=async fn=>{for(let i=0;i<150;i++){if(fn())return;await new Promise(r=>setTimeout(r,10));}throw Error('Render timed out: '+w.document.querySelector('#main').textContent.slice(0,200));};
async function go(hash,selector){const before=w.document.querySelector('.page-title');w.location.hash=hash;await wait(()=>w.document.querySelector('.page-title')!==before&&w.document.querySelector(selector));}
const linked=()=>[...w.document.querySelectorAll('#paper-results a[href^="#/paper/"]')].map(a=>a.getAttribute('href'));
(async()=>{
 await wait(()=>w.document.querySelector('[data-paper-subject="DI03000161"]'));
 assert.equal(w.document.querySelectorAll('.paper-subject-group').length,6);
 for(const code of codes) {
  const group=w.document.querySelector(`[data-paper-subject="${code}"]`);assert(group,'subject missing from Mechanical semester 3: '+code);
  assert(group.querySelector(`a[href="#/paper/${code}/summer-2026"]`));
  assert.equal(group.querySelectorAll('a[href^="#/paper/"]').length,newCodes.includes(code)?2:1,'all supplied sessions grouped together');
  assert.equal(!!group.querySelector(`a[href="#/paper/${code}/winter-2025"]`),newCodes.includes(code),'never invent an unsupplied Winter session');
  assert.equal(!!group.querySelector('.paper-coverage-note'),!newCodes.includes(code),'single-session coverage is explained, not silently hidden');
 }
 assert(!w.document.querySelector('a[href*="/paper/DI03005011/"]'),'Chemical paper must not leak into Mechanical');
 await go('#/subject/DI03000161','a[href="#/paper/DI03000161/winter-2025"]');
 assert(w.document.querySelector('a[href="#/paper/DI03000161/summer-2026"]'));
 assert(w.document.querySelector('a[href="#/unit/DI03000161/1"]'),'existing note link preserved');
 await go('#/paper/DI03000161/winter-2025','.solved-paper details.card');
 assert.equal(w.document.querySelectorAll('details.card').length,28);
 assert(w.document.querySelector('.solved-paper').textContent.includes('original Winter 2025 question PDF was not found'));
 assert(!w.document.querySelector('.paper-downloads a'),'do not link a legacy Summer original to the new Winter exam');
 await go('#/paper/DI03000161/summer-2026','.solved-paper details.card');
 assert(w.document.querySelector('.paper-downloads a[href$="/DI03000161/summer-2026.pdf"]'));
 assert(w.document.querySelector('.solved-paper').textContent.includes('Q1(a) and Q1(b) are common parts, shown once'));
 assert.equal(w.document.querySelectorAll('details.card').length,28,'do not duplicate common Q1 parts');
 const answerText=()=>{const copy=w.document.querySelector('details.card .answer').cloneNode(true);copy.querySelectorAll('button').forEach(b=>b.remove());return copy.textContent;};
 const answer=answerText();
 const before=w.document.querySelector('.page-title');w.document.querySelector('#lang-toggle').click();
 await wait(()=>w.document.querySelector('.page-title')!==before&&w.document.querySelector('details.card .answer'));
 assert(w.document.querySelector('.solved-paper').textContent.includes('English only'));
 assert.equal(answerText(),answer,'no fabricated Gujarati translation');
 const beforeEnglish=w.document.querySelector('.page-title');w.document.querySelector('#lang-toggle').click();await wait(()=>w.document.querySelector('.page-title')!==beforeEnglish&&w.document.querySelector('details.card'));
 await go('#/papers/mechanical/3','#paper-results');
 const branch=w.document.querySelector('#paper-branch-filter'),semester=w.document.querySelector('#paper-semester-filter'),search=w.document.querySelector('#paper-search-input');
 assert.equal(branch.value,'mechanical');assert.equal(semester.value,'3');assert.equal(linked().length,10);
 assert.equal(w.document.querySelectorAll('#paper-results .paper-subject-group').length,6);
 assert(w.document.querySelector('#paper-result-count').textContent.includes('10 paper sets'));
 search.value='winter-2025';search.dispatchEvent(new w.Event('input'));assert.equal(linked().length,4);assert(linked().every(h=>h.endsWith('/winter-2025')));
 search.value='DI03000161';search.dispatchEvent(new w.Event('input'));assert.equal(linked().length,2);assert(linked().every(h=>h.includes('/DI03000161/')));
 search.value='Thermodynamics';search.dispatchEvent(new w.Event('input'));assert.equal(linked().length,2);
 search.value='not-a-subject';search.dispatchEvent(new w.Event('input'));assert.equal(linked().length,0);assert(w.document.querySelector('.empty-state').textContent.includes('No matching papers'));
 search.value='';search.dispatchEvent(new w.Event('input'));assert.equal(linked().length,10);
 branch.value='chemical';branch.dispatchEvent(new w.Event('change'));assert(linked().length>0);assert(!linked().some(h=>codes.some(c=>h.includes('/'+c+'/'))));
 branch.value='mechanical';semester.value='5';semester.dispatchEvent(new w.Event('change'));
 assert(w.document.querySelector('[data-paper-subject="DI05019011"] a[href="#/paper/4351902/summer-2026"]'));
 assert(w.document.querySelector('a[href="#/paper/4351902/summer-2026"]').textContent.includes('Older scheme'));
 await go('#/branch/mechanical','a[href="#/papers/mechanical"]');
 assert(w.document.querySelector('a[href="#/branch/mechanical/3"]').textContent.includes('10 paper sets'));
 assert.equal(requests.filter(s=>s.startsWith('https://api.github.com/')).length,1,'no polling/repeated Drive scans added');
 assert.equal(w.document.querySelectorAll('iframe').length,0);
 w.close();console.log('Mechanical listing: all six Semester 3 subjects, ten real sessions, per-subject grouping, branch/semester/search filters, legacy placement and correct original-PDF links passed.');
})().catch(e=>{console.error(e);w.close();process.exitCode=1;});
