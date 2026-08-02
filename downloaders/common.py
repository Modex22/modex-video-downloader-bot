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

        # Save downloaded file
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",

        # Don't download playlists
        "noplaylist": True,

        # Show yt-dlp logs while debugging
        "quiet": False,
        "no_warnings": False,

        # Progress callback
        "progress_hooks": [hook],
    }

    if options:
        ydl_opts.update(options)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        # Get the actual downloaded filename
        filename = ydl.prepare_filename(info)

        # If yt-dlp changes the extension, return the real file
        if not os.path.exists(filename):
            base = os.path.splitext(filename)[0]

            for ext in [".mp4", ".mkv", ".webm", ".mov"]:
                if os.path.exists(base + ext):
                    return base + ext

        return filename