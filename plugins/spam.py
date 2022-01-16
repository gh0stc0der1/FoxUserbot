from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list, settings
import asyncio

prefix = settings['prefix']

@Client.on_message(filters.command('spam', prefixes=prefix) & filters.me)
async def spam(client, message):
    spam_params = message.text
    spam_params = spam_params.split()
    count = spam_params[0]
    text = spam_params[1:]
    text = ' '.join(text)
    await message.edit(f"""**Spam started.
Number of messages: {count}. 
Spam Text: {text}.**""")
    for i in range(int(count)):
        await message.reply(text)
    
module_list['Spam'] = f'{prefix}spam [number of messages] [text]'
file_list['Spam'] = 'spam.py'