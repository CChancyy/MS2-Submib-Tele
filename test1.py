import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import nest_asyncio
import asyncio

cred = credentials.Certificate('/Applications/NUS/Orbital Material/Database/_MS2 Submission/test1-0807-cloud.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

ref2 = db.collection("washers").document("washers1")
ref2.update({"avail": False})