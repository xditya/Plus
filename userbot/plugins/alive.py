import os
from userbot.plugins.sql_helper.global_variables_sql import ALIVE, ALIVESTR
from userbot.utils import admin_cmd

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
PLUSPIC = ALIVE_PIC

@borg.on(admin_cmd(pattern="alive"))
async def iamalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    
    if PLUSPIC:
    	await borg.send_file(alive.chat_id, PLUSPic, caption=ALIVE)
    	await alive.delete()
    else:
    	await alive.edit(f"{ALIVESTR}")

@borg.on(admin_cmd(pattern="sudo", allow_sudo=True))
async def iamalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    
    if PLUSPIC:
      await borg.send_file(alive.chat_id, PLUSPIC, caption=ALIVE)
      await alive.delete()
    else:
      await alive.reply(f"{ALIVESTR}")
