# Tg:@Sunrises_24

import shutil
import psutil
from pyrogram import filters, enums, Client
from pyrogram.types import (
    Message
)
from config import ADMIN 
from helper.database import db
from main.utils import humanbytes
from main.handlers.broadcast import broadcast_handler


@Client.on_message(filters.command("status") & filters.user(Config.ADMIN))
async def status_handler(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**Total Disk Space:** {total} \n"
             f"**Used Space:** {used}({disk_usage}%) \n"
             f"**Free Space:** {free} \n"
             f"**CPU Usage:** {cpu_usage}% \n"
             f"**RAM Usage:** {ram_usage}%\n\n"
             f"**Total Users in DB:** `{total_users}`",        
        parse_mode="enums",
        quote=True
    )


@Client.on_message(filters.command("broadcast") & filters.user(Config.ADMIN) & filters.reply)
async def broadcast_in(_, m: Message):
    await broadcast_handler(m)
