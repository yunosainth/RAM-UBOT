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


@register(outgoing=True, pattern='^.teman(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ectod**")
    await typew.edit("**Ecca Ngentod**")
    sleep(1)
    await typew.edit("**Simtod**")
    await typew.edit("**Sima Ngentod**")
    sleep(2)
    await typew.edit("**ochtod**")
    await typew.edit("**Ocha Ngentod**")
    sleep(2)
    await typew.edit("**Kentod**")
    await typew.edit("**Ken Ngentod**")
    sleep(2)
    await typew.edit("**Jetod**")
    await typew.edit("**Jeje Ngentod**")
    sleep(2)
    await typew.edit("**Softod**")
    await typew.edit("**Sofi Ngentod**")
    sleep(2)
    await typew.edit("**Loptod**")
    await typew.edit("**Lop ngentod**")
    sleep(2)
    await typew.edit("**Yogtod**")
    await typew.edit("**Yoga Ngentod**")
    sleep(3)
    await typew.edit("**CUMA RAMA YANG IMUT!**")

# Create by myself @localheart

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.teman`\
    \nUsage: misi."
})
