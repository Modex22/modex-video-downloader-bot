import os

from telegram import Update
from telegram.ext import ContextTypes

from keyboards.main import home_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Watsup! Welcome to Modex Downloader!\n\n"
        "Send me a TikTok, Instagram, X (Twitter), or Snapchat link.",
        reply_markup=home_keyboard()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 How to use Modex Downloader\n\n"
        "1. Copy a public video link.\n"
        "2. Send it to me.\n"
        "3. I'll download and send the video back.\n\n"
        "Supported platforms:\n"
        "• TikTok\n"
        "• Instagram\n"
        "• X (Twitter)\n"
        "• Snapchat"
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Modex Video Downloader\n\n"
        "Version: 1.0\n\n"
        "Supports:\n"
        "• TikTok\n"
        "• Instagram\n"
        "• X (Twitter)\n"
        "• Snapchat"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    os.makedirs("downloads", exist_ok=True)

    download_count = len(os.listdir("downloads"))

    await update.message.reply_text(
        f"🟢 Bot Status\n\n"
        f"Downloads folder: {download_count} file(s)\n\n"
        "Supported platforms:\n"
        "• TikTok\n"
        "• Instagram\n"
        "• X (Twitter)\n"
        "• Snapchat"
    )