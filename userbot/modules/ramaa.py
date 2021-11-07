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


@register(outgoing=True, pattern='^.dhan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**RAMA**")
    await typew.edit("**PINTER**")
    sleep(1)
    await typew.edit("**KALIAN**")
    await typew.edit("**ENGGA**")
    sleep(2)
    await typew.edit("**RAMA IMUT**")
    await typew.edit("KALIAN ENGGA**")
    sleep(2)
    await typew.edit("**RAMA CERDAS**")
    await typew.edit("**KALIAN ENGGA**")
    sleep(2)
    await typew.edit("**RAMA WARAS**")
    await typew.edit("**KALIAN ENGGA**")
    sleep(2)
    await typew.edit("**TAPI RAMA**")
    await typew.edit("**SUKA DI GHOTING**")
    sleep(2)
    await typew.edit("**SAMA**")
    await typew.edit("**CEWE CEWE**")
    sleep(2)
    await typew.edit("**RAMA TERUS KAN? **")
    await typew.edit("**IYALAH KAN BOT RAMA**")
    sleep(3)
    await typew.edit("**XIXIXIXIXI**")

# Create by myself @localheart

CMD_HELP.update({
    "dhanbot":
    "`.dhanbot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.dhan`\
    \nUsage: misi."
})
