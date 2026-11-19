// Reuse the owner's checksum-reviewed Summer 2026 Electrical HTML solutions.
// No answer rewriting. Source HTML/PDF bytes live in papers-upload/originals
// and papers/ respectively. SVGs become inert, full-feature PNGs, not the
// reader's intentionally restricted SVG subset. Requires jsdom@26.1.0 and
// @resvg/resvg-js@2.6.2. Run from any directory with NODE_PATH configured.
const fs=require('node:fs'), path=require('node:path'), assert=require('node:assert/strict');
const {createHash}=require('node:crypto');
const {JSDOM}=require('jsdom'), {Resvg}=require('@resvg/resvg-js');
const base=path.resolve(__dirname,'../papers-upload');
const provenance=JSON.parse(fs.readFileSync(path.join(base,'electrical-paper-provenance.json'),'utf8'));
const marker='<meta name="paper-layout" content="source-html-cards-v1">';
const hash=(data,algorithm='sha256')=>createHash(algorithm).update(data).digest('hex');
const expected=Array.from({length:5},(_,i)=>i+1).flatMap(q=>(q===1?['a','b','c','c OR']:['a','b','c','a OR','b OR','c OR']).map(part=>`Q.${q} (${part[0]})${part.endsWith('OR')?' OR':''}`));
const records=[];
const manifestPath=path.join(base,'electrical-card-manifest.json');
const previous=fs.existsSync(manifestPath)?JSON.parse(fs.readFileSync(manifestPath,'utf8')).papers:[];
function readSource(code,language) {
 const rel=`originals/${code}/summer-2026.${language}.html`, file=path.join(base,rel);
 const entry=provenance.find(e=>e.paper===`${code}/summer-2026`).files.find(e=>e.path===rel);
 const data=fs.readFileSync(file);
 assert.equal(hash(data),entry.sha256,`${rel}: changed reviewed source`);
 assert.equal(hash(data,'md5'),entry.md5,`${rel}: changed reviewed source`);
 const dom=new JSDOM(data.toString('utf8')),doc=dom.window.document;
 assert.equal(doc.querySelectorAll('main').length,1);
 assert.equal(doc.querySelectorAll('main > section').length,5);
 assert.equal(doc.querySelectorAll('main details').length,28);
 assert.equal(doc.querySelectorAll('main iframe,main object,main embed').length,0);
 return dom;
}
function combine(en,gu) {
 const doc=en.window.document, main=doc.querySelector('main'), other=gu.window.document.querySelector('main');
 const wrap=(node,language,tag='div')=>{const out=doc.createElement(tag);out.className=language;out.appendChild(doc.importNode(node,true));return out;};
 // Match by section, part order and English OR labels. The separate Electronics
 // Devices Gujarati file omits question IDs; supply the matching ID explicitly.
 const eItems=[...main.querySelectorAll('details')],gItems=[...other.querySelectorAll('details')];
 eItems.forEach((item,i)=>{
  const eSummary=item.querySelector(':scope > summary'),gSummary=gItems[i].querySelector(':scope > summary');
  const match=eSummary.textContent.match(/Q\.\s*\d\s*\([abc]\)(?:\s+OR)?/);
  assert(match);assert.equal(match[0].replace(/ OR$/,''),expected[i].replace(/ OR$/,''));
  if(expected[i].endsWith('OR') && (i===3 || expected[i].includes('(a)')))assert.equal(match[0],expected[i],'Missing start of source OR block');
  const gMatch=gSummary.textContent.match(/Q\.\s*\d\s*\([abc]\)(?:\s+OR)?/);
  if(gMatch)assert.equal(gMatch[0].replace(/ OR$/,''),expected[i].replace(/ OR$/,''));
  for(const [summary,m,document] of [[eSummary,match,doc],[gSummary,gMatch,gu.window.document]]) {
   if(m?.[0]===expected[i])continue;
   assert(!m?.[0].endsWith('OR'),'Unexpected source OR marker');
   const label=document.createElement('span');label.className='paper-choice-label';
   label.textContent=(m?'OR':expected[i])+' · ';summary.prepend(label);
  }
  item.dataset.question=expected[i];
  const summary=doc.createElement('summary');
  for(const [src,language] of [[eSummary,'en'],[gSummary,'gu']]){const span=doc.createElement('span');span.className=language;span.innerHTML=src.innerHTML;summary.appendChild(span);}
  const answer=doc.createElement('div');answer.className='answer';
  answer.append(wrap(item.querySelector(':scope > .answer'),'en'),wrap(gItems[i].querySelector(':scope > .answer'),'gu'));
  // Avoid nesting duplicate bordered answer containers.
  for(const inner of answer.querySelectorAll('.answer'))inner.classList.remove('answer');
  item.replaceChildren(summary,answer);
 });
 const eSections=[...main.querySelectorAll(':scope > section')],gSections=[...other.querySelectorAll(':scope > section')];
 eSections.forEach((section,i)=>{const h=section.querySelector('h2'),gh=gSections[i].querySelector('h2');assert(h&&gh);h.replaceWith(wrap(h,'en'),wrap(gh,'gu'));});
 for(const tag of ['header','footer']) {
  const e=main.querySelector(':scope > '+tag),g=other.querySelector(':scope > '+tag);
  if(e&&g)e.replaceWith(wrap(e,'en'),wrap(g,'gu'));
 }
}
for(const record of provenance) {
 const [code,session]=record.paper.split('/');
 const split=['DI01000081','DI01009011'].includes(code);
 const dom=readSource(code,split?'en':'bilingual'),doc=dom.window.document;
 if(split){const gu=readSource(code,'gu');combine(dom,gu);gu.window.close();}
 const main=doc.querySelector('main');
 main.querySelectorAll('.lang-switch,script,style,button').forEach(e=>e.remove());
 const notice=doc.createElement('p');notice.className='note';
 notice.innerHTML='<span class="en">Supplied unofficial study solution, not an official GTU answer key. Answers and teaching diagrams have not been independently verified. Use Enlarge image for small details.</span><span class="gu">આ આપેલો બિનસત્તાવાર અભ્યાસ ઉકેલ છે, સત્તાવાર GTU જવાબવહી નથી. જવાબો અને આકૃતિઓની સ્વતંત્ર ચકાસણી થઈ નથી. વાંચવા માટે ચિત્ર મોટું કરો.</span>';
 main.prepend(notice);
 const sourceNotes=doc.createElement('div');sourceNotes.className='paper-source-notes';
 for(const child of [...main.children])if(child!==notice&&child.tagName!=='SECTION')sourceNotes.appendChild(child);
 main.insertBefore(sourceNotes,main.querySelector(':scope > section'));
 // Known source errors are prominently flagged, not silently changed or certified.
 if(code==='DI02000161') {
  const items=[...main.querySelectorAll('details')];
  const warnings={
   4:[
    'Source review warning — Q.2(a): The supplied NOR-only construction is incorrect. NOR(A′,B′) = AB, not NAND. A correct four-NOR NAND uses n1=NOR(A,A), n2=NOR(B,B), n3=NOR(n1,n2), Y=NOR(n3,n3). A five-NOR XOR uses p=NOR(A,B), q=NOR(A,p), r=NOR(B,p), s=NOR(q,r), Y=NOR(s,s). The original answer is retained below for traceability.',
    'મૂળ જવાબની નોંધ — Q.2(a): આપેલી NOR-only રચનામાં ભૂલ છે. NOR(A′,B′)=AB છે, NAND નથી. સાચી four-NOR NAND: n1=NOR(A,A), n2=NOR(B,B), n3=NOR(n1,n2), Y=NOR(n3,n3). Five-NOR XOR: p=NOR(A,B), q=NOR(A,p), r=NOR(B,p), s=NOR(q,r), Y=NOR(s,s). નીચે મૂળ જવાબ જાળવ્યો છે.'
   ],
   8:[
    'Source review warning — Q.2(b) OR: The optional simplification in the supplied answer is incorrect. For the printed minterms {0,1,5,6}, a valid simplified SOP is Y=A′B′ + B′C + ABC′, not A′B′ + BC. The unsimplified four-product implementation describes the printed expression; the source answer is retained below.',
    'મૂળ જવાબની નોંધ — Q.2(b) OR: આપેલા જવાબનું optional simplification ખોટું છે. Minterms {0,1,5,6} માટે સાચું SOP: Y=A′B′ + B′C + ABC′; A′B′ + BC નથી. મૂળ four-product રચના printed expression મુજબ છે. નીચે મૂળ જવાબ જાળવ્યો છે.'
   ]
  };
  for(const [index,texts] of Object.entries(warnings))for(const [i,language] of ['en','gu'].entries()){
   const warning=doc.createElement('p');warning.className='note paper-erratum';warning.textContent=texts[i];
   items[Number(index)].querySelector('.answer > .'+language).prepend(warning);
  }
 }
 const assets=[], dedupe=new Map();
 for(const [index,svg] of [...main.querySelectorAll('svg')].entries()) {
  const xml=new dom.window.XMLSerializer().serializeToString(svg);
  assert(!/<(?:script|image|foreignObject)\b|\b(?:href|src)\s*=|url\(\s*(?:https?:|\/\/)/i.test(xml),'Unsafe source SVG');
  const digest=hash(xml);
  let name=dedupe.get(digest);
  if(!name){
   name=String(assets.length+1).padStart(4,'0')+'.png';
   const data=new Resvg(xml,{fitTo:{mode:'width',value:1000},font:{loadSystemFonts:true,fontFiles:[path.resolve(base,'../website/assets/noto-sans-gujarati.ttf')]}}).render().asPng();
   const rel=`${code}/${session}.assets/${name}`,dest=path.join(base,'papers',rel);
   fs.mkdirSync(path.dirname(dest),{recursive:true});
   if(fs.existsSync(dest))assert.equal(hash(fs.readFileSync(dest)),hash(data),`${rel}: refusing changed diagram`);
   else fs.writeFileSync(dest,data);
   assets.push({path:rel,sha256:hash(data),source_svg_sha256:digest});dedupe.set(digest,name);
  }
  const img=doc.createElement('img');img.src=`${session}.assets/${name}`;img.alt=svg.getAttribute('aria-label')||svg.closest('figure')?.querySelector('figcaption')?.textContent||`Question diagram ${index+1}`;img.loading='lazy';
  svg.replaceWith(img);
 }
 assert.equal(main.querySelectorAll('details').length,28);
 assert(main.querySelectorAll('.en').length>=28 && main.querySelectorAll('.gu').length>=28);
 assert.equal(main.querySelectorAll('svg,script,iframe,style').length,0);
 const output='<!doctype html><html lang="en"><head><meta charset="utf-8">'+marker+'<title>'+code+' · Summer 2026 solved question cards</title></head><body>'+main.outerHTML+'</body></html>\n';
 assert(Buffer.byteLength(output)<3000000);
 const dest=path.join(base,'papers',record.paper+'.html');
 if(fs.existsSync(dest)&&hash(fs.readFileSync(dest))!==hash(output)) {
  const old=previous.find(p=>p.paper===record.paper);
  assert(process.argv.includes('--update-reader-copies')&&old&&hash(fs.readFileSync(dest))===old.html_sha256,'Refusing an unreviewed reader copy; review the previous manifest before --update-reader-copies');
 }
 fs.writeFileSync(dest,output);
 records.push({paper:record.paper,html_sha256:hash(output),questions:expected,assets});
 console.log(code,'28 bilingual question cards;',assets.length,'distinct diagrams');
 dom.window.close();
}
fs.writeFileSync(path.join(base,'electrical-card-manifest.json'),JSON.stringify({format:'source-html-cards-v1',papers:records},null,2)+'\n');
