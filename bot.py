from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Yahan apna BotFather se liya hua Token paste karein
TOKEN = "7201127347:AAEVWzTUD7D1O6LuFfrs0lNifye8AkE3dp0"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! Welcome to my bot. How can I help you?")

async def reply(update: Update, context: CallbackContext):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    # Start bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
