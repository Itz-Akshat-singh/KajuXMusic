from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from call.music import play_song
from utils.yt import search_youtube
from config import BOT_NAME

@Client.on_message(filters.command("play") & filters.group)
async def play_handler(client, message):
    if not message.reply_to_message and len(message.command) < 2:
        await message.reply("Usage: /play <song name or YouTube link>")
        return

    query = " ".join(message.command[1:]) or message.reply_to_message.text
    user = message.from_user

    # Search YouTube if not a link
    if not query.startswith("http"):
        query = await search_youtube(query)
        if not query:
            await message.reply("Song not found!")
            return

    # Play the song
    result = await play_song(client, message.chat.id, query, user)
    if result:
        await message.reply(result, reply_markup=get_player_buttons())
    else:
        await message.reply("Failed to play song. Check if VC is active.")

def get_player_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⏸ Pause", callback_data="pause"),
         InlineKeyboardButton("▶ Resume", callback_data="resume")],
        [InlineKeyboardButton("⏭ Skip", callback_data="skip"),
         InlineKeyboardButton("🔁 Loop", callback_data="loop")],
        [InlineKeyboardButton("❌ Stop", callback_data="stop"),
         InlineKeyboardButton("🔉 Volume", callback_data="volume")]
    ])