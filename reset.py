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

data = {'StartTime':datetime.now(), 'avail':True, 'collect': True, 'used_by':'123'}
db.collection('dryers').document('dryer1').set(data)
db.collection('dryers').document('dryer2').set(data)
db.collection('dryers').document('dryer3').set(data)
db.collection('dryers').document('dryer4').set(data)
db.collection('dryers').document('dryer5').set(data)
db.collection('dryers').document('dryer6').set(data)
db.collection('dryers').document('dryer7').set(data)
db.collection('dryers').document('dryer8').set(data)


db.collection('washer').document('washers1').set(data)
db.collection('washer').document('washers2').set(data)
db.collection('washer').document('washers3').set(data)
db.collection('washer').document('washers4').set(data)
db.collection('washer').document('washers5').set(data)
db.collection('washer').document('washers6').set(data)
db.collection('washer').document('washers7').set(data)
db.collection('washer').document('washers8').set(data)