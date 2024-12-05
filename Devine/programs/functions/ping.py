from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Dev import app
from Devine.root.call import Devine
from Devine.utils import system_sys_stats
from Devine.utils.decorators.language import language
from configuration import filter_users, SUPPORT_CHANNEL, SUPPORT_CHAT


@app.on_message(filters.command(["ping", "mping@AizenSupremeBot"]) & ~filter_users)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_text(
        text=_["ping_1"].format(app.mention),
    )  # Fixed missing parenthesis here

    pytgping = await Aizen.ping()
    UP, CPU, RAM, DISK = await system_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=SUPPORT_CHANNEL),
                InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
            ],
            [
                InlineKeyboardButton(text="ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=true"),
            ],
        ])
    )
