import {writeFile} from 'node:fs/promises';
import {auditPublicPapers} from '../src/public-audit.mjs';
const args=process.argv.slice(2),paths=args.filter(a=>!a.startsWith('--'));
const report=args.find(a=>a.startsWith('--report='))?.slice(9);
if(!paths.length||args.some(a=>a.startsWith('--')&&!a.startsWith('--report='))){
 console.error('Usage: npm run audit:public-papers -- APP_CHECKOUT [PUBLIC_CONTENT_CHECKOUT] [--report=PRIVATE_FILE]');process.exitCode=1;
}else try{
 const reports=[];for(const path of paths)reports.push(await auditPublicPapers(path));
 if(report)await writeFile(report,JSON.stringify({version:1,reports},null,2)+'\n',{flag:'wx',mode:0o600});
 const unsafe=reports.reduce((n,r)=>n+r.findings.length,0);
 console.log(JSON.stringify({ready:unsafe===0,publicFilesRequiringMigration:unsafe,historyErased:false,cloudChanges:false}));
 if(unsafe)process.exitCode=2;
}catch(_){console.error('Public-source audit could not complete. No files were deleted or cloud settings changed.');process.exitCode=1;}
