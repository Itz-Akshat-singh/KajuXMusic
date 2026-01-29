from py_tgcalls import PyTgCalls, StreamType
from py_tgcalls.types import AudioPiped
from yt_dlp import YoutubeDL
import os
from utils.thumbnail import get_thumbnail
from utils.formatter import format_duration
from config import BOT_NAME

tgcalls = None  # Will be set in main.py

async def play_song(client, chat_id, url, user):
    try:
        # Check if VC is active
        if not await tgcalls.is_connected(chat_id):
            return None

        # Download audio
        ydl_opts = {'format': 'bestaudio', 'outtmpl': 'temp_audio.%(ext)s'}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        # Get metadata
        title = info['title']
        duration = format_duration(info['duration'])
        thumbnail = await get_thumbnail(url)

        # Stream to VC
        await tgcalls.join_group_call(chat_id, AudioPiped(file_path), stream_type=StreamType().local_stream)

        # Send rich message
        caption = f"""
🔊 Header
▶ NOW PLAYING

🖼 Thumbnail: [Attached]

📄 Song Details
🎵 TITLE : {title}
⏱ DURATION : {duration}
👤 REQUESTED BY : {user.first_name}

🏷 Branding
✨ This bot is created by 𝐘ᴀsʜ ꭙ 𝐀ᴋsʜᴀᴛ
        """
        await client.send_photo(chat_id, thumbnail, caption=caption)

        # Clean up
        os.remove(file_path)
        return caption

    except Exception as e:
        print(f"Error: {e}")
        return None

async def pause(chat_id):
    await tgcalls.pause_stream(chat_id)

async def resume(chat_id):
    await tgcalls.resume_stream(chat_id)

async def skip(chat_id):
    await tgcalls.change_stream(chat_id, None)  # Skip to next in queue (implement queue)

async def stop(chat_id):
    await tgcalls.leave_group_call(chat_id)

async def leave_vc(chat_id):
    await tgcalls.leave_group_call(chat_id)