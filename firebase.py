import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred)
firestore = firestore.client()
Users = firestore.collection('Users')
Exercises = firestore.collection('Exercises')