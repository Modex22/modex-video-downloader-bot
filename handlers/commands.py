from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Watsup! This is Modex.\n\n"
        "Send me a TikTok, Instagram, X, or Snapchat link."
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 Modex Video Downloader\n\n"
        "Supports:\n"
        "• TikTok\n"
        "• Instagram\n"
        "• X (Twitter)\n"
        "• Snapchat"
    )

import os

from telegram import Update
from telegram.ext import ContextTypes


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):

    download_count = len(os.listdir("downloads"))

    from keyboards.main import home_keyboard

    await update.message.reply_text(
    "👋 Watsup! to Modex Downloader!\n\n"
    "Send me a TikTok, Instagram, X or Snapchat link.",
    reply_markup=home_keyboard()
)