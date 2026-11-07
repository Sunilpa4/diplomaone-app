// Check the actual subject renderer used by both the website and the Netlify ZIP.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = process.argv[2] || require('node:path').join(__dirname, 'app.js');
let source = fs.readFileSync(path, 'utf8');
const hook = '  updateHeader();render();\n})();';
assert.equal(source.split(hook).length, 2, 'test hook must be unique');
source = source.replace(hook, `  globalThis.testAPI = { showSubject, setLanguage(value) { lang = value; } };\n})();`);
const element = { addEventListener() {}, setAttribute() {}, querySelectorAll() { return []; } };
const context = { document: { querySelector() { return element; } }, window: { addEventListener() {} }, localStorage: { getItem() { return null; } }, console, setTimeout, clearTimeout };
vm.runInNewContext(source, context);
const { showSubject, setLanguage } = context.testAPI;
for (const code of ['DI03000141','DI03000151','DI03000161','DI03000171','DI03000201','DI03019011']) {
  for (const language of ['en', 'gu']) {
    setLanguage(language);
    const html = showSubject({code, name:{en:'Test subject', gu:'ટેસ્ટ વિષય'}, available_units:[1], units:[{no:1,title:{en:'Test unit'},hours:1,weightage:1}]}, {});
    assert(html.includes(`href="papers/${code}/summer-2026.html"`), `${code}: missing paper link (${language})`);
    assert(html.includes(`href="#/unit/${code}/1"`), `${code}: existing notes link lost`);
    assert(html.includes(language === 'en' ? 'Solved papers' : 'ઉકેલેલા પ્રશ્નપત્રો'));
  }
}
setLanguage('en');
const noPaper = showSubject({code:'DI05019011', name:{en:'Other subject'}, units:[]}, {});
assert(!noPaper.includes('summer-2026.html'), 'do not advertise a paper that was not uploaded');
console.log('Six paper links and existing unit links render in English and Gujarati.');
