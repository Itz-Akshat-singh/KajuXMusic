import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
STRING_SESSION = os.getenv("STRING_SESSION", None)
OWNER_ID = int(os.getenv("OWNER_ID"))

BOT_NAME = "KajuX Music"
BOT_USERNAME = "KajuXMusicBot"  # Replace with your bot's username