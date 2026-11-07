// Verify the uploaded papers remain readable through the website sanitizer.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.resolve(__dirname,'../papers-upload/papers');
const codes = ['4351902','4351903','DI01000181','DI01000191','DI04000241','DI04000251','DI04019011'];
const dom = new JSDOM('<main id="main"></main><span id="year"></span><button id="lang-toggle"></button><button id="menu-toggle"></button><div id="mobile-nav"></div><div id="toast"></div>',{url:'https://diplomaone.in/',runScripts:'outside-only'});
let app=fs.readFileSync(path.join(__dirname,'app.js'),'utf8');
const hook='  updateHeader();render();\n})();';
assert.equal(app.split(hook).length,2);
dom.window.eval(app.replace(hook,'  globalThis.testAPI={sanitizePaper,validPaperCode};\n})();'));
for(const code of codes){
 assert(dom.window.testAPI.validPaperCode(code));
 const source=fs.readFileSync(path.join(root,code,'summer-2026.html'),'utf8');
 for(const lang of ['en','gu']){
  const safe=dom.window.testAPI.sanitizePaper(source,lang);
  const doc=new JSDOM(safe).window.document;
  assert.equal(doc.querySelectorAll('section').length,5,`${code} ${lang} sections`);
  assert.equal(doc.querySelectorAll('details').length,28,`${code} ${lang} question sections`);
  assert(doc.querySelectorAll('figure img').length>0,`${code} ${lang} diagrams`);
  assert.equal(doc.querySelectorAll('script,iframe').length,0);
 }
}
dom.window.close();
console.log('All seven uploaded papers render 28 question sections and diagrams in both languages.');
