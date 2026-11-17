// Split the owner's combined 2025 solutions for the existing in-site reader.
// Requires jsdom and @resvg/resvg-js; the original HTML remains unchanged.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {JSDOM}=require('jsdom'),{Resvg}=require('@resvg/resvg-js');
const base=path.resolve(__dirname,'../papers-upload');
for(const code of ['DI01000181','DI01000191'])for(const season of ['summer','winter']){
 const original=fs.readFileSync(path.join(base,'originals',code,'winter-summer-2025.html'),'utf8');
 const dom=new JSDOM(original),doc=dom.window.document,article=doc.querySelector('#paper-'+season);
 assert(article);assert.equal(article.querySelectorAll('section').length,5);assert.equal(article.querySelectorAll('details').length,28);
 // The deployed reader rejects SVG data URLs. Render the supplied diagrams as
 // inert PNG images, instead of dropping them or injecting external SVG/JS.
 for(const img of article.querySelectorAll('img')){
  const src=img.getAttribute('src');assert(/^data:image\/svg\+xml;base64,[a-z0-9+/=]+$/i.test(src));
  const svg=Buffer.from(src.split(',')[1],'base64').toString('utf8');
  assert(!/<(?:script|image|foreignObject)\b|\b(?:href|src)\s*=|url\(\s*(?:https?:|\/\/)/i.test(svg));
  const png=new Resvg(svg,{fitTo:{mode:'width',value:640},font:{loadSystemFonts:true}}).render().asPng();
  img.setAttribute('src','data:image/png;base64,'+png.toString('base64'));
 }
 article.querySelectorAll('.lang-en-only').forEach(e=>e.classList.add('en'));
 article.querySelectorAll('.lang-gu-only').forEach(e=>e.classList.add('gu'));
 for(const f of article.querySelectorAll('.fraction')){
  assert.equal(f.children.length,2);assert(f.children[1].classList.contains('bar'));
  f.classList.add('frac');f.children[0].classList.add('num');f.children[1].classList.add('den');
 }
 article.querySelectorAll('details').forEach(e=>e.classList.add('card'));
 article.querySelectorAll('.answer-body').forEach(e=>e.classList.add('answer'));
 article.querySelectorAll('.chevron,.section-actions,.paper-actions,button').forEach(e=>e.remove());
 const out=new JSDOM('<!doctype html><html lang="en"><head><meta charset="utf-8"></head><body><main></main></body></html>');
 const od=out.window.document,main=od.querySelector('main');
 const title=od.createElement('title');title.textContent=`${code} · ${season} 2025 model solutions`;od.head.appendChild(title);
 const notice=od.createElement('p');notice.className='note';
 notice.textContent=code==='DI01000191'?'English-only model solution. આ નમૂનાનો ઉકેલ માત્ર અંગ્રેજીમાં ઉપલબ્ધ છે. Original question PDF was not supplied; answers have not been independently verified.':'Unofficial model solution; original question PDF was not supplied and answers have not been independently verified. અસલ પ્રશ્નપત્ર PDF મળ્યું નથી; આ બિનસત્તાવાર નમૂનાના જવાબો છે.';
 main.appendChild(notice);
 if(code==='DI01000191'){const m=od.createElement('meta');m.name='paper-language';m.content='en-only';od.head.appendChild(m);}
 for(const child of [...article.children]) main.appendChild(od.importNode(child,true));
 const output='<!doctype html>\n'+od.documentElement.outerHTML;
 assert(Buffer.byteLength(output)<3000000,`${code} ${season} too large`);
 const dest=path.join(base,'papers',code,`${season}-2025.html`);assert(!fs.existsSync(dest),`refusing to replace ${dest}`);
 fs.writeFileSync(dest,output);console.log(code,season,Buffer.byteLength(output),'bytes',main.querySelectorAll('img').length,'diagrams');
 dom.window.close();out.window.close();
}
