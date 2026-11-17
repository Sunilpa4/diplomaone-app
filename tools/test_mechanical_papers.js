const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{JSDOM}=require('jsdom');
const root=path.resolve(__dirname,'..');
const dom=new JSDOM('<main id="main"></main><span id="year"></span><button id="lang-toggle"></button><button id="menu-toggle"></button><div id="mobile-nav"></div><div id="toast"></div>',{url:'https://diplomaone.in/',runScripts:'outside-only'});
const app=fs.readFileSync(path.join(root,'website/app.js'),'utf8'),hook='  updateHeader();render();\n})();';assert.equal(app.split(hook).length,2);
dom.window.eval(app.replace(hook,'  globalThis.testAPI={sanitizePaper};\n})();'));
const norm=x=>x.replace(/\s+/g,' ').trim();
for(const code of ['DI01000181','DI01000191'])for(const season of ['winter','summer'])for(const lang of ['en','gu']){
 const src=new JSDOM(fs.readFileSync(path.join(root,'papers-upload/originals',code,'winter-summer-2025.html'),'utf8')).window.document;
 const article=src.querySelector('#paper-'+season);
 const expected=[...article.querySelectorAll('details')];
 const diagramCount=article.querySelectorAll('figure img').length;
 for(const e of article.querySelectorAll('.chevron,button,.'+(lang==='en'?'lang-gu-only':'lang-en-only')))e.remove();
 const html=fs.readFileSync(path.join(root,'papers-upload/papers',code,`${season}-2025.html`),'utf8');
 const safe=new JSDOM(dom.window.testAPI.sanitizePaper(html,lang)).window.document;
 const got=[...safe.querySelectorAll('details')];assert.equal(got.length,28);assert.equal(safe.querySelectorAll('section').length,5);
 got.forEach((q,i)=>assert.equal(norm(q.textContent),norm(expected[i].textContent),`${code} ${season} ${lang} question ${i+1}`));
 assert.equal(safe.querySelectorAll('figure img').length,diagramCount);
 assert([...safe.querySelectorAll('figure img')].every(e=>e.src.startsWith('data:image/png;base64,')));
 assert(safe.body.textContent.includes('original question PDF was not supplied')||safe.body.textContent.includes('Original question PDF was not supplied'));
 if(code==='DI01000191')assert(safe.body.textContent.includes('English-only'));
 if(code==='DI01000181'&&season==='winter')assert(safe.querySelector('.frac .num')&&safe.querySelector('.frac .den'),'fraction lost');
}
dom.window.close();console.log('2025 Mechanical text, translations, diagrams and fraction survive reader sanitization.');
