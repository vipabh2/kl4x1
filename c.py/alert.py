from telethon import events
import re, json
GROUPS_FILE = "dialogs.json"
TARGET_CHAT_ID = 1910015590
def load_dialogs():
    if os.path.exists(GROUPS_FILE):
        with open(GROUPS_FILE, "r") as f:
            return set(json.load(f))
    return set()
def save_dialogs():
    with open(GROUPS_FILE, "w") as f:
        json.dump(list(dialog_ids), f)
dialog_ids = load_dialogs()
async def send_message_to_target_chat(message):
    try:
        await ABH.send_message(TARGET_CHAT_ID, message)
    except Exception as e:
        # print(f"فشل إرسال الرسالة {e}")
@ABH.on(events.NewMessage)
async def update_dialogs(event):
    global dialog_ids
    chat = await event.get_chat()
    if chat.id not in dialog_ids:
        try:
            dialog_ids.add(chat.id)
            save_dialogs()
            chat_name = chat.title if hasattr(chat, 'title') else chat.first_name
            return
        except Exception as e:
            await send_message_to_target_chat(f"فشل إضافة المحادثة: {chat.id} - {e}")
@ABH.on(events.NewMessage(pattern="/alert"))
async def send_alert(event):
    if event.sender_id != TARGET_CHAT_ID:
        return
    message_text = None
    if event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()
        message_text = replied_msg.text
    else:
        command_parts = event.raw_text.split(maxsplit=1)
        if len(command_parts) > 1:
            message_text = command_parts[1]
    if not message_text:
        await event.reply("يرجى الرد على رسالة أو كتابة نص بعد `/alert`.")
        return
    await event.reply(f"🚀 جاري إرسال التنبيه إلى {len(dialog_ids)} محادثة...")
    for dialog_id in dialog_ids:
        try:
            await ABH.send_message(dialog_id, f"**{message_text}**")
            await send_message_to_target_chat(f"✅ تم الإرسال إلى: {dialog_id}")
        except Exception as e:
            await send_message_to_target_chat(f"❌ فشل الإرسال إلى {dialog_id}: {e}")
    await event.reply("✅ تم إرسال التنبيه لجميع المحادثات!")
