from pyrogram import Client, filters 
import os
from helper.database import db
from helper.add import add_user_to_database


@Client.on_message(filters.command("show_thumbnail") & filters.private)
async def show_thumbnail(bot, msg):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    thumbnail = await db.get_thumbnail(m.from_user.id)
    if not thumbnail:
        return await m.reply_text("You didn't set custom thumbnail!")
    await c.send_photo(m.chat.id, thumbnail, caption="Custom Thumbnail",
                       reply_markup=types.InlineKeyboardMarkup(
                           [[types.InlineKeyboardButton("Delete Thumbnail",
                                                        callback_data="deleteThumbnail")]]
                       ))


@Client.on_message(filters.command("set_thumbnail") & filters.private)
async def set_thumbnail(bot, msg):
    if (not m.reply_to_message) or (not m.reply_to_message.photo):
        return await m.reply_text("Reply to any image to save in as custom thumbnail!")
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await db.set_thumbnail(m.from_user.id, m.reply_to_message.photo.file_id)
    await m.reply_text("Okay,\n"
                       "I will use this image as custom thumbnail.",
                       reply_markup=types.InlineKeyboardMarkup(
                           [[types.InlineKeyboardButton("Delete Thumbnail",
                                                        callback_data="deleteThumbnail")]]
                       ))


@Client.on_message(filters.command("delete_thumbnail") & filters.private)
async def delete_thumbnail(bot, msg):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await db.set_thumbnail(m.from_user.id, None)
    await m.reply_text("Okay,\n"
                       "I deleted custom thumbnail from my database.")
