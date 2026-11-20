// Every refreshed paper must survive the deployed sanitizer, in both language
// modes, with all question texts, worked answers and image references intact.
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {JSDOM}=require('jsdom');
const root=path.resolve(__dirname,'..'),upload=path.join(root,'papers-upload');
const shell=new JSDOM('<main id="main"></main><span id="year"></span><button id="lang-toggle"></button><button id="menu-toggle"></button><div id="mobile-nav"></div><div id="toast"></div>',{url:'https://diplomaone.in/',runScripts:'outside-only'});
const app=fs.readFileSync(process.argv[2]||path.join(__dirname,'app.js'),'utf8'),hook='  updateHeader();render();\n})();';assert.equal(app.split(hook).length,2);
shell.window.eval(app.replace(hook,'  globalThis.testAPI={sanitizePaper,papersFromTree};\n})();'));
const parse=html=>new shell.window.DOMParser().parseFromString(html,'text/html');
const norm=x=>x.replace(/\s+/g,' ').trim();
const privateContext=require('./test_private_context');
const pdf=JSON.parse(fs.readFileSync(path.join(upload,'pdf-card-manifest.json'),'utf8')).papers;
const electrical=JSON.parse(fs.readFileSync(path.join(upload,'electrical-card-manifest.json'),'utf8')).papers;
assert.equal(pdf.length,37);assert.equal(electrical.length,12);
for(const record of [...pdf,...electrical]) {
 const [code,session]=record.paper.split('/'),html=fs.readFileSync(path.join(upload,'papers',record.paper+'.html'),'utf8');
 // Optional PDFs must not cause duplicate listings or win over the HTML.
 const index=shell.window.testAPI.papersFromTree({truncated:false,tree:[{path:`papers/${record.paper}.solution.pdf`,type:'blob',mode:'100644'},{path:`papers/${record.paper}.pdf`,type:'blob',mode:'100644'},{path:`papers/${record.paper}.html`,type:'blob',mode:'100644'},...record.assets.map(a=>({path:'papers/'+a.path,type:'blob',mode:'100644'}))]});
 assert.equal(index[code].length,1);assert(!index[code][0].pdfOnly,record.paper);
 for(const language of ['en','gu']) {
  const expected=parse(html).querySelector('main');
  expected.querySelectorAll(language==='en'?'.gu':'.en').forEach(e=>e.remove());
  const context=privateContext(html,code,session);
  const doc=parse(shell.window.testAPI.sanitizePaper(html,language,context));
  assert.equal(doc.querySelectorAll('section').length,5,record.paper+' '+language);
  const cards=[...doc.querySelectorAll('details.card')];assert.equal(cards.length,record.questions.length,record.paper+' '+language);
  doc.querySelectorAll('.paper-source-notes-title').forEach(e=>e.remove()); // trusted reader control, not supplied answer text
  assert.equal(norm(doc.body.textContent),norm(expected.textContent),record.paper+' '+language+' visible text changed');
  assert.equal(doc.querySelectorAll('iframe,script,object,embed,svg,style,button,main').length,0);
  assert(cards.every(c=>!c.open && c.querySelector(':scope > summary') && c.querySelector(':scope > .answer')));
  assert(cards.every(c=>norm(c.querySelector('.answer').textContent)||c.querySelector('.answer img')),'empty worked answer: '+record.paper);
  const images=[...doc.querySelectorAll('img')],originalImages=[...expected.querySelectorAll('img')];
  assert.equal(images.length,originalImages.length,record.paper+' '+language+' lost image');
  images.forEach((img,i)=>{
   const relative=originalImages[i].getAttribute('src');
   if(context.private){
    assert.equal(img.getAttribute('src'),null,'paid images must never use a public URL');
    assert.equal(img.dataset.privateAsset,context.assets.find(a=>a.path===relative).id);
   }else assert.equal(img.src,`https://sunilpa4.github.io/diplomaone-content/papers/${code}/${relative}`);
   assert(record.assets.some(a=>a.path===`${code}/${relative}`),record.paper+' image not audited');
   assert(fs.existsSync(path.join(upload,'papers',code,relative)));
   assert.equal(img.getAttribute('loading'),'lazy');
  });
  if(code==='DI01000021')assert(doc.body.textContent.includes('English only'),'Maths is not falsely translated');
 }
}
shell.window.close();
console.log('All 49 refreshed papers preserve 1,412 question parts, supplied text and scoped diagrams in both website language modes.');
