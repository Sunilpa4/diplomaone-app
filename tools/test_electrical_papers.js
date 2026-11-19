// Compare each prepared answer against its unchanged Drive HTML source.
// Added question IDs/OR labels and explicit errata are presentation annotations,
// not silent source edits. All original worked text and diagrams must remain.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {JSDOM}=require('jsdom');
const root=path.resolve(__dirname,'..'),base=path.join(root,'papers-upload');
const shell=new JSDOM('<main id="main"></main><span id="year"></span><button id="lang-toggle"></button><button id="menu-toggle"></button><div id="mobile-nav"></div><div id="toast"></div>',{url:'https://diplomaone.in/',runScripts:'outside-only'});
const app=fs.readFileSync(path.join(root,'website/app.js'),'utf8'),hook='  updateHeader();render();\n})();';assert.equal(app.split(hook).length,2);
shell.window.eval(app.replace(hook,'  globalThis.testAPI={sanitizePaper};\n})();'));
const parse=html=>new shell.window.DOMParser().parseFromString(html,'text/html'),norm=x=>x.replace(/\s+/g,' ').trim();
const records=JSON.parse(fs.readFileSync(path.join(base,'electrical-card-manifest.json'),'utf8')).papers;
for(const {paper} of records) {
 const [code,session]=paper.split('/'),split=['DI01000081','DI01009011'].includes(code);
 const reader=fs.readFileSync(path.join(base,'papers',paper+'.html'),'utf8');
 for(const language of ['en','gu']) {
  const original=parse(fs.readFileSync(path.join(base,'originals',code,`summer-2026.${split?language:'bilingual'}.html`),'utf8'));
  original.querySelectorAll(language==='en'?'.gu':'.en').forEach(e=>e.remove());
  const safe=parse(shell.window.testAPI.sanitizePaper(reader,language,{code,session}));
  const got=[...safe.querySelectorAll('details.card')],expected=[...original.querySelectorAll('main details')];
  assert.equal(got.length,28);assert.equal(expected.length,28);
  got.forEach((card,i)=>{
   const before=expected[i],after=card.querySelector('.answer');
   const count=before.querySelectorAll('figure svg').length;
   before.querySelectorAll('svg').forEach(e=>e.remove());
   const warnings=[...after.querySelectorAll('.paper-erratum')];
   assert.equal(warnings.length,code==='DI02000161'&&[4,8].includes(i)?1:0);
   warnings.forEach(e=>e.remove());
   assert.equal(norm(after.textContent),norm(before.querySelector('.answer').textContent),paper+' '+language+' answer '+(i+1)+' changed');
   assert(norm(card.querySelector('summary').textContent).includes(norm(before.querySelector('summary').textContent)),paper+' '+language+' question '+(i+1)+' changed');
   assert.equal(after.querySelectorAll('figure img').length,count,paper+' '+language+' diagrams '+(i+1));
  });
  assert.equal(safe.querySelectorAll('script,iframe,object,embed,svg').length,0);
 }
}
shell.window.close();console.log('Electrical: all 336 supplied answers, summaries, language variants and diagrams survive the deployed reader.');
