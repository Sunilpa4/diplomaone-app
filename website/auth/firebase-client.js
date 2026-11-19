// This module is bundled locally. No CDN, Analytics, Firestore, Storage,
// payments, admin credentials or client-side purchase entitlements are loaded.
import { initializeApp } from '@firebase/app';
import {
  initializeAuth, browserSessionPersistence, browserPopupRedirectResolver,
  GoogleAuthProvider, onAuthStateChanged, signInWithPopup, signOut,
} from '@firebase/auth';
import { firebaseConfig } from './firebase-config.js';

export function createClient(onUser, onError) {
  const app = initializeApp(firebaseConfig, 'diplomaone-website');
  // Session-only persistence: closing this browser tab ends this site's saved
  // session. Google itself may still be signed in. No tokens are copied by us.
  const auth = initializeAuth(app, {
    persistence: browserSessionPersistence,
    popupRedirectResolver: browserPopupRedirectResolver,
  });
  const provider = new GoogleAuthProvider();
  provider.setCustomParameters({ prompt: 'select_account' });
  const unsubscribe = onAuthStateChanged(auth, onUser, onError);
  return Object.freeze({
    dispose: unsubscribe,
    ready: () => auth.authStateReady(),
    signIn(language) {
      auth.languageCode = language === 'gu' ? 'gu' : 'en';
      // Called directly from the click handler, after readiness. Do not insert
      // an await/import before signInWithPopup or silently fall back to redirect.
      // The returned Google OAuth credential/token never leaves the SDK layer.
      return signInWithPopup(auth, provider).then(() => undefined);
    },
    signOut: () => signOut(auth),
  });
}
