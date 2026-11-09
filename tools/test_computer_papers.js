// Exercise the real website sanitizer against each paper and source language.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const root=path.resolve(__dirname,'..');
const codes=['DI01000131','DI01000151','DI02000101','DI03000011','DI03000021','DI03000031','DI03000041','DI03000051','DI04000011','DI04000021'];
const shell=new JSDOM('<main id="main"></main><span id="year"></span><button id="lang-toggle"></button><button id="menu-toggle"></button><div id="mobile-nav"></div><div id="toast"></div>',{url:'https://diplomaone.in/',runScripts:'outside-only'});
const app=fs.readFileSync(path.join(root,'website/app.js'),'utf8'),hook='  updateHeader();render();\n})();';
assert.equal(app.split(hook).length,2);
shell.window.eval(app.replace(hook,'  globalThis.testAPI={sanitizePaper,validPaperCode};\n})();'));
const normalize=s=>s.replace(/\s+/g,' ').trim();
for(const code of codes) {
  assert(shell.window.testAPI.validPaperCode(code));
  const src=fs.readFileSync(path.join(root,'papers-upload/papers',code,'summer-2026.html'),'utf8');
  for(const lang of ['en','gu']) {
    const language=code==='DI01000151'&&lang==='gu'?'gujarati':'english';
    const original=new JSDOM(fs.readFileSync(path.join(root,'papers-upload/originals',code,language+'.html'),'utf8')).window.document;
    const safe=new JSDOM(shell.window.testAPI.sanitizePaper(src,lang)).window.document;
    assert.equal(safe.querySelectorAll('section').length,5,`${code} ${lang}`);
    const diagramCount=original.querySelectorAll('main figure svg').length;
    original.querySelectorAll('main svg').forEach(svg=>svg.remove()); // diagram text is now in the inert image
    const questions=[...safe.querySelectorAll('details')], expected=[...original.querySelectorAll('main details')];
    assert.equal(questions.length,28,`${code} ${lang}`);
    questions.forEach((d,i)=>assert.equal(normalize(d.textContent),normalize(expected[i].textContent),`${code} ${lang} question ${i+1} changed`));
    const imgs=[...safe.querySelectorAll('figure img')];
    assert.equal(imgs.length,diagramCount,`${code} ${lang} diagrams`);
    assert(imgs.every(img=>img.src.startsWith('data:image/png;base64,')));
    if(code!=='DI01000151')assert(safe.body.textContent.includes('English-only solution'));
    assert.equal(safe.querySelectorAll('script,iframe,object,embed').length,0);
  }
}
shell.window.close();
console.log('All ten papers preserve 28 answer texts and all diagrams in both website language modes.');
