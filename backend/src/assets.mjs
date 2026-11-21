import {Problem,productPattern,assetPattern,MAX_ASSET_BYTES,MIME} from './domain.mjs';
export const PRIVATE_STORE='diplomaone-private-test';
export function privateKey(productId,assetId){
  if(!productPattern.test(productId)||!assetPattern.test(assetId)||assetId.length!==64)throw new Problem(400,'invalid_private_key');
  return productId+'/'+assetId;
}
export function privateAssets(store){
  return {
    get:(id,asset)=>store().get(privateKey(id,asset),{type:'arrayBuffer'}),
    async ready(product){
      if(!Array.isArray(product.assets)||!product.assets.length||product.assets.length>300||
        !product.assets.some(a=>a.id===product.reader_asset&&a.mime==='text/plain; charset=utf-8'))return false;
      for(const asset of product.assets){
        if(!assetPattern.test(asset.id)||asset.id.length!==64||!Number.isInteger(asset.bytes)||asset.bytes<1||
          asset.bytes>MAX_ASSET_BYTES||!Object.values(MIME).includes(asset.mime))return false;
        const result=await store().getMetadata(privateKey(product.id,asset.id),{consistency:'strong'});
        if(result?.metadata?.sha256!==asset.id||result.metadata.bytes!==asset.bytes)return false;
      }
      return true;
    },
  };
}
