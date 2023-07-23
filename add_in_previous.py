###################### Code for all the import ##################################################################
##########################################################################################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import nest_asyncio
import asyncio
from telegram import Update
from telegram.constants import ParseMode
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler
import math
from random import random
import datetime
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram import *
from telegram.ext import *
from requests import *
from datetime import datetime, timedelta

########################## Creating cred ################################################################
cred = credentials.Certificate('/Applications/NUS/Orbital Material/Database/_MS2 Submission/test1-0807-cloud.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

################################ logging ###############################
nest_asyncio.apply()
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Your token goes here
token = "5822080229:AAGQV8VM3SqQ5WfB7P9CNG9sf_q4PodHdy4" ## DAWNUS Bot 

# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
ONE, TWO, THREE, FOUR = range(4)

########################### the start page ##################################################
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [["I am using a machine!"], ["I have finished a machine"], ["Leaderboard"], ["Contact Previous User","Lost and Found"]]
    ## here is the code to add the user's info to the users document 
    if db.collection('users').where('id', '==', str(update.message.from_user.id)).get() == []:
        data = {'id':str(update.message.from_user.id), 'point':0, 'username': str(update.message.from_user.username)}
        db.collection('users').add(data) # store the user's info in firebase 
    
    await update.message.reply_text(
        "Hi! Welcome to NUS Laundry Tracker, how can I help you? ",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard = True, input_field_placeholder="Command"
        ),
    )
    
