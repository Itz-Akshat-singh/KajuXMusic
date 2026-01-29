from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME

# Custom start message with image and buttons
START_CAPTION = """
HEY BABY {username} 🌸

🎶 THIS IS : {bot_name} 🎶
⚡ Smooth Beats • Stable & Seamless Music Flow

💻 This bot is created by 𝐘ᴀsʜ ꭙ 𝐀ᴋsʜᴀᴛ
"""

BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("➕ ADD ME TO YOUR CHAT", url="https://t.me/KajuXMusic_Robot?startgroup=true")],
    [InlineKeyboardButton("🔔 UPDATES", url="https://t.me/PoeticSoulWorld"),  # Customize
     InlineKeyboardButton("🛠 SUPPORT", url="https://t.me/+bg6wB9lkrotkZDE1")],  # Customize
    [InlineKeyboardButton("👑 OWNER", url="https://t.me/Itz_Akshat_Singh")]  # Customize
])

@Client.on_message(filters.command("start"))
async def start_handler(client, message):
    username = message.from_user.first_name or "User"
    await message.reply_photo(
        photo="assets/start.jpg",  # Your custom image
        caption=START_CAPTION.format(username=username, bot_name=BOT_NAME),
        reply_markup=BUTTONS
    )