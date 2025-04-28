from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7671110150:AAGSl9BFTFuY8zxuEELmK2tS9x19p49GJCo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo!selamat datang")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text.lower()  # ubah ke huruf kecil untuk memudahkan pencocokan

    if "hai" in pesan:
        await update.message.reply_text("Hai juga! 😊")
    elif "anjing" in pesan:
        await update.message.reply_text("lo yang kaya anjing")
    elif "assalamualaikum" in pesan:
        await update.message.reply_text("Waalaikumsalam!")
    else:
        await update.message.reply_text("Maaf, saya tidak menegrti.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Bot berjalan...")
app.run_polling()

app.run_polling()
