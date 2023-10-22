from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['/thumbnail']))
async def viewthumb(client,message):
		print(message.chat.id)
		thumb = find(int(message.chat.id))[0]
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("**Sizda hech qanday pechat rasm yo'q!!!\n\nPechat rasm qo'yish uchun shunchaki rasm yuboring.**")
	
	
@Client.on_message(filters.private & filters.command(['/del_thumbnail']))
async def removethumb(client,message):
	delthumb(int(message.chat.id))
	await message.reply_text("**Maxsus pechat rasm muvaffaqiyatli oʻchirildi✅**")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
	file_id = str(message.photo.file_id)
	addthumb(message.chat.id , file_id)
	await message.reply_text("**Maxsus pechat rasm muvaffaqiyatli saqlandi✅**")
