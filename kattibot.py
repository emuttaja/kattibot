#!/usr/bin/env python3

import logging, datetime, pytz, requests

from telegram import (
    Update,
    ParseMode
)

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    MessageFilter,
)

#define timezones
FIN = pytz.timezone("Europe/Helsinki")


CHATS = [-1662405159]



#define handlers

def start(update:Update, context:CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= "Hii!"
    )

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= "@elijjjas is my creator. Message him instead. Use /katti to get a cat pic"
    )

def send_github_link(update:Update, context:CallbackContext):
    update.message.reply_text("Sources at https://github.com/emuttaja/kattibot")

def send_cat_to_groups(context:CallbackContext):
    """Get an ai generated picture of a random cat from
    thiscatdoesnotexist.com and send it to chats defined
    in CHATS

    Parameters
    ----------
    context : CallbackContext
        bot context
    """

    #download the cat
    url = "https://thiscatdoesnotexist.com/"
    img_data = requests.get(url).content

    #send the cat
    for chat in CHATS:
        # in theory we could just send a link to the image's location and telegram 
        # would display it but telegram's caching would not update the image 
        # thus the image would be the same every time
        context.bot.send_photo(chat_id=chat, photo=img_data)
    
def send_cat(update:Update, context:CallbackContext):
    """Get an ai generated picture of a random cat from
    thiscatdoesnotexist.com and send it to the user

    Parameters
    ----------
    context : CallbackContext
        bot context
    """

    #download the cat
    url = "https://thiscatdoesnotexist.com/"
    img_data = requests.get(url).content

    #send the cat
    
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=img_data)


def main():
    #load api key
    with open("api_key.txt", "r") as file:
        api_key = file.readline()
    

    #define bot updater
    updater = Updater(api_key)
    dispatcher = updater.dispatcher

    #add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("katti", send_cat))

    #start job queue
    job = updater.job_queue

    #add jobs
    cat_time = datetime.time(hour=20, minute=00, tzinfo=FIN)
    daily_cat = job.run_daily(send_cat_to_groups, cat_time)

    #main loop
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
