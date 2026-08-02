import os
import yt_dlp

DOWNLOAD_FOLDER = "downloads"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def download(url, progress_callback=None, options=None):

    def hook(data):
        if progress_callback:
            progress_callback(data)

    ydl_opts = {
        # Prefer the original MP4 stream
        "format": "best[ext=mp4]/best",

        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",

        # Don't force a remux
        "noplaylist": True,
        "quiet": True,

        "progress_hooks": [hook],
    }

    if options:
        ydl_opts.update(options)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)