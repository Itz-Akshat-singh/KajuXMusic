def format_duration(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{mins}:{secs:02d}"