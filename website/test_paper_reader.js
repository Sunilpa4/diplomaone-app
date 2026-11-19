// Exercise the real in-site paper renderer using a browser-like DOM.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const appPath = process.argv[2] || path.join(__dirname, 'app.js');
let source = fs.readFileSync(appPath, 'utf8');
const hook = '  updateHeader();render();\n})();';
assert.equal(source.split(hook).length, 2);
source = source.replace(hook, '  globalThis.testAPI = {sanitizePaper,showPaper,bindPaperReader,paperAssetUrl,setLanguage(value){lang=value;}};\n})();');
const dom = new JSDOM('<!doctype html><html><body><main id="main"></main><span id="year"></span><button id="lang-toggle"></button><button id="menu-toggle"></button><div id="mobile-nav"></div><div id="toast"></div></body></html>', {url:'https://diplomaone.in/', runScripts:'outside-only'});
dom.window.eval(source);
const { sanitizePaper, showPaper, bindPaperReader, paperAssetUrl, setLanguage } = dom.window.testAPI;
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
const context={code:'DI01000021',session:'summer-2026'};
const imagePaper=src=>`<main><section><details open onclick="bad()"><summary>Formula question</summary><div class="answer"><figure class="paper-excerpt"><img src="${src}" alt="Source fraction" onerror="bad()" srcset="https://attacker.test/x 2x" style="display:none" width="986" height="140"><figcaption>Source page 2</figcaption></figure></div></details></section></main>`;
for(const extension of ['png','webp']){
 const relative=`summer-2026.assets/0001.${extension}`;
 const safe=sanitizePaper(imagePaper(relative),'en',context);
 const doc=new dom.window.DOMParser().parseFromString(safe,'text/html');
 const img=doc.querySelector('img');assert(img);
 assert.equal(img.src,`https://sunilpa4.github.io/diplomaone-content/papers/DI01000021/${relative}`);
 assert.equal(img.getAttribute('width'),'986');assert(!img.hasAttribute('srcset'));assert(!img.hasAttribute('onerror'));assert(!img.hasAttribute('style'));
 assert.equal(doc.querySelectorAll('main').length,0,'do not nest main landmarks');
 assert.equal(doc.querySelector('details').open,false,'question cards start collapsed');
 assert.equal(sanitizePaper(imagePaper(relative),'en').includes('<img'),false,'context is mandatory for external assets');
}
for(const src of ['../summer-2026.assets/0001.webp','winter-2025.assets/0001.webp','/summer-2026.assets/0001.webp','https://sunilpa4.github.io/diplomaone-content/papers/DI01000021/summer-2026.assets/0001.webp','//attacker.test/x','summer-2026.assets/0001.svg','summer-2026.assets/0001.webp?x=1','summer-2026.assets/%30%30%30%31.webp','summer-2026.assets/0001.webp#x','summer-2026.assets/../../x.png','summer-2026.assets\\\\0001.webp','data:image/svg+xml;base64,YQ==']){
 assert(!sanitizePaper(imagePaper(src),'en',context).includes('<img'),src);
}
assert.equal(paperAssetUrl('summer-2026.assets/0001.webp',{code:'../DI01000021',session:'summer-2026'}),'');
assert.equal(paperAssetUrl('summer-2026.assets/0001.webp',{code:'DI01000021',session:'../summer-2026'}),'');
(async()=>{
 let calls=0;
 dom.window.fetch=async(url,options)=>{calls++; assert(url.startsWith('https://sunilpa4.github.io/diplomaone-content/papers/DI03000141/summer-2026.html?'));assert.equal(options.redirect,'error');return {ok:true,text:async()=>sample}};
 const entry={session:'summer-2026',pdf:'Question_Paper.pdf'};
 setLanguage('en');const first=await showPaper('DI03000141','summer-2026',{name:{en:'Machines'}},entry);
 setLanguage('gu');const second=await showPaper('DI03000141','summer-2026',{name:{en:'Machines'}},entry);
 assert(first.includes('English question'));assert(second.includes('ગુજરાતી પ્રશ્ન'));assert.equal(calls,1,'language change should use cached source');
 assert(first.includes('Question_Paper.pdf'));assert(first.includes('rel="noopener noreferrer"'));
 assert(!first.includes('<iframe'));assert(first.includes('1 question part'));
 setLanguage('en');
 dom.window.document.querySelector('#main').innerHTML=first;bindPaperReader();
 const main=dom.window.document.querySelector('#main'),card=main.querySelector('details.card');
 assert(!card.open);
 main.querySelector('[data-paper-expand="true"]').click();assert(card.open);
 main.querySelector('[data-paper-expand="false"]').click();assert(!card.open);
 const enlarge=main.querySelector('.paper-enlarge');assert(enlarge);enlarge.click();
 const dialog=main.querySelector('dialog');assert(dialog.open);
 assert(dialog.querySelector('img').src.startsWith('data:image/'));
 const zoom=dialog.querySelector('.paper-control');zoom.click();assert(dialog.classList.contains('at-original-size'));zoom.click();assert(!dialog.classList.contains('at-original-size'));
 dialog.querySelectorAll('.paper-control')[1].click();assert(!dialog.open);
 assert.equal(dom.window.document.activeElement,enlarge,'return focus after closing image');
 const fallback=await showPaper('DI01000121','winter-2025',null,{pdfOnly:true,pdf:'winter-2025.pdf',solutionPdf:'winter-2025.solution.pdf'});
 assert.equal(calls,1,'PDF-only fallback does not request non-existent HTML');
 assert(fallback.includes('cards have not yet been prepared'));assert(fallback.includes('Optional solution PDF'));assert(!fallback.includes('<iframe'));
 await assert.rejects(()=>showPaper('../x','summer-2026',null,{}),/Invalid paper path/);
 assert.equal(calls,1);
 console.log('Question cards, scoped assets, image enlargement, language caching, fractions and unsafe markup checks passed.');
})().catch(e=>{console.error(e);process.exitCode=1});
