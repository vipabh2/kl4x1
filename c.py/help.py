from telethon import events

async def help_handler(event):
    if event.raw_text == '/help':
        help_text = """
        الأوامر المتاحة:
        /start - بدء التفاعل مع البوت
        /help - عرض هذا النص
        """
        await event.reply(help_text)
