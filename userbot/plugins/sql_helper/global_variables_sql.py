# global variables will be assigned here
# can be imported in any module to make life easier.
from userbot.config import Config
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, AUTOPIC_FONT_COLOUR, AUTOPIC_FONT, AUTOPIC_COMMENT
	
AUTO_PIC_FONT = str(AUTOPIC_FONT) if AUTOPIC_FONT else "DejaVuSansMono.ttf"
FONT_FILE_TO_USE = f"fonts/{AUTO_PIC_FONT}"
AUTOPIC_STR = str(AUTOPIC_COMMENT) if AUTOPIC_COMMENT else "Life Is too Short.\n And so is TG account."
COLOUR = str(AUTOPIC_FONT_COLOUR) if AUTOPIC_FONT_COLOUR else "#000000"

GN = "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･"
GM = "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･"
LIKE = "👍🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👍🏿\n👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿\n👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👉🏻❤👈🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿\n👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿\n👍🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👍🏿"
LOL = "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥•°\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ \n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ \n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ \n╱┗━━━┛╰━━━╯┗━━━┛╱\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥°•"


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
MODULE = []