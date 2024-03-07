# pip install python-telegram-bot

from telegram.ext import Updater, MessageHandler, Filters

# Função para lidar com novas mensagens
def welcome_message(update, context):
    # Obtém o ID do chat
    chat_id = update.message.chat_id
    # Envia a mensagem de boas-vindas
    context.bot.send_message(chat_id=chat_id, text="Olá! Bem-vindo ao nosso canal!")

def main():
    # Token do seu bot do Telegram
    token = 'SEU_TOKEN_AQUI'

    # Criação do updater e dispatcher
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # Registro do handler para lidar com mensagens de texto
    message_handler = MessageHandler(Filters.text & ~Filters.command, welcome_message)
    dispatcher.add_handler(message_handler)

    # Inicia o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
# Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot, que você obtém ao criar um novo bot com o BotFather no Telegram.