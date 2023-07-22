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

    if "using" in update.message.text:
        reply_keyboard = [["Washer 1", "Washer 2","Washer 3"],["Dryer 1", "Dryer 2","Dryer 3","Dryer 4"]]
        await update.message.reply_text(
            "Please select a location",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard = True, input_field_placeholder="Command"),)
    
    if "Washer" in update.message.text or "Dryer" in update.message.text:
        await update.message.reply_text("Your machine will be done in 30 minutes.")
        now = datetime.now()
        time1 = now + timedelta(seconds=1)
        time2 = now + timedelta(seconds=2)
        #await update.message.reply_text("Your laundry will be done in 30 minutes.")

    if "Washer 1" in update.message.text:
        ref2 = db.collection("washers").document("washers1")
        ref2.update({"avail": False,"used_by":str(update.message.from_user.id), 'StartTime':now, 'collect':False})
    
    while datetime.now() < time1 :
        continue
    else:
        await update.message.reply_text("Your laundry will be done in 5 minutes.")

    while datetime.now() < time2 :
        continue
    else:
        ## here insert if statement 
        if "Washer 1" in update.message.text:
            ref2 = db.collection("washers").document("washers1")
            ref2.update({"avail": True,"used_by":str(update.message.from_user.id),'collect':False}) 
            await update.message.reply_text("Your laundry is done. Please collect soon") 

    if "finish" in update.message.text:
        query1 = db.collection('users').where('id', '==', '5578355017').get()
        query2 = db.collection('washers').where('id', '==', '5578355017').get()
        for post in query1:
            pr = '{} => {}'.format(post.id, post.to_dict())
            await update.message.reply_text(pr) 

            for post2 in query2:
                await update.message.reply_text(f'post2 is {post2}')
                pr2 = '{} => {}'.format(post2.id, post2.to_dict())
                await update.message.reply_text(f'pr is {pr}')
                await update.message.reply_text(f'pr2 is {pr2}')
                finish_time = post2.get('StartTime') + timedelta(seconds = 30)
                await update.message.reply_text(post2.get('StartTime'))
                await update.message.reply_text(f'finishing_time is {finish_time}')
                if finish_time > now: 
                    ori_point = post.get('point')
                    new_point = ori_point + 5
                    ref2 = db.collection("users").document(str(post.id))
                    ref2.update({"point": new_point})

        
        '''
        if now <( time2 + timedelta(seconds = 30)) : ## collect with in 5 min 
            # write the code here
            query1 = db.collection('users').where('id', '==', '5578355017').get()
            for post in query1:
                pr = '{} => {}'.format(post.id, post.to_dict())
                ori_point = post.get('point')
                new_point = ori_point + 5
                ref2 = db.collection("users").document(str(post.id))
                ref2.update({"point": new_point})   
        if now < time2 + timedelta(seconds = 60): # collect with in 10 minutes 
            query1 = db.collection('users').where('id', '==', str(update.message.from_user.id)).get()
            for post in query1:
                pr = '{} => {}'.format(post.id, post.to_dict())
                ref2 = db.collection("users").document(str(post.id)) 
                # get the original point 
                ori_point = pr.get('point')
                new_point = ori_point + 5
                ref2.update({"point": new_point})

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