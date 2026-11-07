// Test route, unlisted subject, new session, validation and failure recovery.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const dom = new JSDOM(fs.readFileSync(path.join(__dirname,'index.html'),'utf8'), {url:'https://diplomaone.in/#/papers',runScripts:'outside-only'});
const w=dom.window, requests=[];
w.scrollTo=()=>{};
const index={version:1,subjects:{DI05019011:[{session:'winter-2027',pdf:'winter-2027.pdf'},{session:'summer-2026',pdf:null},{session:'../../danger',pdf:'x'}],DI09999999:[{session:'winter-2027',pdf:'https://bad.test/evil.pdf'}],'../../bad':[{session:'winter-2027'}]}};
const catalog={branches:[],subjects:{DI05019011:{code:'DI05019011',name:{en:'Future subject'},status:'unavailable'}}};
let failIndex=false;
w.fetch=async url=>{
  requests.push(String(url));
  if(String(url).startsWith('data/catalog'))return {ok:true,json:async()=>catalog};
  if(String(url).includes('/papers/index.json'))return failIndex?{ok:false}:{ok:true,json:async()=>index};
  if(String(url).includes('/papers/'))return {ok:true,text:async()=>'<main><section><details class="card"><summary>New question</summary><div class="answer">New answer</div></details></section></main>'};
  throw Error('Unexpected request '+url);
};
w.eval(fs.readFileSync(path.join(__dirname,'app.js'),'utf8'));
const waitFor=async(fn)=>{for(let i=0;i<100;i++){if(fn())return;await new Promise(r=>setTimeout(r,10));}throw Error('Timed out waiting for render: '+w.document.querySelector('#main').textContent.slice(0,100));};
async function go(hash,selector){w.location.hash=hash;await waitFor(()=>!!w.document.querySelector(selector));}
(async()=>{
 await waitFor(()=>!!w.document.querySelector('a[href="#/paper/DI05019011/winter-2027"]'));
 assert(w.document.querySelector('a[href="#/paper/DI09999999/winter-2027"]'));
 assert(!w.document.body.innerHTML.includes('../../danger'));
 await go('#/subject/DI05019011','a[href="#/paper/DI05019011/summer-2026"]'); // even without notes
 await go('#/paper/DI05019011/winter-2027','.solved-paper details');
 assert(w.document.querySelector('a[href$="winter-2027.pdf"]'));
 assert(w.document.querySelector('.solved-paper').textContent.includes('New answer'));
 await go('#/paper/DI09999999/winter-2027','.solved-paper details');
 await waitFor(()=>w.document.querySelector('.page-subtitle').textContent.includes('DI09999999'));
 assert(!w.document.querySelector('a[href$="evil.pdf"]'));
 assert(!w.document.querySelector('.paper-toolbar a[target="_blank"]'));
 const calls=requests.filter(x=>x.includes('/papers/')&&!x.includes('index.json'));
 assert(calls.every(x=>/^https:\/\/sunilpa4\.github\.io\/diplomaone-content\/papers\/DI\d{8}\/[a-z]+-\d{4}\.html\?/.test(x)));
 // A failed index must not hide notes or pretend that discovery succeeded.
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
