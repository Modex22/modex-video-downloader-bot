from .common import download


def download_tiktok(url, progress_callback=None):
    return download(
        url,
        progress_callback,
        {
            "format": "best[ext=mp4]/best",
            "extractor_args": {
                "tiktok": {
                    "app_info": ["musical_ly"]
                }
            }
        }
    )