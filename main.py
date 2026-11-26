import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

async def start(update, context):
    await update.message.reply_text("Hi muthe! Cinema peru ayachu tha")

async def movie(update, context):
    name = update.message.text
    await update.message.reply_text(f"Nee chodicha cinema: {name} - njan nokkatte!")

def main():
    token = os.environ.get("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, movie))
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
