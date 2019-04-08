import logging

from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text("""Ola, atualmente disponho dos seguintes comandos:\n
                                \proxima -> Lista a/as proximas secoes marcadas\n
                                \\noob   -> Exibe uma serie de mensagens de instrucoes para iniciantes""")


def proxima(context):
    ob = context.job
    context.bot.send_message(job.context, text='Eu ainda nao sei fazer isso...')

def main():
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("733179269:AAHjp4qJUO6Q3rhWJOQAt9kB3VVW86s3s3E", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ajuda", start))
    dp.add_handler(CommandHandler("proxima", proxima)
    dp.add_handler(CommandHandler("noob", noob)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
main()