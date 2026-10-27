"""Shared preview builder: turns a unit JSON + its SVG diagrams into one self-contained HTML file
(same look as the planned app: purple bar, lavender section headers, white tap-to-open cards)."""
import json, os

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
:root{--p:#7B2CD9;--pd:#6420B8;--lav:#EADDF7;--bg:#F3ECFA;--ink:#1d1b20}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{margin:0;background:#d8cce8;font-family:"Noto Sans Gujarati","Shruti","Nirmala UI",system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink)}
.phone{max-width:430px;margin:0 auto;min-height:100vh;background:var(--bg);padding-bottom:70px;position:relative}
.bar{position:sticky;top:0;z-index:10;background:var(--p);color:#fff;box-shadow:0 2px 6px rgba(0,0,0,.2)}
.top{display:flex;align-items:center;gap:14px;padding:14px 14px 10px}
.top svg{flex:none}
.ttl{flex:1;min-width:0}
.ttl b{display:block;font-size:17px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ttl small{opacity:.85;font-size:12.5px}
.lang{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.5);color:#fff;border-radius:18px;padding:6px 12px;font-weight:700;font-size:14px;cursor:pointer}
.tabs{display:flex;overflow-x:auto;scrollbar-width:none;padding:0 6px}
.tabs::-webkit-scrollbar{display:none}
.tab{flex:none;color:rgba(255,255,255,.75);padding:10px 14px 12px;font-size:14.5px;font-weight:600;cursor:pointer;border-bottom:3px solid transparent;background:none;border-top:0;border-left:0;border-right:0}
.tab.on{color:#fff;border-bottom-color:#fff}
.sec{margin-bottom:14px}
.sh{background:var(--lav);display:flex;align-items:center;justify-content:space-between;padding:16px 14px 16px 18px;font-weight:800;font-size:17px;position:relative}
.more{background:none;border:0;padding:4px 6px;cursor:pointer;border-radius:50%}
.menu{display:none;position:absolute;right:12px;top:48px;background:#fff;border-radius:8px;box-shadow:0 4px 16px rgba(0,0,0,.18);z-index:5;overflow:hidden;min-width:150px}
.menu.show{display:block}
.menu button{display:block;width:100%;text-align:left;background:none;border:0;padding:12px 16px;font-size:14.5px;cursor:pointer}
.menu button:hover{background:#f4eefc}
.card{background:#fff;border-radius:6px;margin:0 0 8px;box-shadow:0 1px 3px rgba(60,20,110,.14)}
.q{display:flex;gap:10px;align-items:flex-start;padding:16px 14px 16px 18px;color:var(--p);font-size:16.5px;line-height:1.45;cursor:pointer}
.q .n{flex:none;min-width:24px}
.q .t{flex:1}
.q.hd{font-weight:700}
.chev{flex:none;transition:transform .2s;margin-top:1px}
.card.open .chev{transform:rotate(180deg)}
.a{display:none;padding:0 16px 18px 52px;font-size:15.5px;line-height:1.65;color:#222}
.card.open .a{display:block;animation:fd .2s}
@keyframes fd{from{opacity:0;transform:translateY(-4px)}to{opacity:1}}
.a p{margin:0 0 10px}.a ul,.a ol{margin:0 0 10px;padding-left:20px}.a li{margin-bottom:4px}
.a b{color:#111}
.eq{background:#F5EEFD;border-left:4px solid var(--p);padding:8px 12px;border-radius:4px;font-weight:700;font-size:16.5px;color:var(--pd)}
.tw{overflow-x:auto;margin:0 0 10px -36px;padding-left:0}
table{border-collapse:collapse;font-size:13.5px;min-width:100%;line-height:1.4}
th{background:var(--p);color:#fff;text-align:left;padding:7px 8px;font-weight:700}
td{border-bottom:1px solid #eadff6;padding:7px 8px;vertical-align:top}
tr:nth-child(even) td{background:#faf7fe}
.dg{margin:6px 0 4px -36px;border:1px solid #eadff6;border-radius:10px;overflow:hidden;cursor:zoom-in;background:#fff}
.dg svg{display:block;width:100%;height:auto}
.dg.pg{margin-left:0}
.dgc{font-size:12px;color:#7a6f88;text-align:center;margin:-2px 0 10px -36px}
.dcard{background:#fff;border-radius:10px;margin:0 10px 12px;box-shadow:0 1px 3px rgba(60,20,110,.14);overflow:hidden;cursor:zoom-in}
.dcard .h{padding:12px 14px;color:var(--p);font-weight:700;font-size:15.5px;border-bottom:1px solid #f0e8f9}
.dcard svg{display:block;width:100%;height:auto}
.fbox{margin:4px 0 0;background:#F5EEFD;border-radius:6px;padding:9px 12px;font-size:18px;font-weight:700;color:var(--pd);display:inline-block}
.q .t .nm{display:block}
.mk{flex:none;background:#FFF1D6;color:#9A5B00;border-radius:12px;padding:2px 9px;font-size:12.5px;font-weight:800;margin-top:2px}
.ad{position:fixed;bottom:0;left:50%;transform:translateX(-50%);width:100%;max-width:430px;height:56px;background:#fff;border-top:1px solid #e3d8f0;display:flex;align-items:center;justify-content:center;gap:8px;color:#8b8199;font-size:12.5px;z-index:9}
.ad i{font-style:normal;background:#f2c94c;color:#5b4300;font-weight:800;font-size:10.5px;padding:1px 5px;border-radius:3px}
.modal{position:fixed;inset:0;background:rgba(20,10,35,.92);z-index:50;display:none;flex-direction:column}
.modal.show{display:flex}
.mh{display:flex;align-items:center;justify-content:space-between;color:#fff;padding:12px 16px;font-weight:700}
.mh button{background:rgba(255,255,255,.15);border:0;color:#fff;font-size:18px;width:38px;height:38px;border-radius:50%;cursor:pointer}
.mb{flex:1;overflow:auto;padding:10px}
.mb .zw{background:#fff;border-radius:8px;margin:auto;transform-origin:top left}
.mb svg{display:block;width:100%;height:auto}
.zb{display:flex;justify-content:center;gap:14px;padding:12px}
.zb button{background:#fff;border:0;border-radius:22px;padding:8px 20px;font-size:18px;font-weight:800;color:var(--p);cursor:pointer}
.a h4{margin:14px 0 6px;color:var(--pd);font-size:15.5px}
.a h4:first-child{margin-top:0}
.card.key{border-left:4px solid #2E7D32}
.card.key .q{color:#1B5E20}
.ex{margin:12px 0 10px -36px;border:1.5px dashed #C9A227;background:#FFFBEF;border-radius:10px;padding:10px 12px}
.ex .et{font-weight:800;color:#9A5B00;font-size:13px;margin-bottom:4px}
.ex .eq2{font-weight:700;margin-bottom:6px}
.ex p{margin:0 0 6px}
.a.rn .dg,.a.rn .dgc,.a.rn .tw,.a.rn .ex{margin-left:0}
.intro{margin:12px 10px;background:linear-gradient(135deg,#8E3BE8,#5B1BB0);color:#fff;border-radius:14px;padding:14px 16px}
.intro b{font-size:16px}.intro div{font-size:13px;opacity:.9;margin-top:4px}
.chips{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}
.chips span{background:rgba(255,255,255,.18);border-radius:12px;padding:3px 10px;font-size:12px;font-weight:700}
pre.code{background:#1E1530;color:#EDE7F6;border-radius:8px;padding:10px 12px;font:13px/1.55 "JetBrains Mono",Consolas,"DejaVu Sans Mono","Noto Sans Gujarati",monospace;overflow-x:auto;margin:0 0 10px;white-space:pre;tab-size:4}
pre.out{background:#0E1B12;color:#B9F6CA;border-radius:8px;padding:10px 12px;font:13px/1.5 Consolas,"DejaVu Sans Mono",monospace;overflow-x:auto;margin:0 0 10px;white-space:pre}
.kw{color:#C792EA;font-weight:700}.ty{color:#82AAFF}.st{color:#C3E88D}.cm{color:#8E9AAF;font-style:italic}.pp{color:#F78C6C}.nu{color:#F9C46B}.fn{color:#FFCB6B}
.pl{font-size:12px;font-weight:800;color:var(--pd);margin:10px 0 4px;letter-spacing:.4px;text-transform:uppercase}
@media (max-width:480px){pre.code,pre.out{font-size:11.5px;padding:9px 10px}}
.a code{background:#F1E9FB;color:#5B1BB0;padding:1px 5px;border-radius:4px;font-family:Consolas,"DejaVu Sans Mono",monospace;font-size:.9em}
.pbox{margin:12px 0 10px;border:1.5px dashed #2E8B7A;background:#F2FBF8;border-radius:10px;padding:10px 12px}
.pbox .et{font-weight:800;color:#1F6E60;font-size:13.5px;margin-bottom:6px}
.sx{margin:6px 0 0;font-size:12.5px;padding:8px 10px}
.a.pa{padding-left:16px}
</style></head>
<body><div class="phone">
<div class="bar">
 <div class="top">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12H5M11 5l-7 7 7 7"/></svg>
  <div class="ttl"><b id="title"></b><small id="sub"></small></div>
  <button class="lang" id="lang"></button>
 </div>
 <div class="tabs" id="tabs"></div>
</div>
<div id="view"></div>
</div>
<div class="ad"><i>AD</i> AdMob banner space</div>
<div class="modal" id="modal"><div class="mh"><span id="mt"></span><button id="mx">✕</button></div>
<div class="mb"><div class="zw" id="zw"></div></div>
<div class="zb"><button id="zo">−</button><button id="zr">100%</button><button id="zi">+</button></div></div>
<script>
const U = __UNIT__;
const SVG = __SVGS__;
const META = __META__;
const S = {lang:'en', tab:'notes'};
const STR = {
 en:{notes:'Notes',diagrams:'Diagrams',equations:'Formulas',viva:'Viva',exam:'Exam Qs',expand:'Expand all',collapse:'Collapse all',
     numericals:'Numericals',ex:'✏️ Solved Example',tapzoom:'Tap diagram to zoom',unit:'Unit',examhead:'Important Exam Questions',
     intro:'weightage',hours:'hours',introd:'Detailed notes as per GTU syllabus with diagrams, formulas, solved numericals and viva.',
     marks:'Marks',programs:'Programs',flowcharts:'Flowcharts',syntax:'Syntax',algorithms:'Algorithms',prog:'💻 Program',code:'Code',output:'Output',plot:'Plot window (output)',expl:'Explanation',
     introc:'Detailed notes as per GTU syllabus with flowcharts, solved C programs with real output, syntax and viva.',
     intropy:'Detailed notes as per GTU syllabus with diagrams, solved Python programs with real output, syntax and viva.'},
 gu:{notes:'નોટ્સ',diagrams:'આકૃતિઓ',equations:'સૂત્રો',viva:'વાઈવા',exam:'પરીક્ષા પ્રશ્નો',expand:'બધા ખોલો',collapse:'બધા બંધ કરો',
     numericals:'દાખલા',ex:'✏️ ઉકેલેલો દાખલો',tapzoom:'મોટું જોવા આકૃતિ પર ટેપ કરો',unit:'એકમ',examhead:'મહત્વના પરીક્ષા પ્રશ્નો',
     intro:'વેઇટેજ',hours:'કલાક',introd:'GTU syllabus મુજબ આકૃતિ, સૂત્રો, ઉકેલેલા દાખલા અને viva સાથે વિગતવાર નોટ્સ.',
     marks:'ગુણ',programs:'પ્રોગ્રામ્સ',flowcharts:'ફ્લોચાર્ટ',syntax:'સિન્ટેક્સ',algorithms:'અલ્ગોરિધમ',prog:'💻 પ્રોગ્રામ',code:'કોડ',output:'આઉટપુટ',plot:'પ્લોટ (આઉટપુટ)',expl:'સમજૂતી',
     introc:'GTU syllabus મુજબ flowcharts, આઉટપુટ સાથેના ઉકેલેલા C programs, syntax અને viva સાથે વિગતવાર નોટ્સ.'}};
const L = k => STR[S.lang][k];
const t = o => (o && typeof o === 'object') ? (o[S.lang] || o.en) : (o || '');
const chev = '<svg class="chev" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#7B2CD9" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>';
const dots = '<svg width="22" height="22" viewBox="0 0 24 24" fill="#222"><circle cx="12" cy="5" r="2.2"/><circle cx="12" cy="12" r="2.2"/><circle cx="12" cy="19" r="2.2"/></svg>';
const fixTables = h => h.replace(/<table>/g,'<div class="tw"><table>').replace(/<\/table>/g,'</table></div>');
const head = (title, menu=true) => `<div class="sh"><span>${title}</span>${menu?`<button class="more" data-more>${dots}</button><div class="menu"><button data-act="expand">${L('expand')}</button><button data-act="collapse">${L('collapse')}</button></div>`:''}</div>`;
const dgInline = id => `<div class="dg" data-dg="${id}">${SVG[id]}</div><div class="dgc">📐 ${t(U.diagrams.find(d=>d.id===id).title)} · ${L('tapzoom')}</div>`;

const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const KW = new Set('auto break case const continue default do else enum extern for goto if register return signed sizeof static struct switch typedef union unsigned volatile while'.split(' '));
const TY = new Set('int char float double void long short FILE size_t'.split(' '));
const PKW = new Set('False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield'.split(' '));
const PTY = new Set('int float str bool list tuple set dict complex frozenset bytes bytearray range object'.split(' '));
function hlPy(src){
  const re = /(#[^\n]*)|((?:\b[rRbBfFuU]{1,2})?(?:'{3}[\s\S]*?'{3}|"{3}[\s\S]*?"{3}|'(?:\\.|[^'\\\n])*'|"(?:\\.|[^"\\\n])*"))|(^>>>|^\.\.\.(?= ))|([A-Za-z_]\w*)(?=\s*\()|([A-Za-z_]\w*)|(\b(?:0[xXoObB][0-9a-fA-F_]+|\d[\d_]*(?:\.\d+)?(?:[eE][-+]?\d+)?j?)\b)/gm;
  let o='', last=0, m;
  while ((m = re.exec(src))){
    o += esc(src.slice(last, m.index)); last = re.lastIndex;
    const w = esc(m[0]);
    if (m[1]) o += `<span class="cm">${w}</span>`;
    else if (m[2]) o += `<span class="st">${w}</span>`;
    else if (m[3]) o += `<span class="pp">${w}</span>`;
    else if (m[4]) o += PKW.has(m[4]) ? `<span class="kw">${w}</span>` : PTY.has(m[4]) ? `<span class="ty">${w}</span>` : `<span class="fn">${w}</span>`;
    else if (m[5]) o += PKW.has(m[5]) ? `<span class="kw">${w}</span>` : PTY.has(m[5]) ? `<span class="ty">${w}</span>` : w;
    else o += `<span class="nu">${w}</span>`;
  }
  return o + esc(src.slice(last));
}
function hl(src){
  if (META.code_lang === 'python') return hlPy(src);
  const re = /(\/\/[^\n]*|\/\*[\s\S]*?\*\/)|("(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*')|(^[ \t]*#[^\n]*)|([A-Za-z_]\w*)(?=\s*\()|([A-Za-z_]\w*)|(\b\d+(?:\.\d+)?[fFlLuU]*\b)/gm;
  let o='', last=0, m;
  while ((m = re.exec(src))){
    o += esc(src.slice(last, m.index)); last = re.lastIndex;
    const w = esc(m[0]);
    if (m[1]) o += `<span class="cm">${w}</span>`;
    else if (m[2]) o += `<span class="st">${w}</span>`;
    else if (m[3]) o += `<span class="pp">${w}</span>`;
    else if (m[4]) o += KW.has(m[4]) ? `<span class="kw">${w}</span>` : TY.has(m[4]) ? `<span class="ty">${w}</span>` : `<span class="fn">${w}</span>`;
    else if (m[5]) o += KW.has(m[5]) ? `<span class="kw">${w}</span>` : TY.has(m[5]) ? `<span class="ty">${w}</span>` : w;
    else o += `<span class="nu">${w}</span>`;
  }
  return o + esc(src.slice(last));
}
const progBody = p => `<div class="pl">${L('code')}</div><pre class="code">${hl(t(p.code))}</pre><div class="pl">${L('output')}</div><pre class="out">${esc(p.out)}</pre>${p.plot?`<div class="pl">${L('plot')}</div>`+dgInline(p.plot).replace('class="dg"','class="dg pg"'):''}${p.expl?`<div class="pl">${L('expl')}</div>${fixTables(t(p.expl))}`:''}`;
const pBox = id => { const p=(U.programs||[]).find(x=>x.id===id); if(!p) return ''; return `<div class="pbox"><div class="et">${L('prog')}: ${t(p.title)}</div>${progBody(p)}</div>`; };
const exBox = id => { const n=(U.numericals||[]).find(x=>x.id===id); if(!n) return ''; return `<div class="ex"><div class="et">${L('ex')}</div><div class="eq2">${t(n.q)}</div>${fixTables(t(n.a))}</div>`; };
function notes(){
  let h = `<div class="intro"><b>${t(U.title)}</b><div>${L('unit')} ${U.unit} · ${U.weightage}% ${L('intro')} · ${U.hours} ${L('hours')}</div><div>${L(U.programs?(META.code_lang==='python'?'intropy':'introc'):'introd')}</div></div>`;
  U.notes.forEach((sec,si)=>{
    h += `<div class="sec">${head(t(sec.title))}`;
    sec.items.forEach((it,i)=>{
      const open = si===0&&i===0 ? ' open' : '';
      if (it.h) {
        h += `<div class="card${it.key?' key':''}${open}"><div class="q hd"><span class="t">${it.key?'⭐ ':''}${t(it.h)}</span>${chev}</div>
        <div class="a rn" style="padding-left:18px">${fixTables(t(it.body)).replace(/margin:0 0 10px -36px/g,'')}${it.diagram?dgInline(it.diagram):''}${(it.examples||[]).map(exBox).join('')}${(it.programs||[]).map(pBox).join('')}</div></div>`;
      } else {
        h += `<div class="card${open}"><div class="q"><span class="n">${i+1}.</span><span class="t">${t(it.q)}</span>${chev}</div>
        <div class="a">${fixTables(t(it.a))}${it.diagram?dgInline(it.diagram):''}</div></div>`;
      }
    });
    h += `</div>`;
  });
  return h;
}
function numericals(){
  return `<div class="sec">${head(L('numericals'))}` + (U.numericals||[]).map((n,i)=>
    `<div class="card"><div class="q"><span class="n">${i+1}.</span><span class="t">${t(n.q)}</span>${chev}</div><div class="a">${fixTables(t(n.a))}</div></div>`).join('') + `</div>`;
}
function diagrams(){
  return `<div class="sec">${head(L(U.programs&&META.code_lang!=='python'?'flowcharts':'diagrams'),false)}<div style="height:10px"></div>` + U.diagrams.map((d,i)=>
    `<div class="dcard" data-dg="${d.id}"><div class="h">${i+1}. ${t(d.title)}</div>${SVG[d.id]}</div>`).join('') + `</div>`;
}
function equations(){
  return U.equations.map(g=>`<div class="sec">${head(t(g.title))}` + g.items.map((e,i)=>
    `<div class="card"><div class="q"><span class="n">${i+1}.</span><span class="t"><span class="nm">${t(e.name)}</span><span class="fbox">${e.f}</span></span>${chev}</div>
     <div class="a"><p>${t(e.terms)}</p></div></div>`).join('') + `</div>`).join('');
}
function viva(){
  return U.viva.map(g=>`<div class="sec">${head(t(g.title))}` + g.items.map((v,i)=>
    `<div class="card"><div class="q"><span class="n">${i+1}.</span><span class="t">${t(v.q)}</span>${chev}</div><div class="a"><p>${t(v.a)}</p></div></div>`).join('') + `</div>`).join('');
}
function exam(){
  return `<div class="sec">${head(L('examhead'),false)}` + U.exam_questions.map((x,i)=>
    `<div class="card"><div class="q" style="cursor:default"><span class="n">${i+1}.</span><span class="t">${t(x.q)}</span><span class="mk">${x.marks} ${L('marks')}</span></div></div>`).join('') + `</div>`;
}
function programs(){
  return `<div class="sec">${head(L('programs'))}` + (U.programs||[]).map((p,i)=>
    `<div class="card"><div class="q hd"><span class="n">${i+1}.</span><span class="t">${t(p.title)}</span>${chev}</div><div class="a pa">${progBody(p)}</div></div>`).join('') + `</div>`;
}
function syntax(key){
  return (U[typeof key==='string'?key:'syntax']||[]).map(g=>`<div class="sec">${head(t(g.title))}` + g.items.map((e,i)=>
    `<div class="card"><div class="q"><span class="n">${i+1}.</span><span class="t"><span class="nm">${t(e.name)}</span><pre class="code sx">${hl(e.f)}</pre></span>${chev}</div>
     <div class="a">${e.terms && t(e.terms) ? fixTables(t(e.terms)) : ''}</div></div>`).join('') + `</div>`).join('');
}
const flowcharts = diagrams;
const algorithms = () => syntax('algorithms');
const ALLV = {notes, programs, diagrams, flowcharts, algorithms, syntax, equations, numericals, viva, exam};
const VIEWS = U.tabs ? Object.fromEntries(U.tabs.map(k=>[k, ALLV[k]])) : U.programs ? (META.code_lang==='python' ? {notes, programs, diagrams, syntax, viva, exam} : {notes, programs, flowcharts, syntax, viva, exam}) : U.numericals ? {notes, diagrams, equations, numericals, viva, exam} : {notes, diagrams, equations, viva, exam};
function render(){
  document.getElementById('title').textContent = `${L('unit')} ${U.unit}: ${t(U.title)}`;
  document.getElementById('sub').textContent = `${t(META.name)} · ${META.code}`;
  document.getElementById('lang').textContent = S.lang==='en' ? 'ગુ' : 'EN';
  document.getElementById('lang').style.display = META.languages.includes('gu') ? '' : 'none';
  document.getElementById('tabs').innerHTML = Object.keys(VIEWS).map(k=>`<button class="tab${S.tab===k?' on':''}" data-tab="${k}">${L(k)}</button>`).join('');
  document.getElementById('view').innerHTML = VIEWS[S.tab]();
  document.querySelectorAll('#view pre.c').forEach(e=>{ e.innerHTML = hl(e.textContent); e.className='code'; });
}
let zoom = 1;
function setZoom(z){ zoom = Math.min(4, Math.max(1, z)); const w=document.getElementById('zw'); w.style.width=(zoom*100)+'%'; document.getElementById('zr').textContent=Math.round(zoom*100)+'%'; }
document.addEventListener('click', e=>{
  const q = e.target.closest('.q'); if (q && q.parentElement.querySelector('.a')) { q.parentElement.classList.toggle('open'); return; }
  const tb = e.target.closest('[data-tab]'); if (tb){ S.tab = tb.dataset.tab; render(); window.scrollTo(0,0); return; }
  if (e.target.closest('#lang')){ S.lang = S.lang==='en'?'gu':'en'; render(); return; }
  const m = e.target.closest('[data-more]');
  document.querySelectorAll('.menu.show').forEach(x=>{ if(!m || x!==m.nextElementSibling) x.classList.remove('show'); });
  if (m){ m.nextElementSibling.classList.toggle('show'); return; }
  const act = e.target.closest('[data-act]');
  if (act){ act.closest('.sec').querySelectorAll('.card').forEach(c=>{ if(c.querySelector('.a')) c.classList.toggle('open', act.dataset.act==='expand'); }); act.parentElement.classList.remove('show'); return; }
  const dg = e.target.closest('[data-dg]');
  if (dg){ const id=dg.dataset.dg; document.getElementById('mt').textContent=t(U.diagrams.find(d=>d.id===id).title); document.getElementById('zw').innerHTML=SVG[id]; setZoom(1); document.getElementById('modal').classList.add('show'); return; }
  if (e.target.closest('#mx')) document.getElementById('modal').classList.remove('show');
  if (e.target.closest('#zi')) setZoom(zoom+0.5);
  if (e.target.closest('#zo')) setZoom(zoom-0.5);
  if (e.target.closest('#zr')) setZoom(1);
});
render();
</script></body></html>"""


def build_preview(unit, subject, diag_dir, out_path):
    svgs = {}
    for d in unit["diagrams"]:
        with open(os.path.join(diag_dir, d["id"] + ".svg"), encoding="utf-8") as f:
            svgs[d["id"]] = f.read()
    title = f'{subject["name"]["en"]} – Unit {unit["unit"]}'
    html = (TEMPLATE.replace("__UNIT__", json.dumps(unit, ensure_ascii=False))
            .replace("__SVGS__", json.dumps(svgs, ensure_ascii=False))
            .replace("__META__", json.dumps({"name": subject["name"], "code": subject["code"], "languages": subject.get("languages", ["en", "gu"]), "code_lang": subject.get("code_lang", "c")}, ensure_ascii=False))
            .replace("__TITLE__", title))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return out_path
