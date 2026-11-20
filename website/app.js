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
      home:'Home', branches:'Explore branches', papers:'Solved papers', paperSet:'paper set', paperSets:'paper sets', examPrep:'EXAM PREPARATION', saved:'Saved notes', start:'Start learning', search:'Search subjects', allBranches:'All branches',
      heroEye:'A LITTLE HELP FOR YOUR BIG GOALS', heroTitle:'Your diploma,<br><em>made simpler.</em>', heroText:'Thoughtful notes, clear diagrams, and everything you need to feel a little more ready for class and exams.', browse:'Explore your branch', find:'Find a subject', heroBadge:'Made for diploma students', heroBadgeSmall:'Your learning, your pace',
      trust1:'Built for GTU diploma', trust1s:'Study with direction', trust2:'English & Gujarati', trust2s:'Learn your way', trust3:'Notes that make sense', trust3s:'Clear and easy to follow', trust4:'Free to explore', trust4s:'Your study space, always',
      chooseEye:'LET’S FIND YOUR WAY', choose:'Start with your branch', chooseText:'Pick a branch and find the notes made for your journey.', viewAll:'View all branches', ready:'subjects ready', coming:'More notes coming soon', subject:'subject', subjects:'subjects', subjectReady:'subject ready', subjectsReady:'subjects ready', branch:'Branch',
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
      home:'હોમ', branches:'બ્રાન્ચ જુઓ', papers:'ઉકેલેલા પેપર', paperSet:'પેપર સેટ', paperSets:'પેપર સેટ', examPrep:'પરીક્ષા તૈયારી', saved:'સાચવેલી નોટ્સ', start:'અભ્યાસ શરૂ કરો', search:'વિષય શોધો', allBranches:'બધી બ્રાન્ચ',
      heroEye:'તમારા મોટા સપનાઓ માટે નાની મદદ', heroTitle:'તમારો ડિપ્લોમા,<br><em>હવે વધુ સરળ.</em>', heroText:'સરળ નોટ્સ, સ્પષ્ટ આકૃતિઓ અને વર્ગ તથા પરીક્ષાની તૈયારી માટે જરૂરી માર્ગદર્શન.', browse:'તમારી બ્રાન્ચ શોધો', find:'વિષય શોધો', heroBadge:'ડિપ્લોમા વિદ્યાર્થીઓ માટે', heroBadgeSmall:'તમારો અભ્યાસ, તમારી ગતિએ',
      trust1:'GTU ડિપ્લોમા માટે', trust1s:'સાચી દિશામાં અભ્યાસ', trust2:'ગુજરાતી અને અંગ્રેજી', trust2s:'તમારી રીતે શીખો', trust3:'સરળ સમજાય તેવી નોટ્સ', trust3s:'સ્પષ્ટ અને સહેલી', trust4:'મફત અભ્યાસ', trust4s:'તમારી અભ્યાસની જગ્યા',
      chooseEye:'ચાલો તમારી દિશા શોધીએ', choose:'તમારી બ્રાન્ચથી શરૂઆત કરો', chooseText:'તમારી બ્રાન્ચ પસંદ કરો અને તમારી નોટ્સ શોધો.', viewAll:'બધી બ્રાન્ચ જુઓ', ready:'વિષયો તૈયાર', coming:'વધુ નોટ્સ જલ્દી આવશે', subject:'વિષય', subjects:'વિષયો', subjectReady:'વિષય તૈયાર', subjectsReady:'વિષયો તૈયાર', branch:'બ્રાન્ચ',
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
  let accountState={status:window.DiplomaOneAuth?'idle':'unavailable',user:null,busy:null,error:null};
  let connectionState={status:'idle',code:null},connectionGeneration=0;
  let paymentGeneration=0,paymentView={key:null,status:'idle'},purchaseView={uid:null,status:'idle'},privateObserver=null;
  const freePaperCodes=new Set(['DI01000021','DI01000121']);
  const paperPrices=Object.freeze({computer:1900,mechanical:2900,electrical:2900,civil:2900,chemical:3900});
  const isPaymentSite=()=>['https://www.diplomaone.in','https://vermillion-pothos-520a34.netlify.app'].includes(location.origin);
  const isConnectionTestSite=()=>location.origin==='https://vermillion-pothos-520a34.netlify.app';
  const accountLabels={en:{signIn:'Sign in',account:'My account',purchases:'My purchases'},gu:{signIn:'સાઇન ઇન',account:'મારું ખાતું',purchases:'મારી ખરીદી'}};
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
  const legacyPaperNames = {'4351902':'Manufacturing Engineering – III','4351903':'Thermal Engineering – II','4350501':'Mass Transfer - II','4360501':'Chemical Reaction Engineering'};
  // Names from the supplied Civil paper folders where the catalogue has no entry yet.
  const paperOnlyNames = {'DI03006011':'Construction Technology','DI03006021':'Advance Surveying','DI03006031':'Basic Transportation Engineering','DI03006041':'Mechanics of Structures - I','DI03006051':'Soil Engineering'};
  // Cross-list by matching subject title; these are different GTU scheme codes.
  const legacyPaperSubjects = {'4351902':'DI05019011','4351903':'DI05019021','4350501':'DI05005011','4360501':'DI05005031'};
  const validPaperCode = value => /^(?:DI[0-9]{8}|[0-9]{7})(?![\s\S])/.test(value || '');
  const validPaperSession = value => /^[a-z][a-z0-9]*-[0-9]{4}(?![\s\S])/.test(value || '');
  let paperIndex = null, paperIndexPending = null, paperIndexError = false,paperIndexAttemptRoute=null;
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
    const safe=Object.create(null), seen=new Set();
    for(const path of files) {
      const [,code,file]=path.split('/');
      const isHtml=file.endsWith('.html');
      const isSolutionPdf=file.endsWith('.solution.pdf');
      const isMetadata=file.endsWith('.json'); // Private-paper listing, never answer bytes.
      if(!isHtml&&!isSolutionPdf&&!isMetadata)continue;
      const session=isHtml||isMetadata?file.slice(0,-5):file.slice(0,-13);
      if(!validPaperSession(session))continue;
      const key=`${code}/${session}`;
      if(seen.has(key))continue;
      seen.add(key);
      const html=files.has(`papers/${code}/${session}.html`);
      const solutionPdf=files.has(`papers/${code}/${session}.solution.pdf`)?`${session}.solution.pdf`:null;
      (safe[code] ||= []).push({session,pdf:files.has(`papers/${code}/${session}.pdf`)?`${session}.pdf`:null,legacyPdf:files.has(`papers/${code}/Question_Paper.pdf`), ...(html?{}:{pdfOnly:true}), ...(solutionPdf?{solutionPdf}:{})});
    }
    for(const entries of Object.values(safe)) {
      entries.sort((a,b)=>b.session.slice(-4).localeCompare(a.session.slice(-4))||b.session.localeCompare(a.session));
      if(entries.length===1 && entries[0].legacyPdf && !entries[0].pdf)entries[0].pdf='Question_Paper.pdf';
    }
    return safe;
  }
  async function loadPaperIndex() {
    // Once per tab: a refresh reads GitHub again, never a background timer.
    if(paperIndex&&(!paperIndexError||paperIndexAttemptRoute===location.hash))return paperIndex;
    if(paperIndexPending)return paperIndexPending;
    paperIndexAttemptRoute=location.hash;
    paperIndexPending=(async()=>{
      const controller=new AbortController(), timeout=setTimeout(()=>controller.abort(),8000);
      const privateMetadata=isPaymentSite()?fetch('/api/payments/live/config',{cache:'no-store',redirect:'error',signal:controller.signal})
        .then(response=>response.ok?response.json():null).catch(()=>null):Promise.resolve(null);
      try {
        const response=await fetch(paperTreeUrl,{cache:'no-cache',redirect:'error',signal:controller.signal});
        if(!response.ok)throw new Error('Paper list unavailable');
        paperIndex=papersFromTree(await response.json());paperIndexError=false;
      } catch(error) {
        console.error(error);paperIndexError=true;
        // Preserve known metadata on failure; never cache or fall back to paid answers.
        if(!paperIndex)paperIndex=Object.fromEntries(Object.entries(fallbackPapers).map(([code,entries])=>[code,entries.map(p=>({...p}))]));
      }
      // The private catalog does not depend on GitHub being available. One
      // foreground request per tab, no scheduled polling or public answers.
      try{
        const config=await privateMetadata;
        if(config?.mode==='live'&&config.enabled===true&&Array.isArray(config.products)&&config.products.length<=100)
          for(const product of config.products){
            const parts=typeof product?.id==='string'?product.id.split('--'):[];
            if(parts.length!==2||!validPaperCode(parts[0])||!validPaperSession(parts[1])||freePaperCodes.has(parts[0])||
              !Object.hasOwn(paperPrices,product.branch)||product.amount!==paperPrices[product.branch]||product.currency!=='INR')continue;
            const entries=paperIndex[parts[0]]||=([]),existing=entries.find(p=>p.session===parts[1]);
            if(existing)existing.branch=product.branch;else entries.push({session:parts[1],branch:product.branch,private:true});
          }
        for(const entries of Object.values(paperIndex))entries.sort((a,b)=>b.session.slice(-4).localeCompare(a.session.slice(-4))||b.session.localeCompare(a.session));
      }finally{clearTimeout(timeout);}
      return paperIndex;
    })();
    try{return await paperIndexPending;}finally{paperIndexPending=null;}
  }
  const paperSessionTitle = session => session.split('-').map((word,i)=>i?word:word.charAt(0).toUpperCase()+word.slice(1)).join(' ');
  const paperListNotice = () => paperIndexError ? `<p class="reader-notice">${lang==='gu'?'પેપર યાદી હાલમાં અપડેટ થઈ શકી નથી. જાણીતા પેપર બતાવવામાં આવે છે; પછી ફરી પ્રયાસ કરો.':'The paper list could not be updated. Showing known papers; please try again later.'}</p>` : '';
  const paperEntries = code => paperIndex?.[code] || [];
  const subjectPaperGroups = code => [code, ...Object.keys(legacyPaperSubjects).filter(legacy=>legacyPaperSubjects[legacy]===code)]
    .map(paperCode=>({code:paperCode,entries:paperEntries(paperCode)})).filter(group=>group.entries.length);
  const paperSetLabel = count => `${count} ${tr(count===1?'paperSet':'paperSets')}`;
  const subjectCountLabel = count => `${count} ${tr(count===1?'subject':'subjects')}`;
  const readySubjectLabel = count => `${count} ${tr(count===1?'subjectReady':'subjectsReady')}`;
  const paperName = code => text(subjectMeta(code)?.name || subjectMeta(legacyPaperSubjects[code])?.name) || legacyPaperNames[code] || paperOnlyNames[code] || code;
  function listedPaperPrice(code,entry){
    if(Object.hasOwn(paperPrices,entry?.branch))return paperPrices[entry.branch];
    const amounts=new Set(paperLocations(code).map(l=>paperPrices[l.branch.key]).filter(Boolean));
    return amounts.size===1?[...amounts][0]:null; // Never guess between different branch prices.
  }
  const rupees=paise=>'₹'+(paise/100).toLocaleString('en-IN',{maximumFractionDigits:2});
  function paperCards(code, entries) {
    return entries.map(p=>{
      const free=freePaperCodes.has(code),price=listedPaperPrice(code,p);
      const access=free?(lang==='gu'?'મફત':'Free'):price?`${rupees(price)} · ${lang==='gu'?'આ પેપર':'this paper'}`:(lang==='gu'?'લૉક કરેલું':'Locked');
      return `<a class="subject-card" href="#/paper/${encodeURIComponent(code)}/${encodeURIComponent(p.session)}"><div class="subject-meta"><span>${esc(paperSessionTitle(p.session))}${legacyPaperSubjects[code]?(lang==='gu'?' · જૂની યોજના':' · Older scheme'):''}</span><span class="subject-code">${esc(code)}</span></div><h3>${lang==='gu'?'ઉકેલેલું પ્રશ્નપત્ર':'Solved question paper'}</h3><span class="paper-access-label ${free?'is-free':''}">${free?'':'🔒 '}${esc(access)}</span><div class="subject-foot"><span>${esc(paperName(code))}</span><strong>${free?(lang==='gu'?'વાંચો':'Read'):(lang==='gu'?'પેપર જુઓ':'View paper')} ↗</strong></div></a>`;
    }).join('');
  }
  // Use catalog membership, not the Drive folder or a code-prefix guess. A
  // shared subject can belong to several branches/semesters; legacy codes
  // retain their own exam identities under their reviewed related subject.
  function paperLocations(code) {
    const subject=legacyPaperSubjects[code]||code, locations=[];
    for(const branch of branches())for(const [semester,codes] of Object.entries(branch.semesters||{}))
      if(Array.isArray(codes)&&codes.includes(subject))locations.push({branch,semester});
    return locations;
  }
  function renderPaperGroups(groups, showLocation=false) {
    const subjects=new Map();
    for(const group of groups) {
      const subject=legacyPaperSubjects[group.code]||group.code;
      if(!subjects.has(subject))subjects.set(subject,[]);
      subjects.get(subject).push(group);
    }
    return [...subjects].map(([subject,sources])=>{
      const count=sources.reduce((n,g)=>n+g.entries.length,0), locations=paperLocations(subject);
      const allUploaded=subjectPaperGroups(subject).reduce((n,g)=>n+g.entries.length,0);
      const coverage=allUploaded===1?`<p class="paper-coverage-note">${lang==='gu'?'આ વિષય માટે હાલમાં આ એક જ પરીક્ષા સત્ર અપલોડ થયેલું છે. બીજા આપેલા સત્રો ઉમેરાશે ત્યારે અહીં આપમેળે દેખાશે.':'This is the only uploaded exam session currently available for this subject. Other supplied sessions will appear here when added.'}</p>`:'';
      const branchNames=[...new Set(locations.map(l=>text(l.branch.name)))], semesters=[...new Set(locations.map(l=>l.semester))].sort();
      const location=branchNames.length===1?`${branchNames[0]} · ${tr('semester')} ${semesters.join(', ')}`:
        branchNames.length>1?`${lang==='gu'?'સાંઝો વિષય':'Shared subject'} · ${tr('semester')} ${semesters.join(', ')}`:
        (lang==='gu'?'અન્ય આપેલા પેપર':'Other supplied papers');
      return `<section class="paper-subject-group" data-paper-subject="${esc(subject)}"><div class="paper-group-heading"><div>${showLocation?`<p>${esc(location)}</p>`:''}<h3>${esc(paperName(subject))}</h3><span class="subject-code">${esc(subject)}</span></div><strong>${esc(paperSetLabel(count))}</strong></div>${coverage}<div class="subject-grid">${sources.map(g=>paperCards(g.code,g.entries)).join('')}</div></section>`;
    }).join('');
  }
  function paperFilterResults(branchKey='', semester='', query='') {
    const q=query.trim().toLocaleLowerCase(), groups=[];
    for(const [code,entries] of Object.entries(paperIndex||{})) {
      const locations=paperLocations(code);
      if((branchKey||semester)&&!locations.some(l=>(!branchKey||l.branch.key===branchKey)&&(!semester||l.semester===semester)))continue;
      const meta=subjectMeta(legacyPaperSubjects[code]||code);
      const matched=entries.filter(p=>!q||`${code} ${legacyPaperSubjects[code]||''} ${meta?.name?.en||''} ${meta?.name?.gu||''} ${paperName(code)} ${p.session} ${paperSessionTitle(p.session)}`.toLocaleLowerCase().includes(q));
      if(matched.length)groups.push({code,entries:matched});
    }
    const count=groups.reduce((n,g)=>n+g.entries.length,0);
    return {count,html:groups.length?renderPaperGroups(groups,true):empty(lang==='gu'?'કોઈ પેપર મળ્યા નથી':'No matching papers',lang==='gu'?'બીજી બ્રાન્ચ, સેમેસ્ટર અથવા વિષય અજમાવો.':'Try another branch, semester or subject.',false)};
  }
  function showPapers(initialBranch='', initialSemester='') {
    const selectedBranch=branches().some(b=>b.key===initialBranch)?initialBranch:'', selectedSemester=/^[1-6]$/.test(initialSemester)?initialSemester:'';
    const result=paperFilterResults(selectedBranch,selectedSemester),title=tr('papers');
    const description=lang==='gu'?'બ્રાન્ચ અને સેમેસ્ટર પસંદ કરો. દરેક વિષય હેઠળ તેના બધા ઉપલબ્ધ પરીક્ષા સત્રો સાથે બતાવ્યા છે.':'Choose a branch and semester. All supplied exam sessions are grouped together under their subject.';
    return `${shell(title,description,[{label:title}])}<section class="page-content"><div class="wrap">${paperListNotice()}<div class="paper-filter-bar"><label class="paper-filter-field">${esc(tr('branch'))}<select id="paper-branch-filter"><option value="">${esc(tr('allBranches'))}</option>${branches().map(b=>`<option value="${esc(b.key)}" ${b.key===selectedBranch?'selected':''}>${esc(text(b.name))}</option>`).join('')}</select></label><label class="paper-filter-field">${esc(tr('semester'))}<select id="paper-semester-filter"><option value="">${lang==='gu'?'બધા સેમેસ્ટર':'All semesters'}</option>${[1,2,3,4,5,6].map(s=>`<option value="${s}" ${String(s)===selectedSemester?'selected':''}>${esc(tr('semester'))} ${s}</option>`).join('')}</select></label><div class="search-box">${icon('search')}<label class="sr-only" for="paper-search-input">${esc(tr('searchSubjects'))}</label><input id="paper-search-input" type="search" placeholder="${esc(tr('searchSubjects'))}"></div></div><p id="paper-result-count" class="result-count" aria-live="polite">${esc(paperSetLabel(result.count))}</p><div id="paper-results">${result.html}</div></div></section>`;
  }
  function bindPaperFilters() {
    const branch=main.querySelector('#paper-branch-filter'),semester=main.querySelector('#paper-semester-filter'),search=main.querySelector('#paper-search-input');
    const update=()=>{
      const result=paperFilterResults(branch.value,semester.value,search.value);
      main.querySelector('#paper-results').innerHTML=result.html;
      main.querySelector('#paper-result-count').textContent=paperSetLabel(result.count);
    };
    branch.addEventListener('change',update);semester.addEventListener('change',update);search.addEventListener('input',update);
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
  // Resolve papers through the live branch catalog, so PDFs and legacy-scheme papers
  // appear in the semester of their matching subject instead of a hard-coded branch bucket.
  const branchSemesterPaperGroups = (key, sem) => {
    const branch=branches().find(x=>x.key===key), groups=[], seen=new Set();
    for(const code of branch?.semesters?.[sem]||[]) for(const group of subjectPaperGroups(code)) {
      if(seen.has(group.code))continue;
      seen.add(group.code);groups.push(group);
    }
    return groups;
  };
  function showBranch(key) {
    const b=branches().find(x=>x.key===key); if(!b) return missing();
    const semesters=[1,2,3,4,5,6].map(s=>{
      const sem=String(s), codes=b.semesters?.[sem]||[], groups=branchSemesterPaperGroups(key,sem);
      const subjectCount=codes.filter(code=>subjectMeta(code)).length;
      const readyCount=codes.filter(code=>subjectMeta(code)?.status==='available').length;
      const paperCount=groups.reduce((count,group)=>count+group.entries.length,0);
      const details=subjectCount?subjectCountLabel(subjectCount):paperCount?paperSetLabel(paperCount):tr('coming');
      const status=[readyCount?readySubjectLabel(readyCount):'',subjectCount&&paperCount?paperSetLabel(paperCount):'']
        .filter(Boolean).join(' · ')||(paperCount?tr('papers'):tr('notYet'));
      return `<a class="semester-card" href="#/branch/${encodeURIComponent(key)}/${s}"><span class="semester-number">${s}</span><h3>${esc(tr('semester'))} ${s}</h3><p>${esc(details)}</p><span class="branch-bottom">${esc(status)} &nbsp; →</span></a>`;
    }).join('');
    return `${shell(text(b.name),tr('semesterText'),[{label:tr('allBranches'),href:'#/branches'},{label:text(b.name)}])}<section class="page-content"><div class="wrap">${paperListNotice()}<div class="section-heading"><div><div class="eyebrow">${esc(tr('branch'))} ${esc(b.code)}</div><h2>${esc(tr('semesters'))}</h2></div><a class="section-link" href="#/papers/${encodeURIComponent(key)}">${lang==='gu'?'આ બ્રાન્ચના બધા પેપર':'All papers for this branch'} ↗</a></div><div class="semester-list">${semesters}</div></div></section>`;
  }
  function showSemester(key,sem) {
    const b=branches().find(x=>x.key===key); if(!b || !/^[1-6]$/.test(sem)) return missing();
    const list=(b.semesters?.[sem]||[]).map(subjectMeta).filter(Boolean).sort((a,b)=>Number(b.status==='available')-Number(a.status==='available'));
    const paperGroups=branchSemesterPaperGroups(key,sem);
    const subjectSection=list.length?`<div class="section-heading"><div><div class="eyebrow">${esc(text(b.name))}</div><h2>${esc(tr('subjectList'))}</h2></div></div><div class="subject-grid">${list.map(subjectCard).join('')}</div>`:'';
    const paperSection=paperGroups.length?`<div class="section-heading"><div><div class="eyebrow">${esc(tr('examPrep'))}</div><h2>${esc(tr('papers'))}</h2></div><a class="section-link" href="#/papers/${encodeURIComponent(key)}/${sem}">${lang==='gu'?'પેપર શોધો':'Filter papers'} ↗</a></div>${renderPaperGroups(paperGroups)}`:'';
    const emptyState=!list.length&&!paperGroups.length?empty(tr('emptyTitle'),tr('emptyText')):'';
    return `${shell(`${tr('semester')} ${sem}`,tr('subjectListText'),[{label:tr('allBranches'),href:'#/branches'},{label:text(b.name),href:`#/branch/${encodeURIComponent(key)}`},{label:`${tr('semester')} ${sem}`}])}<section class="page-content"><div class="wrap">${paperListNotice()}${subjectSection}${paperSection}${emptyState}</div></section>`;
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
    return `${shell(text(s.name),`${s.code} · ${meta?.category || s.category || ''}`,crumbs)}<section class="page-content"><div class="wrap">${paperListNotice()}${subjectPaperGroups(s.code).length?`<div class="section-heading"><div><div class="eyebrow">${esc(tr('examPrep'))}</div><h2>${esc(tr('papers'))}</h2><p>${lang==='gu'?'વિષયના ઉકેલેલા પ્રશ્નપત્રો.':'Solved question papers for this subject.'}</p></div></div><div class="subject-grid">${subjectPaperGroups(s.code).map(group=>paperCards(group.code,group.entries)).join('')}</div>`:''}<div class="section-heading"><div><div class="eyebrow">${esc(tr('read'))}</div><h2>${esc(tr('unitsTitle'))}</h2><p>${esc(tr('unitsText'))}</p></div></div><div class="subject-grid">${units.map(u=>`<${available.has(u.no)?'a':'div'} class="subject-card" ${available.has(u.no)?`href="#/unit/${encodeURIComponent(s.code)}/${Number(u.no)}"`:''}><div class="subject-meta"><span>${lang==='gu'?'એકમ':'UNIT'} ${Number(u.no)}</span><span class="subject-code">${available.has(u.no)?esc(tr('available')):esc(tr('notYet'))}</span></div><h3>${esc(text(u.title))}</h3><div class="subject-foot"><span>${u.hours?`${esc(u.hours)} ${esc(tr('hours'))}`:''}${u.weightage?` · ${esc(u.weightage)}%`:''}</span><strong>${available.has(u.no)?`${esc(tr('viewUnit'))} ↗`:' '}</strong></div></${available.has(u.no)?'a':'div'}>`).join('')}</div>${units.length?'':empty(tr('emptyTitle'),tr('emptyText'))}</div></section>`;
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
  // An uploaded paper can reference only its own numbered, inert diagram
  // assets. Never resolve arbitrary relative URLs, hosts, SVGs or other papers.
  function paperAssetUrl(source, paper) {
    if(!validPaperCode(paper?.code)||!validPaperSession(paper?.session)||!freePaperCodes.has(paper.code))return '';
    const parts=source.split('/');
    if(parts.length!==2||parts[0]!==`${paper.session}.assets`||!/^\d{4}\.(?:webp|png)$/.test(parts[1]))return '';
    return `${paperBase}/${paper.code}/${paper.session}.assets/${parts[1]}`;
  }
  function privateImageAsset(source,paper){
    if(!paper?.private||typeof source!=='string'||!source||/^[a-z][a-z0-9+.-]*:|^\/|[?#\\]/i.test(source))return '';
    let decoded;try{decoded=decodeURIComponent(source);}catch(_){return '';}
    if(/^[a-z][a-z0-9+.-]*:|^\/|[?#\\]/i.test(decoded))return '';
    const base='https://private.invalid/',resolved=new URL(decoded,new URL(paper.readerPath,base));
    const relative=resolved.pathname.slice(1),asset=paper.assets.find(a=>a.path===relative&&['image/png','image/webp','image/jpeg'].includes(a.mime));
    return asset&&/^[a-f0-9]{64}$/.test(asset.id)?asset.id:'';
  }
  // Copy only presentational nodes and selected math classes from remote papers.
  // Source scripts, event handlers, links, forms and CSS are never inserted.
  function sanitizePaper(html, language, paper) {
    const source=new DOMParser().parseFromString(html,'text/html');
    const main=source.querySelector('main');
    if(!main||!main.querySelector('details'))throw new Error('Invalid paper format');
    const tags=new Set(['MAIN','SECTION','H2','H3','H4','P','DIV','SPAN','STRONG','B','EM','I','U','SMALL','SUB','SUP','UL','OL','LI','BR','DETAILS','SUMMARY','FIGURE','FIGCAPTION','IMG','TABLE','THEAD','TBODY','TFOOT','TR','TH','TD','CODE','PRE','BLOCKQUOTE']);
    const blocked=new Set(['SCRIPT','STYLE','IFRAME','OBJECT','EMBED','FORM','INPUT','BUTTON','LINK','META','VIDEO','AUDIO']);
    const classes=new Set(['card','answer','note','eq','frac','num','den','result','paper-figure','paper-excerpt','paper-erratum','paper-choice-label','paper-question-hint','paper-source-notes']);
    function copy(node) {
      if(node.nodeType===3)return document.createTextNode(node.nodeValue);
      if(node.nodeType!==1)return null;
      if((node.classList.contains('en')&&language!=='en')||(node.classList.contains('gu')&&language!=='gu'))return null;
      if(node.namespaceURI==='http://www.w3.org/2000/svg')return node.localName==='svg'?paperDiagram(node):null;
      if(blocked.has(node.tagName))return null;
      const sourceNotes=node.tagName==='DIV'&&node.classList.contains('paper-source-notes');
      const out=tags.has(node.tagName)?document.createElement(sourceNotes?'details':node.tagName==='MAIN'?'div':node.localName):document.createDocumentFragment();
      if(sourceNotes) {
        const summary=document.createElement('summary');
        summary.className='paper-source-notes-title';
        summary.textContent=language==='gu'?'મૂળ નોંધો, ધારણાઓ અને પરીક્ષાની સૂચનાઓ':'Source notes, assumptions and exam instructions';
        out.appendChild(summary);
      }
      if(node.tagName==='IMG') {
        const sourceUrl=node.getAttribute('src')||'';
        const embedded=sourceUrl.length<=1200000&&/^data:image\/(png|jpeg|gif|webp);base64,[a-z0-9+/=\s]+$/i.test(sourceUrl);
        const privateAsset=paper?.private&&!embedded?privateImageAsset(sourceUrl,paper):'';
        const src=embedded?sourceUrl:paper?.private?'':paperAssetUrl(sourceUrl,paper);
        if(!src&&!privateAsset)return null;
        if(src)out.setAttribute('src',src);else out.setAttribute('data-private-asset',privateAsset);
        out.setAttribute('alt',node.getAttribute('alt')||'Paper figure');out.setAttribute('loading','lazy');
        out.setAttribute('decoding','async');out.setAttribute('referrerpolicy','no-referrer');
        for(const dimension of ['width','height']) {
          const value=node.getAttribute(dimension)||'';
          if(/^[1-9]\d{0,4}$/.test(value)&&Number(value)<=10000)out.setAttribute(dimension,value);
        }
      }
      if(tags.has(node.tagName)) {
        const names=[...node.classList].filter(c=>classes.has(c));
        if(node.tagName==='DETAILS'&&!names.includes('card'))names.push('card');
        if(names.length)out.className=names.join(' ');
        if(node.tagName==='MAIN')out.classList.add('paper-content');
        if(node.classList.contains('en')||node.getAttribute('lang')==='en')out.lang='en';
        if(node.classList.contains('gu')||node.getAttribute('lang')==='gu')out.lang='gu';
        if(['TH','TD'].includes(node.tagName))for(const attr of ['colspan','rowspan']) {
          const value=node.getAttribute(attr)||'';
          if(/^[1-9]\d?$/.test(value)&&Number(value)<=20)out.setAttribute(attr,value);
        }
      }
      for(const child of node.childNodes){const safe=copy(child);if(safe)out.appendChild(safe);}
      return out;
    }
    const holder=document.createElement('div'), cleaned=copy(main);
    if(!cleaned)throw new Error('Invalid paper content');
    holder.appendChild(cleaned);return holder.innerHTML;
  }
  function bindPaperReader() {
    const article=main.querySelector('.solved-paper');if(!article)return;
    if(article.dataset.privateProduct)bindPrivateAssets(article);
    const cards=[...article.querySelectorAll('details.card')];
    main.querySelectorAll('[data-paper-expand]').forEach(button=>button.addEventListener('click',()=>{
      const open=button.dataset.paperExpand==='true';cards.forEach(card=>{card.open=open;});
    }));
    const figures=[...article.querySelectorAll('figure')].filter(figure=>figure.querySelector('img'));
    if(!figures.length)return;
    const dialog=document.createElement('dialog');dialog.className='paper-image-dialog';
    dialog.setAttribute('aria-label',lang==='gu'?'મૂળ ચિત્ર મોટું કરીને વાંચો':'Enlarged source image');
    const toolbar=document.createElement('div');toolbar.className='paper-image-toolbar';
    const hint=document.createElement('span');hint.textContent=lang==='gu'?'જરૂર પડે ત્યાં ચિત્ર સરકાવીને વાંચો.':'Scroll the image to inspect small details.';
    const zoom=document.createElement('button');zoom.type='button';zoom.className='paper-control';
    const close=document.createElement('button');close.type='button';close.className='paper-control';close.textContent=lang==='gu'?'બંધ કરો ×':'Close ×';
    const stage=document.createElement('div');stage.className='paper-image-stage';stage.tabIndex=0;
    const enlarged=document.createElement('img');enlarged.referrerPolicy='no-referrer';stage.appendChild(enlarged);
    const caption=document.createElement('p');caption.className='paper-image-caption';
    toolbar.append(hint,zoom,close);dialog.append(toolbar,stage,caption);article.appendChild(dialog);
    let trigger=null;
    const setZoom=original=>{
      dialog.classList.toggle('at-original-size',original);zoom.setAttribute('aria-pressed',String(original));
      zoom.textContent=lang==='gu'?(original?'પહોળાઈમાં ફિટ કરો':'મૂળ કદમાં વાંચો'):(original?'Fit to width':'Original size');
    };
    close.addEventListener('click',()=>{if(typeof dialog.close==='function')dialog.close();else {dialog.removeAttribute('open');trigger?.focus();}});
    dialog.addEventListener('close',()=>{enlarged.removeAttribute('src');trigger?.focus();});
    dialog.addEventListener('click',event=>{if(event.target===dialog)close.click();});
    dialog.addEventListener('keydown',event=>{if(event.key==='Escape'&&typeof dialog.close!=='function'){event.preventDefault();close.click();}});
    zoom.addEventListener('click',()=>setZoom(!dialog.classList.contains('at-original-size')));
    for(const figure of figures) {
      const img=figure.querySelector('img'),button=document.createElement('button');
      button.type='button';button.className='paper-enlarge paper-control';button.setAttribute('aria-haspopup','dialog');
      button.textContent=lang==='gu'?'ચિત્ર મોટું કરો ↗':'Enlarge image ↗';
      button.addEventListener('click',async()=>{
        if(img.dataset.privateAsset&&!img.getAttribute('src'))await loadPrivateImage(img,article.dataset.privateProduct);
        if(!button.isConnected||!img.getAttribute('src'))return;
        trigger=button;enlarged.src=img.src;enlarged.alt=img.alt;
        caption.textContent=figure.querySelector('figcaption')?.textContent||img.alt;
        setZoom(false);stage.scrollTop=0;stage.scrollLeft=0;
        if(typeof dialog.showModal==='function')dialog.showModal();else dialog.setAttribute('open','');
        close.focus();
      });
      figure.appendChild(button);
    }
  }
  async function showPaper(code, session, meta, entry) {
    if(!validPaperCode(code)||!validPaperSession(session))throw new Error('Invalid paper path');
    const key=`${code}/${session}`,paid=!freePaperCodes.has(code);
    const privateData=paid&&paymentView.key===paymentKey(code,session)&&paymentView.status==='owned'?paymentView.reader:null;
    if(paid&&!privateData)return showLockedPaper(code,session,meta,entry);
    let html=paid?privateData.html:paperCache.get(key);
    if(!paid&&!html && !entry?.pdfOnly) {
      const response=await fetch(`${paperBase}/${encodeURIComponent(code)}/${session}.html?t=${Math.floor(Date.now()/60000)}`,{cache:'no-cache',redirect:'error'});
      if(!response.ok)throw new Error('Could not load solved paper');
      html=await response.text();if(html.length>3000000)throw new Error('Paper too large');
      paperCache.set(key,html);
    }
    const title=lang==='gu'?'ઉકેલેલું પ્રશ્નપત્ર':'Solved question paper';
    // For older shared PDF names, only link the file if the paper explicitly
    // names it; do not associate one exam's PDF with a different exam.
    const legacyLinked=html && entry?.legacyPdf && [...new DOMParser().parseFromString(html,'text/html').querySelectorAll('a[href]')].some(a=>/^(?:\.\/)?Question_Paper\.pdf$/i.test(a.getAttribute('href')));
    const pdfName=entry?.pdf||(legacyLinked?'Question_Paper.pdf':null);
    const pdf=!paid&&pdfName?`${paperBase}/${encodeURIComponent(code)}/${encodeURIComponent(pdfName)}`:'';
    const related=legacyPaperSubjects[code], relatedMeta=subjectMeta(related);
    const name=text(meta?.name)||text(relatedMeta?.name)||legacyPaperNames[code]||paperOnlyNames[code]||code;
    const back=meta?`#/subject/${encodeURIComponent(code)}`:relatedMeta?`#/subject/${encodeURIComponent(related)}`:'#/papers';
    const schemeNotice=related?(lang==='gu'?`આ જૂની યોજનાનું પ્રશ્નપત્ર છે (કોડ ${code}). સમાન વિષયના નામ હેઠળ બતાવ્યું છે; બંને યોજનાના અભ્યાસક્રમ અલગ હોઈ શકે છે.`:`This is an older-scheme paper (code ${code}), listed with a subject of the same name. The syllabuses may differ.`):'';
    const solvedPdf=!paid&&entry?.solutionPdf?`${paperBase}/${encodeURIComponent(code)}/${encodeURIComponent(entry.solutionPdf)}`:'';
    const privateDownloads=paid?privateData.assets.filter(a=>a.mime==='application/pdf').map(a=>`<button type="button" class="paper-control" data-private-download="${esc(a.id)}" data-download-name="${esc(a.path.split('/').pop())}">${esc(a.path.endsWith('.solution.pdf')?(lang==='gu'?'વૈકલ્પિક ઉકેલ PDF':'Optional solution PDF'):(lang==='gu'?'મૂળ પ્રશ્નપત્ર (PDF)':'Original question paper (PDF)'))} ↧</button>`).join(''):'';
    const pdfNotice=lang==='gu'?'આ પેપર માટે પ્રશ્ન-જવાબ કાર્ડ હજુ તૈયાર થયા નથી. ઉપરની વૈકલ્પિક PDF લિંક્સથી મૂળ સામગ્રી વાંચી શકો છો. આ બિનસત્તાવાર અભ્યાસ ઉકેલ છે; જવાબોની સ્વતંત્ર ચકાસણી થઈ નથી. સાઇટનો ભાષા વિકલ્પ PDF નું ભાષાંતર કરતો નથી.':'Question-and-answer cards have not yet been prepared for this paper. The optional PDF links above provide the supplied material. This is an unofficial study solution; answers have not been independently verified. The site language switch does not translate PDF contents.';
    const body=!paid&&entry?.pdfOnly?`<div class="reader-notice"><p>${esc(pdfNotice)}</p></div>`:sanitizePaper(html,lang,paid?{...privateData,private:true,code,session}:{code,session});
    const count=!paid&&entry?.pdfOnly?0:new DOMParser().parseFromString(body,'text/html').querySelectorAll('details.card').length;
    const controls=count?`<div class="paper-controls"><div><strong>${count} ${lang==='gu'?'પ્રશ્ન ભાગો':count===1?'question part':'question parts'}</strong><p>${lang==='gu'?'જવાબ વાંચવા પ્રશ્ન પર ટેપ કરો. પરીક્ષાની વિકલ્પ સૂચનાઓ અનુસરો.':'Tap a question to read its answer. Follow the original exam choice instructions.'}</p></div><div class="paper-control-buttons"><button type="button" class="paper-control" data-paper-expand="true">${lang==='gu'?'બધા ખોલો':'Expand all'}</button><button type="button" class="paper-control" data-paper-expand="false">${lang==='gu'?'બધા બંધ કરો':'Collapse all'}</button></div></div>`:'';
    return `${shell(title,`${name} · ${code} · ${paperSessionTitle(session)}`,[{label:tr('papers'),href:'#/papers'},{label:name,href:back},{label:title}])}<section class="page-content"><div class="wrap paper-wrap"><div class="paper-toolbar"><a class="button-text" href="${esc(back)}">← ${esc(tr('back'))}</a><div class="paper-downloads">${pdf?`<a class="button-text" href="${esc(pdf)}" target="_blank" rel="noopener noreferrer">${lang==='gu'?'મૂળ પ્રશ્નપત્ર (PDF)':'Original question paper (PDF)'} ↗</a>`:''}${solvedPdf?`<a class="button-text" href="${esc(solvedPdf)}" target="_blank" rel="noopener noreferrer">${lang==='gu'?'વૈકલ્પિક ઉકેલ PDF':'Optional solution PDF'} ↗</a>`:''}</div></div>${schemeNotice?`<p class="reader-notice">${esc(schemeNotice)}</p>`:''}${paid?`<div class="private-paper-status"><span>${lang==='gu'?'ખરીદેલું · માત્ર આ પેપર':'Purchased · this paper only'}</span><a href="#/purchases">${esc(accountLabels[lang].purchases)} →</a></div><div class="paper-downloads">${privateDownloads}</div><p id="private-asset-status" role="status" aria-live="polite"></p>`:''}${controls}<article class="reader-card solved-paper" ${paid?`data-private-product="${esc(code+'--'+session)}"`:''}>${body}</article></div></section>`;
  }
  const paymentText=(en,gu)=>lang==='gu'?gu:en;
  const paymentKey=(code,session)=>`${accountState.user?.uid||'signed-out'}:${code}--${session}`;
  const paymentRoute=(code,session)=>`#/paper/${code}/${session}`;
  function resetPayments(){
    ++paymentGeneration;privateObserver?.disconnect();privateObserver=null;
    window.DiplomaOneAuth?.cancelPayments?.();
    paymentView={key:null,status:'idle'};purchaseView={uid:null,status:'idle'};
    // Remove private bytes synchronously on logout/navigation, before another
    // asynchronous render. Received content cannot be made screenshot-proof.
    main.querySelector('[data-private-product]')?.replaceChildren();
  }
  function paymentMessage(code){
    const messages={
      payment_site_required:['Purchases are available on www.diplomaone.in. No payment was started here.','ખરીદી www.diplomaone.in પર ઉપલબ્ધ છે. અહીં કોઈ ચુકવણી શરૂ થઈ નથી.'],
      sign_in_required:['Sign in with Google to buy or read your purchased paper.','પેપર ખરીદવા અથવા ખરીદેલું પેપર વાંચવા Google દ્વારા સાઇન ઇન કરો.'],
      invalid_or_expired_session:['Your session expired. Sign out and sign in again.','તમારું સત્ર પૂરું થયું. સાઇન આઉટ કરીને ફરી સાઇન ઇન કરો.'],
      live_checkout_disabled:['Checkout is not open yet. No payment can be taken for this paper right now.','ચેકઆઉટ હજી શરૂ નથી. આ પેપર માટે અત્યારે ચુકવણી લઈ શકાતી નથી.'],
      backend_not_configured:['Checkout is not open yet. No payment can be taken for this paper right now.','ચેકઆઉટ હજી શરૂ નથી. આ પેપર માટે અત્યારે ચુકવણી લઈ શકાતી નથી.'],
      paper_unavailable:['This paper is not available for new purchases yet. Your other purchases are unchanged.','આ પેપર હજી નવી ખરીદી માટે ઉપલબ્ધ નથી. તમારી બીજી ખરીદી યથાવત્ છે.'],
      private_paper_not_ready:['This paper’s private files are not ready. No payment was started.','આ પેપરની ખાનગી ફાઇલો તૈયાર નથી. કોઈ ચુકવણી શરૂ થઈ નથી.'],
      live_pilot_only:['Purchases are temporarily limited to an approved launch group. No payment was started.','ખરીદી હમણાં મંજૂર કરેલા શરૂઆતના જૂથ માટે જ છે. કોઈ ચુકવણી શરૂ થઈ નથી.'],
      order_limit:['Too many order attempts. Please wait before trying again.','ઓર્ડરના ઘણા પ્રયાસ થયા. ફરી પ્રયાસ પહેલાં રાહ જુઓ.'],
      order_being_created:['An order is already being prepared. Wait, then check My purchases before trying again.','ઓર્ડર તૈયાર થઈ રહ્યો છે. રાહ જોઈને ફરી પ્રયાસ પહેલાં મારી ખરીદી તપાસો.'],
      order_pending_operator_review:['An earlier order needs review. Do not pay again; check My purchases and contact support with your Razorpay receipt.','અગાઉના ઓર્ડરની તપાસ જરૂરી છે. ફરી ચૂકવશો નહીં; મારી ખરીદી તપાસો અને Razorpay રસીદ સાથે સહાય લો.'],
      checkout_closed:['The payment window closed. If money was debited, do not pay again—check My purchases after capture is confirmed.','ચુકવણીની વિન્ડો બંધ થઈ. પૈસા કપાયા હોય તો ફરી ચૂકવશો નહીં—પુષ્ટિ પછી મારી ખરીદી તપાસો.'],
      payment_failed:['The payment attempt was not confirmed. If money was debited, do not pay again; check My purchases and your Razorpay receipt.','ચુકવણીના પ્રયાસની પુષ્ટિ નથી. પૈસા કપાયા હોય તો ફરી ચૂકવશો નહીં; મારી ખરીદી અને Razorpay રસીદ તપાસો.'],
      payment_not_captured_or_mismatch:['Payment has not been confirmed as fully captured. Do not pay again. Refresh My purchases after confirmation.','ચુકવણી સંપૂર્ણ મળી હોવાની પુષ્ટિ નથી. ફરી ચૂકવશો નહીં. પુષ્ટિ પછી મારી ખરીદી ફરી તપાસો.'],
      payment_revoked:['Access for this payment is no longer active. Check your receipt and contact support.','આ ચુકવણીની પરવાનગી સક્રિય નથી. રસીદ તપાસો અને સહાય લો.'],
      checkout_unavailable:['The secure payment window could not open. Check your connection or content blocker.','સુરક્ષિત ચુકવણીની વિન્ડો ખૂલી નથી. ઇન્ટરનેટ અથવા કન્ટેન્ટ બ્લોકર તપાસો.'],
      payment_timeout:['The request timed out; payment status is unknown. If you paid, do not pay again. Refresh My purchases.','વિનંતીનો સમય પૂરો થયો; ચુકવણીની સ્થિતિ અજ્ઞાત છે. ચૂકવ્યું હોય તો ફરી ચૂકવશો નહીં. મારી ખરીદી ફરી તપાસો.'],
      session_changed:['Your account or page changed. Reopen the selected paper using the Google account that paid.','તમારું એકાઉન્ટ કે પેજ બદલાયું. જે Google એકાઉન્ટથી ચૂકવ્યું તેનાથી પેપર ફરી ખોલો.'],
      payments_unavailable:['We could not confirm access right now. If you paid, do not pay again. Refresh My purchases using the same Google account.','અત્યારે પરવાનગીની પુષ્ટિ થઈ શકી નથી. ચૂકવ્યું હોય તો ફરી ચૂકવશો નહીં. એ જ Google એકાઉન્ટથી મારી ખરીદી ફરી તપાસો.']
    };
    return (messages[code]||messages.payments_unavailable)[lang==='gu'?1:0];
  }
  function showLockedPaper(code,session,meta,entry){
    const view=paymentView.key===paymentKey(code,session)?paymentView:{status:'idle'};
    const selected=view.config?.products?.find(p=>p.id===code+'--'+session),price=selected?.amount||listedPaperPrice(code,entry);
    const signedIn=accountState.status==='signed-in'&&!!accountState.user;
    const busy=['loading','buying'].includes(view.status)||!!accountState.busy;
    const ready=signedIn&&view.status==='locked'&&!!selected&&view.config?.enabled===true&&isPaymentSite();
    const name=text(meta?.name)||paperName(code),title=paymentText('Unlock this paper.','આ પેપર અનલૉક કરો.');
    const related=legacyPaperSubjects[code],back=meta?`#/subject/${code}`:related&&subjectMeta(related)?`#/subject/${related}`:'#/papers';
    const schemeNotice=related?paymentText(`This is an older-scheme paper (code ${code}). The original exam identity is unchanged; the related subject’s syllabus may differ.`,`આ જૂની યોજનાનું પેપર છે (કોડ ${code}). મૂળ પરીક્ષાની ઓળખ યથાવત્ છે; સંબંધિત વિષયનો અભ્યાસક્રમ અલગ હોઈ શકે છે.`):'';
    const sessionLabel=paperSessionTitle(session),auth=accountCopy();
    let action;
    if(!isPaymentSite())action=`<p class="reader-notice">${esc(paymentMessage('payment_site_required'))}</p><a class="button-primary" href="https://www.diplomaone.in/${esc(paymentRoute(code,session))}" rel="noreferrer">${paymentText('Open DiplomaOne','DiplomaOne ખોલો')} ↗</a>`;
    else if(!signedIn)action=`<button type="button" id="paper-signin" class="google-signin-button" ${['idle','loading'].includes(accountState.status)||busy?'disabled':''}>${googleMark()}${esc(auth.google)}</button>${accountState.status==='unavailable'?`<button type="button" id="paper-auth-retry" class="paper-control">${esc(auth.retry)}</button>`:''}<p>${esc(paymentMessage('sign_in_required'))}</p>`;
    else action=`<button type="button" id="buy-paper" class="button-primary" data-checkout ${!ready||busy?'disabled':''}>${esc(view.status==='buying'?paymentText('Opening secure payment…','સુરક્ષિત ચુકવણી ખૂલી રહી છે…'):view.status==='loading'?paymentText('Checking your access…','તમારી પરવાનગી તપાસાઈ રહી છે…'):ready?paymentText(`Pay ${rupees(selected.amount)} & unlock`,` ${rupees(selected.amount)} ચૂકવો અને ખોલો`):paymentText('Checkout not available','ચેકઆઉટ ઉપલબ્ધ નથી'))}</button><button type="button" id="paper-access-retry" class="paper-control" ${busy?'disabled':''}>${paymentText('Check access again','પરવાનગી ફરી તપાસો')}</button>`;
    const message=view.message||(signedIn&&!busy&&!ready?'live_checkout_disabled':null);
    return `${shell(title,`${name} · ${code} · ${sessionLabel}`,[{label:tr('papers'),href:'#/papers'},{label:sessionLabel}])}<section class="page-content"><div class="wrap paper-lock-layout" data-paid-paper="${esc(code+'--'+session)}"><article class="account-card paper-lock-card"><div class="account-emblem" aria-hidden="true">${icon('book')}</div><p class="eyebrow">${paymentText('ONE PAPER · ONE PURCHASE','એક પેપર · એક ખરીદી')}</p><h2>${esc(name)}</h2><p class="subject-code">${esc(code)} · ${esc(sessionLabel)}</p>${schemeNotice?`<p class="reader-notice">${esc(schemeNotice)}</p>`:''}<a class="button-text" href="${esc(back)}">← ${esc(tr('back'))}</a><div class="paper-price">${price?esc(rupees(price)):paymentText('Price available at checkout','ચેકઆઉટ પર કિંમત')}<small>${paymentText('for this exam-session paper only','માત્ર આ પરીક્ષા સત્રના પેપર માટે')}</small></div><p>${paymentText('Unlock the existing expandable question-and-answer cards, worked solutions and diagrams for this paper. Notes, Maths-I and Applied Physics remain free.','આ પેપરના પ્રશ્ન-જવાબ કાર્ડ, વિગતવાર ઉકેલ અને આકૃતિઓ અનલૉક કરો. નોટ્સ, Maths-I અને Applied Physics મફત રહે છે.')}</p><div class="paper-purchase-actions">${action}</div><div id="paper-payment-status" role="status" aria-live="polite" tabindex="-1">${message?esc(paymentMessage(message)):''}</div>${accountState.error?`<p role="alert">${esc(auth.errors[accountState.error.code]||auth.fallback)}</p>`:''}</article><aside class="account-sidebar"><div class="account-phase-note"><h3>${paymentText('Only the paper you choose','માત્ર પસંદ કરેલું પેપર')}</h3><p>${paymentText('Your Google account receives access only after the server verifies a fully captured Razorpay payment. A payment screenshot, sign-in or browser setting cannot unlock a paper.','સર્વર Razorpay ની સંપૂર્ણ મળેલી ચુકવણી ચકાસે પછી જ તમારા Google એકાઉન્ટને પરવાનગી મળે છે. સ્ક્રીનશૉટ, સાઇન ઇન કે બ્રાઉઝર સેટિંગથી પેપર ખૂલતું નથી.')}</p></div><div class="account-reading-note"><a class="button-text" href="#/purchases">${esc(accountLabels[lang].purchases)} →</a><p>${paymentText('Already paid? Use the same Google account. Refresh purchases instead of paying twice.','પહેલેથી ચૂકવ્યું છે? એ જ Google એકાઉન્ટ વાપરો. ફરી ચૂકવવાને બદલે ખરીદીની યાદી ફરી તપાસો.')}</p><a href="#/purchase-info">${paymentText('Purchase information & support','ખરીદીની માહિતી અને સહાય')} ↗</a></div></aside></div></section>`;
  }
  function bindPaidPaper(code,session){
    if(freePaperCodes.has(code)||location.hash!==paymentRoute(code,session))return;
    const service=window.DiplomaOneAuth;if(!service||!isPaymentSite())return;
    const key=paymentKey(code,session),uid=accountState.user?.uid||null;
    if(paymentView.key!==key)paymentView={key,status:'idle'};
    const active=()=>paymentView.key===key&&location.hash===paymentRoute(code,session)&&(accountState.user?.uid||null)===uid;
    main.querySelector('#paper-signin')?.addEventListener('click',event=>{if(event.currentTarget.isConnected)service.signIn(lang);});
    main.querySelector('#paper-auth-retry')?.addEventListener('click',()=>service.initialize());
    main.querySelector('#paper-access-retry')?.addEventListener('click',()=>{if(!['loading','buying'].includes(paymentView.status)){paymentView={key,status:'idle'};render();}});
    main.querySelector('#buy-paper')?.addEventListener('click',async event=>{
      if(!event.currentTarget.isConnected||!active()||paymentView.status!=='locked')return;
      const generation=paymentGeneration;paymentView={...paymentView,status:'buying',message:null};render();
      let result;try{result=await service.buyPaper(code+'--'+session);}catch(_){result={ok:false};}
      if(generation!==paymentGeneration||!active())return;
      paymentView=result?.ok===true||result?.code==='already_owned'?{key,status:'idle'}:
        {...paymentView,status:'locked',message:result?.code||'payments_unavailable'};
      await render();main.querySelector('#paper-payment-status')?.focus();
    });
    if(accountState.status==='idle'){service.initialize();return;}
    if(accountState.status!=='signed-in'||accountState.busy||paymentView.status!=='idle')return;
    const generation=paymentGeneration;paymentView={key,status:'loading'};
    // Rendering this loading state must not start another query.
    render();
    Promise.all([service.paymentConfiguration?.(),service.readPurchasedPaper?.(code+'--'+session)]).then(([config,reader])=>{
      if(generation!==paymentGeneration||!active())return;
      paymentView=reader?.ok===true?{key,status:'owned',reader}:
        {key,status:'locked',config:config?.ok===true?config:null,message:reader?.code==='purchase_required'?null:reader?.code||'payments_unavailable'};
      render();
    }).catch(()=>{if(generation===paymentGeneration&&active()){paymentView={key,status:'locked',message:'payments_unavailable'};render();}});
  }
  async function loadPrivateImage(img,id){
    if(!img.isConnected||img.getAttribute('src')||!id)return;
    img.setAttribute('aria-busy','true');
    const generation=paymentGeneration,result=await window.DiplomaOneAuth?.readPurchasedAsset?.(id,img.dataset.privateAsset);
    if(generation!==paymentGeneration||!img.isConnected)return;
    img.removeAttribute('aria-busy');
    if(result?.ok===true&&typeof result.url==='string'&&result.url.startsWith('blob:'))img.src=result.url;
    else {const status=main.querySelector('#private-asset-status');if(status)status.textContent=paymentText('An image could not load. Reopen this paper to retry; no public copy is used.','આકૃતિ લોડ થઈ નથી. ફરી પ્રયાસ માટે પેપર ખોલો; જાહેર નકલ વપરાતી નથી.');}
  }
  function bindPrivateAssets(article){
    const id=article.dataset.privateProduct,images=[...article.querySelectorAll('img[data-private-asset]')];
    privateObserver?.disconnect();
    const visible=img=>{for(let parent=img.parentElement;parent&&parent!==article;parent=parent.parentElement)if(parent.tagName==='DETAILS'&&!parent.open&&!parent.querySelector('summary')?.contains(img))return false;return true;};
    if(typeof IntersectionObserver==='function'){
      privateObserver=new IntersectionObserver(entries=>{for(const item of entries)if(item.isIntersecting&&visible(item.target))loadPrivateImage(item.target,id);},{rootMargin:'240px'});
      images.forEach(img=>privateObserver.observe(img));
    }else images.filter(visible).forEach(img=>loadPrivateImage(img,id));
    article.querySelectorAll('details').forEach(card=>card.addEventListener('toggle',()=>{
      if(card.open)card.querySelectorAll('img[data-private-asset]').forEach(img=>{if(visible(img))loadPrivateImage(img,id);});
    }));
    main.querySelectorAll('[data-private-download]').forEach(button=>button.addEventListener('click',async()=>{
      if(!button.isConnected||button.disabled)return;button.disabled=true;
      const generation=paymentGeneration,result=await window.DiplomaOneAuth?.readPurchasedAsset?.(id,button.dataset.privateDownload);
      if(generation!==paymentGeneration||!button.isConnected)return;button.disabled=false;
      if(result?.ok===true&&typeof result.url==='string'&&result.url.startsWith('blob:')){
        const a=document.createElement('a');a.href=result.url;a.download=button.dataset.downloadName||'paper.pdf';a.rel='noreferrer';document.body.append(a);a.click();a.remove();
      }else {const status=main.querySelector('#private-asset-status');if(status)status.textContent=paymentMessage(result?.code);}
    }));
  }
  function showPurchasePanel(){
    const signedIn=accountState.status==='signed-in'&&!!accountState.user,view=purchaseView;
    let content;
    if(!signedIn)content=`<p>${esc(paymentMessage('sign_in_required'))}</p>`;
    else if(view.status==='loaded'){
      content=view.purchases.length?`<div class="purchase-list">${view.purchases.map(p=>{
        const parts=p.productId.split('--');if(parts.length!==2||!validPaperCode(parts[0])||!validPaperSession(parts[1]))return '';
        const title=`${p.title} · ${parts[0]} · ${paperSessionTitle(parts[1])}`;
        return `<article class="purchase-item"><h3>${esc(title)}</h3><p>${esc(rupees(p.amount))} · ${esc(new Date(p.purchasedAt).toLocaleDateString(lang==='gu'?'gu-IN':'en-IN'))}</p>${p.active?`<a class="button-text" href="${esc(paymentRoute(...parts))}">${paymentText('Open purchased paper','ખરીદેલું પેપર ખોલો')} →</a>`:`<p>${paymentText('Access inactive. Check your receipt and contact support.','પરવાનગી સક્રિય નથી. રસીદ તપાસો અને સહાય લો.')}</p>`}</article>`;
      }).join('')}</div>`:`<p>${paymentText('No confirmed purchases for this Google account yet.','આ Google એકાઉન્ટ માટે હજી કોઈ ખરીદીની પુષ્ટિ નથી.')}</p>`;
    }else if(view.status==='error')content=`<p role="alert">${esc(paymentMessage(view.code))}</p>`;
    else content=`<p role="status">${paymentText('Loading your purchases…','તમારી ખરીદી લોડ થઈ રહી છે…')}</p>`;
    return `<section class="account-phase-note purchases-panel" data-purchases-panel><h2>${esc(accountLabels[lang].purchases)}</h2><p>${paymentText('Only server-confirmed purchases appear here. Sign-in alone does not unlock a paper.','માત્ર સર્વરે પુષ્ટિ કરેલી ખરીદી અહીં દેખાય છે. માત્ર સાઇન ઇન કરવાથી પેપર ખૂલતું નથી.')}</p>${content}${signedIn?`<button type="button" class="paper-control" id="purchases-refresh" ${view.status==='loading'?'disabled':''}>${paymentText('Refresh purchases','ખરીદી ફરી તપાસો')}</button>`:''}<p>${paymentText('If your payment is still being captured, wait for confirmation and refresh. Do not pay again.','ચુકવણીની પુષ્ટિ બાકી હોય તો રાહ જોઈને ફરી તપાસો. ફરી ચૂકવશો નહીં.')}</p><a href="#/purchase-info">${paymentText('Purchase information & support','ખરીદીની માહિતી અને સહાય')} ↗</a></section>`;
  }
  function bindPurchases(){
    if(location.hash!=='#/purchases'||accountState.status!=='signed-in'||accountState.busy)return;
    const service=window.DiplomaOneAuth,uid=accountState.user?.uid;
    main.querySelector('#purchases-refresh')?.addEventListener('click',()=>{if(purchaseView.status!=='loading'){purchaseView={uid,status:'idle'};render();}});
    if(purchaseView.uid!==uid)purchaseView={uid,status:'idle'};
    if(purchaseView.status!=='idle')return;
    purchaseView={uid,status:'loading'};const generation=paymentGeneration;render();
    Promise.resolve(service?.loadPurchases?.()).then(result=>{
      if(generation!==paymentGeneration||location.hash!=='#/purchases'||accountState.user?.uid!==uid)return;
      purchaseView=result?.ok===true?{uid,status:'loaded',purchases:result.purchases}:{uid,status:'error',code:result?.code};render();
    }).catch(()=>{if(generation===paymentGeneration&&accountState.user?.uid===uid){purchaseView={uid,status:'error',code:'payments_unavailable'};render();}});
  }
  function showPurchaseInfo(){
    const title=paymentText('Purchase information & support','ખરીદીની માહિતી અને સહાય');
    return `${shell(title,paymentText('Individual exam-session paper solutions.','અલગ પરીક્ષા સત્રના પેપરના ઉકેલ.'),[{label:title}])}<section class="page-content"><div class="wrap"><article class="reader-card"><h2>${paymentText('Sales are not open yet','વેચાણ હજી શરૂ નથી')}</h2><p>${paymentText('Before accepting payments, DiplomaOne must publish the merchant’s contact and support details, approved refund/cancellation rules, access duration and delivery terms here. Checkout remains closed until these details are available.','ચુકવણી સ્વીકારતાં પહેલાં DiplomaOne એ વેપારીની સંપર્ક અને સહાયની વિગતો, મંજૂર રિફંડ/રદ કરવાની નીતિ, પરવાનગીનો સમયગાળો અને સામગ્રી આપવાની શરતો અહીં પ્રકાશિત કરવાની છે. આ વિગતો ઉપલબ્ધ થાય ત્યાં સુધી ચેકઆઉટ બંધ રહેશે.')}</p><p>${paymentText('Planned prices per selected paper: Computer ₹19; Mechanical, Electrical and Civil ₹29; Chemical ₹39. Notes, Maths-I and Applied Physics remain free. This is not a subscription or a whole-subject purchase.','પસંદ કરેલા દરેક પેપરની કિંમત: Computer ₹19; Mechanical, Electrical અને Civil ₹29; Chemical ₹39. નોટ્સ, Maths-I અને Applied Physics મફત છે. આ સબ્સ્ક્રિપ્શન કે આખા વિષયની ખરીદી નથી.')}</p><p>${paymentText('Payment access is tied to the Google account used at checkout and requires server-confirmed full capture. If a payment is debited without access, keep your Razorpay receipt and do not pay again. Private delivery does not prevent an authorized reader from making copies.','ચુકવણીની પરવાનગી ચેકઆઉટના Google એકાઉન્ટ સાથે જોડાય છે અને સર્વરની સંપૂર્ણ ચુકવણીની પુષ્ટિ જરૂરી છે. પૈસા કપાયા છતાં પરવાનગી ન મળે તો Razorpay રસીદ સાચવો અને ફરી ચૂકવશો નહીં. ખાનગી સામગ્રી મળ્યા પછી અધિકૃત વાચકને નકલ બનાવતાં રોકી શકાતો નથી.')}</p><a class="button-text" href="#/privacy">${paymentText('Privacy','ગોપનીયતા')} ↗</a></article></div></section>`;
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
  function accountCopy() {
    return lang==='gu'?{
      title:'તમારી અભ્યાસની ઓળખ.',subtitle:'પેપર ખરીદવા અથવા ખરીદેલું પેપર ખોલવા Google દ્વારા સાઇન ઇન કરો. નોટ્સ, Maths-I અને Applied Physics મફત છે.',
      heading:'તમારા Google ખાતા સાથે જોડાઓ',intro:'તમારી ઓળખ Firebase Authentication દ્વારા સંચાલિત થાય છે. DiplomaOne તમારો Google પાસવર્ડ જોતું નથી અને તમારા Drive માટે પરવાનગી માગતું નથી.',
      google:'Google દ્વારા સાઇન ઇન કરો',loading:'સુરક્ષિત સાઇન ઇન તૈયાર થઈ રહ્યું છે…',working:'કૃપા કરીને રાહ જુઓ…',ready:'તમે Google દ્વારા સાઇન ઇન કરી શકો છો.',connected:'તમે સાઇન ઇન કરેલું છે.',
      signOut:'સાઇન આઉટ',retry:'ફરી પ્રયાસ કરો',email:'ઇમેઇલ',emailStatus:'ઇમેઇલની સ્થિતિ',verified:'ઇમેઇલ ચકાસાયેલું છે',unverified:'ઇમેઇલ ચકાસાયેલું નથી',student:'વિદ્યાર્થી',
      session:'સાઇન ઇન આ બ્રાઉઝર ટૅબના સત્ર માટે સાચવાય છે, લાંબા સમયના લૉગિન તરીકે નહીં. શેર કરેલા ઉપકરણ પર સાઇન આઉટ કરો; બ્રાઉઝર ક્યારેક બંધ ટૅબનું સત્ર પાછું લાવી શકે છે. અહીંથી સાઇન આઉટ કરવાથી Googleની અન્ય સેવાઓમાંથી સાઇન આઉટ થતું નથી.',
      local:'સાચવેલી નોટ્સ અને ભાષાની પસંદગી હજુ માત્ર આ ઉપકરણ પર રહે છે; સાઇન ઇન કરવાથી તે સિંક થતી નથી.',
      read:'અભ્યાસ ચાલુ રાખો',privacy:'ગોપનીયતા વિશે વાંચો',purchaseTitle:'તમારા ખરીદેલા પેપર.',
      purchaseNotice:'અલગ પેપરની પરવાનગી',purchaseBody:'દરેક ખરીદી પસંદ કરેલા વિષય અને પરીક્ષા સત્રના એક પેપર માટે છે. સર્વર ચુકવણી ચકાસે પછી જ પરવાનગી મળે છે; મફત નોટ્સ મફત રહે છે.',
      purchaseSignIn:'જે Google એકાઉન્ટથી ચૂકવ્યું તેનાથી સાઇન ઇન કરો. સફળ સાઇન ઇન ખરીદીનો પુરાવો નથી.',
      errors:{
        'auth/popup-closed-by-user':'સાઇન ઇન વિન્ડો બંધ થઈ ગઈ. તમે ફરી પ્રયાસ કરી શકો છો.',
        'auth/cancelled-popup-request':'બીજી સાઇન ઇન વિન્ડો પહેલેથી ખુલ્લી છે. એક જ વિન્ડોનો ઉપયોગ કરો.',
        'auth/popup-blocked':'બ્રાઉઝરે સાઇન ઇન વિન્ડો રોકી છે. આ સાઇટ માટે પોપ-અપને મંજૂરી આપી ફરી પ્રયાસ કરો.',
        'auth/unauthorized-domain':'આ વેબસાઇટનું સરનામું Google સાઇન ઇન માટે હજી અધિકૃત નથી. DiplomaOneને Firebaseમાં આ ડોમેન ઉમેરવાનું કહો.',
        'auth/operation-not-allowed':'આ પ્રોજેક્ટ માટે Google સાઇન ઇન હજી ચાલુ નથી. DiplomaOneએ Firebaseમાં તે સક્ષમ કરવું પડશે.',
        'auth/configuration-not-found':'Firebase Authenticationનું સેટઅપ હજી પૂર્ણ નથી. પછી ફરી પ્રયાસ કરો.',
        'auth/invalid-api-key':'સાઇન ઇનનું સેટઅપ ચકાસવું જરૂરી છે. DiplomaOneને જાણ કરો.',
        'auth/network-request-failed':'સાઇન ઇન સેવા સાથે જોડાણ થઈ શક્યું નથી. ઇન્ટરનેટ તપાસી ફરી પ્રયાસ કરો.',
        'auth/internal-error':'સાઇન ઇન સેવા શરૂ થઈ શકી નથી. ઇન્ટરનેટ તપાસો અને સામાન્ય બ્રાઉઝર ટૅબમાં ફરી પ્રયાસ કરો; કન્ટેન્ટ બ્લોકર Google સાઇન ઇન રોકી શકે છે.',
        'auth/operation-not-supported-in-this-environment':'આ બ્રાઉઝર સાઇન ઇનને સમર્થન આપતું નથી. સાઇટને સામાન્ય બ્રાઉઝર ટૅબમાં ખોલો.',
        'auth/user-token-expired':'સાઇન ઇનનું સત્ર પૂરું થયું છે. સાઇન આઉટ કરીને ફરી સાઇન ઇન કરો.',
        'auth/invalid-user-token':'સાઇન ઇનનું સત્ર ચકાસી શકાયું નથી. સાઇન આઉટ કરીને ફરી સાઇન ઇન કરો.',
        'auth/web-storage-unsupported':'આ બ્રાઉઝરમાં સુરક્ષિત સત્ર સ્ટોરેજ ઉપલબ્ધ નથી. સામાન્ય બ્રાઉઝર ટૅબમાં ફરી પ્રયાસ કરો.',
        'auth/user-disabled':'આ ખાતું નિષ્ક્રિય છે. સહાય માટે DiplomaOneનો સંપર્ક કરો.',
        'auth/too-many-requests':'ઘણા પ્રયાસ થયા છે. થોડી વાર પછી ફરી પ્રયાસ કરો.',
        'auth/account-exists-with-different-credential':'આ ઇમેઇલ માટે અન્ય સાઇન ઇન પદ્ધતિ જોડાયેલી છે. ખાતાઓને જોડવા માટે સહાય લો; નવું ખાતું બનાવશો નહીં.',
      },fallback:'સાઇન ઇન અત્યારે ઉપલબ્ધ નથી. નોટ્સ વાંચવાનું ચાલુ રાખી શકો છો અને પછી ફરી પ્રયાસ કરો.',
    }:{
      title:'Your study account.',subtitle:'Sign in with Google to buy an individual paper or reopen your purchases. Notes, Maths-I and Applied Physics stay free.',
      heading:'Connect your Google account',intro:'Firebase Authentication manages your sign-in. DiplomaOne does not see your Google password or request access to your Drive.',
      google:'Sign in with Google',loading:'Preparing secure sign-in…',working:'Please wait…',ready:'Ready to sign in with Google.',connected:'You are signed in.',
      signOut:'Sign out',retry:'Try again',email:'Email',emailStatus:'Email status',verified:'Email verified',unverified:'Email not verified',student:'Student',
      session:'Sign-in is saved for this browser tab’s session, not as a long-term login. Sign out on shared devices; browsers can sometimes restore closed-tab sessions. Signing out here does not sign you out of other Google services.',
      local:'Saved notes and your language preference remain on this device; signing in does not sync them.',
      read:'Keep learning',privacy:'Read about privacy',purchaseTitle:'Your purchased papers.',
      purchaseNotice:'Individual paper access',purchaseBody:'Each purchase covers one selected subject and exam-session paper. Access is granted only after server-verified payment; your free notes remain free.',
      purchaseSignIn:'Sign in using the same Google account you used to pay. A successful sign-in is not proof of purchase.',
      errors:{
        'auth/popup-closed-by-user':'The sign-in window was closed. You can try again when you are ready.',
        'auth/cancelled-popup-request':'Another sign-in window is already open. Please use one window at a time.',
        'auth/popup-blocked':'Your browser blocked the sign-in window. Allow pop-ups for this site and try again.',
        'auth/unauthorized-domain':'This website address is not authorized for Google sign-in yet. Ask DiplomaOne to add this domain in Firebase.',
        'auth/operation-not-allowed':'Google sign-in is not enabled for this project yet. DiplomaOne must enable it in Firebase.',
        'auth/configuration-not-found':'Firebase Authentication setup is not complete yet. Please try again later.',
        'auth/invalid-api-key':'The sign-in configuration needs attention. Please let DiplomaOne know.',
        'auth/network-request-failed':'We could not reach the sign-in service. Check your connection and try again.',
        'auth/internal-error':'The sign-in service could not start. Check your connection and try a normal browser tab; a content blocker may be preventing Google sign-in.',
        'auth/operation-not-supported-in-this-environment':'This browser cannot run sign-in. Open the site in a normal browser tab.',
        'auth/user-token-expired':'Your sign-in session has expired. Sign out and sign in again.',
        'auth/invalid-user-token':'Your sign-in session could not be verified. Sign out and sign in again.',
        'auth/web-storage-unsupported':'Secure session storage is unavailable in this browser. Try a normal browser tab.',
        'auth/user-disabled':'This account is disabled. Please contact DiplomaOne for help.',
        'auth/too-many-requests':'Too many attempts. Please wait a little before trying again.',
        'auth/account-exists-with-different-credential':'This email already uses another sign-in method. Please get help linking the accounts instead of creating a duplicate.',
      },fallback:'Sign-in is unavailable right now. You can keep reading notes and try again later.',
    };
  }
  const googleMark=()=>'<svg class="google-mark" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M21.6 12.23c0-.71-.06-1.39-.18-2.05H12v3.88h5.38a4.6 4.6 0 0 1-2 3.02v2.51h3.24c1.9-1.75 2.98-4.33 2.98-7.36Z"/><path fill="#34A853" d="M12 22c2.7 0 4.96-.9 6.62-2.41l-3.24-2.51c-.9.6-2.05.96-3.38.96-2.6 0-4.8-1.76-5.6-4.12H3.05v2.6A10 10 0 0 0 12 22Z"/><path fill="#FBBC05" d="M6.4 13.92a6 6 0 0 1 0-3.84v-2.6H3.05a10 10 0 0 0 0 9.04l3.35-2.6Z"/><path fill="#EA4335" d="M12 5.96c1.47 0 2.79.5 3.83 1.5L18.7 4.6A9.62 9.62 0 0 0 12 2a10 10 0 0 0-8.95 5.48l3.35 2.6A5.99 5.99 0 0 1 12 5.96Z"/></svg>';
  function connectionCopy(){
    const local=(en,gu)=>lang==='gu'?gu:en;
    return {
      title:local('Test database connection.','ટેસ્ટ ડેટાબેઝનું જોડાણ.'),
      subtitle:local('A manual, read-only setup check for approved testers. Checkout stays OFF.','મંજૂર ટેસ્ટર માટે મેન્યુઅલ, માત્ર વાંચનની સેટઅપ તપાસ. ચેકઆઉટ બંધ રહે છે.'),
      heading:local('Read-only Firestore check','માત્ર વાંચન માટે Firestore તપાસ'),
      body:local('One manual check queries at most one test product’s metadata. No document contents are shown; no Firestore records are created or changed.','એક મેન્યુઅલ તપાસ વધુમાં વધુ એક ટેસ્ટ પ્રોડક્ટનું મેટાડેટા વાંચે છે. ડોક્યુમેન્ટની વિગતો બતાવાતી નથી; Firestore રેકોર્ડ બનાવાતા કે બદલાતા નથી.'),
      warning:local('This does not test Razorpay, payments or purchases. Do not paste private keys or tokens.','આ Razorpay, પેમેન્ટ કે ખરીદીની તપાસ નથી. ખાનગી કી કે ટોકન ન મોકલો.'),
      connected:local('Google account connected','Google એકાઉન્ટ જોડાયેલું છે'),
      signedIn:local('The server will verify whether this Google account is an approved tester. Signing in alone does not grant access.','સર્વર તપાસશે કે આ Google એકાઉન્ટ મંજૂર ટેસ્ટર છે કે નહીં. માત્ર સાઇન ઇન કરવાથી પરવાનગી મળતી નથી.'),
      check:local('Check Firestore connection','Firestore જોડાણ તપાસો'),
      checking:local('Checking the server’s read-only Firestore connection…','સર્વરનું માત્ર વાંચન માટેનું Firestore જોડાણ તપાસાઈ રહ્યું છે…'),
      success:local('Firestore read succeeded. Checkout remains OFF.','Firestore વાંચન સફળ થયું. ચેકઆઉટ બંધ જ છે.'),
      limits:local('Run once when needed, not repeatedly. Wait at least 30 seconds before another attempt. Even an empty query can incur a read; closing the page or a timeout does not undo a server read. The per-server cooldown is not a billing cap.','જરૂર હોય ત્યારે એક વાર ચલાવો, વારંવાર નહીં. બીજા પ્રયાસ પહેલાં ઓછામાં ઓછી 30 સેકન્ડ રાહ જુઓ. ખાલી ક્વેરીનો પણ વાંચન ચાર્જ થઈ શકે છે; પેજ બંધ કરવાથી કે સમય પૂરો થવાથી સર્વરનું વાંચન રદ થતું નથી. સર્વરનો વિરામ બિલિંગ મર્યાદા નથી.'),
      link:local('Test setup: Firestore connection','ટેસ્ટ સેટઅપ: Firestore જોડાણ'),
      errors:{
        sign_in_required:local('Sign in with your approved Google account before checking.','તપાસ પહેલાં મંજૂર કરેલા Google એકાઉન્ટથી સાઇન ઇન કરો.'),
        invalid_or_expired_session:local('Your session has expired. Sign out, then sign in again.','સત્ર સમાપ્ત થયું છે. સાઇન આઉટ કરીને ફરી સાઇન ઇન કરો.'),
        tester_not_allowed:local('This account is not an approved tester. Privately add its Firebase Authentication UID to PAYMENTS_TESTER_UIDS in the test site’s Production settings, then redeploy. Do not share tokens or keys.','આ એકાઉન્ટ મંજૂર ટેસ્ટર નથી. ટેસ્ટ સાઇટની Production સેટિંગમાં PAYMENTS_TESTER_UIDS માં તેનું Firebase Authentication UID ખાનગી રીતે ઉમેરો અને ફરી ડિપ્લોય કરો. ટોકન કે કી ન મોકલો.'),
        disable_test_checkout:local('Keep both payment flags false, then redeploy the test site before checking.','બંને પેમેન્ટ ફ્લેગ false રાખો અને તપાસ પહેલાં ટેસ્ટ સાઇટ ફરી ડિપ્લોય કરો.'),
        firestore_not_configured:local('The server’s private Firestore configuration is missing or invalid. Review it privately in the test site’s Production settings, then redeploy.','સર્વરની ખાનગી Firestore સેટિંગ અધૂરી અથવા અમાન્ય છે. ટેસ્ટ સાઇટની Production સેટિંગ ખાનગી રીતે તપાસીને ફરી ડિપ્લોય કરો.'),
        firestore_check_failed:local('The server could not read Firestore. Privately review the replacement service account, its Firestore permission and the database settings. No provider details are displayed here.','સર્વર Firestore વાંચી શક્યું નથી. બદલેલા સર્વિસ એકાઉન્ટ, તેની Firestore પરવાનગી અને ડેટાબેઝ સેટિંગ ખાનગી રીતે તપાસો. પ્રોવાઇડરની વિગત અહીં બતાવાતી નથી.'),
        connection_check_rate_limited:local('A check is already running or was just attempted. Wait at least 30 seconds before trying once more.','તપાસ ચાલુ છે અથવા હમણાં થઈ છે. ફરી પ્રયાસ કરતાં પહેલાં ઓછામાં ઓછી 30 સેકન્ડ રાહ જુઓ.'),
        connection_timeout:local('The check timed out. No success is confirmed. Wait at least 30 seconds before retrying.','તપાસનો સમય પૂરો થયો. સફળતાની પુષ્ટિ નથી. ફરી પ્રયાસ કરતાં પહેલાં ઓછામાં ઓછી 30 સેકન્ડ રાહ જુઓ.'),
        session_changed:local('Your account session changed. Sign in again before checking.','તમારા એકાઉન્ટનું સત્ર બદલાયું છે. તપાસ પહેલાં ફરી સાઇન ઇન કરો.'),
        test_site_required:local('This check is available only on the protected test site.','આ તપાસ માત્ર સુરક્ષિત ટેસ્ટ સાઇટ પર ઉપલબ્ધ છે.'),
        connection_check_unavailable:local('The check is unavailable. Confirm you are on the protected test site’s current Production deployment, then try again later.','તપાસ ઉપલબ્ધ નથી. સુરક્ષિત ટેસ્ટ સાઇટના હાલના Production ડિપ્લોયમેન્ટ પર છો તેની ખાતરી કરો અને પછી ફરી પ્રયાસ કરો.')
      }
    };
  }
  function showConnectionPanel(){
    const c=connectionCopy(),s=connectionState,signedIn=accountState.status==='signed-in'&&!!accountState.user;
    const status=s.status==='success'?c.success:s.status==='checking'?c.checking:
      s.status==='error'?(c.errors[s.code]||c.errors.connection_check_unavailable):'';
    return `<section class="account-phase-note connection-panel" aria-labelledby="connection-heading"><h2 id="connection-heading">${esc(c.heading)}</h2><p>${esc(c.body)}</p><p>${esc(c.warning)}</p>
      ${!signedIn?`<p>${esc(c.errors.sign_in_required)}</p>`:''}
      <button type="button" class="button-primary" id="connection-check" ${!signedIn||accountState.busy||s.status==='checking'?'disabled':''}>${esc(s.status==='checking'?c.checking:c.check)}</button>
      <div id="connection-result" class="connection-result" role="${s.status==='error'?'alert':'status'}" aria-live="polite" tabindex="-1">${esc(status)}</div><p class="connection-limits">${esc(c.limits)}</p></section>`;
  }
  function resetConnection(cancel=false){
    ++connectionGeneration;connectionState={status:'idle',code:null};
    if(cancel)window.DiplomaOneAuth?.cancelTestConnection?.();
  }
  function showAccount(purchases=false,connection=false) {
    const c=accountCopy(),check=connectionCopy(),s=accountState,user=s.user,busy=!!s.busy,preparing=['idle','loading'].includes(s.status);
    if(connection&&!isConnectionTestSite())return `${shell(check.title,check.subtitle,[{label:check.heading}])}<section class="page-content"><div class="wrap"><p class="account-phase-note">${esc(check.errors.test_site_required)}</p></div></section>`;
    const labels=accountLabels[lang],title=connection?check.title:purchases?c.purchaseTitle:c.title;
    const error=s.error?`<div class="account-message" role="alert"><p>${esc(c.errors[s.error.code]||c.fallback)}</p><small>${esc(s.error.code)}</small></div>`:'';
    const purchaseNotice=purchases?showPurchasePanel():`<div class="account-phase-note"><strong>${esc(c.purchaseNotice)}</strong><p>${esc(c.purchaseBody)}</p><a class="button-text" href="#/purchases">${esc(labels.purchases)} →</a></div>`;
    let content;
    if(user&&connection){
      // The diagnostic page/status deliberately does not echo profile, UID or
      // email. The existing My account page still has its usual profile view.
      content=`<div class="account-emblem">${icon('check')}</div><h2>${esc(check.connected)}</h2><p class="account-intro">${esc(check.signedIn)}</p><div class="account-actions"><button type="button" id="account-signout" class="save-button" ${busy?'disabled':''}>${esc(busy?c.working:c.signOut)}</button><a class="button-text" href="#/account">${esc(labels.account)} →</a></div>`;
    }else if(user) {
      const display=user.displayName||c.student;
      content=`<div class="account-identity"><span class="account-avatar" aria-hidden="true">${esc(Array.from(display.trim())[0]||'D')}</span><div><p class="eyebrow">${esc(labels.account)}</p><h2>${esc(display)}</h2></div></div><dl class="account-details"><div><dt>${esc(c.email)}</dt><dd>${esc(user.email||'—')}</dd></div><div><dt>${esc(c.emailStatus)}</dt><dd>${esc(user.emailVerified?c.verified:c.unverified)}</dd></div></dl><div class="account-actions"><button type="button" id="account-signout" class="save-button" ${busy?'disabled':''}>${esc(busy?c.working:c.signOut)}</button><a class="button-text" href="#/${purchases?'account':'purchases'}">${esc(purchases?labels.account:labels.purchases)} →</a></div>`;
    } else {
      content=`<div class="account-emblem">${icon('school')}</div><h2>${esc(c.heading)}</h2><p class="account-intro">${esc(connection?check.errors.sign_in_required:purchases?c.purchaseSignIn:c.intro)}</p>${preparing?`<p class="account-preparing"><span class="spinner" aria-hidden="true"></span>${esc(c.loading)}</p>`:''}${s.status==='unavailable'?`<p>${esc(c.fallback)}</p><button type="button" id="account-retry" class="paper-control">${esc(c.retry)}</button>`:`<button type="button" id="account-signin" class="google-signin-button" ${preparing||busy?'disabled':''}>${googleMark()}<span>${esc(busy?c.working:c.google)}</span></button>`}`;
    }
    const setupLink=!connection&&isConnectionTestSite()?`<a class="button-text" href="#/test-connection">${esc(check.link)} →</a>`:'';
    return `${shell(title,connection?check.subtitle:purchases?c.purchaseBody:c.subtitle,[{label:labels.account,href:purchases||connection?'#/account':undefined},...(connection?[{label:check.heading}]:purchases?[{label:labels.purchases}]:[])])}<section class="page-content"><div class="wrap account-layout" data-account-view><article class="account-card" aria-busy="${preparing||busy}">${content}${error}<p id="account-status" class="sr-only" role="status" aria-live="polite">${esc(preparing?c.loading:busy?c.working:user?c.connected:s.status==='signed-out'?c.ready:c.fallback)}</p><p class="account-session">${esc(c.session)}</p><a class="account-privacy" href="#/privacy">${esc(c.privacy)} ↗</a></article><aside class="account-sidebar">${connection?showConnectionPanel():purchaseNotice}${setupLink}<div class="account-reading-note"><p>${esc(c.local)}</p><a class="button-text" href="#/branches">${esc(c.read)} →</a></div></aside></div></section>`;
  }
  function updateAccountLinks() {
    // Before the optional SDK loads, the saved session is unknown, not signed out.
    const labels=accountLabels[lang],label=accountState.status==='signed-out'?labels.signIn:labels.account;
    document.querySelectorAll('[data-account-link]').forEach(a=>{a.textContent=label;});
    document.querySelectorAll('[data-purchases-link]').forEach(a=>{a.textContent=labels.purchases;});
  }
  function bindAccount() {
    if(!main.querySelector('[data-account-view]'))return;
    const service=window.DiplomaOneAuth;
    if(!service){main.querySelector('#account-retry')?.addEventListener('click',()=>location.reload());return;}
    const focusAction=()=>{if(main.querySelector('[data-account-view]'))main.querySelector('#account-signout,#account-signin,#account-retry')?.focus();};
    main.querySelector('#account-signin')?.addEventListener('click',()=>{service.signIn(lang).then(focusAction);});
    main.querySelector('#account-signout')?.addEventListener('click',()=>{service.signOut().then(focusAction);});
    main.querySelector('#account-retry')?.addEventListener('click',()=>{service.initialize().then(focusAction);});
    main.querySelector('#connection-check')?.addEventListener('click',event=>{
      if(!event.currentTarget.isConnected||!isConnectionTestSite()||location.hash!=='#/test-connection'||connectionState.status==='checking'||
        accountState.status!=='signed-in'||!accountState.user||accountState.busy)return;
      const generation=++connectionGeneration;connectionState={status:'checking',code:null};render();
      let request;try{request=service.checkTestConnection();}catch(_){request=Promise.resolve({ok:false});}
      Promise.resolve(request).catch(()=>({ok:false})).then(result=>{
        if(generation!==connectionGeneration||location.hash!=='#/test-connection'||accountState.status!=='signed-in'||accountState.busy)return;
        // Render only local allowlisted copy, not raw data/messages from a server.
        connectionState=result?.ok===true?{status:'success',code:null}:{status:'error',code:result?.code};
        render().then(()=>{if(generation===connectionGeneration&&location.hash==='#/test-connection')main.querySelector('#connection-result')?.focus();});
      });
    });
    if(accountState.status==='idle')service.initialize();
    bindPurchases();
  }
  function startAccount() {
    if(!window.DiplomaOneAuth)return;
    window.DiplomaOneAuth.subscribe(state=>{
      const changed=accountState.user?.uid!==state.user?.uid||state.busy==='signOut'||!!state.error;
      if(changed)resetPayments();
      resetConnection();accountState=state;updateAccountLinks();
      if(/^#\/(?:account|purchases|test-connection)(?:$|\/)/.test(location.hash)||
        /^#\/paper\//.test(location.hash)&&!freePaperCodes.has(location.hash.split('/')[2]))render();
    });
  }
  function showPrivacy() {
    const gu=lang==='gu';
    const title=gu?'ગોપનીયતા':'Privacy';
    const intro=gu?'તમારા અભ્યાસને સરળ અને ખાનગી રાખવાનો અમારો પ્રયાસ છે.':'A simple explanation of how this website handles information.';
    const sections=gu?[
      ['ખાતા વગર અભ્યાસ', 'આ વેબસાઇટ પર નોટ્સ વાંચવા માટે ખાતું, નામ અથવા ઇમેઇલ જરૂરી નથી.'],
      ['વૈકલ્પિક Google સાઇન ઇન', 'મારું ખાતું, મારી ખરીદી અથવા ચૂકવવાનું પેપર ખોલવાથી સ્થાનિક રીતે હોસ્ટ કરેલો Firebase Authentication ક્લાયન્ટ લોડ થાય છે. તમે સાઇન ઇન કરો ત્યારે Google અને Firebase તમારી ઓળખ, નામ, ઇમેઇલ અને ટેકનિકલ માહિતી પર પ્રક્રિયા કરે છે. Firebase Authentication ખાતાની ઓળખનો રેકોર્ડ રાખે છે; સાઇન આઉટ કરવાથી તે રેકોર્ડ કાઢી નાખવામાં આવતો નથી. આ વેબસાઇટ તમારો Google પાસવર્ડ મેળવતી નથી કે Drive માટે પરવાનગી માગતી નથી.'],
      ['આ ઉપકરણ પર સાચવેલી માહિતી', 'ભાષા અને સાચવેલી નોટ્સ બ્રાઉઝરના સ્થાનિક સ્ટોરેજમાં રહે છે; સાઇન ઇન કર્યા પછી પણ અન્ય ઉપકરણો પર સિંક થતી નથી. Firebase સાઇન ઇનને આ ટૅબના સેશન સ્ટોરેજમાં સંભાળે છે, લાંબા સમયના લૉગિન તરીકે નહીં. શેર કરેલા ઉપકરણ પર સાઇન આઉટ કરો; બ્રાઉઝર ક્યારેક બંધ ટૅબનું સત્ર પાછું લાવી શકે છે. અહીંથી સાઇન આઉટ કરવાથી અન્ય Google સેવાઓમાંથી સાઇન આઉટ થતું નથી. બ્રાઉઝર ડેટા દૂર કરવાથી સ્થાનિક પસંદગીઓ દૂર થાય છે.'],
      ['ખરીદી અને ખાનગી સામગ્રી', 'લાઇવ ચેકઆઉટ ચાલુ હોય ત્યારે Razorpay તેના સુરક્ષિત Checkout માં ચુકવણીની માહિતી સંભાળે છે. અમે કાર્ડની વિગતો કે UPI ઓળખ સાચવતા નથી. આ જ સાઇટનો સર્વર Google ID ટોકન અને મળેલી ચુકવણી ચકાસીને Firestore માં Firebase UID, પસંદ કરેલું પેપર, ઓર્ડર/ચુકવણી ID, રકમ, સ્થિતિ અને સમય સાચવે છે. સર્વરની પરવાનગી પછી જ ખાનગી જવાબ અને આકૃતિ મળે છે; એપના સ્ટોરેજ કે લોગમાં ટોકન કે જવાબની ફાઇલો સાચવાતી નથી. બ્રાઉઝરમાં Firestore, Firebase Storage કે Analytics SDK લોડ થતાં નથી. સાઇન ઇન ખરીદીનો પુરાવો નથી.'],
      ['સુરક્ષિત ટેસ્ટ સાઇટની તપાસ', 'ટેસ્ટ સાઇટ પર મંજૂર Google ટેસ્ટર મેન્યુઅલ Firestore જોડાણ તપાસ ચલાવી શકે છે. Firebase ID ટોકન માત્ર આ જ સાઇટના સર્વરને Authorization હેડરમાં મોકલાય છે. સર્વર તેની ઓળખ અને મંજૂર UID યાદી ચકાસે છે, વધુમાં વધુ એક ટેસ્ટ પ્રોડક્ટનું મેટાડેટા વાંચે છે અને માત્ર સુરક્ષિત સ્થિતિ આપે છે. તપાસ કંઈ લખતી નથી કે ચુકવણી ચાલુ કરતી નથી. અમે ટોકન, ડેટાબેઝની વિગતો કે તપાસનું પરિણામ એપના સ્ટોરેજ અથવા લોગમાં સાચવતા નથી.'],
      ['હોસ્ટિંગ અને બહારની લિંક્સ', 'GitHub Pages આ સાઇટ અને મફત નોટ્સ હોસ્ટ કરે છે અને સેવા તથા સુરક્ષા માટે IP એડ્રેસ જેવી ટેકનિકલ માહિતી મેળવી શકે છે. પેપરની યાદી GitHub API પરથી મેળવાય છે. Android એપ ડાઉનલોડની લિંક તમને GitHub પર લઈ જાય છે, જ્યાં તેમની પોતાની ગોપનીયતા નીતિ લાગુ પડે છે.'],
      ['Analytics અને જાહેરાતો', 'આ વેબસાઇટ કોઈ analytics કે જાહેરાત સેવા ઉમેરતી નથી. Google/Firebase, Netlify અને Razorpay પોતાની નીતિઓ હેઠળ ઓળખ, હોસ્ટિંગ અને ચુકવણી માટે ટેકનિકલ માહિતી મેળવી શકે છે. અમારો ઉપયોગ બદલાય તો આ માહિતી અપડેટ થશે.']
    ]:[
      ['No account needed', 'You can read notes without creating an account or giving us your name or email address.'],
      ['Optional Google sign-in', 'Opening My account, My purchases or a paid paper loads the self-hosted Firebase Authentication client. If you choose to sign in, Google and Firebase process your account identifier, name, email and technical information to authenticate you. Firebase Authentication keeps an account identity record; signing out does not delete that record. This website does not receive your Google password or request Drive access.'],
      ['Stored on this device', 'Your language preference and saved units are stored in your browser’s local storage. They do not sync across devices after sign-in. Firebase manages sign-in data in this tab’s session storage, not as a long-term login. Sign out on shared devices; browsers can sometimes restore closed-tab sessions. Signing out here clears this site’s authentication session, not your Google session in other services. Clearing browser data removes locally stored preferences.'],
      ['Purchases and private delivery', 'When live checkout is enabled, Razorpay processes payment information in its secure Checkout. We do not receive or store card details or UPI credentials. The same-origin server verifies your Google ID token and captured payment, then stores your Firebase UID, selected paper, order/payment IDs, amount, status and timestamps in Firestore. Private answers and images are delivered only after server authorization; app-managed storage and logs do not contain your tokens or answer files. The browser does not load a Firestore, Firebase Storage or Analytics SDK. Signing in is not proof of a purchase.'],
      ['Protected test-site check', 'On the protected test site, an approved Google tester can manually run a Firestore connection check. A Firebase ID token goes only to this same site’s server in an Authorization header. The server verifies that identity against the tester UID allowlist, queries at most one test product’s metadata and returns only a safe status. The check does not write records or enable payments. We do not copy tokens, database contents or check results into application storage or logs.'],
      ['Hosting and external links', 'GitHub Pages hosts this website and its free notes and may receive technical information such as IP addresses to operate and secure its service. The paper list is requested from the GitHub API. The Android download link takes you to GitHub, where its own privacy policy applies.'],
      ['Analytics and advertising', 'This website does not add an analytics or advertising service. Google/Firebase, Netlify and Razorpay may process technical information for their authentication, hosting and payment services under their own policies. If our use changes, this information will be updated.']
    ];
    return `${shell(title,intro,[{label:title}])}<section class="page-content"><div class="wrap"><article class="reader-card">${sections.map(([heading,body])=>`<section class="note-section"><h3>${esc(heading)}</h3><p>${esc(body)}</p></section>`).join('')}</article></div></section>`;
  }
  function updateHeader() {
    document.documentElement.lang=lang;
    document.querySelectorAll('[data-nav]').forEach(a=>a.textContent=tr(a.dataset.nav));
    updateAccountLinks();
    const mobile=mobileNav.querySelectorAll('a');['home','branches','papers','saved'].forEach((key,i)=>mobile[i].textContent=tr(key));
    langButton.setAttribute('aria-label',lang==='en'?'Switch to Gujarati':'Switch to English');
    langButton.innerHTML=lang==='en'?'ગુ <span>/</span> <strong>EN</strong>':'<strong>ગુ</strong> <span>/</span> EN';
  }
  async function render() {
    const id=++routeCounter,routeHash=location.hash;
    privateObserver?.disconnect();privateObserver=null;
    const parts=(location.hash.startsWith('#/')?location.hash.slice(2):'').split('/').map(p=>{try{return decodeURIComponent(p)}catch(_){return ''}});
    const [route,arg,sub]=parts; let html='', bind=null;
    main.innerHTML='<div class="loading-page"><span class="spinner" aria-label="Loading"></span></div>';
    try {
      // Account, setup and privacy screens must work without the public catalog.
      if(!catalog&&!['account','purchases','test-connection','privacy','purchase-info'].includes(route)) await loadCatalog();
      if(!route)html=showHome();
      else if(route==='account'||route==='purchases'||route==='test-connection'){html=showAccount(route==='purchases',route==='test-connection');bind=bindAccount;}
      else if(route==='branches'){html=showBranches();bind=bindBranchSearch;}
      else if(route==='branch'){await loadPaperIndex();html=sub?showSemester(arg,sub):showBranch(arg);}
      else if(route==='search'){html=showSearch();bind=bindSubjectSearch;}
      else if(route==='papers'){await loadPaperIndex();html=showPapers(arg,sub);bind=bindPaperFilters;}
      else if(route==='saved')html=showSaved();
      else if(route==='about')html=`${shell(tr('aboutTitle'),tr('aboutText'),[{label:'About'}])}<section class="page-content"><div class="wrap"><div class="reader-card"><p>${esc(tr('aboutNote'))}</p></div></div></section>`;
      else if(route==='privacy')html=showPrivacy();
      else if(route==='purchase-info')html=showPurchaseInfo();
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
        const available=entry||!freePaperCodes.has(arg); // Owners can reopen a delisted paid paper.
        html=available?await showPaper(arg,sub,subjectMeta(arg),entry||{}):missing();
        if(available)bind=()=>{bindPaperReader();bindPaidPaper(arg,sub);};
      } else if(route==='unit'&&safeCode(arg)&&/^(?:0|[1-9]\d*)$/.test(sub||'')&&subjectMeta(arg)?.status==='available') {
        const [subject,unit]=await Promise.all([fetchJson(`subjects/${arg}.json`),fetchJson(`units/${arg}_u${sub}.json`)]);
        html=showUnit(unit,subject);bind=()=>bindReader(unit,subject);
      } else html=missing();
      if(id!==routeCounter||location.hash!==routeHash)return;
      main.innerHTML=html;if(bind)bind();
      document.title=route ? `${main.querySelector('h1')?.textContent || 'Study'} | DiplomaOne`:'DiplomaOne — Your diploma, made simpler';
      document.querySelectorAll('[data-nav]').forEach(a=>a.classList.toggle('active',(route||'home')===a.dataset.nav));
    } catch(error) {
      // Paid responses, identity and provider details never enter app logs.
      if(route!=='paper'&&route!=='purchases')console.error(error);
      if(id!==routeCounter||location.hash!==routeHash)return;
      main.innerHTML=`<div class="error-page"><h1>${esc(tr('loadError'))}</h1><p>${esc(tr('loadErrorText'))}</p><button type="button" id="retry" class="button-primary">${esc(tr('retry'))}</button></div>`;
      document.querySelector('#retry').addEventListener('click',render);
    }
  }
  langButton.addEventListener('click',()=>{lang=lang==='en'?'gu':'en';writeStore('diplomaone.website.lang',lang);updateHeader();render();});
  menuButton.addEventListener('click',()=>{const open=mobileNav.hidden;mobileNav.hidden=!open;menuButton.setAttribute('aria-expanded',String(open));});
  mobileNav.addEventListener('click',e=>{if(e.target.closest('a')){mobileNav.hidden=true;menuButton.setAttribute('aria-expanded','false');}});
  window.addEventListener('hashchange',()=>{resetConnection(true);resetPayments();activeTab='notes';window.scrollTo(0,0);render();});
  startAccount();
  updateHeader();render();
})();
