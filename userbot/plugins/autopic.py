# Modded by @buddhhu

import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
import asyncio
import shutil
from userbot.utils import admin_cmd
from userbot.plugins.sql_helper.global_variables_sql import FONT_FILE_TO_USE, AUTOPIC_STR, COLOUR

@borg.on(admin_cmd(pattern="autopic"))
async def autopic(event):
	await event.edit("**Autopic** has been Enabled!!")
	downloaded_file_name = "userbot/original_pic.png"
	downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)
	downloader.start(blocking=False)
	photo = "userbot/photo_pfp.png"
	while not downloader.isFinished():
		place_holder = None
		counter = -0
		while True:
			shutil.copy(downloaded_file_name, photo)
			im = Image.open(photo)
			file_test = im.rotate(counter, expand=False).save(photo, "PNG")
			current_time = datetime.now().strftime(f"Time: %H:%M \nDate: %d.%m.%y \n{AUTOPIC_STR}")
			img = Image.open(photo)
			drawn_text = ImageDraw.Draw(img)
			fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
			color = (COLOUR)
			drawn_text.text((95, 250), current_time, font=fnt, fill=color)
			img.save(photo)
			file = await bot.upload_file(photo)
			await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
			await event.client(functions.photos.UploadProfilePhotoRequest( file))
			os.remove(photo)
			await asyncio.sleep(60)