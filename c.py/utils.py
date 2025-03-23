async def send_welcome_message(client, user_id):
    await client.send_message(user_id, 'مرحباً بك في البوت!')
