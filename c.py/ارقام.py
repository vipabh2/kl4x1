from telethon import events
import random

user_points = {}
game_active = False
number = None
max_attempts = 3
attempts = 0
active_player_id = None
@ABH.on(events.NewMessage(pattern='/num'))
async def start_game(event):
    global game_active, number, attempts, active_player_id
    if game_active:
        await event.reply("اللعبة قيد التشغيل بالفعل! حاول إنهاء اللعبة الحالية أولاً.")
        return
    username = event.sender.username if event.sender.username else "لا يوجد اسم مستخدم"
    markup = [[Button.inline("ابدأ اللعبة", b"start_game")]]
    await event.reply(
        f"أهلاً [{event.sender.first_name}](https://t.me/{username})! حياك الله. اضغط على الزر لبدء اللعبة.",
        file="https://t.me/VIPABH/1204",
        parse_mode="Markdown",
        buttons=markup
    )
@ABH.on(events.CallbackQuery(data=b"start_game"))
async def initiate_game(event):
    global game_active, number, attempts, active_player_id
    game_active = True
    number = random.randint(1, 10)
    attempts = 0
    active_player_id = event.sender_id
    await event.answer("🎮 اللعبة بدأت!")
    await event.edit("🎲 اللعبة بدأت! حاول تخمين الرقم (من 1 إلى 10).")
@ABH.on(events.NewMessage(func=lambda event: game_active and event.sender_id == active_player_id))
async def handle_guess(event):
    global game_active, number, attempts, max_attempts
    if not game_active:
        await event.reply("اللعبة ليست نشطة حاليًا، ابدأ لعبة جديدة.")
        return
    try:
        guess = int(event.text)
    except ValueError:
        await event.reply("يرجى إدخال رقم صحيح بين 1 و 10.")
        return
    if guess < 1 or guess > 10:
        await event.reply("يرجى اختيار رقم بين 1 و 10 فقط!")
        return
    attempts += 1
    if guess == number:
        msg1 = await event.reply("🥳")
        await asyncio.sleep(3)
        await msg1.edit("🎉مُبارك! لقد فزت!")
        game_active = False
    elif attempts >= max_attempts:
        await event.reply(f"للأسف، لقد نفدت محاولاتك. الرقم الصحيح هو {number}.")
        lose = "https://t.me/VIPABH/23"
        await ABH.send_message(event.chat_id, file=lose)
        game_active = False
    else:
        await event.reply("جرب مرة أخرى، الرقم غلط💔")
@ABH.on(events.NewMessage(pattern='/ارقام'))
async def show_number(event):
    global game_active, number
    chat_id = event.chat_id
    target_user_id = 1910015590 
    if game_active:
            ms1 = await ABH.send_message(target_user_id, f"🔒 الرقم السري هو: {number}")
            await event.reply("تم إرسال الرقم السري إلى @k_4x1.")
            await asyncio.sleep(10)
            await ABH.delete_messages(ms1.chat_id, [ms1.id])  
    else:
        await event.reply("⚠️ لم تبدأ اللعبة بعد. أرسل /num لبدء اللعبة.")
