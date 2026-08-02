import os
import asyncio

from telegram import Update
from telegram.ext import ContextTypes

from utils.validators import (
    is_url,
    get_platform,
)

from utils.cooldown import can_download

from database.database import (
    save_user,
    save_download,
)

from downloaders import download_video
from logger import logger


MAX_FILE_SIZE = 49 * 1024 * 1024  # 49 MB


async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    url = update.message.text.strip()

    logger.info(f"Received URL: {url}")

    save_user(user)

    # Prevent spam
    if not can_download(user_id):
        await update.message.reply_text(
            "⏳ Please wait a few seconds before downloading another video."
        )
        return

    # Validate URL
    if not is_url(url):
        await update.message.reply_text(
            "❌ Please send a valid video URL."
        )
        return

    # Detect platform
    platform = get_platform(url)

    logger.info(f"Detected platform: {platform}")

    if platform is None:
        await update.message.reply_text(
            "❌ Unsupported website.\n\n"
            "Supported platforms:\n"
            "• TikTok\n"
            "• Instagram\n"
            "• X (Twitter)\n"
            "• Snapchat"
        )
        return

    # Downloading message
    message = await update.message.reply_text(
        f"📥 Downloading {platform} video..."
    )

    file = None

    try:
        logger.info(
            f"{user.username or user.first_name} started downloading a {platform} video."
        )

        logger.info("Starting yt-dlp...")

        file = await asyncio.to_thread(
            download_video,
            platform,
            url,
        )

        logger.info(f"Download complete: {file}")

        if not file or not os.path.exists(file):
            raise FileNotFoundError("Downloaded file was not found.")

        # Check file size
        file_size = os.path.getsize(file)

        logger.info(f"File size: {file_size} bytes")

        if file_size > MAX_FILE_SIZE:
            os.remove(file)

            await message.edit_text(
                "❌ This video is too large to send through Telegram."
            )

            logger.warning(
                f"File exceeded Telegram limit ({file_size} bytes)."
            )
            return

        await message.edit_text("⬆ Uploading video...")

        with open(file, "rb") as video:
            await update.message.reply_video(
                video=video,
                supports_streaming=True,
            )

        logger.info("Video uploaded successfully.")

        save_download(
            user.id,
            platform,
            url,
        )

        await message.edit_text(
            "✅ Video sent successfully!"
        )

    except Exception as e:
        logger.exception("Download failed")

        await message.edit_text(
            f"❌ Download failed.\n\n{str(e)}"
        )

    finally:
        if file and os.path.exists(file):
            try:
                os.remove(file)
                logger.info("Temporary file deleted.")
            except Exception:
                logger.warning(
                    f"Could not delete file: {file}"
                )

        await asyncio.sleep(2)

        try:
            await message.delete()
        except Exception:
            pass