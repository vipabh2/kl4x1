import os

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

# تأكد من أن القيم موجودة
if not all([api_id, api_hash, bot_token]):
    raise ValueError("One or more environment variables are missing. Please check your API_ID, API_HASH, and BOT_TOKEN.")
