// Optional OFFLINE Chromium validation of the shipped UI + real request helper.
// All document/assets/HTTP responses are fulfilled from local files/fixtures,
// even when using the test hostname. No real hosting/Google/Firestore is called.
// npm install --prefix build/auth-browser-tools --no-save --ignore-scripts --no-package-lock playwright@1.56.1 @sparticuz/chromium@153.0.0
// python3 tools/build_netlify_site.py
// NODE_PATH="$PWD/build/auth-browser-tools/node_modules:$PWD/website/node_modules" node website/test_connection_browser.js
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {build}=require('esbuild'),{chromium:playwright}=require('playwright');
const root=path.resolve(__dirname,'..'),site=path.resolve(process.argv[2]||path.join(root,'build/netlify-site'));
const testOrigin='https://vermillion-pothos-520a34.netlify.app',token='offlineFixture.onlyNotReal.signature';
const success={mode:'test',database:'firestore',readable:true,readOnly:true,checkoutEnabled:false,paymentsVerified:false};
const sdkBoundary=`
const auth={currentUser:null,authStateReady:()=>Promise.resolve()};let notify;
export const initializeApp=()=>({});
export const initializeAuth=()=>auth;
export const browserSessionPersistence={},browserPopupRedirectResolver={};
export class GoogleAuthProvider{setCustomParameters(){}}
export function onAuthStateChanged(a,next){notify=next;next(null);return()=>{};}
export function signInWithPopup(){const f=window.__connectionFixture;f.gestures.push(navigator.userActivation.isActive);auth.currentUser=f.user;notify(f.user);return Promise.resolve({accessToken:'NEVER_RENDER'});}
export function signOut(){auth.currentUser=null;notify(null);return Promise.resolve();}
`;
async function fixture(browser,origin,width,language,boundary){
  const context=await browser.newContext({viewport:{width,height:960}}),http=[],external=[],unexpected=[],errors=[];
  const mode={value:'success'};
  await context.route('**/*',async route=>{
    const request=route.request(),url=new URL(request.url());
    if(url.origin!==origin){external.push(url.origin);return route.abort();}
    if(url.pathname==='/api/payments/test/connection'){
      http.push(request.method());assert.equal(request.method(),'POST');assert.equal(request.postData(),'{}');
      const headers=await request.allHeaders();assert.equal(headers.authorization,'Bearer '+token);assert.equal(headers.origin,origin);
      if(mode.value==='html')return route.fulfill({contentType:'text/html',body:'<html>NEVER_RENDER hosting gate</html>'});
      if(mode.value==='redirect')return route.fulfill({status:307,headers:{Location:'https://must-never-follow.invalid/private'}});
      return route.fulfill({status:mode.value==='success'?200:403,contentType:'application/json',
        body:JSON.stringify(mode.value==='success'?{...success,documents:['NEVER_RENDER'],uid:'NEVER_RENDER'}:
          {mode:'test',error:mode.value,message:'NEVER_RENDER',private_key:'NEVER_RENDER'})});
    }
    if(url.pathname==='/assets/firebase-auth.js')return route.fulfill({contentType:'text/javascript',body:boundary});
    const relative=url.pathname==='/'?'index.html':url.pathname.slice(1),file=path.resolve(site,relative);
    if(!file.startsWith(site+path.sep)||!fs.existsSync(file)||!fs.statSync(file).isFile()){
      unexpected.push(relative);return route.abort();
    }
    const mime=relative.endsWith('.html')?'text/html':relative.endsWith('.js')?'text/javascript':relative.endsWith('.css')?'text/css':
      relative.endsWith('.ttf')?'font/ttf':relative.endsWith('.svg')?'image/svg+xml':'application/octet-stream';
    return route.fulfill({contentType:mime,body:fs.readFileSync(file)});
  });
  const page=await context.newPage();page.on('pageerror',error=>errors.push(error.message));
  await page.addInitScript(({language,token})=>{
    localStorage.setItem('diplomaone.website.lang',JSON.stringify(language));
    localStorage.setItem('diplomaone.website.saved','[]');window.__connectionCsp=[];
    document.addEventListener('securitypolicyviolation',e=>window.__connectionCsp.push(e.violatedDirective+':'+e.blockedURI));
    const f=window.__connectionFixture={tokenCalls:0,gestures:[],deferToken:false};
    f.user={uid:'PRIVATE_UID',displayName:'PRIVATE_NAME',email:'private@example.test',emailVerified:true,
      getIdToken(){++f.tokenCalls;return f.deferToken?new Promise(resolve=>{f.releaseToken=()=>resolve(token);}):Promise.resolve(token);}};
  },{language,token});
  async function assertSafe(){
    const text=await page.locator('main').textContent();
    for(const value of ['PRIVATE_UID','PRIVATE_NAME','private@example.test','NEVER_RENDER',token])assert(!text.includes(value),value+' leaked into UI');
    assert.deepEqual(external,[]);assert.deepEqual(unexpected,[]);assert.deepEqual(errors,[]);
    assert.deepEqual(await page.evaluate(()=>window.__connectionCsp),[]);
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'horizontal overflow');
    assert.equal(await page.locator('main form,main input,main iframe,main object,main embed,[data-checkout]').count(),0);
  }
  return {context,page,http,mode,assertSafe};
}
(async()=>{
  const result=await build({entryPoints:[path.join(__dirname,'auth/firebase-client.js')],write:false,bundle:true,
    platform:'browser',format:'esm',logLevel:'silent',plugins:[{name:'offline-auth-boundary',setup(build){
      build.onResolve({filter:/^@firebase\//},args=>{assert(['@firebase/app','@firebase/auth'].includes(args.path));return {path:args.path,namespace:'offline'};});
      build.onLoad({filter:/.*/,namespace:'offline'},()=>({contents:sdkBoundary}));
    }}]});
  const module=process.env.CHROMIUM_EXECUTABLE_PATH?null:require('@sparticuz/chromium'),packaged=module?.default||module;
  if(module){const lib=await module.inflate(path.resolve(path.dirname(require.resolve('@sparticuz/chromium')),'../bin/al2023.tar.br'));module.setupLambdaEnvironment(path.join(lib,'lib'));}
  const args=packaged?packaged.args.filter(arg=>!['--disable-web-security','--allow-running-insecure-content','--single-process'].includes(arg)):['--no-sandbox'];
  const browser=await playwright.launch({executablePath:process.env.CHROMIUM_EXECUTABLE_PATH||await packaged.executablePath(),args,headless:true});
  try{
    fs.mkdirSync(path.join(root,'build/connection-browser'),{recursive:true});let checks=0;
    for(const width of [1365,390,320])for(const language of ['en','gu']){
      const f=await fixture(browser,testOrigin,width,language,result.outputFiles[0].text),{page}=f;
      await page.goto(testOrigin+'/#/test-connection');await page.waitForFunction(()=>document.querySelector('#account-signin')?.disabled===false);
      assert.equal(f.http.length,0);assert.equal(await page.locator('#connection-check').isDisabled(),true);
      await page.locator('#account-signin').click();await page.waitForFunction(()=>document.querySelector('#connection-check')?.disabled===false);
      assert.equal(f.http.length,0);assert.equal(await page.evaluate(()=>window.__connectionFixture.tokenCalls),0);
      f.mode.value='tester_not_allowed';await page.locator('#connection-check').click();
      await page.locator('#connection-result[role="alert"]').waitFor();assert.equal(f.http.length,1);
      assert((await page.locator('#connection-result').textContent()).includes('PAYMENTS_TESTER_UIDS'));
      f.mode.value='success';await page.locator('#connection-check').click();
      await page.waitForFunction(()=>document.querySelector('#connection-result')?.textContent.includes(document.documentElement.lang==='gu'?'વાંચન સફળ':'read succeeded'));
      assert.equal(f.http.length,2);await page.waitForFunction(()=>document.activeElement?.id==='connection-result');
      await page.evaluate(()=>document.fonts.ready);await f.assertSafe();
      await page.screenshot({path:path.join(root,'build/connection-browser',width+'-'+language+'.png'),fullPage:true});
      await page.locator('#lang-toggle').click();assert.equal(f.http.length,2);await f.assertSafe();
      // Cancel before token resolution: neither logout nor navigating back may
      // allow that old token to start a request after the user left the screen.
      await page.evaluate(()=>window.__connectionFixture.deferToken=true);await page.locator('#connection-check').click();
      await page.waitForFunction(()=>window.__connectionFixture.tokenCalls===3);
      await page.locator('#account-signout').click();await page.locator('#account-signin').waitFor();
      await page.evaluate(()=>window.__connectionFixture.releaseToken());await page.evaluate(()=>new Promise(requestAnimationFrame));
      assert.equal(f.http.length,2);assert.equal(await page.locator('#connection-result').textContent(),'');
      await page.locator('#account-signin').click();await page.waitForFunction(()=>document.querySelector('#connection-check')?.disabled===false);
      await page.locator('#connection-check').click();await page.waitForFunction(()=>window.__connectionFixture.tokenCalls===4);
      await page.locator('main a[href="#/privacy"]').click();await page.waitForFunction(()=>location.hash==='#/privacy');
      await page.evaluate(()=>window.__connectionFixture.releaseToken());await page.evaluate(()=>new Promise(requestAnimationFrame));
      assert.equal(f.http.length,2);await page.evaluate(()=>location.hash='#/test-connection');
      await page.waitForFunction(()=>document.querySelector('#connection-check')?.disabled===false);
      assert.equal(f.http.length,2);assert.equal(await page.locator('#connection-result').textContent(),'');
      assert.deepEqual(await page.evaluate(()=>window.__connectionFixture.gestures),[true,true]);await f.assertSafe();
      await f.context.close();++checks;console.log(width+'px '+language+': manual request, protected error/success, token/logout/navigation cancellation, layout/CSP passed');
    }
    const f=await fixture(browser,testOrigin,1280,'en',result.outputFiles[0].text);
    await f.page.goto(testOrigin+'/#/test-connection');await f.page.waitForFunction(()=>document.querySelector('#account-signin')?.disabled===false);
    await f.page.locator('#account-signin').click();await f.page.waitForFunction(()=>document.querySelector('#connection-check')?.disabled===false);
    for(const mode of ['html','redirect']){
      f.mode.value=mode;await f.page.locator('#connection-check').click();await f.page.locator('#connection-result[role="alert"]').waitFor();
      assert((await f.page.locator('#connection-result').textContent()).includes('check is unavailable'));await f.assertSafe();
    }
    await f.context.close();++checks;console.log('Hosting HTML/redirect failures are sanitized and redirects never followed');
    for(const origin of ['https://www.diplomaone.in','https://deploy-preview-37--vermillion-pothos-520a34.netlify.app']){
      const f=await fixture(browser,origin,390,'en',result.outputFiles[0].text);
      await f.page.goto(origin+'/#/test-connection');await f.page.locator('main .account-phase-note').waitFor();
      assert((await f.page.locator('main').textContent()).includes('only on the protected test site'));
      assert.equal(await f.page.evaluate(()=>window.DiplomaOneAuth.snapshot().status),'idle');assert.equal(f.http.length,0);await f.assertSafe();
      await f.context.close();++checks;
    }
    console.log(checks+' offline diagnostic browser scenarios passed; no live OAuth, database or deployment acceptance is claimed.');
  }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
