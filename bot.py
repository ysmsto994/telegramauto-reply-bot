import asyncio
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    MessageHandler, ContextTypes, filters
)
import os
from dotenv import load_dotenv

# Memuat file .env dan mengambil token
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Setup logging
logging.basicConfig(level=logging.INFO)

# Pengecekan token
if not TOKEN:
    logging.error("Token tidak ditemukan! Pastikan Anda sudah menambahkan BOT_TOKEN di file .env.")
    exit(1)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("Menerima perintah /start")
    await update.message.reply_text("Hello, I am your bot!")

# Auto-reply handler
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text.lower()
    logging.info(f"Pesan diterima: {pesan}")
    if "utc" in pesan or "jam utc" in pesan:
        # Ambil waktu UTC saat ini
        utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        # Kirim gambar dan waktu UTC
        url_gambar = "https://drive.google.com/file/d/1sMkTVmFaTube-GFQAt1BjrHcgJIua5xt/view?usp=drive_link"
        await update.message.reply_photo(photo=url_gambar, caption=f"Ini adalah waktu UTC saat ini: {utc_time}")
    elif "hai" in pesan:
        await update.message.reply_text("Hai juga! 😊")
    elif "anjing" in pesan:
        await update.message.reply_text("lo yang kaya anjing🦮")
    elif "assalamualaikum" in pesan:
        await update.message.reply_text("Waalaikumsalam!")
    elif "sok keras admin" in pesan:
        await update.message.reply_text("sini maju lu semua biar gue bantai")
    else:
        await update.message.reply_text(f"saya tidak mengerti: {saya hanya keledai}")

# Main function
async def main():
    logging.info("Memulai aplikasi bot...")
    app = ApplicationBuilder().token(TOKEN).build()

    # Menambahkan handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    logging.info("Bot berjalan...")
    await app.run_polling()

# Jalankan bot
if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()

    asyncio.get_event_loop().run_until_complete(main())

