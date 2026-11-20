// TEST DOUBLE ONLY. No application module imports this file. Models document
// paths/snapshots, bounded queries, read-before-write, atomic commits, version
// conflicts and callback retries. It is not a Firestore emulator certification.
import assert from 'node:assert/strict';
const copy=value=>value===undefined?undefined:structuredClone(value);
class Snapshot {
  constructor(ref,record){this.ref=ref;this.id=ref.id;this.exists=!!record;this.value=copy(record?.data);}
  data(){return copy(this.value);}
}
class Document {
  constructor(db,path){this.db=db;this.path=path;this.id=path.split('/').at(-1);}
  collection(name){return new Query(this.db,this.path+'/'+name);}
  async get(){return new Snapshot(this,this.db.rows.get(this.path));}
  async set(value){this.db.put(this,value);}
  async update(value){assert(this.db.rows.has(this.path));this.db.put(this,{...this.db.rows.get(this.path).data,...value});}
  async delete(){this.db.rows.delete(this.path);this.db.versions.set(this.path,++this.db.version);}
}
class Query {
  constructor(db,path,{filters=[],order=null,take=Infinity}={}){this.db=db;this.path=path;this.filters=filters;this.order=order;this.take=take;}
  doc(id){assert(typeof id==='string'&&id&&!id.includes('/'));return new Document(this.db,this.path+'/'+id);}
  where(field,operator,value){assert.equal(operator,'==');return new Query(this.db,this.path,{filters:[...this.filters,[field,value]],order:this.order,take:this.take});}
  orderBy(field,direction){return new Query(this.db,this.path,{filters:this.filters,order:[field,direction],take:this.take});}
  limit(take){return new Query(this.db,this.path,{filters:this.filters,order:this.order,take});}
  async get(){
    let rows=[...this.db.rows].filter(([p])=>p.startsWith(this.path+'/')&&p.split('/').length===this.path.split('/').length+1)
      .filter(([,r])=>this.filters.every(([f,v])=>r.data[f]===v));
    if(this.order){const [field,dir]=this.order;rows.sort((a,b)=>(a[1].data[field]-b[1].data[field])*(dir==='desc'?-1:1));}
    else rows.sort((a,b)=>a[0].localeCompare(b[0]));
    return {docs:rows.slice(0,this.take).map(([p,r])=>new Snapshot(new Document(this.db,p),r))};
  }
}
class Transaction {
  constructor(db){this.db=db;this.reads=new Map();this.writes=[];}
  async get(ref){
    assert.equal(this.writes.length,0,'Firestore requires all reads before any write');
    this.reads.set(ref.path,this.db.versions.get(ref.path)||0);return ref.get();
  }
  create(ref,data){this.writes.push({type:'create',ref,data:copy(data)});return this;}
  set(ref,data){this.writes.push({type:'set',ref,data:copy(data)});return this;}
  update(ref,data){this.writes.push({type:'update',ref,data:copy(data)});return this;}
  delete(ref){this.writes.push({type:'delete',ref});return this;}
  commit(){
    for(const [p,v] of this.reads)if((this.db.versions.get(p)||0)!==v)return false;
    for(const w of this.writes){
      if(w.type==='create')assert(!this.db.rows.has(w.ref.path),'ALREADY_EXISTS');
      if(w.type==='update')assert(this.db.rows.has(w.ref.path),'NOT_FOUND');
    }
    for(const w of this.writes){
      if(w.type==='delete'){this.db.rows.delete(w.ref.path);this.db.versions.set(w.ref.path,++this.db.version);}
      else this.db.put(w.ref,w.type==='update'?{...this.db.rows.get(w.ref.path).data,...w.data}:w.data);
    }
    return true;
  }
}
export class MemoryFirestore {
  constructor(){this.rows=new Map();this.versions=new Map();this.version=0;this.retries=0;}
  doc(path){assert.equal(path.split('/').length%2,0);return new Document(this,path);}
  put(ref,value){this.rows.set(ref.path,{data:copy(value)});this.versions.set(ref.path,++this.version);}
  async runTransaction(fn,{maxAttempts=5}={}){
    for(let attempt=0;attempt<maxAttempts;attempt++){
      const tx=new Transaction(this),result=await fn(tx);
      if(tx.commit())return result;++this.retries;
    }
    throw new Error('ABORTED: test transaction contention');
  }
  async recursiveDelete(ref){for(const p of this.rows.keys())if(p===ref.path||p.startsWith(ref.path+'/')){
    this.rows.delete(p);this.versions.set(p,++this.version);
  }}
  async terminate(){}
}
