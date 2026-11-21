// Test-only bridge from the retained, previously public migration sources to
// the real private-reader manifest shape. NEVER included in static deployment.
const fs=require('node:fs'),path=require('node:path'),{createHash}=require('node:crypto'),{JSDOM}=require('jsdom');
const root=path.resolve(__dirname,'../papers-upload/papers');
module.exports=function privateContext(html,code,session){
 if(['DI01000021','DI01000121'].includes(code))return {code,session};
 const dom=new JSDOM(html),paths=new Set([...dom.window.document.querySelectorAll('img[src]')].map(img=>img.getAttribute('src')).filter(src=>!src.startsWith('data:')));
 dom.window.close();
 const base=path.join(root,code),assets=[...paths].map(relative=>{
  const filename=path.resolve(base,relative);if(!filename.startsWith(base+path.sep))throw Error('Invalid test image');
  const bytes=fs.readFileSync(filename);return {id:createHash('sha256').update(bytes).digest('hex'),path:relative,
   mime:relative.endsWith('.png')?'image/png':relative.endsWith('.webp')?'image/webp':'image/jpeg',bytes:bytes.length};
 });
 return {code,session,private:true,readerPath:session+'.html',assets};
};
