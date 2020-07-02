# global variables will be assigned here
# can be imported in any module to make life easier.
from userbot.config import Config
import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import python_version, uname
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet."

ALIVE = f"**MADE IN 🇮🇳 , MADE FOR 🗺️** \n\n`🔸 Telethon : {version.__version__} \n🔹 Python: {python_version()} \n``🔸 Fork by:` {DEFAULTUSER} \n`🔹 Bot creator:` [//•𝙺𝚞𝚖𝚊𝚛•𝙰𝚖𝚒𝚝•//](tg://user?id=667805879)\n`🔸 Database Status:` **All OK 👌!** \n`🔹 My owner:` {DEFAULTUSER}  \n`🔸 Join` @xtratgplus `For Help` \n\n                      [Deploy✔️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus&template=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus)  \n\n   "

ALIVESTR = [f"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█  █░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n{ALIVE}",
	f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n{ALIVE}",
	f"╔╦═╦╗\n║║║║╠═╦╗╔═╦═╦══╦═╗\n║║║║║╩╣╚╣═╣╬║║║║╩╣\n╚═╩═╩═╩═╩═╩═╩╩╩╩═╝\n{ALIVE}",
	f"╭╮╭╮╭╮╱╱╭╮\n┃┃┃┃┃┃╱╱┃┃\n┃┃┃┃┃┣━━┫┃╭━━┳━━┳╮╭┳━━╮\n┃╰╯╰╯┃┃━┫┃┃╭━┫╭╮┃╰╯┃┃━┫\n╰╮╭╮╭┫┃━┫╰┫╰━┫╰╯┃┃┃┃┃━┫\n╱╰╯╰╯╰━━┻━┻━━┻━━┻┻┻┻━━╯\n{ALIVE}"]
	
LOGGER = Config.PRIVATE_GROUP_BOT_API_ID
BLACKLIST = Config.UB_BLACK_LIST_CHAT
SYNTAX = {}
SUDO_USERS = Config.SUDO_USERS
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
BUILD = "Plus+"
