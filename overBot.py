import os
import logging
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

secao = {"mes": 0, "dia": 0, "hora": 0, "minuto": 0}

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.send_message(update.message.chat_id,"""  *Olá, sou o Bot corno oficial deste grupo*.\n
Atualmente disponho dos seguintes comandos:\n
/ajuda   -> Exibe esta mensagem.\n
/proxima -> Lista a/as próximas sessoes marcadas\n
/marcar  -> Marca a próxima seção no seguinte formato: \"/marcar dia:mes:hora:minuto\"."
/noob    -> Exibe uma serie de mensagens de instruções para iniciantes.\n
Meu [repositório](https://github.com/VRavaglia/overbot)""", parse_mode= 'Markdown')

def parse_marcar(texto):
    global secao
    try:
        data = texto.split(' ')[1].split(':')
        print(data)
    except:
        return False

    if (len(data) != 4):
        return False
    try:
        secao['dia'] = int(data[0])
        secao['mes'] = int(data[1])
        secao['hora'] = int(data[2])
        secao['minuto'] = int(data[3])
    except:
        return False

    return True


def marcar(bot, update):  
    print(update.message.text)
    if (parse_marcar(update.message.text)):
        mensagem = "Próxima sessão marcada!"
    else:
        mensagem = "Não entendi a data, escreva no seguinte formato: \"/marcar dia:mes:hora:minuto\"."
    bot.send_message(update.message.chat_id,mensagem, parse_mode= 'Markdown')

def proxima(bot, update):
    mensagem = "Não há sessão marcada."
    if (secao["dia"] != 0):
        mensagem = "A próxima sessão será: "+ str(secao["dia"]).zfill(2) + "/" + str(secao["mes"]).zfill(2) + " às " + str(secao["hora"]).zfill(2) + ':' + str(secao["minuto"]).zfill(2) + '.'
    bot.send_message(update.message.chat_id,mensagem, parse_mode= 'Markdown')

def noob(bot, update):
    time = datetime.datetime.now().time().hour
    if (time < 6):
        bomdia = "boa noite!"
    elif (time < 12):
        bomdia = "bom dia!"
    elif (time < 18):
        bomdia = "boa tarde!"
    else:
        bomdia = "boa noite!"

    bot.send_message(update.message.chat_id,"  Primeiramente, " + bomdia + """\n\n
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
    updater = Updater(os.environ["TELEGRAM_TOKEN"])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ajuda", start))
    dp.add_handler(CommandHandler("proxima", proxima))
    dp.add_handler(CommandHandler("marcar", marcar))
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

