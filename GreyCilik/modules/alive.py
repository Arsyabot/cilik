import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from GreyCilik.events import register
from GreyCilik import telethn as tbot
from GreyCilik import BOT_USERNAME as bu

PHOTO = "https://telegra.ph/file/d1e8cc958d662150b36ad.jpg"

@register(pattern=("/alive"))
async def awake(event):
  GREY = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm á´ÊÊÊ.** \n\n"
  GREY += "ð **I'm Working Properly** \n\n"
  GREY += f"ð **My Master : [á´ÊÊÊ](https://t.me/punya_alby)** \n\n"
  GREY += f"ð **Library Version :** `{telever}` \n\n"
  GREY += f"ð **Telethon Version :** `{tlhver}` \n\n"
  GREY += f"ð **Pyrogram Version :** `{pyrover}` \n\n"
  GREY += "**Thanks For Adding Me Here â¤ï¸**"
  BUTTON = [[Button.url("Êá´Êá´â", f"https://t.me/{bu}?start=help"), Button.url("sá´á´á´á´Êá´â", "https://t.me/ruangdiskusikami")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=GREY,  buttons=BUTTON)
