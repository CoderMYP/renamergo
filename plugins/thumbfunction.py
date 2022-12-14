from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

log_channel = int(os.environ.get("LOG_CHANNEL", ""))

@Client.on_message(filters.private & filters.command(['hozirgipechatrasm']))
async def viewthumb(client,message):
		print(message.chat.id)
		thumb = find(int(message.chat.id))[0]
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("**Sizda hech qanday pechat rasm yo'q!!!\n\nPechat rasm qo'yish uchun shunchaki rasm yuboring.**")
	
	
@Client.on_message(filters.private & filters.command(['rasmniochirish']))
async def removethumb(client,message):
	delthumb(int(message.chat.id))
	await message.reply_text("**Maxsus pechat rasm muvaffaqiyatli oʻchirildi✅**")
async def addthumbs(client,message):
	file_id = str(message.photo.file_id)
	addthumb(message.chat.id , file_id)
	await message.reply_text("**Maxsus pechat rasm muvaffaqiyatli saqlandi✅**")
       
