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


@register(outgoing=True, pattern='^.kel(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Egin**")
    await typew.edit("**BUNDA TAYANG**")
    sleep(1)
    await typew.edit("**Kia**")
    await typew.edit("**TUKANG NGAMBEK**")
    sleep(2)
    await typew.edit("**Rama**")
    await typew.edit("GANTENG**")
    sleep(2)
    await typew.edit("**Yaya**")
    await typew.edit("**SI LEMOT**")
    sleep(2)
    await typew.edit("**Bingung**")
    await typew.edit("**PAKE BANGET**")
    sleep(2)
    await typew.edit("**Pokonya**")
    await typew.edit("**RAMA IMUT**")
    sleep(2)
    await typew.edit("**Bingung lagi**")
    await typew.edit("**BINGUNG BANGETT**")
    sleep(2)
    await typew.edit("**Udah ah**")
    await typew.edit("**BYE SAJA**")
    sleep(3)
    await typew.edit("**CUMA RAMA YANG WARAS!**")

# Create by myself @localheart

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.kel`\
    \nUsage: misi."
})