# now is another function
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if 'Contact Previous User' in update.message.text: 
        await update.message.reply_text(
            "Please send the message in the following format: \n \nTo the previous user: [the content you want to send] \n \nNotice that you can also provide your telegram handle so that the previous user can get back to you :) ")
    
    if 'previous' in update.message.text: 
        ## if he is the pre and he need to find the prepre
        if db.collection('washers').where('previous', '==', str(update.message.from_user.id)).get() != []:
            query = db.collection('washers').where('previous', '==', str(update.message.from_user.id)).get()
            for post in query:
                target_chat_id = post.get('prepre')
                message = update.message
                await context.bot.send_message(chat_id=target_chat_id, text="Hi! You have an incoming message from the next user of the machine.")
                await context.bot.forward_message(chat_id=target_chat_id, from_chat_id=message.chat.id, message_id=message.message_id)
                await context.bot.send_message(chat_id=update.effective_chat.id, text="Message forwarded successfully!")

        if db.collection('dryers').where('previous', '==', str(update.message.from_user.id)).get() != []:
            query = db.collection('dryers').where('previous', '==', str(update.message.from_user.id)).get()
            for post in query:
                target_chat_id = post.get('prepre')
                message = update.message
                await context.bot.send_message(chat_id=target_chat_id, text="Hi! You have an incoming message from the next user of the machine.")
                await context.bot.forward_message(chat_id=target_chat_id, from_chat_id=message.chat.id, message_id=message.message_id)
                await context.bot.send_message(chat_id=update.effective_chat.id, text="Message forwarded successfully!")

        ## if he is the current and he need to find the previous
        if db.collection('washers').where('used_by', '==', str(update.message.from_user.id)).get() != []:
            query = db.collection('dryers').where('used_by', '==', str(update.message.from_user.id)).get()
            for post in query:
                target_chat_id = post.get('previous')
                message = update.message
                await context.bot.send_message(chat_id=target_chat_id, text="Hi! You have an incoming message from the next user of the machine.")
                await context.bot.forward_message(chat_id=target_chat_id, from_chat_id=message.chat.id, message_id=message.message_id)
                await context.bot.send_message(chat_id=update.effective_chat.id, text="Message forwarded successfully!")


        if db.collection('dryers').where('used_by', '==', str(update.message.from_user.id)).get() != []:
            query = db.collection('dryers').where('used_by', '==', str(update.message.from_user.id)).get()
            for post in query:
                target_chat_id = post.get('previous')
                message = update.message
                await context.bot.send_message(chat_id=target_chat_id, text="Hi! You have an incoming message from the next user of the machine.")
                await context.bot.forward_message(chat_id=target_chat_id, from_chat_id=message.chat.id, message_id=message.message_id)
                await context.bot.send_message(chat_id=update.effective_chat.id, text="Message forwarded successfully!")

        

        
    if "using" in update.message.text: ## select location
        reply_keyboard = [["RVRC BLK E"],["RVRC BLK F"]]
        await update.message.reply_text(
            "Please select a location",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard = True, input_field_placeholder="Command"),)
        
    if "BLK E" in update.message.text and "Washer" not in update.message.text and "Dryer" not in update.message.text: ## select machine
        reply_keyboard = [["E Washer 1", "E Washer 2","E Washer 3","E Washer 4"],["E Dryer 1", "E Dryer 2","E Dryer 3","E Dryer 4"]]
        await update.message.reply_text(
            "Please select a location",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard = True, input_field_placeholder="Command"),)
        
    if "BLK F" in update.message.text and "Washer" not in update.message.text and "Dryer" not in update.message.text: ## select machine
        reply_keyboard = [["F Washer 1", "F Washer 2","F Washer 3","F Washer 4"],["F Dryer 1", "F Dryer 2","F Dryer 3","E Dryer 4"]]
        await update.message.reply_text(
            "Please select a location",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard = True, input_field_placeholder="Command"),)

    if "Washer" in update.message.text or "Dryer" in update.message.text:
        await update.message.reply_text("Your machine will be done in 30 minutes.")
        now = datetime.now()
        time1 = now + timedelta(seconds=1)
        global finish_time 
        finish_time = now + timedelta(seconds=2)
        
        #await update.message.reply_text("Your laundry will be done in 30 minutes.")

    if "E Washer 1" in update.message.text:
        ref2 = db.collection("washers").document("washers1")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "E Washer 2" in update.message.text:
        ref2 = db.collection("washers").document("washers2")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "E Washer 3" in update.message.text:
        ref2 = db.collection("washers").document("washers3")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "E Washer 4" in update.message.text:
        ref2 = db.collection("washers").document("washers4")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "F Washer 1" in update.message.text:
        ref2 = db.collection("washers").document("washers5")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "F Washer 2" in update.message.text:
        ref2 = db.collection("washers").document("washers6")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "F Washer 3" in update.message.text:
        ref2 = db.collection("washers").document("washers7")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "F Washer 4" in update.message.text:
        ref2 = db.collection("washers").document("washers8")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})

    if "E Dryer 1" in update.message.text:
        ref2 = db.collection("dryers").document("dryer1")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "E Dryer 2" in update.message.text:
        ref2 = db.collection("dryers").document("dryer2")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "E Dryer 3" in update.message.text:
        ref2 = db.collection("dryers").document("dryer3")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "E Dryer 4" in update.message.text:
        ref2 = db.collection("dryers").document("dryer4")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "F Dryer 1" in update.message.text:
        ref2 = db.collection("dryers").document("dryer5")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "F Dryer 2" in update.message.text:
        ref2 = db.collection("dryers").document("dryer6")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "F Dryer 3" in update.message.text:
        ref2 = db.collection("dryers").document("dryer7")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    if "F Dryer 4" in update.message.text:
        ref2 = db.collection("dryers").document("dryer8")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})


    if "finish" in update.message.text: 
        collect_time = datetime.now()
        while collect_time > ( finish_time + timedelta(seconds = 30)) :
            # await update.message.reply_text("while is executing")
            continue
        else:
            # the following is the code for award the point
            query1 = db.collection('users').where('id', '==', str(update.message.from_user.id)).get()
            for post in query1:
                ref2 = db.collection("users").document(str(post.id))
                ref2.update({"point": post.get('point') + 5})  
                await update.message.reply_text(f"Thank you for collecting your clothes in time! \n 5 points has been awarded to you. \n Your current point is {post.get('point') + 5}." )
            
            ## write a function to determine either washer or dryer is used
            if db.collection('washers').where('used_by', '==', str(update.message.from_user.id)).get() != []:
                query2 = db.collection('washers').where('used_by', '==', str(update.message.from_user.id)).get()
                for post2 in query2:
                    ref3 = db.collection("washers").document(str(post2.id))
                    ref3.update({"collect": True})
                    #await update.message.reply_text("finish changing the status of collection to true") 
                    
            if db.collection('dryers').where('used_by', '==', str(update.message.from_user.id)).get() != []:
                query2 = db.collection('dryers').where('used_by', '==', str(update.message.from_user.id)).get()
                for post2 in query2:
                    ref3 = db.collection("dryers").document(str(post2.id))
                    ref3.update({"collect": True})
                    #await update.message.reply_text("finish changing the status of collection to true")      

    if 'Leaderboard' in update.message.text: 
        # write code here
        query = db.collection('users').order_by('point',direction=firestore.Query.DESCENDING).limit(5)
        results = query.get()
        a = 1
        message = ''
        for post in results:
            message = message + "No." + str(a) + '       ' + str(post.get('username'))  + '       '  + str(post.get('point')) + '\n'
            a = a + 1 
        await update.message.reply_text (message)
        

    while datetime.now() < time1 :
        continue
    else:
        await update.message.reply_text("Your laundry will be done in 5 minutes.")

    while datetime.now() < finish_time :
        continue
    else:
        ## here insert if statement, change the state of washing machine to finish
        if db.collection('washers').where('used_by', '==', str(update.message.from_user.id)).get() != []:
            query2 = db.collection('washers').where('used_by', '==', str(update.message.from_user.id)).get()
            for post2 in query2:
                ref3 = db.collection("washers").document(str(post2.id))
                ref3.update({"avail": True})
            await update.message.reply_text("Your laundry is done. Please collect soon") 
        
        if db.collection('dryers').where('used_by', '==', str(update.message.from_user.id)).get() != []:
            query2 = db.collection('dryers').where('used_by', '==', str(update.message.from_user.id)).get()
            for post2 in query2:
                ref3 = db.collection("dryers").document(str(post2.id))
                ref3.update({"avail": True}) 
            await update.message.reply_text("Your laundry is done. Please collect soon") 
    
