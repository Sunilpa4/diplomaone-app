// Offline launch audit. It reports current files; it cannot erase Git history,
// CDN caches, forks, releases or copies previously downloaded by a visitor.
import {readdir,lstat,readFile,realpath} from 'node:fs/promises';
import path from 'node:path';
import {FREE_CODES,digest,validateProduct,reject} from './domain.mjs';
const code=/^(?:DI[0-9]{8}|[0-9]{7})$/;
async function files(directory){
 let entries;try{
  if((await lstat(directory)).isSymbolicLink())return [directory];
  entries=await readdir(directory,{withFileTypes:true});
 }catch(error){if(error.code==='ENOENT')return [];throw error;}
 const result=[];
 for(const entry of entries){const file=path.join(directory,entry.name);
  if(entry.isDirectory())result.push(...await files(file));else result.push(file);
 }return result;
}
export async function auditPublicPapers(checkout){
 const root=await realpath(checkout),findings=[];
 reject(!(await lstat(root)).isDirectory(),400,'invalid_audit_root');
 for(const surface of ['papers','papers-upload/papers','papers-upload/originals']){
  for(const file of await files(path.join(root,surface))){
   const relative=path.relative(path.join(root,surface),file).split(path.sep),subject=relative[0];
   const info=await lstat(file);
   if(FREE_CODES.includes(subject)&&!info.isSymbolicLink())continue;
   let metadata=false;
   if(surface==='papers'&&code.test(subject)&&relative.length===2&&/^[a-z][a-z0-9]*-[0-9]{4}\.json$/.test(relative[1])&&info.isFile()){
    try{const raw=await readFile(file,'utf8'),item=raw.length<=2048?JSON.parse(raw):null;
     metadata=item?.version===1&&item.private===true&&item.id===subject+'--'+relative[1].slice(0,-5)&&
      Object.keys(item).every(k=>['version','private','id','title','branch','amount','currency'].includes(k));
     if(metadata&&Object.keys(item).length!==3){
      const canonical=validateProduct(item);
      metadata=Object.keys(item).length===7&&item.amount===canonical.amount&&item.currency==='INR';
     }
    }catch(_){metadata=false;}
   }
   if(metadata)continue;
   // Unknown files are NOT presumed free. Symlinks are reported, not followed.
   findings.push({path:path.relative(root,file).split(path.sep).join('/'),
    reason:info.isSymbolicLink()?'symlink':code.test(subject)?'public_paid_source':'unreviewed_paper_file',
    bytes:info.isFile()?info.size:null,sha256:info.isFile()?digest(await readFile(file)):null});
  }
 }
 return {version:1,ready:findings.length===0,historyErased:false,findings:findings.sort((a,b)=>a.path.localeCompare(b.path))};
}
