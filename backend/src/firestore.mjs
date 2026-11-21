import {Firestore} from '@google-cloud/firestore';
import {firestoreOptions} from './firestore-config.mjs';
import {Problem} from './domain.mjs';

export function firestoreDatabase(env=process.env){
  const options=firestoreOptions(env);
  if(!options||process.env.FIRESTORE_EMULATOR_HOST)throw new Problem(503,'firestore_not_configured');
  // Construction is lazy with respect to network; explicit owner credentials,
  // fixed project/database and verified HTTPS. No ADC, emulator or public rules.
  return new Firestore(options);
}
