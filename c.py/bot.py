from telethon import TelegramClient, events
from config import API_ID, API_HASH, BOT_TOKEN  # استيراد الإعدادات من config.py
from commands import start_command, help_command, custom_command  # استيراد الأوامر من commands.py

# إعداد البوت باستخدام API_ID و API_HASH و BOT_TOKEN
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# ربط الأوامر المختلفة
@client.on(events.NewMessage(pattern='/start'))  # عند استقبال الأمر /start
async def start(event):
    await start_command(event)  # تنفيذ الأمر المناسب من commands.py

@client.on(events.NewMessage(pattern='/help'))  # عند استقبال الأمر /help
async def help(event):
    await help_command(event)  # تنفيذ الأمر المناسب من commands.py

@client.on(events.NewMessage(pattern='/custom'))  # عند استقبال الأمر /custom
async def custom(event):
    await custom_command(event)  # تنفيذ الأمر المناسب من commands.py

# بدء البوت والعمل على استقبال الرسائل والأوامر
client.run_until_disconnected()
