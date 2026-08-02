from .common import download


def download_instagram(url, progress_callback=None):
    return download(
        url,
        progress_callback
    )