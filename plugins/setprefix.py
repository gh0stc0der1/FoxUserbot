from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list, settings

main_settings = open('plugins/settings/main_settings.py')

prefix = settings['prefix']

@Client.on_message(filters.command('setprefix', prefixes=prefix))
async def setprefix(client: Client, message: Message):
	new_prefix = message.command[1]
	main_settings.write('"""Please, ignore this file.\n"""', '+w')
	main_settings.write(f"settings = {'prefix': '{new_prefix}'}", '+a')
	main_settings.write("module_list = {}", '+a')
	main_settings.write("requirements_list = []", '+a')
	main_settings.write("file_list = {}")
	await message.edit(f"**Prefix changed.**\n**Current prefix** ```{new_prefix}```")

module_list['SetPrefix[BETA]'] = '!setprefix [new prefix]'
file_list['SetPrefix[BETA]'] = 'setprefix.py'
    
