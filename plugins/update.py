from pyrogram import Client, filters
from plugins.help import module_list, file_list

@Client.on_message(filters.command('update', prefixes='!') & filters.me)
async def update(client, message):
  await message.edit('Обновление...')
  os.system('git pull')
  await message.edit('Юзербот успешно обновлен.')
  
module_list['Update'] = '!update'
file_list['Update'] = 'update.py'
