// Test route, unlisted subject, new session, validation and failure recovery.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const dom = new JSDOM(fs.readFileSync(path.join(__dirname,'index.html'),'utf8'), {url:'https://diplomaone.in/#/papers',runScripts:'outside-only'});
const w=dom.window, requests=[];
w.scrollTo=()=>{};
const file=(path,mode='100644')=>({path,mode,type:'blob'});
const tree={truncated:false,tree:[
 file('papers/DI05019011/winter-2027.html'), file('papers/DI05019011/winter-2027.pdf'),
 file('papers/DI05019011/summer-2026.html'), file('papers/DI05019011/Question_Paper.pdf'),
 file('papers/4351902/summer-2026.html'), file('papers/4351902/summer-2026.pdf'),
 file('papers/4351903/summer-2026.html'), file('papers/4351903/summer-2026.pdf'),
 file('papers/4350501/winter-2025.solution.pdf'), file('papers/4350501/winter-2025.pdf'),
 file('papers/4350501/summer-2026.solution.pdf'), file('papers/4350501/summer-2026.pdf'),
 file('papers/4360501/winter-2025.solution.pdf'), file('papers/4360501/winter-2025.pdf'),
 file('papers/4360501/summer-2026.solution.pdf'), file('papers/4360501/summer-2026.pdf'),
 file('papers/DI03006011/winter-2025.solution.pdf'), file('papers/DI03006011/winter-2025.pdf'),
 file('papers/DI03006021/winter-2025.solution.pdf'), file('papers/DI03006021/winter-2025.pdf'),
 file('papers/DI03006031/summer-2026.solution.pdf'), file('papers/DI03006031/summer-2026.pdf'),
 file('papers/DI03006031/winter-2025.solution.pdf'), file('papers/DI03006031/winter-2025.pdf'),
 file('papers/DI03006041/summer-2026.solution.pdf'), file('papers/DI03006041/summer-2026.pdf'),
 file('papers/DI03006041/winter-2025.solution.pdf'), file('papers/DI03006041/winter-2025.pdf'),
 file('papers/DI03006051/summer-2026.solution.pdf'), file('papers/DI03006051/summer-2026.pdf'),
 file('papers/DI03006051/winter-2025.solution.pdf'), file('papers/DI03006051/winter-2025.pdf'),
 file('papers/DI01006021/summer-2026.solution.pdf'), file('papers/DI01006021/summer-2026.pdf'),
 file('papers/DI01006021/winter-2025.solution.pdf'), file('papers/DI01006021/winter-2025.pdf'),
 file('papers/DI01000021/summer-2026.solution.pdf'), file('papers/DI01000021/summer-2026.pdf'),
 file('papers/DI01000021/winter-2025.solution.pdf'), file('papers/DI01000021/winter-2025.pdf'),
 file('papers/DI01000121/summer-2026.solution.pdf'), file('papers/DI01000121/summer-2026.pdf'),
 file('papers/DI01000121/winter-2025.solution.pdf'), file('papers/DI01000121/winter-2025.pdf'),
 file('papers/DI09999999/winter-2027.html'), file('papers/DI09999999/evil.pdf'),
 file('papers/DI09999999/spring-2028.html','120000'), file('papers/DI09999999/../../danger.html'),
 file('papers/../../bad/winter-2027.html'), file('papers/DI09999999/index.html')
]};
// Converted HTML is the default even while its optional solution PDF remains.
for(const item of [...tree.tree])if(item.path.endsWith('.solution.pdf'))tree.tree.push(file(item.path.replace('.solution.pdf','.html')));
tree.tree.push(file('papers/DI09999998/winter-2025.solution.pdf'),file('papers/DI09999998/winter-2025.pdf'),file('papers/DI01000021/summer-2026.assets/0001.webp'),file('papers/DI01000021/summer-2026.assets/evil.html'));
const catalog={branches:[{key:'civil',code:'06',name:{en:'Civil Engineering',gu:'Civil Engineering'},semesters:{'1':['DI01000021','DI01000121','DI01006021'],'3':['DI03006011','DI03006021','DI03006031','DI03006041','DI03006051']}},{key:'chemical',code:'05',name:{en:'Chemical Engineering',gu:'Chemical Engineering'},semesters:{'5':['DI05005011','DI05005031']}},{key:'mechanical',code:'01',name:{en:'Mechanical Engineering',gu:'Mechanical Engineering'},semesters:{'1':['DI01000021'],'2':['DI01000121'],'5':['DI05019011','DI05019021']}}],subjects:{DI05019011:{code:'DI05019011',name:{en:'Manufacturing Engineering - III',gu:'મેન્યુફેક્ચરિંગ ઇજનેરી - III'},status:'available'},DI05019021:{code:'DI05019021',name:{en:'Thermal Engineering - II',gu:'થર્મલ ઇજનેરી - II'},status:'available'},DI05005011:{code:'DI05005011',name:{en:'Mass Transfer - II'},status:'available'},DI05005031:{code:'DI05005031',name:{en:'Chemical Reaction Engineering'},status:'available'},DI01000021:{code:'DI01000021',name:{en:'Mathematics - I'},status:'unavailable'},DI01000121:{code:'DI01000121',name:{en:'Applied Physics'},status:'unavailable'},DI01006021:{code:'DI01006021',name:{en:'Construction Material'},status:'available'},DI03006011:{code:'DI03006011',name:{en:'Construction Technology'},status:'available'},DI03006021:{code:'DI03006021',name:{en:'Advance Surveying'},status:'available'},DI03006031:{code:'DI03006031',name:{en:'Basic Transportation Engineering'},status:'available'},DI03006041:{code:'DI03006041',name:{en:'Mechanics of Structures-I'},status:'available'},DI03006051:{code:'DI03006051',name:{en:'Soil Engineering'},status:'available'}}};
let failIndex=false;
w.fetch=async url=>{
  requests.push(String(url));
  if(String(url).startsWith('data/catalog'))return {ok:true,json:async()=>catalog};
  if(String(url).startsWith('data/subjects/')){const code=String(url).split('/').pop().split('?')[0].replace('.json','');return {ok:true,json:async()=>({code,name:catalog.subjects[code]?.name,units:[],available_units:[]})};}
  if(String(url).startsWith('https://api.github.com/'))return failIndex?{ok:false}:{ok:true,json:async()=>tree};
  if(String(url).includes('/papers/'))return {ok:true,text:async()=>'<main><section><details class="card"><summary>New question</summary><div class="answer">New answer</div></details></section></main>'};
  throw Error('Unexpected request '+url);
};
w.eval(fs.readFileSync(path.join(__dirname,'app.js'),'utf8'));
const waitFor=async(fn)=>{for(let i=0;i<100;i++){if(fn())return;await new Promise(r=>setTimeout(r,10));}throw Error('Timed out waiting for render: '+w.document.querySelector('#main').textContent.slice(0,100));};
async function go(hash,selector){const previous=w.document.querySelector('.page-title');w.location.hash=hash;await waitFor(()=>w.document.querySelector('.page-title')!==previous && !!w.document.querySelector(selector));}
(async()=>{
 await waitFor(()=>!!w.document.querySelector('a[href="#/paper/DI05019011/winter-2027"]'));
 assert(w.document.querySelector('a[href="#/paper/DI09999999/winter-2027"]'));
 assert(w.document.querySelector('a[href="#/paper/4351902/summer-2026"]').textContent.includes('Manufacturing Engineering'));
 assert(w.document.querySelector('a[href="#/paper/4350501/winter-2025"]').textContent.includes('Mass Transfer'));
 assert(w.document.querySelector('a[href="#/paper/DI03006041/summer-2026"]').textContent.includes('Mechanics of Structures'));
 assert(w.document.querySelector('a[href="#/paper/DI01000021/summer-2026"]').textContent.includes('Mathematics - I'));
 assert(w.document.querySelector('a[href="#/paper/DI01000021/winter-2025"]').textContent.includes('Mathematics - I'));
 assert(w.document.querySelector('a[href="#/paper/DI01000121/summer-2026"]').textContent.includes('Applied Physics'));
 assert(w.document.querySelector('a[href="#/paper/DI01000121/winter-2025"]').textContent.includes('Applied Physics'));
 await go('#/paper/DI01000021/summer-2026','.solved-paper details');
 assert(w.document.querySelector('.paper-toolbar a[href$="summer-2026.pdf"]'));
 assert(w.document.querySelector('.paper-toolbar a[href$="summer-2026.solution.pdf"]'));
 assert(w.document.querySelector('.solved-paper').textContent.includes('New answer'));
 assert.equal(w.document.querySelectorAll('iframe').length,0,'never use a PDF viewer as a question card');
 assert(requests.some(x=>x.includes('/DI01000021/summer-2026.html')));
 w.document.querySelector('[data-paper-expand="true"]').click();assert(w.document.querySelector('details.card').open);
 w.document.querySelector('[data-paper-expand="false"]').click();assert(!w.document.querySelector('details.card').open);
 await go('#/paper/DI01000121/winter-2025','.solved-paper details');
 assert(w.document.querySelector('.paper-toolbar a[href$="winter-2025.pdf"]'));
 assert(w.document.querySelector('.paper-toolbar a[href$="winter-2025.solution.pdf"]'));
 assert(w.document.querySelector('.solved-paper').textContent.includes('New answer'));
 assert.equal(w.document.querySelectorAll('iframe').length,0);
 await go('#/paper/4350501/winter-2025','[data-paid-paper]');
 assert(!w.document.querySelector('.solved-paper'));
 assert(!w.document.querySelector('a[href$="winter-2025.pdf"]'));
 assert(!requests.some(x=>x.includes('/4350501/winter-2025.html')), 'legacy paid answers cannot fall back to public HTML');
 await go('#/paper/DI09999998/winter-2025','[data-paid-paper]');
 assert(!w.document.querySelector('.solved-paper'));
 assert(!w.document.querySelector('a[href$="winter-2025.solution.pdf"]'));
 assert(!requests.some(x=>x.includes('/DI09999998/winter-2025.html')), 'an unconverted paid PDF cannot bypass the lock');
 assert.equal(w.document.querySelectorAll('iframe,object,embed').length,0);
 await go('#/branch/civil','a[href="#/branch/civil/3"]');
 assert(w.document.querySelector('a[href="#/branch/civil/3"]').textContent.includes('8 paper sets'));
 await go('#/branch/civil/3','a[href="#/paper/DI03006041/summer-2026"]');
 assert(w.document.querySelector('a[href="#/paper/DI03006041/summer-2026"]').textContent.includes('Mechanics of Structures'));
 await go('#/subject/DI03006041','a[href="#/paper/DI03006041/summer-2026"]');
 assert(w.document.querySelector('.section-heading h2').textContent.includes('Solved papers'));
 await go('#/branch/civil/1','a[href="#/paper/DI01006021/summer-2026"]');
 await go('#/subject/DI01006021','a[href="#/paper/DI01006021/summer-2026"]');
 assert(w.document.querySelector('a[href="#/paper/DI01006021/summer-2026"]').textContent.includes('Construction Material'));
 await go('#/branch/chemical','a[href="#/branch/chemical/5"]');
 assert(w.document.querySelector('a[href="#/branch/chemical/5"]').textContent.includes('4 paper sets'));
 await go('#/branch/chemical/5','a[href="#/paper/4360501/summer-2026"]');
 assert(w.document.querySelector('a[href="#/paper/4350501/winter-2025"]').textContent.includes('Mass Transfer'));
 assert(w.document.querySelector('a[href="#/paper/4360501/summer-2026"]').textContent.includes('Chemical Reaction Engineering'));
 await go('#/subject/DI05005011','a[href="#/paper/4350501/summer-2026"]');
 await go('#/subject/DI05005031','a[href="#/paper/4360501/summer-2026"]');
 await go('#/branch/mechanical','a[href="#/branch/mechanical/5"]');
 assert(w.document.querySelector('a[href="#/branch/mechanical/5"]').textContent.includes('4 paper sets'));
 await go('#/branch/mechanical/5','a[href="#/paper/4351902/summer-2026"]');
 assert(w.document.querySelector('a[href="#/paper/4351902/summer-2026"]').textContent.includes('Manufacturing Engineering'));
 await go('#/branch/mechanical/1','a[href="#/paper/DI01000021/summer-2026"]');
 assert(w.document.querySelector('a[href="#/paper/DI01000021/summer-2026"]').textContent.includes('Mathematics - I'));
 await go('#/papers','a[href="#/paper/4351902/summer-2026"]');
 assert(!w.document.body.innerHTML.includes('../../danger'));
 assert(!w.document.querySelector('a[href*=spring-2028]')); // symlink is not a paper
 await go('#/subject/DI05019011','a[href="#/paper/DI05019011/summer-2026"]'); // even without notes
 assert(w.document.querySelector('a[href="#/paper/4351902/summer-2026"]'));
 assert(!w.document.querySelector('a[href="#/paper/4351903/summer-2026"]'));
 assert(w.document.querySelector('a[href="#/paper/4351902/summer-2026"]').textContent.includes('Older scheme'));
 await go('#/paper/DI05019011/winter-2027','[data-paid-paper]');
 assert(!w.document.querySelector('a[href$="winter-2027.pdf"]'));assert(!w.document.querySelector('.solved-paper'));
 await go('#/paper/4351902/summer-2026','[data-paid-paper]');
 assert(w.document.querySelector('.page-subtitle').textContent.includes('4351902'));
 assert(w.document.querySelector('.reader-notice').textContent.includes('older-scheme paper (code 4351902)'));
 assert(w.document.querySelector('a[href="#/subject/DI05019011"]'));
 assert(!w.document.querySelector('a[href$="summer-2026.pdf"]'));
 await go('#/subject/DI05019021','a[href="#/paper/4351903/summer-2026"]');
 assert(!w.document.querySelector('a[href="#/paper/4351902/summer-2026"]'));
 await go('#/paper/4351903/summer-2026','[data-paid-paper]');
 assert(w.document.querySelector('.page-subtitle').textContent.includes('4351903'));
 assert(w.document.querySelector('a[href="#/subject/DI05019021"]'));
 assert(w.document.querySelector('.reader-notice').textContent.includes('older-scheme paper (code 4351903)'));
 await go('#/paper/DI09999999/winter-2027','[data-paid-paper]');
 assert(w.document.querySelector('.page-subtitle').textContent.includes('DI09999999'));
 assert(!w.document.querySelector('a[href$="evil.pdf"]'));
 assert(!w.document.querySelector('.paper-toolbar a[target="_blank"]'));
 const calls=requests.filter(x=>x.includes('/papers/')&&!x.includes('index.json'));
 assert.equal(requests.filter(x=>x.startsWith('https://api.github.com/')).length,1,'no polling or repeated requests within a tab');
 assert(calls.every(x=>/^https:\/\/sunilpa4\.github\.io\/diplomaone-content\/papers\/(?:DI\d{8}|\d{7})\/[a-z]+-\d{4}\.html\?/.test(x)));
 // A newly committed filename is discovered on a fresh page without any index update.
 tree.tree.push(file('papers/DI05019011/summer-2029.html'));
 const fresh=new JSDOM(fs.readFileSync(path.join(__dirname,'index.html'),'utf8'),{url:'https://diplomaone.in/#/papers',runScripts:'outside-only'}).window;
 fresh.scrollTo=()=>{};fresh.fetch=w.fetch;
 fresh.eval(fs.readFileSync(path.join(__dirname,'app.js'),'utf8'));
 for(let i=0;i<100&&!fresh.document.querySelector('a[href="#/paper/DI05019011/summer-2029"]');i++)await new Promise(r=>setTimeout(r,10));
 assert(fresh.document.querySelector('a[href="#/paper/DI05019011/summer-2029"]'));
 fresh.close();
 // A failed GitHub request must not hide notes or pretend discovery succeeded.
 failIndex=true;
 const w2=new JSDOM(fs.readFileSync(path.join(__dirname,'index.html'),'utf8'),{url:'https://diplomaone.in/#/papers',runScripts:'outside-only'}).window;
 w2.scrollTo=()=>{};w2.console={...console,error:()=>{}};w2.fetch=w.fetch;
 w2.eval(fs.readFileSync(path.join(__dirname,'app.js'),'utf8'));
 for(let i=0;i<100&&!w2.document.querySelector('.reader-notice');i++)await new Promise(r=>setTimeout(r,10));
 assert(w2.document.querySelector('.reader-notice').textContent.includes('could not be updated'));
 assert(w2.document.querySelector('a[href="#/paper/DI03000141/summer-2026"]'));
 w2.close();
 console.log('Automatic listing/catalog placement, free question controls and locked paid legacy/unknown/PDF-only papers passed.');
 w.close();
})().catch(e=>{console.error(e);w.close();process.exitCode=1});
