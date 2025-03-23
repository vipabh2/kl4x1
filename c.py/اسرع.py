import asyncio, time
from telethon import event
from faker import Faker
res = {}
a = 0
players = {}
answer = None
is_on = False
start_time = None
fake = Faker("ar_AA")
@ABH.on(events.NewMessage(pattern=r"(?i)^(?:اسرع|/faster)$"))  
async def start_s(event):
    global is_on, players
    is_on = True
    players.clear()
    uid = event.sender_id
    sender = await event.get_sender()
    name = sender.first_name
    if uid not in players:
         players[uid] = {"username": name}
         res[name] = {"name": name, "score": 0}
         await event.reply("اهلاً ضفتك للعبة , للانضمام ارسل `انا` للبدء `تم` \n**ENJOY BABY✌**")
@ABH.on(events.NewMessage(pattern="(?i)انا$"))
async def sign_in(event):
    if is_on:
        uid = event.sender_id
        sender = await event.get_sender()
        name = sender.first_name
        if uid not in players:
            players[uid] = {"username": name}
            res[name] = {"name": name, "score": 0}
            await event.reply('سجلتك باللعبة، لا ترسل مجددًا!')
        else:
            await event.reply("عزيزي الصديق، سجلتك والله!")
@ABH.on(events.NewMessage(pattern="(?i)الاعبين$"))
async def players_show(event):
    global is_on
    if is_on and players:
        player_list = "\n".join([f"{pid} - {info['username']}" for pid, info in players.items()])
        await event.reply(f"📜 قائمة اللاعبين:\n{player_list}")
        is_on = True
    else:
        await event.reply('ماكو لاعبين 🙃')
@ABH.on(events.NewMessage(pattern="(?i)تم$"))
async def start_f(event):
    global answer, is_on, start_time
    if is_on:
        await event.reply('تم بدء اللعبة، انتظر ثواني...')
        await asyncio.sleep(2)
        for _ in range(5):
            word = fake.word()
            answer = (word)
            await event.respond(f'✍ اكتب ⤶ {answer}')
            start_time = time.time()
            await asyncio.sleep(10)
        points_list = "\n".join([f"{info['name']} - {info['score']} نقطة" for info in res.values()])
        await event.reply(f"**ترتيب اللاعبين بالنقاط**\n{points_list}")
@ABH.on(events.NewMessage)
async def check(event):
    global is_on, start_time, answer, a
    if not is_on or start_time is None:
        return
    elapsed_time = time.time() - start_time
    seconds = int(elapsed_time)
    milliseconds = int((elapsed_time - seconds) * 1000)
    isabh = event.text.strip()
    wid = event.sender_id
    if answer and isabh.lower() == answer.lower() and wid in players:
        username = players[wid]["username"]
        if username not in res:
            res[username] = {"name": username, "score": 0}
        res[username]["score"] += 1
        await event.reply(f'إجابة صحيحة! أحسنت الوقت المستغرق: {seconds} ثانية و {milliseconds} مللي ثانية.')
        answer = None
        start_time = None
    elif elapsed_time >= 10:
        is_on = False
        answer = None
        start_time = None
        if a == 5:
            is_on = False
            points_list = "\n".join([f"{pid} -> {info['score']} نقطة" for pid, info in res.items()])
            await event.reply(f"**ترتيب اللاعبين بالنقاط**\n{points_list}")
