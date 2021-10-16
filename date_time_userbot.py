#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [DATE_TIME Telegram userbot by TeLe TiPs] (https://github.com/sinan-m-116/DATE_TIME_USERBOT)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from lists_sinzz.quotes_sinzz import *
from lists_sinzz.emojis_sinzz import *
from PIL import Image, ImageDraw, ImageFont
import datetime
import pytz
import asyncio
import random
import os

Date_Time_Userbot=Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)

Time_Zone = os.environ["TIME_ZONE"]

async def main_sinzz():
    try:
        while True:
            if Date_Time_Userbot.is_connected:
                Quotes_sinzz = random.choice(quotes_sinzz)
                Emojis_sinzz = random.choice(emojis_sinzz)
                TimeZone_sinzz = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))
                Time_sinzz = TimeZone_sinzz.strftime("%I:%M %p")
                Date_sinzz = TimeZone_sinzz.strftime("%b %d") 
                Image_sinzz = Image.open("image.jpg")
                Image_font_sinzz = ImageFont.truetype("439415", 360)
                Image_text_sinzz = f"{Time_sinzz}"
                Image_edit_sinzz = ImageDraw.Draw(Image_sinzz)
                Image_edit_sinzz.text((690, 550), Image_text_sinzz, (0, 255, 255), font = Image_font_sinzz)
                Image_sinzz.save("Image_final_teletips.jpg")
                await Date_Time_Userbot_sinzz.update_profile(bio = f"{Emojis_sinzz} {Quotes_sinzz}" , last_name = f"| ⏰ {Time_sinzz} | 📅 {Date_sinzz}")
                await Date_Time_Userbot_sinzz.set_profile_photo(photo="Image_final_teletips.jpg")
                me = await Date_Time_Userbot_sinzz.get_me()
                photos = await Date_Time_Userbot_sinzz.get_profile_photos("me")
                try:
                    await Date_Time_Userbot_sinzz.delete_profile_photos(photos[1].file_id)
                except Exception:
                    pass        
                print("Profile Updated!")
            await asyncio.sleep(60)     
    except FloodWait as e:
        await asyncio.sleep(e.x)         

print("DATE TIME USERBOT IS ALIVE!")
asyncio.ensure_future(main_sinzz())
Date_Time_Userbot_sinzz.run()

#Copyright ©️ 2021 TeLe tips. All Rights Reserved
