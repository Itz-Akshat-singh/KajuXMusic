from yt_dlp import YoutubeDL

async def search_youtube(query):
    ydl_opts = {'default_search': 'ytsearch', 'noplaylist': True}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        return info['entries'][0]['webpage_url'] if info['entries'] else None