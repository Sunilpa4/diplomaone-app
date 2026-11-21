// Keep the exact pinned Firebase app/auth browser bundle self-hosted.
// npm ci --prefix website && npm run build:auth --prefix website
import { build } from 'esbuild';
import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const result=await build({
  absWorkingDir:root,
  entryPoints:['auth/firebase-client.js'],
  outfile:'assets/firebase-auth.js',
  bundle:true,format:'esm',platform:'browser',target:['es2020'],minify:true,
  legalComments:'external',charset:'utf8',write:false,metafile:true,
});
if(Object.keys(result.metafile.inputs).some(file=>/firebase\/(analytics|firestore|storage)|@firebase\/(analytics|firestore|storage)/.test(file)))
  throw new Error('Only Firebase app/auth may be shipped in this phase');
for(const output of result.outputFiles) {
  if(process.argv.includes('--check')) {
    const existing=await readFile(output.path);
    if(!existing.equals(output.contents))throw new Error('Stale auth bundle: run npm run build:auth --prefix website');
  } else await writeFile(output.path,output.contents);
  console.log(path.relative(root,output.path),output.contents.length,'bytes',process.argv.includes('--check')?'verified':'built');
}
