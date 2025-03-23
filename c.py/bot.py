from telethon import TelegramClient, events
from config import api_id, api_hash, bot_token
from start import start_handler  # استيراد أمر start
from help import help_handler    # استيراد أمر help

def main():
    # تهيئة البوت
    client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
    
    # ربط الأوامر بالبوت
    client.add_event_handler(start_handler)
    client.add_event_handler(help_handler)
    
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
