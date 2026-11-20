// Optional offline Chromium checks for the shipped scripts/CSP and responsive UI.
// No real Google sign-in, Firebase console changes, payments or external calls.
// Install dependencies in an ignored folder, then run with the preview server:
// npm install --prefix build/auth-browser-tools --no-save --ignore-scripts --no-package-lock playwright@1.56.1 @sparticuz/chromium@153.0.0
// NODE_PATH="$PWD/build/auth-browser-tools/node_modules:$PWD/website/node_modules" node website/test_account_browser.js
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium:playwright}=require('playwright');
const root=path.resolve(__dirname,'..'),base=process.env.ACCOUNT_TEST_URL||'http://127.0.0.1:8000';
const origin=new URL(base).origin,out=path.join(root,'build/account-browser');
const mockSDK=`export function createClient(onUser){
  const f=window.__accountFixture;f.emit=onUser;
  return {ready(){onUser(null);return Promise.resolve();},dispose(){},
    signIn(language){f.signIns.push({language,gesture:navigator.userActivation.isActive});
      if(f.error)return Promise.reject({code:f.error,message:'NEVER-RENDER'});
      onUser(f.user);return Promise.resolve({accessToken:'NEVER-RENDER'});},
    signOut(){if(f.error)return Promise.reject({code:f.error});onUser(null);return Promise.resolve();}
  };
}`;
async function layout(page,label){
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),label+' horizontal overflow');
  assert(await page.locator('.account-card').evaluate(el=>el.getBoundingClientRect().width<=innerWidth),label+' card fits');
  const csp=await page.evaluate(()=>window.__accountCsp);assert.deepEqual(csp,[],label+' unexpected CSP violation');
}
(async()=>{
  const module=process.env.CHROMIUM_EXECUTABLE_PATH?null:require('@sparticuz/chromium'),packaged=module?.default||module;
  if(module){const lib=await module.inflate(path.resolve(path.dirname(require.resolve('@sparticuz/chromium')),'../bin/al2023.tar.br'));module.setupLambdaEnvironment(path.join(lib,'lib'));}
  const args=packaged?packaged.args.filter(arg=>!['--disable-web-security','--allow-running-insecure-content','--single-process'].includes(arg)):['--no-sandbox'];
  const browser=await playwright.launch({executablePath:process.env.CHROMIUM_EXECUTABLE_PATH||await packaged.executablePath(),args,headless:true});
  fs.mkdirSync(out,{recursive:true});let checks=0;
  try{
    for(const [width,height] of [[1365,960],[1024,900],[768,960],[390,844],[320,740]])for(const language of ['en','gu']){
      const context=await browser.newContext({viewport:{width,height}}),requests=[],errors=[];
      await context.route('**/*',r=>new URL(r.request().url()).origin===origin?r.continue():r.abort());
      await context.route('**/assets/firebase-auth.js',r=>r.fulfill({contentType:'text/javascript',body:mockSDK}));
      const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>requests.push(r.url()));
      await page.addInitScript(language=>{
        localStorage.setItem('diplomaone.website.lang',JSON.stringify(language));
        localStorage.setItem('diplomaone.website.saved','[{"code":"DI03000161","unit":1}]');
        window.__accountCsp=[];document.addEventListener('securitypolicyviolation',e=>window.__accountCsp.push(e.violatedDirective+':'+e.blockedURI));
        window.__accountFixture={signIns:[],error:null,user:{uid:'PRIVATE-UID',displayName:'Test Student',email:'student@example.test',emailVerified:true,photoURL:'https://invalid.test/tracker',accessToken:'NEVER-RENDER'}};
      },language);
      await page.goto(base+'/#/account');await page.waitForFunction(()=>document.querySelector('#account-signin')?.disabled===false);
      const label=width+'px '+language;
      await layout(page,label);assert.equal(await page.locator('iframe,object,embed').count(),0);
      assert(!requests.some(url=>url.includes('/data/')||url.includes('api.github.com')),'account is catalog-independent');
      if(width===1365||width===390)await page.screenshot({path:path.join(out,label.replace(' ','-')+'-signed-out.png'),fullPage:true});
      // Check an actionable, translated popup error before a successful mock sign-in.
      await page.evaluate(()=>window.__accountFixture.error='auth/popup-blocked');await page.locator('#account-signin').click();
      await page.locator('.account-card [role="alert"]').waitFor();
      assert((await page.locator('.account-card [role="alert"]').textContent()).includes(language==='en'?'Allow pop-ups':'પોપ-અપને મંજૂરી'));
      assert(!(await page.locator('main').textContent()).includes('NEVER-RENDER'));
      await page.evaluate(()=>window.__accountFixture.error=null);await page.locator('#account-signin').click();
      await page.locator('#account-signout').waitFor();
      await page.waitForFunction(()=>document.activeElement?.id==='account-signout');
      assert.equal(await page.locator('.account-identity h2').textContent(),'Test Student');
      assert.deepEqual(await page.evaluate(()=>window.__accountFixture.signIns.map(c=>[c.language,c.gesture])),[[language,true],[language,true]],'adapter invoked within the browser user gesture');
      assert(!(await page.locator('main').textContent()).includes('PRIVATE-UID'));assert.equal(await page.locator('main img').count(),0);
      await layout(page,label+' signed in');
      if(width===1365||width===390)await page.screenshot({path:path.join(out,label.replace(' ','-')+'-signed-in.png'),fullPage:true});
      await page.locator('.account-actions a[href="#/purchases"]').click();
      await page.waitForFunction(()=>location.hash==='#/purchases'&&!!document.querySelector('#account-signout'));
      await page.locator('[data-purchases-panel]').waitFor();
      assert((await page.locator('main').textContent()).includes(language==='en'?'Only server-confirmed purchases appear here':'માત્ર સર્વરે પુષ્ટિ કરેલી ખરીદી અહીં દેખાય છે'));
      assert.equal(await page.locator('[data-checkout],form,input,iframe').count(),0);await layout(page,label+' purchases');
      await page.evaluate(()=>window.__accountFixture.error='auth/network-request-failed');await page.locator('#account-signout').click();
      await page.locator('.account-card [role="alert"]').waitFor();assert.equal(await page.locator('.account-details dd').first().textContent(),'student@example.test');
      await page.evaluate(()=>window.__accountFixture.error=null);await page.locator('#account-signout').click();
      await page.locator('#account-signin').waitFor();await page.waitForFunction(()=>document.activeElement?.id==='account-signin');
      assert(!(await page.locator('main').textContent()).includes('student@example.test'));
      assert.equal(await page.evaluate(()=>localStorage.getItem('diplomaone.website.saved')),'[{"code":"DI03000161","unit":1}]');
      assert.equal(requests.filter(url=>url.includes('/assets/firebase-auth.js')).length,1,'SDK loaded once');
      assert(requests.every(url=>new URL(url).origin===origin),'mock scenarios must not reach any external service');
      if(width<=1000){
        await page.locator('#menu-toggle').click();await page.locator('#mobile-nav').waitFor({state:'visible'});
        await page.locator('#mobile-nav [href="#/account"]').click();
        assert.equal(await page.locator('#mobile-nav').isVisible(),false);
      }
      assert.deepEqual(errors,[]);await context.close();checks+=3;
      console.log(label+': signed-out/signed-in/purchases, errors, focus, gestures, CSP and layout passed');
    }
    // Use the actual, unmodified self-hosted SDK, not the double. Network is
    // deliberately aborted, so this proves loading/readiness and failure UI,
    // not OAuth completion. A mobile UA also exercises proactive GAPI loading.
    for(const mobile of [false,true]){
      const external=[],errors=[],context=await browser.newContext({viewport:{width:mobile?390:1280,height:900},
        ...(mobile?{isMobile:true,userAgent:'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1'}:{})});
      await context.route('**/*',r=>{if(new URL(r.request().url()).origin===origin)return r.continue();external.push(r.request().url());return r.abort();});
      const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
      await page.addInitScript(()=>{window.__accountCsp=[];document.addEventListener('securitypolicyviolation',e=>window.__accountCsp.push(e.violatedDirective+':'+e.blockedURI));});
      await page.goto(base+'/#/account');await page.waitForFunction(()=>document.querySelector('#account-signin')?.disabled===false);
      assert.equal(await page.evaluate(()=>window.DiplomaOneAuth.snapshot().status),'signed-out');
      await page.locator('#account-signin').click();await page.locator('.account-card [role="alert"]').waitFor();
      const alert=await page.locator('.account-card [role="alert"]').textContent();
      // Firebase reports an aborted GAPI <script> load as internal-error.
      assert(alert.includes('auth/internal-error')&&alert.includes('content blocker'),alert+'; external requests: '+external.map(url=>new URL(url).origin).join(', '));
      assert(external.some(url=>url.startsWith('https://apis.google.com/')),'real SDK requests GAPI at its allowed host');
      assert(external.every(url=>url.startsWith('https://apis.google.com/')),'no unexpected external service during offline smoke test');
      assert.deepEqual(errors,[]);assert.deepEqual(await page.evaluate(()=>window.__accountCsp),[]);
      await context.close();console.log('Actual SDK '+(mobile?'mobile UA':'desktop')+': local ESM, readiness and network-failure UI passed');++checks;
    }
    // Check relative SDK URLs on a GitHub Pages-style project subpath too.
    const context=await browser.newContext();
    await context.route(origin+'/diplomaone-content/**',r=>{
      const rel=new URL(r.request().url()).pathname.slice('/diplomaone-content/'.length)||'index.html';
      const file=path.resolve(root,'website',rel);assert(file.startsWith(path.join(root,'website')+path.sep));
      const mime=rel.endsWith('.html')?'text/html':rel.endsWith('.js')?'text/javascript':rel.endsWith('.css')?'text/css':rel.endsWith('.ttf')?'font/ttf':rel.endsWith('.svg')?'image/svg+xml':'application/octet-stream';
      return r.fulfill({contentType:mime,body:fs.readFileSync(file)});
    });
    const page=await context.newPage(),requests=[];page.on('request',r=>requests.push(r.url()));
    await page.goto(origin+'/diplomaone-content/#/account');await page.waitForFunction(()=>document.querySelector('#account-signin')?.disabled===false);
    assert(requests.some(url=>url===origin+'/diplomaone-content/assets/firebase-auth.js'));
    await context.close();++checks;console.log('Project-subpath SDK resolution passed');
    console.log(checks+' offline account browser checks passed. Live Google OAuth remains unverified.');
  }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
