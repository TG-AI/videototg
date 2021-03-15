import redis
import pyrogram
# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

r = redis.from_url(os.environ.get("REDIS_URL"))
db_keys = r.keys(pattern="*")
@pyrogram.Client.on_message(pyrogram.filters.command(["bodcast"]))
async def bodcast(bot, update):
    
    if update.from_user.id in Config.AUTH_USERS:
      for keys in db_keys:
        keys_values = r.get(keys).decode("UTF-8")
        print(keys_values)
        await bot.send_message(
                  chat_id=keys_values,
                  text=update.reply_to_message
        ) 
          
       
          
