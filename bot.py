import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    MessageHandler, ContextTypes, filters
)

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am your bot!")

# Auto-reply handler
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text.lower()

    if "hai" in pesan:
        await update.message.reply_text("Hai juga! 😊")
    elif "anjing" in pesan:
        await update.message.reply_text("lo yang kaya anjing🦮")
    elif "assalamualaikum" in pesan:
        await update.message.reply_text("Waalaikumsalam!")
    elif "sok keras admin" in pesan:
        await update.message.reply_text("sini maju lu semua, biar gue bantai")
    else:
        await update.message.reply_text(f"Echo: {update.message.text}")

# Main function
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Bot berjalan...")
    await app.run_polling()

# Jalankan bot
if __name__ == "__main__":
    asyncio.run(main())

