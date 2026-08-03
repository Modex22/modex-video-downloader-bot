import os
import threading
import logging

from flask import Flask

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
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

from handlers.callbacks import button_callback
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

    # Create SQLite tables
    create_tables()

    # Create Telegram application
    app = Application.builder().token(BOT_TOKEN).build()

    # -------------------------
    # Debug Handler
    # -------------------------
    async def debug(update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.info(f"UPDATE RECEIVED: {update}")

    app.add_handler(
        MessageHandler(
            filters.ALL,
            debug,
        ),
        group=0,
    )

    # -------------------------
    # Command Handlers
    # -------------------------
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("status", status))

    # -------------------------
    # Button Callback Handler
    # -------------------------
    app.add_handler(
        CallbackQueryHandler(button_callback)
    )

    # -------------------------
    # Video Download Handler
    # -------------------------
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
        allowed_updates=Update.ALL_TYPES,
    )


if __name__ == "__main__":
    threading.Thread(
        target=run_web,
        daemon=True,
    ).start()

    main()