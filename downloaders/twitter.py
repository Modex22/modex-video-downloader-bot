from .common import download


def download_twitter(url, progress_callback=None):
    return download(
        url,
        progress_callback
    )