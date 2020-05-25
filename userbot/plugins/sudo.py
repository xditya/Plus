# Type .showsudo This will show your sudo users.

@command(pattern="^.showsudo", outgoing=True)
async def hello_world(event):
    if event.fwd_from:
        return
    await event.edit("**HELLO EVERYONE**\n\nThe following is controlling me too!\n" + Var.SUDO_USERS)


@command(pattern="^.showsudo", outgoing=True, allow_sudo=True)
async def hello_world(event):
    if event.fwd_from:
        return
    await event.reply("**HELLO EVERYONE**\n\nThe following is controlling me too!\n" + Var.SUDO_USERS)
