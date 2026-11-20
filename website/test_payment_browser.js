// OFFLINE Chromium: packaged SPA/controller + real payment/Auth adapter,
// with only Firebase, HTTP and Checkout-provider boundaries replaced. Every
// request is fulfilled locally; no owner/cloud/provider call or charge occurs.
// NODE_PATH="$PWD/build/auth-browser-tools/node_modules:$PWD/website/node_modules" node website/test_payment_browser.js
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {build}=require('esbuild'),{chromium:playwright}=require('playwright');
const root=path.resolve(__dirname,'..'),site=path.resolve(process.argv[2]||path.join(root,'build/netlify-site'));
const origin='https://www.diplomaone.in',code='DI03000161',other='DI03000171',session='summer-2026',id=code+'--'+session;
const readerId='a'.repeat(64),imageId='b'.repeat(64),pdfId='c'.repeat(64),keyId='rzp_live_OfflineFixtureOnly';
const png=Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+a7ioAAAAASUVORK5CYII=','base64');
const pdf=Buffer.from('%PDF-offline-fixture');
const reader=Buffer.from('<main><section><h2>Question 1</h2><details><summary><strong class="en">Q.1 (c) OR · Protected question</strong><strong class="gu">Q.1 (c) OR · ખાનગી પ્રશ્ન</strong></summary><div class="answer"><div class="en"><p>PRIVATE SELECTED ANSWER <span class="frac"><span class="num">a</span><span class="den">b</span></span></p></div><div class="gu"><p>ખાનગી પસંદ કરેલો જવાબ</p></div><figure><img src="summer-2026.assets/0001.png" alt="Protected diagram"></figure></div></details></section></main>');
const assets=[{id:readerId,path:session+'.html',mime:'text/plain; charset=utf-8',bytes:reader.length},
 {id:imageId,path:session+'.assets/0001.png',mime:'image/png',bytes:png.length},{id:pdfId,path:session+'.solution.pdf',mime:'application/pdf',bytes:pdf.length}];
const catalog={branches:[{key:'mechanical',code:'19',name:{en:'Mechanical Engineering',gu:'મિકેનિકલ એન્જિનિયરિંગ'},semesters:{'3':[code,other]}}],
 subjects:{[code]:{code,name:{en:'Manufacturing Engineering I',gu:'મેન્યુફેક્ચરિંગ એન્જિનિયરિંગ I'},status:'available'},[other]:{code:other,name:{en:'Metrology'},status:'available'}}};
