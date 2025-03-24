
mohmurl = random.randint(119, 138)
basimurl = random.randint(50, 118)
musurl = random.randint(139, 154)
nurl = random.randint(164, 170)
furl = random.randint(171, 174)
async def send_audio_from_list(event, url_list):
    rl = random.choice(url_list)
    audio_url = f"https://t.me/sossosic/{rl}"
    await event.reply(file=audio_url)
banned_url = [
    9,  25, 94, 131, 175,
    26, 40, 110, 136, 194,
    71, 72, 111, 142, 212,
    77, 79, 114, 148, 230,
    80, 81, 115, 150, 245,
    82, 93, 121, 152, 254,
    273
]
latmiyat_range = range(50, 274)
async def send_random_latmia(event):
    try:
        chosen = random.choice(list(latmiyat_range))
        if chosen in banned_url:
            return await send_random_latmia(event)
        latmia_url = f"https://t.me/x04ou/{chosen}"
        await event.reply(file=latmia_url)
    except Exception as e:
        await event.reply(f"اعد المحاولة مره اخرى")
@ABH.on(events.NewMessage(pattern=r"^(لطمية|لطميه)$"))
async def handle_latmia_command(event):
    await send_random_latmia(event)
