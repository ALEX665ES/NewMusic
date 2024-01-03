from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOGGER_ID
from InflexMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def new_message(chat_id: int, message: str, reply_markup=None):
    await app.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = f"{message.from_user.first_name}"
        chatusername = f"@{message.chat.username}"
        title = message.chat.title
        chat_id = message.chat.id
        sigma = f" <u>#Nᴇᴡ Gʀᴏᴜᴘ</u> :\n\nCʜᴀᴛ ɪᴅ : {chat_id}\nCʜᴀᴛ Tɪᴛʟᴇ : {title}\nCʜᴀᴛ Usᴇʀɴᴀᴍᴇ : {chatusername}\nAᴅᴅᴇᴅ ʙʏ : {added_by}"

        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, user_id=message.from_user.id
                    )
                ]
            ]
        )

        await new_message(LOGGER_ID, sigma, reply_markup)


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    if (await client.get_me()).id == message.left_chat_member.id:
        removed_by = f"{message.from_user.first_name}"
        title = message.chat.title
        chat_id = message.chat.id
        bye = f" <u>#Lᴇғᴛ Gʀᴏᴜᴘ</u> :\n\nCʜᴀᴛ ɪᴅ : {chat_id}\nCʜᴀᴛ Tɪᴛʟᴇ : {title}\nRᴇᴍᴏᴠᴇᴅ Bʏ : {removed_by}"

        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, user_id=message.from_user.id
                    )
                ]
            ]
        )

        await new_message(LOGGER_ID, bye, reply_markup)
