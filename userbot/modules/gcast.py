# frm Ultroid
# port by Koala @manusiarakitann
# @LordUserbot_Group
# Rama Ganteng mks sm sm

from userbot.events import register
from userbot import CMD_HELP, bot
# Rama Ganteng mks sm sm


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Teks nya mana tolol!!`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`Sedang Mengirim Pesan Secara Global... ⭐`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")

# Rama Ganteng mks sm sm
CMD_HELP.update(
    {
        "gcast": "`.gcast <pesan>`\
    \nPenjelasan: Global Broadcast mengirim pesan ke Seluruh Grup yang kamu Masuki."
    })
