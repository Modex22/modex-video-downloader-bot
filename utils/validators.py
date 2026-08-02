import re


def is_url(text):
    pattern = r"https?://\S+"
    return re.match(pattern, text)


def get_platform(url):
    if "tiktok.com" in url or "vt.tiktok.com" in url:
        return "TikTok"

    elif "instagram.com" in url:
        return "Instagram"

    elif "twitter.com" in url or "x.com" in url:
        return "Twitter"

    elif "snapchat.com" in url:
        return "Snapchat"

    return None