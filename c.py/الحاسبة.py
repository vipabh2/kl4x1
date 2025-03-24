from telethon import events

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
@ABH.on(events.NewMessage(pattern=r'احسب (\d+)\s*([\+\-\*/÷])\s*(\d+)'))
async def calc(event):
    try:
        match = event.pattern_match 
        a = int(match.group(1))
        mark = match.group(2)
        b = int(match.group(3))
        if mark in operations:
            result = operations[mark](a, b)
            await event.respond(f"النتيجة `{result}`", reply_to=event.message.id)
        else:
            await event.respond("عملية غير مدعومة!", reply_to=event.message.id)
    except ZeroDivisionError:
        await event.respond("خطأ: لا يمكن القسمة على صفر!", reply_to=event.message.id)
        await event.reply(abh)    
