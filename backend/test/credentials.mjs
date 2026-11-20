// Ephemeral local test key only; no owner credential is requested or retained.
import {generateKeyPairSync} from 'node:crypto';
export const fixturePrivateKey=generateKeyPairSync('rsa',{modulusLength:2048,
  privateKeyEncoding:{type:'pkcs8',format:'pem'},publicKeyEncoding:{type:'spki',format:'pem'}}).privateKey;
export const fixtureFirestoreEnv=Object.freeze({FIREBASE_PROJECT_ID:'diplomaone-53b4e',
  FIREBASE_CLIENT_EMAIL:'unit-fixture@diplomaone-53b4e.iam.gserviceaccount.com',FIREBASE_PRIVATE_KEY:fixturePrivateKey});
