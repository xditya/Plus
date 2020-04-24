"""
Time In Profile Pic.....
Command: `.Bloom`

Recoded :: Now It is just plug and play ;)

:::::Credit Time::::::
1) Coded By: @s_n_a_p_s
2) Ported By: @r4v4n4 (Noodz Lober)
3) End Game Help By: @spechide
4) Better Colour Profile Pic By @PhycoNinja13b

#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN. WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""

import io
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions
from uniborg.util import admin_cmd
from misc.font_sel import fontsel
import asyncio
import random


@borg.on(admin_cmd(pattern="bloom ?(.*)", allow_sudo=True))
async def autopic(event): 
    await event.reply("Bloom colour profile pic have been enabled © @PhycoNinja13b") 
    
    while True:
        #RIP Danger zone Here no editing here plox

        FONT_FILE_TO_USE = fontsel()

        #Background Colour
        R = random.randint(0,256)
        B = random.randint(0,256)
        G = random.randint(0,256)

        #Username/Date/Time Colour
        FR = (256 - R) 
        FB = (256 - B) 
        FG = (256 - G)

        #Optional Emoji Colour
        ER = (128 - FR)
        EB = (128 - FB)
        EG = (128 - FG)

        #Check, so that output is not negative 
        if ER<0:
            ER = ER*(-1)
        if EB<0:
            EB = EB*(-1)
        if EG<0:
            EG = EG*(-1)
        
        bg_img = Image.new("RGB", (640, 640), (R, G, B))
        
        #Edit only Below part 🌚 Or esle u will be responsible 🤷‍♂
        current_time = datetime.now().strftime("\nTime: %H:%M:%S \n \nDate: %d/%m/%y")
        drawn_text = ImageDraw.Draw(bg_img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 60)
        ofnt = ImageFont.truetype(FONT_FILE_TO_USE, 20)
        efnt = ImageFont.truetype(FONT_FILE_TO_USE, 200)
        
        drawn_text.text((100, 200), current_time, font=fnt, fill=(FR,FG,FB))
        drawn_text.text((100, 200), "© @PhycoNinja13b", font = ofnt, fill=(FR,FG,FB))
        drawn_text.text((120, 50), "    😼", font = efnt, fill=(ER,EG,EB))
        
        pic_img = io.BytesIO()
        bg_img.save(pic_img,"Jpeg")
        pic_img.seek(0)
        file = await event.client.upload_file(pic_img)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            await asyncio.sleep(59)
        except:
            return
