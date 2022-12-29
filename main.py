import os
import telegram.ext
import telegram.bot
import random
import time
from dotenv import load_dotenv

# commands for BotFather
# bg_pvp - fancy a pvp board game
# bg_coop - fancy a coop board game
# roll1 - roll a D6
# roll2 - roll 2D6


# Initial settings
load_dotenv()
API_KEY = os.getenv('TOKEN')
bot = telegram.Bot(API_KEY)
bext = telegram.ext
updater = telegram.ext.Updater(token=API_KEY, use_context=True)
disp = updater.dispatcher

bg_list = {
    "competitive": {
        "name": ["King of Tokyo", "Unmatched", "Jamaica", "Terror Below", "Zombies!!!", "The Bloody Inn", "Gekido",
                 "Destinies", "Alien Frontiers", "Cartagena", "Histrio", "Tapeworm", "Neon Gods", "Deep Sea Adventure",
                 "Colt Express", "Hit Z Road", "Ticket to Ride"]
    },
    "co-op": {
        "name": ["Reign of Cthulhu", "Horrified"]
    }
}


# The fun part.
def start(update, context):
    bot.send_message(chat_id=999004365, text="Welcome to kamaBot!")


def bg_pvp(update, context):
    get_rand = random.randint(0, (len(bg_list["competitive"]["name"]) - 1))
    bot.send_message(chat_id=999004365, text=f"Why don't you try {bg_list['competitive']['name'][get_rand]} today?")


def bg_coop(update, context):
    get_rand = random.randint(0, (len(bg_list["co-op"]["name"]) - 1))
    bot.send_message(chat_id=999004365, text=f"Why don't you try {bg_list['co-op']['name'][get_rand]} today?")


def die(update, context):
    d1 = bot.send_dice(chat_id=999004365)
    time.sleep(3.7)
    bot.send_message(chat_id=999004365, text=f'You rolled a {d1["dice"]["value"]}')


def dice(update, context):
    d1 = bot.send_dice(chat_id=999004365)
    d2 = bot.send_dice(chat_id=999004365)
    time.sleep(3.7)
    if d1["dice"]["value"] == 1 and d2["dice"]["value"] == 1:
        bot.send_message(chat_id=999004365, text='Wow... double 1. Nice try!')
    elif d1["dice"]["value"] == 6 and d2["dice"]["value"] == 6:
        bot.send_message(chat_id=999004365, text='Double 6! It must be your lucky day!')
    else:
        bot.send_message(chat_id=999004365, text=f'You rolled a {(d1["dice"]["value"] + d2["dice"]["value"])}')


disp.add_handler(bext.CommandHandler("start", start))
disp.add_handler(bext.CommandHandler("bg_pvp", bg_pvp))
disp.add_handler(bext.CommandHandler("bg_coop", bg_coop))
disp.add_handler(bext.CommandHandler("roll1", die))
disp.add_handler(bext.CommandHandler("roll2", dice))

updater.start_polling()
updater.idle()
