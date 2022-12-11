import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.progress import humanbytes

from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"")
import datetime
from datetime import date as date_
STRING = os.environ.get("STRING","")
log_channel = int(os.environ.get("LOG_CHANNEL",""))
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]

#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "Good morning."
elif 12 <= currentTime.hour < 12:
	wish = 'Good afternoon.'
else:
	wish = 'Good evening.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	try:
	    id = message.text.split(' ')[1]
	except:
	    await message.reply_text(text =f"""
	Salom {message.from_user.first_name }
Men Telegram fayllarni nomini o'zgartirib va videoga pechat qo'yib beradigan botman! 
Menga Fayl/Video/Audio yuboring va uni qayta nomlang✍️
	
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("Press Chiqarish 💪" ,url="https://t.me/+TaweX_GKt4VmZjky") ], 
	[InlineKeyboardButton("Muzikalar 🎶", url="https://t.me/+Ona2jSz88bs0MmUy") ]  ]))
	    return
	if id:
	    if old == True:
	        try:
	            await client.send_message(id,"Your Frind Alredy Using Our Bot")
	            await message.reply_text(text =f"""
	Salom {message.from_user.first_name }
Men Telegram fayllarni nomini o'zgartirib va videoga pechat qo'yib beradigan botman! 
Menga Fayl/Video/Audio yuboring va uni qayta nomlang✍️
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("Press Chiqarish 💪" ,url="https://t.me/+TaweX_GKt4VmZjky") ], 
	[InlineKeyboardButton("Muzikalar 🎶", url="https://t.me/+Ona2jSz88bs0MmUy") ]  ]))
	        except:
	             return
	    else:
	         await client.send_message(id,"Tabrik! Siz 100MB yutib oldingiz.")
	         _user_= find_one(int(id))
	         limit = _user_["uploadlimit"]
	         new_limit = limit + 104857600
	         uploadlimit(int(id),new_limit)
	         await message.reply_text(text =f"""
	Salom {message.from_user.first_name }
Men Telegram fayllarni nomini o'zgartirib va videoga pechat qo'yib beradigan botman! 
Menga Fayl/Video/Audio yuboring va uni qayta nomlang✍️
	
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("Press Chiqarish 💪" ,url="https://t.me/+TaweX_GKt4VmZjky") ], 
	[InlineKeyboardButton("Muzikalar 🎶", url="https://t.me/+Ona2jSz88bs0MmUy") ]  ]))
	         



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("Mendan foydalanish uchun @Renamere_bot_adminlar_uchun guruhiga obuna boʻling!!!\n\nGuruhdan chiqsangiz foydalanishdan banlanasiz!",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Guruhga ulanish" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       
       bot_data = find_one(int(botid))
       prrename = bot_data['total_rename']
       prsize = bot_data['total_size']
       user_deta = find_one(user_id)
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       except:
           await message.reply_text("Botni ishlatish uchun qayta /start tugmasini bosing.")
           return
           
           
       c_time = time.time()
       
       if buy_date==None:
           LIMIT = 100
       else:
           LIMIT = 10
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"```Kechirasiz men faqat SIZ uchun emasman.\nFlood nazorati faol shuning uchun kuting {ltime}```",reply_to_message_id = message.id)
       else:
       		# Forward a single message
       		await client.forward_messages(log_channel, message.from_user.id, message.id)
       		await client.send_message(log_channel,f"User Id :- {user_id}")       		
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 15360000000
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)			     		
       		remain = 2200000000
       		if remain < int(file.file_size):
       		    await message.reply_text(f"Kechirasiz! Men {humanbytes(limit)}dan katta fayllarni sizga yubora olmayman.\nAniqlangan fayl hajmi {humanbytes(file.file_size)}\nKunlik foydalanilgan limit {humanbytes(used)}",)
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f" Siz {humanbytes(limit)} dan ko'p yuklay olmaysiz.\nKunlik foydalanilgan limit {humanbytes(used)} ",)
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__Ushbu faylni nima qilmoqchisiz?__\n**Fayl Nomi**: {filename}\n**Fayl Hajmi**: {humanize.naturalsize(file.file_size)}\n**DC ID**: {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Qayta nomlash 📝",callback_data = "rename"),InlineKeyboardButton("Bekor qilish ✖️",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            await message.reply_text(f"Nimadir xato ketdi! Admin bilan bog'laning!!! ",quote=True) #Sizning ta'rifingiz {buy_date}da tugaydi!
       		            return
       		    else:
       		          	await message.reply_text("2GB dan katta faylni yuklay olmayman ")
       		          	return
       		else:
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""__Ushbu faylni nima qilmoqchisiz?__\n**Fayl Nomi**: {filename}\n**Fayl Hajmi**: {filesize}\n**DC ID**: {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("Qayta nomlash 📝",callback_data = "rename"),
       		InlineKeyboardButton("Bekor qilish ✖️",callback_data = "cancel")  ]]))
       		
