from telethon import TelegramClient, events
from config import api_id, api_hash, bot_token
from start import start_handler
from help import help_handler
from الردود import reply
async def main():
    # تهيئة البوت
    ABH = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
    
    await load_plugins("c")
    ABH.add_event_handler(start_handler)
    ABH.add_event_handler(help_handler)
    ABH.add_event_handler(reply)
    ABH.run_until_disconnected()

if __name__ == '__main__':
    main()
