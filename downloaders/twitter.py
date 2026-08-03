import os
import yt_dlp

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def download_twitter(url, progress_callback=None):

    def hook(data):
        if progress_callback:
            progress_callback(data)

    ydl_opts = {
        # Download the highest quality video + audio
        "format": "bv*+ba/b",

        # Save file
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",

        # Merge to MP4
        "merge_output_format": "mp4",

        # Don't download playlists
        "noplaylist": True,

        "quiet": True,

        "progress_hooks": [hook],

        # Fix Twitter/X compatibility
        "postprocessors": [
            {
                "key": "FFmpegVideoRemuxer",
                "preferedformat": "mp4",
            }
        ],

        # Extra FFmpeg arguments for better Telegram/iPhone compatibility
        "postprocessor_args": [
            "-movflags", "+faststart"
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)