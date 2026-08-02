from .common import download


def download_tiktok(url, progress_callback=None):

    options = {
        "extractor_args": {
            "tiktok": {
                "app_info": ["musical_ly"]
            }
        }
    }

    return download(
        url,
        progress_callback,
        options
    )

from .common import download

def download_tiktok(url, progress_callback=None):
    return download(
        url,
        progress_callback,
        {
            "format": "best",
        },
    )