/* DiplomaOne's website reads the same published catalog and units as the app. */
(() => {
  'use strict';
  const main = document.querySelector('#main');
  const year = document.querySelector('#year');
  const langButton = document.querySelector('#lang-toggle');
  const menuButton = document.querySelector('#menu-toggle');
  const mobileNav = document.querySelector('#mobile-nav');
  const toast = document.querySelector('#toast');
  year.textContent = new Date().getFullYear();

  const strings = {
    en: {
      home:'Home', branches:'Explore branches', papers:'Solved papers', saved:'Saved notes', start:'Start learning', search:'Search subjects', allBranches:'All branches',
      heroEye:'A LITTLE HELP FOR YOUR BIG GOALS', heroTitle:'Your diploma,<br><em>made simpler.</em>', heroText:'Thoughtful notes, clear diagrams, and everything you need to feel a little more ready for class and exams.', browse:'Explore your branch', find:'Find a subject', heroBadge:'Made for diploma students', heroBadgeSmall:'Your learning, your pace',
      trust1:'Built for GTU diploma', trust1s:'Study with direction', trust2:'English & Gujarati', trust2s:'Learn your way', trust3:'Notes that make sense', trust3s:'Clear and easy to follow', trust4:'Free to explore', trust4s:'Your study space, always',
      chooseEye:'LET’S FIND YOUR WAY', choose:'Start with your branch', chooseText:'Pick a branch and find the notes made for your journey.', viewAll:'View all branches', ready:'subjects ready', coming:'More notes coming soon', subjects:'subjects', branch:'Branch',
      howEye:'A SIMPLER WAY TO STUDY', howTitle:'Less searching.<br>More learning.', howText:'From the first chapter to the final revision, your next step is always easy to find.', step1:'Choose your branch', step1s:'Start where you belong, across all diploma branches.', step2:'Find your subject', step2s:'Browse by semester or search by name and code.', step3:'Learn at your pace', step3s:'Read clear notes, diagrams, questions and more.',
      exploreEye:'PICK UP WHERE CURIOSITY STARTS', explore:'Ready when you are', exploreText:'A few subjects to get you started.', viewSubjects:'Search all subjects', units:'units', study:'Start studying',
      ctaTitle:'A little support goes a long way.', ctaText:'Take your notes with you, wherever your learning happens.', download:'Get the Android app',
      branchesTitle:'Every journey starts somewhere.', branchesText:'Find your branch and take the next step in your diploma journey.', searchBranches:'Search branches...', searchSubjects:'Search by subject name or code...', result:'results', semester:'Semester', semesters:'Semesters', semesterText:'Choose a semester to see the subjects available for this branch.', subjectList:'Subjects', subjectListText:'Choose a subject to explore its study material.',
      noBranches:'No branches found', noSubjects:'No subjects found', noSearch:'Try another name or subject code.', emptyTitle:'A little more is on the way.', emptyText:'Notes for this selection haven’t been added yet. Explore another branch in the meantime.',
      available:'Available', notYet:'Coming soon', unitsTitle:'Choose a unit', unitsText:'Select a unit to start reading.', hours:'hours', weightage:'weightage', viewUnit:'Read unit',
      read:'Study notes', notes:'Notes', programs:'Programs', diagrams:'Diagrams', flowcharts:'Flowcharts', equations:'Formulas', numericals:'Numericals', syntax:'Syntax', algorithms:'Algorithms', viva:'Viva', exam:'Exam questions', sources:'References', sourceIntro:'References supplied with this unit. External links may lead to other websites.', suggestedMarks:'Marks shown are suggested for practice, not official marks.', englishOnly:'This unit is currently available in English.',
      question:'Question', answer:'Answer', code:'Code', output:'Output', explanation:'Explanation', marks:'marks', noContent:'There is no content in this section yet.',
      save:'Save for later', savedButton:'Saved', savedTitle:'Your little study list.', savedText:'Keep the units you want to come back to. Saved on this device.', savedEmpty:'Nothing saved just yet', savedEmptyText:'When you save a unit, it will be waiting here for your next study session.', exploreBranches:'Explore branches',
      searchTitle:'Find what you need.', searchText:'Search the catalog by subject name or code, in English or Gujarati.', searchPrompt:'What are you looking for?', searchPromptText:'Type a subject name or code to begin.', retry:'Try again', loadError:'We couldn’t load this content.', loadErrorText:'Please check your connection and try again.', noUnit:'This unit is not available yet.', aboutTitle:'Made for the journey.', aboutText:'DiplomaOne is an independent study resource created to help GTU diploma students find clear, accessible learning material in English and Gujarati.', aboutNote:'DiplomaOne is not affiliated with Gujarat Technological University. Always refer to your official syllabus and your institution for authoritative information.', remove:'Remove', back:'Back',
    },
    gu: {
      home:'હોમ', branches:'બ્રાન્ચ જુઓ', papers:'ઉકેલેલા પેપર', saved:'સાચવેલી નોટ્સ', start:'અભ્યાસ શરૂ કરો', search:'વિષય શોધો', allBranches:'બધી બ્રાન્ચ',
      heroEye:'તમારા મોટા સપનાઓ માટે નાની મદદ', heroTitle:'તમારો ડિપ્લોમા,<br><em>હવે વધુ સરળ.</em>', heroText:'સરળ નોટ્સ, સ્પષ્ટ આકૃતિઓ અને વર્ગ તથા પરીક્ષાની તૈયારી માટે જરૂરી માર્ગદર્શન.', browse:'તમારી બ્રાન્ચ શોધો', find:'વિષય શોધો', heroBadge:'ડિપ્લોમા વિદ્યાર્થીઓ માટે', heroBadgeSmall:'તમારો અભ્યાસ, તમારી ગતિએ',
      trust1:'GTU ડિપ્લોમા માટે', trust1s:'સાચી દિશામાં અભ્યાસ', trust2:'ગુજરાતી અને અંગ્રેજી', trust2s:'તમારી રીતે શીખો', trust3:'સરળ સમજાય તેવી નોટ્સ', trust3s:'સ્પષ્ટ અને સહેલી', trust4:'મફત અભ્યાસ', trust4s:'તમારી અભ્યાસની જગ્યા',
      chooseEye:'ચાલો તમારી દિશા શોધીએ', choose:'તમારી બ્રાન્ચથી શરૂઆત કરો', chooseText:'તમારી બ્રાન્ચ પસંદ કરો અને તમારી નોટ્સ શોધો.', viewAll:'બધી બ્રાન્ચ જુઓ', ready:'વિષયો તૈયાર', coming:'વધુ નોટ્સ જલ્દી આવશે', subjects:'વિષયો', branch:'બ્રાન્ચ',
      howEye:'અભ્યાસની સરળ રીત', howTitle:'ઓછું શોધો.<br>વધુ શીખો.', howText:'પહેલા પ્રકરણથી અંતિમ પુનરાવર્તન સુધી, આગળનું પગલું શોધવું હવે સહેલું છે.', step1:'તમારી બ્રાન્ચ પસંદ કરો', step1s:'તમારી ડિપ્લોમા બ્રાન્ચથી શરૂઆત કરો.', step2:'તમારો વિષય શોધો', step2s:'સેમેસ્ટર, નામ અથવા કોડથી વિષય શોધો.', step3:'તમારી ગતિએ શીખો', step3s:'નોટ્સ, આકૃતિઓ અને પ્રશ્નો વાંચો.',
      exploreEye:'શીખવાની શરૂઆત અહીંથી', explore:'અભ્યાસ માટે તૈયાર', exploreText:'શરૂઆત કરવા માટે થોડા વિષયો.', viewSubjects:'બધા વિષયો શોધો', units:'એકમો', study:'વાંચવાનું શરૂ કરો',
      ctaTitle:'થોડી મદદથી ઘણો ફરક પડે છે.', ctaText:'અભ્યાસ જ્યાં પણ કરો, નોટ્સ તમારી સાથે રાખો.', download:'Android એપ મેળવો',
      branchesTitle:'દરેક સફરની એક શરૂઆત હોય છે.', branchesText:'તમારી બ્રાન્ચ શોધો અને ડિપ્લોમાની સફરમાં આગળ વધો.', searchBranches:'બ્રાન્ચ શોધો...', searchSubjects:'વિષયનું નામ અથવા કોડ શોધો...', result:'પરિણામો', semester:'સેમેસ્ટર', semesters:'સેમેસ્ટર', semesterText:'વિષયો જોવા માટે સેમેસ્ટર પસંદ કરો.', subjectList:'વિષયો', subjectListText:'અભ્યાસ સામગ્રી માટે વિષય પસંદ કરો.',
      noBranches:'કોઈ બ્રાન્ચ મળી નથી', noSubjects:'કોઈ વિષય મળ્યો નથી', noSearch:'બીજું નામ અથવા વિષય કોડ અજમાવો.', emptyTitle:'વધુ સામગ્રી જલ્દી આવશે.', emptyText:'આ પસંદગી માટે નોટ્સ હજુ ઉમેરાઈ નથી. ત્યાં સુધી બીજી બ્રાન્ચ જુઓ.',
      available:'ઉપલબ્ધ', notYet:'જલ્દી આવશે', unitsTitle:'એકમ પસંદ કરો', unitsText:'વાંચવાનું શરૂ કરવા માટે એકમ પસંદ કરો.', hours:'કલાક', weightage:'વેઇટેજ', viewUnit:'એકમ વાંચો',
      read:'અભ્યાસ નોટ્સ', notes:'નોટ્સ', programs:'પ્રોગ્રામ્સ', diagrams:'આકૃતિઓ', flowcharts:'ફ્લોચાર્ટ્સ', equations:'સૂત્રો', numericals:'ગણિતના દાખલા', syntax:'સિન્ટેક્સ', algorithms:'અલ્ગોરિધમ્સ', viva:'વાઇવા', exam:'પરીક્ષા પ્રશ્નો', sources:'સંદર્ભો', sourceIntro:'આ એકમ સાથે આપેલા સંદર્ભો. બહારની લિંક્સ અન્ય વેબસાઇટ પર લઈ જઈ શકે છે.', suggestedMarks:'દર્શાવેલા ગુણ અભ્યાસ માટે સૂચિત છે; તે સત્તાવાર ગુણ નથી.', englishOnly:'આ એકમ હાલમાં અંગ્રેજીમાં ઉપલબ્ધ છે.',
      question:'પ્રશ્ન', answer:'જવાબ', code:'કોડ', output:'આઉટપુટ', explanation:'સમજૂતી', marks:'ગુણ', noContent:'આ વિભાગમાં હજુ સામગ્રી નથી.',
      save:'પછી માટે સાચવો', savedButton:'સાચવ્યું', savedTitle:'તમારી અભ્યાસ યાદી.', savedText:'જે એકમો ફરી વાંચવા છે તે અહીં સાચવો. આ ઉપકરણ પર સાચવાય છે.', savedEmpty:'હજુ કંઈ સાચવ્યું નથી', savedEmptyText:'એકમ સાચવો અને તે તમારી આગામી અભ્યાસ માટે અહીં મળશે.', exploreBranches:'બ્રાન્ચ જુઓ',
      searchTitle:'તમને જે જોઈએ તે શોધો.', searchText:'વિષયના નામ અથવા કોડથી ગુજરાતી કે અંગ્રેજીમાં શોધો.', searchPrompt:'તમે શું શોધી રહ્યા છો?', searchPromptText:'વિષયનું નામ અથવા કોડ લખો.', retry:'ફરી પ્રયાસ કરો', loadError:'સામગ્રી લોડ થઈ શકી નથી.', loadErrorText:'ઇન્ટરનેટ તપાસો અને ફરી પ્રયાસ કરો.', noUnit:'આ એકમ હજુ ઉપલબ્ધ નથી.', aboutTitle:'તમારી સફર માટે.', aboutText:'DiplomaOne એ GTU ડિપ્લોમા વિદ્યાર્થીઓને ગુજરાતી અને અંગ્રેજીમાં સુલભ અભ્યાસ સામગ્રી આપવા માટેનું સ્વતંત્ર સાધન છે.', aboutNote:'DiplomaOne ગુજરાત ટેક્નોલોજિકલ યુનિવર્સિટી સાથે સંલગ્ન નથી. અધિકૃત માહિતી માટે હંમેશા તમારા સત્તાવાર અભ્યાસક્રમ અને સંસ્થાનો સંદર્ભ લો.', remove:'દૂર કરો', back:'પાછા',
    },
  };
  const readStore = (key, fallback) => { try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; } catch (_) { return fallback; } };
  const writeStore = (key, value) => { try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch (_) { return false; } };
  let lang = readStore('diplomaone.website.lang', 'en') === 'gu' ? 'gu' : 'en';
  let saved = readStore('diplomaone.website.saved', []);
  if (!Array.isArray(saved)) saved = [];
  let catalog = null;
  let activeTab = 'notes';
  let routeCounter = 0;
  let toastTimer;
  const tr = (key) => strings[lang][key] || strings.en[key] || key;
  const text = (value) => value == null ? '' : typeof value === 'object' ? String(value[lang] || value.en || value.gu || '') : String(value);
  const esc = (value) => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const icon = (name) => {
    const shapes = {
      search:'<circle cx="11" cy="11" r="7"/><path d="m16 16 4 4"/>',
      computer:'<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
      settings:'<circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 0-.1-1l1.8-1.4-1.7-3-2.2.8a7 7 0 0 0-1.8-1L14.7 4h-3.4L11 6.4a7 7 0 0 0-1.8 1L7 6.6l-1.7 3L7.1 11a7 7 0 0 0 0 2L5.3 14.4l1.7 3 2.2-.8a7 7 0 0 0 1.8 1l.3 2.4h3.4l.3-2.4a7 7 0 0 0 1.8-1l2.2.8 1.7-3-1.8-1.4c.1-.3.1-.7.1-1Z"/>',
      bolt:'<path d="m13 2-8 12h6l-1 8 9-13h-6z"/>',
      science:'<path d="M9 3h6M10 3v6l-5.5 8.5A2 2 0 0 0 6.2 21h11.6a2 2 0 0 0 1.7-3.5L14 9V3M8 16h8"/>',
      book:'<path d="M4 5.5C7.5 4 10 4.5 12 6c2-1.5 4.5-2 8-.5v13c-3.5-1.5-6-1-8 .5-2-1.5-4.5-2-8-.5zM12 6v13"/>',
      globe:'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 4 6 4 9s-1 6-4 9c-3-3-4-6-4-9s1-6 4-9Z"/>',
      check:'<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
      heart:'<path d="M20.5 5.5c-2-2-5-1.5-6.5.5L12 8l-2-2C8.5 4 5.5 3.5 3.5 5.5s-1.5 5 .5 7L12 20l8-7.5c2-2 2.5-5 .5-7Z"/>',
      grid:'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
      school:'<path d="M3 9l9-5 9 5-9 5-9-5ZM7 11.5V17c3 2 7 2 10 0v-5.5M21 9v7"/>',
    };
    const key = ({lan:'computer',terminal:'computer',wifi:'computer',factory:'settings',bolt:'bolt',science:'science',settings:'settings',apartment:'grid'})[name] || name;
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${shapes[key] || shapes.grid}</svg>`;
  };
  const safeCode = code => /^[A-Za-z0-9_-]+$/.test(code || '');
  const paperBase = 'https://sunilpa4.github.io/diplomaone-content/papers';
  const paperTreeUrl = 'https://api.github.com/repos/Sunilpa4/diplomaone-content/git/trees/main?recursive=1';
  const paperCache = new Map();
  // The older GTU scheme uses seven-digit codes, distinct from DI codes.
  const legacyPaperNames = {'4351902':'Manufacturing Engineering – III','4351903':'Thermal Engineering – II'};
  const validPaperCode = value => /^(?:DI[0-9]{8}|[0-9]{7})$/.test(value || '');
  const validPaperSession = value => /^[a-z][a-z0-9]*-[0-9]{4}$/.test(value || '');
  let paperIndex = null, paperIndexPending = null, paperIndexError = false;
  const fallbackPapers = Object.fromEntries(['DI03000141','DI03000151','DI03000161','DI03000171','DI03000201','DI03019011'].map(code=>[code,[{session:'summer-2026',pdf:'Question_Paper.pdf'}]]));
  // Discover only filenames, with no background polling or scheduled indexing.
  function papersFromTree(data) {
    if(!data || data.truncated!==false || !Array.isArray(data.tree))throw new Error('Paper directory is unavailable or incomplete');
    const files=new Set();
    for(const item of data.tree) {
      if(item.type!=='blob'||!['100644','100755'].includes(item.mode)||typeof item.path!=='string')continue;
      const parts=item.path.split('/');
      if(parts.length===3 && parts[0]==='papers' && validPaperCode(parts[1])) files.add(item.path);
    }
    const safe=Object.create(null);
    for(const path of files) {
      const [,code,file]=path.split('/');
      if(!file.endsWith('.html'))continue;
      const session=file.slice(0,-5);
      if(!validPaperSession(session))continue;
      (safe[code] ||= []).push({session,pdf:files.has(`papers/${code}/${session}.pdf`)?`${session}.pdf`:null,legacyPdf:files.has(`papers/${code}/Question_Paper.pdf`)});
    }
    for(const entries of Object.values(safe)) {
      entries.sort((a,b)=>b.session.slice(-4).localeCompare(a.session.slice(-4))||b.session.localeCompare(a.session));
      if(entries.length===1 && entries[0].legacyPdf && !entries[0].pdf)entries[0].pdf='Question_Paper.pdf';
    }
    return safe;
  }
  async function loadPaperIndex() {
    // Once per tab: a refresh reads GitHub again, never a background timer.
    if(paperIndex && !paperIndexError)return paperIndex;
    if(paperIndexPending)return paperIndexPending;
    paperIndexPending=(async()=>{
      const controller=new AbortController(), timeout=setTimeout(()=>controller.abort(),8000);
      try {
        const response=await fetch(paperTreeUrl,{cache:'no-cache',redirect:'error',signal:controller.signal});
        if(!response.ok)throw new Error('Paper list unavailable');
        paperIndex=papersFromTree(await response.json());paperIndexError=false;
      } catch(error) {
        console.error(error);paperIndexError=true;
        // Preserve the last known list on failure; retry when the user navigates.
        if(!paperIndex)paperIndex=fallbackPapers;
      } finally { clearTimeout(timeout); }
      return paperIndex;
    })();
    try{return await paperIndexPending;}finally{paperIndexPending=null;}
  }
  const paperSessionTitle = session => session.split('-').map((word,i)=>i?word:word.charAt(0).toUpperCase()+word.slice(1)).join(' ');
  const paperListNotice = () => paperIndexError ? `<p class="reader-notice">${lang==='gu'?'પેપર યાદી હાલમાં અપડેટ થઈ શકી નથી. જાણીતા પેપર બતાવવામાં આવે છે; પછી ફરી પ્રયાસ કરો.':'The paper list could not be updated. Showing known papers; please try again later.'}</p>` : '';
  const paperEntries = code => paperIndex?.[code] || [];
  function paperCards(code, entries) {
    return entries.map(p=>`<a class="subject-card" href="#/paper/${encodeURIComponent(code)}/${encodeURIComponent(p.session)}"><div class="subject-meta"><span>${esc(paperSessionTitle(p.session))}</span><span class="subject-code">${esc(code)}</span></div><h3>${lang==='gu'?'ઉકેલેલું પ્રશ્નપત્ર':'Solved question paper'}</h3><div class="subject-foot"><span>${esc(text(subjectMeta(code)?.name)||legacyPaperNames[code]||code)}</span><strong>${lang==='gu'?'વાંચો':'Read'} ↗</strong></div></a>`).join('');
  }
  function showPapers() {
    const entries=Object.entries(paperIndex||{}).flatMap(([code,papers])=>papers.map(p=>({code,p})));
    const title=tr('papers');
    const description=lang==='gu'?'વિષય અને પરીક્ષા પ્રમાણે ઉકેલેલા પેપર વાંચો.':'Read solved papers by subject and exam.';
    return `${shell(title,description,[{label:title}])}<section class="page-content"><div class="wrap">${paperListNotice()}${entries.length?`<div class="subject-grid">${entries.map(({code,p})=>paperCards(code,[p])).join('')}</div>`:empty(lang==='gu'?'હજુ કોઈ પેપર નથી':'No papers yet',lang==='gu'?'નવા પેપર અહીં ઉમેરાશે.':'New papers will appear here.',false)}</div></section>`;
  }
  const branches = () => Array.isArray(catalog?.branches) ? catalog.branches : [];
  const subjectMeta = code => catalog?.subjects?.[code];
  const allSubjects = () => Object.values(catalog?.subjects || {});
  const readyInBranch = (branch) => Object.values(branch.semesters || {}).flat().filter(code => subjectMeta(code)?.status === 'available').length;
  const whereIs = code => { for (const b of branches()) for (const [s,codes] of Object.entries(b.semesters || {})) if (Array.isArray(codes) && codes.includes(code)) return [b,s]; return null; };
  const url = (path, hash) => `data/${path.split('/').map(encodeURIComponent).join('/')}${hash ? `?h=${encodeURIComponent(hash)}` : ''}`;
  async function fetchJson(path) {
    const hash = catalog?.files?.[path];
    const response = await fetch(url(path, hash), {cache:'default'});
    if (!response.ok) throw new Error(`Could not load ${path}`);
    return response.json();
  }
  async function loadCatalog() {
    const response = await fetch(`data/catalog.json?t=${Math.floor(Date.now()/60000)}`, {cache:'no-cache'});
    if (!response.ok) throw new Error('Catalog unavailable');
    const value = await response.json();
    if (!Array.isArray(value.branches) || !value.subjects || typeof value.subjects !== 'object') throw new Error('Invalid catalog');
    catalog = value;
  }
  function announce(message) { toast.textContent = message; toast.classList.add('visible'); clearTimeout(toastTimer); toastTimer=setTimeout(()=>toast.classList.remove('visible'),2300); }
  function shell(title, subtitle, crumbs = []) {
    const trail = [{label:tr('home'),href:'#/'}, ...crumbs];
    return `<section class="page-hero"><div class="wrap"><div class="breadcrumb">${trail.map((c,i)=>`${i?'<span>/</span>':''}${c.href?`<a href="${esc(c.href)}">${esc(c.label)}</a>`:`<span aria-current="page">${esc(c.label)}</span>`}`).join('')}</div><h1 class="page-title">${esc(title)}</h1><p class="page-subtitle">${esc(subtitle)}</p></div></section>`;
  }
  function branchCard(b) {
    const n=readyInBranch(b);
    return `<a class="branch-card" href="#/branch/${encodeURIComponent(b.key)}"><div class="branch-top"><span class="branch-icon">${icon(b.icon)}</span><span class="branch-arrow">↗</span></div><h3>${esc(text(b.name))}</h3><p>${esc(tr('branch'))} ${esc(b.code)}</p><div class="branch-bottom"><span><i class="dot ${n?'':'soon'}"></i>${n?`${n} ${esc(tr('ready'))}`:esc(tr('coming'))}</span><b>→</b></div></a>`;
  }
  function subjectCard(m) {
    const location=whereIs(m.code), subtitle=location ? `${tr('semester')} ${location[1]} · ${text(location[0].name)}` : (m.category || '');
    const available=m.status==='available';
    return `<a class="subject-card" href="#/subject/${encodeURIComponent(m.code)}"><div class="subject-meta"><span>${esc(available?tr('available'):tr('notYet'))}</span><span class="subject-code">${esc(m.code)}</span></div><h3>${esc(text(m.name))}</h3><div class="subject-foot"><span>${esc(subtitle)}</span><strong>${available?`${esc(m.units || 0)} ${esc(tr('units'))} ↗`:'↗'}</strong></div></a>`;
  }
  function searchBox(placeholder, value='') { return `<div class="search-box">${icon('search')}<label class="sr-only" for="search-input">${esc(placeholder)}</label><input id="search-input" type="search" autocomplete="off" placeholder="${esc(placeholder)}" value="${esc(value)}"></div>`; }
  function showHome() {
    const ready=branches().filter(b=>readyInBranch(b)>0), subjects=allSubjects().filter(s=>s.status==='available');
    const preferred=['DI01000131','DI03000021','DI01000191','DI01000081','DI01005011','DI02000101'];
    const picks=preferred.map(subjectMeta).filter(x=>x?.status==='available');
    for (const s of subjects) { if (picks.length>=6) break; if(!picks.includes(s)) picks.push(s); }
    return `<section class="hero"><div class="wrap hero-inner"><div class="hero-copy"><div class="eyebrow">${esc(tr('heroEye'))}</div><h1>${tr('heroTitle')}</h1><p>${esc(tr('heroText'))}</p><div class="hero-actions"><a href="#/branches" class="button-primary large">${esc(tr('browse'))} <span>↗</span></a><a href="#/search" class="button-text">${esc(tr('find'))} →</a></div></div><div class="hero-image"><img src="assets/study-illustration.webp" alt="Students studying engineering together" fetchpriority="high"></div><span class="hero-sparkle" aria-hidden="true">✳</span><div class="hero-note"><span class="hero-note-icon">${icon('school')}</span><span><b>${esc(tr('heroBadge'))}</b>${esc(tr('heroBadgeSmall'))}</span></div></div></section>
    <div class="trust-strip"><div class="wrap trust-inner">${[['school','trust1','trust1s'],['globe','trust2','trust2s'],['book','trust3','trust3s'],['heart','trust4','trust4s']].map(([ic,a,b])=>`<div class="trust-item"><span class="trust-icon">${icon(ic)}</span><span><b>${esc(tr(a))}</b>${esc(tr(b))}</span></div>`).join('')}</div></div>
    <section class="section"><div class="wrap"><div class="section-heading"><div><div class="eyebrow">${esc(tr('chooseEye'))}</div><h2>${esc(tr('choose'))}</h2><p>${esc(tr('chooseText'))}</p></div><a href="#/branches" class="section-link">${esc(tr('viewAll'))} ↗</a></div><div class="branch-grid">${ready.slice(0,4).map(branchCard).join('')}</div></div></section>
    <section class="section how-section"><div class="wrap how-grid"><div class="how-heading"><div class="eyebrow">${esc(tr('howEye'))}</div><h2>${tr('howTitle')}</h2><p>${esc(tr('howText'))}</p><a href="#/branches" class="button-text">${esc(tr('browse'))} →</a></div><div class="steps">${[1,2,3].map(i=>`<div class="step"><span class="step-number">0${i}</span><div><b>${esc(tr('step'+i))}</b><p>${esc(tr('step'+i+'s'))}</p></div></div>`).join('')}</div></div></section>
    <section class="section section-white"><div class="wrap"><div class="section-heading"><div><div class="eyebrow">${esc(tr('exploreEye'))}</div><h2>${esc(tr('explore'))}</h2><p>${esc(tr('exploreText'))}</p></div><a class="section-link" href="#/search">${esc(tr('viewSubjects'))} ↗</a></div><div class="subject-grid">${picks.map(subjectCard).join('')}</div></div></section>
    <section class="section"><div class="wrap"><div class="cta-band"><div><h2>${esc(tr('ctaTitle'))}</h2><p>${esc(tr('ctaText'))}</p></div><a class="button-light" href="https://github.com/Sunilpa4/diplomaone-content/releases/latest" target="_blank" rel="noopener noreferrer">${esc(tr('download'))} <span>↗</span></a></div></div></section>`;
  }
  function showBranches() {
    return `${shell(tr('branchesTitle'),tr('branchesText'),[{label:tr('allBranches')}])}<section class="page-content"><div class="wrap"><div class="filter-bar">${searchBox(tr('searchBranches'))}<span class="result-count" id="result-count"></span></div><div class="branch-grid" id="results"></div></div></section>`;
  }
  function bindBranchSearch() {
    const input=document.querySelector('#search-input'), results=document.querySelector('#results'), count=document.querySelector('#result-count');
    const list=branches().slice().sort((a,b)=>Number(readyInBranch(b)>0)-Number(readyInBranch(a)>0));
    const update=()=>{const q=input.value.trim().toLocaleLowerCase();const found=list.filter(b=>`${b.name?.en||''} ${b.name?.gu||''} ${b.code||''}`.toLocaleLowerCase().includes(q)); count.textContent=`${found.length} ${tr('result')}`;results.innerHTML=found.length?found.map(branchCard).join(''):`<div class="empty-state"><h3>${esc(tr('noBranches'))}</h3><p>${esc(tr('noSearch'))}</p></div>`;}; input.addEventListener('input',update);update();
  }
  function showBranch(key) {
    const b=branches().find(x=>x.key===key); if(!b) return missing();
    return `${shell(text(b.name),tr('semesterText'),[{label:tr('allBranches'),href:'#/branches'},{label:text(b.name)}])}<section class="page-content"><div class="wrap"><div class="section-heading"><div><div class="eyebrow">${esc(tr('branch'))} ${esc(b.code)}</div><h2>${esc(tr('semesters'))}</h2></div></div><div class="semester-list">${[1,2,3,4,5,6].map(s=>{const codes=b.semesters?.[String(s)]||[], n=codes.filter(c=>subjectMeta(c)?.status==='available').length;return `<a class="semester-card" href="#/branch/${encodeURIComponent(key)}/${s}"><span class="semester-number">${s}</span><h3>${esc(tr('semester'))} ${s}</h3><p>${codes.length?`${codes.length} ${esc(tr('subjects'))}`:esc(tr('coming'))}</p><span class="branch-bottom">${n?`${n} ${esc(tr('ready'))}`:esc(tr('notYet'))} &nbsp; →</span></a>`}).join('')}</div></div></section>`;
  }
  function showSemester(key,sem) {
    const b=branches().find(x=>x.key===key); if(!b || !/^[1-6]$/.test(sem)) return missing();
    const list=(b.semesters?.[sem]||[]).map(subjectMeta).filter(Boolean).sort((a,b)=>Number(b.status==='available')-Number(a.status==='available'));
    return `${shell(`${tr('semester')} ${sem}`,tr('subjectListText'),[{label:tr('allBranches'),href:'#/branches'},{label:text(b.name),href:`#/branch/${encodeURIComponent(key)}`},{label:`${tr('semester')} ${sem}`}])}<section class="page-content"><div class="wrap"><div class="section-heading"><div><div class="eyebrow">${esc(text(b.name))}</div><h2>${esc(tr('subjectList'))}</h2></div></div>${list.length?`<div class="subject-grid">${list.map(subjectCard).join('')}</div>`:empty(tr('emptyTitle'),tr('emptyText'))}</div></section>`;
  }
  function empty(title, description, button=true) { return `<div class="empty-state"><h3>${esc(title)}</h3><p>${esc(description)}</p>${button?`<a href="#/branches" class="button-primary">${esc(tr('exploreBranches'))} →</a>`:''}</div>`; }
  function missing() { return `${shell(tr('loadError'),tr('loadErrorText'))}<section class="page-content"><div class="wrap">${empty(tr('loadError'),tr('loadErrorText'))}</div></section>`; }
  function showSearch() { return `${shell(tr('searchTitle'),tr('searchText'),[{label:tr('search')}])}<section class="page-content"><div class="wrap"><div class="filter-bar">${searchBox(tr('searchSubjects'))}<span class="result-count" id="result-count"></span></div><div id="results"></div></div></section>`; }
  function bindSubjectSearch() {
    const input=document.querySelector('#search-input'),results=document.querySelector('#results'),count=document.querySelector('#result-count');
    const update=()=>{const q=input.value.trim().toLocaleLowerCase();if(!q){count.textContent='';results.innerHTML=empty(tr('searchPrompt'),tr('searchPromptText'),false);return;}const found=allSubjects().filter(s=>`${s.code||''} ${s.alt_code||''} ${s.name?.en||''} ${s.name?.gu||''}`.toLocaleLowerCase().includes(q)).sort((a,b)=>Number(b.status==='available')-Number(a.status==='available'));count.textContent=`${found.length} ${tr('result')}`;results.innerHTML=found.length?`<div class="subject-grid">${found.map(subjectCard).join('')}</div>`:empty(tr('noSubjects'),tr('noSearch'),false);};input.addEventListener('input',update);update();
  }
  function showSaved() {
    const cards=saved.map(item=>{const meta=subjectMeta(item.code);if(!meta)return '';return `<a class="subject-card" href="#/unit/${encodeURIComponent(item.code)}/${Number(item.unit)}"><div class="subject-meta"><span>${esc(tr('read'))}</span><span class="subject-code">${esc(item.code)}</span></div><h3>${esc(tr('semester')==='Semester'?'Unit':'એકમ')} ${Number(item.unit)} · ${esc(text(item.title))}</h3><div class="subject-foot"><span>${esc(text(meta.name))}</span><strong>↗</strong></div></a>`}).filter(Boolean);
    return `${shell(tr('savedTitle'),tr('savedText'),[{label:tr('saved')}])}<section class="page-content"><div class="wrap">${cards.length?`<div class="subject-grid">${cards.join('')}</div>`:empty(tr('savedEmpty'),tr('savedEmptyText'))}</div></section>`;
  }
  function showSubject(s, meta) {
    const location=whereIs(s.code), available=new Set(s.available_units||[]), units=Array.isArray(s.units)?s.units:[];
    const crumbs=[{label:tr('allBranches'),href:'#/branches'}]; if(location)crumbs.push({label:text(location[0].name),href:`#/branch/${encodeURIComponent(location[0].key)}`},{label:`${tr('semester')} ${location[1]}`,href:`#/branch/${encodeURIComponent(location[0].key)}/${location[1]}`});crumbs.push({label:text(s.name)});
    return `${shell(text(s.name),`${s.code} · ${meta?.category || s.category || ''}`,crumbs)}<section class="page-content"><div class="wrap">${paperListNotice()}${paperEntries(s.code).length?`<div class="section-heading"><div><div class="eyebrow">EXAM PREPARATION</div><h2>${esc(tr('papers'))}</h2><p>${lang==='gu'?'વિષયના ઉકેલેલા પ્રશ્નપત્રો.':'Solved question papers for this subject.'}</p></div></div><div class="subject-grid">${paperCards(s.code,paperEntries(s.code))}</div>`:''}<div class="section-heading"><div><div class="eyebrow">${esc(tr('read'))}</div><h2>${esc(tr('unitsTitle'))}</h2><p>${esc(tr('unitsText'))}</p></div></div><div class="subject-grid">${units.map(u=>`<${available.has(u.no)?'a':'div'} class="subject-card" ${available.has(u.no)?`href="#/unit/${encodeURIComponent(s.code)}/${Number(u.no)}"`:''}><div class="subject-meta"><span>${lang==='gu'?'એકમ':'UNIT'} ${Number(u.no)}</span><span class="subject-code">${available.has(u.no)?esc(tr('available')):esc(tr('notYet'))}</span></div><h3>${esc(text(u.title))}</h3><div class="subject-foot"><span>${u.hours?`${esc(u.hours)} ${esc(tr('hours'))}`:''}${u.weightage?` · ${esc(u.weightage)}%`:''}</span><strong>${available.has(u.no)?`${esc(tr('viewUnit'))} ↗`:' '}</strong></div></${available.has(u.no)?'a':'div'}>`).join('')}</div>${units.length?'':empty(tr('emptyTitle'),tr('emptyText'))}</div></section>`;
  }
  // Build an inert image from a restricted SVG tree. Never inject remote SVG/JS.
  function paperDiagram(source) {
    const svgNS='http://www.w3.org/2000/svg';
    const tags=new Set(['svg','defs','marker','path','line','rect','circle','text']);
    const attrs=new Set(['viewBox','width','height','x','y','x1','y1','x2','y2','cx','cy','r','rx','d','fill','stroke','stroke-width','stroke-dasharray','font-size','text-anchor','id','refX','refY','markerWidth','markerHeight','orient','marker-end','role','aria-label']);
    function copy(node) {
      if(node.nodeType===3)return document.createTextNode(node.nodeValue);
      if(node.nodeType!==1||node.namespaceURI!==svgNS||!tags.has(node.localName))return null;
      const out=document.createElementNS(svgNS,node.localName);
      for(const a of node.attributes) {
        if(!attrs.has(a.name))continue;
        if(a.name==='marker-end'&&!/^url\(#[A-Za-z0-9_-]+\)$/.test(a.value))continue;
        if(a.name==='id'&&!/^[A-Za-z0-9_-]+$/.test(a.value))continue;
        if(a.name!=='marker-end'&&/url\s*\(|javascript:|data:/i.test(a.value))continue;
        out.setAttribute(a.name,a.value);
      }
      if(node.localName==='text'&&node.classList.contains('svg-title')){out.setAttribute('font-size','14');out.setAttribute('font-weight','700');}
      if(node.localName==='text'&&node.classList.contains('svg-sub'))out.setAttribute('font-size','10');
      for(const child of node.childNodes){const safe=copy(child);if(safe)out.appendChild(safe);}
      return out;
    }
    const svg=copy(source);if(!svg)return null;
    svg.setAttribute('xmlns',svgNS);
    const img=document.createElement('img');
    img.setAttribute('alt',source.getAttribute('aria-label')||'Diagram');
    img.setAttribute('loading','lazy');
    img.setAttribute('src','data:image/svg+xml;charset=utf-8,'+encodeURIComponent(new XMLSerializer().serializeToString(svg)));
    return img;
  }
  // Copy only presentational nodes and selected math classes from remote papers.
  // Event handlers, scripts, URLs, forms and source CSS are never inserted.
  function sanitizePaper(html, language) {
    const source=new DOMParser().parseFromString(html,'text/html');
    const main=source.querySelector('main');
    if(!main||!main.querySelector('details'))throw new Error('Invalid paper format');
    const tags=new Set(['MAIN','SECTION','H2','H3','P','DIV','SPAN','STRONG','B','EM','I','U','SMALL','SUB','SUP','UL','OL','LI','BR','DETAILS','SUMMARY','FIGURE','FIGCAPTION','IMG','TABLE','THEAD','TBODY','TR','TH','TD']);
    const blocked=new Set(['SCRIPT','STYLE','IFRAME','OBJECT','EMBED','FORM','INPUT','BUTTON','LINK','META','VIDEO','AUDIO']);
    const classes=new Set(['card','answer','note','eq','frac','num','den','result','paper-figure']);
    function copy(node) {
      if(node.nodeType===3)return document.createTextNode(node.nodeValue);
      if(node.nodeType!==1)return null;
      if((node.classList.contains('en')&&language!=='en')||(node.classList.contains('gu')&&language!=='gu'))return null;
      if(node.namespaceURI==='http://www.w3.org/2000/svg')return node.localName==='svg'?paperDiagram(node):null;
      if(blocked.has(node.tagName))return null;
      const out=tags.has(node.tagName)?document.createElement(node.localName):document.createDocumentFragment();
      if(node.tagName==='IMG') {
        const src=node.getAttribute('src')||'';
        if(src.length>1200000||!/^data:image\/(png|jpeg|gif|webp);base64,[a-z0-9+/=\s]+$/i.test(src))return null;
        out.setAttribute('src',src);out.setAttribute('alt',node.getAttribute('alt')||'Paper figure');out.setAttribute('loading','lazy');
      }
      if(tags.has(node.tagName)) {
        const names=[...node.classList].filter(c=>classes.has(c));if(names.length)out.className=names.join(' ');
      }
      for(const child of node.childNodes){const safe=copy(child);if(safe)out.appendChild(safe);}
      return out;
    }
    const holder=document.createElement('div'), cleaned=copy(main);
    if(!cleaned)throw new Error('Invalid paper content');
    holder.appendChild(cleaned);return holder.innerHTML;
  }
  async function showPaper(code, session, meta, entry) {
    const key=`${code}/${session}`;
    let html=paperCache.get(key);
    if(!html) {
      const response=await fetch(`${paperBase}/${encodeURIComponent(code)}/${session}.html?t=${Math.floor(Date.now()/60000)}`,{cache:'no-cache',redirect:'error'});
      if(!response.ok)throw new Error('Could not load solved paper');
      html=await response.text();if(html.length>3000000)throw new Error('Paper too large');
      paperCache.set(key,html);
    }
    const title=lang==='gu'?'ઉકેલેલું પ્રશ્નપત્ર':'Solved question paper';
    // For older shared PDF names, only link the file if the paper explicitly
    // names it; do not associate one exam's PDF with a different exam.
    const legacyLinked=entry?.legacyPdf && [...new DOMParser().parseFromString(html,'text/html').querySelectorAll('a[href]')].some(a=>/^(?:\.\/)?Question_Paper\.pdf$/i.test(a.getAttribute('href')));
    const pdfName=entry?.pdf||(legacyLinked?'Question_Paper.pdf':null);
    const pdf=pdfName?`${paperBase}/${encodeURIComponent(code)}/${encodeURIComponent(pdfName)}`:'';
    const name=text(meta?.name)||legacyPaperNames[code]||code, back=meta?`#/subject/${encodeURIComponent(code)}`:'#/papers';
    return `${shell(title,`${name} · ${code} · ${paperSessionTitle(session)}`,[{label:tr('papers'),href:'#/papers'},{label:name,href:back},{label:title}])}<section class="page-content"><div class="wrap"><div class="paper-toolbar"><a class="button-text" href="${esc(back)}">← ${esc(tr('back'))}</a>${pdf?`<a class="button-text" href="${esc(pdf)}" target="_blank" rel="noopener noreferrer">${lang==='gu'?'મૂળ પ્રશ્નપત્ર (PDF)':'Original question paper (PDF)'} ↗</a>`:''}</div><article class="reader-card solved-paper">${sanitizePaper(html,lang)}</article></div></section>`;
  }
  // Only allow inert, presentational markup from note content. Never execute source HTML or SVG.
  function safeHtml(value) {
    const template=document.createElement('template'); template.innerHTML=text(value);
    const allowed=new Set(['P','BR','STRONG','B','EM','I','U','S','SMALL','SUB','SUP','UL','OL','LI','H3','H4','H5','H6','DIV','SPAN','BLOCKQUOTE','PRE','CODE','TABLE','THEAD','TBODY','TFOOT','TR','TH','TD','IMG','HR']);
    const blocked=new Set(['SCRIPT','STYLE','IFRAME','OBJECT','EMBED','SVG','MATH','FORM','INPUT','BUTTON','LINK','META','VIDEO','AUDIO']);
    function clean(parent) { for(const node of [...parent.childNodes]) { if(node.nodeType===Node.COMMENT_NODE){node.remove();continue;} if(node.nodeType!==Node.ELEMENT_NODE)continue; if(blocked.has(node.tagName)){node.remove();continue;} if(!allowed.has(node.tagName)){clean(node);node.replaceWith(...node.childNodes);continue;} for(const a of [...node.attributes]) { const keep=(node.tagName==='P' && a.name==='class' && a.value==='result') || (node.tagName==='IMG' && (a.name==='alt'||a.name==='title'||(a.name==='src'&&/^data:image\/(png|jpeg|gif|webp);base64,[a-z0-9+/=\s]+$/i.test(a.value)))); if(!keep)node.removeAttribute(a.name); } if(node.tagName==='IMG'&&!node.getAttribute('src')){node.remove();continue;} clean(node); } }
    clean(template.content);return template.innerHTML;
  }
  function diagram(unit,id,title) {
    const svg=unit.svgs?.[id]; if(typeof svg!=='string' || !svg.trim().startsWith('<svg'))return '';
    const src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg);
    return `<figure class="diagram-frame"><img loading="lazy" src="${esc(src)}" alt="${esc(title||id)}"><figcaption>${esc(title||id)}</figcaption></figure>`;
  }
  function card(title,body,open=false) { return `<details class="note-card" ${open?'open':''}><summary>${esc(title || tr('read'))}</summary><div class="note-body">${body}</div></details>`; }
  function qaItem(item,i) {
    const q=text(item.q||item.question||item.title)||`${tr('question')} ${i+1}`;
    const a=text(item.a||item.answer||item.body);
    const marks=item.marks ? ` <span>(${esc(item.marks)} ${esc(tr('marks'))})</span>` : '';
    return a?card(q, safeHtml(a)): `<div class="note-card"><div class="note-body" style="padding:15px 17px">${esc(q)}${marks}</div></div>`;
  }
  function groupCards(list,unit,type) {
    return list.map((group,gi)=>{
      const items=Array.isArray(group.items)?group.items:null;
      if(items) {
        let inner=items.map((item,i)=>{
          if(type==='viva'||type==='exam'||type==='numericals')return qaItem(item,i);
          if(type==='notes') { const title=text(item.h||item.title||item.q)||`${tr('read')} ${i+1}`; const body=safeHtml(item.body||item.a||''); const examples=(Array.isArray(item.examples)?item.examples:[]).map(id=>{const n=(unit.numericals||[]).find(x=>x.id===id);return n?`<h4>${esc(tr('numericals'))}: ${esc(text(n.q))}</h4>${safeHtml(n.a)}`:'';}).join(''); const programs=(Array.isArray(item.programs)?item.programs:[]).map(id=>{const p=(unit.programs||[]).find(x=>x.id===id);return p?`<h4>${esc(text(p.title))}</h4><pre class="code-output">${esc(text(p.code))}</pre>${p.out?`<pre class="code-output">${esc(text(p.out))}</pre>`:''}${p.expl?safeHtml(p.expl):''}`:'';}).join(''); return card(title,body+(item.diagram?diagram(unit,item.diagram,title):'')+examples+programs,false); }
          const title=text(item.name||item.title||item.h)||`${tr(type)} ${i+1}`;
          if(item.body) return card(title,safeHtml(item.body)+(item.diagram?diagram(unit,item.diagram,title):''));
          const formula=text(item.f||item.code), terms=text(item.terms||item.expl);
          const body=(formula?(type==='equations'?`<p><strong>${safeHtml(formula)}</strong></p>`:`<pre class="code-output">${esc(formula)}</pre>`):'')+(terms?`<p>${safeHtml(terms)}</p>`:'');
          return card(title,body);
        }).join('');
        return `<section class="note-section">${group.title?`<h3>${esc(text(group.title))}</h3>`:''}${inner}</section>`;
      }
      if(type==='viva'||type==='exam'||type==='numericals')return qaItem(group,gi);
      if(type==='programs') {
        const title=text(group.title||group.name)||`${tr('programs')} ${gi+1}`;
        const code=text(group.code),out=text(group.out||group.output),expl=text(group.expl||group.explanation);
        return card(title,`${code?`<h4>${esc(tr('code'))}</h4><pre class="code-output">${esc(code)}</pre>`:''}${out?`<h4>${esc(tr('output'))}</h4><pre class="code-output">${esc(out)}</pre>`:''}${expl?`<h4>${esc(tr('explanation'))}</h4>${safeHtml(expl)}`:''}`);
      }
      if(type==='diagrams'||type==='flowcharts')return diagram(unit,group.id,text(group.title));
      if(group.body||group.content)return card(text(group.title||group.h),safeHtml(group.body||group.content));
      return '';
    }).join('');
  }
  function unitTabs(unit) {
    const tabs=unit.content_kind==='theory_trimmed_civil' && Array.isArray(unit.equations) ? ['notes','diagrams','numericals','equations','viva','exam'] : ['notes','programs','diagrams','flowcharts','equations','numericals','syntax','algorithms','viva','exam','sources'];
    return tabs.filter(k=>Array.isArray(k==='exam'?(unit.exam_questions||unit.exam):unit[k]) && (k==='exam'?(unit.exam_questions||unit.exam):unit[k]).length);
  }
  function sourceList(sources) {
    const items=sources.map(source=>{
      if(typeof source==='string') return `<li>${esc(source)}</li>`;
      if(!source || typeof source!=='object') return '';
      const title=text(source.title||source.name||source.reference||source.file);
      if(!title) return '';
      let link='';
      if(typeof source.url==='string') {
        try { const parsed=new URL(source.url); if(['https:','http:'].includes(parsed.protocol)) link=parsed.href; } catch (_) { /* Not a URL. */ }
      }
      const label=link?`<a href="${esc(link)}" target="_blank" rel="noopener noreferrer">${esc(title)} ↗</a>`:esc(title);
      const detail=text(source.status||source.authority||source.role||source.use||source.review_status);
      return `<li>${label}${detail?` <small>${esc(detail)}</small>`:''}</li>`;
    }).join('');
    return `<section class="note-section references"><h3>${esc(tr('sources'))}</h3><p>${esc(tr('sourceIntro'))}</p><ul>${items}</ul></section>`;
  }
  function tabContent(unit,tab) {
    if(tab==='sources') return sourceList(unit.sources);
    const content=tab==='exam'?(unit.exam_questions||unit.exam):unit[tab];
    const html=Array.isArray(content)?groupCards(content,unit,tab):'';
    const policy=tab==='exam' ? [text(unit.exam_policy), text(unit.assessment_note), unit.question_marks_are_suggested ? tr('suggestedMarks') : ''].filter(Boolean) : [];
    const notice=policy.length ? `<div class="reader-notice">${policy.map(p=>`<p>${esc(p)}</p>`).join('')}</div>` : '';
    return notice+(html || `<p class="page-subtitle">${esc(tr('noContent'))}</p>`);
  }
  function showUnit(unit,subject) {
    const num=Number(unit.unit), tabs=unitTabs(unit);if(!tabs.includes(activeTab))activeTab=tabs[0]||'notes';
    const exists=saved.some(x=>x.code===subject.code&&Number(x.unit)===num);
    const languages=Array.isArray(unit.languages)?unit.languages:subject.languages;
    const languageNotice=lang==='gu' && Array.isArray(languages) && languages.includes('en') && !languages.includes('gu') ? `<p class="reader-notice">${esc(tr('englishOnly'))}</p>` : '';
    return `${shell(text(subject.name),`${subject.code} · ${lang==='gu'?'એકમ':'Unit'} ${num}`,[{label:tr('subjectList'),href:`#/subject/${encodeURIComponent(subject.code)}`},{label:`${lang==='gu'?'એકમ':'Unit'} ${num}`}])}<section class="page-content"><div class="wrap reader-layout"><aside class="reader-sidebar" aria-label="${esc(tr('unitsTitle'))}"><h3>${esc(tr('unitsTitle'))}</h3>${(subject.units||[]).filter(u=>(subject.available_units||[]).includes(u.no)).map(u=>`<a class="${Number(u.no)===num?'active':''}" href="#/unit/${encodeURIComponent(subject.code)}/${Number(u.no)}">${lang==='gu'?'એકમ':'Unit'} ${Number(u.no)} · ${esc(text(u.title))}</a>`).join('')}</aside><article class="reader-card"><div class="reader-actions"><div><div class="eyebrow">${lang==='gu'?'એકમ':'UNIT'} ${num}</div><h2 class="reader-title">${esc(text(unit.title))}</h2><div class="reader-sub">${esc(text(subject.name))}</div></div><button class="save-button ${exists?'saved':''}" id="save-unit" type="button" aria-pressed="${exists}">${exists?'♥':'♡'} &nbsp;${esc(tr(exists?'savedButton':'save'))}</button></div><div class="reader-tabs" role="tablist" aria-label="${esc(tr('read'))}">${tabs.map(t=>`<button type="button" role="tab" aria-selected="${t===activeTab}" class="${t===activeTab?'active':''}" data-tab="${t}">${esc(unit.content_kind==='theory_trimmed_civil' && Array.isArray(unit.equations) ? ({notes:'Notes',diagrams:'Diagrams',numericals:'Numericals',equations:'Formulae',viva:'Viva',exam:'Exam'}[t] || tr(t)) : tr(t))}</button>`).join('')}</div>${languageNotice}<div id="reader-content" role="tabpanel">${tabContent(unit,activeTab)}</div></article></div></section>`;
  }
  function bindReader(unit,subject) {
    document.querySelectorAll('[data-tab]').forEach(btn=>btn.addEventListener('click',()=>{activeTab=btn.dataset.tab;document.querySelectorAll('[data-tab]').forEach(b=>{const on=b===btn;b.classList.toggle('active',on);b.setAttribute('aria-selected',String(on));});document.querySelector('#reader-content').innerHTML=tabContent(unit,activeTab);}));
    document.querySelector('#save-unit').addEventListener('click',e=>{const num=Number(unit.unit),exists=saved.some(x=>x.code===subject.code&&Number(x.unit)===num);const next=exists?saved.filter(x=>!(x.code===subject.code&&Number(x.unit)===num)):[...saved,{code:subject.code,unit:num,title:unit.title}];if(!writeStore('diplomaone.website.saved',next)){announce('Unable to save on this device.');return;}saved=next;const b=e.currentTarget;b.classList.toggle('saved',!exists);b.setAttribute('aria-pressed',String(!exists));b.innerHTML=`${exists?'♡':'♥'} &nbsp;${esc(tr(exists?'save':'savedButton'))}`;announce(tr(exists?'remove':'savedButton'));});
  }
  function showPrivacy() {
    const gu=lang==='gu';
    const title=gu?'ગોપનીયતા':'Privacy';
    const intro=gu?'તમારા અભ્યાસને સરળ અને ખાનગી રાખવાનો અમારો પ્રયાસ છે.':'A simple explanation of how this website handles information.';
    const sections=gu?[
      ['ખાતા વગર અભ્યાસ', 'આ વેબસાઇટ પર નોટ્સ વાંચવા માટે ખાતું, નામ અથવા ઇમેઇલ જરૂરી નથી.'],
      ['આ ઉપકરણ પર સાચવેલી માહિતી', 'તમારી ભાષા પસંદગી અને સાચવેલા એકમો તમારા બ્રાઉઝરના સ્થાનિક સ્ટોરેજમાં રહે છે. બ્રાઉઝર ડેટા દૂર કરવાથી તે પણ દૂર થશે; તે અન્ય ઉપકરણો સાથે સિંક થતું નથી.'],
      ['હોસ્ટિંગ અને બહારની લિંક્સ', 'GitHub Pages આ સાઇટ અને નોટ્સ હોસ્ટ કરે છે અને સેવા તથા સુરક્ષા માટે IP એડ્રેસ જેવી ટેકનિકલ માહિતી મેળવી શકે છે. પેપરની યાદી GitHub API પરથી મેળવાય છે. Android એપ ડાઉનલોડની લિંક તમને GitHub પર લઈ જાય છે, જ્યાં તેમની પોતાની ગોપનીયતા નીતિ લાગુ પડે છે.'],
      ['Analytics અને જાહેરાતો', 'આ વેબસાઇટ હાલમાં કોઈ analytics અથવા જાહેરાત સેવા ઉમેરતી નથી. જો આ બદલાય, તો આ માહિતી અપડેટ કરવામાં આવશે.']
    ]:[
      ['No account needed', 'You can read notes without creating an account or giving us your name or email address.'],
      ['Stored on this device', 'Your language preference and saved units are stored in your browser’s local storage. Clearing your browser data removes them, and they do not sync across devices.'],
      ['Hosting and external links', 'GitHub Pages hosts this website and its notes and may receive technical information such as IP addresses to operate and secure its service. The paper list is requested from the GitHub API. The Android download link takes you to GitHub, where its own privacy policy applies.'],
      ['Analytics and advertising', 'This website does not currently include an analytics or advertising service. If that changes, this information will be updated.']
    ];
    return `${shell(title,intro,[{label:title}])}<section class="page-content"><div class="wrap"><article class="reader-card">${sections.map(([heading,body])=>`<section class="note-section"><h3>${esc(heading)}</h3><p>${esc(body)}</p></section>`).join('')}</article></div></section>`;
  }
  function updateHeader() {
    document.documentElement.lang=lang;
    document.querySelectorAll('[data-nav]').forEach(a=>a.textContent=tr(a.dataset.nav));
    document.querySelector('.header-cta').innerHTML=`${esc(tr('start'))} <span aria-hidden="true">↗</span>`;
    const mobile=mobileNav.querySelectorAll('a');['home','branches','papers','saved'].forEach((key,i)=>mobile[i].textContent=tr(key));
    langButton.setAttribute('aria-label',lang==='en'?'Switch to Gujarati':'Switch to English');
    langButton.innerHTML=lang==='en'?'ગુ <span>/</span> <strong>EN</strong>':'<strong>ગુ</strong> <span>/</span> EN';
  }
  async function render() {
    const id=++routeCounter;
    const parts=(location.hash.startsWith('#/')?location.hash.slice(2):'').split('/').map(p=>{try{return decodeURIComponent(p)}catch(_){return ''}});
    const [route,arg,sub]=parts; let html='', bind=null;
    main.innerHTML='<div class="loading-page"><span class="spinner" aria-label="Loading"></span></div>';
    try {
      if(!catalog) await loadCatalog();
      if(!route)html=showHome();
      else if(route==='branches'){html=showBranches();bind=bindBranchSearch;}
      else if(route==='branch')html=sub?showSemester(arg,sub):showBranch(arg);
      else if(route==='search'){html=showSearch();bind=bindSubjectSearch;}
      else if(route==='papers'){await loadPaperIndex();html=showPapers();}
      else if(route==='saved')html=showSaved();
      else if(route==='about')html=`${shell(tr('aboutTitle'),tr('aboutText'),[{label:'About'}])}<section class="page-content"><div class="wrap"><div class="reader-card"><p>${esc(tr('aboutNote'))}</p></div></div></section>`;
      else if(route==='privacy')html=showPrivacy();
      else if(route==='subject'&&safeCode(arg)) {
        const meta=subjectMeta(arg);
        if(!meta)html=missing();
        else {
          await loadPaperIndex();
          const subject=meta.status==='available'?await fetchJson(`subjects/${arg}.json`):{code:arg,name:meta.name,units:[],available_units:[]};
          html=showSubject(subject,meta);
        }
      } else if(route==='paper'&&validPaperCode(arg)&&validPaperSession(sub)) {
        await loadPaperIndex();
        const entry=paperEntries(arg).find(p=>p.session===sub);
        html=entry?await showPaper(arg,sub,subjectMeta(arg),entry):missing();
      } else if(route==='unit'&&safeCode(arg)&&/^(?:0|[1-9]\d*)$/.test(sub||'')&&subjectMeta(arg)?.status==='available') {
        const [subject,unit]=await Promise.all([fetchJson(`subjects/${arg}.json`),fetchJson(`units/${arg}_u${sub}.json`)]);
        html=showUnit(unit,subject);bind=()=>bindReader(unit,subject);
      } else html=missing();
      if(id!==routeCounter)return;
      main.innerHTML=html;if(bind)bind();
      document.title=route ? `${main.querySelector('h1')?.textContent || 'Study'} | DiplomaOne`:'DiplomaOne — Your diploma, made simpler';
      document.querySelectorAll('[data-nav]').forEach(a=>a.classList.toggle('active',(route||'home')===a.dataset.nav));
    } catch(error) {
      console.error(error);if(id!==routeCounter)return;
      main.innerHTML=`<div class="error-page"><h1>${esc(tr('loadError'))}</h1><p>${esc(tr('loadErrorText'))}</p><button type="button" id="retry" class="button-primary">${esc(tr('retry'))}</button></div>`;
      document.querySelector('#retry').addEventListener('click',render);
    }
  }
  langButton.addEventListener('click',()=>{lang=lang==='en'?'gu':'en';writeStore('diplomaone.website.lang',lang);updateHeader();render();});
  menuButton.addEventListener('click',()=>{const open=mobileNav.hidden;mobileNav.hidden=!open;menuButton.setAttribute('aria-expanded',String(open));});
  mobileNav.addEventListener('click',e=>{if(e.target.closest('a')){mobileNav.hidden=true;menuButton.setAttribute('aria-expanded','false');}});
  window.addEventListener('hashchange',()=>{activeTab='notes';window.scrollTo(0,0);render();});
  updateHeader();render();
})();
