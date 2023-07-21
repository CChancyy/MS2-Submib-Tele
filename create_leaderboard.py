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


ref1 = db.collection("dryers").document("dryer1")
ref2 = db.collection("users").document("user_5")
ref2.update({"point": 0})

existing_posts = db.collection(u'users').where(u'id', u'==', u'tele_handle_1').get()
for post in existing_posts:
    print(u'{} => {}'.format(post.id, post.to_dict()))
    print (post.get('username')) ## it has returned the correct one 


bal = ref1.get(field_paths={'StartTime'}).to_dict().get('StartTime')
print (bal)
##print (existing_posts.get('username'))

## time2 = now + timedelta(seconds=60)
'''
    if "finish" in update.message.text:
        collect_tiem = datetime.now()
        if collect_tiem < time2 + timedelta(seconds=60): # collect with in 5 min 
            ## need to write the command to change the thing here use where i think 

            await update.message.reply_text("Thank you! We have awarded you 5 ponits.")

'''