// Offline preparation only. No credentials, Firestore, provider or cloud SDK.
import {readdir,readFile,realpath,mkdir,writeFile} from 'node:fs/promises';
import path from 'node:path';
import {prepareImport,prepareImportData} from './import.mjs';
import {FREE_CODES,PRICES,productPattern,reject,digest} from './domain.mjs';

export async function prepareMigration(source,mappingFile,{withoutPdfs=false}={}){
 const base=await realpath(source),mapping=JSON.parse(await readFile(mappingFile,'utf8'));
 reject(mapping.version!==1||!mapping.subjects||typeof mapping.subjects!=='object'||Array.isArray(mapping.subjects),400,'invalid_product_mapping');
 const products=[],publicMetadata=[],seen=new Set();
 for(const directory of (await readdir(base,{withFileTypes:true})).sort((a,b)=>a.name.localeCompare(b.name))){
  reject(directory.isSymbolicLink(),400,'migration_symlink');if(!directory.isDirectory())continue;
  const code=directory.name;
  reject(!/^(?:DI[0-9]{8}|[0-9]{7})$/.test(code),400,'invalid_paper_directory');
  if(FREE_CODES.includes(code))continue;
  const info=mapping.subjects[code];
  reject(!info||!Object.hasOwn(PRICES,info.branch)||typeof info.title!=='string'||!info.title.trim(),400,'paper_branch_review_required');
  const files=await readdir(path.join(base,code),{withFileTypes:true});
  reject(files.some(f=>f.isSymbolicLink()),400,'migration_symlink');
  const readers=files.filter(f=>f.isFile()&&f.name.endsWith('.html')).sort((a,b)=>a.name.localeCompare(b.name));
  // Do not convert a PDF-only exam into an invented card reader.
  for(const file of files)if(file.isFile()&&file.name.endsWith('.solution.pdf'))
   reject(!readers.some(r=>r.name===file.name.slice(0,-13)+'.html'),400,'question_card_reader_required');
  for(const reader of readers){
   const session=reader.name.slice(0,-5),id=code+'--'+session;
   reject(!productPattern.test(id)||seen.has(id),400,'invalid_product');seen.add(id);
   const paths=[reader.name],assetName=session+'.assets',assetDirectory=files.find(f=>f.name===assetName);
   if(assetDirectory){
    reject(!assetDirectory.isDirectory(),400,'unsupported_asset');
    for(const asset of (await readdir(path.join(base,code,assetName),{withFileTypes:true})).sort((a,b)=>a.name.localeCompare(b.name))){
     reject(!asset.isFile()||asset.isSymbolicLink(),400,'unsupported_asset');paths.push(assetName+'/'+asset.name);
    }
   }
   if(!withoutPdfs)for(const name of [session+'.pdf',session+'.solution.pdf'])if(files.some(f=>f.isFile()&&f.name===name))paths.push(name);
   const sourceReader=await readFile(path.join(base,code,reader.name),'utf8');
   if(!withoutPdfs&&files.some(f=>f.name==='Question_Paper.pdf')&&/href=["'](?:\.\/)?Question_Paper\.pdf["']/i.test(sourceReader))paths.push('Question_Paper.pdf');
   const title=info.title+' · '+session.replace('-', ' ');
   const manifest={version:1,id,title,branch:info.branch,reader:reader.name,files:paths};
   const prepared=await prepareImportData(manifest,path.join(base,code));
   const sourceFiles=prepared.files.map(({path,content,bytes})=>({path,content,sha256:digest(content),bytes}));
   products.push({manifest,sourceFiles});
   publicMetadata.push({id,branch:info.branch,title,amount:PRICES[info.branch],currency:'INR'});
  }
 }
 reject(!products.length,400,'no_private_papers');
 return {version:1,mode:'live',withoutPdfs,products,publicMetadata};
}
export async function writeMigration(plan,destination){
 // Refuse overwrites, including an existing non-empty output; exported private
 // data belongs only in an owner-private/ignored directory, never source Git.
 await mkdir(destination,{recursive:false,mode:0o700});
 for(const {manifest,sourceFiles} of plan.products){
  const directory=path.join(destination,manifest.id);await mkdir(directory,{mode:0o700});
  for(const file of sourceFiles){
   const target=path.join(directory,file.path);await mkdir(path.dirname(target),{recursive:true,mode:0o700});
   await writeFile(target,file.content,{flag:'wx',mode:0o600});
  }
  const filename=path.join(directory,'paper.json');await writeFile(filename,JSON.stringify(manifest,null,2)+'\n',{flag:'wx',mode:0o600});
  // Uses the exact same reader/image/bounds validation as the live importer.
  await prepareImport(filename);
 }
 const journal={version:1,mode:'live',privateImportApplied:false,withoutPdfs:plan.withoutPdfs,
  products:plan.products.map(({manifest,sourceFiles})=>({id:manifest.id,manifest:manifest.id+'/paper.json',
   files:sourceFiles.map(({content,...metadata})=>metadata)}))};
 await writeFile(path.join(destination,'migration.json'),JSON.stringify(journal,null,2)+'\n',{flag:'wx',mode:0o600});
 // Only this separate directory is suitable for a PUBLIC content checkout.
 for(const product of plan.publicMetadata){
  const [code,session]=product.id.split('--'),directory=path.join(destination,'public-metadata/papers',code);
  await mkdir(directory,{recursive:true,mode:0o700});
  await writeFile(path.join(directory,session+'.json'),JSON.stringify({version:1,private:true,...product})+'\n',{flag:'wx',mode:0o600});
 }
 return journal;
}
