from telegram import Update
from telegram.ext import ContextTypes

from handlers.commands import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Watsup! Welcome to Modex Downloader!\n\n"
        "Send me a TikTok, Instagram, X (Twitter), or Snapchat link.",
        reply_markup=main_menu(),
    )