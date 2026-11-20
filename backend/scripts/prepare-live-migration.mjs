// OWNER-OPERATED, offline only. This NEVER imports or deletes cloud content.
import {fileURLToPath} from 'node:url';
import {mkdir,lstat} from 'node:fs/promises';
import path from 'node:path';
import {prepareMigration,writeMigration} from '../src/migration.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..'),args=process.argv.slice(2);
const source=args.find(a=>!a.startsWith('--'))||'papers-upload/papers';
const output=args.find(a=>a.startsWith('--out='))?.slice(6)||'build/private-live-import';
const mapping=args.find(a=>a.startsWith('--mapping='))?.slice(10)||'backend/paper-products.json';
if(args.filter(a=>!a.startsWith('--')).length>1||args.some(a=>a.startsWith('--')&&a!=='--write'&&a!=='--without-pdfs'&&!a.startsWith('--out=')&&!a.startsWith('--mapping='))){
 console.error('Usage: npm run prepare:live-papers -- [PRIVATE_SOURCE] [--mapping=FILE] [--without-pdfs] [--write --out=build/PRIVATE_NAME]');process.exitCode=1;
}else try{
 const plan=await prepareMigration(source,mapping,{withoutPdfs:args.includes('--without-pdfs')});
 const summary={mode:'live',offline:true,imported:false,papers:plan.products.length,
  assets:plan.products.reduce((n,p)=>n+p.sourceFiles.length,0),bytes:plan.products.reduce((n,p)=>n+p.sourceFiles.reduce((sum,f)=>sum+f.bytes,0),0)};
 if(args.includes('--write')){
  const destination=path.resolve(output),build=path.join(root,'build');
  if(!destination.startsWith(build+path.sep))throw Error('Private output must be inside ignored build/');
  // Lexical containment alone would allow build/link-to-public/EXPORT.
  // Create/check one parent at a time; never traverse a symbolic link.
  let parent=build;
  for(const part of ['',...path.relative(build,path.dirname(destination)).split(path.sep).filter(Boolean)]){
   if(part)parent=path.join(parent,part);
   try{await mkdir(parent,{mode:0o700});}catch(error){if(error.code!=='EEXIST')throw error;}
   if(!(await lstat(parent)).isDirectory())throw Error('Private output parent must be a real directory');
  }
  await writeMigration(plan,destination);summary.exported=true;
 }else summary.dryRun=true;
 console.log(JSON.stringify(summary));
}catch(error){
 // Only local, allowlisted validation codes, never raw manifest/answer bytes.
 const code=typeof error?.code==='string'&&/^[a-z_]+$/.test(error.code)?error.code:'migration_preparation_failed';
 console.error(code+'. No cloud import, public deletion or payment was performed.');process.exitCode=1;
}
