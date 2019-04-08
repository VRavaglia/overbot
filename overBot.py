import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.send_message(update.message.chat_id,"""  *Olá, sou o Bot corno oficial deste grupo*.\n
Atualmente disponho dos seguintes comandos:\n
/ajuda   -> Exibe esta mensagem\n
/proxima -> Lista a/as próximas sessoes marcadas\n
/noob    -> Exibe uma serie de mensagens de instruções para iniciantes\n
Meu [repositório](https://github.com/VRavaglia/overbot)""", parse_mode= 'Markdown')


def proxima(bot, update):
    bot.send_message(update.message.chat_id,'Eu ainda nao sei fazer isso...', parse_mode= 'Markdown')

def noob(bot, update):
    bot.send_message(update.message.chat_id,"""  Primeiramente, bom/boa dia/tarde/noite (meu desenvolvedor ainda não gera esse tipo de mensagem de forma inteligente)\n\n
*1* - Peça para o @raposo criar uma ficha no Roll20 para você.\n
*2* - Falando em Roll20, segue o link da [aventura](https://app.roll20.net/join/4330618/qy_bdA)\n
*3* - No canto superior direito há um ícone de um \"jornal\" se você seguiu o passo 1, terá um personagem com
    seu nome, clique nele e siga as instruções para criação de ficha (\"use charactermancer\")\n
*4* - Atualmente dispomos de um bárbaro humano, um monge elfo, um mago meio-elfo, um bardo humano,
    um bruxo meio-orc e um paladino humano.
*5* - Falando em classes e raças, uma lista de [raças](https://www.dndbeyond.com/races), uma lista de 
    [classes](https://www.dndbeyond.com/classes)\n
*6* - Link do [manual do jogador](https://drive.google.com/file/d/1oEHIYiFtlvGWfMNzfRuCZX9ZWgvayisE/view?usp=sharing)\n
*7* - Lista de páginas interessantes:\n
    *5 - 17* (Introdução)\n
    *18 - 44* (Leia apenas a descrição da raça escolhida)\n
    *45* (Breve introdução sobre as classes)\n
    *46 - 122* (Leia apenas a descrição da classe escolhida)\n
    *123 - 128* (Recomendo mas não é necessário)\n
    *145 - 157* (Recomendo mas não é necessário)\n
    *165 - 172* (Personalização do personagem, não é necessário se quiser seguir a classe a risca)\n
    *175 - 181* (Como jogar de fato)\n
    *183 - 189* (Movimentação, recomendo mas não é necessário)\n
    *191 - 200* (Combate)\n
    *203 - 207* (Magia, requisito se sua classe usar magia e recomendação caso contrário)\n
*8* - Boa sorte lendo tudo isso!""", parse_mode= 'Markdown')

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("733179269:AAHjp4qJUO6Q3rhWJOQAt9kB3VVW86s3s3E")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ajuda", start))
    dp.add_handler(CommandHandler("proxima", proxima))
    dp.add_handler(CommandHandler("noob", noob))

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