const firebaseBoundary=`
const auth={currentUser:null,authStateReady:()=>Promise.resolve()};let notify;
export const initializeApp=()=>({});export const initializeAuth=()=>auth;
export const browserSessionPersistence={},browserPopupRedirectResolver={};
export class GoogleAuthProvider{setCustomParameters(){}}
export function onAuthStateChanged(a,next){notify=next;next(null);return()=>{};}
export function signInWithPopup(){const f=window.__paymentFixture;f.gestures.push(navigator.userActivation.isActive);auth.currentUser=f.user;notify(f.user);return Promise.resolve();}
export function signOut(){auth.currentUser=null;notify(null);return Promise.resolve();}
`;
const checkoutBoundary=`window.Razorpay=class {constructor(settings){window.__paymentFixture.checkout=settings;this.settings=settings;this.events={};}on(name,cb){this.events[name]=cb;}open(){window.__paymentFixture.opens++;}close(){this.settings.modal.ondismiss();}};`;
async function fixture(browser,bundle,{width=1365,language='en',enabled=true,pending=false,pageOrigin=origin}={}){
 const context=await browser.newContext({viewport:{width,height:960},acceptDownloads:true}),owned=new Set(),requests=[],errors=[],unexpected=[];
 let orders=0,verifications=0;
 const products=[id,other+'--'+session].map(value=>({id:value,title:'Manufacturing I · Summer 2026',branch:'mechanical',amount:2900,currency:'INR'}));
 await context.route('**/*',async route=>{
  const request=route.request(),url=new URL(request.url()),headers=await request.allHeaders();requests.push(url.href);
  if(url.href==='https://checkout.razorpay.com/v1/checkout.js'){
   assert(!headers.authorization,'Google token must never be sent to Razorpay');return route.fulfill({contentType:'text/javascript',body:checkoutBoundary});
  }
  if(url.origin==='https://api.github.com')return route.fulfill({json:{truncated:false,tree:[code,other].map(c=>({path:`papers/${c}/${session}.json`,type:'blob',mode:'100644'}))}});
  if(url.origin!==pageOrigin){unexpected.push(url.origin);return route.abort();}
  if(url.pathname==='/assets/firebase-auth.js')return route.fulfill({contentType:'text/javascript',body:bundle});
  if(url.pathname==='/data/catalog.json')return route.fulfill({json:catalog});
  if(url.pathname.startsWith('/api/payments/live/')){
   const suffix=url.pathname.slice('/api/payments/live'.length);
   if(suffix==='/config')return route.fulfill({json:{mode:'live',enabled,keyId,currency:'INR',products:enabled?products:[]}});
   assert.equal(headers.authorization,'Bearer PRIVATE_UID.offlineFixture.signature');
   assert(!url.search);if(request.method()==='POST')assert.equal(headers.origin,pageOrigin);
   if(suffix==='/orders'){
    ++orders;const body=request.postDataJSON();assert.equal(body.productId,id);assert.equal(body.amount,undefined);
    return route.fulfill({status:201,json:{mode:'live',productId:id,keyId,orderId:'order_OfflineFixture',amount:2900,currency:'INR'}});
   }
   if(suffix==='/verify'){
    ++verifications;if(pending)return route.fulfill({status:409,json:{mode:'live',error:'payment_not_captured_or_mismatch'}});
    owned.add(id);return route.fulfill({json:{mode:'live',productId:id,owned:true}});
   }
   if(suffix==='/purchases')return route.fulfill({json:{mode:'live',purchases:owned.has(id)?[{productId:id,title:'Manufacturing I',branch:'mechanical',amount:2900,currency:'INR',active:true,purchasedAt:'2026-10-30T00:00:00.000Z'}]:[]}});
   const parts=/^\/content\/([^/]+)(?:\/([^/]+))?$/.exec(suffix);assert(parts);
   if(!owned.has(parts[1]))return route.fulfill({status:403,json:{mode:'live',error:'purchase_required'}});
   if(!parts[2])return route.fulfill({json:{mode:'live',productId:parts[1],readerAsset:readerId,assets}});
   const asset=assets.find(a=>a.id===parts[2]);assert(asset);
   return route.fulfill({contentType:asset.mime,body:asset.id===readerId?reader:asset.id===imageId?png:pdf});
  }
  const relative=url.pathname==='/'?'index.html':url.pathname.slice(1),file=path.resolve(site,relative);
  if(!file.startsWith(site+path.sep)||!fs.existsSync(file)||!fs.statSync(file).isFile()){unexpected.push(relative);return route.abort();}
  const mime=relative.endsWith('.html')?'text/html':relative.endsWith('.js')?'text/javascript':relative.endsWith('.css')?'text/css':relative.endsWith('.ttf')?'font/ttf':relative.endsWith('.svg')?'image/svg+xml':'application/octet-stream';
  return route.fulfill({contentType:mime,body:fs.readFileSync(file)});
 });
 const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
 await page.addInitScript(language=>{
  localStorage.setItem('diplomaone.website.lang',JSON.stringify(language));window.__paymentCsp=[];
  document.addEventListener('securitypolicyviolation',e=>window.__paymentCsp.push(e.violatedDirective+':'+e.blockedURI));
  window.__paymentFixture={gestures:[],opens:0,user:{uid:'PRIVATE_UID',displayName:'Offline Student',email:'fixture@example.test',emailVerified:true,
   getIdToken:()=>Promise.resolve('PRIVATE_UID.offlineFixture.signature')}};
 },language);
 const safe=async()=>{
  assert.deepEqual(unexpected,[]);assert.deepEqual(errors,[]);assert.deepEqual(await page.evaluate(()=>window.__paymentCsp),[]);
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'horizontal overflow');
  assert(!(await page.locator('main').textContent()).includes('offlineFixture.signature'));
  assert(!requests.some(url=>url.includes('/diplomaone-content/papers/')),'paid public fallback is forbidden');
  assert.equal(await page.locator('iframe,object,embed').count(),0);
 };
 return {context,page,requests,safe,owned,orders:()=>orders,verifications:()=>verifications,
  start:()=>page.goto(pageOrigin+'/#/paper/'+code+'/'+session),
  callback:()=>page.evaluate(()=>window.__paymentFixture.checkout.handler({razorpay_order_id:'order_OfflineFixture',razorpay_payment_id:'pay_OfflineFixture',razorpay_signature:'0'.repeat(64)}))};
}
let scenario='browser startup';
(async()=>{
 const bundle=await build({entryPoints:[path.join(__dirname,'auth/firebase-client.js')],write:false,bundle:true,platform:'browser',format:'esm',logLevel:'silent',plugins:[{
  name:'offline-firebase-boundary',setup(build){build.onResolve({filter:/^@firebase\//},args=>{assert(['@firebase/app','@firebase/auth'].includes(args.path));return {path:args.path,namespace:'fixture'};});
   build.onLoad({filter:/.*/,namespace:'fixture'},()=>({contents:firebaseBoundary}));}}]});
 const module=process.env.CHROMIUM_EXECUTABLE_PATH?null:require('@sparticuz/chromium'),packaged=module?.default||module;
 if(module){const lib=await module.inflate(path.resolve(path.dirname(require.resolve('@sparticuz/chromium')),'../bin/al2023.tar.br'));module.setupLambdaEnvironment(path.join(lib,'lib'));}
 const args=packaged?packaged.args.filter(arg=>!['--disable-web-security','--allow-running-insecure-content','--single-process'].includes(arg)):['--no-sandbox'];
 const browser=await playwright.launch({executablePath:process.env.CHROMIUM_EXECUTABLE_PATH||await packaged.executablePath(),args,headless:true});
 fs.mkdirSync(path.join(root,'build/payment-browser'),{recursive:true});let checks=0;
 try{
  for(const width of [1365,390,320])for(const language of ['en','gu']){
   scenario=width+'px '+language;
   const f=await fixture(browser,bundle.outputFiles[0].text,{width,language}),{page}=f;
   await f.start();await page.waitForFunction(()=>document.querySelector('#paper-signin')?.disabled===false);
   await page.evaluate(()=>document.fonts.ready);assert(await page.evaluate(()=>document.fonts.check('38px "Noto Gujarati"','₹')),'self-hosted rupee glyph must load');
   assert.equal(f.orders(),0);assert((await page.locator('.paper-price').textContent()).includes('₹29'));await f.safe();
   if(width===390&&language==='en')await page.screenshot({path:path.join(root,'build/payment-browser/locked-mobile.png'),fullPage:true});
   await page.locator('#paper-signin').click();await page.waitForFunction(()=>document.querySelector('#buy-paper')?.disabled===false);
   assert.deepEqual(await page.evaluate(()=>window.__paymentFixture.gestures),[true]);
   await page.locator('#buy-paper').click();await page.waitForFunction(()=>window.__paymentFixture.opens===1);assert.equal(f.orders(),1);
   assert.equal(await page.locator('.solved-paper').count(),0);await f.callback();await page.locator('.solved-paper details').waitFor();
   assert((await page.locator('.solved-paper').textContent()).includes(language==='en'?'PRIVATE SELECTED ANSWER':'ખાનગી પસંદ કરેલો જવાબ'));
   assert((await page.locator('summary').textContent()).includes('OR'));if(language==='en')assert.equal(await page.locator('.frac .num').count(),1);
   await page.locator('[data-paper-expand="true"]').click();await page.waitForFunction(()=>document.querySelector('img[data-private-asset]')?.naturalWidth>0);
   assert((await page.locator('img[data-private-asset]').getAttribute('src')).startsWith('blob:'));
   await page.locator('.paper-enlarge').click();await page.locator('dialog[open]').waitFor();await page.locator('.paper-image-toolbar button').last().click();
   const download=page.waitForEvent('download');await page.locator('[data-private-download]').click();assert.equal((await download).suggestedFilename(),session+'.solution.pdf');
   await f.safe();if(width===390&&language==='en')await page.screenshot({path:path.join(root,'build/payment-browser/unlocked-mobile.png'),fullPage:true});
   await page.locator('.private-paper-status a').click();await page.locator('.purchase-item a').waitFor();await f.safe();
   await page.reload();await page.waitForFunction(()=>document.querySelector('#account-signin')?.disabled===false);
   await page.locator('#account-signin').click();await page.locator('.purchase-item a').waitFor();assert.equal(f.orders(),1);
   await page.locator('.purchase-item a').click();await page.locator('.solved-paper details').waitFor();
   await page.evaluate(({other,session})=>location.hash='#/paper/'+other+'/'+session,{other,session});
   await page.waitForFunction(()=>document.querySelector('#buy-paper')?.disabled===false);assert.equal(await page.locator('.solved-paper').count(),0);assert.equal(f.orders(),1);
   await f.safe();await f.context.close();++checks;console.log(`${width}px ${language}: locked → captured selected cards, images/PDF, reload, other-paper denial and CSP/layout passed`);
  }
  for(const mode of ['off','pending','navigation']){
   scenario=mode;
   const f=await fixture(browser,bundle.outputFiles[0].text,{enabled:mode!=='off',pending:mode==='pending'}),{page}=f;
   await f.start();await page.waitForFunction(()=>document.querySelector('#paper-signin')?.disabled===false);await page.locator('#paper-signin').click();
   if(mode==='off'){
    await page.waitForFunction(()=>document.querySelector('#paper-payment-status')?.textContent.includes('not open yet'));assert(await page.locator('#buy-paper').isDisabled());assert.equal(f.orders(),0);
    assert(!f.requests.some(url=>url.includes('checkout.razorpay.com')));
   }else{
    await page.waitForFunction(()=>document.querySelector('#buy-paper')?.disabled===false);await page.locator('#buy-paper').click();await page.waitForFunction(()=>window.__paymentFixture.opens===1);
    if(mode==='navigation'){
     await page.evaluate(()=>{location.hash='#/privacy';window.__paymentFixture.checkout.handler({razorpay_order_id:'order_OfflineFixture',razorpay_payment_id:'pay_OfflineFixture',razorpay_signature:'0'.repeat(64)});});
     await page.waitForFunction(()=>document.querySelector('.page-title')?.textContent==='Privacy');assert.equal(f.verifications(),0);
    }else{await f.callback();await page.waitForFunction(()=>document.querySelector('#paper-payment-status')?.textContent.includes('not been confirmed as fully captured'));}
   }
   assert.equal(await page.locator('.solved-paper').count(),0);await f.safe();await f.context.close();++checks;
  }
  console.log(`${checks} offline Chromium live-flow scenarios passed; no real payment/cloud call was made.`);
 }finally{await browser.close();}
})().catch(error=>{
 const detail=('Offline payment browser ('+scenario+'): '+String(error.stack||error)).slice(0,8000);
 console.error('::error::'+detail.replaceAll('%','%25').replaceAll('\r','%0D').replaceAll('\n','%0A'));
 console.error(error);process.exitCode=1;
});
