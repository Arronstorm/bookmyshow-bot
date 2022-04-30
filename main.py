import logging
import os

from telegram.ext import *
from constants import *
from telegram import *
from datetime import datetime
from datelist import Datelist
from movielist import Movielist
from theaterlist import TheaterListFinder
from theater import Theater_finder

print("the bot has started...........")

# constants for data storage
datetocheck = ""
location = ""
theater = ""
now = datetime.now()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start_command(update, context):
    user = update.message.from_user
    update.message.reply_text("Hi " + user.first_name + START_MSG)
    update.message.reply_text("To start with add your city by /city")


def help_command(update, context):
    update.message.reply_text(HELP_MSG)


def city_command(update, context):

    global location, theaterlist

    if len(context.args) == 1:
        tempArg = str(context.args[0])

        if tempArg in city_list:
            location = city_list[tempArg]
            update.message.reply_text("you have set the city as " + location)
            theaterlist = TheaterListFinder(location)

        else:
            location = tempArg
            update.message.reply_text("you have set the city as " + location)
            theaterlist = TheaterListFinder(location)

        update.message.reply_text("now add /theaters")

    else:
        update.message.reply_text(IF_NO_ARG_IS_GIVEN)


def theaters_command(update, context):

    global theater, theaternames, listofdates, theaternamelist

    if len(context.args) == 1:
        theater = (str(context.args[0])).lower()
        theaternames = Theater_finder(theaterlist, theater)

        if len(theaternames) > 1:
            update.message.reply_text(
                "your search has given these theater names")

            for theaterNamesPointer in range(len(theaternames)):
                theaternamelist = theaternames[theaterNamesPointer].split("_")
                update.message.reply_text(theaternamelist[1])

            update.message.reply_text("copy your theater and then proceed")
            update.message.reply_text("USE  '-'  INSTED OF '  '")

        else:
            datesetter = now.strftime("%Y%m%d")
            theaternamelist = theaternames[0].split("_")
            update.message.reply_text("Your have selected " + theaternamelist[1])
            monthnumber = int(now.strftime('%m'))
            tempDatelist = str(
                Datelist(location, theaternamelist[0], datesetter, monthnumber))
            listofdates = tempDatelist.replace("'", '').replace('[', '').replace(']', '')

            update.message.reply_text(
                theaternamelist[1] + " has shows in the dates below")
            update.message.reply_text(listofdates)
            update.message.reply_text("Proceed to /date if this is the one")
            update.message.reply_text("syntax - /date yyyy-mm-dd")
    else:
        update.message.reply_text(IF_NO_ARG_IS_GIVEN)


def date_command(update, context):

    global datetocheck

    if len(context.args) == 1:
        datetocheck = str(context.args[0])
        update.message.reply_text("You have set the date as " + datetocheck )
        update.message.reply_text("now get the movie list by /movies")

    else:
        year = now.strftime("%Y")
        month = now.strftime("%m")
        date = now.strftime("%d")
        datetocheck = year + "-" + month + "-" + date
        update.message.reply_text(IF_NO_ARG_IS_GIVEN_FOR_DATE + datetocheck)
        update.message.reply_text("now get the movie list by /movies")


def movies_command(update, context):

    listofmovies = Movielist(location, theaternamelist[0], datetocheck)

    update.message.reply_text(
        "These are the movies in " + theaternamelist[1] + " on " + datetocheck)

    for i in range(len(listofmovies)):
        update.message.reply_text(listofmovies[i])

if __name__ == "__main__":

    # stored in Heroku and is taken from there
    PORT = os.environ.get('PORT')
    API_KEY = os.getenv('API_KEY')
    HEROKU_LINK = os.getenv('HEROKU_LINK')

    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("date", date_command))
    dp.add_handler(CommandHandler("theaters", theaters_command))
    dp.add_handler(CommandHandler("city", city_command))
    dp.add_handler(CommandHandler("movies", movies_command))

    updater.start_webhook(listen="0.0.0.0", port=int(PORT),url_path=API_KEY,webhook_url=HEROKU_LINK + API_KEY)
    # updater.bot.setWebhook(HEROKU_LINK + API_KEY)
    # updater.idle()

    # updater.start_polling(1)
    updater.idle()
