from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(bot, msg):
    if len(msg.command) == 1:
       return await msg.reply_text("**Give me a caption to set.\n\nExample:- `/set_caption {filename}`**")
    caption = msg.text.split(" ", 1)[1]
    addcaption(int(msg.chat.id), caption)
    await msg.reply_text("**yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy ᴀᴅᴅᴇᴅ !!**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(bot, msg): 
    caption = find(int(msg.chat.id))[1]
    if not caption:
        await msg.reply_text("**yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴy ᴄᴏꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**")
        return
    delcaption(int(msg.chat.id))
    await msg.reply_text("**yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy ᴅᴇʟᴇᴛᴇᴅ !!**")
                                      
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(bot, msg): 
    caption = find(int(msg.chat.id))[1]
    if caption:
       await msg.reply_text(f"<b><u>Your Caption:</b></u>\n\n`{caption}`")
    else:
       await msg.reply_text("**yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴy ᴄᴏꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**")

          
