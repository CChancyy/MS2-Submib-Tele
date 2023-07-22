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

query1 = db.collection('users').where('id', '==', '5578355017').get()
for post in query1:
    pr = '{} => {}'.format(post.id, post.to_dict())
    ori_point = post.get('point')
    new_point = ori_point + 5
    ref2 = db.collection("users").document(str(post.id))
    ref2.update({"point": new_point})





'''
data = {'id':'123', 'point':0, 'username': '123'}
db.collection('users').add(data)


# id point and username


ref1 = db.collection("dryers").document("dryer1")
ref2 = db.collection("users").document("user_5")
ref2.update({"point": 0})

existing_posts = db.collection(u'users').where(u'id', u'==', u'tele_handle_1').get()
for post in existing_posts:
    print(u'{} => {}'.format(post.id, post.to_dict()))
    print (post.get('username')) ## it has returned the correct one 

print ('the testing is velow')


bal = ref1.get(field_paths={'StartTime'}).to_dict().get('StartTime')
print (bal)

## seem like it is still can use if we delet the u 
print ("below is not using u")

ref6 = db.collection(u'users').where(u'id', u'==', u'tele_handle_1').get()
for post in ref6:
    print ('here is test')
    print(u'{} => {}'.format(post.id, post.to_dict()))
    print (post.get('username')) ## it has returned the correct one 
print('\n fisnish')
print(f'ref6 type is {type(ref6)}')
print(f'ref6  is {ref6}') ## so the 判定方法是 empty list or not 

existing_posts = db.collection('users').where('id', '==', 'tele_handle_2').get()
for post in existing_posts:

    pr = '{} => {}'.format(post.id, post.to_dict())
    print (f'pr it {pr}')
    print (post.get('username')) ## it has returned the correct one 
    print(f'existing_posts it {existing_posts}')
    print (f'post it {post}')
    print(f'post id it {post.id}') ## post.id is the name of the document 
           
    ref5 = db.collection("users").document(str(post))
    ref2.update({"point": 5})
        ## create a new thing to store the guy's info

##print (existing_posts.get('username'))

## time2 = now + timedelta(seconds=60)


    if "finish" in update.message.text:
        collect_tiem = datetime.now()
        if collect_tiem < time2 + timedelta(seconds=60): # collect with in 5 min 
            ## need to write the command to change the thing here use where i think 

            await update.message.reply_text("Thank you! We have awarded you 5 ponits.")

'''