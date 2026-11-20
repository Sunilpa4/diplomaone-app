import {randomUUID} from 'node:crypto';
import {reject,validateProduct} from './domain.mjs';

async function recordEvent(query,event){
  if(!event)return;
  const {rows}=await query(`INSERT INTO diplomaone_test.events(id,body_hash) VALUES($1,$2)
    ON CONFLICT(id) DO UPDATE SET id=excluded.id WHERE diplomaone_test.events.body_hash=excluded.body_hash RETURNING id`,[event.id,event.hash]);
  reject(rows.length!==1,409,'event_id_conflict');
}

// query(text, values) -> {rows}; transaction(fn) supplies a connection-scoped query.
// There is deliberately no in-memory production fallback.
export class Repository {
  constructor(database){this.db=database;}
  async products(){
    const {rows}=await this.db.query('SELECT id,title,branch FROM diplomaone_test.products WHERE active=true ORDER BY id');
    return rows.map(validateProduct);
  }
  async product(id){
    const {rows}=await this.db.query('SELECT * FROM diplomaone_test.products WHERE id=$1 AND active=true',[id]);
    return rows[0]?validateProduct(rows[0]):null;
  }
  async importProduct(product){
    const p=validateProduct(product);
    const {rows}=await this.db.query(`INSERT INTO diplomaone_test.products(id,title,branch,assets,reader_asset,active)
      VALUES ($1,$2,$3,$4::jsonb,$5,true) ON CONFLICT(id) DO NOTHING RETURNING id`,
      [p.id,p.title,p.branch,JSON.stringify(p.assets),p.reader_asset]);
    reject(rows.length!==1,409,'product_already_imported_review_required');
  }
  async reserve(uid,product,requestId){
    return this.db.transaction(async query=>{
      // Global pilot budget and per-user/paper reservation are serialized across
      // instances, not just within one function's memory. 50 new orders/day.
      await query("SELECT pg_advisory_xact_lock(hashtextextended('diplomaone-test-checkout',0))");
      let {rows}=await query('SELECT * FROM diplomaone_test.orders WHERE uid=$1 AND request_id=$2',[uid,requestId]);
      if(rows[0]){reject(rows[0].product_id!==product.id,409,'idempotency_conflict');return {created:false,order:rows[0]};}
      ({rows}=await query('SELECT active FROM diplomaone_test.entitlements WHERE uid=$1 AND product_id=$2',[uid,product.id]));
      reject(rows[0]?.active,409,'already_owned');
      ({rows}=await query("SELECT * FROM diplomaone_test.orders WHERE uid=$1 AND product_id=$2 AND status IN ('reserving','created','unknown')",[uid,product.id]));
      if(rows[0])return {created:false,order:rows[0]};
      ({rows}=await query(`SELECT count(*)::int AS total,
        count(*) FILTER (WHERE uid=$1 AND created_at>now()-interval '1 hour')::int AS user_total
        FROM diplomaone_test.orders WHERE created_at>now()-interval '24 hours'`,[uid]));
      reject(rows[0].total>=50||rows[0].user_total>=5,429,'test_order_limit');
      const id=randomUUID(),receipt='dt_'+id.replaceAll('-','');
      ({rows}=await query(`INSERT INTO diplomaone_test.orders(id,uid,product_id,request_id,receipt,amount,status)
        VALUES($1,$2,$3,$4,$5,$6,'reserving') RETURNING *`,[id,uid,product.id,requestId,receipt,product.amount]));
      return {created:true,order:rows[0]};
    });
  }
  async attachOrder(id,providerId){
    const {rows}=await this.db.query(`UPDATE diplomaone_test.orders SET status='created',razorpay_order_id=$2
      WHERE id=$1 AND status='reserving' RETURNING *`,[id,providerId]);
    reject(rows.length!==1,409,'order_state_conflict');return rows[0];
  }
  async unavailable(id){await this.db.query("UPDATE diplomaone_test.orders SET status='failed' WHERE id=$1 AND status='reserving'",[id]);}
  async uncertain(id){await this.db.query("UPDATE diplomaone_test.orders SET status='unknown' WHERE id=$1 AND status='reserving'",[id]);}
  async order(id){return (await this.db.query('SELECT * FROM diplomaone_test.orders WHERE razorpay_order_id=$1',[id])).rows[0]||null;}
  async payment(id){return (await this.db.query('SELECT * FROM diplomaone_test.orders WHERE payment_id=$1',[id])).rows[0]||null;}
  async event(id,hash){
    if(!id)return false;
    const row=(await this.db.query('SELECT body_hash FROM diplomaone_test.events WHERE id=$1',[id])).rows[0];
    reject(row&&row.body_hash!==hash,409,'event_id_conflict');return !!row;
  }
  async grant(orderId,paymentId,event=null){
    return this.db.transaction(async query=>{
      const stored=(await query('SELECT * FROM diplomaone_test.orders WHERE razorpay_order_id=$1 FOR UPDATE',[orderId])).rows[0];
      reject(!stored,404,'order_not_found');
      reject(stored.status==='revoked',409,'payment_revoked');
      reject(stored.payment_id&&stored.payment_id!==paymentId,409,'payment_conflict');
      reject(!['created','paid'].includes(stored.status),409,'order_state_conflict');
      await query("UPDATE diplomaone_test.orders SET status='paid',payment_id=$2,paid_at=coalesce(paid_at,now()) WHERE id=$1",[stored.id,paymentId]);
      await query(`INSERT INTO diplomaone_test.entitlements(uid,product_id,order_id) VALUES($1,$2,$3)
        ON CONFLICT(uid,product_id) DO UPDATE SET active=true,order_id=excluded.order_id,created_at=now()
        WHERE diplomaone_test.entitlements.active=false`,[stored.uid,stored.product_id,stored.id]);
      await recordEvent(query,event);
      return {productId:stored.product_id,owned:true,mode:'test'};
    });
  }
  async revoke(orderId,paymentId,event){
    return this.db.transaction(async query=>{
      // Resolve by canonical order, including a refund that arrives BEFORE the
      // captured webhook/callback has saved payment_id. Never re-grant it later.
      const order=(await query('SELECT * FROM diplomaone_test.orders WHERE razorpay_order_id=$1 FOR UPDATE',[orderId])).rows[0];
      if(!order)return;
      reject(order.payment_id&&order.payment_id!==paymentId,409,'payment_conflict');
      await query("UPDATE diplomaone_test.orders SET status='revoked',payment_id=$2 WHERE id=$1",[order.id,paymentId]);
      await query('UPDATE diplomaone_test.entitlements SET active=false WHERE order_id=$1',[order.id]);
      await recordEvent(query,event);
    });
  }
  async purchases(uid){
    return (await this.db.query(`SELECT e.product_id AS "productId",p.title,p.branch,e.active,o.amount,o.currency,e.created_at AS "purchasedAt"
      FROM diplomaone_test.entitlements e JOIN diplomaone_test.products p ON p.id=e.product_id
      JOIN diplomaone_test.orders o ON o.id=e.order_id WHERE e.uid=$1 ORDER BY e.created_at DESC LIMIT 100`,[uid])).rows;
  }
  async owns(uid,id){return (await this.db.query('SELECT active FROM diplomaone_test.entitlements WHERE uid=$1 AND product_id=$2',[uid,id])).rows[0]?.active===true;}
}

export function pgDatabase(pool){
  return {query:(...args)=>pool.query(...args),async transaction(fn){
    const client=await pool.connect();
    try{await client.query('BEGIN');const result=await fn((...args)=>client.query(...args));await client.query('COMMIT');return result;}
    catch(error){await client.query('ROLLBACK');throw error;}
    finally{client.release();}
  }};
}
