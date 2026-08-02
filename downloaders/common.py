import os
import yt_dlp

DOWNLOAD_FOLDER = "downloads"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def download(url, progress_callback=None, options=None):

    def hook(data):
        if progress_callback:
            progress_callback(data)

    ydl_opts = {
        "format": "best",
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": True,
        "progress_hooks": [hook],
    }

    if options:
        ydl_opts.update(options)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)