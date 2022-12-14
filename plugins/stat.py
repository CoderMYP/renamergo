import os
import asyncio
from pyrogram import Client ,filters
from helper.database import getid ,delete
import time
ADMIN = int(os.environ.get("ADMIN", 5415124528))
 

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["stat"]))
async def stat(bot, message):
   ms = await message.reply_text("Azolar sanalmoqda...........")
   ids = getid()
   tot = len(ids)
   success = 0 
   failed = 0 
   await ms.edit(f"Bot foydalanuvchilari {tot} ta")
