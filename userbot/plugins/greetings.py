import asyncio
from uniborg.util import admin_cmd
from userbot.plugins.sql_helper.global_variables_sql import GN, GM, LIKE, LOL

DEL_TIMEOUT = 5

@borg.on(admin_cmd(pattern="gn"))
async def gn(event):
    await event.edit(f"{GN}")
    await asyncio.sleep(DEL_TIMEOUT)
    await event.delete()
    

@borg.on(admin_cmd(pattern="gm"))
async def gm(event):
    await event.edit(f"{GM}")
    await asyncio.sleep(DEL_TIMEOUT)
    await event.delete()


@borg.on(admin_cmd(pattern="like"))
async def like(event):
    await event.edit(f"{LIKE}")
    await asyncio.sleep(DEL_TIMEOUT)
    await event.delete()


@borg.on(admin_cmd(pattern="lol"))
async def lol(event):
    await event.edit(f"{LOL}")
    await asyncio.sleep(DEL_TIMEOUT)
    await event.delete()


@borg.on(admin_cmd(pattern="sudogn", allow_sudo=True))
async def gn(event):
    a = await event.reply(f"{GN}")
    await asyncio.sleep(DEL_TIMEOUT)
    await a.delete()
    

@borg.on(admin_cmd(pattern="sudogm", allow_sudo=True))
async def gm(event):
    a = await event.reply(f"{GM}")
    await asyncio.sleep(DEL_TIMEOUT)
    await a.delete()


@borg.on(admin_cmd(pattern="sudolike", allow_sudo=True))
async def like(event):
    a = await event.reply(f"{LIKE}")
    await asyncio.sleep(DEL_TIMEOUT)
    await a.delete()


@borg.on(admin_cmd(pattern="sudolol", allow_sudo=True))
async def lol(event):
    a = await event.reply(f"{LOL}")
    await asyncio.sleep(DEL_TIMEOUT)
    await a.delete()
