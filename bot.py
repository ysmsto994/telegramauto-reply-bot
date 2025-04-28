from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7671110150:AAGSl9BFTFuY8zxuEELmK2tS9x19p49GJCo"

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Echo: {update.message.text}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply("Hello, I am your bot!")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text.lower()  # ubah ke huruf kecil untuk memudahkan pencocokan

    if "hai" in pesan:
        await update.message.reply_text("Hai juga! 😊")
    elif "anjing" in pesan:
        await update.message.reply_text("lo yang kaya anjing🦮")
    elif "assalamualaikum" in pesan:
        await update.message.reply_text("Waalaikumsalam!")
    elif "sok keras admin" in pesan:
        await update.message.reply_text("sini maju lu semua,biar gue bantai")
    else:
        await update.message.reply_text("Maaf, saya tidak mengerti.")

application = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot berjalan...")
app.run_polling()
