""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/gksukaribett)"
        "\n[Repo](https://github.com/ramadhan73/DHAN-UBOT)"
        "\n[Channel](https://t.me/calonpenyanyi)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/ramadhan73/DHAN-UBOT/DHAN-UBOT/varshelper.txt)")


CMD_HELP.update({
    "dhanhelper":
    "`.helpme`\
\nPenjelasan: Bantuan Untuk DHAN-UBOT.\
\n`.vars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
