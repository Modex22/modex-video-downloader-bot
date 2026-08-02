from .common import download


def download_snapchat(url, progress_callback=None):
    return download(
        url,
        progress_callback
    )