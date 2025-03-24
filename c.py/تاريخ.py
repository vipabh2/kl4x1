from telethon import event
from hijri_converter import Gregorian
@ABH.on(events.NewMessage(pattern='^/dates$'))
async def show_dates(event):
    btton = [[
        Button.inline("محرم", b"m"),
        Button.inline("رمضان", b"rm"),
        Button.inline("شعبان", b"sh"),
        Button.inline("رجب", b"r"),
        Button.inline("حدد تاريخ", b"set_date")
    ]]
    await event.respond("اختر الشهر المناسب أو حدد تاريخ خاص 👇", buttons=btton)
@ABH.on(events.CallbackQuery)
async def handle_callback(event):
    data = event.data.decode("utf-8")
    if data == "set_date":
        await event.edit("من فضلك أدخل التاريخ بصيغة YYYY-MM-DD مثال: 2025-06-15", buttons=None)
    elif data == "m":
        await count_m(event)
    elif data == "rm":
        await count_rm(event)
    elif data == "sh":
        await count_sh(event)
    elif data == "r":
        await count_r(event)
@ABH.on(events.NewMessage(pattern=r'^\d{4}-\d{2}-\d{2}$'))
async def set_user_date(event):
    user_id = event.sender_id
    date = event.text
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        save_date(user_id, date)
        await event.reply(f"تم حفظ التاريخ {date}. يمكنك الآن معرفة كم باقي.")
    except ValueError:
        await event.reply("التاريخ المدخل غير صالح، يرجى إدخاله بصيغة YYYY-MM-DD.")
@ABH.on(events.NewMessage(pattern='^كم باقي$'))
async def check_remaining_days(event):
    user_id = event.sender_id
    saved_date = get_saved_date(user_id)
    if saved_date:
        t = datetime.datetime.today()
        saved_date_obj = datetime.datetime.strptime(saved_date, "%Y-%m-%d").date()
        days_difference = (saved_date_obj - t.date()).days
        msg = f"باقي {days_difference} ايام" if days_difference >= 0 else f"التاريخ قد مضى منذ {abs(days_difference)} يوم"
        await event.reply(msg)
    else:
        await event.reply("لم تحدد تاريخًا بعد، يرجى تحديد تاريخ أولاً.")
async def count_r(event):
    await calculate_days(event, datetime.date(2025, 12, 22))
async def count_sh(event):
    await calculate_days(event, datetime.date(2026, 1, 20))
async def count_rm(event):
    await calculate_days(event, datetime.date(2025, 3, 1))
async def count_m(event):
    await calculate_days(event, datetime.date(2025, 6, 26))
async def calculate_days(event, target_date):
    t = datetime.datetime.today()
    days_difference = (target_date - t.date()).days
    msg = f"باقي {days_difference} ايام" if days_difference >= 0 else "الشهر قد بدأ \n يا مطوري حدث الكود @k_4x1"
    await event.edit(msg)
@ABH.on(events.NewMessage(pattern='^تاريخ$'))
async def start_handler(event):
    t = datetime.datetime.now().date()
    hd = Gregorian(t.year, t.month, t.day).to_hijri()
    hd_str = f"{hd.day} {hd.month_name('ar')} {hd.year} هـ"    
    await event.reply(f" الهجري: \n {hd_str} \n الميلادي: \n {t}")
