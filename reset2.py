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

data = {'StartTime':datetime.now(), 'avail':True, 'collect': True, 'used_by':'', 'previous':'','prepre':''}
db.collection('dryersE').document('dryer1').set(data)
db.collection('dryersE').document('dryer2').set(data)
db.collection('dryersE').document('dryer3').set(data)
db.collection('dryersE').document('dryer4').set(data)

db.collection('dryersF').document('dryer1').set(data)
db.collection('dryersF').document('dryer2').set(data)
db.collection('dryersF').document('dryer3').set(data)
db.collection('dryersF').document('dryer4').set(data)



db.collection('washersE').document('washers1').set(data)
db.collection('washersE').document('washers2').set(data)
db.collection('washersE').document('washers3').set(data)
db.collection('washersE').document('washers4').set(data)

db.collection('washersF').document('washers1').set(data)
db.collection('washersF').document('washers2').set(data)
db.collection('washersF').document('washers3').set(data)
db.collection('washersF').document('washers4').set(data)