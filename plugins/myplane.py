import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from helper.database import  find_one,used_limit 
from helper.database import daily as daily_ 
import datetime
from datetime import timedelta, date ,datetime
from datetime import date as date_
from helper.progress import humanbytes


@Client.on_message(filters.private & filters.command(["tarif"]))
async def start(client,message):
	used_ = find_one(message.from_user.id)	
	daily = used_["daily"]
	expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
	if expi != 0:
	     today = date_.today()
	     pattern = '%Y-%m-%d'
	     epcho = int(time.mktime(time.strptime(str(today), pattern)))
	     daily_(message.from_user.id,epcho)
	     used_limit(message.from_user.id,0)
	_newus = find_one(message.from_user.id)
	used = _newus["used_limit"]
	limit = _newus["uploadlimit"]
	remain = int(limit)- int(used)
	user =  _newus["usertype"]
	ends = _newus["prexdate"]
	if ends == None:
	    text = f"Foydalanuvchi ID: ```{message.from_user.id}```\nTarif: {user}\nKunlik yuklash limiti: {humanbytes(limit)}\nBugun foydalanilgan: {humanbytes(used)}\nQolgan hajm: {humanbytes(remain)}"
	else:
	    normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
	    text = f"Foydalanuvchi ID: ```{message.from_user.id}```\nTa'rif : {user}\nKunlik yuklash limiti: {humanbytes(limit)}\nBugun foydalanilgan: {humanbytes(used)}\nQolgan hajm: {humanbytes(remain)}\n\n```Sizning ta'rifingiz tugaydi: {normal_date} da"
	    
	if user == "Bepul":
	    await message.reply(text,quote = True,reply_markup = InlineKeyboardMarkup([[       			InlineKeyboardButton("Bekor qilish ✖️ ",callback_data = "cancel") ]]))
	else:
	    await message.reply(text,quote=True)
	    
