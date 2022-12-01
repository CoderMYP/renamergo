import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit , usertype,addpre
ADMIN = int(os.environ.get("ADMIN", 1706776746))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["ban"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("Foydalanuvchi muvaffaqqiyatli banlandi!")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("Foydalanuvchi banlanmadi xatolik!!!") 


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["dovip"]))
async def buypremium(bot, message):
	await message.reply_text("Ta'rifni tanlang.........",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Lite✨",callback_data = "vip1"), 
        			InlineKeyboardButton("VIP⚡",callback_data = "vip2") ]]))
        			

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/dovip")
	user_id = id[1].replace(" ", "")
	inlimit  = 16106127360
	uploadlimit(int(user_id),16106127360)
	usertype(int(user_id),"Lite✨")
	addpre(int(user_id))
	await update.message.edit("Ushbu user Lite✨ tarifiga ulandi! 15GB")
	await bot.send_message(user_id,"Ta'rifingiz Lite✨ ga ko'tarildi /tarif buyrug'i orqali ko'rishingzi mumkin.")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/dovip")
	user_id = id[1].replace(" ", "")
	inlimit  = 53687091200
	uploadlimit(int(user_id),53687091200)
	usertype(int(user_id),"VIP⚡")
	addpre(int(user_id))
	await update.message.edit("Ushbu user VIP⚡ tarifiga ulandi 50GB")
	await bot.send_message(user_id,"Ta'rifingiz VIP⚡ ga ko'tarildi /tarif buyrug'i orqali ko'rishingzi mumkin.")
