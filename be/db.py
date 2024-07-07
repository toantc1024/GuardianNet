from functools import lru_cache


import pyrebase

# Todo: Create .env file and read later!
firebase_config = {
  "storageBucket": "guardiannet-7a1a8.appspot.com",
  "messagingSenderId": "279238680698",
  "apiKey": "AIzaSyA-TYhHB2B-OTgETDhhoCaMuvXKvqwwli0",
  "authDomain": "guardiannet-7a1a8.firebaseapp.com",
  "projectId": "guardiannet-7a1a8",
  "databaseURL": "https://guardiannet-7a1a8-default-rtdb.asia-southeast1.firebasedatabase.app",
  "appId": "1:279238680698:web:1262bb45dff259bb125bc3",
  "measurementId": "G-VG9JG1VMCP"
};


firebase = pyrebase.initialize_app(firebase_config)  
auth = firebase.auth()

db = firebase.database()


