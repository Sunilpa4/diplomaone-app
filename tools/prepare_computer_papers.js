// Prepare the owner's Summer 2026 Computer Engineering papers for the deployed
// reader. Requires jsdom and @resvg/resvg-js; see papers-upload/README.md.
// Original HTML and PDFs remain unchanged; only the public reader copies differ.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const {JSDOM} = require('jsdom');
const {Resvg} = require('@resvg/resvg-js');
const base = path.resolve(__dirname, '..', 'papers-upload');
const codes = ['DI01000131','DI01000151','DI02000101','DI03000011','DI03000021','DI03000031','DI03000041','DI03000051','DI04000011','DI04000021'];
function load(code, language) {
  const dom = new JSDOM(fs.readFileSync(path.join(base,'originals',code,language+'.html'),'utf8'));
  const doc = dom.window.document;
  assert.equal(doc.querySelectorAll('main').length,1);
  assert.equal(doc.querySelectorAll('main section').length,5);
  assert.equal(doc.querySelectorAll('main details').length,28);
  assert.equal(doc.querySelectorAll('script,iframe,object,embed').length,0);
  // The deployed sanitizer does not retain all SVG features (e.g. ellipses,
  // patterns or font styling). Rasterizing preserves the entire diagram safely.
  for(const svg of doc.querySelectorAll('main svg')) {
    const source = new dom.window.XMLSerializer().serializeToString(svg);
    const png = new Resvg(source, {fitTo:{mode:'width',value:640}, font:{loadSystemFonts:true}}).render().asPng();
    const img=doc.createElement('img');
    img.setAttribute('src','data:image/png;base64,'+png.toString('base64'));
    img.setAttribute('alt',svg.getAttribute('aria-label')||'Diagram');
    svg.replaceWith(img);
  }
  return dom;
}
function bilingual(en, gu) {
  const doc=en.window.document, ed=doc.querySelector('main'), gd=gu.window.document.querySelector('main');
  const eSections=[...ed.querySelectorAll(':scope > section')], gSections=[...gd.querySelectorAll(':scope > section')];
  const wrap=(node,language)=>{const div=doc.createElement('div');div.className=language;div.appendChild(doc.importNode(node,true));return div;};
  // Keep the distinct introductions and footers for each language.
  for(const tag of ['header','footer']) {
    const e=ed.querySelector(':scope > '+tag), g=gd.querySelector(':scope > '+tag);
    assert(e&&g); e.replaceWith(wrap(e,'en'),wrap(g,'gu'));
  }
  eSections.forEach((section,i)=>{
    const other=gSections[i], es=[...section.querySelectorAll(':scope > details')], gs=[...other.querySelectorAll(':scope > details')];
    assert.equal(es.length,gs.length);
    const h=section.querySelector(':scope > h2'), gh=other.querySelector(':scope > h2');
    assert(h&&gh);h.replaceWith(wrap(h,'en'),wrap(gh,'gu'));
    es.forEach((item,j)=>{
      const eSummary=item.querySelector(':scope > summary'), gSummary=gs[j].querySelector(':scope > summary');
      const key=s=>s.textContent.match(/^Q\d\([abc]\)(?: OR)?/)?.[0];
      assert(key(eSummary)&&key(eSummary)===key(gSummary),`${i}/${j} language question mismatch`);
      const summary=doc.createElement('summary');
      for(const [src,lang] of [[eSummary,'en'],[gSummary,'gu']]){
        const span=doc.createElement('span');span.className=lang;span.innerHTML=src.innerHTML;summary.appendChild(span);
      }
      const eBody=doc.createElement('div'),gBody=doc.createElement('div');eBody.className='en';gBody.className='gu';
      for(const child of [...item.childNodes])if(child!==eSummary)eBody.appendChild(child);
      for(const child of [...gs[j].childNodes])if(child!==gSummary)gBody.appendChild(doc.importNode(child,true));
      item.replaceChildren(summary,eBody,gBody);
    });
  });
}
for(const code of codes){
  const en=load(code,'english'),doc=en.window.document;
  if(code==='DI01000151'){
    const gu=load(code,'gujarati');bilingual(en,gu);gu.window.close();
  } else {
    assert.equal(doc.querySelectorAll('main .en,main .gu').length,0);
    const meta=doc.createElement('meta');meta.name='paper-language';meta.content='en-only';doc.head.appendChild(meta);
    const notice=doc.createElement('p');notice.className='note';
    notice.textContent='English-only solution. આ ઉકેલ માત્ર અંગ્રેજીમાં ઉપલબ્ધ છે.';
    doc.querySelector('main').prepend(notice);
  }
  const output='<!doctype html>\n'+doc.documentElement.outerHTML;
  assert(Buffer.byteLength(output)<3000000,`${code} exceeds publisher limit`);
  fs.writeFileSync(path.join(base,'papers',code,'summer-2026.html'),output);
  console.log(code,Buffer.byteLength(output),'bytes');en.window.close();
}
