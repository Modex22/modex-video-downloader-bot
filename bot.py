from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN
from logger import logger

from database.database import create_tables

from handlers.commands import (
    start,
    help_command,
    about,
    status,
)

from handlers.download import download


async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Handle unexpected errors."""
    logger.exception(
        "Unhandled exception:",
        exc_info=context.error,
    )

    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ An unexpected error occurred.\n"
                "Please try again later."
            )
        except Exception:
            pass


def main():
    logger.info("Starting Modex Video Downloader Bot...")

    # Create database tables if they don't exist
    create_tables()

    # Create the Telegram application
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("status", status))

    # Handle video links
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            download,
        )
    )

    # Register global error handler
    app.add_error_handler(error_handler)

    logger.info("Bot started successfully.")
    print("🚀 Modex Video Downloader Bot is running...")

    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()