from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, settings
import os

prefix = settings['prefix']

@Client.on_message(filters.command('loadmod', prefixes=prefix) & filters.me)
async def load_module(client: Client, message: Message):
	if not message.reply_to_message:
		await message.edit("<b>Нету реплай!</b>")
	else:
		if not message.reply_to_message.document:
			await message.edit("<b>Это не файл!</b>")
		else:
			await client.download_media(message.reply_to_message.document,file_name="plugins")
			await message.edit("<b>Модуль загружен!</b>")
			os.execvp("python3",["python3","main.py",],)
    
module_list['Loadmod'] = f'{prefix}loadmod REPLY message'
