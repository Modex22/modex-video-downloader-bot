import time

users = {}


def can_download(user_id):

    now = time.time()

    if user_id not in users:
        users[user_id] = now
        return True

    if now - users[user_id] >= 5:
        users[user_id] = now
        return True

    return False