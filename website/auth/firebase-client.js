// This module is bundled locally. No CDN, Analytics, Firestore, Storage,
// admin credentials or client-side purchase entitlements are loaded.
import { initializeApp } from '@firebase/app';
import {
  initializeAuth, browserSessionPersistence, browserPopupRedirectResolver,
  GoogleAuthProvider, onAuthStateChanged, signInWithPopup, signOut,
} from '@firebase/auth';
import { firebaseConfig } from './firebase-config.js';
import { createConnectionCheck } from './connection-check.js';
import { createPaymentClient } from './payment-client.js';

export function createClient(onUser, onError) {
  const app = initializeApp(firebaseConfig, 'diplomaone-website');
  // Session-only persistence: closing this browser tab ends this site's saved
  // session. Google may still be signed in. No tokens enter app-managed storage;
  // the manual read-only check sends an ID token only as a same-origin header.
  const auth = initializeAuth(app, {
    persistence: browserSessionPersistence,
    popupRedirectResolver: browserPopupRedirectResolver,
  });
  const provider = new GoogleAuthProvider();
  provider.setCustomParameters({ prompt: 'select_account' });
  const connection=createConnectionCheck(()=>auth.currentUser),payments=createPaymentClient(()=>auth.currentUser);
  const changed=()=>{connection.cancel();payments.cancel();};
  const unsubscribe = onAuthStateChanged(auth,user=>{changed();onUser(user);},error=>{changed();onError?.(error);});
  return Object.freeze({
    dispose(){connection.dispose();payments.dispose();unsubscribe();},
    paymentConfiguration:()=>payments.configuration(),
    loadPurchases:()=>payments.purchases(),
    readPurchasedPaper:id=>payments.readPaper(id),
    readPurchasedAsset:(id,asset)=>payments.readAsset(id,asset),
    buyPaper:id=>payments.buy(id),
    cancelPayments:()=>payments.cancel(),
    checkTestConnection:()=>connection.check(),
    cancelTestConnection:()=>connection.cancel(),
    ready: () => auth.authStateReady(),
    signIn(language) {
      auth.languageCode = language === 'gu' ? 'gu' : 'en';
      // Called directly from the click handler, after readiness. Do not insert
      // an await/import before signInWithPopup or silently fall back to redirect.
      // The returned Google OAuth credential/token never leaves the SDK layer.
      return signInWithPopup(auth, provider).then(() => undefined);
    },
    signOut(){changed();return signOut(auth);},
  });
}
