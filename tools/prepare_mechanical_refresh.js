// Reuse the four checksum-verified combined Mechanical Semester 3 Drive HTMLs.
// No generated answers or translations. Original HTML and prior published
// Summer readers remain in originals/. Requires jsdom@26.1.0/resvg@2.6.2.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {createHash}=require('node:crypto'),{JSDOM}=require('jsdom'),{Resvg}=require('@resvg/resvg-js');
const base=path.resolve(__dirname,'../papers-upload'),papers=path.join(base,'papers');
const hash=(bytes,algorithm='sha256')=>createHash(algorithm).update(bytes).digest('hex');
const norm=s=>s.replace(/\s+/g,' ').trim();
const sources=JSON.parse(fs.readFileSync(path.join(base,'mechanical-refresh-sources.json'),'utf8')).sources;
const manifestPath=path.join(base,'mechanical-refresh-manifest.json');
const previous=fs.existsSync(manifestPath)?JSON.parse(fs.readFileSync(manifestPath,'utf8')).papers:[];
const records=[],replacements=[];
const expectedLabels=()=>[1,2,3,4,5].flatMap(q=>(q===1?[[false,'a'],[false,'b'],[false,'c'],[true,'c']]:[[false,'a'],[false,'b'],[false,'c'],[true,'a'],[true,'b'],[true,'c']]).map(([alt,part])=>`Q.${q} (${part})${alt?' OR':''}`));
for(const source of sources) {
 const bytes=fs.readFileSync(path.join(base,source.source.path));
 assert.equal(bytes.length,source.source.size);assert.equal(hash(bytes,'md5'),source.source.drive_md5);assert.equal(hash(bytes),source.source.sha256);
 for(const [season,year] of [['winter',2025],['summer',2026]]) {
  const session=`${season}-${year}`,key=`${source.code}/${session}`,dom=new JSDOM(bytes.toString('utf8')),doc=dom.window.document;
  const articles=[...doc.querySelectorAll('main > article')].filter(a=>a.id===`paper-${season}`||a.id===`paper-${session}`);
  assert.equal(articles.length,1,key);const article=articles[0];
  assert(article.querySelector('.paper-meta').textContent.includes(source.code));
  assert(article.querySelector('.paper-meta').textContent.includes(`${season[0].toUpperCase()+season.slice(1)}-${year}`));
  assert.equal(article.querySelectorAll('section').length,5);
  const sourceCount=article.querySelectorAll('details').length,aliases=new Map();
  for(const card of article.querySelectorAll('details'))aliases.set(card.id,[card.id]);
  const repeatedCommonParts=season==='summer'&&['DI03000161','DI03000171'].includes(source.code);
  if(repeatedCommonParts) {
   // The original Summer paper offers OR only for Q1(c). The supplied HTML
   // repeats the identical common Q1(a)/Q1(b) answers inside both branches.
   // Show them once, audit both source IDs, never drop a distinct explanation.
   assert.equal(sourceCount,30);
   for(const part of [1,2]) {
    const first=article.querySelector(`#summer-q1-s1-i${part}`),duplicate=article.querySelector(`#summer-q1-s2-i${part}`);
    assert(first&&duplicate);assert.equal(norm(first.textContent),norm(duplicate.textContent));
    assert.deepEqual([...first.querySelectorAll('img')].map(i=>i.src),[...duplicate.querySelectorAll('img')].map(i=>i.src));
    aliases.get(first.id).push(duplicate.id);duplicate.remove();
   }
   const captions=article.querySelector('section').querySelectorAll('.set-caption');assert.equal(captions.length,2);
   captions[0].textContent='Q1(a) and Q1(b) are common to both choices; choose one Q1(c) option.';
   captions[1].textContent='OR alternative for Q1(c)';
   article.querySelectorAll('.paper-meta span').forEach(e=>{e.textContent=e.textContent.replace('30 answer cards','28 unique question parts');});
  } else assert.equal(sourceCount,28);
  article.querySelectorAll('.chevron,.section-actions,.paper-actions,button').forEach(e=>e.remove());
  article.querySelectorAll('.assumption-note').forEach(e=>e.classList.add('note'));
  for(const fraction of article.querySelectorAll('.fraction')) {
   assert.equal(fraction.children.length,2);fraction.classList.add('frac');
   fraction.children[0].classList.add('num');fraction.children[1].classList.add('den');
  }
  const cards=[];
  for(const card of article.querySelectorAll('details')) {
   const code=card.querySelector('.question-code'),match=code.textContent.match(/^Q([1-5])\(([abc])\)/);assert(match,card.id);
   const alt=card.id.includes('-s2-'),label=`Q.${match[1]} (${match[2]})${alt?' OR':''}`;
   if(alt&&!/\bOR\b/.test(code.textContent))code.appendChild(doc.createTextNode(' — OR'));
   card.classList.add('card');card.dataset.question=label;card.removeAttribute('open');
   const answer=card.querySelector(':scope > .answer-body');assert(answer);answer.classList.add('answer');
   cards.push({label,source_card_ids:aliases.get(card.id)});
  }
  assert.deepEqual(cards.map(c=>c.label),expectedLabels(),key);
  const assets=[],images=new Map(),assetDir=path.join(papers,source.code,`${session}.assets`);fs.mkdirSync(assetDir,{recursive:true});
  for(const img of article.querySelectorAll('img')) {
   assert(/^data:image\/svg\+xml;base64,[a-z0-9+/=]+$/i.test(img.getAttribute('src')));
   const svg=Buffer.from(img.getAttribute('src').split(',')[1],'base64'),digest=hash(svg);
   assert(!/<(?:script|image|foreignObject)\b|\b(?:href|src)\s*=|url\(\s*(?:https?:|\/\/)/i.test(svg.toString('utf8')));
   let asset=images.get(digest);
   if(!asset) {
    const png=new Resvg(svg,{fitTo:{mode:'width',value:1000},font:{loadSystemFonts:true,fontFiles:[path.resolve(base,'../website/assets/noto-sans-gujarati.ttf')]}}).render().asPng();
    assert(png.length<2000000);
    const name=String(assets.length+1).padStart(4,'0')+'.png';
    asset={path:`${source.code}/${session}.assets/${name}`,sha256:hash(png),source_svg_sha256:digest,width:png.readUInt32BE(16),height:png.readUInt32BE(20)};
    const dest=path.join(assetDir,name);if(fs.existsSync(dest))assert.equal(hash(fs.readFileSync(dest)),asset.sha256,'Refusing a changed diagram');else fs.writeFileSync(dest,png);
    images.set(digest,asset);assets.push(asset);
   }
   img.setAttribute('src',asset.path.split('/').slice(1).join('/'));img.setAttribute('width',asset.width);img.setAttribute('height',asset.height);img.setAttribute('loading','lazy');
  }
  const out=new JSDOM('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="paper-layout" content="source-html-cards-v1"><meta name="paper-language" content="en-only"><meta name="paper-question-count" content="28"></head><body><main></main></body></html>');
  const od=out.window.document,main=od.querySelector('main'),title=od.createElement('title');title.textContent=`${source.code} · ${session} · Supplied worked study answers`;od.head.appendChild(title);
  const notice=od.createElement('p');notice.className='note';
  notice.textContent='Updated supplied study solution — English only. આ નવો આપેલો ઉકેલ માત્ર અંગ્રેજીમાં છે; ભાષા બદલવાથી જવાબોનું ભાષાંતર થતું નથી. Unofficial model answers, not a GTU marking scheme; answers have not been independently verified.';
  main.appendChild(notice);
  if(season==='winter') {
   const missing=od.createElement('p');missing.className='note';missing.textContent='The original Winter 2025 question PDF was not found in the supplied Drive files. This reader preserves the Winter questions and answers from the combined source HTML; the Summer PDF is not linked to this exam.';main.appendChild(missing);
  }
  if(repeatedCommonParts) {
   const duplicateNote=od.createElement('p');duplicateNote.className='note';duplicateNote.textContent='Exam choice: Q1(a) and Q1(b) are common parts, shown once. The supplied HTML repeats their identical answers in both Q1(c) choice branches; both source occurrences are recorded in the audit. Choose one Q1(c) option as printed on the original paper.';main.appendChild(duplicateNote);
  }
  const notes=od.createElement('div');notes.className='paper-source-notes';
  for(const child of [...article.children]) {
   if(child.tagName==='SECTION')continue;
   const clone=od.importNode(child,true);
   for(const header of clone.querySelectorAll('h1')) {const h=od.createElement('h3');h.innerHTML=header.innerHTML;header.replaceWith(h);}
   notes.appendChild(clone);
  }
  const footer=doc.querySelector('main > .site-footer');if(footer)notes.appendChild(od.importNode(footer,true));
  main.appendChild(notes);
  for(const section of article.querySelectorAll(':scope > section'))main.appendChild(od.importNode(section,true));
  assert.equal(main.querySelectorAll('section').length,5);assert.equal(main.querySelectorAll('details.card').length,28);
  assert.equal(main.querySelectorAll('svg,script,button,iframe,object,embed').length,0);
  const output=('<!doctype html>\n'+od.documentElement.outerHTML+'\n').replace(/[ \t]+\n/g,'\n');assert(Buffer.byteLength(output)<3000000);
  const dest=path.join(papers,key+'.html');
  if(fs.existsSync(dest)&&hash(fs.readFileSync(dest))!==hash(output)) {
   const old=previous.find(r=>r.paper===key);assert(process.argv.includes('--update-reader-copies')&&old&&hash(fs.readFileSync(dest))===old.html_sha256,'Refusing an unreviewed reader copy');
  }
  fs.writeFileSync(dest,output);
  records.push({paper:key,source_sha256:source.source.sha256,source_card_count:sourceCount,questions:cards.map(c=>c.label),cards,html_sha256:hash(output),languages:['en'],assets});
  if(season==='summer')replacements.push({path:key+'.html',old_sha256:source.sessions[session].previous_reader.sha256,new_sha256:hash(output),reason:'Owner requested the newly supplied worked Summer 2026 answers for this exact Mechanical Semester 3 exam; prior reader archived unchanged.',source_drive_id:source.source.drive_id});
  console.log(key,28,'question cards;',assets.length,'distinct diagrams;',sourceCount,'source card occurrences preserved');
  dom.window.close();out.window.close();
 }
}
fs.writeFileSync(manifestPath,JSON.stringify({format:'source-html-cards-v1',papers:records},null,2)+'\n');
fs.writeFileSync(path.join(base,'reviewed-paper-replacements.json'),JSON.stringify(replacements,null,2)+'\n');
