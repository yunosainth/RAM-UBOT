from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.nyanyi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**POTONG**")
    await typew.edit("**BEBEK ANGSA**")
    sleep(1)
    await typew.edit("**MASAK DI**")
    await typew.edit("**KUALIIIII**")
    sleep(2)
    await typew.edit("**DEKET UDAH LAMA**")
    await typew.edit("TAPI BELOM PASTIIII**")
    sleep(2)
    await typew.edit("**SORONG KE KIRIII**")
    await typew.edit("**SORONG KE KANANN**")
    sleep(2)
    await typew.edit("**LALALALA**")
    await typew.edit("**LALALALA TAIIIII**")
    sleep(2)
    await typew.edit("**MENULIS TUGAS DI ATAS KERTAS**")
    await typew.edit("**SELESAI ITU KU MASUKAN TAS**")
    sleep(2)
    await typew.edit("**AKU KIRA AKU PRIORITAS**")
    await typew.edit("**TERNYATA ADA YANG LEBIH PANTAS**")
    sleep(2)
    await typew.edit("**MUKA LU JELEK**")
    await typew.edit("**GK USAH SOK GHOSTING ORANG**")
    sleep(3)
    await typew.edit("**XIXIXIXIXI**")

# Create by myself @localheart

CMD_HELP.update({
    "dhanbot":
    "`.dhanbot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.nyanyi`\
    \nUsage: misi."
})
