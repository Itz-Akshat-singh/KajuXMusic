from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION
from handlers import start, play, admin
from call.music import app as music_app

# Initialize bot
app = Client(
    "KajuXMusic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    session_string=STRING_SESSION
)

# Initialize PyTgCalls for VC
tgcalls = PyTgCalls(app)

# Register handlers
app.add_handler(start.handler)
app.add_handler(play.handler)
app.add_handler(admin.handler)

# Start the bot
if __name__ == "__main__":
    print("Starting KajuX Music Bot...")
    tgcalls.start()
    app.run()
