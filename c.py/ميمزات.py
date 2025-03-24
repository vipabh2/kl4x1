from telethon import event
import random
c = [
    "ههههههه",
    "😂",
    "يسعدلي مسائك😀"
]
@ABH.on(events.NewMessage(pattern='ميم|ميمز'))
async def start(event):
    global c
    rl = random.randint(2, 273)
    url = f"https://t.me/IUABH/{rl}"
    cap = random.choice(c)
    await ABH.send_file(event.chat_id, url, caption=f"{cap}", reply_to=event.id)
@ABH.on(events.NewMessage(pattern=r'^(مخفي طكة زيج|زيج)$'))
async def reply_abh(event):
    replied_message = await event.get_reply_message()
    if replied_message and replied_message.sender_id == 1910015590:
        await event.reply("عزيزي الغبي ... \n تريدني اعفط للمطور شكلت لربك؟")
        return
    if replied_message:
        await event.client.send_file(replied_message.peer_id, "https://t.me/VIPABH/1171", reply_to=replied_message.id)
    else:
        await event.reply("عزيزي الفاهي ... \n الامر يعمل بالرد , اذا عدتها وما سويت رد اعفطلك")
@ABH.on(events.NewMessage(pattern=r'^(ميعرف|مايعرف)$'))
async def reply_abh(event):
    replied_message = await event.get_reply_message()
    if replied_message:
        await event.client.send_file(replied_message.peer_id, "https://t.me/recoursec/3", reply_to=replied_message)
    else:
        await event.reply(file="https://t.me/recoursec/3", reply_to=event.message.id)
@ABH.on(events.NewMessage(pattern=r'^(صباح النور|صباح الخير)$'))
async def reply_abh(event):
    replied_message = await event.get_reply_message()
    if replied_message:
        await event.client.send_file(replied_message.peer_id, "https://t.me/recoursec/4", reply_to=replied_message)
    else:
        await event.reply(file="https://t.me/recoursec/4", reply_to=event.message.id)
@ABH.on(events.NewMessage(pattern=r'^(لا تتمادة|لا تتماده|تتماده)$'))
async def reply_abh(event):
    replied_message = await event.get_reply_message()
    if replied_message:
        await event.client.send_file(replied_message.peer_id, "https://t.me/recoursec/5", reply_to=replied_message)
    else:
        await event.reply(file="https://t.me/recoursec/5", reply_to=event.message.id)
@ABH.on(events.NewMessage(pattern=r'^(هاي بعد|اي هاي)$'))
async def reply_abh(event):
    replied_message = await event.get_reply_message()
    if replied_message:
        await event.client.send_file(replied_message.peer_id, "https://t.me/recoursec/6", reply_to=replied_message)
    else:
        await event.reply(file="https://t.me/recoursec/6", reply_to=event.message.id)
