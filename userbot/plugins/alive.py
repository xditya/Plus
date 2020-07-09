import random
from userbot.plugins.sql_helper.global_variables_sql import ALIVESTR
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="alive"))
async def alive(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(random.choice(ALIVESTR))
        
@borg.on(admin_cmd(pattern="sudoalive", allow_sudo=True))
async def sudo(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.reply(random.choice(ALIVESTR))