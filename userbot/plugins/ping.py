from telethon import events
from datetime import datetime
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="ping"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!\n{}".format(ms))

@borg.on(admin_cmd(pattern="ping", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    a = await event.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await a.edit("Pong!\n{}".format(ms))