from asyncio import Queue

download_queue = Queue()

import asyncio

from .queue import download_queue


async def worker():

    while True:

        job = await download_queue.get()

        try:
            await job()

        finally:
            download_queue.task_done()