from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


def home_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "📥 Download Video",
                callback_data="download"
            )
        ],

        [
            InlineKeyboardButton(
                "❓ Help",
                callback_data="help"
            ),

            InlineKeyboardButton(
                "ℹ About",
                callback_data="about"
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)