import {createPrivateKey} from 'node:crypto';

export const FIREBASE_PROJECT='diplomaone-53b4e';
export const FIRESTORE_DATABASE='(default)';
export const FIRESTORE_ROOT='diplomaone_test/v1';

// Backend-only, explicit credentials. Never use browser config as an Admin key,
// implicitly discover an unrelated ADC project, or honor an emulator in a live
// Function. Returning null deliberately exposes no raw PEM/parser errors.
export function firestoreOptions(env=process.env){
  if(env.FIREBASE_PROJECT_ID!==FIREBASE_PROJECT||env.FIRESTORE_EMULATOR_HOST||
    (env.FIRESTORE_DATABASE_ID&&env.FIRESTORE_DATABASE_ID!==FIRESTORE_DATABASE))return null;
  const email=env.FIREBASE_CLIENT_EMAIL;
  if(typeof email!=='string'||!/^[a-zA-Z0-9._-]+@diplomaone-53b4e\.iam\.gserviceaccount\.com$/.test(email))return null;
  if(typeof env.FIREBASE_PRIVATE_KEY!=='string'||env.FIREBASE_PRIVATE_KEY.length>16384)return null;
  try{
    const pem=env.FIREBASE_PRIVATE_KEY.replace(/\\n/g,'\n').trim()+'\n';
    const key=createPrivateKey(pem);
    if(key.asymmetricKeyType!=='rsa'||key.asymmetricKeyDetails.modulusLength<2048)return null;
    return {projectId:FIREBASE_PROJECT,databaseId:FIRESTORE_DATABASE,preferRest:true,
      apiEndpoint:'firestore.googleapis.com',ssl:true,
      credentials:{client_email:email,private_key:pem}};
  }catch(_){return null;}
}
