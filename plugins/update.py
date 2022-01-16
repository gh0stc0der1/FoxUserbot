from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list, settings
import os

prefix = settings['prefix']

@Client.on_message(filters.command('update', prefixes=prefix) & filters.me)
async def update(client: Client, message: Message):
  try:
    await message.edit('**Обновление...**')
    os.system('git pull')
    await message.edit('**Юзербот успешно обновлен.**')
  except:
    await message.edit("**Произошла ошибка...**")
    
module_list['Update'] = f'{prefix}update'
file_list['Update'] = 'update.py'
