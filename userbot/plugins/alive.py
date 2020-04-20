"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet."

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("   **Welcome To X-Tra-TG**\n\n"
    				 "` 🔸 Telethon version:` **1.11.3**\n` 🔹 Python:` **3.6.10** \n` 🔸 Fork by:` @buddhhu\n"
                     "` 🔹 Bot created by:` [༺•|•𝙺𝚄𝙼𝙰𝚁•𝙰𝙼𝙸𝚃•|•༻](tg://user?id=667805879)\n"
                     "` 🔸 Database Status:` **All OK 👌!**\n"
                     f"` 🔹 My peru owner`: {DEFAULTUSER}\n\n"
                     "           [Deploy this userbot Now](https://github.com/amitsharma123234/X-tra-Telegram)")
