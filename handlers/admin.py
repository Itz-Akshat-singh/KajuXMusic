from pyrogram import Client, filters
from config import OWNER_ID
from call.music import pause, resume, skip, stop, leave_vc

@Client.on_message(filters.command(["pause", "resume", "skip", "end"]) & filters.group)
async def admin_controls(client, message):
    if message.from_user.id != OWNER_ID:
        await message.reply("Only owner can use this!")
        return

    cmd = message.command[0]
    chat_id = message.chat.id

    if cmd == "pause":
        await pause(chat_id)
        await message.reply("Paused!")
    elif cmd == "resume":
        await resume(chat_id)
        await message.reply("Resumed!")
    elif cmd == "skip":
        await skip(chat_id)
        await message.reply("Skipped!")
    elif cmd == "end":
        await leave_vc(chat_id)
        await message.reply("Left VC!")

@Client.on_callback_query()
async def callback_handler(client, query):
    data = query.data
    chat_id = query.message.chat.id

    if data == "pause":
        await pause(chat_id)
    elif data == "resume":
        await resume(chat_id)
    elif data == "skip":
        await skip(chat_id)
    elif data == "stop":
        await stop(chat_id)
    elif data == "loop":
        # Implement loop logic in music.py
        pass
    elif data == "volume":
        # Implement volume control in music.py
        pass

    await query.answer()