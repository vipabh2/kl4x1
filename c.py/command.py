async def start_command(event):
    await event.reply('مرحباً! كيف يمكنني مساعدتك؟')

async def help_command(event):
    help_text = """
    الأوامر المتاحة:
    /start - بدء التفاعل مع البوت
    /help - عرض هذا النص
    /custom - أمر مخصص
    """
    await event.reply(help_text)

async def custom_command(event):
    await event.reply('لقد قمت بإرسال أمر مخصص!')
