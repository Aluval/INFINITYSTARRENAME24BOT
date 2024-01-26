import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
#from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt=f"Hᴇʏ {msg.from_user.mention} Mᴀᴡᴀ❤️.ɪ ᴀᴍ Sɪᴍᴘʟᴇ Rᴇɴᴀᴍᴇ 𝟸𝟺 Bᴏᴛ⚡.\n Tʜɪꜱ ʙᴏᴛ ɪꜱ ᴍᴀᴅᴇ ʙʏ<b><a href=https://t.me/Sunrises24botupdates>SUNRISES ™💥</a></b>"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ ❤️", url="https://t.me/Sunrises_24")
        ],[
        InlineKeyboardButton("Uᴘᴅᴀᴛᴇs 📢", url="https://t.me/Sunrises24botupdates")
    ],[
        InlineKeyboardButton("Hᴇʟᴘ 🌟", callback_data="help"),
        InlineKeyboardButton("Aʙᴏᴜᴛ 🧑🏻‍💻", callback_data="about") 
    ]])
    if msg.from_user.id:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)

@Client.on_message(filters.command("about"))
async def about_command(bot, msg):
    about_text = """
<b>✯ Mʏ Nᴀᴍᴇ : <a href=https://t.me/INFINITYSTARRENAME24BOT>INFINITY ♾️</a></b>
<b>✯ Dᴇᴠᴇʟᴏᴘᴇʀ 🧑🏻‍💻 : <a href=https://t.me/Sunrises_24>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™ ✨</a></b>
<b>✯ Uᴘᴅᴀᴛᴇs 📢 : <a href=https://t.me/Sunrises24BotUpdates>𝐔𝐏𝐃𝐀𝐓𝐄𝐒 📢</a></b>
<b>✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs 📊 : ᴠ2 [Sᴛᴀʙʟᴇ]</b>
    """
    await msg.reply_text(about_text)

@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "Sᴇɴᴅ ᴀ ғɪʟᴇ ᴀɴᴅ /ʀᴇɴᴀᴍᴇ <ɴᴇᴡ ɴᴀᴍᴇ> ᴡɪᴛʜ ʀᴇᴘʟᴀʏᴇᴅ ʏᴏᴜʀ ғɪʟᴇ\n\n"
    txt += "ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄ🌟\n"
    txt += "/ᴠɪᴇᴡ ᴛᴏ ꜱᴇᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ 👀\n"
    txt += "/ᴅᴇʟ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ❌"
    txt += "Jᴏɪɴ : @Sunrises24BotUpdates"
    button= [[        
        InlineKeyboardButton("Cʟᴏꜱᴇ ❌", callback_data="del")   
    ]] 
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Dᴇᴠᴇʟᴏᴘᴇʀ 🧑🏻‍💻=f"<a href=https://t.me/Sunrises_24>SUNRISES™</a>"     
    txt=f"<b>Mʏ Nᴀᴍᴇ: {me.mention}\nUᴘᴅᴀᴛᴇs 📢: <a href=https://t.me/Sunrises24botupdates>SUNRISES™™</a></b>"                 
    button= [[        
        InlineKeyboardButton("Cʟᴏꜱᴇ ❌", callback_data="del")       
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#Ping
@Client.on_message(filters.command("ping"))
async def ping(bot, msg):
    start_t = time.time()
    rm = await msg.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!📍\n{time_taken_s:.3f} ms")
 
