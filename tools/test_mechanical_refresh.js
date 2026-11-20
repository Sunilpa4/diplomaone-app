// All 228 supplied source-card occurrences must survive as 224 unique parts.
// The four repeated common Q1(a)/Q1(b) occurrences are exact duplicates, not
// omitted work. Compare every worked answer and diagram in both site languages.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{createHash}=require('node:crypto');
const {JSDOM}=require('jsdom');
const root=path.resolve(__dirname,'..'),base=path.join(root,'papers-upload');
const hash=(x,a='sha256')=>createHash(a).update(x).digest('hex'),norm=x=>x.replace(/\s+/g,' ').trim();
const shell=new JSDOM('<main id="main"></main><span id="year"></span><button id="lang-toggle"></button><button id="menu-toggle"></button><div id="mobile-nav"></div><div id="toast"></div>',{url:'https://diplomaone.in/',runScripts:'outside-only'});
const app=fs.readFileSync(process.argv[2]||path.join(root,'website/app.js'),'utf8'),hook='  updateHeader();render();\n})();';assert.equal(app.split(hook).length,2);
shell.window.eval(app.replace(hook,'  globalThis.testAPI={sanitizePaper};\n})();'));
const parse=html=>new shell.window.DOMParser().parseFromString(html,'text/html');
const privateContext=require('../website/test_private_context');
const sources=JSON.parse(fs.readFileSync(path.join(base,'mechanical-refresh-sources.json'),'utf8')).sources;
const manifest=JSON.parse(fs.readFileSync(path.join(base,'mechanical-refresh-manifest.json'),'utf8')).papers;
const replacements=JSON.parse(fs.readFileSync(path.join(base,'reviewed-paper-replacements.json'),'utf8'));
assert.equal(sources.length,4);assert.equal(manifest.length,8);assert.equal(replacements.length,4);
assert.equal(manifest.reduce((n,r)=>n+r.questions.length,0),224);
assert.equal(manifest.reduce((n,r)=>n+r.source_card_count,0),228);
assert.equal(manifest.reduce((n,r)=>n+r.assets.length,0),109);
for(const source of sources) {
 const bytes=fs.readFileSync(path.join(base,source.source.path));assert.equal(hash(bytes,'md5'),source.source.drive_md5);assert.equal(hash(bytes),source.source.sha256);assert.equal(bytes.length,source.source.size);
 const original=parse(bytes.toString('utf8'));
 const previous=source.sessions['summer-2026'].previous_reader;
 assert.equal(hash(fs.readFileSync(path.join(base,previous.path))),previous.sha256,'previous supplied reader preserved');
 for(const season of ['winter','summer']) {
  const session=season==='winter'?'winter-2025':'summer-2026',record=manifest.find(r=>r.paper===`${source.code}/${session}`);assert(record);
  const article=original.querySelector(`#paper-${season}`)||original.querySelector(`#paper-${session}`);
  const sourceCards=[...article.querySelectorAll('details')];assert.equal(sourceCards.length,record.source_card_count);
  assert.deepEqual(record.cards.flatMap(c=>c.source_card_ids).sort(),sourceCards.map(c=>c.id).sort(),'every supplied source occurrence accounted for');
  const html=fs.readFileSync(path.join(base,'papers',record.paper+'.html'),'utf8');assert.equal(hash(html),record.html_sha256);
  assert.equal(record.source_sha256,source.source.sha256);
  const raw=parse(html);assert(raw.querySelector('meta[name="paper-language"][content="en-only"]'));
  assert.deepEqual([...raw.querySelectorAll('details.card')].map(c=>c.dataset.question),record.questions);
  const assetMap=new Map(record.assets.map(a=>[a.path,a]));
  for(const asset of record.assets) {
   const image=fs.readFileSync(path.join(base,'papers',asset.path));assert.equal(hash(image),asset.sha256);assert.equal(image.readUInt32BE(16),asset.width);assert.equal(image.readUInt32BE(20),asset.height);
  }
  for(const language of ['en','gu']) {
   const doc=parse(shell.window.testAPI.sanitizePaper(html,language,privateContext(html,source.code,session)));
   const cards=[...doc.querySelectorAll('details.card')];assert.equal(cards.length,28);assert.equal(doc.querySelectorAll('section').length,5);
   assert(doc.body.textContent.includes('English only'),'do not invent a Gujarati translation');
   assert.equal(doc.querySelectorAll('svg,script,iframe,object,embed,button').length,0);
   record.cards.forEach((card,i)=>{
    const got=cards[i],after=got.querySelector('.answer');assert(after&&!got.open);
    for(const id of card.source_card_ids) {
     const before=original.getElementById(id);assert(before&&article.contains(before));
     assert.equal(norm(after.textContent),norm(before.querySelector('.answer-body').textContent),`${record.paper} ${id} ${language}: worked answer changed`);
     assert(norm(got.querySelector('summary').textContent).includes(norm(before.querySelector('.question-text').textContent)),`${record.paper} ${id}: question lost`);
     assert(norm(got.querySelector('summary').textContent).includes(norm(before.querySelector('.marks').textContent)),'marks retained');
     const expected=[...before.querySelectorAll('.answer-body img')],images=[...after.querySelectorAll('img')];assert.equal(images.length,expected.length);
     images.forEach((img,j)=>{
      assert.equal(img.getAttribute('src'),null,'no public image fallback for paid papers');
      const asset=[...assetMap.values()].find(a=>a.sha256===img.dataset.privateAsset);assert(asset,'unscoped or unaudited private diagram');
      const svg=Buffer.from(expected[j].getAttribute('src').split(',')[1],'base64');assert.equal(hash(svg),asset.source_svg_sha256,'wrong diagram');
     });
    }
   });
   if(season==='winter')assert(doc.body.textContent.includes('original Winter 2025 question PDF was not found'));
  }
  if(season==='summer') {
   const replacement=replacements.find(r=>r.path===record.paper+'.html');assert(replacement);assert.equal(replacement.old_sha256,previous.sha256);assert.equal(replacement.new_sha256,record.html_sha256);assert.equal(replacement.source_drive_id,source.source.drive_id);
   if(record.source_card_count===30) {
    assert.equal(record.cards[0].source_card_ids.length,2);assert.equal(record.cards[1].source_card_ids.length,2);
    assert(raw.body.textContent.includes('Q1(a) and Q1(b) are common parts, shown once'));
   }
  }
 }
}
const audit=JSON.parse(fs.readFileSync(path.join(base,'mechanical-placement-audit.json'),'utf8'));
for(const record of audit.previous_public_papers) {
 const pdf=fs.readFileSync(path.join(base,'papers',record.code,'summer-2026.pdf'));
 assert.equal(hash(pdf),record.question_sha256);assert.equal(hash(Buffer.concat([Buffer.from(`blob ${pdf.length}\0`),pdf]),'sha1'),record.question_git_blob);
 if(['DI03000141','DI03000151'].includes(record.code))assert.equal(hash(fs.readFileSync(path.join(base,'papers',record.code,'summer-2026.html'))),record.original_html_sha256,'do not overwrite the other two subjects');
}
shell.window.close();console.log('Mechanical recheck: all 228 supplied occurrences, 224 unique worked parts, 109 diagrams and four exact replacement hashes verified in both site language modes.');
