import os
import threading
import logging

from flask import Flask
from telegram import BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from config import BOT_TOKEN
from database.database import create_tables

from handlers.start import (
    start,
    help_command,
    about,
    status,
    settings,
)

from handlers.callbacks import button_callback
from handlers.download import download


logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

# -----------------------------
# Flask App (Railway Health Check)
# -----------------------------

web = Flask(__name__)


@web.route("/")
def home():
    return "✅ Modex Video Downloader Bot is running."


def run_web():
    port = int(os.environ.get("PORT", 8080))

    web.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False,
    )


# -----------------------------
# Telegram Bot
# -----------------------------

async def post_init(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "Bot main menu"),
        BotCommand("help", "How to use the bot"),
        BotCommand("settings", "Bot settings"),
        BotCommand("about", "About Modex Downloader"),
        BotCommand("status", "Bot status"),
    ])


def main():
    logger.info("Starting Modex Video Downloader Bot...")

    create_tables()

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("settings", settings))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("status", status))

    # Buttons
    app.add_handler(
        CallbackQueryHandler(button_callback)
    )

    # Downloads
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