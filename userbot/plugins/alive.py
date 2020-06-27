"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import python_version, uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet."

@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("   **MADE IN 🇮🇳 , MADE FOR 🗺️** \n\n"
    				 "`"
    				 f"    🔸 Telethon : {version.__version__} \n   🔹 Python: {python_version()} \n"
    				 "`"
                     f"`  🔸 Fork by:` {DEFAULTUSER} \n "
                     "`🔹 Bot creator:` [//•𝙺𝚞𝚖𝚊𝚛•𝙰𝚖𝚒𝚝•//](tg://user?id=667805879)\n"
                     "`  🔸 Database Status:` **All OK 👌!** \n"
                     f"`   🔹 My owner:` {DEFAULTUSER}  \n"
                     "`    🔸 Join` @xtratgplus `For Help` \n\n"
                     "                      [Deploy✔️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus&template=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus)  \n\n    ")

@borg.on(admin_cmd(pattern="sudo", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.reply("   **MADE IN 🇮🇳 , MADE FOR 🗺️** \n\n"
    				 "`"
    				 f"    🔸 Telethon : {version.__version__} \n   🔹 Python: {python_version()} \n"
    				 "`"
                     f"`  🔸 Fork by:` {DEFAULTUSER} \n "
                     "`🔹 Bot creator:` [//•𝙺𝚞𝚖𝚊𝚛•𝙰𝚖𝚒𝚝•//](tg://user?id=667805879)\n"
                     "`  🔸 Database Status:` **All OK 👌!** \n"
                     f"`   🔹 My owner:` {DEFAULTUSER}  \n"
                     "`    🔸 Join` @xtratgplus `For Help` \n\n"
                     "                      [Deploy✔️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus&template=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus) \n\n",  link_preview=False
                     )
