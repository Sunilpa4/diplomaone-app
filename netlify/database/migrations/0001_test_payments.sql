-- Test-only, additive schema. No public note/content tables are modified.
-- No products or fake purchases are seeded. Do not reuse these tables for live.
CREATE SCHEMA IF NOT EXISTS diplomaone_test;
REVOKE ALL ON SCHEMA diplomaone_test FROM PUBLIC;

CREATE TABLE diplomaone_test.products (
  id text PRIMARY KEY CHECK (id ~ '^(DI[0-9]{8}|[0-9]{7})--[a-z][a-z0-9]*-[0-9]{4}$'),
  title text NOT NULL CHECK (length(title) BETWEEN 1 AND 200),
  branch text NOT NULL CHECK (branch IN ('computer','mechanical','electrical','civil','chemical')),
  assets jsonb NOT NULL CHECK (jsonb_typeof(assets)='array' AND jsonb_array_length(assets)>0),
  reader_asset text NOT NULL CHECK (reader_asset ~ '^[a-f0-9]{64}$'),
  active boolean NOT NULL DEFAULT false,
  created_at timestamptz NOT NULL DEFAULT now(),
  CHECK (split_part(id,'--',1) NOT IN ('DI01000021','DI01000121'))
);
CREATE TABLE diplomaone_test.orders (
  id uuid PRIMARY KEY,
  uid text NOT NULL CHECK (length(uid) BETWEEN 1 AND 128),
  product_id text NOT NULL REFERENCES diplomaone_test.products(id),
  request_id uuid NOT NULL,
  receipt text NOT NULL UNIQUE CHECK (length(receipt)<=40),
  amount integer NOT NULL CHECK (amount IN (1900,2900,3900)),
  currency text NOT NULL DEFAULT 'INR' CHECK (currency='INR'),
  status text NOT NULL CHECK (status IN ('reserving','created','paid','unknown','failed','revoked')),
  razorpay_order_id text UNIQUE CHECK (razorpay_order_id ~ '^order_[A-Za-z0-9]{5,80}$'),
  payment_id text UNIQUE CHECK (payment_id ~ '^pay_[A-Za-z0-9]{5,80}$'),
  created_at timestamptz NOT NULL DEFAULT now(),
  paid_at timestamptz,
  UNIQUE (uid,request_id),
  UNIQUE (id,uid,product_id)
);
CREATE UNIQUE INDEX one_active_test_order_per_paper ON diplomaone_test.orders(uid,product_id)
  WHERE status IN ('reserving','created','unknown');
CREATE INDEX test_orders_user_time ON diplomaone_test.orders(uid,created_at DESC);
CREATE INDEX test_orders_time ON diplomaone_test.orders(created_at DESC);
CREATE TABLE diplomaone_test.entitlements (
  uid text NOT NULL,
  product_id text NOT NULL,
  order_id uuid NOT NULL UNIQUE,
  active boolean NOT NULL DEFAULT true,
  created_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (uid,product_id),
  FOREIGN KEY (order_id,uid,product_id) REFERENCES diplomaone_test.orders(id,uid,product_id)
);
CREATE TABLE diplomaone_test.events (
  id text PRIMARY KEY CHECK (length(id) BETWEEN 1 AND 200),
  body_hash text NOT NULL CHECK (body_hash ~ '^[a-f0-9]{64}$'),
  created_at timestamptz NOT NULL DEFAULT now()
);
REVOKE ALL ON ALL TABLES IN SCHEMA diplomaone_test FROM PUBLIC;
