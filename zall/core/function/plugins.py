import importlib
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from zall import bot, ubot
from zall.core.helpers import PY
from zall.modules import loadModule
from zall.core.database import *
from zall.config import OWNER_ID
from platform import python_version
from pyrogram import __version__
HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = importlib.import_module(f"zall.modules.{mod}")
        module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
        if module_name:
            HELP_COMMANDS[module_name] = imported_module
    print(f"[🤖 @{bot.me.username} 🤖] [💠 SUKSES ONLINE 💠]")
    await bot.send_message(OWNER_ID, 
       f"""                    
<b>🤖 {bot.me.mention} ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪꜰᴋᴀɴ</b>
<b>📁 ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}</b>
<b>📘 ᴘʏᴛʜᴏɴ: {python_version()}</b>
<b>📙 ᴘʏʀᴏɢʀᴀᴍ: {__version__}</b>

<b>👤 ᴜsᴇʀʙᴏᴛ: {len(ubot._ubot)}</b>
""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🤖 ʟɪꜱᴛ ᴜꜱᴇʀʙᴏᴛ 🤖", callback_data="cek_ubot"),
                ],
            ]
        ),
                          )
    
@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
