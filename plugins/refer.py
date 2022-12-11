from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["referal"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Shaxsiy havolani tarqatish" ,url=f"https://t.me/share/url?url=https://t.me/Renamere_Bot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Do'stni chaqiring va har bir do'stingiz uchun 100Mb qo'shimcha joy olasiz!\nSizning havolangiz: https://t.me/azik_renamerbot?start={message.from_user.id}\n\n\n<b>Do'stingiz botga start bosib kanalga a'zo bo'lishi kerak kanaldan chiqsa yoki botni bloklasa sizdan joy olib tashlanadi!!!</b>",reply_to_message_id = message.id,reply_markup=reply_markup,)
