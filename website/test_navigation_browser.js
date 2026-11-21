// OFFLINE Chromium against the built Netlify SPA. All HTTP boundaries are
// fulfilled from local files/synthetic fixtures, never owner/provider systems.
// NODE_PATH="$PWD/build/auth-browser-tools/node_modules:$PWD/website/node_modules" node website/test_navigation_browser.js
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium:playwright}=require('playwright'),fixture=require('./test_navigation_fixture');
const root=path.resolve(__dirname,'..'),site=path.resolve(process.argv[2]||path.join(root,'build/netlify-site')),origin='https://www.diplomaone.in';
const out=path.join(root,'build/navigation-browser');
const saved=JSON.stringify(['computer','hiddenSemester','hiddenBranch'].map(key=>({code:fixture.codes[key],unit:1,title:{en:key}})));
async function contextFor(browser,width,language){
 const context=await browser.newContext({viewport:{width,height:960}}),requests=[],errors=[],unexpected=[];
 const catalog=fixture.catalog();
 await context.route('**/*',async route=>{
  const request=route.request(),url=new URL(request.url());requests.push(url.href);
  if(url.origin==='https://api.github.com')return route.fulfill({json:fixture.tree()});
  if([fixture.codes.maths,fixture.codes.physics].some(code=>url.href.startsWith('https://sunilpa4.github.io/diplomaone-content/papers/'+code+'/')))
   return route.fulfill({contentType:'text/html; charset=utf-8',body:fixture.freeReader});
  if(url.origin!==origin){unexpected.push(url.href);return route.abort();}
  if(url.pathname==='/data/catalog.json')return route.fulfill({json:catalog});
  if(url.pathname==='/api/payments/live/config'){
   assert(!(await request.allHeaders()).authorization);return route.fulfill({json:{mode:'live',enabled:false,products:[]}});
  }
  const subject=/^\/data\/subjects\/([A-Z0-9]+)\.json$/.exec(url.pathname);
  if(subject)return route.fulfill({json:fixture.subject(subject[1],catalog)});
  const unit=/^\/data\/units\/([A-Z0-9]+)_u([0-9]+)\.json$/.exec(url.pathname);
  if(unit)return route.fulfill({json:fixture.unit(unit[1],unit[2])});
  if(url.pathname==='/assets/firebase-auth.js'||url.pathname.startsWith('/api/')){unexpected.push(url.pathname);return route.abort();}
  const relative=url.pathname==='/'?'index.html':url.pathname.slice(1),file=path.resolve(site,relative);
  if(!file.startsWith(site+path.sep)||!fs.existsSync(file)||!fs.statSync(file).isFile()){unexpected.push(relative);return route.abort();}
  const contentType=relative.endsWith('.html')?'text/html':relative.endsWith('.js')?'text/javascript':relative.endsWith('.css')?'text/css':relative.endsWith('.ttf')?'font/ttf':relative.endsWith('.svg')?'image/svg+xml':'application/octet-stream';
  return route.fulfill({contentType,body:fs.readFileSync(file)});
 });
 const page=await context.newPage();page.on('pageerror',error=>errors.push(error.message));
 await page.addInitScript(({language,saved})=>{
  localStorage.setItem('diplomaone.website.lang',JSON.stringify(language));localStorage.setItem('diplomaone.website.saved',saved);
  window.__navigationCsp=[];document.addEventListener('securitypolicyviolation',event=>window.__navigationCsp.push(event.violatedDirective+':'+event.blockedURI));
 },{language,saved});
 const safe=async()=>{
  assert.deepEqual(errors,[]);assert.deepEqual(unexpected,[]);assert.deepEqual(await page.evaluate(()=>window.__navigationCsp),[]);
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'horizontal overflow');
  assert.equal(await page.evaluate(()=>window.DiplomaOneAuth.snapshot().status),'idle','ordinary learning must not initialize Auth');
  assert.equal(await page.evaluate(()=>localStorage.getItem('diplomaone.website.saved')),saved,'UI scope must not delete saved data');
  assert(!requests.some(url=>url.includes('/assets/firebase-auth.js')||url.includes('razorpay.com')||url.endsWith('/orders')));
 };
 const navigate=async(hash,selector)=>{await page.evaluate(hash=>{location.hash=hash;},hash);await page.locator(selector).first().waitFor();};
 return {context,page,requests,safe,navigate};
}
let scenario='browser startup';
(async()=>{
 const module=process.env.CHROMIUM_EXECUTABLE_PATH?null:require('@sparticuz/chromium'),packaged=module?.default||module;
 if(module){const lib=await module.inflate(path.resolve(path.dirname(require.resolve('@sparticuz/chromium')),'../bin/al2023.tar.br'));module.setupLambdaEnvironment(path.join(lib,'lib'));}
 const args=packaged?packaged.args.filter(arg=>!['--disable-web-security','--allow-running-insecure-content','--single-process'].includes(arg)):['--no-sandbox'];
 const browser=await playwright.launch({executablePath:process.env.CHROMIUM_EXECUTABLE_PATH||await packaged.executablePath(),args,headless:true});
 fs.mkdirSync(out,{recursive:true});let checks=0;
 try{
  for(const width of [1440,1024,390,320])for(const language of ['en','gu']){
   scenario=width+'px '+language;const f=await contextFor(browser,width,language),{page}=f;
   await page.goto(origin+'/#/');await page.locator('#home-search').waitFor();await page.evaluate(()=>document.fonts.ready);
   assert.deepEqual(await page.locator('main .branch-card').evaluateAll(nodes=>nodes.map(node=>node.dataset.branch)),fixture.keys);
   assert.equal(await page.locator('main .hero-image,main .trust-strip,main .how-section,main .cta-band,main img').count(),0);
   assert.equal(await page.locator('main h1').count(),1);assert.equal(await page.locator('.footer-tools').evaluate(el=>el.open),false);
   if(width<=600)assert(await page.locator('.common-resources>div:not(.common-links)').evaluate(el=>el.getBoundingClientRect().width>=innerWidth*.6),'free-paper text must not be squeezed between its links on mobile');
   await f.safe();
   if(width===1440&&language==='en'||width===390)await page.screenshot({path:path.join(out,'home-'+width+'-'+language+'.png'),fullPage:true});
   await page.locator('#home-search-input').fill(language==='gu'?'કમ્પ્યુટર':fixture.codes.computer);await page.locator('#home-search-input').press('Enter');
   await page.locator('#results a[href="#/subject/'+fixture.codes.computer+'"]').waitFor();await f.safe();
   await f.navigate('#/branches','#results .branch-card');
   assert.equal(await page.locator('#results .branch-card').count(),5);
   await page.locator('#search-input').fill('Information Technology');assert.equal(await page.locator('#results .branch-card').count(),0);
   await page.locator('#search-input').fill('');await page.locator('main a[href="#/branch/computer"]').click();await page.locator('.semester-card').first().waitFor();
   assert.equal(await page.locator('.semester-card').count(),5);assert.equal(await page.locator('main a[href="#/branch/computer/6"]').count(),0);await f.safe();
   if(width===1440&&language==='en')await page.screenshot({path:path.join(out,'semesters-desktop.png'),fullPage:true});
   await page.locator('main a[href="#/branch/computer/2"]').click();await page.locator('main a[href="#/subject/'+fixture.codes.computer+'"]').waitFor();
   assert.equal(await page.locator('.desktop-nav [data-nav="branches"]').getAttribute('aria-current'),'page');await f.safe();
   await f.navigate('#/papers','#paper-results .paper-subject-group');
   assert.deepEqual(await page.locator('#paper-branch-filter option').evaluateAll(nodes=>nodes.map(node=>node.value)),['',...fixture.keys]);
   assert.deepEqual(await page.locator('#paper-semester-filter option').evaluateAll(nodes=>nodes.map(node=>node.value)),['','1','2','3','4','5']);
   for(const code of [fixture.codes.hiddenSemester,fixture.codes.hiddenBranch])assert.equal(await page.locator('#paper-results a[href*="/paper/'+code+'/"]').count(),0);
   for(const [key,price] of [['computer','₹19'],['civil','₹29'],['chemical','₹39'],['electrical','₹29'],['mechanical','₹29']])
    assert((await page.locator('#paper-results a[href*="/paper/'+fixture.codes[key]+'/"] .paper-access-label').textContent()).includes(price));
   await page.locator('#paper-branch-filter').selectOption('chemical');await page.locator('#paper-semester-filter').selectOption('5');
   assert.equal(await page.locator('#paper-results a[href*="/paper/4350501/"]').count(),1);await f.safe();
   await page.locator('#paper-branch-filter').selectOption('');await page.locator('#paper-semester-filter').selectOption('');
   if(width===390&&language==='en')await page.screenshot({path:path.join(out,'papers-mobile.png'),fullPage:true});
   await page.locator('#paper-results a[href*="/paper/'+fixture.codes.maths+'/"]').click();await page.locator('.solved-paper details.card').waitFor();
   await page.locator('[data-paper-expand="true"]').click();assert((await page.locator('.solved-paper').textContent()).includes(language==='gu'?'મફત જવાબ':'FREE ANSWER FIXTURE'));await f.safe();
   await f.navigate('#/saved','main .subject-card');assert.equal(await page.locator('main .subject-card').count(),1);await f.safe();
   await f.navigate('#/branch/computer/6','[data-catalog-limited]');assert.equal(await page.locator('main .subject-card,main .semester-card').count(),0);await f.safe();
   if(width<=1050){
    await page.locator('#menu-toggle').click();await page.locator('#mobile-nav').waitFor({state:'visible'});
    assert.equal(await page.locator('#menu-toggle').getAttribute('aria-label'),language==='gu'?'નેવિગેશન બંધ કરો':'Close navigation');
    await page.keyboard.press('Escape');assert.equal(await page.locator('#mobile-nav').isVisible(),false);assert.equal(await page.evaluate(()=>document.activeElement.id),'menu-toggle');
    await page.locator('#menu-toggle').click();await page.locator('#mobile-nav a[href="#/branches"]').click();await page.locator('#results .branch-card').first().waitFor();
    assert.equal(await page.locator('#mobile-nav').isVisible(),false);await f.safe();
   }
   for(const href of ['#/account','#/purchases','#/privacy','#/purchase-info'])assert(await page.locator('a[href="'+href+'"]').count()>0);
   assert.equal(f.requests.filter(url=>url.startsWith('https://api.github.com/')).length,1);
   assert(!f.requests.some(url=>url.includes('/papers/'+fixture.codes.hiddenSemester+'/')||url.includes('/papers/'+fixture.codes.hiddenBranch+'/')));
   await f.context.close();++checks;console.log(scenario+': compact home, search, five branches, semesters, prices/free reader, saved data, menu and CSP passed');
  }
  scenario='keyboard focus, reduced motion and translated chrome';
  const f=await contextFor(browser,390,'en'),{page}=f;await page.emulateMedia({reducedMotion:'reduce'});
  await page.goto(origin+'/#/');await page.locator('#home-search').waitFor();await page.keyboard.press('Tab');
  assert.equal(await page.evaluate(()=>document.activeElement.className),'skip-link');
  await page.keyboard.press('Enter');assert.equal(await page.evaluate(()=>document.activeElement.id),'main');await page.locator('#home-search').waitFor();
  await page.locator('#lang-toggle').click();await page.waitForFunction(()=>document.documentElement.lang==='gu');
  assert.equal(await page.locator('.footer-tools summary').textContent(),'વધુ સાધનો');
  await page.locator('#lang-toggle').click();await page.waitForFunction(()=>document.documentElement.lang==='en');
  const motion=await page.locator('main .branch-card').first().evaluate(el=>({transition:getComputedStyle(el).transitionDuration,animation:getComputedStyle(el).animationName,scroll:getComputedStyle(document.documentElement).scrollBehavior}));
  assert.equal(motion.transition,'0s');assert.equal(motion.animation,'none');assert.equal(motion.scroll,'auto');await f.safe();await f.context.close();++checks;
  console.log(checks+' offline redesigned-navigation scenarios passed; no cloud/payment call or source deletion.');
 }finally{await browser.close();}
})().catch(error=>{
 const detail=('Offline navigation browser ('+scenario+'): '+String(error.stack||error)).slice(0,8000);
 console.error('::error::'+detail.replaceAll('%','%25').replaceAll('\r','%0D').replaceAll('\n','%0A'));console.error(error);process.exitCode=1;
});
