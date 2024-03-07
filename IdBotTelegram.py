# ...

# Função para lidar com o comando /verificar_id
def verify_id(update, context):
    # Obtém o ID do chat
    chat_id = update.message.chat_id
    # Envia o ID do chat como resposta ao comando
    context.bot.send_message(chat_id=chat_id, text=f"Seu ID é: {chat_id}")

def main():
    # ...

    # Registro do handler para o comando /verificar_id
    verify_id_handler = CommandHandler('verificar_id', verify_id)
    dispatcher.add_handler(verify_id_handler)

    # ... Lembre-se de substituir 'SEU_TOKEN_AQUI' pelo token do seu bot e ajustar conforme suas necessidades. Este é apenas um exemplo básico para ajudar a começar.
