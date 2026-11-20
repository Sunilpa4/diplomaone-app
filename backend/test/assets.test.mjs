import {test} from 'node:test';
import assert from 'node:assert/strict';
import {privateAssets,privateKey} from '../src/assets.mjs';
import {MAX_ASSET_BYTES} from '../src/domain.mjs';
const product={id:'DI03000161--summer-2026',reader_asset:'a'.repeat(64),
  assets:[{id:'a'.repeat(64),mime:'text/plain; charset=utf-8',bytes:100,path:'reader.html'},
    {id:'b'.repeat(64),mime:'image/png',bytes:200,path:'reader.assets/diagram.png'}]};

test('actual private storage adapter checks every asset via strong metadata before checkout',async()=>{
  const calls=[],store={async getMetadata(key,options){calls.push([key,options]);const asset=product.assets.find(a=>key.endsWith(a.id));return {metadata:{sha256:asset.id,bytes:asset.bytes}};}};
  assert.equal(await privateAssets(()=>store).ready(product),true);
  assert.equal(calls.length,2);assert.deepEqual(calls[0],[privateKey(product.id,product.reader_asset),{consistency:'strong'}]);
});

test('missing, changed or incomplete blob metadata fails readiness',async()=>{
  for(const metadata of [null,{metadata:{}},{metadata:{sha256:'c'.repeat(64),bytes:100}},
    {metadata:{sha256:'a'.repeat(64),bytes:99}}]){
    assert.equal(await privateAssets(()=>({async getMetadata(){return metadata;}})).ready(product),false);
  }
});

test('missing reader, active mime, malformed hash, empty or oversized manifests fail readiness without any blob read',async()=>{
  let reads=0;const adapter=privateAssets(()=>({async getMetadata(){++reads;throw Error('must not read');}}));
  for(const p of [{...product,assets:[]},{...product,reader_asset:'c'.repeat(64)},
    {...product,assets:[{...product.assets[0],bytes:MAX_ASSET_BYTES+1}]},
    {...product,assets:[{...product.assets[0],mime:'text/html'}]},
    {...product,assets:[{...product.assets[0],id:'a'.repeat(64)+'\n'}]}])assert.equal(await adapter.ready(p),false);
  assert.equal(reads,0);
});

test('private get uses only validated content-addressed keys and binary response type',async()=>{
  const calls=[],adapter=privateAssets(()=>({async get(...args){calls.push(args);return new Uint8Array([1,2]).buffer;}}));
  assert.equal((await adapter.get(product.id,product.reader_asset)).byteLength,2);
  assert.deepEqual(calls,[[privateKey(product.id,product.reader_asset),{type:'arrayBuffer'}]]);
  assert.throws(()=>adapter.get(product.id,'../other-secret'));
});
