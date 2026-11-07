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
 file('papers/DI09999999/winter-2027.html'), file('papers/DI09999999/evil.pdf'),
 file('papers/DI09999999/spring-2028.html','120000'), file('papers/DI09999999/../../danger.html'),
 file('papers/../../bad/winter-2027.html'), file('papers/DI09999999/index.html')
]};
const catalog={branches:[],subjects:{DI05019011:{code:'DI05019011',name:{en:'Future subject'},status:'unavailable'}}};
let failIndex=false;
w.fetch=async url=>{
  requests.push(String(url));
  if(String(url).startsWith('data/catalog'))return {ok:true,json:async()=>catalog};
  if(String(url).startsWith('https://api.github.com/'))return failIndex?{ok:false}:{ok:true,json:async()=>tree};
  if(String(url).includes('/papers/'))return {ok:true,text:async()=>'<main><section><details class="card"><summary>New question</summary><div class="answer">New answer</div></details></section></main>'};
  throw Error('Unexpected request '+url);
};
w.eval(fs.readFileSync(path.join(__dirname,'app.js'),'utf8'));
const waitFor=async(fn)=>{for(let i=0;i<100;i++){if(fn())return;await new Promise(r=>setTimeout(r,10));}throw Error('Timed out waiting for render: '+w.document.querySelector('#main').textContent.slice(0,100));};
async function go(hash,selector){w.location.hash=hash;await waitFor(()=>!!w.document.querySelector(selector));}
(async()=>{
 await waitFor(()=>!!w.document.querySelector('a[href="#/paper/DI05019011/winter-2027"]'));
 assert(w.document.querySelector('a[href="#/paper/DI09999999/winter-2027"]'));
 assert(w.document.querySelector('a[href="#/paper/4351902/summer-2026"]').textContent.includes('Manufacturing Engineering'));
 assert(!w.document.body.innerHTML.includes('../../danger'));
 assert(!w.document.querySelector('a[href*=spring-2028]')); // symlink is not a paper
 await go('#/subject/DI05019011','a[href="#/paper/DI05019011/summer-2026"]'); // even without notes
 await go('#/paper/DI05019011/winter-2027','.solved-paper details');
 assert(w.document.querySelector('a[href$="winter-2027.pdf"]'));
 assert(w.document.querySelector('.solved-paper').textContent.includes('New answer'));
 await go('#/paper/4351902/summer-2026','.solved-paper details');
 await waitFor(()=>w.document.querySelector('.page-subtitle').textContent.includes('4351902'));
 assert(w.document.querySelector('a[href$="summer-2026.pdf"]'));
 await go('#/paper/DI09999999/winter-2027','.solved-paper details');
 await waitFor(()=>w.document.querySelector('.page-subtitle').textContent.includes('DI09999999'));
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
 console.log('Automatic listing, new exams, unknown subjects, optional PDFs, route safety and fallback passed.');
 w.close();
})().catch(e=>{console.error(e);w.close();process.exitCode=1});
