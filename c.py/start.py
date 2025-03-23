from telethon import events

async def start_handler(event):
    if event.raw_text == '/start':
        await event.reply('مرحباً! كيف يمكنني مساعدتك؟')
