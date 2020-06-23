"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import python_version, uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet."

@command(outgoing=True, pattern="^.alive$")
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
                     "                      [Deploy✔️](https://github.com/amitsharma123234/X-tra-TG-plus) \n\n    ")

@command(outgoing=True, pattern="^.sudo$", allow_sudo=True)
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
                     "                      [Deploy✔️](https://github.com/amitsharma123234/X-tra-TG-plus) \n\n",  link_preview=False
                     )
