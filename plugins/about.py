import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["status"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Umumiy foydalanuvchilar: {total_user()}ta\nUmumiy qayta nomlangan fayllar: {total_rename}ta\nUmumiy qayta nomlangan fayllar hajmi: {humanbytes(int(total_size))} ",quote=True)
