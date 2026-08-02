from .tiktok import download_tiktok
from .instagram import download_instagram
from .twitter import download_twitter
from .snapchat import download_snapchat


def download_video(platform, url, progress_callback=None):
    downloaders = {
        "TikTok": download_tiktok,
        "Instagram": download_instagram,
        "Twitter": download_twitter,
        "Snapchat": download_snapchat,
    }

    downloader = downloaders.get(platform)

    if downloader is None:
        raise ValueError(f"Unsupported platform: {platform}")

    return downloader(url)