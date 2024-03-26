#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import asyncio, time
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
#from config import ADMIN

START_TEXT = """
Hᴇʟʟᴏ Mᴀᴡᴀ ❤️ ɪ ᴀᴍ Sɪᴍᴘʟᴇ Rᴇɴᴀᴍᴇ 𝟸𝟺 Bᴏᴛ⚡\n Tʜɪꜱ ʙᴏᴛ ɪꜱ ᴍᴀᴅᴇ ʙʏ <b><a href=https://t.me/Sunrises24botupdates>SUNRISES ™💥</a></b>
"""

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#START
@Client.on_message(filters.command("start") & filters.private)
async def start(bot, msg):       
    if FSUB_CHANNEL:
        try:
            # Check if the user is banned
            user = await client.get_chat_member(FSUB_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await message.reply_text("Sᴏʀʀʏ, Yᴏᴜ ᴀʀᴇ **B ᴀ ɴ ɴ ᴇ ᴅ**")
                return
        except UserNotParticipant:
            # If the user is not a participant, prompt them to join
            await message.reply_text(
                text="**❤️ Pʟᴇᴀꜱᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Bᴇғᴏʀᴇ Uꜱɪɴɢ Mᴇ ❤️**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="➕ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ ➕", url=f"https://t.me/{FSUB_CHANNEL}")]
                ])
            )
            return
        else:
            # If the user is not banned and is a participant, send the start message
            start_text = START_TEXT.format(message.from_user.first_name) if hasattr(message, "message_id") else START_TEXT
            await message.reply_text(
                text=start_text,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ ❤️", url="https://t.me/Sunrises_24")
                    ],[
                    InlineKeyboardButton("Uᴘᴅᴀᴛᴇs 📢", url="https://t.me/Sunrises24botupdates")
                    ],[
                    InlineKeyboardButton("Hᴇʟᴘ 🌟", callback_data="help"),
                    InlineKeyboardButton("Aʙᴏᴜᴛ 🧑🏻‍💻", callback_data="about") 
                    ]]
                ),
                reply_to_message_id=getattr(message, "message_id", None)
            )
            return            

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#FUNCTION ABOUT HANDLER
@Client.on_message(filters.command("about"))
async def about_command(bot, msg):
    about_text = """
<b>✯ Mʏ Nᴀᴍᴇ : <a href=https://t.me/INFINITYSTARRENAME24BOT>INFINITY ♾️</a></b>
<b>✯ Dᴇᴠᴇʟᴏᴘᴇʀ 🧑🏻‍💻 : <a href=https://t.me/Sunrises_24>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™ ✨</a></b>
<b>✯ Uᴘᴅᴀᴛᴇs 📢 : <a href=https://t.me/Sunrises24BotUpdates>𝐔𝐏𝐃𝐀𝐓𝐄𝐒 📢</a></b>
<b>✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs 📊 : ᴠ2 [Sᴛᴀʙʟᴇ]</b>
    """
    await msg.reply_text(about_text)

# Function to handle /help command
@Client.on_message(filters.command("help"))
async def help_command(bot, msg):
    help_text = """
    <b>Hᴇʟʟᴏ Mᴀᴡᴀ ❤️
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.

🦋 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ
◉ Reply To Any Video/File 🖼️

/start - 𝐵𝑜𝑡 𝑎𝑙𝑖𝑣𝑒 𝑜𝑟 𝑁𝑜𝑡 🚶🏻
/rename - 𝑟𝑒𝑝𝑙𝑎𝑦 𝑤𝑖𝑡ℎ 𝑓𝑖𝑙𝑒 𝑡𝑜 𝑅𝑒𝑛𝑎𝑚𝑒📝
/help - 𝐺𝑒𝑡 𝑑𝑒𝑡𝑎𝑖𝑙𝑒𝑑 𝑜𝑓 𝑏𝑜𝑡 𝑐𝑜𝑚𝑚𝑎𝑛𝑑𝑠 📝
/about - 𝐿𝑒𝑎𝑟𝑛 𝑚𝑜𝑟𝑒 𝑎𝑏𝑜𝑢𝑡 𝑡ℎ𝑖𝑠 𝑏𝑜𝑡 🧑🏻‍💻
ping - 𝑇𝑜 𝐶ℎ𝑒𝑐𝑘 𝑇ℎ𝑒 𝑃𝑖𝑛𝑔 𝑂𝑓 𝑇ℎ𝑒 𝐵𝑜𝑡 📍                   
/view - 𝑇𝑜  𝑆𝑒𝑒 𝑌𝑜𝑢𝑟 𝐶𝑢𝑠𝑡𝑜𝑚 𝑇ℎ𝑢𝑚𝑏𝑛𝑎𝑖𝑙🖼
/del - 𝑇𝑜 𝐷𝑒𝑙𝑒𝑡𝑒 𝑌𝑜𝑢𝑟 𝐶𝑢𝑠𝑡𝑜𝑚 𝑇ℎ𝑢𝑚𝑏𝑛𝑎𝑖𝑙🖼

 💭This bot is rename the files[#2GB].
 
🔱 𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 : <a href='https://t.me/Sunrises_24'>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™</a></b>
    
   """
    await msg.reply_text(help_text)



#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#FUNCTION CALLBACK HELP
@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "Sᴇɴᴅ ᴀ ғɪʟᴇ ᴀɴᴅ /rename <new name> ᴡɪᴛʜ ʀᴇᴘʟᴀʏᴇᴅ ʏᴏᴜʀ ғɪʟᴇ\n\n"
    txt += "ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄ🌟\n"
    txt += "/view ᴛᴏ ꜱᴇᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ 👀\n"
    txt += "/del ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ❌"
    txt += "Jᴏɪɴ : @Sunrises24BotUpdates"
    button= [[        
        InlineKeyboardButton("Cʟᴏꜱᴇ ❌", callback_data="del")   
    ]] 
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#FUNCTION CALL BACK ABOUT
@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Dᴇᴠᴇʟᴏᴘᴇʀ =f"<a href=https://t.me/Sunrises_24>SUNRISES™🧑🏻‍💻</a>"     
    txt=f"<b>Mʏ Nᴀᴍᴇ: {me.mention}\nUᴘᴅᴀᴛᴇs 📢: <a href=https://t.me/Sunrises24botupdates>SUNRISES™™</a></b>"                 
    button= [[        
        InlineKeyboardButton("Cʟᴏꜱᴇ ❌", callback_data="del")       
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
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
 
