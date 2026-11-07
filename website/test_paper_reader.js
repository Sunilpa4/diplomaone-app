// Exercise the real in-site paper renderer using a browser-like DOM.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const appPath = process.argv[2] || path.join(__dirname, 'app.js');
let source = fs.readFileSync(appPath, 'utf8');
const hook = '  updateHeader();render();\n})();';
assert.equal(source.split(hook).length, 2);
source = source.replace(hook, '  globalThis.testAPI = {sanitizePaper,showPaper,setLanguage(value){lang=value;}};\n})();');
const dom = new JSDOM('<!doctype html><html><body><main id="main"></main><span id="year"></span><button id="lang-toggle"></button><button id="menu-toggle"></button><div id="mobile-nav"></div><div id="toast"></div></body></html>', {url:'https://diplomaone.in/', runScripts:'outside-only'});
dom.window.eval(source);
const { sanitizePaper, showPaper, setLanguage } = dom.window.testAPI;
const sample = `<!doctype html><main><div class="note"><div class="en">English intro</div><div class="gu">ગુજરાતી માહિતી</div></div>
<section><h2>Question 1</h2><details class="card" onclick="window.attack=1"><summary><strong class="en">English question</strong><strong class="gu">ગુજરાતી પ્રશ્ન</strong></summary><div class="answer"><div class="en"><p>Safe <span class="frac"><span class="num">a</span><span class="den">b</span></span></p><figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" onload="window.attack=2"><script>window.attack=3</script><foreignObject><div>bad</div></foreignObject><line x1="1" y1="2" x2="3" y2="4" stroke="red" marker-end="url(https://attacker.test/x)"/></svg><figcaption>Caption</figcaption></figure><img src="https://attacker.test/x" onerror="window.attack=4"><img src="data:image/png;base64,YQ==" alt="Original figure"></div><div class="gu"><p>ગુજરાતી જવાબ</p></div></div></details></section><script>window.attack=5</script></main>`;
for (const [language,expected,hidden] of [['en','English question','ગુજરાતી પ્રશ્ન'],['gu','ગુજરાતી પ્રશ્ન','English question']]) {
  const result = sanitizePaper(sample,language);
  const rendered = new JSDOM(result).window.document;
  assert(result.includes(expected)); assert(!result.includes(hidden));
  assert.equal(rendered.querySelectorAll('details.card').length,1);
  assert.equal(rendered.querySelectorAll('.frac .num').length,language==='en'?1:0);
  assert(!result.includes('onclick')); assert(!result.includes('onerror')); assert(!result.includes('<script'));
  assert(!result.includes('https://attacker.test')); assert(!result.includes('foreignObject'));
  if(language==='en') {
    const image=rendered.querySelector('figure img');assert(image && image.src.startsWith('data:image/svg+xml;charset=utf-8,'));
    const svg=decodeURIComponent(image.getAttribute('src').split(',')[1]);
    assert(svg.includes('<line'));assert(!svg.includes('onload'));assert(!svg.includes('marker-end'));assert(!svg.includes('<script'));
    assert(rendered.querySelector('img[alt="Original figure"]'));
  }
}
assert.throws(()=>sanitizePaper('<main>missing details</main>','en'),/Invalid paper format/);
(async()=>{
 let calls=0;
 dom.window.fetch=async(url,options)=>{calls++; assert(url.startsWith('https://sunilpa4.github.io/diplomaone-content/papers/DI03000141/summer-2026.html?'));assert.equal(options.redirect,'error');return {ok:true,text:async()=>sample}};
 const entry={session:'summer-2026',pdf:'Question_Paper.pdf'};
 setLanguage('en');const first=await showPaper('DI03000141','summer-2026',{name:{en:'Machines'}},entry);
 setLanguage('gu');const second=await showPaper('DI03000141','summer-2026',{name:{en:'Machines'}},entry);
 assert(first.includes('English question'));assert(second.includes('ગુજરાતી પ્રશ્ન'));assert.equal(calls,1,'language change should use cached source');
 assert(first.includes('Question_Paper.pdf'));assert(first.includes('rel="noopener noreferrer"'));
 console.log('In-site paper rendering, bilingual content, fractions, diagrams and unsafe markup checks passed.');
})().catch(e=>{console.error(e);process.exitCode=1});
