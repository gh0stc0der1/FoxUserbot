from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, settings
import asyncio

prefix = settings['prefix']

@Client.on_message(filters.command('help', prefixes=prefix) & filters.me)
async def help(client: Client, message: Message):
    list = []
    for k, v in module_list.items():
        list.append(f'**• {k}**: ```{v}```')
    a = " "
    for i in list:
        a = a.lstrip() + f'{i}\n'
    await message.edit(f"""
**{len(module_list)} available modules.**

{a}""")

module_list['Help'] = f'{prefix}help'