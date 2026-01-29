import aiohttp
from yt_dlp import YoutubeDL

async def get_thumbnail(url):
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info['thumbnail']