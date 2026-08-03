import yt_dlp
import os

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def download_twitter(url, progress_callback=None):

    def hook(data):
        if progress_callback:
            progress_callback(data)

    ydl_opts = {
        # Preserve Twitter's original stream
        "format": "bv*+ba/b",

        # Output
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",

        # Always output MP4
        "merge_output_format": "mp4",

        # No playlist
        "noplaylist": True,

        "progress_hooks": [hook],

        "quiet": True,

        # Let ffmpeg remux if needed
        "postprocessors": [
            {
                "key": "FFmpegVideoRemuxer",
                "preferedformat": "mp4",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)