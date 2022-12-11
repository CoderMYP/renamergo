"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """Bepul Foydalanuvchi ta'rifi
	 Kunlik fayllarni qayta nomlash limiti: 300MB
	 Narxi: Bepul
 
	 Lite✨ 
 	 Kunlik fayllarni qayta nomlash limiti: 15GB
 	 4GBgacha fayllarni qayta nomlash mumkin!
 	 Narxi: Haftasiga 0.75💲 yoki Oyiga 3💲
 
	 VIP⚡
	 Kunlik fayllarni qayta nomlash limiti: 50GB
	 4GBgacha fayllarni qayta nomlash mumkin!
 	 Narxi: Haftasiga 1.5💲 yoki Oyiga 5💲
 
	 To'lov usullari: HUMO💳  | UZCARD💳 |  VISA💳
 
 	 Ta'rif sotib olmoqchi bo'lsangiz admin bilan bog'laning.
	 4Gbgacha faylni yuklash uchun Telegram Premium va undan tashqari bot ishlashi uchun server kerak. Bizni to'g'ri tushundingiz degan umiddamiz🙂"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Administrator",url = "https://t.me/azik_developer")], 
        		        [InlineKeyboardButton("Bekor qilish",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """Bepul Foydalanuvchi ta'rifi
	 Kunlik fayllarni qayta nomlash limiti: 300MB
	 Narxi: Bepul
 
	 Lite✨ 
 	 Kunlik fayllarni qayta nomlash limiti: 15GB
 	 4GBgacha fayllarni qayta nomlash mumkin!
 	 Narxi: Haftasiga 0.75💲 yoki Oyiga 3💲
 
	 VIP⚡
	 Kunlik fayllarni qayta nomlash limiti: 50GB
	 4GBgacha fayllarni qayta nomlash mumkin!
 	 Narxi: Haftasiga 1.5💲 yoki Oyiga 5💲
 
	 To'lov usullari: HUMO💳  | UZCARD💳 |  VISA💳
 
 	 Ta'rif sotib olmoqchi bo'lsangiz admin bilan bog'laning.
	 4Gbgacha faylni yuklash uchun Telegram Premium va undan tashqari bot ishlashi uchun server kerak. Bizni to'g'ri tushundingiz degan umiddamiz🙂"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Administrator",url = "https://t.me/azik_developer")], 
        			[InlineKeyboardButton("Payme💰",url = "https://payme.uz/632a1e4dcad1c751639f6e8a"),
        			InlineKeyboardButton("VISA💳",url = "https://t.me/azik_developer")],[InlineKeyboardButton("Bekor qilish",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
