from telethon import event
import random
choices = {"rock": "🪨حجره", "paper": "📜ورقة", "cuter": "✂️مقص"}
active_games = {}
@ABH.on(events.NewMessage(pattern="حجرة|/rock"))
async def start(event):
    global n
    active_games[event.chat_id] = event.sender_id
    n = event.sender.first_name
    buttons = [
        [Button.inline("🪨", b"rock"), Button.inline("✂️", b"cuter"), Button.inline("📜", b"paper")]
    ]
    await event.respond("اختر أحد الاختيارات 🌚", buttons=buttons)
async def process_choice(event, user_choice):
    game_owner = active_games.get(event.chat_id)
    if game_owner != event.sender_id:
        await event.answer("من تدخل في ما لا يعنيه لقي كلام لا يرضيه 🙄", alert=True)
        return  
    bot_choice_key = random.choice(list(choices.keys()))
    bot_choice = choices[bot_choice_key]  
    user_id = event.sender_id
    result = "🤝تعادل" if user_choice == bot_choice_key else "🎉فزت" if (
        (user_choice == "rock" and bot_choice_key == "cuter") or 
        (user_choice == "paper" and bot_choice_key == "rock") or 
        (user_choice == "cuter" and bot_choice_key == "paper")
    ) else "😢خسرت"
