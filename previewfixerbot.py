
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('I add dd to Instagram links, fx to Twitter links and fixupx to X links')
def modify_links(update: Update, context: CallbackContext) -> None:
    if update.message.text:
        urls = [word for word in update.message.text.split() if word.startswith(("https://www.instagram.com/", "https://twitter.com/", "https://x.com/"))]

        for url in urls:
            if url.startswith("https://www.instagram.com/"):
                modified_url = url.replace("https://www.instagram.com/", "https://www.ddinstagram.com/")
                update.message.reply_text(f"Modified Instagram link: {modified_url}")
            elif url.startswith("https://twitter.com/"):
                modified_url = url.replace("https://twitter.com/", "https://fxtwitter.com/")
                update.message.reply_text(f"Modified Twitter link: {modified_url}")
            elif url.startswith("https://x.com/"):
                modified_url = url.replace("https://x.com/", "https://fixupx.com/")
                update.message.reply_text(f"Modified X link: {modified_url}")
def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, modify_links))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
