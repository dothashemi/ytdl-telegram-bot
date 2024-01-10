from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from local import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send me a YouTube link!')
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('For example: https://www.youtube.com/watch?v=4WJbPNpV0sw')

    
async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text

    # log!
    print(f"User ({update.message.chat.id}): {text}")

    # TODO: download the video
    # TODO: send the video

    await update.message.reply_text("I will send!!")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # just log!
    print(f"--- NOTICE: {update} caused error {context.error} ---")


def start():
    # log!
    print("Starting Telegram Bot ...")

    app = Application.builder().token(TKEY).build()

    # define commands:
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))

    # message handler:
    app.add_handler(MessageHandler(filters.TEXT, message))

    # error handler:
    app.add_error_handler(error)

    # log!
    print("Polling ...")

    app.run_polling(poll_interval=3)
