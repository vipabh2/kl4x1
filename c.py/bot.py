from telethon import TelegramClient, events
from config import api_id, api_hash, bot_token

def main():
    # تهيئة البوت
    client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    
    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.reply('مرحباً! كيف يمكنني مساعدتك؟')
    
    @client.on(events.NewMessage(pattern='/help'))
    async def help(event):
        help_text = """
        الأوامر المتاحة:
        /start - بدء التفاعل مع البوت
        /help - عرض هذا النص
        """
        await event.reply(help_text)
    
    # بدء البوت
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
