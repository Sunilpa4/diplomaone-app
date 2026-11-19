// Optional real-Chromium regression test. Start with:
// python3 tools/preview_paper_cards.py
// Dependencies: playwright@1.56.1 and @sparticuz/chromium@153.0.0 (or set
// CHROMIUM_EXECUTABLE_PATH). Uses the production JS/CSP with local, CORS-enabled
// responses for the exact trusted GitHub URLs, so no external network is needed.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium:playwright}=require('playwright');
const root=path.resolve(__dirname,'..'),base=process.env.PAPER_TEST_URL||'http://127.0.0.1:4173';
 const content='https://sunilpa4.github.io/diplomaone-content/papers/';
const staged=path.join(root,'papers-upload/papers');
const tree=JSON.stringify({truncated:false,tree:fs.readdirSync(staged,{recursive:true})
 .filter(rel=>fs.statSync(path.join(staged,rel)).isFile())
 .map(rel=>({path:'papers/'+rel.split(path.sep).join('/'),type:'blob',mode:'100644'}))});
(async()=>{
 const packagedModule=process.env.CHROMIUM_EXECUTABLE_PATH?null:require('@sparticuz/chromium');
 const packaged=packagedModule?.default||packagedModule;
 if(packagedModule) {
  // The sandbox is minimal Debian, not Lambda. Use the package's NSS/NSPR
  // libraries without installing system packages or disabling web security.
  const lib=await packagedModule.inflate(path.resolve(path.dirname(require.resolve('@sparticuz/chromium')),'../bin/al2023.tar.br'));
  packagedModule.setupLambdaEnvironment(path.join(lib,'lib'));
 }
 const args=packaged?packaged.args.filter(arg=>!['--disable-web-security','--allow-running-insecure-content','--single-process'].includes(arg)):['--no-sandbox'];
 const browser=await playwright.launch({executablePath:process.env.CHROMIUM_EXECUTABLE_PATH||await packaged.executablePath(),args,headless:true});
 const cases=[
  ['DI03006041','summer-2026','en',28],
  ['DI01005021','winter-2025','en',28],
  ['4350501','winter-2025','gu',28],
  ['DI01000021','summer-2026','gu',38],
  ['DI01000121','winter-2025','gu',38],
  ['DI02000161','summer-2026','en',28],
  ['DI03000081','summer-2026','gu',28],
  ['DI01000081','summer-2026','gu',28],
  ['DI01000181','winter-2025','gu',28],
  ['DI04019011','summer-2026','en',28],
 ];
 fs.mkdirSync(path.join(root,'build/card-browser'),{recursive:true});
 for(const [label,viewport] of [['desktop',{width:1365,height:960}],['mobile',{width:390,height:844}]]) {
  const context=await browser.newContext({viewport});
  await context.route('**/app.js',r=>r.fulfill({contentType:'text/javascript',body:fs.readFileSync(path.join(root,'website/app.js'),'utf8')}));
  await context.route('https://api.github.com/repos/Sunilpa4/diplomaone-content/git/trees/main?recursive=1',r=>r.fulfill({contentType:'application/json',headers:{'Access-Control-Allow-Origin':'*'},body:tree}));
  await context.route(content+'**',async r=>{
   const rel=decodeURIComponent(new URL(r.request().url()).pathname.split('/papers/')[1]);
   const file=path.resolve(root,'papers-upload/papers',rel);
   assert(file.startsWith(path.join(root,'papers-upload/papers')+path.sep));
   assert(fs.existsSync(file),'Missing reader asset: '+rel);
   const mime=file.endsWith('.html')?'text/html':file.endsWith('.png')?'image/png':file.endsWith('.webp')?'image/webp':'application/pdf';
   await r.fulfill({contentType:mime,headers:{'Access-Control-Allow-Origin':'*'},body:fs.readFileSync(file)});
  });
  for(const [code,session,language,count] of cases) {
   const page=await context.newPage(),errors=[];
   page.on('pageerror',e=>errors.push(e.message));
   await page.addInitScript(language=>{
    localStorage.setItem('diplomaone.website.lang',JSON.stringify(language));
    window.__paperCsp=[];document.addEventListener('securitypolicyviolation',e=>window.__paperCsp.push(e.violatedDirective+':'+e.blockedURI));
   },language);
   await page.goto(`${base}/#/paper/${code}/${session}`,{waitUntil:'networkidle'});
   await page.locator('.solved-paper details.card').first().waitFor();
   assert.equal(await page.locator('.solved-paper details.card').count(),count,`${label} ${code}`);
   assert.equal(await page.locator('iframe,object,embed').count(),0);
   assert.equal(await page.locator('details.card[open]').count(),0);
   await page.locator('details.card summary').first().click();
   assert.equal(await page.locator('details.card[open]').count(),1);
   const imageCard=page.locator('details.card:has(figure img)').first();
   await imageCard.evaluate(e=>{e.open=true;});
   const figure=imageCard.locator('figure').first(),image=figure.locator('img');
   await image.scrollIntoViewIfNeeded();
   await image.evaluate(img=>new Promise((resolve,reject)=>{if(img.complete)return img.naturalWidth?resolve():reject(Error('Image failed'));img.onload=resolve;img.onerror=()=>reject(Error('Image failed'));}));
   assert(await image.evaluate(img=>img.naturalWidth>0));
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`${label} ${code} horizontal page overflow`);
   await figure.locator('button.paper-enlarge').click();
   const dialog=page.locator('dialog[open]');await dialog.waitFor({state:'visible'});
   await dialog.locator('button').first().click();
   assert(await dialog.evaluate(el=>el.classList.contains('at-original-size')));
   if(label==='mobile')assert(await dialog.locator('.paper-image-stage').evaluate(el=>{
    const img=el.querySelector('img');return img.naturalWidth<=el.clientWidth||el.scrollWidth>el.clientWidth;
   }),'large original-size image can scroll on mobile');
   if(['DI03006041','DI01000021','DI03000081'].includes(code))await page.screenshot({path:path.join(root,'build/card-browser',`${label}-${code}-${language}-enlarged.png`)});
   await page.keyboard.press('Escape');await dialog.waitFor({state:'hidden'});
   assert(await figure.locator('button.paper-enlarge').evaluate(el=>el===document.activeElement));
   if(code==='DI02000161')assert.equal(await page.locator('.paper-erratum').count(),2);
   if(code==='DI01000021')assert((await page.locator('.solved-paper').textContent()).includes('English only'));
   if(code==='DI03006041') {
    await page.locator('[data-paper-expand="true"]').click();assert.equal(await page.locator('details.card[open]').count(),count);
    await page.locator('[data-paper-expand="false"]').click();assert.equal(await page.locator('details.card[open]').count(),0);
    await page.locator('details.card summary').first().click();
   }
   assert.deepEqual(errors,[]);assert.deepEqual(await page.evaluate(()=>window.__paperCsp),[],'source image must pass production CSP');
   await page.locator('details.card').first().evaluate(e=>window.scrollTo({top:e.getBoundingClientRect().top+window.scrollY-95,behavior:'instant'}));
   await page.screenshot({path:path.join(root,'build/card-browser',`${label}-${code}-${language}.png`),fullPage:false});
   console.log(label,code,session,language,count,'cards; images, dialog, CSP and layout passed');
   await page.close();
  }
  await context.close();
 }
 await browser.close();
 console.log('20 real-browser paper/language/viewport checks passed.');
})().catch(e=>{console.error(e);process.exit(1);});
