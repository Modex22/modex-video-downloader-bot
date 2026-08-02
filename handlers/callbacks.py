from telegram import Update
from telegram.ext import ContextTypes

from handlers.start import help_command, about


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    # Stop Telegram's loading animation
    await query.answer()

    if query.data == "download":
        await query.message.reply_text(
            "📥 Send me a TikTok, Instagram, X (Twitter), or Snapchat link."
        )

    elif query.data == "help":
        await help_command(update, context)

    elif query.data == "about":
        await about(update, context)