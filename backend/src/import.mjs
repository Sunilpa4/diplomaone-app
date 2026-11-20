import {readFile,realpath,stat} from 'node:fs/promises';
import path from 'node:path';
import {parse} from 'parse5';
import {MAX_ASSET_BYTES,MIME,digest,reject,validateProduct} from './domain.mjs';

function checkReader(reader,files){
  const tree=parse(reader.content.toString('utf8')),nodes=[];
  const walk=node=>{nodes.push(node);for(const child of node.childNodes||[])walk(child);if(node.content)walk(node.content);};walk(tree);
  reject(!nodes.some(n=>n.tagName==='main')||!nodes.some(n=>n.tagName==='details')||
    nodes.some(n=>['iframe','object','embed'].includes(n.tagName)),400,'question_card_reader_required');
  const paths=new Set(files.map(file=>file.path));
  for(const node of nodes){
    const attributes=Object.fromEntries((node.attrs||[]).map(a=>[a.name,a.value]));
    if(node.tagName!=='img'&&node.tagName!=='image')continue;
    const src=attributes.src||attributes.href||attributes['xlink:href']||'';
    reject(!!attributes.srcset||!src,400,'unsupported_image_reference');
    if(/^data:image\/(?:png|jpeg|webp);base64,[a-z0-9+/=\s]+$/i.test(src))continue;
    reject(/^[a-z][a-z0-9+.-]*:|^\/|[?#\\]/i.test(src),400,'image_must_be_private');
    let decoded;try{decoded=decodeURIComponent(src);}catch(_){reject(true,400,'invalid_image_reference');}
    reject(/^[a-z][a-z0-9+.-]*:|^\/|[?#\\]/i.test(decoded),400,'image_must_be_private');
    const target=path.posix.normalize(path.posix.join(path.posix.dirname(reader.path),decoded));
    reject(!paths.has(target),400,'missing_private_image');
  }
}

export async function prepareImport(manifestPath){
  const filename=await realpath(manifestPath),base=path.dirname(filename);
  const manifest=JSON.parse(await readFile(filename,'utf8'));
  return prepareImportData(manifest,base);
}

// Shared by the offline migration planner; no source manifest needs to be
// temporarily written into a public checkout just to validate existing files.
export async function prepareImportData(manifest,base){
  base=await realpath(base);
  const product=validateProduct(manifest);
  reject(manifest.version!==1||!Array.isArray(manifest.files)||manifest.files.length<1||manifest.files.length>300,400,'invalid_manifest');
  const seen=new Set(),files=[];
  for(const relative of manifest.files){
    reject(typeof relative!=='string'||!relative||relative.length>220||/[\\\x00-\x1f?#%]/.test(relative)||
      relative.split('/').some(part=>!part||part==='.'||part==='..')||path.isAbsolute(relative)||seen.has(relative),400,'invalid_asset_path');
    seen.add(relative);
    const resolved=await realpath(path.join(base,relative));
    reject(!resolved.startsWith(base+path.sep),400,'asset_outside_import');
    const info=await stat(resolved),mime=MIME[path.extname(relative).toLowerCase()];
    reject(!info.isFile()||!mime||info.size<1||info.size>MAX_ASSET_BYTES,400,'unsupported_asset');
    const bytes=await readFile(resolved);
    files.push({id:digest(bytes),path:relative,mime,bytes:bytes.length,content:bytes});
  }
  const reader=files.find(f=>f.path===manifest.reader&&f.path.endsWith('.html'));
  reject(!reader,400,'reader_required');
  checkReader(reader,files);
  return {product:{id:product.id,title:product.title,branch:product.branch,
    reader_asset:reader.id,assets:files.map(({content,...metadata})=>metadata)},files};
}

export async function applyImport(prepared,{store,repository}){
  // Upload and strong-read verification MUST finish before the product becomes
  // active in Firestore. Failures leave no purchasable partial paper.
  for(const file of prepared.files){
    const key=prepared.product.id+'/'+file.id;
    await store.set(key,file.content,{metadata:{sha256:file.id,bytes:file.bytes,mime:file.mime}});
    const saved=await store.get(key,{type:'arrayBuffer',consistency:'strong'});
    reject(!saved||digest(Buffer.from(saved))!==file.id,503,'private_upload_not_verified');
  }
  await repository.importProduct(prepared.product);
}
