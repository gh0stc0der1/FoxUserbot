from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list, settings

prefix = settings['prefix']

@Client.on_message(filters.command('setprefix', prefixes=prefix))
async def setprefix(client: Client, message: Message):
	new_prefix = message.command[1]
	settings['prefix'] = new_prefix
	await message.edit(f"**Prefix changed.**\n**Current prefix** ```{new_prefix}```")

module_list['SetPrefix[BETA]'] = '!setprefix [new prefix]'
file_list['SetPrefix[BETA]'] = 'setprefix.py'
    
