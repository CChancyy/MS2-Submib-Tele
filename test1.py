import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import nest_asyncio
import asyncio
import datetime
from datetime import datetime, timedelta

cred = credentials.Certificate('/Applications/NUS/Orbital Material/Database/_MS2 Submission/test1-0807-cloud.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

ref2 = db.collection("dryers").document("dryer1")
ref2.update({"avail": False})

#bal = ref2.get(field_paths={'avail'}).to_dict().get('avail')
bal = ref2.get(field_paths={'StartTime'}).to_dict().get('StartTime')
print (bal)
print (bal + timedelta (seconds=30))
ref2.update({"End": bal + timedelta (seconds=30)})

