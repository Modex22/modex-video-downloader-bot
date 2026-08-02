import os
import threading
import logging

from flask import Flask

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from database.database import create_tables

from handlers.start import (
    start,
    help_command,
    about,
    status,
)

from handlers.download import download

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

# ---------------------------------
# Flask App (Render Health Check)
# ---------------------------------

web = Flask(__name__)


@web.route("/")
def home():
    return "✅ Modex Video Downloader Bot is running."


def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False,
    )


# ---------------------------------
# Telegram Bot
# ---------------------------------

def main():
    logger.info("Starting Modex Video Downloader Bot...")

    # Create database tables
    create_tables()

    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("status", status))

    # Video Downloader
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            download,
        )
    )

    logger.info("Bot started successfully.")
    print("🚀 Modex Video Downloader Bot is running...")

    app.run_polling(
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    threading.Thread(
        target=run_web,
        daemon=True,
    ).start()

    main()