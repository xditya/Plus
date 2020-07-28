from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.utils import load_module
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS, PLUG
from pathlib import Path
import asyncio
import telethon.utils
from telethon import events, functions, types
from telethon.tl.types import InputMessagesFilterDocument
import traceback
import userbot.utils

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
    
import glob
async def main():
	chat = Var.PLUGIN_CHANNEL
	documentss = await bot.get_messages(chat, None , filter=InputMessagesFilterDocument)
	total = int(documentss.total)
	total_doxx = range(0, total)
	for ixo in total_doxx:
		mxo = documentss[ixo].id
		downloaded_file_name = await bot.download_media(await bot.get_messages(chat, ids=mxo), "userbot/plugins/")
		path1 = Path(downloaded_file_name)
		shortname = path1.stem
		load_module(shortname.replace(".py", ""))


import userbot._core

print("Installed every plugin. Your bot is now ready...")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()


