// Check dynamic listing and existing unit links in website and Netlify package.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = process.argv[2] || require('node:path').join(__dirname, 'app.js');
let source = fs.readFileSync(path, 'utf8');
const hook = '  updateHeader();render();\n})();';
assert.equal(source.split(hook).length, 2, 'test hook must be unique');
source = source.replace(hook, `  globalThis.testAPI = { showSubject, showPapers, setIndex(value) { paperIndex = value; }, setLanguage(value) { lang = value; } };\n})();`);
const element = { addEventListener() {}, setAttribute() {}, querySelectorAll() { return []; } };
const context = { document: { querySelector() { return element; } }, window: { addEventListener() {} }, localStorage: { getItem() { return null; } }, console, setTimeout, clearTimeout };
vm.runInNewContext(source, context);
const { showSubject, showPapers, setIndex, setLanguage } = context.testAPI;
const index = {};
for (const code of ['DI03000141','DI03000151','DI03000161','DI03000171','DI03000201','DI03019011']) index[code]=[{session:'summer-2026',pdf:'Question_Paper.pdf'}];
index.DI05019011=[{session:'winter-2027',pdf:null},{session:'summer-2026',pdf:null}];
index.DI09999999=[{session:'winter-2027',pdf:null}]; // No catalog subject yet.
setIndex(index);
for (const [code,entries] of Object.entries(index)) {
  for (const language of ['en', 'gu']) {
    setLanguage(language);
    const html = showSubject({code, name:{en:'Test subject', gu:'ટેસ્ટ વિષય'}, available_units:[1], units:[{no:1,title:{en:'Test unit'},hours:1,weightage:1}]}, {});
    for(const {session} of entries) assert(html.includes(`href="#/paper/${code}/${session}"`), `${code}: missing ${session} link (${language})`);
    assert(html.includes(`href="#/unit/${code}/1"`), `${code}: existing notes link lost`);
    assert(html.includes(language === 'en' ? 'Solved papers' : 'ઉકેલેલા પેપર'));
  }
}
// Same-titled older-scheme papers appear on the correct Semester 5 subject,
// without changing their original codes or hiding newer DI-code papers.
index['4351902']=[{session:'summer-2026',pdf:'summer-2026.pdf'}];
index['4351903']=[{session:'summer-2026',pdf:'summer-2026.pdf'}];
for(const language of ['en','gu']) {
  setLanguage(language);
  for(const [subject,legacy,other] of [['DI05019011','4351902','4351903'],['DI05019021','4351903','4351902']]) {
    const html=showSubject({code:subject,name:{en:'Test subject',gu:'ટેસ્ટ વિષય'},available_units:[1],units:[{no:1,title:{en:'Test unit'}}]},{});
    assert(html.includes(`href="#/paper/${legacy}/summer-2026"`));
    assert(html.includes(legacy), 'original exam code must remain visible');
    assert(!html.includes(`href="#/paper/${other}/summer-2026"`), 'do not cross-list the wrong subject');
    assert(html.includes(language==='en'?'Older scheme':'જૂની યોજના'));
    assert(html.includes(`href="#/unit/${subject}/1"`));
    if(subject==='DI05019011') assert(html.includes('#/paper/DI05019011/winter-2027'), 'newer paper links must remain');
  }
}
setLanguage('en');
assert(showPapers().includes('#/paper/DI09999999/winter-2027'), 'unregistered subjects remain discoverable');
assert(!showSubject({code:'DI05007011', name:{en:'Other subject'}, units:[]}, {}).includes('#/paper/DI05007011/'), 'do not advertise unlisted papers');
console.log('Dynamic subject and all-paper listings preserve note links in both languages.');