'''
       if "E Washer 1" in update.message.text:
            ref2 = db.collection("washers").document("washers1")
            ref2.update({"avail": True,"used_by":str(update.message.from_user.id),'collect':False}) 
            await update.message.reply_text("Your laundry is done. Please collect soon") 
        if "E Washer 2" in update.message.text:
            ref2 = db.collection("washers").document("washers2")
            ref2.update({"avail": True,"used_by":str(update.message.from_user.id),'collect':False}) 
            await update.message.reply_text("Your laundry is done. Please collect soon") 
        if "E Washer 3" in update.message.text:
            ref2 = db.collection("washers").document("washers3")
            ref2.update({"avail": True,"used_by":str(update.message.from_user.id),'collect':False}) 
            await update.message.reply_text("Your laundry is done. Please collect soon") 
        if "E Washer 4" in update.message.text:
            ref2 = db.collection("washers").document("washers4")
            ref2.update({"avail": True,"used_by":str(update.message.from_user.id),'collect':False}) 
            await update.message.reply_text("Your laundry is done. Please collect soon") 
        if "E Washer 4" in update.message.text:
            ref2 = db.collection("washers").document("washers3")
            ref2.update({"avail": True,"used_by":str(update.message.from_user.id),'collect':False}) 
            await update.message.reply_text("Your laundry is done. Please collect soon") 
'''


################################ this is the cannot change part ################################

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text="You are saved!")
    #TODO 3 Register my handlers

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """In the case of an unknown command"""
    #TODO 4
    pass

async def quadratic(update, context) -> None:
    # This will give us all the words in the message, which will be something like "/quadratic 1 2 3"
    # Hint: You can use the `split()` method of a Python string
    # TODO 5
    pass

async def cat(update, context) -> None:
    timestamp = datetime.datetime.now().isoformat()
    url = f"https://cataas.com/cat?a={timestamp}" # As Telegram caches the URL
    #Hint: You can use the `reply_photo()` method
    # TODO 6
    pass

# Bonus content - inline mode. To test this out, type `/setinline` in @BotFather and type @ in any of your other chats to talk to your bot
async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Capitalises the message."""
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    """Start the bot."""
    application = ApplicationBuilder().token(token).build()

    # Create your handlers here
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)


    # Register your handlers here
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    # Error handler
    application.add_error_handler(error)

    # Add your quadratic and cat handlers here
    # TODO 7

    # We pass in the Telegram event loop as a nested event loop here - only for Jupyter
    # Python version < 3.7
    # loop = asyncio.get_event_loop()
    # loop.create_task(application.run_polling())
    # Python version >= 3.7
    asyncio.run(application.run_polling())

main()


