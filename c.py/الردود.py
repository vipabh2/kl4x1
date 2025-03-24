from telethon import event
import google.generativeai as genai
GEMINI = "AIzaSyA5pzOpKVcMGm6Aek82KoB3Pk94dYg3LX4"
genai.configure(api_key=GEMINI)
model = genai.GenerativeModel("gemini-1.5-flash")
@ABH.on(events.NewMessage(pattern=r'(?i)مخفي'))
async def ai(event):
    if event.text.strip() == "مخفي طكة زيج":
        return
    if (event.is_reply or len(event.text.strip().split()) > 1) and not event.out:
        try:
            if event.is_reply:
                replied_message = await event.get_reply_message()
                user_input = replied_message.text.strip()
            else:
                user_input = event.text.strip().split(" ", 1)[1]
            ABH_response = model.generate_content(user_input)
            await event.reply(f"**{ABH_response.text}**")
        except Exception as e:
            await event.reply(f"صار خطأ: {e}")
import random
from telethon import events
abh = [
    "ها",
    "تفظل",
    "كول",
    "اسمعك",
    "شرايد",
    "خلصني",
    "https://t.me/VIPABH/1214",
    "https://t.me/VIPABH/1215"
]
@ABH.on(events.NewMessage(pattern=r'^مخفي$'))
async def reply(event):
    if event.is_reply:
        return
    vipabh = random.choice(abh)
    if vipabh.startswith("http"):
        await event.reply(file=vipabh)
    else:
        await event.reply(vipabh)
@ABH.on(events.NewMessage(pattern='ابن هاشم'))
async def reply_abh(event):
    if event.chat_id == -1001968219024:
        rl = random.randint(1222, 1241)
        url = f"https://t.me/VIPABH/{rl}"
        caption = "أبن هاشم (رض) مرات متواضع ،🌚 @K_4x1"
        button = [Button.url(text="الking", url="https://t.me/K_4x1")]
        await event.client.send_file(event.chat_id, url, caption=caption, reply_to=event.message.id, buttons=button)
    else:
        return
@ABH.on(events.NewMessage(pattern='زهراء'))
async def reply_abh(event):
    if event.chat_id == -1001968219024:
        url = "https://t.me/VIPABH/1220"  
        caption = "@klix_78 ( لَقَدْ كَفَرَ الّذِينَ قَالُوا إنَّ الله هُو المَسِيحُ ابْنُ مَرْيَم)." 
        await event.client.send_file(event.chat_id, url, caption=caption, reply_to=event.message.id)    
    else: 
        return
@ABH.on(events.NewMessage(pattern='امريجا|الامريكي'))
async def reply_abh(event):
    if event.chat_id == -1001968219024:
        url = "https://files.catbox.moe/p9e75j.mp4"  
        caption = "@l_h_2" 
        await event.client.send_file(event.chat_id, url, caption=caption, reply_to=event.message.id)    
    else: 
        return
@ABH.on(events.NewMessage(pattern='امير'))
async def reply_abh(event):
    if event.chat_id == -1001968219024:
        ur = ["https://files.catbox.moe/k44qq6.mp4",
               'https://t.me/KQK4Q/23',
               'https://t.me/KQK4Q/22'
               ]
        url = random.choice(ur)
        caption = "@xcxx1x" 
        await event.client.send_file(event.chat_id, url, caption=caption, reply_to=event.message.id)    
    else: 
        return
@ABH.on(events.NewMessage(pattern='عبدالله|عبود'))
async def reply_abh(event):
    if event.chat_id == -1001968219024:
        url = "https://files.catbox.moe/qohqtp.MP4"  
        caption = "@UU77QQ" 
        await event.client.send_file(event.chat_id, url, caption=caption, reply_to=event.message.id)    
    else: 
        return
@ABH.on(events.NewMessage(pattern='مقتدى'))
async def reply_abh(event):
    if event.chat_id == -1001968219024:
        await event.reply('@hiz8s')
    else: 
        return
@ABH.on(events.NewMessage(pattern='يزيد'))
async def reply_abh(event):
    if event.chat_id == -1001968219024:
        await event.reply('@l7QQI')
    else: 
        return
auto = [
        "ع س",
        "عليكم السلام",
        "عليكم السلام والرحمة والاكرام",
        "عليكم سلام الله"
        ]
@ABH.on(events.NewMessage(pattern=r'^(سلام عليكم|السلام عليكم)$'))
async def reply_abh(event):
        abh = random.choice(auto)
