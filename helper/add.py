#Tg: @Sunrises_24

from configs import Config
from helper.database import db
from pyrogram import Client



async def add_user_to_database(bot, msg):
    if not await db.is_user_exist(msg.from_user.id):
        await db.add_user(msg.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_flooded_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER: \n\nNew User [{msg.from_user.first_name}](tg://user?id={msg.from_user.id}) started @{(await bot.get_me()).username} !!"
            )
