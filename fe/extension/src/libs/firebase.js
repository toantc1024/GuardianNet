// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAnalytics } from 'firebase/analytics';
import { getDatabase } from 'firebase/database';

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: 'AIzaSyA-TYhHB2B-OTgETDhhoCaMuvXKvqwwli0',
  authDomain: 'guardiannet-7a1a8.firebaseapp.com',
  databaseURL:
    'https://guardiannet-7a1a8-default-rtdb.asia-southeast1.firebasedatabase.app',
  projectId: 'guardiannet-7a1a8',
  storageBucket: 'guardiannet-7a1a8.appspot.com',
  messagingSenderId: '279238680698',
  appId: '1:279238680698:web:1262bb45dff259bb125bc3',
  measurementId: 'G-VG9JG1VMCP',
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export const database = getDatabase(app);
